from mycube import RubiksCube,State
import solver

""" 
Main programm , select the number of moves to randomize the cube and specify K and M in astar if necessary

Algorithm might need multiple runs to succeed

"""
rand=5
K=6
M=1000
cube=RubiksCube()

cube.randomize(rand)


print("___starting cube___rand={}".format(rand))

cube.prntcube()
print("----------start----------")



solvedcube=solver.astar(cube,K,M)
solvedcube.prntcube()


