import app.interactors.ml as ml

lightfm_model = ml.LightFMModel()
lightfm_model.load_users_history('/var/datasets/utf8/train_users.csv')
lightfm_model.load_books('/var/datasets/utf8/train_books.csv')
lightfm_model.build_dataset()
lightfm_model.train()
lightfm_model.save_model('/code/app/models/model.pickle')
lightfm_model.save_mappings(
    users_ids_path='/code/app/model/mappings/user_id2lightfm_id.csv',
    books_ids_path='/code/app/model/mappings/main_id2lightfm_id.csv')
