import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Load messages and categories csv files from the file path given,
    and merge them into a dataframe.
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.join(categories.set_index('id'), on='id')
    return df


def clean_data(df):
    '''
    Process data for analysis and modeling.
    '''
    # split categories into separate category columns
    categories = df['categories'].str.split(';', expand=True)
    row = categories.loc[0]
    category_colnames = row.apply(lambda col: col[:-2]).values
    categories.columns = category_colnames
    
    # convert category values to just numbers 0 or 1
    for column in categories:
        categories[column] = categories[column].astype(str).str[-1].astype(int)
    
    # replace categories column in df with new category columns
    df.drop(columns='categories', inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    # remove duplicates & index with erroenous data(Related column can't have other values than 0 or 1)
    df.drop_duplicates(inplace=True)
    df.drop(df[df['related']==2].index ,inplace=True)
    return df    
    
    
def save_data(df, database_filepath):
    '''
    Save the clean dataset into an sqlite database.
    '''
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df.to_sql('message_with_category', engine, if_exists='replace', index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
