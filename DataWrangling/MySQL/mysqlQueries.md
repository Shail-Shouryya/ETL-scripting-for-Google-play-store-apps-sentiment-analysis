DROP TABLE IF EXISTS combined_apps_table;

CREATE TABLE combined_apps_table SELECT * FROM
(SELECT * FROM googleplaystore_first4000
UNION ALL
SELECT * FROM googleplaystore_second4001to8000
UNION ALL
SELECT * FROM googleplaystore_third8001to10842
) AS derived_tables;

SELECT * FROM google_play_store.combined_apps_table;


DROP TABLE IF EXISTS combined_reviews_table;

CREATE TABLE combined_reviews_table SELECT * FROM
(
SELECT * FROM google_play_store.googleplaystore_user_reviews05000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews10000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews15000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews20000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews25000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews30000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews35000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews40000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews45000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews50000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews55000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews60000
UNION ALL
SELECT * FROM google_play_store.googleplaystore_user_reviews64296
) AS derived_tables;

SELECT * FROM google_play_store.combined_reviews_table;

----------------------------------------------------------------------------------
SELECT * FROM combined_apps_table
INNER JOIN combined_reviews_table
ON combined_apps_table.App = combined_reviews_table.App
LIMIT 200000;
----------------------------------------------------------------------------------
16:20:06	CREATE TABLE merged_apps_and_reviews SELECT * FROM ( SELECT * FROM combined_apps_table CA INNER JOIN combined_reviews_table CR USING App )AS merged_table	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'App )AS merged_table' at line 6	0.000 sec


MySQL workbench timed out while doing query, needed to go to 
Edit -> Preferences -> SQL Editor -> DBMS connection read timeout interval (in seconds):
16:21:57	CREATE TABLE merged_apps_and_reviews SELECT * FROM ( SELECT * FROM combined_apps_table CA INNER JOIN combined_reviews_table CR USING (App) )AS merged_table	Error Code: 2013. Lost connection to MySQL server during query	30.000 sec

USE google_play_store;
-- DROP TABLE IF EXISTS merged_apps_and_reviews;

CREATE TABLE merged_apps_and_reviews
SELECT * FROM
(
SELECT * FROM combined_apps_table CA
INNER JOIN combined_reviews_table CR
USING (App)
)AS merged_table;

SELECT * FROM merged_apps_and_reviews ORDER BY App;

CREATE TABLE ordered_apps_and_reviews
SELECT * FROM merged_apps_and_reviews ORDER BY App;


CREATE TABLE test
SELECT * FROM ordered_apps_and_reviews;

SELECT * FROM test;
DELETE FROM test WHERE Sentiment_Polarity IS NULL;

SELECT * FROM test;

------------------------------------------------------------------------------------------------------------

CREATE TABLE distinct_apps
SELECT * FROM 
(
SELECT DISTINCT(App) FROM combined_apps_table
) AS unique_apps
ORDER BY App;

SELECT * FROM distinct_apps;

SELECT * FROM combined_reviews_table;


SELECT * FROM
(
SELECT * FROM combined_reviews_table WHERE Sentiment_Polarity IS NOT NULL
) AS no_null_reviews;

SELECT * FROM
(
SELECT * FROM 
(
SELECT DISTINCT App, Translated_Review, Sentiment, Sentiment_Polarity, Sentiment_Subjectivity
FROM combined_reviews_table
) AS no_null_reviews
WHERE no_null_reviews.Sentiment_Polarity IS NOT NULL
)
AS no_null_or_duplicate_reviews;