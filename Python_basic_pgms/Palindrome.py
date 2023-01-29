inp = "lool"
#Method1
inp = inp.casefold()
rev_str = reversed(inp)

if list(inp)==list(rev_str):
    print("palindrome")
else:
    print("not a palindrome")

#Method2

