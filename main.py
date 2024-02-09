import os
import random
import shutil

import eyed3
from dotenv import load_dotenv

from model.Song import Song

load_dotenv()

PLAYLIST = f"{os.getenv('ROOT_PATH')}/{os.getenv('TARGET_PATH')}"
MAX_LENGTH_IN_MINUTES = os.getenv('PLAYLIST_MAX_LENGTH') * 60


def main():
    # Clear existing playlist folder
    for file in os.listdir(PLAYLIST):
        os.remove(os.path.join(PLAYLIST, file))

    # Read all music files with name and length
    songs = []
    for (path, dirs, files) in os.walk(os.getenv('ROOT_PATH')):
        for filename in files:
            file = os.sep.join([path, filename])
            mp3 = eyed3.load(file)
            songs.append(Song(filename, file, mp3.info.time_secs))

    total_length = 0
    counter = 1

    while len(songs) > 0:
        song = random.choice(songs)
        songs.remove(song)
        if total_length + song.length <= MAX_LENGTH_IN_MINUTES:
            total_length += song.length
            destination = f"{PLAYLIST}/{counter:02} - {song.name}"
            shutil.copy(song.path, destination)
            counter += 1
        else:
            break

    print(f"Number of songs: {counter}. Total length: {total_length}")


if __name__ == '__main__':
    main()
