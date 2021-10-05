# Combo-Fixer
A simple python code to fix your combo list by removing any text after a separator

As an example we have the following combo list file:
```
abc123@mail.com:password |  leaked by anonymous
def456@mail.com:password |  leaked by anonymous
ghi789@mail.com:password |  leaked by anonymous
```
Obviously, if you want to check these accounts with a checker, you will have problems.

So, by using this code, the top combo list will be like this by setting " |" as a the separator:
```
abc123@mail.com:password
def456@mail.com:password
ghi789@mail.com:password
```

Hope you like the code ❤
