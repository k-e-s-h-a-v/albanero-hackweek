# Q.46 Given a simple sentence and a set of syntax rules, 
# validate if it is syntactically correct or not. 
# If correct return "True" otherwise "False".
# Assume that a sentence is syntactically correct if it fulfills the following rules:
# A sentence must start with an uppercase character.
# There must be spaces between words.
# Then the sentence must end with a full stop ( . ) 
# Two continuous spaces are not allowed.
# Two continuos uppercase characters are not allowed.
# Examples:
# Input : This sentence is syntactically correct.
# Output : True
# Input : This is SYntactically correct.
# Output : False

def isCapital(letter):
    if ord(letter)>=65 and ord(letter)<=90:
        return True
    return False

def syntaxCheck(s):
    if s[-1]!='.' or not isCapital(s[0]):
        return False
    for i in range(len(s)-1):
        if s[i]==s[i+1]==' ':
            return False
        elif isCapital(s[i]): 
            if isCapital(s[i+1]): 
                return False
    return True

sentence = 'This sentence is Syntactically correct.'
print(syntaxCheck(sentence))