favorite_places = {"alice": ["kyoto", "reykjavik"], "bob": ["lisbon"], "charlie": ["nairobi", "cairo"]}
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes:")
    for place in places:
        print(f" - {place.title()}")
