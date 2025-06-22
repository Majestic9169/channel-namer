from english_words import get_english_words_set
import pandas as pd
import os
import fnmatch

# TODO: make this less convoluted
contact_files = sorted([os.path.join("./Contacts/", file) for file in fnmatch.filter(os.listdir("./Contacts/"), "*.csv") if os.path.isfile(os.path.join("./Contacts/", file))], reverse=True)[:4]

# ensure names column is "Name" exactly
name_lists = [pd.read_csv(file).Name.to_list() for file in contact_files]

# Name parser to extract letters
letter_sets = []
for name_list in name_lists:
    letters = set()
    for name in name_list:
        for first_letters in name.split():
            letters.add(first_letters[0].lower())
    letter_sets.append(letters)

# generate a set of english words
web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True) # web2 | gcide, usually web2 better

combos = set()

for a in letter_sets[3]:
    for b in letter_sets[2]: 
        for c in letter_sets[1]: 
            for d in letter_sets[0]:
                combos.add(f'{a}{b}{c}{d}')

for combo in combos:
    if combo in web2lowerset:
        print(combo)
