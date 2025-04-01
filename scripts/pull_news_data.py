import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Define the path to your kaggle.json file
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset identifier and the destination directory
dataset = 'oliviervha/crypto-news'
destination = os.path.expanduser('~/Desktop/MoodyCrypto/MoodyCrypto/data/raw')  
# Download the dataset
api.dataset_download_files(dataset, path=destination, unzip=True)

print(f"Dataset downloaded and extracted to {destination}")
