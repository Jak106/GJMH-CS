import pathlib

path = pathlib.Path('')

content = []

output = {}

for item in path.rglob("*"):
    if item.is_file():
        content.append(str(item))
        
# display_filename_prefix_middle = '├──'
#     display_filename_prefix_last = '└──'
#     display_parent_prefix_middle = '    '
#     display_parent_prefix_last = '│   '

for ct in content:
    if "/" not in content:
        output[ct] = {}
    else:
        ct = ct.split("/")
        output[ct[0]] = []
    
    