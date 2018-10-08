def hello():
    print('Nigger')

def hello_return():
    return 'Nigger returned'

def hello_greeting(greeting, mname='You'):
    return '{} {}'.format(greeting, mname)

def stud_info(*args, **kwargs):
    print(args)
    print(kwargs)

print hello #<function hello at 0x7fd6efac4578>

hello() #Nigger
print hello_return() # Nigger returned
print hello_greeting('Hello', ) #Hello You
print hello_greeting('Hello', 'Naten') #Hello Naten
stud_info('')