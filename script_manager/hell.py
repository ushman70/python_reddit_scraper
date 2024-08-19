import praw
from praw.models import MoreComments
import csv
import time
import os




reddit = praw.Reddit(
    client_id="AFsSr6eIFwLdFyInAT6Eig",
    client_secret="4dH_trT9OSlcdBMs1MyKYIbR1_4ewA",
    password="",
    user_agent="Independent_Pickle34",
    username="",
)

url = input("Enter url")
csv_file_name = input("Name the CSV file. Make sure to add: .csv after naming the file. Ex: Craig.csv")
f = open(csv_file_name, "a")
submission = reddit.submission(url=url)
submission.comments.replace_more(limit=None)
with open(csv_file_name, 'r', newline='') as file:
     writer = csv.reader(file)
     
array = []
obj = {}
try:
    
  for top_level_comment in submission.comments[:]:
      array.append({"Comment":top_level_comment.body.encode(), "Likes": top_level_comment.score})
except:
  print('There is an issue')
  
finally:
  with open(csv_file_name, 'w', newline='') as file:
      writer = csv.writer(file)
      field = ["Comment", "Likes", "Length"]
      for x in array:
          writer.writerow([x.get("Comment"), x.get("Likes"), len(x.get("Comment"))])
     
          
          
print("Finish")
    
    
    

