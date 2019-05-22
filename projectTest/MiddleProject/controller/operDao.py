# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:01
    @author: YangZhen
    @editor：LiJiaHe/GaoJiaYang
    @title: 处理用户移动操作
    @file: gameController.py
"""
import queue

class UserDao:
    def __init__(self, num_list, vector):
        """
        构造方法
        :param num_list: 待移动列表
        :param vector: 移动点坐标
        """
        self.num_list = num_list
        self.vector = vector

    def remove(self,atlas, num1, num2):
        """
        消除操作(LiJiaHe)
        :return:
        """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # 直接调find，使用消除功能，atlas为6*6消消乐游戏地图参数，num1为X轴，num2为Y轴
    q = queue.Queue(maxsize=0)
    block_color = atlas[num1][num2]
    if block_color == 0:
        return False

    q.put((num1, num2))
    cnt = 0
    # qsize判断队列长度，不为空则循环
    while q.qsize():
        # get从队列中获取任务，并且从队列中移除此任务。
        num1, num2 = q.get()
        # 点击位置(num1, num2)的周围元素
        for i in range(4):
            s = dx[i] + num1
            t = dy[i] + num2

            if s < 0 or s > 5 or t < 0 or t > 5 or atlas[s][t] != block_color:
                continue
            cnt += 1
            # 若同色，则将这个位置初始化为0，被标记为0的数就相当于被消除了
            atlas[s][t] = 0
            # 将(s, t)加入队列
            q.put((s, t))
    atlas_zero_to_end(atlas)
    return atlas

    def zero_to_end(list_target):
    new_list = [item for item in list_target if item != 0]
    new_list += [0] * list_target.count(0)
    # return new_list
    # list_target = new_list  #此时修改的是变量，不是传入的对象
    list_target[:] = new_list[:]
    return list_target

    def print_atlas(list_atlas):
    for r in range(len(list_atlas)):
        for c in range(len(list_atlas[r])):
            print(list_atlas[r][c], end=" ")
        print()

    #  在核心处理函数处理完，将列表中的零元素放置最右端和最上端
    def atlas_zero_to_end(atlas):
    # 先进行横向向有移动0元素
    for r in range(6):
        row_list = []
        for c in range(6):
            row_list.append(atlas[r][c])

        zero_to_end(row_list)

        for c in range(6):
            atlas[r][c] = row_list[c]
    # 再进行0元素整体上移
    for c in range(6):
        col_list = []
        for r in range(5, -1, -1):
            col_list.append(atlas[r][c])

        zero_to_end(col_list)

        for r in range(5, -1, -1):
            atlas[r][c] = col_list[5 - r]

    print_atlas(atlas)

    def can_remove(self):
        """
        判断列表是否可以消除
        :return: 可以消除返回True，不可以消除返回False
        """
        pass

    def __remove_row(self):
        """
        游戏列表行消除操作(LiJiaHe)
        :return:
        """
        pass

    def __remove_col(self):
        """
        游戏列表列消除操作
        :return:
        """
