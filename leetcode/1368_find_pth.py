from functools import partial

visited = []
graph = {}

def get_distance(target,curr):
    return abs(curr[0]-target[0]) + abs(curr[1]-target[1])


def valid_next(index,dimensions,curr,direction):

    i = dimensions[0]
    j = dimensions[1]

    if not (next_i <= i-1 and next_j <= j-1):
        return 
    
    dist = get_dist((i,j))
    dict_ = add_to_dict(dict_,(i,j),(i,j),dist)
    next_ = grid[i][j]
    
    valid,co_ord = get_valid_next((i,j),next_)

    match direction:
        case 1:
            next_i =i
            next_j = j+1
        case 2:
            next_i = i
            next_j = j-1
        case 3:
            next_i = i+1
            next_j = j
        case 4:
            next_i = i-1
            next_j = j
    
        
    if next_i <= i-1 and next_j <= j-1:
        # add entry and call next.
        return True,(next_i,next_j)
    valid_next(index,dimensions,curr,direction)
    
def add_to_dict(dict_,key,value,dist,connected=False):
    if dict_.get(key):
        arr,distance,connected = dict_[key]
        arr.append(value)
        if dist<distance:
            distance = dist
        dict_[key] = [arr,distance,connected]
    else:
        dict_[key] = [[value],dist,False]
    return dict_ 

def minCost(grid) -> int:
    # graph : visited ?  
    changes = 0
    rows = len(grid)
    columns = len(grid[0])
    get_dist = partial(get_distance,(rows-1,columns-1))
    get_valid_next = partial(valid_next,(rows,columns),)
    global visited
    visited = [[False for _ in range(columns)] for _ in range(rows)]

    for i in range(len(grid)):

        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            dist = get_dist((i,j))
            dict_ = add_to_dict(dict_,(i,j),(i,j),dist)
            next_ = grid[i][j]

            valid,co_ord = get_valid_next((i,j),next_)
            
            if valid:
                # traverse the path.
                pass
                
                