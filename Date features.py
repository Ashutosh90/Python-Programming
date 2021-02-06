import pandas as pd

def create_date_featues(df):

    df['Year'] = pd.to_datetime(df['datetime']).dt.year

    df['Month'] = pd.to_datetime(df['datetime']).dt.month

    df['Day'] = pd.to_datetime(df['datetime']).dt.day

    df['Dayofweek'] = pd.to_datetime(df['datetime']).dt.dayofweek

    df['DayOfyear'] = pd.to_datetime(df['datetime']).dt.dayofyear

    df['Week'] = pd.to_datetime(df['datetime']).dt.week

    df['Quarter'] = pd.to_datetime(df['datetime']).dt.quarter 

    #df['Is_month_start'] = pd.to_datetime(df['datetime']).dt.is_month_start

    #df['Is_month_end'] = pd.to_datetime(df['datetime']).dt.is_month_end

    #df['Is_quarter_start'] = pd.to_datetime(df['datetime']).dt.is_quarter_start

    #df['Is_quarter_end'] = pd.to_datetime(df['datetime']).dt.is_quarter_end

    #df['Is_year_start'] = pd.to_datetime(df['datetime']).dt.is_year_start

    #df['Is_year_end'] = pd.to_datetime(df['datetime']).dt.is_year_end

    df['Semester'] = np.where(df['Quarter'].isin([1,2]),1,2)

    df['Is_weekend'] = np.where(df['Dayofweek'].isin([5,6]),1,0)

    df['Is_weekday'] = np.where(df['Dayofweek'].isin([0,1,2,3,4]),1,0)

    #df['Days_in_month'] = pd.to_datetime(df['datetime']).dt.days_in_month
    
    df['Hour'] = pd.to_datetime(df['datetime']).dt.hour

    return df
    
    
    
    
df=create_date_featues(df)