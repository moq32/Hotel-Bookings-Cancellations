import pandas as pd
from sklearn.model_selection import train_test_split

def clean_data(df):
    """
    Cleans the hotel booking dataset based on Group 15's project logic.
    """
    # Handle missing values
    df['children'] = df['children'].fillna(0)
    df['country'] = df['country'].fillna('Unknown')
    df['agent'] = df['agent'].fillna(0)
    df['company'] = df['company'].fillna(0)
    
    # Filter out entries with 0 guests
    df = df[df['adults'] + df['children'] + df['babies'] > 0]
    
    return df

def split_data(df, target='is_canceled'):
    """
    Splits the data into training and testing sets.
    """
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

print("Preprocessing script initialized successfully.")
