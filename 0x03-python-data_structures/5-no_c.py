#!/ussr/bin/python3
def no_c(mystring):
    i = 0
    for i in range((len(mystring))):
        mystring = mystring.translate({ord(i): None for i in 'Cc'})
        return (mystring)
