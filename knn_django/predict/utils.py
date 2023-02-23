import pickle

def load_model():
    # Charger le modèle KNN à partir du fichier pickle
    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model