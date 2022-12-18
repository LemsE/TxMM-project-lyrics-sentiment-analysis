import numpy as np
import pandas as pd


def drop_unnecessary(df_before):
    df_after = df_before.drop(['dating', 'violence', 'world/life', 'night/time', 'shake the audience', 'family/gospel', 'romantic',
                  'communication', 'obscene', 'music', 'movement/places', 'light/visual perceptions',
                  'family/spiritual', 'like/girls', 'sadness', 'feelings', 'danceability', 'loudness', 'acousticness',
                  'instrumentalness', 'valence', 'energy', 'genre', 'len', 'topic', 'age'], axis='columns')
    return df_after


def get_mask_year_df(interval, df):
    df_t = df.loc[df['year_interval'] == interval]
    array = np.random.randint(0, df_t.shape[0], 10)
    index_arr = df_t.iloc[array, :].index.values
    mask = pd.DataFrame(df.loc[index_arr, :])
    return mask


def fill_df_val(df_old):
    df_validation = pd.DataFrame()
    intervals = ['1950-1960', '1960-1970', '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010-2019']
    for i in intervals:
        mask = get_mask_year_df(i, df_old)
        df_validation = pd.concat([df_validation, mask])
    return df_validation

# Load dataset
df = pd.read_csv(r'tcc_ceds_music.csv')
# Drop unnecessary columns
df = drop_unnecessary(df)
# add year interval columns
df['year_interval'] = pd.cut(df['release_date'], bins=[1950, 1960, 1970, 1980,1990,2000,2010,2019],
                             include_lowest=True,
                             labels=['1950-1960', '1960-1970', '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010-2019'])
# create validation test set
df_val = fill_df_val(df)

df_val = df_val.drop(['Unnamed: 0', 'release_date'], axis='columns')
for col in df_val.columns:
    print(col)

df_val.to_csv('validation_set.csv')
