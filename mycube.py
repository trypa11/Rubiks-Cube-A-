import numpy 
import random
from copy import deepcopy

class State:
    def __init__(self,side,row,col,colour ):
        self.side=side
        self.row=row
        self.col=col
        self.colour=colour
    
    def set_side(self,side):
        self.side=side
    
    def set_row(self,row):
        self.row=row
    
    def set_col(self,col):
        self.col=col
    
    def get_side(self):
        return self.side
    
    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col
    
    def get_colour(self):
        return self.colour
    
    def __str__(self) -> str:
        return self.colour

    

class RubiksCube:
    """
    gia thn ylopoihsh toy kyvou exoume ena array 6x3x3 opou plevra X grammh X sthlh 
    # face : colour -- position  
    # 0 : "w" (white) -- top
    # 1 : "g" (green) -- left
    # 2 : "r" (red) -- front
    # 3 : "b" (blue) -- right
    # 4 : "o" (orange) -- back
    # 5 : "y" (yellow) -- bottom

    """

    def __init__(self):
        self.h=0
        self.g=0
        self.parent=None
        colours=['w', 'g', 'r', 'b', 'o', 'y']
        self.cube = numpy.zeros((6, 3, 3), dtype=object)  # 6 by 3 by 3 array
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    self.cube[i, j, k] = State(i,j,k,colours[i])
    
    def prntcube(self):
        for i in range(6):
            print("")
            for j in range(3):
                print("")
                for k in range(3):
                    print(self.cube[i, j, k], end=" ")
        print("")

    def hor_twist(self, row, dir):
        """
        row- grammh pou tha gyrisoume

        dir- katefthinsh pou gyrizoume 
        0 = left 
        1 = right
        """
        if row==0 or row==2:
            if dir == 0:  # twist left
                temp = deepcopy(self.cube[1, row])
                self.cube[1, row] = self.cube[2, row]
                self.cube[2, row] = self.cube[3, row]
                self.cube[3, row] = self.cube[4, row]
                self.cube[4, row] = temp
            elif dir == 1:  # twist right
                temp = deepcopy(self.cube[1, row])
                self.cube[1, row] = self.cube[4, row]
                self.cube[4, row] = self.cube[3, row]
                self.cube[3, row] = self.cube[2, row]
                self.cube[2, row] = temp
        else:
            print("Error, row must be 0,1 or 2")

        # strofh ths pano h kato plevras
        if dir == 0:  # aristera
            if row == 0:
                temp1 = deepcopy(self.cube[0, 0, 0])
                self.cube[0, 0, 0] = self.cube[0, 2, 0]
                self.cube[0, 2, 0] = self.cube[0, 2, 2]
                self.cube[0, 2, 2] = self.cube[0, 0, 2]
                self.cube[0, 0, 2] = temp1
                temp2 = deepcopy(self.cube[0, 0, 1])
                self.cube[0, 0, 1] = self.cube[0, 1, 0]
                self.cube[0, 1, 0] = self.cube[0, 2, 1]
                self.cube[0, 2, 1] = self.cube[0, 1, 2]
                self.cube[0, 1, 2] = temp2
            elif row == 2:
                temp1 = deepcopy(self.cube[5, 0, 0])
                self.cube[5, 0, 0] = self.cube[5, 0, 2]
                self.cube[5, 0, 2] = self.cube[5, 2, 2]
                self.cube[5, 2, 2] = self.cube[5, 2, 0]
                self.cube[5, 2, 0] = temp1
                temp2 = deepcopy(self.cube[5, 0, 1])
                self.cube[5, 0, 1] = self.cube[5, 1, 2]
                self.cube[5, 1, 2] = self.cube[5, 2, 1]
                self.cube[5, 2, 1] = self.cube[5, 1, 0]
                self.cube[5, 1, 0] = temp2

        elif dir == 1:  # dejia
            if row == 0:
                temp1 = deepcopy(self.cube[0, 0, 0])
                self.cube[0, 0, 0] = self.cube[0, 0, 2]
                self.cube[0, 0, 2] = self.cube[0, 2, 2]
                self.cube[0, 2, 2] = self.cube[0, 2, 0]
                self.cube[0, 2, 0] = temp1
                temp2 = deepcopy(self.cube[0, 0, 1])
                self.cube[0, 0, 1] = self.cube[0, 1, 2]
                self.cube[0, 1, 2] = self.cube[0, 2, 1]
                self.cube[0, 2, 1] = self.cube[0, 1, 0]
                self.cube[0, 1, 0] = temp2
            elif row == 2:
                temp1 = deepcopy(self.cube[5, 0, 0])
                self.cube[5, 0, 0] = self.cube[5, 2, 0]
                self.cube[5, 2, 0] = self.cube[5, 2, 2]
                self.cube[5, 2, 2] = self.cube[5, 0, 2]
                self.cube[5, 0, 2] = temp1
                temp2 = deepcopy(self.cube[5, 0, 1])
                self.cube[5, 0, 1] = self.cube[5, 1, 0]
                self.cube[5, 1, 0] = self.cube[5, 2, 1]
                self.cube[5, 2, 1] = self.cube[5, 1, 2]
                self.cube[5, 1, 2] = temp2

    def ver_twist(self, col, dir):
        """
        dir: 0==down, 1==up

        """
        if col==0 or col==2:
            if dir == 0:  # down
                for i in range(3):
                    temp = deepcopy(self.cube[0, i, col])
                    self.cube[0, i, col] = self.cube[3, -i-1, -col-1]
                    self.cube[3, -i-1, -col-1] = self.cube[5, i, col]
                    self.cube[5, i, col] = self.cube[1, i, col]
                    self.cube[1, i, col] = temp
            elif dir == 1:  # up
                for i in range(3):
                    temp = deepcopy(self.cube[0, i, col])
                    self.cube[0, i, col] = self.cube[1, i, col]
                    self.cube[1, i, col] = self.cube[5, i, col]
                    self.cube[5, i, col] = self.cube[3, -i-1, -col-1]
                    self.cube[3, -i-1, -col-1] = temp
        else:
            print("Error, col must be 0,1 or 2")

        # strofh ths aristera h dejias plevras
        if dir == 0:
            if col == 0:
                temp1 = deepcopy(self.cube[4, 0, 0])
                self.cube[4, 0, 0] = self.cube[4, 2, 0]
                self.cube[4, 2, 0] = self.cube[4, 2, 2]
                self.cube[4, 2, 2] = self.cube[4, 0, 2]
                self.cube[4, 0, 2] = temp1
                temp2 = deepcopy(self.cube[4, 0, 1])
                self.cube[4, 0, 1] = self.cube[4, 1, 0]
                self.cube[4, 1, 0] = self.cube[4, 2, 1]
                self.cube[4, 2, 1] = self.cube[4, 1, 2]
                self.cube[4, 1, 2] = temp2
            elif col == 2:
                temp1 = deepcopy(self.cube[2, 0, 0])
                self.cube[2, 0, 0] = self.cube[2, 0, 2]
                self.cube[2, 0, 2] = self.cube[2, 2, 2]
                self.cube[2, 2, 2] = self.cube[2, 2, 0]
                self.cube[2, 2, 0] = temp1
                temp2 = deepcopy(self.cube[2, 0, 1])
                self.cube[2, 0, 1] = self.cube[2, 1, 2]
                self.cube[2, 1, 2] = self.cube[2, 2, 1]
                self.cube[2, 2, 1] = self.cube[2, 1, 0]
                self.cube[2, 1, 0] = temp2
        elif dir == 1:
            if col == 0:
                temp1 = deepcopy(self.cube[4, 0, 0])
                self.cube[4, 0, 0] = self.cube[4, 0, 2]
                self.cube[4, 0, 2] = self.cube[4, 2, 2]
                self.cube[4, 2, 2] = self.cube[4, 2, 0]
                self.cube[4, 2, 0] = temp1
                temp2 = deepcopy(self.cube[4, 0, 1])
                self.cube[4, 0, 1] = self.cube[4, 1, 2]
                self.cube[4, 1, 2] = self.cube[4, 2, 1]
                self.cube[4, 2, 1] = self.cube[4, 1, 0]
                self.cube[4, 1, 0] = temp2
            elif col == 2:
                temp1 = deepcopy(self.cube[2, 0, 0])
                self.cube[2, 0, 0] = self.cube[2, 2, 0]
                self.cube[2, 2, 0] = self.cube[2, 2, 2]
                self.cube[2, 2, 2] = self.cube[2, 0, 2]
                self.cube[2, 0, 2] = temp1
                temp2 = deepcopy(self.cube[2, 0, 1])
                self.cube[2, 0, 1] = self.cube[2, 1, 0]
                self.cube[2, 1, 0] = self.cube[2, 2, 1]
                self.cube[2, 2, 1] = self.cube[2, 1, 2]
                self.cube[2, 1, 2] = temp2

    def side_twist(self, col, dir):
        if col==0 or col==2:
            for i in range(3):

                if dir == 0:  # twist left
                    temp = deepcopy(self.cube[0, -col-1, i])
                    self.cube[0, -col-1, i] = self.cube[2, i, col]
                    self.cube[2, i, col] = self.cube[5, col, -i-1]
                    self.cube[5, col, -i-1] = self.cube[4, -i-1, -col-1]
                    self.cube[4, -i-1, -col-1] = temp
                elif dir == 1:  # right
                    temp = deepcopy(self.cube[0, -col-1, i])
                    self.cube[0, -col-1, i] = self.cube[4, -i-1, -col-1]
                    self.cube[4, -i-1, -col-1] = self.cube[5, col, -i-1]
                    self.cube[5, col, -i-1] = self.cube[2, i, col]
                    self.cube[2, i, col] = temp

        else:
            print("Error, col must be 0,1 or 2")

        if dir == 0:
            if col == 0:
                temp1 = deepcopy(self.cube[1, 0, 0])
                self.cube[1, 0, 0] = self.cube[1, 0, 2]
                self.cube[1, 0, 2] = self.cube[1, 2, 2]
                self.cube[1, 2, 2] = self.cube[1, 2, 0]
                self.cube[1, 2, 0] = temp1
                temp2 = deepcopy(self.cube[1, 0, 1])
                self.cube[1, 0, 1] = self.cube[1, 1, 2]
                self.cube[1, 1, 2] = self.cube[1, 2, 1]
                self.cube[1, 2, 1] = self.cube[1, 1, 0]
                self.cube[1, 1, 0] = temp2
            elif col == 2:
                temp1 = deepcopy(self.cube[3, 0, 0])
                self.cube[3, 0, 0] = self.cube[3, 2, 0]
                self.cube[3, 2, 0] = self.cube[3, 2, 2]
                self.cube[3, 2, 2] = self.cube[3, 0, 2]
                self.cube[3, 0, 2] = temp1
                temp2 = deepcopy(self.cube[3, 0, 1])
                self.cube[3, 0, 1] = self.cube[3, 1, 0]
                self.cube[3, 1, 0] = self.cube[3, 2, 1]
                self.cube[3, 2, 1] = self.cube[3, 1, 2]
                self.cube[3, 1, 2] = temp2
        elif dir == 1:
            if col == 0:
                temp1 = deepcopy(self.cube[1, 0, 0])
                self.cube[1, 0, 0] = self.cube[1, 2, 0]
                self.cube[1, 2, 0] = self.cube[1, 2, 2]
                self.cube[1, 2, 2] = self.cube[1, 0, 2]
                self.cube[1, 0, 2] = temp1
                temp2 = deepcopy(self.cube[1, 0, 1])
                self.cube[1, 0, 1] = self.cube[1, 1, 0]
                self.cube[1, 1, 0] = self.cube[1, 2, 1]
                self.cube[1, 2, 1] = self.cube[1, 1, 2]
                self.cube[1, 1, 2] = temp2
            elif col == 2:
                temp1 = deepcopy(self.cube[3, 0, 0])
                self.cube[3, 0, 0] = self.cube[3, 0, 2]
                self.cube[3, 0, 2] = self.cube[3, 2, 2]
                self.cube[3, 2, 2] = self.cube[3, 2, 0]
                self.cube[3, 2, 0] = temp1
                temp2 = deepcopy(self.cube[3, 0, 1])
                self.cube[3, 0, 1] = self.cube[3, 1, 2]
                self.cube[3, 1, 2] = self.cube[3, 2, 1]
                self.cube[3, 2, 1] = self.cube[3, 1, 0]
                self.cube[3, 1, 0] = temp2

    def randomize(self,t):
        for i in range(t):
            t = random.randint(0, 2)
            r = random.randint(0, 1)
            if r == 1:
                r = 2
            dir = random.randint(0, 1)

            if t == 0:
                self.hor_twist(r, dir)
            elif t == 1:
                self.ver_twist(r, dir)
            elif t == 2:
                self.side_twist(r, dir)

    def isfacesolved(self, face):
        solved = True
        for i in range(3):
            for j in range(3):
                """if self.cube[face, i, j].get_side()!= face or self.cube[face, i, j].get_row()!= i or self.cube[face, i, j].get_col()!= j  :
                    solved = False
                    break"""
                if self.cube[face,i,j].get_colour()!=self.cube[face,1,1].get_colour():
                    solved=False
                    break
        return solved

    def iscubeKsolved(self, K):
        solved = False
        sf = 0
        for i in range(6):
            if self.isfacesolved(i):
                sf += 1
            if sf == K:
                solved = True
                break
        return solved
    
    def make_move(self,move):
        if move==1:
            self.hor_twist(0,0)
            
        if move==2:
            self.hor_twist(0,1)
            
        if move==3:
            self.hor_twist(2,0)
            
        if move==4:
            self.hor_twist(2,1)
            
        if move==5:
            self.ver_twist(0,0)
            
        if move==6:
            self.ver_twist(0,1)

        if move==7:
            self.ver_twist(2,0)
            
        if move==8:
            self.ver_twist(2,1)
            
        if move==9:
            self.side_twist(0,0)
            
        if move==10:
            self.side_twist(0,1)

        if move==11:
            self.side_twist(2,0)
            
        if move==12:
            self.side_twist(2,1)
            
    def manhattan_distance(self,side,row,col):
        d=abs(side-self.cube[side,row,col].get_side())+abs(row-self.cube[side,row,col].get_row())+abs(col-self.cube[side,row,col].get_col())
        return d

    def min_max_sum_edge_corner(self):#heuristic
        l_edges=list()
        l_corners=list()
        corners=0
        edges=0
        for s in range(6):
            for r in range(3):
                for c in range(3):
                    if r==1 and c==1:
                        continue
                    d=self.manhattan_distance(s,r,c)
                    if c==1 or r==1:
                        l_edges.append(d)
                    else:
                        l_corners.append(d)        
            corners=corners+min(l_corners)
            edges=edges+min(l_edges)
            l_corners.clear()
            l_edges.clear()
        return max(corners/4,edges/4)

    """def max_sum_edge_corner(self):#heuristic
        corners=0
        edges=0
        for s in range(6):
            for r in range(3):
                for c in range(3):
                    if r==1 and c==1:
                        continue
                    d=self.manhattan_distance(s,r,c)
                    if c==1 or r==1:
                        corners=corners+d
                    else:
                        edges=edges+d      
        return max(corners/4,edges/4)"""

    def set_h(self,h):
        self.h=h
    
    def get_h(self):
        return self.h
    
    def set_g(self,g):
        self.g=g
    
    def get_g(self):
        return self.g

    def set_parent(self,parent):
        self.parent=parent
    
    def get_parent(self):
        return self.parent

    def get_cube(self):
        return self.cube