from pytube import YouTube

link = input("Enter YT link: ")
yt = YouTube(link)

print('\nTitle: ', yt.title)
print('Length: ', yt.length, 'seconds')
print('Ratings: ', yt.rating)
# similarly all attributes can be done

# print(yt.streams)
# print(yt.streams.filter(only_audio=True)) or only_video

# print(yt.streams.filter(progressive=True))

dl = yt.streams.get_highest_resolution()
# dl = yt.streams.get_by_itag('ITAG_NUM')
print('Downloading')
dl.download()
print('Download Complete')
