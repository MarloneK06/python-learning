#FizzBuzz
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
#Time Table Pattern
n = 6

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
    
#Remove Duplicates Preserving Order
def unique_preserve_order(lst):
    result = []
    seen = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.append(item)

    return result

# example test
print(unique_preserve_order([1, 2, 2, 3, 1, 4, 4, 5]))
