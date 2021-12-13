import os 
import pyvista as pv 

def vtk2stl(path, fname):
    vtk_f = pv.read(os.path.join(path, fname))
    pv.save_meshio(fname[:-4] + '.stl', vtk_f)
    print(fname + ' is changed to STL !')

def stl2vtk(path, fname): 
    stl_f = pv.read(os.path.join(path, fname))
    pv.save_meshio(fname[:-4] + '.vtk', stl_f)
    print(fname + ' is changed to VTK !')
    

# stl to vtk
path = os.getcwd()
fname = 'bunny.stl'
stl2vtk(path, fname)

