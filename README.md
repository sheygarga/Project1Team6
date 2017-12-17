## To use the functions:
1) copy shoujun-dev.py to your working dir.
2) add the following code before all your codes:
   ```
   import shoujun-dev as sj
   ```  
3) to call functions, use code as:
    ```
    sj.function_name(params)
    ```  
## Functions:
### sj.tweets_to_csv(*tweets*, [*filename*])  
   Extract the tweets info and write them to csv file in the working dir.  
   Function return is the count of tweets which are written to the csv file.

   Allowed inputs are:  
  *tweets*: An object returned by api.search()    
  *filename*: The output filename. If not provide, it will use 'tweets.csv' as default.  

  Example:  
    ```  
    sj.tweets_to_csv(test_tweets, 'test.csv')
    ```
