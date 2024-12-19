from functools import lru_cache

cache = {}
@lru_cache(maxsize=None)
def check_if_pattern_matches(pattern):
    results = [0]* (int(len(pattern))+1)
    results[0] = 1
    
    for i in range(1, len(pattern)+1):
        for j in lengths:
            if i >= j and pattern[i-j:i] in patterns:
                results[i] += results[i-j]

    return results[len(pattern)]

def parse_input(input_text):
    # Split the input into lines
    lines = input_text.strip().split('\n')
    
    # First line contains the pattern
    patterns = [pattern.strip() for pattern in lines[0].split(",")]
    
    # Rest of the lines form the list
    entries = lines[2:]
    
    return patterns, entries

with open("input") as file:
    input_text = file.read()

patterns, entries = parse_input(input_text)
print("Pattern:", patterns)
patterns = set(patterns)
lengths = {len(pattern) for pattern in patterns}
res = 0
for entry in entries:
    x = check_if_pattern_matches(entry)
    print(entry, x)
    res += x
print(res)