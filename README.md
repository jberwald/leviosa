# Overview

The purpose of this test suite is to have a stable set of problems to gain understanding of Qubo solver behavior. We want to appraoch this from a number of angles which will be outlined below. 

One primary goal is to have a general collection of problems that we understand well and can modify according to the needs of new HW. At first, breadth is more important than depth. As we discover specific area and doensions to test with respect to HW characteristics, the composition of problems will change.

A secondary goal is to have a sound resource demonstrating performance of solvers against a static set of problems. From both a hadware and a software perspective (CMOS and QBSolv, for instance) we need to have a database of results at all parameters. This is important from an internal perspective (for regression testing, for instance) and for external investors, to show continued improvement in an objective manner.

## Key components of the test suite

We want a test suite of problems and associated results that has the following characteristics:
- Provides a pure classical understanding of problem solutions using QBSolv
  - Results include the Optimal energy values and degenerate solutions to problems when available
  - Results form a baseline for HW comparisons
- Ideas and experiments for problem manipulation should be easy to test
  - Split Hamiltonians for solving on parallel HW
  - Graph partition software should be easy to integrate
- Mimic the size, density and othe limitations/requirements of various HW generations
- Solutions should be stored in a central repository or database for easy lookup, comparison and visualization
- Classical solutions should allow for ease of comparison to HW solutions 
  - Eg., it should be easy to compute percent solutions reaching optimality; or x% within 99% of optimal. TBD. 
 
## Problem classes

Benchmark and test suite will contain a variety of problems: 
- graph problems
- small toy problems
- small 'difficult' problems (eg., GKA graph qubo suite)
- random qubos or various densities
- TSP problems
- parallel-solved problems from graph cuts
- simulation of single-bit flip in postprocessing step (possible in QBSolv?)

## Software requirements

- QBSolv (see src/ directory for installation)
- High performance graph partition software (eventually, NetworkX will suffice for now)
- A simple database for storage and lookup

Software will be broken into 
- Testing
- Performance analysis
- Device performance comparison pipelines


