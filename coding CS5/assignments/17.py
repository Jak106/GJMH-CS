def is_valid(content:str, compare:list):
    global order
    content = list(content)
    for letter in content:
        letter = letter.upper()
        if letter not in compare:
            return False
    else:
        return True

def errorCheck(content:str):
    global order
    content = list(content)
    for letter in content:
        letter = letter.upper()
        if letter not in dnaContent and letter not in rnaContent:
            return f"{order}. Sequence contains nucleotides which are not known to human"
    else:
        return f"{order}. Sequence contains nuceotides from both RNA and DNA"

def turn(content:str, to:list, orig:list):
    res = ""
    for letter in list(content):
        letter = letter.upper()
        res += to[orig.index(letter)]
    return res
        
dnaContent = ["G", "C", "T", "A"]
rnaContent = ["C", "G", "A", "U"]

with open("DNARNA.txt", "r", encoding="utf-8") as f:
    sequences = f.read().split("\n")

order = 1

for seq in sequences:
    if len(seq) >= 1:
        if is_valid(seq, dnaContent):
            print(f"{order}. DNA sequence turned into {turn(seq, rnaContent, dnaContent)}")
        if is_valid(seq, rnaContent):
            print(f"{order}. RNA sequence turned into {turn(seq, dnaContent, rnaContent)}")
        if is_valid(seq, rnaContent) == False and is_valid(seq, dnaContent) == False:
            print(errorCheck(seq))
    else:
        print(f"{order}. Sequence number does not contain any nucleotides (blank line)")
    order += 1    
