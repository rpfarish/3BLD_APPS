from statistics import mean, StatisticsError

# Opens source file for scrambles.
scrambles = open("scrambles.txt", "r")
# Opens mean of 3 text file to write to.
mo3 = open("Mo3.txt", "a")
# Select and press alt and / to comment out multiple lines
# ctrl alt shift to insert multiple cursors

# Highlight a func call
# and press alt + enter it will show an option
# to add type to docstring  dont think this is useful


# Init all num var
attempts = 0
solves = 0
display_count = 1
# Init all lists
display_list = []
solve_list = []


# TODO Does ip num have to be an int or can it only be a float (minus dnfs)
# Well it can be but then you can't check for it being a dnf?
def is_float(str1):
    """Returns True if str1 is float. Specifically an int with one period"""
    isfloat = False
    if str1.count(".") == 1 and str1.replace(".", "").isdigit():
        isfloat = True
    return isfloat


def ip_num(str2):
    """Casts str2 as a float if it can be a float or is decimal"""
    if is_float(str2) or str2.isdecimal():
        str2_float = float(str2)
        return str2_float


def is_num(str3):
    """Returns True if the input str con be a float or if it is decimal
    (a num that is not a float or is alphanumeric text or is complex)"""
    is_number = False
    if is_float(str3) or str3.isdecimal():
        is_number = True
    return is_number


def ip_lower_str(str4):
    """ Function returns the string.lower if the input is a string
    Input can be a float(if type is a str)."""
    if isinstance(str4, str):
        lower_case = str4.lower()
        return lower_case


def append_float(num):
    """Appends both the display list (cont DNFs) and
        solve list (does not cont DNFs)"""
    solve_list.append(num)
    display_list.append(num)


def while_ip(string_solve, dispcount=1):
    """Inputs string solve and display count. If the input is neither
    a 'num' nor the string 'dnf', it continues to loop."""
    low = ip_lower_str(string_solve)
    new_ip_solve = ""
    if not is_num(string_solve) and not low == "dnf":
        while not is_num(new_ip_solve) and not low == "dnf":
            new_ip_solve = input(f"Enter solve {dispcount}: ")
            low = ip_lower_str(new_ip_solve)
        return low


# display_count += 1212
# print(while_ip("", display_count))


def display_mean(solves_lst):
    # TODO Figure out bo3 means and if total ave of non-dnfs is good
    # TODO doesn't filter out dnfs
    try:
        flt = [float(i) for i in solves_lst]
        print(f'Average: {mean(flt)} for {attempts} solves yay')
    except StatisticsError:
        print("StatisticsError:", solves_lst)
    except TypeError:
        print("TypeError: can't convert type 'str' to numerator/denominator")


# TODO Print means bo3 with the mean number
# TODO Print the Accuracy of the Bo3s, total solves and the Mo3s
# TODO Print the Accuracy
# TODO Print the num of successes af each mo3 after it
# TODO Print the means of bo3s and of mo3s
# TODO Maybe add a good note func (Called analyze?)
# Only add num to solve list
display_list.append("23")
attempts += 1
display_list.append("DNF")
attempts += 1
display_list.append("23")
attempts += 1

display_mean(solve_list)
attempts = 0

while attempts < 3:
    print("I Love you Mom")
    attempts += 1
