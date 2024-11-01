  #Write a program to calculate the number of notes in the given amount?

a = int(input('Enter the amount you would like to withdraw'))
b = a//100
c = (a%100)//50
d = ((a%100)%50)//10
print('Notes of 100',b)
print('Notes of 50',c)
print('Notes of 10',d)