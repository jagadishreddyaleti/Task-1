'''write a python programme which iterates the integers from 1 to 50.
for multiples of three print "fizz" instead of the number and for the multiples of five print "buzz"
for numbers which are multiples of three and five printb"fizzbuzz"'''
for i in range(1,50):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else :print(i)