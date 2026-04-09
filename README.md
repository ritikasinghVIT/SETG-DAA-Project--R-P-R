# SETG-DAA-Project--R-P-R
# SETG – Smart Exam Timetable Generator

## Project Overview

The Smart Exam Timetable Generator (SETG) models exam scheduling as a graph coloring problem.

* Courses are taken as nodes
* Conflicts (common students) are taken as edges
* Time slots are represented as colors

The goal is to generate a conflict-free timetable while minimizing the number of time slots.

## Real-World Relevance

Universities require efficient exam scheduling to:

* Avoid conflicts between exams for students
* Optimize usage of available time slots
* Handle large student-course datasets

## Objectives

* Apply graph-based algorithms to scheduling
* Implement and compare:

  * Greedy Coloring
  * Backtracking (Exact Solution)
  * DSATUR (Heuristic Optimization)
* Minimize the number of slots used

## Repository Structure

```bash
SETG/
│── data/
│── src/
│── experiments/
│── results/
│── docs/
│── logs/
```

## Progress Log

### Day 1 – Problem Understanding and Setup

* Created GitHub repository
* Understood the problem statement
* Modeled the problem as a graph coloring problem
* Identified algorithms to implement
* Set up project structure

## Next Steps

* Implement conflict graph construction
* Develop greedy coloring algorithm
* Test with sample datasets

### Day 2 – Conflict Graph Construction
- Implemented conflict graph using adjacency list
- Converted student-course mapping into graph
- Created edges between courses sharing common students
- Tested graph with sample dataset

### Day 3 – Greedy Graph Coloring
- Implemented greedy coloring algorithm
- Assigned minimum available slot to each course
- Tested on sample dataset
- Observed fast execution but not always optimal

### Day 4 – Backtracking Graph Coloring
- Implemented backtracking algorithm for exact graph coloring
- Explored all possible color assignments
- Ensured minimum number of slots (optimal solution)
- Observed high execution time for larger graphs
