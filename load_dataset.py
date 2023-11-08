from pyspark.sql import SparkSession, dataframe

spark = SparkSession.builder.getOrCreate()

datasets = {
    "flight_data": "./data/flight-data/json/*-summary.json",
    "retail_data": "./data/retail-data/by-day/*.csv",
    "bike_stations": "./data/bike-data/201508_station_data.csv",
    "bike_trips": "./data/bike-data/201508_trip_data.csv",
}

def load_dataset(key: str) -> dataframe.DataFrame:
    path = datasets[key]
    if path.endswith("csv"):
        return spark.read.option("inferSchema", "true").option("header", "true").csv(path)
    elif path.endswith("json"):
        return spark.read.format("json").load(path)
    else:
        raise ValueError(f"Do not understand path '{path}'")