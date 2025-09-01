## Phasefield L-BFGS monolithic solver
A monolithic solver based on the limited memory BFGS method for phase-field fracture simulation.

### Purpose 
This repository provides the source code and the input files for the numerical examples used in the paper draft titled “A novel phase-field monolithic scheme for brittle crack propagation based on the limited-memory BFGS method with adaptive mesh refinement”. The L-BFGS monolithic solver has the following features:
1. It uses the limited memory BFGS (L-BFGS) method to overcome the non-convexity of the total energy functional of the phase-field fracture formulation.
2. It uses the history variable (the maximum of the positive strain energy in history) approach to enforce the phase-field irreversibility.
3. It adopts an adaptive mesh refinement technique to reduce computational cost.
4. It works for both 2D and 3D phase-field fracture simulations.

### Content
The repository contains the following content:
1. the source code of the L-BFGS method for the phase-field monolithic solver.
2. the input files for several 2D and 3D phase-field fracture simulations included in the aforementioned manuscript.

### How to compile
The L-BFGS finite element procedure is implemented in [deal.II](https://www.dealii.org/) (originally with version 9.4.0 and also works for 9.5.1), which is an open source finite element library. In order to use the code (**main.cc**) provided here, deal.II should be configured with MPI and at least with the interfaces to BLAS, LAPACK, Threading Building Blocks (TBB), and UMFPACK. For optional interfaces to other software packages, see https://www.dealii.org/developer/readme.html.

Once the deal.II library is compiled, for instance, to "~/dealii-9.5.1/bin/", follow the steps listed below:
1. cd SourceCode
2. cmake -DDEAL_II_DIR=~/dealii-9.5.1/bin/  .
3. make debug or make release
4. make

### Potential compilation and compatibility issues
The code uses the `SolutionTransfer` class during the adaptive mesh refinement technique. The member function `interpolate()` of the `SolutionTransfer` class has different interfaces between the develop ("master") branch and older versions of deal.ii (for instance, 9.4.0 and 9.5.1). If you use the develop branch, you should use the following interface: `interpolate(std::vector< VectorType > & all_out)`. If you use an older version of deal.ii, you should use the following interface: `interpolate(const std::vector< VectorType > & all_in, std::vector< VectorType > & all_out )`. Please look at the interfaces of the member function `interpolate()` in the `SolutionTransfer` class in the specific version of deal.ii used by you.

### Latest update:
1. (Sept. 1st, 2025) Add a new gradient-based line search method. Comparing with the previously implemented Strong Wolfe line search, the new line search method could reduce the wall-clock time by 30 to 50 percent.

### How to run
1. Go into one of the examples folders.
2. For instance a 2D test case: go into simple_shear_test/adaptive_refinement
3. Run via ./../../SourceCode/main 2
4. For 3D test cases, run via ./../../SourceCode/main 3

### How to cite this work:
Jin T, Li Z, Chen K. A novel phase-field monolithic scheme for brittle crack propagation based on the limited-memory BFGS method with adaptive mesh refinement. Int J Numer Methods Eng. 2024;e7572. doi: 10.1002/nme.7572
