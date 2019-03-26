• Decomposing the Goal:
    Is there a correlation between the ratings an app receives on the Google Play Store with the genre the app is categorized as and the number of downloads and reviews it receives?
    
• Identify Data Sources
    Used web scraped data of 10,000 Play Store apps for analysing the Android market from [Kaggle](https://www.kaggle.com/lava18/google-play-store-apps)
    
• Define Strategy and Metrics
    Use pandas to create dataframes for the app information and app reviews, remove irrelevant or incomplete data, merge the dataframes, then insert merged dataframe into a SQL database, then use sqlalchemy to connect to the database and use Flask to render an html template that visualizes a dashboard of the Google Play Store apps with information about the app.
    
• Build Data Retrieval Plan
    Use the kaggle source
    
• Retrieve the Data
    Use the scraped dataset from kaggle

• Assemble and Clean
    Drop NaN values and merge dataframes

• Analyze for Trends
    Group data by app, genre, ...... and observe trends

• Acknowledge Limitations
    Used the default column value for sentiment analysis since didn't get own ML model figured out yet

• Make the Call or Tell the Story
    