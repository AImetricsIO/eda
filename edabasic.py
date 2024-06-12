# To be used in google collab notebooks

# Intraday data shows NaN in the last volume row. We'll change it with an average
def fill_na_with_previous_mean(df, window=78):
    for i in range(len(df)):
        if pd.isna(df.loc[i, 'volume']):
           start = max(0, i - window)
           subset = df.loc[start:i, 'volume']
           mean_value = subset.mean() if not subset.empty else 0
           df.loc[i, 'volume'] = mean_value
    return df

# Daily prices are adjusted with splits and other corporte events
def adjust_close(df):
    # Calculate the adjusted_close ratio
    df['ratio'] = df['close'] / df['adjusted_close']
    
    df['open'] = df['open'] / df['ratio']
    df['high'] = df['high'] / df['ratio']
    df['low'] = df['low'] / df['ratio']
    df['close'] = df['close'] / df['ratio']
    df['volume'] = df['volume'] * df['ratio']
    
    # Drop the ratio column if it's no longer needed
    df.drop(columns=['ratio'], inplace=True)
    df.drop(columns=['adjusted_close'], inplace=True)

    return df
