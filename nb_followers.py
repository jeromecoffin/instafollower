import instaloader
import schedule
import time
import datetime
from tinydb import TinyDB
from tinydb.operations import add
from tinyflux import TinyFluxDB
import csv


def get_num_followers(username):
    # create an instance of Instaloader class
    L = instaloader.Instaloader()

    # get profile instance
    profile = instaloader.Profile.from_username(L.context, username)

    # get the number of followers of the profile
    num_followers = profile.followers

    # print the number of followers
    print("Number of followers of", username, "is:", num_followers)

    # store the number of followers in the time series database
    current_time = datetime.datetime.now()
    db.insert({"time": current_time.isoformat(), "username": username, "followers": num_followers})

# create an empty list
usernames = []

# open the CSV file and read its contents into the list
with open('usernames.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        usernames.append(row[0])

# create a TinyFluxDB instance
fluxdb = TinyFluxDB("example_db")

# get the database instance
db = TinyDB(fluxdb.db_path)

# run the function for each username every 6 hours
for username in usernames:
    schedule.every(6).hours.do(get_num_followers, username)

while True:
    schedule.run_pending()
    time.sleep(1)
