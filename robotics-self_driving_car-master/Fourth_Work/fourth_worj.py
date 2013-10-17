# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import time
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
cost = 1
g_value = 0
def search():
    check_list = []
    state = [g_value,init[0],init[1]]
    state_temp_store = []
    check_list = []
    check_list.append(state)
    # put the position in checked list
    lowest_g_value = 0
    while(state[1:] != goal):
	possible_moved_position=[[state[0]+cost,state[1]+move[0],state[2]+move[1]]  for move in delta]
        for i in possible_moved_position:
            if i[1] >= 0 and i[2]>=0 and i[1] <=4 and i[2]<=5:
                if grid[i[1]][i[2]] == 1: 
		    pass
		elif any(i[1:] == val[1:] for val in state_temp_store):
		    check_list.append(i)
                else:
	#	    print "i",i,"check",check_list
		    if not any(i[1:] == var[1:] for var in check_list) and not any(i[1:] == var[1:] for var in state_temp_store): 
                    	state_temp_store.append(i)
	#raw_input("Press ENTER to exit")
	if any(val for val in state_temp_store):
	        lowest_g_value = min([inner_state[0] for inner_state in state_temp_store])
		for var in state_temp_store:
		    if var[0] == lowest_g_value:
			state_temp_store.remove(var)
			check_list.append(var)
			state = var
	else:
		print "fail"
		return False
    print state
    return state
search()
#    if any(checkLower == val for val in ["qwert", "AsDf"])
    
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------





