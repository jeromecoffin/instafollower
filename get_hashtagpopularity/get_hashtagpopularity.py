import csv
import requests
from bs4 import BeautifulSoup

# Open the CSV file and read the hashtags
with open('/Users/jeromecoffin/git_repo/instafollower/data/sustainablehashtag.csv', 'r') as f:
    reader = csv.reader(f)
    hashtags = [row[0] for row in reader]

# Open a new CSV file to write the results
with open('/Users/jeromecoffin/git_repo/instafollower/data/hashtags_with_counts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for hashtag in hashtags:
        url = f"https://www.instagram.com/explore/tags/{hashtag}/"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        meta = soup.find("meta", attrs={"name": "description"})

        if meta:
            description = meta.attrs["content"]
            parts = description.split(" ")
            posts = parts[0].replace(",", "")
            print(f"The hashtag '{hashtag}' has {posts} posts on Instagram.")
            writer.writerow([hashtag] + [posts])  # write the result to the new column
        else:
            print(f"Could not find data for the hashtag '{hashtag}'.")
            writer.writerow([hashtag] + ['Not Found'])  # write "Not Found" to the new column
