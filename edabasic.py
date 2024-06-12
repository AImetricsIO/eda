# mi_libreria.py

def funcion1(param):
    return f'Función 1 dice: {param}'

def funcion2(param):
    return f'Función 2 dice: {param}'

def sumar(a, b):
    return a + b

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
