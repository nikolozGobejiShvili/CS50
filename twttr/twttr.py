text=input("input word :")
text3=""
for char in text:
    if  char not in "aeiouAEIOU":
        text3+=char

print(text3)