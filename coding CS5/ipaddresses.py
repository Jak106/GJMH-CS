import re

with open("Apache.log") as f:
    test_str = f.read()

    emails = {}

    matches = re.finditer(r"[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,4}", test_str, re.MULTILINE)

    for matchNum, match, in enumerate(matches, start=1):
        found = match.group()
        if found in emails:
            emails[found] += 1
        else:
            emails[found] =1
        
    print(emails)
