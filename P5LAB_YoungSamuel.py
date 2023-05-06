# Define your function here.

def days_in_feb(user_year): 
    if user_year % 4 == 0 and user_year % 100 != 0: #Condition to check regular leap years 
        return 29
    elif user_year % 400 == 0:                      #Condition to check XX00s
        return 29
    else:                                           #Condition for non-leap years
        return 28

if __name__ == '__main__':
    year = int(input())
    day = days_in_feb(int(year))
    print(f'{year} has {day} days in February.')

    # Type your code here. Your code must call the function.