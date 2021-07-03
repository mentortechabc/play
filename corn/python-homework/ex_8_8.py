def make_album(name, album_name, track=""):
    r = {}
    if track:
        r["name"] = name
        r["album_name"] = album_name
        r["track"] = track
        return r
    else:
        r["name"] = name
        r["album_name"] = album_name
        return r


while True:
    name = input("\ninput name or 'q' to exit: ")
    if name == "q":
        break
    album_name = input("\ninput album name or q to exit: ")
    if album_name == 'q':
        break
    track = input("\ninput number tracks or q to exit: ")
    if track == 'q':
        break
    print(make_album(name, album_name, track))
