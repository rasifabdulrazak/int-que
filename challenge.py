# 1.Write an function that accept a number and return its square root if its divisible by 5 or else return its reminder
from traceback import print_tb


def squarer_or_reminder(number:int):
    # check if number is divisible by 5
    import math
    if number%5==0:
        return round(math.sqrt(number),2)
    else:
        return number%5


# print(squarer_or_reminder(10))

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

# print(register_check({"peter":"Yes","albin":"No","febrile":"Yes"}))

# 6. Lower case names : from a list of mixed names return only lower case names in descending order
def lowercase_descending(names:list):
    new_list = sorted([name for name in names if name.islower()],reverse=True)
    return new_list

# print(lowercase_descending(["Name","massif","abc"]))

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

# print(word_index(["indie","word","open"]))

# 9.Discount % of a price.Make 2 input from user as price and discount value.and return discount value

def my_discount(price,discount):
    return price - (price * (discount/100))

# print(my_discount(75,10))

# 10. Tuple of student sex ex:["male","female"]=>[("male",1),("female",1)]
def student_sex(list_of_sex:list):
    result = {}
    for sex in list_of_sex:
        result[sex] = result.get(sex,0)+1
    return result

# print(student_sex(["male","female","male"]))

# 11.Username generator from an email : ex:ben@gmail.com => ben
def username_generator(email:str)->str:
    name = email.split("@")
    return name[0]

# print(username_generator("rasif@gmail.com"))

# 12. Zero both ends:
def zero_end(nums:list)->list:
    nums[0] ,nums[-1] = 0,0
    return nums

# print(zero_end([2,3,4,5,8]))

# 13.String range : ex: 6 => "0.1.2.3.4.5"
def string_range(num):
    return ".".join([str(i) for i in range(num)])

# print(string_range(5))

# 14.Start with "S" and return its count in dictionary
def start_with_s(names:list)->dict:
    result_dict = {}
    for name in names:
        if name.lower().startswith("s"):
            result_dict[name] = result_dict.get(name,0)+1
    return result_dict

# print(start_with_s(["sneha","sujith","lima","sneha"]))

# 15.Odd or even
def odd_or_even(nums:list):
    # even_numbers = [i for i in nums if i%2==0]
    # odd_numbers = [i for i in nums if i%2!=0]
    # largets_even_number = max(even_numbers)
    # smallest_odd_number = min(odd_numbers)
    largets_even_number = None
    smallest_odd_number = None
    for num in nums:
        if num%2==0:
            if largets_even_number is None or num > largets_even_number:
                largets_even_number = num
        else:
            if smallest_odd_number is None or num < smallest_odd_number:
                smallest_odd_number = num
    return largets_even_number - smallest_odd_number
# print(odd_or_even([1,2,4,5,6]))

# 16.List of Prime numbers
def prime_numbers(limit:int)->list:
    if limit < 2:return []
    result_list = []
    for i in range(2,limit):
        print(i,"==========")
        if limit%i!=0:
            result_list.append(i)
    return result_list

# print(prime_numbers(10))

# 17.Biggest odd number in a string:
def biggest_odd(num:str):
    list_of_num = [int(i) for i in num if int(i)%2!=0]
    return max(list_of_num)
# print(biggest_odd("1234589"))

# 18.Zeros to end of list of integers with maintaining ascending order ex: [1,0,9,9] => [1,9,9,0]
def zeros_last(nums):
    numbers = sorted([num for num in nums if num!=0])
    zeros = [0]*(len(nums)-len(numbers))
    return numbers + zeros
# print(zeros_last([1,0,9,9,8,0,0,0]))

# 19. Hide Password and return character length
def hide_password(password:str):
    len_password = len(password)
    return f'{len_password * "*" } Your password contain {len_password} characters'

# print(hide_password("rasif"))

# 20. Thousand Seperator
def thousand_seperator(num):
    return f"{num:,}"
# print(thousand_seperator(10000000))

# 21.Equal string : ex : love==olve => True
def equal_string(string1:str,string2:str):
    return sorted(string1) == sorted(string2)
# print(equal_string("love","olve"))

# 22.Swap numbers in list [1,2,3,4] => [4,2,3,1]
def swap_numbers(nums:list):
    nums[0],nums[-1] = nums[-1],nums[0]
    return nums
# print(swap_numbers([4,2,3,1,0]))

# 23.count dots ex:hel.p. => 2
def count_dots(string:str):
    return string.count(".")
# print(count_dots("hel.p."))

# 24.Age in minutes
def age_in_minutes(age):
    if age < 1900 or age > 2025:
        return "Please enter a correct age"

print(age_in_minutes(1890))