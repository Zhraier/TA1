vow = "aeiouAEIOU"
con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
spec_num = 0
vow_num = 0
space_num = 0
con_num = 0

word = input("Enter a string: ")

for i in word:
    if i in vow:
        vow_num += 1
    elif i in con:
        con_num += 1
    elif i.isspace():
        space_num += 1
    else:
        spec_num += 1
        
print()
print("Number of vowels: ", vow_num)
print("Number of consonants: ", con_num)
print("Number of spaces: ", space_num)
print("Number of special characters: ", spec_num)
