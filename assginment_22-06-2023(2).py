asciidict = dict()
for i in range(97,123):
    asciidict[chr(i)]= i
    key = asciidict.keys()
    value = asciidict.values()
print('ASCII Dict:',asciidict)
n = str(input('enter the key-'))
print('key:',n)    
print('value:',asciidict[n])

