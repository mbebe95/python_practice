from pytube import YouTube

def download_video(url):
    try:
        # YouTube objektum létrehozása az URL alapján
        yt = YouTube(url)

        # A videó címe és nézettsége
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        # A legmagasabb felbontású stream kiválasztása
        ys = yt.streams.get_highest_resolution()

        # Videó letöltése az aktuális könyvtárba
        print("Downloading...")
        ys.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Bekéri a felhasználótól a YouTube URL-t
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)