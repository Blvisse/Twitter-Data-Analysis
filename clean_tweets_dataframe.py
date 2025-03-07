class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    import pandas as pd 

    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df.drop_duplicates()
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        

        df['created_at']=pd.to_datetime(df['created_at'],format='%Y%m%d')
        
        
        
        df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """

        

        df['polarity'] = pd.to_numeric(df['polarity'])
        df['subjectivity']=pd.to_numeric(df['subjectivity'])
        df['retweet_count']=pd.to_numeric(['retweet_count'])
        df['favorite_count']=pd.to_numeric(['favorite_count'])
        df['followers_count']=pd.to_numeric(['followers_count'])
        df['friends_count']=pd.to_numeric(['friends_count'])
        
        
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """

        import ntlk 
        words=set(ntlk.corpus.words.words())        
        df = df['lang'].join(r for r in ntlk.wordpunct_tokenize(df['lang']) if r.lower() in words or not r.isalpha())
        
        return df