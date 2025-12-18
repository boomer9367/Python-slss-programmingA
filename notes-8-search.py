# Data Analysis
# Author: Justin L
# # Heavily based on ubial's code
import csv

# Analyse the data provided in class
# Introduction to Search Algorithms
# Search for all songs by "Kendrick"
# Display all YouTube and TikTok views
# Sort by either YouTube or TikTok views


def main():
    artist = "Kendrick Lamar"  # artist to find
    artist_two = "Justin Bieber"
    artist_three = "Taylor Swift"
    track_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)
        songs = []

        # read each line of data
        for info in r:
            if artist_three == info[artist_col]:
                songs.append(info)

        # print how many songs are in the list
        print(f"Number of" + artist_three + "songs: {len(songs)}")

        for song in songs:
            current_trackname = song[track_col]
            current_ytviews = song[yt_views_col]
            current_tiktokviews = song[tiktok_views_col]

            # display information in a clear way
            # Squabble Up       100,000,000     120,000,000
            if 7 < len(current_trackname) < 14:
                tabs = "\t\t\t"
            elif 14 < len(current_trackname) < 18:
                tabs = "\t\t"
            elif 18 < len(current_trackname):
                tabs = "\t"
            else:
                tabs = "\t\t\t\t"

            print(
                f"{current_trackname.strip()}{tabs}{current_ytviews.strip()}\t{current_tiktokviews.strip()}"
            )

        # for song in kendrick_songs:
        #     print(song)


if __name__ == "__main__":
    main()
