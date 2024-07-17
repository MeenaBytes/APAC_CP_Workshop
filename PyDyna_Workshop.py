import os
import sys
 
#Import Libraries
 
from ansys.dyna.core.pre.dynasolution import DynaSolution
from ansys.dyna.core.pre import launch_dynapre
from ansys.dyna.core.pre.dynamech import (
    DynaMech,
    Velocity,
    PartSet,
    ShellPart,
    SolidPart,
    NodeSet,
    Contact,
    ContactSurface,
    ShellFormulation,
    SolidFormulation,
    ContactType,
    AnalysisType
)
from ansys.dyna.core.pre.dynamaterial import (
    MatRigid,
    MatPiecewiseLinearPlasticity,
)
from ansys.dyna.core.pre.misc import check_valid_ip
from ansys.dyna.core.pre.dynabase import Curve
 
 
#Launch pyDyna
hostname = "localhost"
 
solution = launch_dynapre(ip=hostname)
 
 
#Reading the input file
 
input_file_directory = r"D:\C_Drive\Work\2024\13_PyAnsys_Training\input_keyfile"
os.chdir(input_file_directory)
print("Current working directory : ",os.getcwd())
path = input_file_directory + os.sep
solution.open_files([path+"ball_plate.k"])
print("Input file is read")
 
 
#Create Database and control cards
 
solution.set_termination(10)
 
 
ballplate = DynaMech(AnalysisType.EXPLICIT)
timestep_curve = Curve(x=[0,10],y=[0.0001,0.001])
ballplate.set_timestep(max_timestep=timestep_curve)
solution.add(ballplate)
 
# checking how many parts are availble
 
solution.model._sync_up_model()
 
input_parts = solution.model.parts
 
for i in input_parts:
    print("Name of Part : ",i.name)
    print("ID of the part : ",i.id)
 
 
#Part Defination
 
#Material and Section Defination
 
 
matelastic = MatPiecewiseLinearPlasticity(mass_density=7.83e-6,young_modulus=207,yield_stress=0.2,tangent_modulus=2)
matrigid = MatRigid(mass_density=7.83e-6,young_modulus=207,poisson_ratio=0.3)
 
#PART1
plate = ShellPart(1)
plate.set_element_formulation(ShellFormulation.BELYTSCHKO_TSAY)
plate.set_material(matelastic)
plate.set_thickness(1)
plate.set_integration_points(5)
ballplate.parts.add(plate)
 
 
#PART2
 
ball = SolidPart(2)
ball.set_material(matrigid)
ball.set_element_formulation(SolidFormulation.CONSTANT_STRESS_SOLID_ELEMENT)
ballplate.parts.add(ball)
 
 
#Contact Defination
 
single_surface = Contact(ContactType.AUTOMATIC)
slave_surf = ContactSurface(PartSet([1,2]))
single_surface.set_slave_surface(slave_surf)
ballplate.contacts.add(single_surface)
 
# Boundary conditions
 
spc_nodes = [1,17,273,289]
spc_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 18, 35, 52, 69, 86, 103, 120, 137, 154, 171, 188, 205, 222, 239, 256]
 
ballplate.boundaryconditions.create_spc(NodeSet(spc_nodes),rx=False,ry=False,rz=False)
 
#Intial conditions
 
ballplate.initialconditions.create_velocity(PartSet([2]),velocity=Velocity(0,0,-10))
 
# Define database outputs
 
solution.set_output_database(glstat=0.1,bndout=0.1)
solution.create_database_binary(dt=0.1,filetype="D3PLOT")
 
out = solution.save_file()
 
print("The output directory : ",out)
 
import shutil
 
 
source = out + os.sep + "ball_plate.k"
target_directory = r"D:\C_Drive\Work\2024\13_PyAnsys_Training\input_keyfile\output" + os.sep + "ball_plate.k"
 
shutil.copyfile(source, target_directory)
 
 
#solver
 
from ansys.dyna.core.solver import launch_dyna
hostname = 'localhost'
dyna = launch_dyna(ip=hostname,port="5000")
target_directory = r"D:\C_Drive\Work\2024\13_PyAnsys_Training\input_keyfile\output" + os.sep + "ball_plate.k"
dyna.start_locally(preset="MPP",input = target_directory,nproc=4,memory=20)