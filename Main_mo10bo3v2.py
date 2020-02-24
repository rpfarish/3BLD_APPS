from statistics import mean, StatisticsError
import gui_display_stats as gui

# TODO add functionality to be able to dnf and record the time
#  TODO Create a set of files every new session?
# TODO Open and print using turtle a chart of stats
# Opens source file for scrambles.
scrambles = open("scrambles.txt", "r")
# Opens mean of 3 text file to write to.
mo3 = open("Mo3.txt", "a")
solves_txt = open("solves.txt", "a")


# Select and press alt and / to comment out multiple lines
# alt to insert multiple cursors

# Highlight a func call
# and press alt + enter it will show an option
# to add type to docstring, don't think this is useful
# Surround ctrl alt + t


def start():
    num_of_solves = 30
    attempts = 0
    solves = 0
    display_count = 1
    num_of_mean = 0

    display_list = []  # Stores strings
    solve_list = []  # Stores floats
    display_bo3 = []
    solve_bo3 = []

    def is_float(str1):
        """Returns True if str1 is flr Specifically an int with one period"""
        isfloat = False
        if str1.count(".") == 1 or str1.replace(".", "").isdigit():
            isfloat = True
        return isfloat

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

    def while_ip(str_solve, disp_count=1):
        """Inputs string solve and display count. If the input is neither
        a 'num' nor the string 'dnf', it continues to loop."""
        low = ip_lower_str(str_solve)
        new_ip_solve = ""
        if not is_num(str_solve) and not low == "dnf":
            while not is_num(new_ip_solve) and not low == "dnf":
                new_ip_solve = input(f"Enter solve {disp_count}: ")
                low = ip_lower_str(new_ip_solve)
        return low

    def display_mean(solves_lst):
        """Averages all non-dnf solves"""
        try:
            flt = [float(i) for i in solves_lst]
            return f'Average: {mean(flt)} for {attempts} solves yay'
        except StatisticsError:
            print("StatisticsError:", solves_lst)
        except TypeError:
            print("TypeError: can't convert type 'str' to numerator/denominator")

    # TODO Maybe add a good note func (Called analyze?)

    while attempts < num_of_solves:
        print("Scramble {}".format(display_count))
        print(scrambles.readline() + "Enter solve")
        string_solve = (input(">"))
        lower = while_ip(string_solve, display_count)
        if lower == "dnf":
            lower = lower.upper()
            display_list.append(lower)
        else:
            solves += 1
            lower = float(lower)
            solve_list.append(lower)
            display_list.append(lower)
        print("{} display list".format(display_list[-12:]))

        if display_count % 3 == 0:
            num_of_mean += 1
            mo3.write("\n")
            mo3.write(f"Mean of 3 #{num_of_mean}:\n")
            mo3.write(f"{display_list[-3:]}\n")
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
            # TODO reduce into a function
            if last_3_dnf_num == 3:
                display_bo3.append("DNF")
                last_bo3 = "Last Bo3: DNF" + "\n"
                print(last_bo3)
                mo3.write(last_bo3)
            elif last_3_dnf_num == 0:
                minimum = min(solve_list[-3:])
                display_bo3.append(minimum)
                solve_bo3.append(minimum)
                lst_bo3 = "Last Bo3: " + str(display_bo3[-1:]) + "\n"
                print(lst_bo3)
                mo3.write(lst_bo3)
            elif last_3_dnf_num == 1:
                minimum = min(solve_list[-2:])
                display_bo3.append(minimum)
                solve_bo3.append(minimum)
                lst_bo3 = "Last Bo3: " + str(display_bo3[-1:]) + "\n"
                print(lst_bo3)
                mo3.write(lst_bo3)
            elif last_3_dnf_num == 2:
                minimum = min(solve_list[-1:])
                display_bo3.append(minimum)
                solve_bo3.append(minimum)
                lst_bo3 = "Last Bo3: " + str(display_bo3[-1:]) + "\n"
                print(lst_bo3)
                mo3.write(lst_bo3)
        print("\n")
        display_count += 1
        attempts += 1

    accuracy = "Accuracy: {}/{} \n".format(solves, num_of_solves)
    # TODO
    percent = "Percent {}\n".format((solves / num_of_solves) * 100)
    mean_of_all_solves = display_mean(solve_list)
    mo3.write(mean_of_all_solves)
    solves_txt.write(accuracy)
    solves_txt.write(percent)

    solves_txt.write(f"Mean of Bo3: {mean(solve_bo3)}\n\n")
    return solve_bo3, display_list, display_count, num_of_solves


bo3, display_list, display_count, num_of_solves = start()

# This is the end of the file
gui.window()
gui.draw_grid(600, 300, -300, -25)

disp = 0
lines = 0
x_coord = -275
y_coord = 248
loop_num = 0
list_num = 0
pointer = False
while lines < num_of_solves // 3:
    lines += 1
    if pointer:
        pointer = False
        disp = 0
    while disp < 3:
        gui.draw_num(display_list[list_num], x_coord, y_coord, size=15)
        list_num += 1
        disp += 1
        x_coord += 45
        if disp % 3 == 0:
            pointer = True
            y_coord -= 30
            x_coord = -275


# gui.draw_num(display_list[0], -275, 250, size=15)
# gui.draw_num(display_list[1], -230, 250, size=15)
# gui.draw_num(display_list[2], -185, 250, size=15)

gui.keep_open()


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
