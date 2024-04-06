from pytube import YouTube

# Replace the link which you want to download
yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')

# Filter only progressive streams (progressive: file containing both audio and video file)
video_streams = yt.streams.filter(progressive=True)

# Displays list of available stream
for i,streams in enumerate(video_streams):
    print(f"{i}: {streams}")

# Select the audio stream to download
stream_number = int(input('Enter the number of the stream you wnat to download: '))
chosen_stream = video_streams[stream_number]

# Download the video
path = chosen_stream.download('downloads/')
print(f'Your file is downloaded at {path}')