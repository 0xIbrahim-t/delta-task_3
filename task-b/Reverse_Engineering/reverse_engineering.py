import z3

hardcoded_value = 99903
len_of_word = 0

while True:
    if hardcoded_value % len_of_word != 0:
        continue

    if hardcoded_value // (32*(len_of_word ** 2)) == 0:
        break

    chars = [z3.Int(f"char_{i}") for i in range(len_of_word)]
    solver = z3.Solver()

    for char in chars:
        solver.add(char >= 32, char <= 126)

    squared_sum = z3.Sum([(i + 1) * (chars[i] * chars[i]) for i in range(len_of_word)])
    solver.add(squared_sum * len_of_word == hardcoded_value)

    while solver.check() == z3.sat:
        model = solver.model()
        print(''.join([chr(model[char].as_long()) for char in chars]))

        for char in chars:
            solver.add(char != model[char].as_long())

print("End of the solutions")
