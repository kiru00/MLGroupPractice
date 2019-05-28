__author__ = "Shubham Kumar"

# TimeSeries Basics
import pandas as pd
print("Pandas Version:  "+ pd.__version__)

# Basic TimeSeries
dt_rng = pd.date_range(start='1-2-2017',end='1-3-2019')
df = pd.DataFrame({
    "Date" : dt_rng,
    "Day" : dt_rng.day,
    "Weekday" : dt_rng.weekday,
    "Weekday_Name" : dt_rng.weekday_name,
    "Month": dt_rng.month,
    "Year": dt_rng.year,
})
print(df.head(3))

df['Month_Start'] = df['Date'].dt.is_month_start
df['Month_End'] = df['Date'].dt.is_month_end
df['Quarter_Start'] = df['Date'].dt.is_quarter_start
df['Quarter_End'] = df['Date'].dt.is_quarter_end
print(df.head(3))

# Finding Weekends and Weekdays in the given TimeSeries
df['Weekends'] = df['Weekday_Name'].map(lambda x: True if(x=='Sunday' or x=='Saturday') else False)
print('Counting Weekends[True] and Weekdays[False]')
print(df['Weekends'].value_counts())
print('No. of Weekends: ' ,len(df[df['Weekends'] == True]))

print('DataFrame dimension', df.shape)
print(df.dtypes)
print(df.describe())
print('DataFrame Size on Ram(in Bytes)', df.size)
print(df.info())

