"""
Por Medina Peraza Caleb
6/05/2021

(Note to self> in python, within a function, put ALL relevant code inside try-except. Otherwise, if part of the code is inside of try, and another outside, and outside calls other functions and maybe there's an if check, unexpected behaviour may happen. Please spare yourself the headache of hunting your mistakes!)
"""
import math
# <global variables>
header_list = ["#", "x_i", "x_u",
               "f(x_i)", "x_r", "f(x_r)", "E_a", "E_r (%)", "Sign"]
var_list = []
# <state variables>
x_i = 0
x_u = 0
fx_i = 0
x_r = 0
x_r_temp = 0
fx_r = 0
E_r = 0  # Relative error (%)
E_a = 0  # Absolute eror
sign = ""
# </state variables>
# <control variables>
iter = 0
max_error = 0
string = ""
# </control variables>
# </global variables>


def print_table():
    # keyword global allows functions to change global variables
    global x_i
    global x_u
    global fx_i
    global x_r
    global x_r_temp
    global fx_r
    global E_r
    global E_a
    global sign
    global var_list
    # <Stop criteria variables>
    global iter
    global max_error
    global string
    flag = True
    counter = 0
    # </Stop criteria variables>

    for item in header_list:
        # column formatting. {column(number or item) : number of spaces or width}
        # > align to the right, < align to the left
        # end="", what to print at the end. Default is '\n'
        print(f"{item: >14}", end="")

    print("\n")

    # calculate values for table, while the flag is true (conditionals can change it to false). Always gives aproximations.
    # x_r approaches root. As it approaches, f(x_r) comes closer to 0
    while flag == True:
        var_list.append(counter)
        var_list.append(x_i)
        var_list.append(x_u)

        fx_i = function(string, x_i)
        fx_i = truncate(fx_i, 7)
        var_list.append(fx_i)

        x_r = (x_i + x_u)/2  # bisection formula
        E_a = abs(x_r - x_r_temp)
        E_r = relative_error(x_r, x_r_temp)
        x_r_temp = x_r
        x_r = truncate(x_r, 7)
        E_a = truncate(E_a, 7)
        E_r = truncate(E_r, 7)
        # <Stop conditional by error>
        if E_r < max_error:
            flag = False
        # </Stop conditional by error>
        E_r = str(E_r) + " %"
        var_list.append(x_r)

        fx_r = function(string, x_r)
        fx_r = truncate(fx_r, 7)
        var_list.append(fx_r)

        var_list.append(E_a)
        var_list.append(E_r)

        # x_u becomes ceiling or upper limit:
        if (function(string, x_i)*function(string, x_r) < 0):
            x_u = x_r
            sign = "-"
            var_list.append(sign)
        # x_i becomes floor or lower limit:
        elif (function(string, x_i)*function(string, x_r) > 0):
            x_i = x_r
            sign = "+"
            var_list.append(sign)
        # in the rare event of finding the exact root, print last result and stop iterating:
        else:
            sign = "null"
            var_list.append(sign)
            for item in var_list:
                print(f"{item:>14}", end=" ")
            break

        x_i = truncate(x_i, 7)
        x_u = truncate(x_u, 7)
        # print current result row:
        for item in var_list:
            print(f"{item:>14}", end=" ")
        print("\n")
        # clear result row (array) to store the next batch:
        var_list = []
        # <Stop conditional by iterations>
        counter += 1
        if counter == iter:
            flag = False
        # </Stop conditional by iterations>

    iter = counter


def print_result():
    global iter
    global E_r
    print("\n")
    if iter == 0:
        iter += 1
    if E_r == "100.0 %":
        E_r = "null"
    print(
        f"Aproximate root is {x_r}, with error of {E_r}, on iteration {iter-1}.\n")

# Absolute (relative, in %) error function:


def relative_error(x_r, x_r_temp):
    # x_r can return 0. If not 0, then:
    if (x_r != 0):
        E_r = abs((x_r - x_r_temp) / x_r)*100
        return E_r
    # however, if x_r = 0, to avoid an error in E_r (as NoneType), return 100
    # which is our 'null' value for Error
    else:
        return 100


def limits_input():
    global x_i, x_u

    try:
        # use float for decimal limits
        x_i = float(input(f"Input lower limit x_i: "))
        x_u = float(input(f"Input upper limit x_u: "))

        if (function(string, x_i)*function(string, x_u) >= 0):
            print(
                "Limits dont't bracket any root (f(x_i) * f(x_u) > 0). Input again until product is < 0.\n")
            limits_input()

        print("\n")
    except:
        print("\nOnly input integer or float numbers please!")
        limits_input()


def stop_criteria():
    global iter
    print("Select the stop criteria by inputting the number:")
    print("1. By number of iterations")
    print("2. By maximum error")

    try:
        select = int(input("Your selection: "))

        print("\n")
        if select == 1:
            num_of_iterations()
        elif select == 2:
            max_error_input()
        else:
            print("Only input 1 or 2!")
            stop_criteria()
    except:
        print("\nOnly input integers, and only 1 or 2!")
        stop_criteria()


def max_error_input():
    global max_error

    try:
        max_error = float(
            input("Input the maximum error allowed, between 0 and 100: "))
        if max_error <= 0 or max_error >= 100:
            print("\nError must be between 0 and 100%. Input error again.")
            max_error_input()
        print("\n")
    except:
        print("\nOnly input integer or float numbers please!")
        max_error_input()


def num_of_iterations():
    global iter

    try:
        iter = int(input("Input the number of iterations for bisection method: "))
        print("\n")
    except:
        print("\nOnly input integers please!")
        num_of_iterations()


def function(string, m):
    # We take a string, and a numerical value 'm'
    # Since the math expression in the string only recognizes 'n' as a variable,
    # the value in 'm' is assigned to 'n' within this method
    # Then, the eval() function evaluates the string as python code
    # in this case, a math expression, and returns the result.
    n = m
    return eval(string)


def function_input():
    global string
    string = input("Please input a math expression with 'n' variable, with python syntax (for math expressions such as euler 'e', sine, cosine, etc., prepend with 'math.'; e.g. math.exp()).\nYour answer: ")
    print("\n")


def try_again():
    answer = input("Try again? (y/n): ")
    if answer.lower() == "y":
        print("\n----------------------------------------------------------------------------------------------------------------------------------->\n")
        init()
    elif answer.lower() == "n":
        exit()
    else:
        print("Please give either 'y' or 'n'.\n")
        try_again()


def restart_variables():
    global x_i
    global x_u
    global fx_i
    global x_r
    global x_r_temp
    global fx_r
    global E_r
    global E_a
    global sign
    global var_list
    # <Stop criteria variables>
    global iter
    global max_error
    global string
    # </Stop criteria variables>

    # <global variables>
    var_list = []
    # <state variables>
    x_i = 0
    x_u = 0
    fx_i = 0
    x_r = 0
    x_r_temp = 0
    fx_r = 0
    E_r = 0  # Relative error (%)
    E_a = 0  # Absolute eror
    sign = ""
    # </state variables>
    # <control variables>
    iter = 0
    max_error = 0
    string = ""
    # </control variables>
    # </global variables>

# this funtion truncates the decimal places to a more manageable amount


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def init():
    restart_variables()
    function_input()
    limits_input()
    stop_criteria()
    print_table()
    print_result()
    try_again()


init()
