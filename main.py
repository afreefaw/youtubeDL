from pytube import YouTube
import csv
import configparser

#load settings.ini
config = configparser.ConfigParser()
config.read('settings.ini');
path = config['SETTINGS']['download_path']

# Open the CSV file using the csv.DictReader() function
with open('video_urls.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create an empty list to store the URLs
    url_list = []

    # Iterate over the rows in the CSV file
    for row in reader:
        # Get the URL from the 'url' column
        url = row['url']

        # Add the URL to the list
        url_list.append(url)

start = int(config['SETTINGS']['start_num'])
end = len(url_list) if int(config['SETTINGS']['end_num']) == -1 else int(config['SETTINGS']['end_num'])

for url in url_list[start:end]:
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(config['SETTINGS']['stream_itag'])
    stream.download(output_path = path)