# RandomRobot

随机寻宝机器人

## 函数声明

### `RandomRobot.py`  

> 主程序



### `map.py`

> `self.env_data` 是地图，
>
> > 其中3代表宝藏
> >
> > 2代表方块 [不可通行] ，
> >
> > 1 代表初始位置 [可通行] 
> >
> > 0代表通路 [可通行]

> `get_map_size()` 以元组的形式返回行列数
>
> `get_start()` 以元组的形式返回起始位置，代码可简化
>
> `set_blocks()` 返回一个列表，存储不可通行的坐标
>
> `set_treasure()` 以元组的形式返回宝藏位置坐标



### `action.py` 

> `is_move_valid()` 判定是否可通行
>
> `valid_actions()` 返回当下可行动的方位
>
> `move_robot()` 移动并返回更新后的位置



### `draw.py` 

>`draw_window()` 绘制主界面
>
>`draw_blocks()` 绘制方块 [不可通行]
>
>`draw_treasure()` 绘制宝藏 

![7sPMzd.gif](https://s4.ax1x.com/2022/01/19/7sPMzd.gif)
