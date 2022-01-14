# @Author: LiuYuZhao
# @Date: 2022-01-13

def is_move_valid(env_data, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """

    x, y = loc
    if act == 'u':
        if x == 0:
            return False

        elif env_data[x-1][y] == 2:
            return False
        else:
            return True

    if act == 'd':
        if x == (len(env_data)-1):
            return False

        elif env_data[x+1][y] == 2:
            return False
        else:
            return True

    if act == 'l':
        if y == 0:
            return False

        elif env_data[x][y-1] == 2:
            return False
        else:
            return True

    if act == 'r':
        if y == (len(env_data[0])-1):
            return False

        elif env_data[x][y+1] == 2:
            return False
        else:
            return True


def valid_actions(env_data, loc):
    lists = []
    if is_move_valid(env_data, loc, 'u'):
        lists.append('u')
    if is_move_valid(env_data, loc, 'd'):
        lists.append('d')
    if is_move_valid(env_data, loc, 'l'):
        lists.append('l')
    if is_move_valid(env_data, loc, 'r'):
        lists.append('r')
    return lists


def move_robot(env_data, loc, act):
    if act in valid_actions(env_data, loc):
        if act == 'u':
            return (loc[0]-1, loc[1])
        if act == 'd':
            return (loc[0]+1, loc[1])
        if act == 'l':
            return (loc[0], loc[1]-1)
        if act == 'r':
            return (loc[0], loc[1]+1)
