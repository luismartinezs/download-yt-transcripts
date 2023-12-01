import os
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

load_dotenv()  # This loads the .env file

api_key = os.getenv('YOUTUBE_API_KEY')
if not api_key:
    raise ValueError("Please set the YOUTUBE_API_KEY environment variable.")

youtube = build('youtube', 'v3', developerKey=api_key)

# Retrieve all video IDs from a YouTube channel
def get_video_ids(channel_id):
    video_ids = []
    request = youtube.search().list(part='id', channelId=channel_id, maxResults=50, type='video')
    response = request.execute()

    while request is not None:
        for item in response['items']:
            video_ids.append(item['id']['videoId'])
        request = youtube.search().list_next(request, response)
        response = request.execute() if request is not None else []

    return video_ids

# Replace with the channel ID you're interested in
channel_id = 'UC2D2CMWXMOVWx7giW1n3LIg'
video_ids = get_video_ids(channel_id)

# Open a single file with the channel ID as the filename
with open(f"{channel_id}.txt", 'a') as file:
    for video_id in video_ids:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            # Write a header for the transcript
            file.write(f"Transcript for Video ID: {video_id}\n")
            # Append the transcript to the file
            for line in transcript:
                file.write(f"{line['text']}\n")
            # Optionally, write a separator after each transcript
            file.write("\n\n---\n\n")
        except Exception as e:
            print(f"An error occurred for video ID {video_id}: {e}")