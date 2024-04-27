from pytube import Playlist

# Replace this with the actual playlist URL
playlist_url = input(str('inter playlist URL : '))


# Specify the download directory
download_dir = ""

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate through each video in the playlist
for video in playlist.videos:
    # Get the highest quality video stream
    # You can also specify the video resolution or other attributes here
    video_stream = video.streams.order_by('resolution').desc().first()

    # Download the video with the highest quality
    print(f"Downloading video: {video.title}")
    video_stream.download(output_path=download_dir, filename=f"{video.title}.mp4")

print(f"Successfully downloaded {len(playlist.videos)} videos from the playlist!")
