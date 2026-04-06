# SETG-DAA-Project--R-P-R
# SETG – Smart Exam Timetable Generator

## Project Overview

The Smart Exam Timetable Generator (SETG) models exam scheduling as a graph coloring problem.

* Courses are represented as nodes
* Conflicts (common students) are represented as edges
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

