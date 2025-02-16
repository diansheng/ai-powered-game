import random

def generate_puzzle():
    a, b, c = random.randint(100, 999), random.randint(100, 999), random.randint(10, 99)
    puzzle = f"密码是 {a} + {b} - {c}"
    answer = str(a + b - c)
    return puzzle, answer
