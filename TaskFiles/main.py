import functions

request, allocation, available = functions.read_csv_files()


functions.check_dimension(request, allocation, available)

finish = functions.generate_finish_matrix(allocation)

work = available[0]

finished_list = functions.detect_deadlock(work, allocation, request, finish)

if len(finished_list) == len(allocation):
    print("There is no deadlock ^_^")

functions.print_result(finished_list, len(allocation))
