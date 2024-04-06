from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley') #replace the link which you want to download

# all = yt.streams.all()
# video = yt.streams.filter(type="video") #Filters only video
audio = yt.streams.filter(only_audio = True) #Filters only mp3
audio_list = list(enumerate(audio))

for i in audio_list:
    print (i)

stream = int(input('Enter the number you want to download: '))

audio[stream].download('downloads/')

