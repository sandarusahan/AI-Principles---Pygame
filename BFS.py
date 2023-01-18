import math

class BFS_Algorithm:
    
    def __init__(self, resolution, robot_radius):
        
        self.obstacle_map = None
        self.resolution = resolution
        self.robot_radius = robot_radius # agent size in grids cells

        self.ox = None
        self.oy = None
        self.min_x = None
        self.min_y = None
        self.max_x = None
        self.max_y = None
        self.x_width = None
        self.y_width = None

        self.motion = self.get_motion_model_4n()
        # self.motion = self.get_motion_model_8n()
        
    class Node:
        def __init__(self, x, y, cost, parent_index, parent):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index  # index of previous Node
            self.parent = parent

    
    def start_with_bfs(self, sx, sy, gx, gy, obs_map_arr):
        goal_reached = False
        self.calc_obstacle_map(obs_map_arr)
        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1, None)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1, None)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_index(start_node)] = start_node
        closed_set[self.calc_index(start_node)] = start_node

        while 1:
            
            if len(open_set) == 0:
                print("Open set is empty..")
                break
            

            current = open_set.pop(list(open_set.keys())[0])
            c_id = self.calc_index(current)
            closed_set[c_id] = current


            # checking if goal is reached, break loop if it does
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Goal Reached") 
                goal_reached = True
                                    
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                print("cost :" ,goal_node.cost)
                break
            
            
              # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                current.y + self.motion[i][1],
                                current.cost + self.motion[i][2], c_id, None)
                n_id = self.calc_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):                     
                    continue


            ######################Graph Search ##########################

                if (n_id not in closed_set) and (n_id not in open_set):
                    node.parent = current
                    open_set[n_id] = node            
                algorithm = "BFS Graph" 
            
            ######################Tree Search ##########################
                # open_set[n_id] = node
                # closed_set[n_id] = node
                # node.parent = current
                # algorithm = "BFS Tree"       	
 

        rx, ry = self.calc_final_path(goal_node, closed_set)
        rx.reverse()
        ry.reverse()
        return rx, ry, goal_reached, algorithm

    @staticmethod
    def get_motion_model_4n():
        """
        Get all possible 4-connectivity movements.
        :return: list of movements with cost [[dx, dy, cost]]
        """
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]
        return motion
    
    @staticmethod
    def get_motion_model_8n():
        # dx, dy, cost
        motion =[[-1, -1, math.sqrt(2)],
                [-1, 0, 1],
                [-1, 1, math.sqrt(2)],
                [0, 1, 1],
                [1, 1, math.sqrt(2)],
                [1, 0, 1],
                [1, -1, math.sqrt(2)],
                [0, -1, 1]
                ]
        return motion
    ##get index from coordinates based on x or y
    ## use in determining start node

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)


    def calc_final_path(self, goal_node, closedset):
        # generate final path

        rx, ry = [self.calc_position(goal_node.x, self.min_x)], [
            self.calc_position(goal_node.y, self.min_y)]
            
        n = closedset[goal_node.parent_index]  # colsedset is a dict, use index to retrieve node

        while n is not None:
            rx.append(self.calc_position(n.x, self.min_x))
            ry.append(self.calc_position(n.y, self.min_y))
            n = n.parent

        return rx, ry


    ##get index from coordinates based on x and y
    def calc_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    # def calc_grid_index(self, node):
    #     return (node.y - self.min_y) * self.xwidth + (node.x - self.min_x)

    
    def verify_node(self, node):
        px = self.calc_position(node.x, self.min_x)
        py = self.calc_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False
        
        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True
    
    ##get coordinates from index in grid system
    def calc_position(self, index, minp):
        pos = index * self.resolution + minp
        return pos


    def calc_obstacle_map(self, map_arr):

        # Obstacle and free grid positions
        ox, oy = [], [] #obstacle
        fx, fy = [], [] #free 

        for iy in range(map_arr.shape[0]):
            for ix in range(map_arr.shape[1]):
                if map_arr[iy, ix] == 1:
                    ox.append(ix)
                    oy.append(iy)
                else:
                    fx.append(ix)
                    fy.append(iy)

        self.ox = ox
        self.oy = oy
        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))


        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)

        self.obstacle_map = [[0 for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.robot_radius:
                        self.obstacle_map[ix][iy] = 1
                        break
