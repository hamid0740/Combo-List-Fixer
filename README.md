# Combo List Fixer
A simple python code to fix your combo list by removing any text after a separator or removing duplicate combos


## Removing any text after a separator
As an example we have the following combo list file:
```
abc123@mail.com:password |  leaked by anonymous
def456@mail.com:password |  leaked by anonymous
ghi789@mail.com:password |  leaked by anonymous
```
Obviously, if you want to check these accounts with a checker, you will encounter some problems.

So, by using this code, the above combo list will be like the bottom by setting " |" as the separator:
```
abc123@mail.com:password
def456@mail.com:password
ghi789@mail.com:password
```

## Removing duplicate combos
As an example we have the result of that following combo list file:
```
abc123@mail.com:password
def456@mail.com:password
ghi789@mail.com:password
def456@mail.com:password
```
Then after you accept to remove duplicate combos, the results bottom will be saved:
```
abc123@mail.com:password
def456@mail.com:password
ghi789@mail.com:password
```

## Output
After you enter the required info, if the operation completes successfully, the results will be saved as `output.txt`.

Hope you like the code ❤
