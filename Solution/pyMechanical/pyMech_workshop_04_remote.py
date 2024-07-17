import ansys.mechanical.core as pymechanical
import os

mechanical =pymechanical.launch_mechanical()

print(mechanical)

script_path=os.path.join(os.getcwd(),'pyMechanical_Workshop\script.py')
print(script_path)
mechanical.run_python_script_from_file(script_path)

############print statements equivalent 
print('Mode 1 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_1.LoadMultiplier")))
print('Mode 2 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_2.LoadMultiplier")))
print('Mode 3 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_3.LoadMultiplier")))
print('Mode 4 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_4.LoadMultiplier")))
print('Mode 5 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_5.LoadMultiplier")))
print('Mode 6 deformation load multiplier: '+str(mechanical.run_python_script("buck_deformation_6.LoadMultiplier")))

print('Mode 6 equivalent stress maximum: '+str(mechanical.run_python_script("buck_stress_eqv.Maximum")))

mechanical.exit(force=True)