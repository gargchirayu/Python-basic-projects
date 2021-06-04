from pytube import YouTube
from pytube.cli import on_progress

link = input("Enter YT link: ")
yt = YouTube(link, on_progress_callback=on_progress)
print('\nTitle: ', yt.title)
print('Length: ', yt.length, 'seconds')
print('Ratings: ', yt.rating)
# similarly all attributes can be done

# print(yt.streams)
# print(yt.streams.filter(only_audio=True)) or only_video

print(yt.streams.filter(progressive=True).order_by('resolution').desc())
dl = yt.streams.get_highest_resolution()
# dl = yt.streams.get_by_itag('ITAG_NUM')
print('Downloading')
dl.download()
# print('Download Complete')

# to be implemented in GUI with proper progress bar calibration
# ref: https://stackoverflow.com/questions/56197879/how-to-use-progress-bar-in-pytube
