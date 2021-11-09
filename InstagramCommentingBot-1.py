from instapy import InstaPy
from instapy_cli import client
import time
import random
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("C:\\Users\stavr\PycharmProjects\Epiphany") if isfile(join("C:\\Users\stavr\PycharmProjects\Epiphany", f))]
filesofphotos = []

for i in range(len(files)):
    if '.jpg' in files[i]:
        filesofphotos.append(files[i])
    if '.png' in files[i]:
        filesofphotos.append(files[i])

start_time = int(time.time())
username = "username"
password = "password"
session = InstaPy(username=username, password=password,geckodriver_path='your path to the geckodriver',show_logs=True)
comments = ['comments']
commentchance = random.choice([70,64,73,62,60,84,85,96,79,99,65,86])

session.login()
session.set_relationship_bounds(min_followers=30,max_followers=10000,min_posts=5,min_following=0)
session.set_quota_supervisor(peak_comments_daily=500,peak_likes_daily=500,peak_comments_hourly= 10,peak_likes_hourly=10)
session.set_do_comment(enabled=True,comment_liked_photo=True,percentage=commentchance)
session.set_comments(comments)
times = [25,42,59,60,72,59,131,28,71,46,20,153,172,147,145,164,137,128,134]
session.set_action_delays(enabled=True,comment=10,like=10)


hashtags = ['hashtags']
randomaction = random.choice([0,1,2,3])
if randomaction == 0:
    session.like_by_tags([hashtags])
    session.do_comment()
else:
    session.like_by_tags([hashtags], amount=50)
    session.do_comment()




time.sleep(random.choice(times))


session.end()
