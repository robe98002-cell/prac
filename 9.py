def is_wcwr(string):
    stack = []
    found_c = False
    for char in string:
        if char != 'c' and not found_c:
            stack.append(char)
        elif char == 'c' and not found_c:
            found_c = True
        else:
            if not stack:
                return False
            if char != stack.pop():
                return False
    return found_c and len(stack) == 0

test_cases = [
    "abba c abba",
    "abc c cba",
    "a c a",
    "ab c ba",
    "ab c ab",
    "abc c abc",
    " c ",
    "aabbc bbaa"
]

print("PDA Simulation for wcwR")
for test in test_cases:
    test = test.replace(" ", "")
    if is_wcwr(test):
        print(test, "Accepted")
    else:
        print(test, "Rejected")
