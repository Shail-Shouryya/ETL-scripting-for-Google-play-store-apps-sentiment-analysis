import runETL as ETL

RM = ETL.Raw_Methods('googleplaystore.csv', 'googleplaystore_user_reviews.csv')
pd.read_csv('googleplaystore.csv')