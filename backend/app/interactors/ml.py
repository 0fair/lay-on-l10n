import time
import random
import pandas as pd
import numpy as np
import pickle

from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score

pd.options.display.max_colwidth = 200
pd.options.display.max_columns = 200


class LightFMModel:
    def __init__(self):
        self.model = None
        self.model_path = None
        self.users_history = None
        self.books_history = None
        self.books_history_converted = None
        self.books_features = None
        self.books_labels = None
        self.interactions = None
        self.interaction_weights = None
        self.books_features_matrix = None

        self.user_id_map = None
        self.user_feature_map = None
        self.book_id_map = None
        self.book_feature_map = None

        self.CAT_COLUMNS = [
            'author_id', 'rubric_id', 'publicationType',
            'language_id', 'ageRestriction_id', 'NORM_bbk',
            'is_collection'
        ]
        self.NUM_COLUMNS = [
            'NORM_rounded_author_year_p',
            'NORM_rounded_year_p',
            'NORM_volume_p'
        ]

    def load_users_history(self, history_path, verbose=True):
        self.history_path = history_path
        self.users_history = pd.read_csv(history_path, sep=',')
        self.users_v = self.users_history.readerID.unique()
        if verbose:
            print(f'Total interactions: {self.users_history.shape}')
            print(f'Total users: {self.users_v.shape}')

    @staticmethod
    def to_lightfm_fea(fea, prefix):
        if type(fea) == int:
            return f'{prefix}:{fea}'
        if type(fea) == float:
            return f'{prefix}:{int(fea)}'
        else:
            return f'{prefix}:{fea}'

    def agg_fea_row(self, row, features):
        res = {}
        for f in features:
            if f in self.CAT_COLUMNS:
                res[row[f]] = 1
            if f in self.NUM_COLUMNS:
                res[f] = row[f]
        return (row['main_id'], res)

    def calc_books_features(self, books, target_features):
        tmp_df = books[target_features + ['main_id']].copy()
        tmp_df['features'] = tmp_df.apply(
            lambda row: self.agg_fea_row(row, target_features), axis=1)
        features = tmp_df.features.values
        labels = []
        for c in target_features:
            if c in self.CAT_COLUMNS:
                for value in books[c].unique():
                    labels.append(value)
            if c in self.NUM_COLUMNS:
                labels.append(c)
        return (features, labels)

    def load_books(self, books_path, verbose=True):
        self.books_path = books_path
        self.books_history = pd.read_csv(books_path, sep=',')
        self.books_v = self.books_history.main_id.unique()

        column2name = {}
        for i, c in enumerate(self.books_history.columns):
            column2name[c] = f'f{i}'
            if verbose:
                print(f'Book feature: {c}: {column2name[c]}')
        if verbose:
            print(f'Total books: {self.books_v.shape}')

        self.books_history_converted = self.books_history.copy()
        for c in self.CAT_COLUMNS:
            self.books_history_converted[c] = self.books_history_converted[c].apply(
                lambda x: self.to_lightfm_fea(x, column2name[c]))

        self.books_features, self.books_labels = self.calc_books_features(
            self.books_history_converted,
            self.NUM_COLUMNS + self.CAT_COLUMNS
        )

    def build_dataset(self):
        self.dataset = Dataset()
        self.dataset.fit(self.users_v, self.books_v, item_features=self.books_labels)
        user_interactions = [(x[0], x[1]) for x in self.users_history.values]
        self.interactions, self.interaction_weights = self.dataset.build_interactions(user_interactions)
        self.books_features_matrix = self.dataset.build_item_features(
            self.books_features, normalize=False)
        m1, m2, m3, m4 = self.dataset.mapping()
        self.user_id_map, self.user_feature_map, self.book_id_map, self.book_feature_map = m1, m2, m3, m4

    def train(self, epochs=10, n_threads=4, random_seed=123,
              test_share=0.2, lr=0.05, loss='warp', save_epochs=False):
        train_mapks = []
        test_mapks = []
        train_aucs = []
        test_aucs = []

        (train, test) = random_train_test_split(self.interactions,
                                                test_percentage=test_share,
                                                random_state=random_seed)

        self.model = LightFM(learning_rate=lr, loss=loss)
        for epoch in range(epochs):
            print(f'EPOCH {epoch} ---------')
            start_time = time.time()
            if save_epochs:
                pickle.dump(self.model, open(f'epoch_{epoch}.pickle', 'wb'))
            self.model.fit_partial(train, item_features=self.books_features_matrix,
                                   epochs=1, num_threads=n_threads)

            train_mAPk = precision_at_k(self.model, train,
                                        item_features=self.books_features_matrix,
                                        k=5, num_threads=n_threads).mean()
            test_mAPk = precision_at_k(self.model, test,
                                       item_features=self.books_features_matrix,
                                       k=5, num_threads=n_threads).mean()

            train_auc = auc_score(self.model, train, item_features=self.books_features_matrix,
                                  num_threads=n_threads).mean()
            test_auc = auc_score(self.model, test, item_features=self.books_features_matrix,
                                 num_threads=n_threads).mean()
            train_mapks.append(train_mAPk)
            test_mapks.append(test_mAPk)
            train_aucs.append(train_auc)
            test_aucs.append(test_auc)

            end_time = time.time()

            print(f'\tmAPk: train {np.round(train_mAPk, 3)}, test {np.round(test_mAPk, 3)}')
            print(f'\tAUC train: {train_auc}, test {test_auc}')
            print(f'\tTime spent: {(end_time - start_time) / 60} minutes')
            print(f'{epoch} Mean train mAPk: {np.mean(train_mapks)}')
            print(f'{epoch} Mean test mAPk: {np.mean(test_mapks)}')
            print(f'{epoch} Mean train auc: {np.mean(train_aucs)}')
            print(f'{epoch} Mean test auc: {np.mean(test_aucs)}')

    def fit_partitial(self, users, books, books_features):
        # To be done
        pass

    def save_model(self, model_path):
        pickle.dump(self.model, open(model_path, 'wb'))

    def save_mappings(self,
                      users_ids_path='user_id2lightfm_id.csv',
                      books_ids_path='main_id2lightfm_id.csv'):
        df = pd.DataFrame.from_dict(self.user_id_map, orient='index', columns=None).reset_index()
        df.columns = ['user_id', 'lightfm_id']
        df.to_csv(users_ids_path, columns=None, header=True, index=False, sep=',')

        df = pd.DataFrame.from_dict(self.book_id_map, orient='index', columns=None).reset_index()
        df.columns = ['main_id', 'lightfm_id']
        df.to_csv(books_ids_path, columns=None, header=True, index=False, sep=',')
        # self.user_feature_map and self.book_feature_map to be done

    def load_model(self, model_path):
        self.model_path = model_path
        self.model = pickle.load(open(model_path, 'rb'))

    def load_mappings(self,
                      users_ids_path='user_id2lightfm_id.csv',
                      books_ids_path='main_id2lightfm_id.csv',
                      id2main_id_path='id2main_id.csv'):
        self.users_ids_path = users_ids_path
        self.books_ids_path = books_ids_path
        self.user_id_map_df = pd.read_csv(users_ids_path)
        self.book_id_map_df = pd.read_csv(books_ids_path)
        self.user_id_map = self.user_id_map_df.set_index('user_id').lightfm_id.to_dict()
        self.book_id_map = self.book_id_map_df.set_index('main_id').lightfm_id.to_dict()
        # self.user_feature_map and self.book_feature_map to be done

        self.id2main_id_df = pd.read_csv(id2main_id_path)
        serial_ids_1 = self.id2main_id_df[self.id2main_id_df.is_collection == 1].main_id.unique()
        serial_ids_2 = self.id2main_id_df[self.id2main_id_df.parentId != 0].parentId.unique()
        serial_ids = set(serial_ids_1).union(set(serial_ids_2))
        self.book_id_map_df['is_serial'] = self.book_id_map_df.main_id.isin(serial_ids)

    def predict(self, user_id, books_n=None, top_n=1000):
        if not books_n:
            books_n = len(self.book_id_map)
        lightfm_user_id = self.user_id_map.get(user_id, -1)
        if lightfm_user_id == -1:
            return np.array([])
        weights = self.model.predict(lightfm_user_id, np.arange(books_n))
        books = self.book_id_map_df.main_id.values
        serial = self.book_id_map_df.is_serial.values
        weights = weights[~serial]
        books = books[~serial]
        predictions = books[weights.argsort()][::-1][:top_n]
        weights[::-1].sort()
        return (predictions, weights[:top_n])

    def predict_n(self, users):
        n_ratings = len(self.book_id_map)
        user2recommendations = {}
        for user_id in users:
            recommendations, weights = self.predict(user_id, books_n=n_ratings)
            if not len(recommendations):
                print(f'User {user_id} not found')
                user2recommendations[user_id] = ()
            user2recommendations[user_id] = (recommendations, weights)
            print(f'Processed: {user_id}')
        return user2recommendations
