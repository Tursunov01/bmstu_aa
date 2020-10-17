from main import LevRecursion, LevTable, DamLevRecursion, DamLevTable, GenerateString

def BasicTests(function):
    errors = 0
    errors += 1 if function("", "") != 0 else 0
    errors += 1 if function("abc", "abc") != 0 else 0
    errors += 1 if function("0", "0") != 0 else 0
    errors += 1 if function("a", "") != 1 else 0
    errors += 1 if function("", "1") != 1 else 0
    errors += 1 if function("b", "c") != 1 else 0
    errors += 1 if function("bc", "b") != 1 else 0
    errors += 1 if function("bc", "c") != 1 else 0
    errors += 1 if function("ab", "cd") != 2 else 0
    return errors

def ProTests(f1, f2):
    errors = 0
    str1 = GenerateString(5)
    str2 = GenerateString(5)                       
    errors += 1 if f1(str1, str2) != f2(str1, str2) else 0
    str1 = GenerateString(3)
    str2 = GenerateString(5)                       
    errors += 1 if f1(str1, str2) != f2(str1, str2) else 0
    str1 = GenerateString(4)
    str2 = GenerateString(0)                       
    errors += 1 if f1(str1, str2) != f2(str1, str2) else 0
    return errors
        
def start():
    print("Basic tests:")
    print("Number of failed tests in LevRecursion method: ", BasicTests(LevRecursion))
    print("Number of failed tests in LevTable method: ", BasicTests(LevTable))
    print("Number of failed tests in DamLevRecursion method: ", BasicTests(DamLevRecursion))
    print("Number of failed tests in DamLevTable method: ", BasicTests(DamLevTable))
    print("Pro tests(Here we check how works table and recursions methods):")
    print("Levenstein method: ", ProTests(LevRecursion, LevTable))
    print("Damerau-Levenstein method: ", ProTests(DamLevRecursion, DamLevTable))

    

if __name__ == '__main__':
    start()