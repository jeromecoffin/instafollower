import csv
import instaloader
from instaloader import Hashtag

# Create an instance of Instaloader
L = instaloader.Instaloader()
L.load_session_from_file("jerome.devops", "/Users/jeromecoffin/git_repo/instafollower/session-jerome.devops")

# Load the CSV file containing the hashtags
with open('/Users/jeromecoffin/git_repo/instafollower/data/sustainablehashtag.csv', newline='') as csvfile:
    hashtag_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    # Create a list to hold the hashtag data
    hashtag_data = []

    # Loop through each hashtag in the CSV file
    for row in hashtag_reader:
        hashtag = row[0]
        print(hashtag)

        # Use Instaloader to get the number of posts with this hashtag
        h = Hashtag.from_name(L.context, hashtag)
        count = h.mediacount

        # Add the hashtag and the number of posts to the hashtag data list
        hashtag_data.append([hashtag, count])

# Write the hashtag data back to the CSV file
with open('/Users/jeromecoffin/git_repo/instafollower/data/sustainablehashtag.csv', mode='w', newline='') as csvfile:
    hashtag_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Write the hashtag data to the CSV file
    for row in hashtag_data:
        hashtag_writer.writerow(row)
