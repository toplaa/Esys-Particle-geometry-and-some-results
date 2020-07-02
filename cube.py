#Code to generate a cubic particle
#Acknowledge ESyS particle tutorial

from gengeo import *

minRadius = 0.08
maxRadius = 0.32

# corner points
conPoint1 = Vector3(-5.0,0.0,-5.0)
conPoint2 = Vector3(5.0,10.0,5.0)

# block volume
box = BoxWithPlanes3D(conPoint1,conPoint2)

# neighbour table
mntable = MNTable3D (
	minPoint = Vector3 (-7,-7,-7),
	maxPoint = Vector3 (7,20,7),
	gridSize = 2.5*maxRadius,
	numGroups = 1)

# iteration parameters
insertFails = 10000
maxIter = 1000
tol = 1.0e-6

# packer
packer = InsertGenerator3D(minRadius,maxRadius,insertFails,maxIter,tol)

# pack particles into volume
packer.generatePacking(box,mntable,0,1)

#tag particles along plane of the rod
mntable.tagParticlesAlongPlane (
	plane = Plane (Vector3(0,0,0),Vector3(0,1,0)),
	distance = 2.5*maxRadius,
	tag = 2,
	groupID = 0
)

# create bonds between neighbouring particles:
mntable.generateBonds(0,1.0e-5,1)

# write a geometry file
mntable.write("cube.geo",1)
mntable.write("cube.vtu",2)
