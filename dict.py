"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["WoW"] = "Classic comes out in 3 and a half hours"
word_definitions["South Park"] = "A show that made fun of WoW"
word_definitions["Matthew"] = "Wants to play WoW with me"
word_definitions["Tyler"] = "Addicted to Coca-Cola."
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["WoW"])
print(word_definitions["South Park"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f'The Definition of {key} is {value}')

#print(word_definitions)