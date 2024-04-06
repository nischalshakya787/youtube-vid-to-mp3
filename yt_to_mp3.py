from pytube import YouTube
import moviepy.editor as mp
import os

# Replace the link which you want to download
yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')

# Filter only audio streams
audio_streams = yt.streams.filter(only_audio=True)

# Displays list of available stream
for i, stream in enumerate(audio_streams):
    print(f"{i}: {stream}")

# Select the audio stream to download
stream_number = int(input('Enter the number of the stream you want to download: '))
chosen_stream = audio_streams[stream_number]

# Download the audio
audio_file_path = chosen_stream.download('downloads/')

# Convert the audio to MP3
audio_clip = mp.AudioFileClip(audio_file_path)
mp3_file_path = audio_file_path[:-4] + '.mp3'  # Change the extension to .mp3
audio_clip.write_audiofile(mp3_file_path)

# Delete the original audio file
audio_clip.close()
os.remove(audio_file_path)

print(f"MP3 file downloaded at: {mp3_file_path}")
