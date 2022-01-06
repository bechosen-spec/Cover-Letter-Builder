from entrylevel import EntryLvl
from middlelevel import MiddleLvl
from seniorlevel import SeniorLvl

print("Welcome to Cover letter builder app!")

print("Indicate the level you are applying for: ", end="")
print(f" \nEntry Level = E \
        \nMiddle Level = M \
        \nSenior Level = S", end="")
print(f"\nEnter Your Level:", end="")
level = input()
if len(level) > 1:
    print("\nInvalid Input!")
else:
    if level >= 'E' and level <= 'e':
        EntryLvl.EntryLevel()
    elif level >= 'M' and level <= 'm':
        MiddleLvl.MiddleLevel()
    elif level >= 'S' and level <= 's':
        SeniorLvl.SeniorLevel()
    else:
        print("\nInvalid level entered!")
