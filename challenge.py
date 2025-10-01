# 1.Write an function that accept a number and return its square root if its divisible by 5 or else return its reminder
def squareroot_or_reminder(number:int):
    # check if number is divisible by 5
    import math
    if number%5==0:
        return round(math.sqrt(number),2)
    else:
        return number%5


# print(squareroot_or_reminder(10))

# 2.Longest value of a dictionary ex: {"fruit":"apple","color":"green"} => "apple"
def longest_value(dic:dict):
    longest_val = ""
    longest_key = ""
    for key,value in dic.items():
        print(len(longest_val),len(value),value)
        if len(longest_val)<len(value):
            longest_val = value
    return longest_val


# print(longest_value({"fruit":"apple","color":"green"}))

# 3.Function which convert a list of string to number and add the numbers ["1","2","3"] => [1,2,3] 6
def convert_add(nums:list):
    converted_list = sum([int(num) for num in nums])
    return converted_list

# print(convert_add(["1","23","3"]))

# 4.Duplicate names in a list. if duplicates found return list of duplicate.Or else "No duplicate" ["apple","banana","apple"] => ["apple"]
def check_duplicates(sequence:list):
    duplicates = []
    seen = []
    for word in sequence:
        if word not in duplicates and word in seen:
            duplicates.append(word)
        seen.append(word)
    return duplicates if duplicates else "No"

# print(check_duplicates(["apple","apple","banana"]))

# 5.Register Check . Check the dict where student is present and return the number of students present {"peter":"Yes","albin":"No","ebin":"Yes"}=>2
def register_check(students:dict):

