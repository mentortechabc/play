def make_album(album_name, artist, amount_tracks=''):
    album = {'album_name': album_name, 'artist': artist}
    if amount_tracks:
        album['amount_tracks'] = amount_tracks
    return album

list_albums = []
while True:
    print('for exit enter q')
    album_name = input('enter allbum\'s name')
    if album_name == 'q':
        break
    artist = input('enter artist\'s name')
    if artist == 'q':
        break
    amount_tracks = input('amount tracks:')
    if amount_tracks == 'q':
        break
    list_albums.append(make_album(album_name, artist,amount_tracks))
for album in list_albums:
    print(album)