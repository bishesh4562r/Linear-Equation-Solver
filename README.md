# Linear-Equation-Solver
A simple python script that can solve linear equations with any number of unknowns. It does not use any external library . Can check consistency of the system.
A global variable **consistent** is defined with a default value **True** i.e by default any system of linear equations is consistent.
A class **Arr** is created and using magic functions some operations are defined so that it will be easier to apply those operations to perform *Elementary Row Operations* while solving the equation.
Functions **inf** and **nos** take an **Arr** object and are used to determine if the system of linear equations have infinitely many or no solutions respectively.
When the script is run the user is asked the no. of unknowns, coefficients and constant of the equations by which augmented matrix **ag_m** is made, then the script loops within **ag_m** and performs row operations and the resulting matrix is such that the cofficient part is an *Identity Matrix* and the last column contains the solution for all the unknowns. The resulting matrix is again looped to display results.
