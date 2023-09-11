def hello10 () :
    print ("Hello "*10)

def pyramid () :
    star = ' * ' 

    for i in range (0,10) :
        print (star.center (20,' '))
        star +='**'

hello10 ()
pyramid ()