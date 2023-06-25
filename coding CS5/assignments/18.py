# option selection
option = input("Option 1 - press A (or a), Option 2 - any other key: ")
if option == 'A' or option == 'a':
  print('Option 1 has been selected')
else:
  print('Option 2 has been selected')
  
#---------------------------------------
import random
# generate 10 random integers between 1 and 100
numbers = [random.randint(1,100) for i in range(10)]

for num in numbers.copy():
   # remove all even numbers
    if num % 2 == 0:
        numbers.remove(num)

#---------------------------------------
# save the numbers to a file
output_file = open("out.txt", "w")
for number in numbers:
    output_file.write(str(number) + "\n")
output_file.close()
    
#---------------------------------------
# sort and show both lists
list1 = [6, 1, 7, 2, 9, 5]
print(sorted(list1))

list2 = [6, 2, 8, 5, 3, 11]
print(sorted(list2))

#---------------------------------------
# get another set of random values
randomList = []
for i in range(10):
    randomList.append(random.randint(-20,20))

print(randomList)
#---------------------------------------
# figure out the student's mark
points = int(input("Enter the number of points the student earned (max = 70): "))

while points not in range(0,71):
    points = int(input("Wrong input. Enter the number of points the student earned (max = 70): "))
    
percent = points / 70 * 100

if percent >= 90:
    print('Mark -> A')
elif percent >= 75:
    print('Mark -> B')
elif percent >= 50:
    print('Mark -> C')
elif percent >= 33:
    print('Mark -> D')
else:
    print('Mark -> E')
