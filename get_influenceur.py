import instaloader
import csv
import asyncio
from datetime import datetime, timedelta
import pytz
import sys

async def get_usernames(hashtag, location, start_date, end_date, existing_usernames, writer):
    L = instaloader.Instaloader(quiet=True)
    L.load_session_from_file("jerome.devops", "/Users/jeromecoffin/session-jerome.devops")

    for post in L.get_hashtag_posts(hashtag):
        post_date = post.date_local.astimezone(pytz.timezone('Europe/Paris'))
        if post.date_local >= start_date and post.date_local <= end_date and hasattr(post, 'location') and post.location is not None and location.lower() in post.location.name.lower():
            username = post.owner_username
            if not username in existing_usernames:
                print(location)
                print(username)
                existing_usernames.add(username)
                await writer.writerow([username])

async def main():
    hashtag = sys.argv[1]
    print(hashtag)
    locations = ["Paris", "France", "Paris, France"]
    end_date = datetime.now(pytz.timezone('Europe/Paris'))
    start_date = end_date - timedelta(days=7)
    existing_usernames = set()
    with open('influenceurs.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        existing_usernames = set([row[0] for row in reader])

    with open('influenceurs.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        tasks = []
        for location in locations:
            tasks.append(asyncio.ensure_future(get_usernames(hashtag, location, start_date, end_date, existing_usernames, writer)))

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())