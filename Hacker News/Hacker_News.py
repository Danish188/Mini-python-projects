import datetime as dt
import csv
# open and read file
file = open('HN_posts_year_to_Sep_26_2016.csv' , encoding="UTF-8")
read_file = list(csv.reader(file))
data = read_file[1:]

ask_post =[]
show_post = []
other_post = []
# seperate data according to ask hn and show hn
for line in data:
    title = line[1]
    if title.lower().startswith("ask hn"):
        ask_post.append(line)
    elif title.lower().startswith("show hn"):
        show_post.append(line)
    else:
        other_post.append(line)
# count total comments that are asked
total_ask_comments = 0
for i in ask_post:
    total_ask_comments += int(i[4])
avg_ask = total_ask_comments/len(ask_post)
# total show comments
total_show_comments = 0
for i in show_post:
    total_show_comments += int(i[4])
avg_show = total_show_comments/len(show_post)

result = []
# get the date and comments count from data
for i in ask_post:
    result.append([i[6] , int(i[4])])
# count comments by hours 
comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"
for i in result:
    date = i[0]
    comment = i[1]
    date = dt.datetime.strptime(date , date_format).strftime("%H")
    if date in counts_by_hour:
        comments_by_hour[date] += comment
        counts_by_hour[date] += 1
    else:
        comments_by_hour[date] = comment
        counts_by_hour[date] = 1

avg_hours = []
# get average of commnets in each hour
for h in comments_by_hour:
    avg_hours.append([h , comments_by_hour[h]/counts_by_hour[h]])
# swap the values in list
swapped = []
for hour , avg in avg_hours:
    swapped.append([avg , hour])
# show output
for avg, hour in sorted(swapped, reverse=True)[:5]:
    print("{}: {:.2f} average comments per hour".format(dt.datetime.strptime(hour , "%H").strftime("%H:%M") , avg))