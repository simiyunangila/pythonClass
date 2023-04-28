
 

def my_country(country="Rwanda"):
    print(f"I am from {country}")
def greet(*names):
        for name in names:
            print(f"Hello {name}") 
def sum (*numbers):
    anwer=0
    for number in numbers:
        anwer+=number
    return anwer 
def multiply(*num):
    result=1
    for nums in num:
        result*=nums
    return result
def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")  
        
# A function named concatenate_args that takes any number of string arguments in positional 
# arguments format and concatenates them into a single string
def concatenate_args(*numbs):
    stmt=""
    for words in numbs:
        stmt+=" "+words
        words
    return stmt    
# A function named concatenate_kwargs that takes any number of string arguments in keyword 
# arguments  format and concatenates them into a single string 
def concatenate_kwargs(**sentence):
    product=""
    for key, value in sentence.items():
        product+=" "+value
    return product   