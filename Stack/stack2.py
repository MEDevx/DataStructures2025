browsing_history = [] # A stack representing my browsing history

browsing_history.append("facebook.com") # Accessing a new website adds it to the browsing history
browsing_history.append("youtube.com")
browsing_history.append("reddit.com")
browsing_history.append("tiktok.com")

print(f"\nThis is my browsing history from least to most recent access websites: \n{browsing_history}")
most_recent_website = browsing_history[-1] # The website that is currently open
print (f"I am currently on {most_recent_website}.")

browsing_history.pop() # Go back to the previously accessed website
most_recent_website = browsing_history[-1]
print (f"\nAfter pressing the back button, I got redirected to {most_recent_website}.")

browsing_history.clear() # Clear the browsing history
website_left = len(browsing_history)
print (f"\nAfter closing all tabs and clearing my browsing history, there are {website_left} websites left in my history.\n")

