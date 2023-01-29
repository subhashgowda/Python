# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

mystr = "My!!! People have the tendency to& ,speak more loudly? ---==when they get excited/."
no_punct=""

for i in mystr:
    if i not in punctuations:
        no_punct = no_punct + i

print(no_punct)