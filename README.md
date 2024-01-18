# Deadlock-Detection-in-Resource-Allocation
This project implements a deadlock detection algorithm for a system with N processes, M resources, and multiple instances of each resource. The deadlock detection is based on input matrices from CSV files representing the allocation matrix, request matrix, and available vector.

## Files

- `Allocation.csv`: Represents the NxM allocation matrix.
- `Request.csv`: Represents the NxM request matrix.
- `Available.csv`: Represents the M available vector.

  ## Prerequisites

- Python (version 3.11)
- Required Python packages (e.g., pandas)

  ## Implementation
  The functions.py script contains functions for reading CSV files, checking matrix dimensions, generating finish matrices, detecting deadlock, comparing work and requests, and printing results. The main.py script demonstrates the usage of these functions for deadlock detection.

  ## Functions

### `read_csv_files()`
- Reads the input files and returns matrices Request, Allocation, and Available.

### `check_dimension(req, alloc, avail)`
- Checks the dimensions of matrices to ensure consistency.

### `generate_finish_matrix(alloc)`
  - Generates a list indicating whether a process has finished or not.

### `detect_deadlock(work, alloc, req, finish)`
   - Detects deadlock and updates the finish list.

### `cmp_work(work, req)`
  - Compares work and request to check if a process can finish.

### `print_result(finish, num_of_threads)`
   - Prints the result in a formatted box.

## Authors

- [Mohammed Abed Alkareem](https://github.com/Mohammed-Abed-Alkareem)

