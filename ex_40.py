# -*-  coding:utf-8 -*-

class Song(object):
    def __init__(self,Iyrics):
        self.Iyrics = Iyrics

    def sing_me_a_song(self):
        for line in self.Iyrics:
            print(line)

happy_day = Song(['Happy birthday to you',"I don't want to get sued"])
happy_day.sing_me_a_song()