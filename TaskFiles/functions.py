import pandas as pd


def read_csv_files():
    """Function to read CSV files and return the matrices  Request, Allocation, and Available"""
    try:
        # Read the CSV file, drop the first column, and convert to a list of lists
        req = pd.read_csv('csv_files/Request.csv').iloc[:, 1:].fillna(0).values.tolist()
        # Read the CSV file, drop the first column, and convert to a list of lists
        alloc = pd.read_csv('csv_files/Allocation.csv').iloc[:, 1:].fillna(0).values.tolist()
        # Read the CSV file and convert to a list of lists
        avail = pd.read_csv('csv_files/Available.csv').fillna(0).values.tolist()
        return req, alloc, avail
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure the CSV files are in the correct directory.")
        exit(1)


def check_dimension(req, alloc, avail):
    """ Function to check dimensions of matrices"""

    # Check if the number of processes is the same in req and alloc
    if len(req) != len(alloc):
        raise ValueError("Number of threads in Request and Allocation matrices do not match.")

    if not (len(avail[0]) == len(req[0]) and
            len(avail[0]) == len(alloc[0])):
        raise ValueError("number of resources does not match in the matrices")

    print("\nThere is no errors with the dimensions ^_^\n")
    print("Dimensions of Request Matrix:", len(req), "x", len(req[0]))
    print("Dimensions of Allocation Matrix:", len(alloc), "x", len(alloc[0]))
    print("Dimensions of Available Matrix:", len(avail), "x", len(avail[0]), "\n")


def generate_finish_matrix(alloc):
    """Function to generate a list indicating whether a process has finished or not"""
    false_list = []

    for i in range(len(alloc)):
        bool_var = True

        for j in range(len(alloc[0])):
            if alloc[i][j] != 0:
                bool_var = False
                continue

        false_list.append(bool_var)

    return false_list


def detect_deadlock(work, alloc, req, finish):
    """Function to detect deadlock and update the finish list"""
    finished_list = []

    i = 0
    while i < len(req):
        if i not in finished_list:
            if not finish[i]:
                if cmp_work(work, req[i]):
                    finish[i] = True
                    finished_list.append(i)
                    for k in range(len(work)):
                        work[k] += alloc[i][k]
                    i = 0  # Restart the loop from the beginning
                else:
                    i += 1  # Move to the next iteration
        else:
            i += 1  # Move to the next iteration if (i) is in finished_list

    return finished_list


def cmp_work(work, req):
    """Function to compare work and request to check if a process can finish"""

    for i in range(len(req)):
        if work[i] < req[i]:
            return False

    return True


def print_result(finish, num_of_threads):
    # Function to print a line of the box
    def print_box_line(line):
        print(f"+{'-' * (len(line) + 2)}+")
        print(f"| {line} |")
        print(f"+{'-' * (len(line) + 2)}+")

    if len(finish) != 0:
        processes_line = f"Non-deadlocked processes: P{finish[0] +1}"

        for i in finish[1:]:
            processes_line += f" -> P{i +1}"

        print_box_line(processes_line)

        for i in range(num_of_threads):
            if i not in finish:
                print_box_line(f"P{i +1} deadlocked *_*")

    else:
        print_box_line("All Processes are Deadlocked *_*")


def print_resources(work):
    ascii_value = 65
    print("\nAvailable resources:")
    for resource in work:
        print(f"Resource {chr(ascii_value)}: {resource}\t", end="")
        ascii_value += 1
    print()
