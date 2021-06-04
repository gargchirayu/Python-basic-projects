from pyshorteners import Shortener
ACCESS_TOKEN = '6bc9b2d0fe3690c5226323f55f4d29d8a47c6707'

# using bitly for this program, can use others as well, based on pyshorteners doc
url_shortener = Shortener(api_key=ACCESS_TOKEN)

# shortening a url
long_url1 = input("Long URL:  ")
short_url1 = url_shortener.bitly.short(long_url1)
print('Short URL:', short_url1)

print('\n')
# expanding a link
short_url2 = input("Short URL: ")
long_url2 = url_shortener.bitly.expand(short_url2)
print('Long URL: ', long_url2)