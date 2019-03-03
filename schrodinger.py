"""
This module contains all the definitions necessary for 2D.

Main functions:
    - generate(ngen, lgen, mgen, rad, granularity, subfolder='') creates a set of data for the orbital specified in the arguments.
    - runbatch(granularity, subfolder='') creates a complete set of data up to n=4 at the resolution specified in the argument.
    - plot(nget, lget, mget, subfolder='', contours=100) uses mayavi to generate the orbital plot using the data from the specified subfolder.
    - plotslice(nget, lget, mget, subfolder='') creates a slice plot of the orbital using the data from the specified subfolder.
"""


import numpy as np
import scipy.constants as c
from time import time
from os import makedirs
from os.path import exists
from mayavi import mlab
from traits.api import HasTraits, Instance, Array, on_trait_change
from traitsui.api import View, Item, HGroup, Group
from tvtk.api import tvtk
from tvtk.pyface.scene import Scene
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, MlabSceneModel

a=c.physical_constants['Bohr radius'][0]

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)
    if not theta:
        phi = 0
    else:
        phi = np.arcsin(y/(r*np.sin(theta)))
    return round(r, 5), round(theta, 5), round(phi, 5)

def angular_wave_func(m,l,theta,phi):
    if(not(m<=l and m>=(-l))):
        raise ValueError("The value for m is not valid for this value of l.")
    elif(l<0):
        raise ValueError("l must be a positive integer.")
    else:
        if (l == 0):
            sol = np.complex((1/(4*c.pi)) ** (0.5))
        elif (l == 1):
            if(m == 1):
                sol = np.complex(-((3/(8*c.pi))**0.5 * np.sin(theta) * np.exp(phi*1j)))
            elif(m == -1):
                sol = np.complex((3/(8*c.pi))**0.5 * np.sin(theta) * np.exp(phi * (-1j)))
            elif(m == 0):
                sol = np.complex((3/(4*c.pi))**0.5 * np.cos(theta))
        elif (l == 2):
            if(m == 2):
                sol = np.complex((15/(32*c.pi))**0.5 * (np.sin(theta))**2 * np.exp(2 * phi * 1j))
            elif(m == 1):
                sol = np.complex(-((15/(8*c.pi))**0.5 * np.cos(theta) * np.sin(theta) * np.exp(phi * 1j)))
            elif(m == 0):
                sol = np.complex((5 / (16 * c.pi))**0.5 * (3 * ((np.cos(theta))**2) - 1))
            elif(m == -1):
                sol = np.complex((15 / (8 * c.pi))**0.5 * np.cos(theta) * np.sin(theta) * np.exp(phi * (-1j)))
            elif(m == -2):
                sol = np.complex((15/(32 * c.pi))**0.5 * (np.sin(theta))**2 * np.exp(2 * phi * (-1j)))
        elif (l == 3):
            if(m == 3):
                sol = np.complex(-((35/(64*c.pi))**0.5 * (np.sin(theta))**3 * np.exp(3 * phi * 1j)))
            elif(m == 2):
                sol = np.complex((105/(32 * c.pi))**0.5 * np.cos(theta) * (np.sin(theta))**2 * np.exp(2 * phi * 1j))
            elif(m == 1):
                sol = np.complex(-((21/(64 * c.pi))**0.5 * np.sin(theta) * (5 * (np.cos(theta))**2 - 1) * np.exp(phi * 1j)))
            elif(m == 0):
                sol = np.complex((7/(16 * c.pi))**0.5 * (5 * (np.cos(theta))**3 - 3 * np.cos(theta)))
            elif(m == -1):
                sol = np.complex((21/(64*c.pi))**0.5 * np.sin(theta) * (5 * (np.cos(theta))**2 - 1) * np.exp(phi * (-1j)))
            elif(m == -2):
                sol = np.complex((105/(32 * c.pi))**0.5 * np.cos(theta) * (np.sin(theta))**2 * np.exp(2 * phi * (-1j)))
            elif(m == -3):
                sol = np.complex((35/(64*c.pi))**0.5 * (np.sin(theta))**3 * np.exp(3 * phi * (-1j)))
        else:
            raise Exception('No solution found.')
        return np.round(sol, 5)

def radial_wave_func(n,l,r):
    normal = a**(-3/2)
    if(l < 0 or l>= n):
        raise ValueError("The value for m is not valid for this value of n.")
    elif(n < 0):
        raise ValueError("n must be a positive integer.")
    else:
        if(n == 1):
            sol = (2/(a**1.5)) * np.exp(-r/a)
        elif(n == 2):
            if(l == 0):
                sol = (1/(2**0.5)) * (a**(-3/2)) * (1 - r/(2*a)) * np.exp(-r/(2*a))
            elif(l == 1):
                sol = (1/(24**0.5)) * (a**(-3/2)) * (r/a) * np.exp(-r/(2*a))
        elif(n == 3):
            if(l == 0):
                sol = (2/(81 * 3**0.5)) * (a**(-3/2)) * (27 - 18 * r/a + 2 *((r/a)**2)) * np.exp(-r/(3*a))
            elif(l == 1):
                sol = (8/(27 * 6**0.5)) * (a**(-3/2)) * (1 - r/(6*a)) * (r/a) * np.exp(-r/(3*a))
            elif(l == 2):
                sol = (4/(81 * 30**0.5)) * (a**(-3/2)) * ((r/a)**2) * np.exp(-r/(3*a))
        elif(n == 4):
            if(l == 0):
                sol = 0.25 * (a**(-3/2)) * (1 - 0.75 * r/a + 0.125 * ((r/a)**2) - (1/192) * ((r/a)**3)) * np.exp(-r/(4*a))
            elif(l == 1):
                sol = (((5/3)**0.5)/16) * (a**(-3/2)) * r/a * (1 - 0.25 * r/a + ((r/a)**2)/80) * np.exp(-r/(4*a))
            elif(l == 2):
                sol = (1/(64 * ((5)**0.5))) * (a**(-3/2)) * ((r/a)**2) * (1 - (r/a)/12) * np.exp(-r/(4*a))
            elif(l == 3):
                sol = (1/(768 * (35**0.5))) * (a**(-3/2)) * ((r/a)**3) * np.exp(-r/(4*a))
        return np.round(sol / normal, 5)

def hydrogen_wave_func(n,l,m,roa,Nx,Ny,Nz):
    xx, yy, zz = np.mgrid[-roa:roa:Nx*1j, -roa:roa:Ny*1j, -roa:roa:Nz*1j]
    
    def mag(n):
        return (n.real**2 + n.imag**2)**0.5
        
    def realangular(m, l, theta, phi):
        m = float(m)
        if m > 0:
            return mag((angular_wave_func(-m, l, theta, phi) + (-1)**m * angular_wave_func(m, l, theta, phi))/(2**0.5))
        elif m < 0:
            return mag((angular_wave_func(m, l, theta, phi) - (-1)**m * angular_wave_func(-m, l, theta, phi))*(1j/(2**0.5)))
        else:
            return mag(angular_wave_func(m, l, theta, phi))
        
    sphevec = np.vectorize(cartesian_to_spherical)
    radialvec = np.vectorize(radial_wave_func)
    angularvec = np.vectorize(realangular)
    
    rr, tt, pp = sphevec(xx, yy, zz)
    radialsols = radialvec(n, l, rr * a)
    angularsols = angularvec(m, l, tt, pp)
    density = (angularsols * radialsols) ** 2
    
    return np.round(xx, 5), np.round(yy, 5), np.round(zz, 5), np.round(density, 5)

def hms(seconds):
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes % 60
            return '{} h, {} m, {} s'.format(int(hours), int(minutes), round(seconds, 1))
        return '{} m {} s'.format(int(minutes), round(seconds, 1))
    return '{} s'.format(round(seconds, 1))

def generate(ngen, lgen, mgen, rad, granularity, subfolder=''):
    start = time()
    if not subfolder:
        subfolder = '{granularity}/'
    directory = 'data/{}{}/{}/{}'.format(subfolder, ngen, lgen, mgen)
    print('Generating data for n={}, l={}, m={} up to r={}...'.format(ngen, lgen, mgen, rad))
    x, y, z, mag = hydrogen_wave_func(ngen, lgen, mgen, rad, granularity, granularity, granularity)
    
    if not exists(directory):
        makedirs(directory)
    
    x.dump(directory + '/x.dat')
    y.dump(directory + '/y.dat')
    z.dump(directory + '/z.dat')
    mag.dump(directory + '/den.dat')
    
    elapsed = round(time() - start, 1)
    meta = open(directory + '/meta.txt', 'w+')
    meta.write('n={}, l={}, m={}\nMaximum distance of plot: {}, granularity: {}\nGenerated in {} s'.format(ngen, lgen, mgen, rad, granularity, elapsed))
    meta.close()
    print('Data for n={}, l={}, m={} successfully generated and saved in {}.\n'.format(ngen, lgen, mgen, hms(elapsed)))
    
def runbatch(granularity, subfolder='', nrange=range(1, 5)):
    start = time()
    rads = {1:10, 2:10, 3:25, 4:40}
    print('Beginning data generation...\n\n')
    for n in nrange:
        for l in range(n):
            for m in range(-l, l+1):
                    generate(n, l, m, rads[n], granularity, subfolder=subfolder)
    totals = round(time() - start, 1)
    print('\nAll data generated in {}.'.format(hms(totals)))
    
def plot(nget, lget, mget, subfolder='', contours=100):    
    density = np.load('data/{}{}/{}/{}/den.dat'.format(subfolder, nget, lget, mget))
    figure = mlab.figure('DensityPlot')
    pts = mlab.contour3d(density,contours=contours,opacity=0.4, colormap='CMRmap')
    mlab.axes()
    mlab.show()
    
def plotslice(nget, lget, mget, subfolder=''):
    density = np.load('data/{}{}/{}/{}/den.dat'.format(subfolder, nget, lget, mget))
    sliceplot = VolumeSlicer(data=density)
    sliceplot.configure_traits()

class VolumeSlicer(HasTraits):
    # The data to plot
    data = Array()

    # The 4 views displayed
    scene3d = Instance(MlabSceneModel, ())
    scene_x = Instance(MlabSceneModel, ())
    scene_y = Instance(MlabSceneModel, ())
    scene_z = Instance(MlabSceneModel, ())

    # The data source
    data_src3d = Instance(Source)

    # The image plane widgets of the 3D scene
    ipw_3d_x = Instance(PipelineBase)
    ipw_3d_y = Instance(PipelineBase)
    ipw_3d_z = Instance(PipelineBase)

    _axis_names = dict(x=0, y=1, z=2)


    #---------------------------------------------------------------------------
    def __init__(self, **traits):
        super(VolumeSlicer, self).__init__(**traits)
        # Force the creation of the image_plane_widgets:
        self.ipw_3d_x
        self.ipw_3d_y
        self.ipw_3d_z


    #---------------------------------------------------------------------------
    # Default values
    #---------------------------------------------------------------------------
    def _data_src3d_default(self):
        return mlab.pipeline.scalar_field(self.data,
                            figure=self.scene3d.mayavi_scene)

    def make_ipw_3d(self, axis_name):
        ipw = mlab.pipeline.image_plane_widget(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        plane_orientation='%s_axes' % axis_name)
        return ipw

    def _ipw_3d_x_default(self):
        return self.make_ipw_3d('x')

    def _ipw_3d_y_default(self):
        return self.make_ipw_3d('y')

    def _ipw_3d_z_default(self):
        return self.make_ipw_3d('z')


    #---------------------------------------------------------------------------
    # Scene activation callbaks
    #---------------------------------------------------------------------------
    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        outline = mlab.pipeline.outline(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        )
        self.scene3d.mlab.view(40, 50)
        # Interaction properties can only be changed after the scene
        # has been created, and thus the interactor exists
        for ipw in (self.ipw_3d_x, self.ipw_3d_y, self.ipw_3d_z):
            # Turn the interaction off
            ipw.ipw.interaction = 0
        self.scene3d.scene.background = (0, 0, 0)
        # Keep the view always pointing up
        self.scene3d.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleTerrain()


    def make_side_view(self, axis_name):
        scene = getattr(self, 'scene_%s' % axis_name)

        # To avoid copying the data, we take a reference to the
        # raw VTK dataset, and pass it on to mlab. Mlab will create
        # a Mayavi source from the VTK without copying it.
        # We have to specify the figure so that the data gets
        # added on the figure we are interested in.
        outline = mlab.pipeline.outline(
                            self.data_src3d.mlab_source.dataset,
                            figure=scene.mayavi_scene,
                            )
        ipw = mlab.pipeline.image_plane_widget(
                            outline,
                            plane_orientation='%s_axes' % axis_name)
        setattr(self, 'ipw_%s' % axis_name, ipw)

        # Synchronize positions between the corresponding image plane
        # widgets on different views.
        ipw.ipw.sync_trait('slice_position',
                            getattr(self, 'ipw_3d_%s'% axis_name).ipw)

        # Make left-clicking create a crosshair
        ipw.ipw.left_button_action = 0
        # Add a callback on the image plane widget interaction to
        # move the others
        def move_view(obj, evt):
            position = obj.GetCurrentCursorPosition()
            for other_axis, axis_number in self._axis_names.items():
                if other_axis == axis_name:
                    continue
                ipw3d = getattr(self, 'ipw_3d_%s' % other_axis)
                ipw3d.ipw.slice_position = position[axis_number]

        ipw.ipw.add_observer('InteractionEvent', move_view)
        ipw.ipw.add_observer('StartInteractionEvent', move_view)

        # Center the image plane widget
        ipw.ipw.slice_position = 0.5*self.data.shape[
                    self._axis_names[axis_name]]

        # Position the view for the scene
        views = dict(x=( 0, 90),
                     y=(90, 90),
                     z=( 0,  0),
                     )
        scene.mlab.view(*views[axis_name])
        # 2D interaction: only pan and zoom
        scene.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleImage()
        scene.scene.background = (0, 0, 0)


    @on_trait_change('scene_x.activated')
    def display_scene_x(self):
        return self.make_side_view('x')

    @on_trait_change('scene_y.activated')
    def display_scene_y(self):
        return self.make_side_view('y')

    @on_trait_change('scene_z.activated')
    def display_scene_z(self):
        return self.make_side_view('z')


    #---------------------------------------------------------------------------
    # The layout of the dialog created
    #---------------------------------------------------------------------------
    view = View(HGroup(
                  Group(
                       Item('scene_y',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene_z',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                  Group(
                       Item('scene_x',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene3d',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                ),
                resizable=True,
                title='Volume Slicer',
                )
                    

# Additional functions
# These are not necessary to create orbital visualizations
# However, they have been written as part of 2D
                       
def deg_to_rad(deg):
    return deg * c.pi / 180
  
def rad_to_deg(rad):
    return rad * 180 / c.pi

def spherical_to_cartesian(r,theta,phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return round(x, 5), round(y, 5), round(z, 5)

def mgrid2d(xstart, xend, xpoints, ystart, yend, ypoints):
    xgrid = []
    ygrid = []
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    #xgrid: for xpoints times, each row is the same across all columns, increment with each row.
    for i in range(xpoints):
        xgrid.append([])
        for j in range(ypoints):
            xgrid[i].append(xstart+xstep*i)
    #ygrid: for xpoints times, each column is the same across all rows, increment with each column.
    for i in range(xpoints):
        ygrid.append([])
        for j in range(ypoints):
            ygrid[i].append(ystart+ystep*j)
    grid = [xgrid, ygrid]
    return grid

def mgrid3d(xstart, xend, xpoints, 
            ystart, yend, ypoints, 
            zstart, zend, zpoints):
    xgrid, ygrid, zgrid = [], [], []
    xstep = (xend-xstart)/(xpoints-1)
    ystep = (yend-ystart)/(ypoints-1)
    zstep = (zend-zstart)/(zpoints-1)
    #xgrid
    for i in range(xpoints):
        xgrid.append([])
        for j in range(ypoints):
            xgrid[i].append([])
            for k in range(zpoints):
                xgrid[i][j].append(xstart+xstep*i)
    #ygrid
    for i in range(xpoints):
        ygrid.append([])
        for j in range(ypoints):
            ygrid[i].append([])
            for k in range(zpoints):
                ygrid[i][j].append(ystart+ystep*j)
    #zgrid
    for i in range(xpoints):
        zgrid.append([])
        for j in range(ypoints):
            zgrid[i].append([])
            for k in range(zpoints):
                zgrid[i][j].append(zstart+zstep*k)
    grid = [xgrid, ygrid, zgrid]
    return grid

