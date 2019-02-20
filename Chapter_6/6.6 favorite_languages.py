favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
names = ['jen','edward']
for name in favorite_languages.keys():
    if name in names:
        print("Thank's for voting, " + name)
    else:
        print("We are inviting you to vote, " + name)