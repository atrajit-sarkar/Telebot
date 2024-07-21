from instascrape import Reel
import os

dir=os.getcwd()
# Replace 'instagram_link' with the actual link to the Instagram reel or video
instagram_link=input("Enter Instagram Link: ")
insta_reel = Reel(instagram_link)

# Scrape the reel's data
insta_reel.scrape()

# Download the reel to the specified path
insta_reel.download(f'{dir}/video.mp4')
