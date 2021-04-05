import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter your name? \n")

result = [new_dict[letter.upper()] for letter in word]

print(result)