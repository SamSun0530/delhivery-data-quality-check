import pandas as pd

df = pd.read_csv("../data/delhivery_data.csv")


print(f"There are {df.shape[0]} rows and {df.shape[1]} columns")
print(df.info())
print()

columns = df.columns
descriptions = [
    "data type",
    "time a trip created",
    "uuid of a route schedule",
    "route type",
    "uuid of trip",
    "source center",
    "source name",
    "destination center",
    "destination name",
    "od start time",
    "od end time",
    "start scan to end scan",
    "is there a cutoff",
    "factor of cutoff",
    "date and time of cutoff",
    "actual distance to destination",
    "actual time",
    "osrm time",
    "osrm distance",
    "factor",
    "actual time of segment",
    "osrm time of segment",
    "osrm distance of segment",
    "factor of segment"
]

for i in range(columns.size):
    print(f"{columns[i]}: {descriptions[i]}")
print()
print(df.isnull().sum())
print()
print(df.dtypes)
print()




print(df[df['osrm_time'] < 0])

print(df[df.duplicated()])

