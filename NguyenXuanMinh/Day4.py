def hang1():
    print ('+ - - - - + - - - - +')
def hang2():
    print ('|         |         |')
def hang3():
    print ('|    *    |    *    |')
a = [hang1(), hang2(), hang3(), hang2(), hang1(), 
    hang2(), hang3(), hang2(), hang1(), 
    hang2(), hang3(), hang2(), hang1()]
for i in a:
    i
