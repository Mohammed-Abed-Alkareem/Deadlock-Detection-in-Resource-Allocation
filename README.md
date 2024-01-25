# Deadlock-Detection-in-Resource-Allocation
This project implements a deadlock detection algorithm for a system with N processes, M resources, and multiple instances of each resource. The deadlock detection is based on input matrices from CSV files representing the allocation matrix, request matrix, and available vector.

## Files

- `Allocation.csv`: Represents the NxM allocation matrix.
- `Request.csv`: Represents the NxM request matrix.
- `Available.csv`: Represents the M available vector.

  ## Prerequisites

- Python (version 3.11)
-  Required Python packages:
  - pandas

## Setup
1. **Clone the Repository**
   - Clone or download this project to your local machine.

2. **Install Dependencies**
   - Ensure Python 3.11 is installed.
   - Install required Python packages: `pip install pandas`

3. **Place CSV Files**
   - Ensure `Allocation.csv`, `Request.csv`, and `Available.csv` are placed in the project directory.

## Usage
 **Run the Main Script**
   - Execute `main.py` to start the deadlock detection process.
   - `python main.py`


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

## Example CSV Content

### Allocation.csv

| Process | ResourceA | ResourceB | ResourceC | ResourceD | ResourceE |
|---------|-----------|-----------|-----------|-----------|-----------|
| P1      | 5         | 6         | 0         | 3         | 1         |
| P2      | 1         | 0         | 6         | 5         | 4         |
| P3      | 2         | 4         | 1         | 0         | 2         |
| P4      | 4         | 3         | 2         | 0         | 4         |
| P5      | 6         | 2         | 3         | 2         | 2         |
| P6      | 1         | 1         | 3         | 2         | 3         |
| P7      | 0         | 0         | 5         | 1         | 1         |
| P8      | 0         | 5         | 7         | 3         | 0         |
| P9      | 2         | 6         | 0         | 5         | 0         |
| P10     | 3         | 7         | 1         | 6         | 2         |


### Request.csv

| Process | ResourceA | ResourceB | ResourceC | ResourceD | ResourceE |
|---------|-----------|-----------|-----------|-----------|-----------|
| P1      | 2         | 0         | 4         | 5         | 5         |
| P2      | 3         | 4         | 2         | 2         | 3         |
| P3      | 0         | 3         | 3         | 4         | 4         |
| P4      | 1         | 2         | 1         | 1         | 2         |
| P5      | 3         | 1         | 4         | 4         | 1         |
| P6      | 2         | 5         | 5         | 3         | 4         |
| P7      | 0         | 3         | 2         | 2         | 3         |
| P8      | 2         | 2         | 1         | 1         | 2         |
| P9      | 3         | 1         | 6         | 0         | 1         |
| P10     | 5         | 0         | 3         | 3         | 4         |


### Available.csv

| ResourceA | ResourceB | ResourceC | ResourceD | ResourceE |
|-----------|-----------|-----------|-----------|-----------|
| 2         | 0         | 2         | 1         | 3         |


## Output Screenshot
![Deadlock Detection Output](https://user-images.githubusercontent.com/.../screenshot.png)

## Authors

- [Mohammed Abed Alkareem](https://github.com/Mohammed-Abed-Alkareem)

