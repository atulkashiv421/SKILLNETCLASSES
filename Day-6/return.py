def my_function(x):
    return 5 *x
print(my_function(3))

def my_function(x,/):
    print(x)
my_function(5)

#keyword only arguments

def my_function(*,x):
    print(x)
my_function(x=5)

def my_function(*,x):
    print(x)
my_function(x=6)


#combine key form and  position form
def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
my_function(5,6,c=7,d=8)

