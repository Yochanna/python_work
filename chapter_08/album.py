def make_album(artist, title, tracks=None):
    album = {"artist": artist.title(), "title": title.title()}
    if tracks is not None:
        album["tracks"] = tracks
    return album

print(make_album("metallica", "ride the lightning"))
print(make_album("pink floyd", "the wall", tracks=26))


