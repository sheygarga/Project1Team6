# Project1Team6

This python project helps display how certain cities and counties in California felt about the significant wildfires such as the Thomas Fire, Rye Fire, Creek Fire, and Skirball Fire.

# Modules and Language

This project utilizes: Python3, Pandas, Numpy, MatPlotLib, Requests, JSON, Tweepy, Time, Seaborn, Unicodedata, Census, and US


# Methodology

By selecting a few cities in California, specifically based on proximity to the fire, we isolated the locations we wanted to analyze. We broke it down into 3 categories: Cities heavily affected by the fire when it is uncontained (Ojai, San Fernando), Cities that dealt with a fire that had been contained (Beverly Hills, La Crescenta), and Cities unaffected by the fire as a control group (Long Beach, Santa Barbara)

We used Tweepy to select the tweets from these locations and Vader for sentiment analysis on those tweets. 

We then utilized census data to gain demographic data for the cities, specifically poverty rate, unemployment rate, median house value, and other information to convey how well off each area is. 

Using MatPlotLib we displayed the correlated information on various plots. 