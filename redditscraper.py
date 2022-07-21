import os
from datetime import datetime
import pandas as pd
import praw
cwd = os.getcwd()

utctime = datetime.utcnow()

reddit = praw.Reddit(
    client_id="QivJl9MHxfjIp2jotV_NfA",
    client_secret="f7Ws5CpbmLRwKK3E_S8tITSI5QLF1g",
    user_agent="Important_Run1968",
)


class RedditScraper:
    def __init__(self, instanceid):
        print('start redditscrape')
        df = pd.DataFrame()
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()

        for submission in reddit.subreddit("AskReddit").hot(limit=10):
            print('finding post')
            df = pd.DataFrame(

                columns=['title', 'submission_id', 'score', 'url', 'selftext', 'upvote_ratio', 'num_comments', 'created_utc'],
                data={
                    "title": [submission.title],
                    'submission_id': [submission.id],
                    'score': [submission.score],
                    'url': [submission.url],
                    'selftext': [submission.selftext],
                    'upvote_ratio': [submission.upvote_ratio],
                    'num_comments': [submission.num_comments],
                    'created_utc': [submission.created_utc]

                })
            print('post data fetch')
            df1 = pd.concat([df1, df])
        print('comment start ')
        for index, row in df1.iterrows():
            submission = reddit.submission(row['submission_id'])
            submission.comment_limit = 5
            submission.comment_sort = 'top'
            for top_level_comment in submission.comments:
                print('comment find ')
                if isinstance(top_level_comment, praw.models.MoreComments):
                    continue
                df2 = pd.DataFrame(
                    columns=["title", 'comment_id', 'body', 'score', 'permalink', 'distinguished', 'submission_id'],
                    data={
                        "title": [submission.title],
                        'submission_id': [submission.id],
                        'comment_id': [top_level_comment.id],
                        "body": [top_level_comment.body],
                        'score': [top_level_comment.score],
                        'permalink': [top_level_comment.permalink],
                        'distinguished': [top_level_comment.distinguished],

                    })
                print('comment fetched ')
                df3 = pd.concat([df3, df2])
        print('done')
        df1.to_csv(path_or_buf=cwd + '/data/' + instanceid + '.csv')
        df3.to_csv(path_or_buf=cwd + '/data/' + instanceid + 'comments.csv')
