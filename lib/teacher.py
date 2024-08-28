#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name, knowledge = None):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge if knowledge is not None else ["default knowledge"]

    def teach(self):
        return random.choice(self.knowledge)
        pass