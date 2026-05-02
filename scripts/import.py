#Loads Formula 1 dataset from CSV files into MySQL database
# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:mitssql%402006@localhost/f1proj")
# to remove errors due to '\N' and convert ti null
def clean_df(df):
    df.replace(r'\\N', pd.NA, inplace=True)
    return df

# Drivers
df = pd.read_csv("path/to/drivers.csv")
df = clean_df(df)
df.to_sql('drivers_staging', con=engine, if_exists='append', index=False)

# Constructors
df2 = pd.read_csv("path/to/constructors.csv")
df2 = clean_df(df2)
df2.drop(['constructorRef','url'], axis=1, inplace=True, errors='ignore')
df2['constructorId'] = pd.to_numeric(df2['constructorId'], errors='coerce')
df2.to_sql('constructors', con=engine, if_exists='append', index=False, method='multi')

#Circuits
df3 = pd.read_csv("path/to/circuits.csv")
df3 = clean_df(df3)
df3.drop(['url','lat','lng','alt'], axis=1, inplace=True, errors='ignore')
df3['circuitId'] = pd.to_numeric(df3['circuitId'], errors='coerce')
df3.to_sql('circuits', con=engine, if_exists='append', index=False, method='multi')

#races
df4 = pd.read_csv("path/to/races.csv")
df4 = clean_df(df4)
df4.drop([
    'url','fp2_date','fp1_date','time',
    'fp3_date','fp1_time','fp2_time','fp3_time',
    'quali_date','quali_time','sprint_date','sprint_time'
], axis=1, inplace=True, errors='ignore')
df4['raceId'] = pd.to_numeric(df4['raceId'], errors='coerce')
df4['year'] = pd.to_numeric(df4['year'], errors='coerce')
df4.to_sql('races', con=engine, if_exists='append', index=False, method='multi')

#results
df5 = pd.read_csv("path/to/results.csv")
df5 = clean_df(df5)
df5.drop(['rank','number','positionText'], axis=1, inplace=True, errors='ignore')
numeric_cols = [
    'resultId','raceId','driverId','constructorId',
    'grid','position','positionOrder','points',
    'laps','milliseconds','fastestLap','fastestLapSpeed','statusId'
]
for col in numeric_cols:
    if col in df5.columns:
        df5[col] = pd.to_numeric(df5[col], errors='coerce')
df5.to_sql('results', con=engine, if_exists='append', index=False, method='multi')

#lap times
df6 = pd.read_csv("path/to/lap_times.csv")
df6 = clean_df(df6)
numeric_cols = ['raceId','driverId','lap','position','milliseconds']
for col in numeric_cols:
    df6[col] = pd.to_numeric(df6[col], errors='coerce')
df6.to_sql('lap_times', con=engine, if_exists='append', index=False, method='multi')

#pit stops
df7 = pd.read_csv("path/to/pit_stops.csv")
df7 = clean_df(df7)
df7.drop('time', axis=1, inplace=True, errors='ignore')
numeric_cols = ['raceId','driverId','stop','lap','milliseconds']
for col in numeric_cols:
    df7[col] = pd.to_numeric(df7[col], errors='coerce')
df7['duration'] = pd.to_numeric(df7['duration'], errors='coerce')
df7.to_sql('pit_stops', con=engine, if_exists='append', index=False, method='multi')

#qualifying
df8 = pd.read_csv("path/to/qualifying.csv")
df8 = clean_df(df8)
df8.drop('number', axis=1, inplace=True, errors='ignore')

#converting string to numeric data
def time_to_ms(t):
    try:
        if pd.isna(t):
            return None
        mins, secs = str(t).split(':')
        return int(mins)*60000 + float(secs)*1000
    except:
        return None
df8['q1'] = df8['q1'].apply(time_to_ms)
df8['q2'] = df8['q2'].apply(time_to_ms)
df8['q3'] = df8['q3'].apply(time_to_ms)

numeric_cols = ['qualifyId','raceId','driverId','constructorId','position']
for col in numeric_cols:
    df8[col] = pd.to_numeric(df8[col], errors='coerce')

df8.to_sql('qualifying', con=engine, if_exists='append', index=False, method='multi')

print("All tables loaded successfully!")
