n = int(input())

is_balanced = True
last_bracket = ""

for _ in range(n):
    line = input()

    if line == "(":
        # Ако вече имаме отваряща скоба, това означава влагане (невалидно)
        if last_bracket == "(":
            is_balanced = False
        last_bracket = "("

    elif line == ")":
        # Ако затваряме скоба, без да има отворена преди това (невалидно)
        if last_bracket != "(":
            is_balanced = False
        last_bracket = ")"

            # Накрая проверяваме дали последната отваряща скоба е останала незатворена
if last_bracket == "(":
    is_balanced = False

if is_balanced:
            print("BALANCED")
else:
            print("UNBALANCED")