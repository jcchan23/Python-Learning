def make_album(musician,music_name,number=''):
    if number:
        disk ={
            'author':musician,
            'name':music_name,
            'number':number,
        }
    else:
        disk ={
            'author':musician,
            'name':music_name,
        }
    return disk
print(make_album('Hong Kia Kui','myth',25))
print(make_album('Eason','Christmas'))
print(make_album('Kay','Sing'))