# Q33. Write a program that takes an array of names and returns an array 
# where only the first letter of each name is capitalized.

#   Examples
#     (["mavis", "senaida", "letty"]) ➞ ["Mavis", "Senaida", "Letty"]
#     (["samuel", "MABELLE", "letitia", "meridith"]) ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]
#     (["Slyvia", "Kristal", "Sharilyn", "Calista"]) ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]
  
#   Notes
#     Don't change the order of the original array.
#     Notice in the second example above, "MABELLE" is returned as "Mabelle".

def toCapitalize(wordArr):
    capitalizeArr = []
    for word in wordArr:
        capitalizeArr.append(word.capitalize())
    return capitalizeArr

examples = [["mavis", "senaida", "letty"],  ["samuel", "MABELLE", "letitia", "meridith"], ["Slyvia", "Kristal", "Sharilyn", "Calista"]]
for example in examples:
        print(example,'➞',toCapitalize(example))