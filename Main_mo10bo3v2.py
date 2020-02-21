from statistics import mean, StatisticsError

# Opens source file for scrambles.
scrambles = open("scrambles.txt", "r")
# Opens mean of 3 text file to write to.
mo3 = open("Mo3.txt", "a")
solves_txt = open("solves.txt", "a")
# Select and press alt and / to comment out multiple lines
# alt to insert multiple cursors

# Highlight a func call
# and press alt + enter it will show an option
# to add type to docstring  dont think this is useful
# Surround ctrl alt + t

# Const
num_of_solves = 3
# Init all num var
attempts = 0
solves = 0
display_count = 1
# Init all lists
display_list = []  # Stores strings
solve_list = []  # Stores floats
display_bo3 = []
solve_bo3 = []


# TODO Does ip num have to be an int or can it only be a float (minus dnfs)
# Well it can be but then you can't check for it being a dnf?
def is_float(str1):
    """Returns True if str1 is flr Specifically an int with one period"""
    isfloat = False
    if str1.count(".") == 1 or str1.replace(".", "").isdigit():
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


def while_ip(str_solve, dispcount=1):
    """Inputs string solve and display count. If the input is neither
    a 'num' nor the string 'dnf', it continues to loop."""
    low = ip_lower_str(str_solve)
    new_ip_solve = ""
    if not is_num(str_solve) and not low == "dnf":
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


while attempts < num_of_solves:
    print("\n")
    print("Scramble {}".format(display_count))
    print(scrambles.readline() + "Enter solve")
    string_solve = (input(">"))
    lower = while_ip(string_solve)
    if lower == "dnf":
        lower = lower.upper()
        display_list.append(lower)
    else:
        solves += 1
        lower = float(lower)
        display_list.append(lower)
        solve_list.append(lower)
    print("{} display list".format(display_list))
    # print("{} solve list".format(solve_list))

    # todo Print the means of mo3
    if display_count % 3 == 0:
        # TODO write the num if the mean with the stats
        mo3.write("\n")
        # Check if [-3:] in display_list contains a DNF
        # Display list is still a 'str' so it should be pretty easy to check
        dnf_in_last_3 = "DNF" in display_list[-3:]
        if dnf_in_last_3:
            lst_mo3 = "Last Mean of 3: DNF \n"
            print(lst_mo3)
            mo3.write(lst_mo3)
        else:
            print("Last Mean of 3: " + str(mean(solve_list[-3:])) + "\n")
            mo3.write("Last Mean of 3: " + str(mean(solve_list[-3:])) + "\n")
        last_3_dnf_num = display_list[-3:].count("DNF")

        # TODO print bo3 and add to a bo3 list
        if last_3_dnf_num == 3:
            display_bo3.append("DNF")
            print("Last Bo3: DNF" + "\n")
        else:
            minimum = min(solve_list[-3:])
            display_bo3.append(minimum)
            lst_bo3 = "Last Bo3: " + str(display_bo3[-1:]) + "\n"
            print(lst_bo3)
            mo3.write(lst_bo3)

    display_count += 1
    attempts += 1
# TODO print on one line
accuracy = "Accuracy: {}/{} \n".format(solves, num_of_solves)
percent = "Percent {}\n".format((solves/num_of_solves)*100)
solves_txt.write(accuracy)
solves_txt.write(percent)
# def mutate_string(string, position, character):
# string = string[:position] + character + string[position + 1:]
#     return string
# This isn't fair
# n = 12
# for i in range(1, n + 1):
#     print(i, end='')


# string.swapcase() is cool
# def split_and_join(line):
#     line = line.split(" ") # a is converted to a list of strings.
#     line = "-".join(line)
#     return line
#
def staircase(n):
    sign = n - (n - 1)
    temp = n - 1
    clock = 0
    while clock < n:
        print(" " * temp + "#" * sign)
        temp -= 1
        clock += 1
        sign += 1


def add_two_a_and_b(a, b):
    a += 2
    b += 2
    return a, b


ax, ay = add_two_a_and_b(4, 6)
# print(ax)
# print(ay)
