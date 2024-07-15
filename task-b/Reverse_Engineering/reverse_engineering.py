import subprocess
import z3

hardcoded_value = 1640

chars = [z3.BitVec(f'char_{i}', 8) for i in range(4)]
solver = z3.Solver()

def str_to_val(string):
    result = subprocess.run(["./string_to_value", string], capture_output=True, text=True)
    return int(result.stdout.split(",")[0])

for char in chars:
    solver.add(char >= 32, char <= 126)

tested_strings = set()

while solver.check() == z3.sat:
    model = solver.model()
    candidate_string = ''.join([chr(model[char].as_long()) for char in chars])
    
    if candidate_string not in tested_strings:
        tested_strings.add(candidate_string)
    
        if str_to_val(candidate_string) == hardcoded_value:
            print(f"Secret string found: '{candidate_string}'")
            solver.add(z3.Or([char != model[char] for char in chars]))
        
    solver.add(z3.Or([char != model[char] for char in chars]))
else:
    print("No solution exists")
