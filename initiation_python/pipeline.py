from kfp import dsl

@dsl.component
def preprocess():
    print("Nettoyage des données")

@dsl.component
def train():
    print("Entraînement du modèle")

@dsl.pipeline
def mon_pipeline():
    p = preprocess()
    t = train().after(p)