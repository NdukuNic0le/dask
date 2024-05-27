import dask.dataframe as dd

df = dd.read_csv("./twitter_training.csv")

print(df.head())

df = df.repartition(npartitions=20)
print(f"{df.npartitions}")

df.to_parquet("./twitter_training.parquet")
