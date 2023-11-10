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
channel_id = 'UC68TLK0mAEzUyHx5x5k-S1Q'
video_ids = get_video_ids(channel_id)

# Download and save transcripts
for video_id in video_ids:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Save the transcript with the video ID as the filename
        with open(f"{video_id}.txt", 'w') as file:
            for line in transcript:
                file.write(f"{line['text']}\n")
    except Exception as e:
        print(f"An error occurred for video ID {video_id}: {e}")
