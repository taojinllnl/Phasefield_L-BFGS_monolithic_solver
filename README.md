## Phasefield L-BFGS monolithic solver
A monolithic solver based on the limited memory BFGS method for phase-field fracture simulation.

### Purpose 
This repository provides the source code and the input files for the numerical examples used in the paper draft titled “A robust phase-field monolithic scheme based on the limited-memory BFGS method with adaptive mesh refinement”. The L-BFGS monolithic solver has the following features:
1. It uses the limited memory BFGS (L-BFGS) method to overcome the non-convexity of the total energy functional of the phase-field fracture formulation.
2. It adopts an adaptive mesh refinement technique to reduce computational cost.
3. It works for both 2D and 3D phase-field fracture simulations.

### Content
The repository contains the following content:
1. the source code of the L-BFGS method for the phase-field monolithic solver.
2. the input files for several 2D and 3D phase-field fracture simulations included in the aforementioned manuscript.

### How to compile
The three-field finite element procedure is implemented in [deal.II](https://www.dealii.org/) (version 9.4.0), which is an open source finite element library. In order to use the code (**main.cc**) provided here, deal.II should be configured with MPI and at least with the interfaces to BLAS, LAPACK, Threading Building Blocks (TBB), and UMFPACK. For optional interfaces to other software packages, see https://www.dealii.org/developer/readme.html.

Once the deal.II library is compiled, for instance, to "~/dealii-9.5.1/bin/", follow the steps listed below:
1. cd SourceCode
2. cmake -DDEAL_II_DIR=~/dealii-9.5.1/bin/  .
3. make debug or make release
4. make

### How to run
1. Go into one of the examples folders.
2. For instance a 2D test case: go into simple_shear_test/adaptive_refinement
3. Run via ./../../SourceCode/main 2
4. For 3D test cases, run via ./../../SourceCode/main 3

### How to cite this work:
TBD...




