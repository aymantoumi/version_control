from pytube import YouTube

# Replace this with the actual video URL

video_url = input(str('inter video URL : '))

# Specify the download directory
download_dir = ""

# Create a YouTube object
video = YouTube(video_url)

# Get the highest quality video stream
# You can also specify the video resolution or other attributes here
video_stream = video.streams.order_by('resolution').desc().first()

# Download the video with the highest quality
print(f"Downloading video: {video.title}")
video_stream.download(output_path=download_dir, filename=f"{video.title}.mp4")

print(f"Video '{video.title}' successfully downloaded!")
