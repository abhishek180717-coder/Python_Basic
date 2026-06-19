dictionary = {
"cat": "chat", 
"dog": "chien", 
"horse": "cheval"
   }
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))

print(dictionary['cat'])
print(phone_numbers['Suzy'])
print(phone_numbers['president'])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
         print(word, "is not in dictionary")

print(dictionary.keys())

for key  in dictionary.keys():
    print(key, "->", dictionary[key])
    
print(dictionary.items())    
    
    
for key, value in dictionary.items():
    print(key, "->", value)    
    
print(dictionary.values())    
    
    
for value in dictionary.values():
    print(value)        


pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
print("pol_eng_dictionary:", pol_eng_dictionary)
copy_dictionary = pol_eng_dictionary.copy()

print("copy_dictionary:", copy_dictionary)

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]
print(item)
print(pol_eng_dictionary)

phonebook = {}

print(phonebook)
phonebook["Adam"] = 3456783958
print(phonebook)

del phonebook["Adam"]
print(phonebook)

pol_eng_dictionary = {"kwiat": "flower"}
pol_eng_dictionary.update({"gleba": "soil"})

print(pol_eng_dictionary)

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)


pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
   print("Yes")
else:
   print("No")
   
 
 
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek1" in pol_eng_dictionary:
   print("Yes! zamek1 is present in the Dictionary")
else:
   print("No! zamek1 is not present in the Dictionary")
   
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(pol_eng_dictionary)
print(len(pol_eng_dictionary))
 
del pol_eng_dictionary["zamek"]
print(pol_eng_dictionary) 
print(len(pol_eng_dictionary)) 

pol_eng_dictionary.clear()
print(pol_eng_dictionary) 
print(len(pol_eng_dictionary)) 

del pol_eng_dictionary
print(pol_eng_dictionary) 


