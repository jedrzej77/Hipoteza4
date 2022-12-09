alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #
# # a=input("podaj hasło: ")
# # b=list(a)
# # print(b)
# #
# for i in range(len(b)):
#     counter=1
#     for j in range(len(alfabet)) :
#         if b[i]==alfabet[j]:
#             b[i]=alfabet[j+i]
#     counter=counter+1
# #
# # print(b)
#
word=input("podaj hasło: ")

# for i in range(len(word)):
#     print(ord(word[i]))

# letter='a'
# print("stara literka: ", letter)
# letter_ascli = ord(letter)
# letter_ascli +=3
# letter=chr(letter_ascli)
# print("literka przesunięta i jeden: ", letter)
#
wyraz2=[]
couter=1
for i in range(len(word)):
    for j in range(len(alfabet)) :
        if word[i]==alfabet[j]:
            counter =i+j+1
            wyraz2.append(alfabet[counter])


print(wyraz2)


