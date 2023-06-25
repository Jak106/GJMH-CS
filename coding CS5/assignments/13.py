with open("samples.txt", "r", encoding="utf-8") as f:
    sequences = f.read().split("\n")

good, bad = [], []

resDic = {}

def is_valid(dna:str):
    for letter in list(dna):
        if letter != "A" and letter != "C" and letter != "T" and letter != "G":
            return False
    else:
        print(f"Sequence: {dna} is valid")
        return True

def get_hamming_distance(sample1, sample2):
    sample1, sample2 = list(sample1), list(sample2)
    diff = 0
    for i in range(max([len(sample1), len(sample2)])):
        try:
            if sample1[i] != sample2[i]:
                diff += 1
        except:
            diff += 1
            
    sample1 = "".join(sample1)
    sample2 = "".join(sample2)
    return [sample1, sample2, diff]

for seq in sequences:
    if is_valid(seq):
        good.append(seq)
    else:
        bad.append(seq)
    
least = [0, 0, 99]

for i in range(len(good)-1):
    for j in range(i+1, len(good)):
        res = get_hamming_distance(good[i], good[j])
        if res[2] < least[2]:
            least = res

print(f"Sequence 1: {least[0]}, Sequence 2: {least[1]}, Hamming distance: {least[2]}")
