'''What is String'''

# String is a group of characters. These characters may be 
# alphabets, digits or special characters including spaces. 
# String values are enclosed either in single quotation
#strings are immutable cannot change the predefined values
'basic use of string'
single = 'hello'
double = "\nhello"
multi = """multi line string
hello world"""
print(single, double, multi)

'slicing in string'
#string[start : stop : step]
p = 'PriyaGawhane'
print(p[0]) #p
print(p[3]) #y
print(p[-6]) #a it will go from reverse side and it starts from -1 not from 0
print(p[-9]) #y
print(p[2:6]) # iyaG from 2 to 5th always remember 6th char will not print
print(p[-9:-2]) #yaGawha 
print(p[:7]) #PriyaGa prints all from start 1 to 6th char
print(p[7:]) #whane prints all from char 7th to end
print(p[::-1]) #enahwagayirp reverse the string
print(p[2:8:2]) #iaa jumping from 2 char
print(p[::-1][::2]) #eawGyr reverse jump of two char
print(p[10:2:-1]) #nahwaGay
print(p[10:2:-2]) #nhaa reverse slicing jump

'iteration in string'
s='priya'

for char in s:
    print(char)

#string immutability
s = 'o' + s[1:]
print(s) #oriya

#Updating a string
s1 = 'h' + s[1:]
s2 = s.replace('riya', 'gawhane')
print(s1)
print(s2)

'Common string method'
u = 'Priya says hello'
print(len(u)) # 16 space is counted as well
print(u.upper()) #PRIYA SAYS HELLO Capitalize everything
print(u.lower()) #priya says hello lowerize everything
print(u.strip()) #Priya says hello removes spaces at the start or end of the string.
print(u.replace('riya', 'books')) #Pbooks says hello replace substring riya by book
print(u.title()) #Priya Says Hello  print first letter capital
print(u.find('say')) #6 its at 6th char
print(u.split()) #['Priya', 'says', 'hello'] prints like a list
print(" ".join(u)) #P r i y a   s a y s   h e l l o joined the list
print(u.startswith("Priya")) #True
print(u.isdigit()) #false
print(u * 9) #can repeat string multiple times
print(u + " " + p) #Priya says hello PriyaGawhane -> concatening 2 strings
print(u + p) #Priya says helloPriyaGawhane

