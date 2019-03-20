# Shail Shouryya
# python script to expedite ETL process with Pandas

import pandas as pd

class Raw_Methods:
    """These are the fundamental methods required to implement this program."""
    def __init__ (self, csv1, csv2):
        self.csv1 = csv1
        self.csv2 = csv2
        print (f"Initialized {self.csv1} as self.csv1 and {self.csv2} as self.csv2. \n")

    def import_csvs (self):
        left_df = pd.read_csv(self.csv1)
        print (f"The first CSV has {len(left_df)} rows of data after converting the CSV to a Pandas dataframe.")
        right_df = pd.read_csv(self.csv2)
        print (f"The second csv has {len(right_df)} rows of data after converting the CSV to a Pandas dataframe.")
        return (left_df, right_df)

    def drop_right_NaN (self):
        left_df, right_df = self.import_csvs()
        dropped_NaN_right_df = right_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        print (f'The seond dataframe has {len(dropped_NaN_right_df)} rows after dropping the "NaN" values.')
        return (left_df, dropped_NaN_right_df)

    def drop_right_duplicates_then_NaN (self):
        left_df, right_df = self.import_csvs()
        dropped_duplicates_right_df = right_df.drop_duplicates()
        dropped_duplicates_and_NaN_right_df = dropped_duplicates_right_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        print (f'The seond dataframe has {len(dropped_duplicates_and_NaN_right_df)} rows after dropping the "NaN" values.')
        return (left_df, dropped_duplicates_and_NaN_right_df)

    def drop_left_NaN (self):
        left_df, right_df = self.import_csvs()
        dropped_NaN_left_df = left_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        print (f'The first dataframe has {len(dropped_NaN_left_df)} rows after dropping the "NaN" values.')
        return (dropped_NaN_left_df, right_df)

    def drop_left_duplicates (self):
        left_df, right_df = self.import_csvs()
        dropped_NaN_left_df = left_df.drop_duplicates() #keep='first'
        print (f'The first dataframe has {len(dropped_NaN_left_df)} rows after dropping the duplicate values.')
        return (dropped_NaN_left_df, right_df)





    def merge_dfs_dropped_right_NaN (self):
        left_df, dropped_NaN_right_df = self.drop_right_NaN()
        merged_df = pd.merge(left_df, dropped_NaN_right_df, how='inner', on='App')
        print (f"The merged dataframe has {len(merged_df)} rows of data. \n")
        return (merged_df)

    def merge_dfs_dropped_left_NaN (self):
        dropped_NaN_left_df, right_df = self.drop_left_NaN()
        merged_df = pd.merge(dropped_NaN_left_df, right_df, how='inner', on='App')
        print (f"The merged dataframe has {len(merged_df)} rows of data. \n")
        return (merged_df)
    
    def merge_dfs_dropped_left_duplicates (self):
        dropped_duplicates_left_df, right_df = self.drop_left_duplicates()
        merged_df = pd.merge(dropped_duplicates_left_df, right_df, how='inner', on='App')
        print (f"The merged dataframe has {len(merged_df)} rows of data. \n")
        return (merged_df)

    def merge_dfs_dropped_left_duplicates_and_right_NaN (self):
        dropped_duplicates_left_df, _ = self.drop_left_duplicates()
        _, dropped_NaN_right_df = self.drop_right_NaN()
        merged_df = pd.merge(dropped_duplicates_left_df, dropped_NaN_right_df, how='inner', on='App')
        print (f"The merged dataframe has {len(merged_df)} rows of data. \n")
        return (merged_df)


    def merge_dfs_dropped_left_duplicates_and_right_duplicates_and_NaN (self):
        dropped_duplicates_left_df, _ = self.drop_left_duplicates()
        _, dropped_duplicates_and_NaN_right_df = self.drop_right_duplicates_then_NaN()
        merged_df = pd.merge(dropped_duplicates_left_df, dropped_duplicates_and_NaN_right_df, how='inner', on='App')
        print (f"The merged dataframe has {len(merged_df)} rows of data. \n")
        return (merged_df)

RM = Raw_Methods('googleplaystore.csv', 'googleplaystore_user_reviews.csv')
print ('This method drops the "NaN" values from the right dataframe.')
RM.merge_dfs_dropped_right_NaN()
print ('This method drops the "NaN" values from the left dataframe.')
RM.merge_dfs_dropped_left_NaN()
print ("This method drops the duplicate values from the left dataframe.")
RM.merge_dfs_dropped_left_duplicates()
print ('This method drops the duplicate values from the left dataframe and the "NaN" values from the right dataframe.')
RM.merge_dfs_dropped_left_duplicates_and_right_NaN()

RM.merge_dfs_dropped_left_duplicates_and_right_duplicates_and_NaN()

    