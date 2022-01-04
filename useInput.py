userAge = input("please enter your age: ")
userName = input("Please enter your name: ")

userAgeNum = int(userAge)
birthYear = (2021 - userAgeNum)
hYear = (birthYear + 100)

responseString = "Hello {}, you are {} years old, and you will turn 100 years old in {}".format(userName, userAge, hYear)
print(responseString)