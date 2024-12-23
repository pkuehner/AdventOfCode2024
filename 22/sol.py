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
    result = 0
    for line in lines:
        secret = int(line)
        for i in range(STEPS):
            secret = step(secret)
        result += secret
    print(result)