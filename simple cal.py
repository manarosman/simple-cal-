#simple cal:

x=float(input('Enter num1 '))
y=float(input('Enter num2 '))
print('جمع = '+ str(x+y))
print('طرح = '+ str(x-y))
print('ضرب= '+  str(x*y))
print('قسمة ='+  str(x/y))


#complex cal:

def cal(x,y):
    print('جمع = '+ str(x+y))
    print('طرح = '+ str(x-y))
    print('ضرب= '+  str(x*y))
    print('قسمة ='+  str(x/y))

cal(8,2)    




#complex cal2:

def c():
    x=float(input('Enter num1 '))
    y=float(input('Enter num2 '))
    print('جمع = '+ str(x+y))
    print('طرح = '+ str(x-y))
    print('ضرب= '+  str(x*y))
    print('قسمة ='+  str(x/y))

c()


#complex cal3 using return :

def cal():
    x=float(input('Enter num1 '))
    y=float(input('Enter num2 '))
    return x*y

print(cal())

#or using lambda :

sum= lambda x,y :x+y
print(sum(8,2))


    
