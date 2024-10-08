#!/usr/bin/python3
"""
this module contains function to fetche all post from
JSONPlaceholder.
"""
import json
import requests
import csv


def fetch_and_print_posts():
    """
    print all the posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    stat = r.status_code
    print("Status Code: {}".format(stat))

    if stat == 200:
        data_json = r.json()
        for post in data_json:
            print(post['title'])
    else:
        print("failed to load from requsest")


def fetch_and_save_posts():
    """
    save posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    stat = r.status_code
    data_json = r.json()
    list_data = []
    if stat == 200:
        for post in data_json:
            rows = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
        list_data.append(rows)
    with open('posts.csv', "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "body"])
        for post in data_json:
            writer.writerow([post['id'], post['title'], post['body']])
