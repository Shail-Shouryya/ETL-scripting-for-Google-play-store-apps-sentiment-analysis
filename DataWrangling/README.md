## Decomposing the Goal
Is there a correlation between the ratings an app receives on the Google Play Store with the genre the app is categorized as and the number of downloads and reviews it receives?
    
## Identify Data Sources
Used web scraped data of 10,000 Play Store apps for analysing the Android market from [Kaggle](https://www.kaggle.com/lava18/google-play-store-apps)
    
## Define Strategy and Metrics
Use Pandas to create Pandas dataframes for the app information and app reviews, remove irrelevant data from the reviews dataframe, merge the app information and reviews dataframes, then insert the merged dataframe into a SQL database and use sqlAlchemy to connect to a PostgreSQL database with Flask to render an HTML template visualizing the dashboard of the Google Play Store apps with information about the app.
    
## Build Data Retrieval Plan
Use the Kaggle source and clean the data using Pandas.
    
## Retrieve the Data
Use the scraped dataset formatted as CSVs from Kaggle.

## Assemble and Clean
Drop the NaN and duplicate reviews values and merge the app and review dataframes.

## Dealing with Challenges
Pandas did not join the dataframes properly after dropping the incomplete and duplicate review values, so the ETL process was much more involved. First approach was to convert the raw Google Play data into readable SQL using [SQLizer](https://sqlizer.io/#/), then working with the data directly in MySQL. Doing the same things in MySQL as with Pandas - dropping the duplicate and null reviews data and then merging with the app information - surprisingly yielded slightly different results. Then, merging the two datasets without dropping any values yielded 144k rows of data, which was a clear indication something was wrong.\
\
Finally resorted to using nested subqueries in MySQL to drop not only the duplicate and null reviews data, but also the app information data - apparently the scraped data had the same app information multiple times...

## Analyze for Trends
    Group data by app, genre, ...... and observe trends

## Acknowledge Limitations
    Used the default column value for sentiment analysis since didn't get own ML model figured out yet

## Make the Call or Tell the Story
    
