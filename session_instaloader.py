import instaloader

L = instaloader.Instaloader()

# Login
L.context.log("Logging in...")
L.interactive_login("jerome.devops")

# Save session to file
L.context.log("Saving session to file...")
L.save_session_to_file("/Users/jeromecoffin/session-jerome.devops")

#topcet-goMfiq-datqo3
