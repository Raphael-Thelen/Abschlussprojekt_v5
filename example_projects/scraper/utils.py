def deprecated_function():
    print("This function is outdated but still here for some reason.")

def complex_function(x):
    result = 0
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            result += j / (i + 1)
    return result