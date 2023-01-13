import json
import logging
import dill
import pandas as pd

from pathlib import Path

path = Path.cwd()

def predict():
    with open(f'{path}/data/models/file_names', 'r') as file:
        model_filename = file.read()
    with open(model_filename, 'rb') as file:
        model = dill.load(file)
    logging.info(f'{model_filename} loading')
    test_files = [
        '7310993818.json',
        '7313922964.json',
        '7315173150.json',
        '7316152972.json',
        '7316509996.json'
    ]

    df_out = pd.DataFrame(columns=['id', 'predict_cat']) # Make an empty dataframe for save predicts

    def prediction(dict_):
        df = pd.DataFrame(dict_, index=[0])
        y = model.predict(df)
        return y

    for elem in test_files:
        with open(f'{path}/data/test/{elem}') as file:
            x = json.load(file)
            df_out.loc[len(df_out.index)] = [x['id'], prediction(x)[0]]
    df_out.to_csv(f'{path}/data/predictions/predict.csv', index=False)


if __name__ == '__main__':
    predict()
