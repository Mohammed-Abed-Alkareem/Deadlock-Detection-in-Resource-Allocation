from functions import *

request, allocation, available = read_csv_files()


check_dimension(request, allocation, available)

finish = generate_finish_matrix(allocation)

work = available[0]

finished_list = detect_deadlock(work, allocation, request, finish)

if len(finished_list) == len(allocation):
    print("There is no deadlock ^_^")

print_result(finished_list, len(allocation))

print_resources(work)
