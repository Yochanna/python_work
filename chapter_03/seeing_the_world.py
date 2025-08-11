places = ["Kyoto", "Reykjavik", "Cape Town", "Auckland", "Lisbon"]

print("Original order:", places)
print("Sorted:", sorted(places))
print("Original again:", places)
print("Reverse sorted:", sorted(places, reverse=True))
print("Original again:", places)

places.reverse()
print("Reversed in place:", places)
places.reverse()
print("Back to original:", places)

places.sort()
print("Sorted in place:", places)
places.sort(reverse=True)
print("Reverse-sorted in place:", places)
