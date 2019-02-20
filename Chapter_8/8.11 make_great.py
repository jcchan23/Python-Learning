magicians = ['Jack','Tony','John','Jerry']
make_great_magician=[]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    while magicians:
        magician = 'the Great ' + magicians.pop()
        make_great_magician.append(magician)

show_magicians(magicians)
make_great(magicians[:])
show_magicians(make_great_magician)
show_magicians(magicians)
