# README

Downlaod transcripts for entire youtube channels, might take some minutes depending on number of videos

## Setup

- Get youtube api key to interact with youtube api

## Run script

- Get youtube channel id:
  - Navigate to channel page
  - Open dev tools
  - In html tree search for "?channel_id"
  - Copy the value
- Paste channel id into file `download-transcripts.py`
- Change the language tag in `languages=['en']` if you need to
- Run script `py download-transcripts.py`, all transcripts will be appended to a new file