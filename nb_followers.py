import requests
from bs4 import BeautifulSoup
import schedule
import time
import datetime
from tinydb import TinyDB
from tinydb.operations import add
from tinyflux import TinyFlux
import csv
from tinyflux import Point

def get_num_followers(username):
    print(username)
    # get the profile page HTML
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # get the number of followers from the page HTML
    followers_text = soup.find("meta", property="og:description")["content"]
    num_followers = int(followers_text.split()[0].replace(",", ""))

    # print the number of followers
    print("Number of followers of", username, "is:", num_followers)

    # store the number of followers in the time series database
    current_time = datetime.datetime.now()

    from tinyflux import Point

    point = Point(
        time=current_time,
        measurement='followers',
        tags={'username': username},
        fields={'count': num_followers}
    )
    fluxdb.insert(point)

# create an empty list
usernames = []

# open the CSV file and read its contents into the list
with open('usernames.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        usernames.append(row[0])

# create a TinyFluxDB instance
fluxdb = TinyFlux("example_db")

for username in usernames:
    get_num_followers(username)

# run the function for each username every 6 hours
#for username in usernames:
#    schedule.every(6).hours.do(get_num_followers, username)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
