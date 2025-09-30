# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

#======Reverse and Palindrome=================
def is_palindrome(string:str)->bool:
    reversed_string = ("")
    for i in range(len(string)-1,-1,-1):
        reversed_string += string[i]
    return reversed_string == string
    # return string == string[::-1]


print(is_palindrome("mno"))
# =============================================

#========= Non Repeating Charecter (Frequecy Count)==========================
def non_repeating_char(string:str):
    result_dict = {}
    for char in string:
        result_dict[char] = result_dict.get(char,0) + 1
    final_result = {key:value for key,value in result_dict.items() if value==1}
    return final_result

print(non_repeating_char("string"))
# =====================================================

# ========Remove duplicate and maintain order==========
def remove_duplicate(string:str):
    seen = set()
    result = []
    for i in string:
        if i not in seen:
            result.append(i)
            seen.add(i)
    result_in_word = "".join(result)
    print(result)
    return result_in_word

print(remove_duplicate("geeeks"))
# ====================================

# =======All substring of a string=========
def longest(substring):
    size = 0
    string = ""
    for i in substring:
        if len(i)>size:
            size = len(i)
            string = i
    return string

def substring(string:str):
    result = []
    size = len(string)
    for i in range(size):
        for j in range(i,size):
            result.append(string[i:j+1])
    long = longest(set(result))
    print(long)
    return set(result)

print(substring("aab"))
# ================================

# ============Longest Unique Substring===================
def longest_unique_substring(string):
    seen = {}
    left = 0
    max_len = 0
    for key,value in enumerate(string):
        print("index=",key,"value=",value,"left=",left,"max_len=",max_len,"seen=",seen)
        if value in seen and seen[value]>=1:
            left = seen[value]+1
        seen[value] = key
    max_len = max(max_len,key-left+1)
    return max_len

print(longest_unique_substring("posdkod"))
# =======================================================

# =====Second largest number of a list==========
def second_largest(nums):
    largest,second_largest = 0,0
    for val in nums:
        print("val=",val,"largets=",largest,"sclar=",second_largest)
        if val > largest:
            second_largest = largest
            largest = val
        elif val>=second_largest and val!=largest:
            second_largest = val
    return largest,second_largest
print(second_largest([1,23,3]))
# ================================

# ===Prime Number=========
# def list_prime(size):
#     if size <= 1:return "None"
#     for i in range(size):
#         if
#     pass
def check_prime(num):
    if num <= 1:return "Not Prime"
    for i in range(2,num):
        if num%i==0:
            return "Not Prime"
    return "Prime"
print(check_prime(9))
# =========================

# Remove Duplicates==========
def remove_duplicate(nums):
    seen = []
    for i in nums:
        if i not in seen:
            seen.append(i)
    return seen
print(remove_duplicate([1,2,3,1]))
# ============================

# Self==================
class A():
    def __init__(self):
        pass

a = A()
print(a)
# =======================

# Decorator===================
def wrapper(func):
    def inner(*args):
        result = func(*args)
        return result.lower()
    return inner

def splits(func):
    def inner(*args):
        result = func(*args)
        print(result)
        return result.split()
    return inner

@splits
@wrapper
def hel(name):
    return "HELLO " + name

print(hel("RASIF"))
# =============================

#=============== 2 Sum====================
def sum_of_two(nums,target):
    seen_dict = {}
    for num in nums:
        print(seen_dict)
        if target - num in seen_dict:
            return (seen_dict[target-num],num)
        seen_dict[num] = num
    print(seen_dict)
    return "Not Found"

print(sum_of_two([1,2,3,9],6))
# ======================================




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
