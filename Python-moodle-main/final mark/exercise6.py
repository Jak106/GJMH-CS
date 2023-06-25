days = [9, 9]
progress = 0
for x in range(1, len(days)):
    if days[x] > days[x-1]:
        progress += 1

if progress == 1:
    print(progress, "day")
else:
    print(progress, "days")