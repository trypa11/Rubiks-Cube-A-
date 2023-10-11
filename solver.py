from mycube import State,RubiksCube
import numpy as np
import copy


def contCP(child,parent):
    curr=parent.get_parent()
    while curr is not None:
        if arr_equal(curr.cube,child.cube):
            return True
        curr=curr.get_parent()
    return False

def contCF(child,frontier):
    for curr in frontier :
        if arr_equal(curr.cube,child.cube):
            return True
    return False

def arr_equal(arr1,arr2):
    eq=True
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if (arr1[i,j,k].get_side()==arr2[i,j,k].get_side() and 
                    arr1[i,j,k].get_row()==arr2[i,j,k].get_row() and 
                    arr1[i,j,k].get_col()==arr2[i,j,k].get_col()):
                    continue
                eq=False
    return eq

        
def astar(start=RubiksCube(),K=2, M=1000):
    """
    algorithmos iterrative deepening Astar

    # Cube object 
    # K faces to solve (default 2)
    # M max moves to complete (default 1000)
    """
    start.set_h(start.min_max_sum_edge_corner())
    cost_limit=start.get_h()
    start.set_g(start.get_h())
    m=0
    frontier=list()

    while True:
        minimum=None
        frontier.append(start)

        while len(frontier)!=0:
            curr=frontier.pop()
            
            if curr.iscubeKsolved(K):
                print("Solved in {} moves for K={} ".format(m,K) )
                return curr
            if m==M:
                print("Didn't solve cube in under {} moves".format(M))
                return curr
            for i in range(1,13):
                new= copy.deepcopy(curr)
                new.set_g(curr.get_g()+curr.get_h())
                new.set_parent(curr)
                
                new.make_move(i)
                new.set_h(new.min_max_sum_edge_corner())
                    
                if (new.get_h() + new.get_g()) >cost_limit:
                    if minimum is None or (new.get_h() + new.get_g())<minimum:
                        minimum=new.get_h() + new.get_g()
                    continue
                if curr.get_parent() is not None and (contCP(new,curr) or contCF(new,frontier)):
                    continue
                frontier.append(new)
            m+=1     
           
        cost_limit=minimum

