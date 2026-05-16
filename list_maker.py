import pandas as pd


def gk_spjeld(path):
    df = pd.read_excel(path)

    # Lag base_tag og suffix fra Tag
    df['Tag'] = df['Tag'].str.upper()
    df[['TFM', 'suffix']] = df['Tag'].str.rsplit('_', n=1, expand=True)

    # Pivot slik at suffix blir egne kolonner
    df_pivot = (
        df
        .pivot_table(
            index=['TFM'],
            columns='suffix',
            values='Value',
            aggfunc='first'
        )
        .reset_index()
    )
    df_pivot.columns.name = None
    
    return df_pivot


def change_format(df):
    df["FLW"] = df['FLW'].str.rsplit(',', n=1).str[0]
    df["TFM"] = df["TFM"].str.replace('B', '+', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', '=', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', '.', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', ':', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', '-', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', '.', n=1, regex=False)
    df["TFM"] = df["TFM"].str.replace('_', '/', n=1, regex=False)
    df["FLW"] = df["FLW"].fillna(0).astype(float)
    df["MAX"] = df["MAX"].fillna(0).astype(float)
    df["MIN"] = df["MIN"].fillna(0).astype(float)
    df["POS"] = df["POS"].fillna(0).astype(float)

    dict = df.to_dict()

    return dict

def test_spjeld(path):
    df = pd.read_excel(path)
    dict = df.to_dict()
    return dict


def calculator(er, skal):
    if er > skal:
        differanse = (skal / er) * 100
    else:
        differanse = (er / skal) * 100

    if differanse >= 90:
        return False
    else:
        return f"Er {round(er, 2)} m3/h skal ha {round(skal, 2)} m3/h"
    
        
def check_if_zero(er, skal):
    if skal == 0:
        return "Brann spjeld liste mangler verdi"
    elif er == 0:
        return "Ingen verdier i liste fra OneCo eller ikke programert"
    else:
        return False


    
# def check_vav(er, skal):

  
    
