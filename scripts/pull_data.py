import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Define the path to your kaggle.json file
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the dataset identifier and the destination directory
news_dataset = 'oliviervha/crypto-news'
price_dataset = 'kapturovalexander/bitcoin-and-ethereum-prices-from-start-to-2023'

destination = os.path.expanduser('~/Desktop/MoodyCrypto/MoodyCrypto/data/raw')  
api.dataset_download_files(news_dataset, path=destination, unzip=True)
api.dataset_download_files(price_dataset, path=destination, unzip=True)

print(f"Dataset downloaded and extracted to {destination}")

