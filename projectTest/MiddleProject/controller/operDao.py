# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:01
    @author: YangZhen
    @editor：LiJiaHe-LeoLi/GaoJiaYang
    @title: 处理用户移动操作
    @file: gameController.py
"""


class UserDao:
    def __init__(self, num_list, vector):
        """
        构造方法
        :param num_list: 待移动列表
        :param vector: 移动点坐标
        """
        self.num_list = num_list
        self.vector = vector

    def remove(self):
        """
        消除操作(LiJiaHe)
        :return:
        """
        self.__remove_row()
        self.__remove_col()
        # 首先实现相邻横向相同元素合并
    def merge(list_target):
        for i in range(len(list_target)-1):
            # 如果遇到左边或者右边有相同元素，则将元素变成0
            # 【未完成】问题，如果i+2+3,或者i-2-3的数字都相等，怎么办？
            if list_target[i] == list_target[i+1] or list_target[i] == list_target[i-1]:
                list_target[i]

        # 再将0元素统一放到最后，有几个零，依次从第一个15分，第二个加10分分别统计最后汇总，核算出本轮分数
        # 【未完成】问题，核算出0的个数，如何进行分数累加汇总？如何将列表中0元素去除显示
        zero_to_end(list_target)
        # 核算出list_target中有多少个0元素，核算分数
        num_zero == list_target.count(0)
        # 再将零元素删除显示


    def zero_to_end(list_target):
        new_list = [item for item in list_target if item != 0]
        new_list += [0]*list_target.count(0)
        list_target[:] = new_list[:]
        return list_target
    
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
