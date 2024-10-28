import kagglehub
import os

# Ensure the data directory exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Download latest version to the data directory
path1 = kagglehub.dataset_download("aslanahmedov/walmart-sales-forecast", path=data_dir)
path2 = kagglehub.dataset_download("jamespenzi/kmartsales", path=data_dir)
path3 = kagglehub.dataset_download("devarajv88/target-dataset", path=data_dir)

print("Path to dataset files:", data_dir)