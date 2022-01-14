# @Author: LiuYuZhao
# @Date: 2022-01-13

from draw import draw_window
from map import map

if __name__ == '__main__':
    # define pixels peer block
    block_size = 50
    # init map
    Map = map()
    # draw main window
    draw_window(Map.get_map_size(), block_size, Map.set_blocks(),
                Map.set_treasure(), Map.env_data, Map.get_start())
