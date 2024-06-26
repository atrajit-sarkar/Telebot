import youtube_dl
import os

y={}


url=input("Enter your facebook url: ")

with youtube_dl.YoutubeDL(y) as u:
    u.download([url])

print("Done")