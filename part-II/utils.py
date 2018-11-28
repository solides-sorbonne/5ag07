import dolfin 
import matplotlib.pyplot as plt

def plotbeam(dtheta):
    """ Utility function to represent the shape of beam given 
        the rotation field theta(s) and the boundary conditions
        It formulate in the weak form and solve with the 
        finite element method the equations
        x'(s) = cos(theta(s)), x(0)=0
        y'(s) = sin(theta(s)), y(0)=0
    """
    V = dtheta.function_space()
    x_ = dolfin.Function(V) 
    y_ = dolfin.Function(V) 
    test = dolfin.TestFunction(V) 
    trial = dolfin.TrialFunction(V)
    # Solve x'(s)=cos(theta), x(0)=0 with FE
    dx = dolfin.dx
    a = trial.dx(0) * test * dx
    fx = dolfin.interpolate(dolfin.Expression("cos(dtheta)",dtheta=dtheta,pi=dolfin.pi,degree=1), V)
    Lx = fx*test*dx
    bc = dolfin.DirichletBC(V, 0., "near(x[0], 0.) && on_boundary") 
    dolfin.solve(a==Lx, x_, bc)
    # Solve y'(s)=sing(theta), y(0)=0 with FE    
    fy = dolfin.interpolate(dolfin.Expression("sin(dtheta)",dtheta=dtheta,pi=dolfin.pi,degree=1), V) 
    Ly = fy*test*dx
    dolfin.solve(a==Ly, y_, bc)
    p = plt.plot(x_.compute_vertex_values(), y_.compute_vertex_values())
    return (p, x_, y_)