# lower-to-uppercase
i=input()
for f in i:
    if f.islower():
        print(f.upper(),end='')
    else:
        print(f.lower(),end='')
