import pandas as pd
import os

def load_data(file_path):
    """Load raw data from the specified file path."""
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        return data
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def clean_data(data):
    """Clean the data by handling missing values and duplicates."""
    data = data.dropna()  # Remove missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    return data

def normalize_data(data):
    """Normalize the numerical features in the dataset."""
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()
    return data

def preprocess_data(file_path):
    """Load, clean, and normalize the data."""
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    normalized_data = normalize_data(cleaned_data)
    return normalized_data

def save_processed_data(data, output_path):
    """Save the processed data to the specified output path."""
    data.to_csv(output_path, index=False)