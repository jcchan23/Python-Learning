def make_album(musician,music_name):
    disk ={
        'author':musician,
        'name':music_name,
    }
    return disk

while True:
    print("\nPlease tell the musician name and music name:")
    print("\n(enter 'q' at any time to quit)")

    musician_name = input("musician name:")
    if musician_name == 'q':
        break
    
    music_name = input("music name:")
    if music_name == 'q':
        break

    format_name = make_album(musician_name,music_name)
    print(format_name)
