from math import sqrt

argNum = int(input("how many coordinates do you have? "))
arg = []#[sqrt(5), -9/2, -1], [3, 0, sqrt(3)]]

if argNum == 3:
    arg.append([float(input("x: ")), float(input("y: ")), float(input("z: "))])
    arg.append([float(input("x: ")), float(input("y: ")), float(input("z: "))])
elif argNum == 2:
    arg.append([float(input("x: ")), float(input("y: "))]) 
    arg.append([float(input("x: ")), float(input("y: "))])

nums = []
for x in range(len(arg[0])):
    nums.append((arg[1][x]-arg[0][x])**2)
if argNum == 3:
    length = sqrt(nums[0] + nums[1] + nums[2])
    midPoint = [(arg[0][0]+arg[1][0])/2, (arg[0][1]+arg[1][1])/2, (arg[0][2]+arg[1][2])/2]
    vector = [arg[1][0]-arg[0][0], arg[1][1]-arg[0][1], arg[1][2]-arg[0][2]]
elif argNum == 2:
    length = sqrt(nums[0] + nums[1])
    midPoint = [(arg[0][0]+arg[1][0])/2, (arg[0][1]+arg[1][1])/2]
    vector = [arg[1][0]-arg[0][0], arg[1][1]-arg[0][1]]

print("Vector =", vector)
print("Length =", length)
print("Midpoint =", midPoint)
