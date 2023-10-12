def tri_recursion(k, total):
    if(k > 0):
        result = k + tri_recursion(k - 1, total)
        print("We are at recursion #{} of {}".format(k, total))
        print("result: {}".format(result))
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
recursions = int(input("Enter a number: "))
tri_recursion(recursions, recursions)