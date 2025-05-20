# Day-5 >> Function , Global & Local Variable, Practice Problem

# Function ------ :

def my_first_function():
    return "hello! World"


# print(my_first_function())

# Parameter >> Arguments
# return


def new_fun(a, b ):
    return a + b


# print(new_fun(10 , 20))

# key = value

def new_function(kid1, kid2, kid3):

        print(f"Hey {kid2}")


# new_function(kid1= "Tahsin", kid2="Rup", kid3="Proxima IT")


# Default Parameter Value

def country_name(country = 'Bangladesh'):
    print(f"My country name is {country}")


# country_name("Argentina")

# Return ____

def myFun(x , y):
    return x + y

# my_sum = myFun(10, 20) * 2
# print(my_sum)

# Practice_Problem -1:

def greet(name):
    return f"Hello, {name}! Welcome to the Bootcamp."

print(greet("Rup"))

# Global Variable & Local Variable

global_variable = 10

def sum_function(num):
    local_variable = 20
    return global_variable * num , local_variable



reult = sum_function(2)
print(reult)

# print(global_variable)