favorite_places = {
    'Tom' : ['London','Guang Zhou','Chang Sha'],
    'Jack' : ['Guang Zhou','Lan Zhou','Bei Jing'],
    'Jerry' : ['Shang Hai','Xi An','Xi Zang'],
}

for name,citys in favorite_places.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for city in citys:
        print("\t" + city)
