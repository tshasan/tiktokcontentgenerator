from datetime import datetime
import pandas as pd
import os
now = datetime.now()
timestamp = datetime.timestamp(now)
timestamp = datetime.utcfromtimestamp(timestamp)
cwd = os.getcwd()
from postmaker import PostMaker
from redditscraper import RedditScraper
from tts import Tts
from moviemaker import MovieMaker

#creating instanceid params included dateandpost pos based off from df col
for index in range(3):
    instanceid=str(timestamp)+' '+str(index)
    print(instanceid)
    RedditScraper(instanceid)
    df = pd.DataFrame()
    df1 = pd.DataFrame()
    df = pd.read_csv(cwd + '/data/' + instanceid + ".csv")
    df1 = pd.read_csv(cwd + '/data/' +instanceid+ "comments.csv")
    df1.sort_values(by="score",inplace=True, ascending=False)
    text = df1._get_value(int(index), 3, takeable = True)
    title = df1._get_value(int(index), 1, takeable = True)



    print(text)
    PostMaker(timestamp,text,title,instanceid)
    type = 'bodytext'
    Tts(timestamp,text,type,instanceid)
    type = 'titletext'
    Tts(timestamp,title,type,instanceid)
    MovieMaker(instanceid)

