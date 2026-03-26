from src.data_ingestion import CSVBatteryLoader

loader = CSVBatteryLoader("data/raw", max_files=150)

df = loader.load()

print(df.shape)
print(df.head())