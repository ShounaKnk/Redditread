import csv
import praw

with open('cmmnts.csv', 'w') as file:
    fieldnames = ['author','title', 'comment 1', 'comment 2']
    writer = csv.DictWriter(file, fieldnames= fieldnames)
    writer.writeheader()
