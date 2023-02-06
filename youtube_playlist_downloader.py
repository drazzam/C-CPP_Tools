!pip install pytube
import pytube
from google.colab import drive

def download_video(url):
    yt = pytube.YouTube(url)
    video = yt.streams.filter(file_extension='mp4').first()
    video_filename = video.default_filename
    video.download()
    return video_filename
  
# Enter Google Drive Folder Path to Save the Videos:
def upload_to_drive(file_path):
    drive.mount('/content/drive')
    !cp "$file_path" "/content/drive/My Drive/Hematology"
    print(f"{file_path} has been uploaded to Google Drive.")

def download_playlist(url):
    yt = pytube.Playlist(url)
    for url in yt.video_urls:
        file_path = download_video(url)
        upload_to_drive(file_path)
        
# Enter The YouTube Playlist:
playlist_url = "https://www.youtube.com/playlist?list=PLHZI7nXaX_S2_-zaJrrp77BsYO6o83WQW"
download_playlist(playlist_url)
