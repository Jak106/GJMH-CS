nums = [13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]
nums.sort()

gapData = {
    "numStart": 0,
    "numEnd": 0,
    "gap": 0
}

for x in range(1, len(nums)):
    if nums[x] - nums[x-1] > gapData["gap"]:
        gapData["numStart"] = nums[x-1]
        gapData["numEnd"] = nums[x]
        gapData["gap"] = nums[x] - nums[x-1]

print(f'the result is {gapData["gap"]}, (between {gapData["numStart"]} and {gapData["numEnd"]} in the sorted version)')