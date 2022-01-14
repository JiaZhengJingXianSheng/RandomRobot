# @Author: LiuYuZhao
# @Date: 2022-01-13

class map:
    def __init__(self):
        self.env_data = [
            [3, 2, 2, 2, 2, 2, 2, 2, 1],
            [0, 0, 2, 2, 2, 2, 2, 0, 0],
            [2, 0, 0, 2, 2, 2, 0, 0, 2],
            [2, 2, 0, 0, 2, 0, 0, 2, 2],
            [2, 2, 2, 0, 0, 0, 2, 2, 2]]

    # get map rows and columns
    def get_map_size(self):
        self.rows = len(self.env_data)
        self.columns = len(self.env_data[0])
        return (self.rows, self.columns)

    # get start local
    # this function can be simplify
    def get_start(self):
        loc_map = {}
        for i in range(len(self.env_data)):
            for j in range(len(self.env_data[i])):
                if self.env_data[i][j] == 1:
                    loc_map['start'] = (i, j)
                if self.env_data[i][j] == 3:
                    loc_map['destination'] = (i, j)
        self.robot_current_loc = loc_map['start']
        return self.robot_current_loc

    # get blocks local list
    def set_blocks(self):
        self.block_lists = []
        for i in range(len(self.env_data)):
            for j in range(len(self.env_data[i])):
                if self.env_data[i][j] == 2:
                    self.block_lists.append((i, j))
        return self.block_lists

    # get treasure local
    def set_treasure(self):
        for i in range(len(self.env_data)):
            for j in range(len(self.env_data[i])):
                if self.env_data[i][j] == 3:
                    return (i, j)
