import subprocess
import z3

hardcoded_value = 1640

string = z3.String('string')
solver = z3.Solver()

def str_to_val(stri):
    result = subprocess.run([f"./string_to_value {stri}"], capture_output=True, text=True)
    _result = result.stdout
    return int(_result.split(",")[0])

solver.add(str_to_val(string) == hardcoded_value)

if solver.check() == z3.sat:
    model = solver.model()
    answer = model[string].as_string()
    print(f"secret string found, string = '{answer}'")
else:
    print("No solution exists")
