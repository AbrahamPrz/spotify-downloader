import re
import os

# function to validate Spotify URL
def validate_url(url):
    # regex pattern for Spotify URL
    pattern = r"^https:\/\/open.spotify.com\/(track|album|artist|playlist)\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$"
    # match pattern with input URL
    match = re.match(pattern, url)
    # if URL is valid, return True; otherwise, return False
    if match:
        return True
    else:
        return False

# check if SpotDL is installed
try:
    import spotdl
except ImportError:
    # if not installed, install SpotDL
    os.system("pip install spotdl")

# get Spotify URL from user input
url = input("Enter Spotify URL: ")

# validate URL
if validate_url(url):
    # use SpotDL to download track, album, artist, or playlist
    category = re.findall(r"^https:\/\/open.spotify.com\/(track|album|artist|playlist)\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$", url)[0][0]
    os.system(f"spotdl --output '{category}/' {url}")
    print(f"Download completed successfully. Saved in {category} folder.")
else:
    print("Invalid Spotify URL.")
