import random

def calculate_backoff (tentativa):
    delay = tentativa ** 2

    delay = min(delay, 60)

    jitter = random.uniform(0, 1)

    return delay + jitter