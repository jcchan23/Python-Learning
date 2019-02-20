def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile_1 = build_profile('Chen','Jian Wen', location = 'Guang Zhou',field = 'Chemistry',age = '23')
print(user_profile_1)
user_profile_2 = build_profile('Cen','Jun Hong', location = 'Guang Zhou',field = 'Computer',age = '22')
print(user_profile_2)
user_profile_3 = build_profile('Ye',' Zhuo Zhong', location = 'Guang Zhou',field = 'Electronic',age = '22')
print(user_profile_3)