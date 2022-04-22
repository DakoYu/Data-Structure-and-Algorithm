# Reverse an array

def reverse(arr):
    # Get the middle index
    mid_index = len(arr) // 2
    # Get the last index
    last_index = len(arr) - 1

    # Iterate through the mid index
    for i in range(mid_index):
        arr[i], arr[last_index - i] = arr[last_index - i], arr[i]

arr = [0, 1, 2, 3, 4, 5]
reverse(arr)
print(arr)


# Palindrome problem

def palindrome(s):
    # Initialize starting index and end index
    start_index = 0
    end_index = len(s) - 1

    # Use a while loop to check
    while start_index <= end_index:
        if s[start_index] != s[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True

s = 'abaa'

print(palindrome(s))

# Integer Reversion

def reverse_integer(num):
    # Initialize reverse num and remainder
    reverse_num = 0
    remainder = 0

    while num > 0:
        remainder = num % 10
        num //= 10
        reverse_num = reverse_num * 10 + remainder

    return reverse_num

num = 1234
print(reverse_integer(num))


# Anagram Problem

def anagram(str1, str2):
    # Sort the strings and check if they are equal to each other
    return sorted(str1) == sorted(str2)

str1 = 'abc'
str2 = 'cbd'
print(anagram(str1, str2))

# Dijkstra Problem

def dijkstra(arr):
    # Initialize variables
    w = b = 0
    r = len(arr) - 1
    
    # Iterate through a while loop
    while w <= r:
        print(w,b,r)
        if arr[w] == 'B':
            arr[w], arr[b] = arr[b], arr[w]
            w += 1
            b += 1
        elif arr[w] == 'W':
            w += 1
        elif arr[w] == 'R':
            arr[w], arr[r] = arr[r], arr[w]
            r -=1

arr = ['R', 'R', 'B', 'W', 'B']
dijkstra(arr)
print(arr)


# Trapping Rain Water Problem

def max_rain(arr):
    # Base Case
    if len(arr) < 3: return 0
    # Dynamically create left max boundary and right max boundary
    max_left = [0 for _ in range(len(arr))]
    max_right = [0 for _ in range(len(arr))]
    trap_water = 0

    # Create left max boundary
    for i in range(1, len(arr)):
        max_left[i] = max(arr[i - 1], max_left[i - 1])

    # Create right max boundary
    for i in range(len(arr) - 2, -1, -1):
        max_right[i] = max(arr[i + 1], max_right[i + 1])
    print(max_left, max_right)
    # Create trap water
    for i in range(1, len(arr) - 1):
        if min(max_left[i], max_right[i]) > arr[i]:
            trap_water += min(max_left[i], max_right[i]) - arr[i]
    return trap_water

heights = [1, 0, 2, 1, 3, 1, 2, 0, 3]
print(max_rain(heights))