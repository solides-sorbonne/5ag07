#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    This modules generates meshes with gmsh and convert to xml and xdmf formats
    You can reuse it with your own geo file
"""

import subprocess
import os

geo_script_tube = """
    radius = 1.0;
    h = par_h;
    rho = par_rho; 
    thickness =  rho*radius;

    
    p0 = newp; Point(p0) = {0., 0., 0., h};
    p1 = newp; Point(p1) = {radius*(1-0.5*rho), 0., 0., h};
    p2 = newp; Point(p2) = {radius*(1+0.5*rho), 0., 0., h};
    p3 = newp; Point(p3) = {0., radius*(1+0.5*rho), 0., h};
    p4 = newp; Point(p4) = {0., radius*(1-0.5*rho), 0., h};
    
    l1 = newl; Line(l1) = {p1, p2};
    l2 = newl; Circle(l2) = {p2, p0, p3};
    l3 = newl; Line(l3) = {p3, p4};
    l4 = newl; Circle(l4) = {p4, p0, p1};
    
    ll0 = newll; Line Loop(ll0) = {l1, l2, l3, l4};
    s0 = news; Plane Surface(s0) = {ll0};
    
    Physical Surface(10) = {s0};
    Physical Line(1) = {l1};
    Physical Line(2) = {l2};
    Physical Line(3) = {l3};
    Physical Line(4) = {l4};
    """

def generate_mesh_gmsh(geo_script, meshname, pars, verbose = False):
    outname = meshname
    for k,v in pars.items():
        if verbose:
            print("replacing","par_%s"%k,"with",v)
        outname+="-"+str(k)+str(v).replace(".","_")
        geo_script = geo_script.replace("par_"+str(k), str(v))
    geofile = outname + ".geo"
    if verbose:
        print("saving the following script to ",geofile)
        print(geo_script)
    os.makedirs(os.path.dirname(geofile), exist_ok=True)
    with open(geofile, "w+") as file1:
        file1.write(geo_script)
    gmsh_cmd = "gmsh -2 -o %s.msh %s"%(outname,geofile)
    if verbose:
        print("Running " + gmsh_cmd)
    subprocess.call(gmsh_cmd, shell = True)
    if verbose:
        print("Converting the mesh format with meshio")
    subprocess.call("dolfin-convert %s.msh %s.xdmf"%(outname,outname), shell = True)
    subprocess.call("dolfin-convert %s.msh %s.xml"%(outname,outname), shell = True)
    return outname

def generate_mesh_gmsh_tube(meshname, pars, verbose = False):
    return generate_mesh_gmsh(geo_script_tube,meshname,pars,verbose = False)

if __name__ == "__main__":
    # execute only if run as a script
    pars = {"h": 0.1, "rho": 0.5}
    meshname = generate_mesh_gmsh("meshes/tube", pars, verbose = True)
    print(meshname)