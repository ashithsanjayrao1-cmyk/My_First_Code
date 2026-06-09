# def say_name():
#     print("Ashith")
   
# def add_borders(func):
#     print("******")
#     func()
#     print("**********")
    
# add_borders(say_name)

# def add_borders(func):

#     def wrapper():
#         print("*******")
#         func()
#         print("*****")

#     return wrapper

# @add_borders
# def say_name():
#     print("ASHITH")

# say_name()

import time

def slow_down(func):

    def wrapper():
        print("Ashith")
        time.sleep(2)
        func()
    return wrapper

@slow_down
def fetch_data():
        print("Data Fetched")
    
fetch_data()
