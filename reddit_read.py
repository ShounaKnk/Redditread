import praw
import csv

username = "Greedy_House1185"
cid = "4uFvwHNEi4yfAITNi8yqRg"
sid = "1hOueoSRQZo5fjL20Mm663XKVKB8zQ"
pword = "Shnk#6703"

inst = praw.Reddit(
    client_id = cid,
    client_secret=sid,
    password = pword,
    username=username,
    user_agent = "test_bot"
)

def makeList(submission, comments, num_comments):
    submission_comments = []
    plist = {'author': 'u/'+ str(submission.author), 'title': submission.title}
    clist = {}
    for comment in comments[:num_comments]:
        if isinstance(comment, praw.models.MoreComments):
            continue
        submission_comments.append(comment.body)
        for i, c in enumerate(submission_comments):
            c = c.replace('\n', ' ')
            clist[f'comment {i+1}'] = c
    plist.update(clist)
    return plist
    
def get_posts(subreddit_name, num_posts=5, num_comments=2):
    subreddit = inst.subreddit(subreddit_name)
    top_comments = []
    for submission in subreddit.top(time_filter='day', limit=num_posts):
        comments = submission.comments
        top_comments.append(makeList(submission, comments, num_comments))
    return top_comments

if __name__ == "__main__":
    subreddit_name = "AskReddit"
    posts = get_posts(subreddit_name)
    fieldnames = ['author', 'title', 'comment 1', 'comment 2']
    with open('cmmnts.csv', 'a') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for post in posts:
            writer.writerow(post)