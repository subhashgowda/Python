Vowel = "aeiou"
ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str.casefold()
counter = 0
for word in ip_str:
    if word in Vowel:
        counter = counter +1

print(counter)


count={}.fromkeys(Vowel,0)
for char in ip_str:
    if char in count:
        count[char] +=1

print(count)

str = "Subhash"
str= [67,98,"sfsd"]
u = {}.fromkeys(str,0)
v = u.items()
print(u)
print(v)