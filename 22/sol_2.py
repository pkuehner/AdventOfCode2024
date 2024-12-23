from functools import lru_cache

@lru_cache(maxsize=None)
def first(secret):
    val = secret*64
    return mix_and_prune(secret, val)

@lru_cache(maxsize=None)
def second(secret):
    val = int(secret/32)
    return mix_and_prune(secret, val)

@lru_cache(maxsize=None)
def third(secret):
    val = int(secret*2048)
    return mix_and_prune(secret, val)

@lru_cache(maxsize=None)
def mix_and_prune(secret, val):
    secret = mix(secret, val)
    secret = prune(secret)
    return secret

@lru_cache(maxsize=None)
def mix(secret, a):
    return secret ^ a

@lru_cache(maxsize=None)
def prune(secret):
    return secret % 16777216

@lru_cache(maxsize=None)
def step(secret):
    secret = first(secret)
    secret = second(secret)
    secret = third(secret)
    return secret

STEPS = 2000
secret = 123
with open("input") as f:
    lines = f.readlines()
    max_cost = 0
    max_sequence = None
    sequences = {}
    for line in lines:
        print(line)
        secret = int(line)
        diffs = []
        last_cost = -1
        single_sequencs = set()
        for i in range(STEPS):
            secret = step(secret)
            cost = secret%10
            if last_cost != -1:
                diffs.append(last_cost - cost)
            last_cost = cost
            if i >= 4:
                #print(diffs)
                sequence = ",".join([str(diff) for diff in diffs[-4:]])
                if sequence in single_sequencs:
                    continue
                single_sequencs.add(sequence)
                if sequence not in sequences:
                    sequences[sequence] = ([], 0)
                seq, cost_before = sequences[sequence]
                seq.append(sequence)
                sequences[sequence] = (seq, cost_before+cost)
                if cost_before+cost > max_cost:
                    max_sequence = seq
                    max_cost = cost_before+cost
    print("Price", max_cost)



    print(len(sequences))