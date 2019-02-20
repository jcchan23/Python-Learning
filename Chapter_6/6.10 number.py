numbers = {
    'Jian Wen':['16','11','6','8','23'],
    'Jun Hong':['5','4','3','2','1'],
    'Zhi Jian':['76','33','40','26','57'],
    'Can Wen':['56','45','20','30','100'],
    'Chuo Zhong':['87','09','24','20','5'],
}
for name,favorite_numbers in numbers.items():
    print(name + "'s favorite numbers are ")
    for favorite_number in favorite_numbers:
        print(favorite_number)