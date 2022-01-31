from gettext import find


def findMax(a,b,c):
    answer = max(a,b,c)
    return answer

print(findMax(14,8,6))

def countUpper_Lower(myStr):
    upperCount = 0
    lowerCount = 0
    for letter in myStr:
        if letter.isupper():
            upperCount += 1
        elif letter.islower():
            lowerCount += 1
    return 'Uppercase count is: ' + str(upperCount) + '\nLowercase count is: ' + str(lowerCount)
    

upperCase = countUpper_Lower('HI thEre')
print(upperCase)
