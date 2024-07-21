import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# The shortcode is part of the video URL: https://www.instagram.com/p/SHORTCODE/
shortcode ="https://www.instagram.com/reel/C9He4wsyh0Q/?igsh=OGg2MTNmNjBxYjhr"
shortcode=shortcode.split("/")
# print((shortcode[4]))
# Load the post using the shortcode
post = instaloader.Post.from_shortcode(L.context, shortcode[4])

# Download the video from the post
L.download_post(post, target=post.owner_username)

