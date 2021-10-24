import app.interactors.ml as ml

lightfm_model = ml.LightFMModel()
lightfm_model.load_model('models/epoch_9.pickle')
lightfm_model.load_mappings(
    users_ids_path='/code/app/model/mappings/user_id2lightfm_id.csv',
    books_ids_path='/code/app/model/mappings/main_id2lightfm_id.csv')
