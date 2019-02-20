current_users = ['JCChan','Jack','John','Tom','admin']
new_users = ['Jerry','Peter','John','Mary','Tom']
for new_user in new_users:
    if new_user.lower().title() in current_users:
        print(str(new_user) + " had been used, please input another name!")
    else:
        print(str(new_user) + " can be used!")