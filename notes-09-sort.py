import helper_spotify


# Sorting Algorithms
def selection_sort(l: list[int], ascending=True) -> list[int]:
    num_items = len(l)

    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i

        for j in range(i + 1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]

        l[i], l[candidate_index] = l[candidate_index], l[i]

    return l


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    num_songs = len(songs)

    for i in range(num_songs):
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i

        for j in range(i + 1, num_songs):
            this_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                if this_val < candidate_val:
                    candidate_val = this_val
                    candidate_idx = j
            else:
                if this_val > candidate_val:
                    candidate_val = this_val
                    candidate_idx = j

        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # --------------------------------------------------------
    # TASK 1 — Songs by Ed Sheeran, print YT views
    # --------------------------------------------------------
    print("\nTASK 1 — Ed Sheeran Songs")
    print("---------------------------")

    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")

    for song in ed_songs:
        print(song[0], "\t", song[11])  # Track name, YouTube views

    # --------------------------------------------------------
    # TASK 2 — Sort by YouTube Views (ascending)
    # --------------------------------------------------------
    print("\nTASK 2 — Sorted by YouTube Views (Ascending)")
    print("---------------------------------------------")

    yt_sorted = sort_songs(ed_songs.copy(), 11, ascending=True)

    for song in yt_sorted:
        print(song[0], "\t", song[11])

    # --------------------------------------------------------
    # TASK 3 — Sort by TikTok Views (descending)
    # --------------------------------------------------------
    print("\nTASK 3 — Sorted by TikTok Views (Descending)")
    print("---------------------------------------------")

    tiktok_sorted_desc = sort_songs(ed_songs.copy(), 12, ascending=False)

    for song in tiktok_sorted_desc:
        print(song[0], "\t", song[12])

    # --------------------------------------------------------
    # TASK 4 — songs containing "the" in track name
    # --------------------------------------------------------
    print("\nTASK 4 — Songs with 'the' in the Track Name")
    print("---------------------------------------------")

    songs_with_the = helper_spotify.songs_by_title("data/spotify2024.csv", "the")

    for song in songs_with_the:
        print(song[0])  # Track name

    # --------------------------------------------------------
    # TASK 5 — Sort the Task 3 results again by TikTok views
    # --------------------------------------------------------
    print("\nTASK 5 — TikTok-sorted list (from Task 3 data)")
    print("------------------------------------------------")

    tiktok_sorted_again = sort_songs(tiktok_sorted_desc.copy(), 12, ascending=False)

    for song in tiktok_sorted_again:
        print(song[0], "\t", song[12])
