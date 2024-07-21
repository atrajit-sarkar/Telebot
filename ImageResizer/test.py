from PIL import Image

# Open an image file
with Image.open('path/to/image.jpg') as img:
    # The new size (width, height)
    new_size = (800, 600)
    # Resize the image
    resized_img = img.resize(new_size)

# Save the resized image
resized_img.save('path/to/resized_image.jpg')
