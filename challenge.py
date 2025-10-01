# 1.Write an function that accept a number and return its square root if its divisible by 5 or else return its reminder
from traceback import print_tb


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
    return len([value for key,value in students.items() if value=="Yes"])

# print(register_check({"peter":"Yes","albin":"No","ebin":"Yes"}))

# 6. Lower case names : from a list of mixed names return only lower case names in descending order
def lowercase_descending(names:list):
    new_list = sorted([name for name in names if name.islower()],reverse=True)
    return new_list

# print(lowercase_descending(["Name","rasif","abc"]))

# 7.Check if 2 numbers are float and return its count if its float : ex:2,5.6 =>1
def only_floats(num1,num2):
    return sum(isinstance(num,float) for num in (num1,num2))
# print(only_floats(2.8,4))

# 8. Index of longest word:
def word_index(words:list):
    longest_word_index = 0
    longest_word = ""
    for i,word in enumerate(words):
        if len(word)>len(longest_word):
            longest_word = word
            longest_word_index = i
    return longest_word_index

# print(word_index(["inde","word","open"]))

# 9.Discoutn % of a price.Make 2 input from user as price and discoutn value.and return discount value

def my_discount(price,discount):
    return price - (price * (discount/100))

# print(my_discount(75,10))

# 10. Tuple of student sex ex:["male","female"]=>[("male",1),("female",1)]
def student_sex(list_of_sex:list):
    result = []
    for sex in list_of_sex:
        print(sex,"======")
        count = 0
        for s in list_of_sex:
            print(s,"+++++++++")
            if s==sex:
                count+=1
        if (sex,count) not in result:
            result.append((sex,count))
    return result

# print(student_sex(["male","female"]))

