#String in Python:
# city = 'Bhopal'
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])

# name = 'Abhishek Thakur'
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])

# print(len(city))
# print(len(name))


# text = 'Hello Python World'

# #Case
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# #Strip Whitespace
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# #Search
# print('Python' in text)
# print(text.find('Python'))
# print(text.count('l'))


# #Replace
# print(text.replace('Python', 'AI'))

# #Split and Join:
# csv = 'Rahul,22,Bhopal,Enginner'
# parts = csv.split(',')
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# #Check Content
# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print('  '.isspace())

# #Start/End Check
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))


#F Strings:
# name, marks, rank = 'Anita' , 92.567, 3

# #Basic
# print(f'Hello, {name}!')

# #Format numbers
# print(f'Marks: {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'Count: {1000000:,}')

# #Padding and alignment:
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')
# print(f'hello{name:^10}')
# print(f'hello{name:>10}')
# print(f'hello{name:<10}')
# print(f'hello{name:*^11}')

# #Expressions inside {}
# price, gst = 500, 0.18
# print(f'price:Rs.{price} | GST:Rs.{price*gst:2f} | Total:RS.{price*(1+gst):.2f}')