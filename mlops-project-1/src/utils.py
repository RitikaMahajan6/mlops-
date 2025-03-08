def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def save_data(data, file_path):
    data.to_csv(file_path, index=False)

def log(message):
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info(message)