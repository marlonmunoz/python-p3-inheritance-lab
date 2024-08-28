#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge=None):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge if knowledge is not None else []
    
    def learn(self, new_info):
        self.knowledge.append(new_info)
        pass