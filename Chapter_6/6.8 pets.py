Tom = {
    'class':'dog',
    'host':'Jerry',
}
Martin = {
    'class':'cat',
    'host':'Jackson',
}
King = {
    'class':'horse',
    'host':'Young',
}
pets = [Tom , Martin , King]
for pet in pets:
    print(pet)
    print(pet['class'] + " " + pet['host'])