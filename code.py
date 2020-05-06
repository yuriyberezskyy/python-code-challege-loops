# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

# For example, consider th
# Write your function here


def exponents(lst1, lst2):
    new_list = []
    for num1 in lst1:
        for num2 in lst2:
            new_list.append(num1**num2)
    return new_list


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

# Write your function here


def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if (sum > 9000):
            break
    return sum


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
