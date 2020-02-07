from statistics import mean

print("Hello from Iceland!")

scrm = open("scrambles.txt", "r")

attempts = 0
disp_count = 1
solves = 0
disp_list = []
solve_list = []

'''for var in range(1, 30):
    print(f"30/{var} with a {30 % var} remainder")'''


class MySolve:
    def __init__(self, num=1, time=0, isdnf=False, scramble=""):
        self.num = num
        self.time = time
        self.isdnf = isdnf
        self.scramble = scramble

    def write_out(self):
        print(self.time, self.isdnf, self.scramble)

    def solve_ip(self, num):
        self.time, self.isdnf = input("Enter Time then If is dnf").split()
        self.num = MySolve(self.time, self.isdnf, self.scramble)


'''s1 = MySolve()
s1.write_out()
s1.solve_ip(1)
s1.write_out()'''




# Determines if input is a float?
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def print_ave():
    # TODO change attempts to solves after logic is fixed
    print(f'Average: {mean(solve_list)} for {attempts} solves yay')


scrm = open("scrambles.txt", "r")
while attempts < 6:
    print(scrm.readline())
    str_last_solve = input(f"Solve number {str(disp_count)} Time: ")
    attempts += 1
    disp_count += 1
    # First input
    if str_last_solve != "dnf":
        last_solve = float(str_last_solve)
        confirm = input("Are You sure?").lower()
        solves += 1
        # Input confirmation
        if confirm == "no":
            last_solve = input("Solve Time: ")
            if str_last_solve == "dnf":
                last_solve = float(input("Solve Time: "))
            disp_list.append("DNF")
            count_dnf = disp_list.count("DNF")
            print(str(count_dnf) + "here i am")
            solves -= 1
        else:
            last_solve = float(last_solve)
        print(last_solve)
        solve_list.append(last_solve)
        disp_list.append(last_solve)

    elif str_last_solve == "dnf":
        confirm = input("Are You sure?").lower()
        solves -= 1
        if confirm == "no":
            str_last_solve = input("New Solve Time: ")
            if str_last_solve != "dnf":
                last_solve = float(str_last_solve)
                solves += 1
                disp_list.append(last_solve)
                solve_list.append(last_solve)
            else:
                # TODO do i need to add to solves
                disp_list.append("DNF")
                count_dnf = disp_list.count("DNF")
                print(str(count_dnf) + " here i am")
        else:
            disp_list.append("DNF")
            count_dnf = disp_list.count("DNF")
            print(str(count_dnf) + " here i am")

    #   solves -= 1
    if attempts % 3 == 0:
        print(disp_list)
        print("Last mean of 3: " + str(mean(solve_list[-3:])) + "\n")
# End of loop

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
print_ave()
# Trying to calculate accuracy
# print(solves)
print("Accuracy:")
print(solves)
print(attempts)
print(1 - (total_dnfs / attempts))
str2 = str(mean(solve_list))
save.write(str1 + " Ave: " + str2 + "\n")
save.close()

# TODO Built in stats?
# TODO data collect/store
# TODO compute data
# TODO change last item
# TODO compute accuracy
# TODO print data
# TODO saves/prints data to external .txt file
# TODO prints scrambles before timer input
# TODO how to deal with dnfs
# TODO fix counting logic for input and checks
# TODO disp list and solve list fix