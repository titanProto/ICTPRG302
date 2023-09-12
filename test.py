#                _    _
#  _ __   _   _ | |_ | |__    ___   _ __
# | '_ \ | | | || __|| '_ \  / _ \ | '_ \
# | |_) || |_| || |_ | | | || (_) || | | |
# | .__/  \__, | \__||_| |_| \___/ |_| |_|
# |_|     |___/

#  _               _    _
# | |_   ___  ___ | |_ (_) _ __    __ _
# | __| / _ \/ __|| __|| || '_ \  / _` |
# | |_ |  __/\__ \| |_ | || | | || (_| |
#  \__| \___||___/ \__||_||_| |_| \__, |
#                                 |___/
## This is a general code testing file, it will be used to test anything and generate code for examples in assignments for this subject

#ASSESSMENT 1
a = 15
b = 7

def coolFunction():
    global c
    c = "abc"
    x = True
    print(a)
    print(b)
    print(c)
    print(x)

coolFunction()

print(a)
print(b)
print(c)
# print(x) #won't print, not globalled