# /// script
# dependencies = [
#   "requests<3",
#   "rich",
#   "datetime",
# ] 
# requires-python = ">=3.11"
# ///

import requests
import json
from datetime import datetime


start_date=datetime.strptime("2025-01-01T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
end_date=datetime.strptime("2025-04-15T23:59:59.999Z", "%Y-%m-%dT%H:%M:%S.%fZ")


# Open cookie file
with open("./cookie.txt", "r") as f:
    content = f.read()
headers = {
    'Cookie': content
}

print(content)
#send request to discourse API
response = requests.get(f'https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json?page=8',headers=headers)

#Complete set of topics
topics = response.json()['topic_list']['topics']


filtered_topics = [
    topic for topic in topics
    if start_date <= datetime.strptime(topic['last_posted_at'], "%Y-%m-%dT%H:%M:%S.%fZ") <= end_date
]

# filter posts based on dates
def filtered_posts(post):
    if start_date <= datetime.strptime(post['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ") <= end_date:
        return True
    return False

# Format the topics with required and important fields
def format_topic(topics):
    format_topics = [{key: topic[key] for key in['id', 'title', 'slug', 'posts_count', 'reply_count', 'created_at', 'last_posted_at', 'closed']} 
    for topic in topics]
    return  format_topics



def read_posts(topics):
    for topic in topics:
        print("Topic ID:", topic['id'])
        response = requests.get(f'https://discourse.onlinedegree.iitm.ac.in/t/{topic["id"]}.json', headers=headers)
        topic_posts = response.json()['post_stream']['posts']
        posts = []
        for post in topic_posts:
            print("Before Filter Post Date", post['created_at'])
            if filtered_posts(post):
                print("After Post Date", post['created_at'])
                post_data = {
                    'id': post['id'],
                    'username': post['username'],
                    'name': post['name'],
                    'post_url': post['post_url'],
                    'created_at': post['created_at'],
                    'cooked': post['cooked'],
                    'topic_id': topic['id'],
                    'topic_title': topic['title']
                    }
                posts.append(post_data)
                with open(f'./markdowns/discourse/discourse_{topic["id"]}.json', 'a') as file:
                    json.dump(posts, file, indent=4)
    

#all topics
formatted_topics = format_topic(topics)
read_posts(formatted_topics)




'''with open('discourse_complete.json', 'w') as file:
    json.dump(read_posts(topics), file, indent=4)'''




