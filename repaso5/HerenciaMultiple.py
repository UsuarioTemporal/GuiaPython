#!/usr/bin/env python3









class Email():
    def __init__(self,password):
        self.__password=password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        self.__password=value

thom =Email('112')
# thom.getPassword='15'
thom.password='45'
print(thom.password)