import requests
import os

def download_facebook_video(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print("Video downloaded successfully!")
        else:
            print("Failed to download video.")
    except PermissionError:
        print(f"Permission denied: You don't have write access to the save path {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
video_url = input("Enter your link: ")
save_file_path = os.getcwd()
download_facebook_video(video_url, save_file_path)
