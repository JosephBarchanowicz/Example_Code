# C-project-files
My project files using C code

## Banker's Algorithm 
Bankers Algorithm is a dynamic deadlock avoidance algorithm which is used to check for deadlock by trying to satisfy the needs for all the processes.  
##### Purpose:  
To implement resource allocation and demonstrate deadlock avoidance using the Banker's algorithm.
#### Specification:
The program simulates resource allocation to requesting processes and demonstrates deadlock avoidance with the Banker's algorithm. A menu controls the operations, and each choice calls the appropriate procedure, where the choices are:
1) Enter parameters
2) Run the Banker's algorithm to determine a safe sequence
3) Quit program and free memory

## Batch Process Scheduling
Batch process performs a long-running and generally repetitive task that does not require any intervention from the user.
##### Purpose:
To calculate the timing parameters of batch processes based on different scheduling algorithms.  
#### Specification:
The program mimics the execution of different processes under different scheduling algorithms. The simulation maintains a table that reflects the current state of the system, based on choosing from a menu of choices, where each choice calls the appropriate procedure, where the choices are:
1) Enter parameters
2) Schedule processes with FIFO algorithm
3) Schedule processes with SJF algorithm
4) Schedule processes with SRT algorithm
5) Quit program and free memory

## Disk Scheduling
The simplest approach to disk scheduling is to service all requests in first in first out (FIFO) order, which is the order of arrivals.  
The Shortest seek time first (SSTF) scheduling algorithm considers the list of all pending requests and always selects the request that requires the shortest travel distance from the current position.  
The Scan scheduling algorithm mimics the behavior of an elevator in a building.  
The C-Scan scheduling algorithm is a variant of the Scan algorithm that services requests in only one direction.  
#### Purpose:
To compare the performance of disk scheduling algorithms: First-in-first-out (FIFO), Shortest-seek-time-first (SSTF), Scan, and C-Scan.
#### Specification:  
The program compares the disk scheduling algorithms: First-in-first-out (FIFO), Shortest-seek-time-first (STTF), Scan, and C-Scan in terms of traversing a set of tracks input by the user, and calculates the total distance of the tracks traversed.  
A menu controls the operations, and each choice calls the appropriate procedure, where the choices are:
1) Enter parameters
2) Calculate distance to traverse tracks using FIFO
3) Calculate distance to traverse tracks using SSTF
4) Calculate distance to traverse tracks using Scan
5) Calculate distance to traverse tracks using C-Scan
6) Quit program and free memory

## Memory Allocation Algorithms
First-fit always starts the search from the beginning of the list and allocates the first hole large enough to accommodate the request.  
Best-fit searches the entire list and chooses the smallest hole large enough to accommodate the request.
#### Purpose:  
To simulate memory allocation with hole-fitting algorithms (First-fit, Best-fit) and implement deallocation and defragmentation of memory blocks.
#### Specification:
The program simulates memory allocation with a chosen hole-fitting algorithm (First-fit, Best-fit) and implements deallocation and defragmentation. A menu controls the operations, and each choice calls the appropriate procedure, where the choices are:
1) Enter parameters
2) Allocate memory for a block
3) Deallocate memory for a block
4) Defragment memory
5) Quit program and free memory

## Process Creation Hierarchy  
Process Creation Hierarchy is a graphical representation of the dynamically changing parent-child relationships among all processes.  
#### Purpose: 
To simulate the process creation and destruction when implemented with linked lists.
#### Specification:
The program creates/destroys child processes based on choosing from a menu of choices, where each choice calls the appropriate procedure, where the choices are:
1) Enter parameters
2) Create a new child process
3) Destroy all descendants of a process
4) Quit program and free memory
