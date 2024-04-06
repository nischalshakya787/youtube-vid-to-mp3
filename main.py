from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley') #replace the link which you want to download

# If you want to dowload the video you can uncomment the command with filter type = video and filter only_audio for mp3

# type = yt.streams.all()
# type = yt.streams.filter(type="video") #Filters only video
type = yt.streams.filter(only_audio = True) #Filters only mp3
type_list = list(enumerate(type))

for i in type_list:
    print (i)

stream = int(input('Enter the number you want to download: '))

type[stream].download('downloads/')

