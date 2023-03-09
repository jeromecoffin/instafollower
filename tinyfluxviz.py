import matplotlib.pyplot as plt
from tinydb import TinyDB
from tinyflux import TinyFluxDB

# create a TinyFluxDB instance
fluxdb = TinyFluxDB("example_db")

# get the database instance
db = TinyDB(fluxdb.db_path)

# retrieve the data from the database
data = db.all()

# extract the time, username, and followers data into separate lists
times = [entry["time"] for entry in data]
usernames = [entry["username"] for entry in data]
followers = [entry["followers"] for entry in data]

# create a line chart
plt.plot(times, followers)

# set the chart title and axis labels
plt.title("Number of Followers Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Followers")

# display the chart
plt.show()
