# Workshop 1: Pressure Vessel Mesh Convergence Study

# Problem statement
In this workshop, we will perform stress analysis of pipe due to internal pressure. Due to the symmetry in geometry and loading, the strain along its axis is negligible and therefore we model this system as 2D plane strain.

The objective is to convert the mapdl script to pymapdl and find out the optimum mesh size. 


1. Converting MAPDL script file to pyMAPDL
    1. Using `pymapdl convert` command utility
    2. Using `pymapdl.convert_script()` method
2. Create function to run the pymapdl script for varying mesh sizes
3. Plot mesh size vs stress to check connvergence in mesh size


![model setup](./Files/2d_pressure.png)

# Workspace
See `mapdl_script.inp` for the original mapdl script.


