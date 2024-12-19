from functools import lru_cache

@lru_cache(maxsize=None)
def check_if_pattern_matches(pattern):
    if pattern in patterns:
        return 1
    if len(pattern) == 1:
        return 0
    
    res = 0
    for i in range(1, len(pattern)):
        i_pattern = check_if_pattern_matches(pattern[0:i])
        if i_pattern > 0:
            j_pattern = check_if_pattern_matches(pattern[i:])
            if j_pattern > 0:
                res += i_pattern * j_pattern
    return res

def parse_input(input_text):
    # Split the input into lines
    lines = input_text.strip().split('\n')
    
    # First line contains the pattern
    patterns = [pattern.strip() for pattern in lines[0].split(",")]
    
    # Rest of the lines form the list
    entries = lines[2:]
    
    return patterns, entries

with open("debug") as file:
    input_text = file.read()

patterns, entries = parse_input(input_text)
print("Pattern:", patterns)
patterns = set(patterns)
print("Entries:", entries)
result = 0
for entry in entries:
    x = check_if_pattern_matches(entry)
    print(entry, x)
    result += x
print(result)