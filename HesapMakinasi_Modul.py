def toplama(a,b):
    return a+b

def cikarma(a,b):
    if(a>b):
        return a-b
    else:
        return b-a
    
def carpma(a,b):
    return a*b

def bolme(a,b):
    if(b == 0):
        print("Sifira bolme hatasi!")
    else:
        return a//b
