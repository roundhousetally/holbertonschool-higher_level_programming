#!/usr/bin/python3
def no_c(mystring):
    if (mystring):
        for i in range((len(mystring))):
            mystring = mystring.translate({ord(i): None for i in 'Cc'})
        return (mystring)
