""" Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string. """
# str = "noha"
# length =  len(str)
# count = 0 
# vowels = 'aeiou'

# for ch in range(length):
#     if str[ch].lower() in vowels:
#         count+=1 

# print(count)      


""" Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output. """

# userInput = []

# for i in range(5):
#     str = input("insert element : ")
#     userInput.append(str)

# ascending = sorted(userInput)
# descending = sorted(userInput,reverse=True)

# print("in ascending order " , ascending)
# print("in descending order " , descending)


""" Write a program that prints the number of times the string 'iti' occurs in anystring. """

# str = "iti is a information technology institute iti iti iti"
# str = str.split()
# count = 0 
# for i in range(len(str)):
#     if str[i] == 'iti':
#         count+= 1

# print(count)

""" Write a program that remove all vowels from the input word and generate a brief version of it. """

# str = input("insert element : ")
# vowels = 'aeiou'
# newversion =""
# for ch in range(len(str)):
#     if str[ch].lower() not in vowels:
#         newversion+= str[ch]

# print(newversion)


""" Write a program that prints the locations of "i" character in any string you added. """

# str = input("insert element : ")
# locations = []
# for i in range(len(str)):
#     if str[i].lower() == "i":
#         locations.append(i)

# print(locations)


""" Write a program that generate a multiplication table from 1 to the number passed. """

# number = int(input("insert number : ")) 

# res = []

# for i in range(1 , number+1):
#     arr = []
#     for j in range(1 , i+1):
#         arr.append(i*j)
#     res.append(arr)

# print(res)


""" Write a program that build a Mario pyramid like below  """

# num = int(input("Enter the number of rows: ")) 

# for i in range(1, num+1):
#     for j in range(num-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()