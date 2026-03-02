import pandas as pd
df = df.read_csv("athlete_events.csv")
region_df = df.read_csv("noc_regions.csv")

def preprocessor(df):
    global df, region_df
    df = df[df["Season"] == "Summer"]
    df = df.merge(region_df, how="left", on="NOC")
    df.drop_duplicates(inplace=True)
    df = df.concate([df, pd.get_dummies(df["Medal"])] , axis = 1)

    return df