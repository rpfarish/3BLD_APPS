from statistics import mean, StatisticsError

print("Hello from Iceland! Hello from Greenland!")

scrm = open("scrambles.txt", "r")
mo3 = open("Mo3.txt", "a")

attempts = 0
disp_count = 1
solves = 0
disp_list = []
solve_list = []
lower = ""
last_solve = []
flt_list = []


# Determines if input is a float?
def is_float(s):
    """Returns True if s is a float. Specifically a int with one period"""
    print("is_float gets run")
    result = False
    if s.count(".") == 1:
        if s.replace(".", "").isdigit():
            result = True
    return result


def ip_num(string):
    if is_float(string) or string.isdecimal():
        last = float(str_solve)
        print("ip_num gets run")
        return last


def is_num(str3):
    """Returns True if the input str con be a float or if it is decimal
    (a num that is not a float or is alphanumeric text or is complex)"""
    is_number = False
    if is_float(str3) or str3.isdecimal():
        is_number = True
    return is_number


# ip_lower_str
def ip_str(is_str):
    """ Function returns the string.lower if the input is a string"""
    print("ip_str gets run")
    if isinstance(is_str, str):
        lower_case = is_str.lower()
        return lower_case


def append_float(num):
    """Appends both the display list (cont DNFs) and
        solve list (does not cont DNFs)"""
    print("append_float gets run")
    solve_list.append(num)
    disp_list.append(num)


# TODO this FUNCTION IS LKEUNLJWNVDWKJNDC! Dnf wrecks it.
def while_ip(str_slv, low, dsp_cnt):
    """Inputs string solve and display count. If the input is neither
    a float or the string dnf"""
    print('while_ip gets run')
    while not is_num(str_slv) and not low == "dnf":
        str_slv = input(f"Enter solve {dsp_cnt}:")
        print("This prints low before ip_str" + low)
        low = ip_str(str_slv)
        print("This prints low after ip_str" + low)
        print("print me")
        print(type(low))
    # Returns a decimal, float or "dnf"
    return str_slv


def print_ave(slv):
    """Prints the average of a list. Takes a list and loops through it and each item is equal to dnf then it adds a num
    if the num is equal the len of the list then print the Average is DNF"""
    global total_dnfs
    print("print total dnfs")
    print(total_dnfs)
    temp1 = 0
    flt = [float(i) for i in slv]
    print(flt)
    try:
        print(f'Average: {mean(flt)} for {attempts} solves yay')
    except StatisticsError:
        print(f'Average: DNF for {attempts} solves yay')


while attempts < 3:
    # TODO How to loop input until correct
    print(scrm.readline())
    str_solve = input(f"Enter solve {disp_count}:")

    lower = ip_str(str_solve)

    # Prompts until user ip that Returns a decimal, float or "dnf"
    # var = while_ip(str_solve, lower, disp_count)

    if is_float(str_solve):
        last_solve = float(str_solve)

    print("in the middle of the while loop")
    attempts += 1
    solves += 1
    disp_count += 1
    print("after this lower is printed")
    print(lower)
    if lower != "dnf":
        print("when lower is not  dnf This code gets run")
        disp_list.append(str_solve)
        solve_list.append(str_solve)
        print(disp_list)
        print(solve_list)
    elif lower == "dnf":
        disp_list.append("DNF")
        print(disp_list)

    if attempts % 3 == 0:
        # flt list is really only for the case when there where no dnfs in the last 3 solves
        flt_list = [float(i) for i in solve_list]
        print("This prints flt_list", flt_list)
        print(type(flt_list))
        print(len(flt_list))
        print(len(disp_list))
        # need to figure out how many dnfs were in the last three solves
        totdnf = len(disp_list[-3:])-len(flt_list)
        print(totdnf != len(disp_list))
        dnf_list = disp_list[-3:]
        print(disp_list)
        if totdnf != len(disp_list) and totdnf < 1:
            print("Last mean of 3: " + str(mean(flt_list[-3:])) + "\n")
            str2 = str1 = ', '.join(str(e) for e in dnf_list)
            # Should have written these next 2 lines in 1
            mo3.write(str2)
            mo3.write(" Last mean of 3: " + str(mean(flt_list[-3:])) + "\n")
        else:
            print("Last mean of 3: DNF \n")
            # TODO What is this doing?
            str2 = str1 = ', '.join(str(e) for e in dnf_list)
            mo3.write(str2)
            mo3.write(" Last mean of 3: DNF \n")

mo3.close()

save = open("solves.txt", "a")
str1 = ', '.join(str(e) for e in disp_list)

print("Solves saved to text file.")

dnf_input = disp_list.count("DNF")
dnf_num_confirm = disp_list.count("dnf")
total_dnfs = dnf_num_confirm + dnf_input
try:
    disp_list.remove("DNF")
except ValueError:
    print("You got no DNFs!")

print(solve_list)
print_ave(solve_list)
# Trying to calculate accuracy
# print(solves)
print("Accuracy:")
print(1 - (total_dnfs / attempts))
flt_list = [float(i) for i in solve_list]
try:
    str2 = str(mean(flt_list))
    save.write(str1 + " Ave: " + str2 + "\n")
except StatisticsError:
    save.write(str1 + " Ave: DNF" + "\n")

save.close()

# TODO Built in stats?
# TODO data collect / store
# TODO compute data
# TODO change last item
# TODO compute accuracy
# TODO print data
# TODO saves / prints data to external .txt file
# TODO prints scrambles before timer input
# TODO how to deal with dnfs
# TODO fix counting logic for input and checks
# TODO disp list and solve list fix
print(is_num.__doc__)

print(type(total_dnfs))