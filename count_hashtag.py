from instaloader import Hashtag
import instaloader
import sys

L = instaloader.Instaloader(quiet=True)
L.load_session_from_file("jerome.devops", "/Users/jeromecoffin/session-jerome.devops")
h = Hashtag.from_name(L.context, sys.argv[1])
print(h.mediacount)
