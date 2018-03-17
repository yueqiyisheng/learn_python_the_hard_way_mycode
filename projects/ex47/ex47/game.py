# -*- coding:utf-8 -*-
class Room(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self,direction):
        return self.paths.get(direction,None) #安全方式提取字典

    def add_paths(self,paths):
        self.paths.update(paths)