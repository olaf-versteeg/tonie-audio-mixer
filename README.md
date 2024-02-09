# What is this?
Given a folder with audio files and a target folder, this script generates a random playlist of all songs with the
given max. length. The original intention was to create a shuffled playlist for Creative-Tonies which have a
capacity of 90 minutes, but it can be used for playlists of arbitrary length.

# Prepare
Copy `.env.template` to `.env` and provide the path of the music folder, the path of the target folder and the
desired max. length of the playlist. The songs will be prefixed with a two digit number.