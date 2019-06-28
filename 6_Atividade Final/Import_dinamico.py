# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:39:35 2019

@author: FelipePC
"""
from importlib import import_module
#import sklearn.neighbors.KNeighborsClassifier

def dynamic_import(abs_module_path, class_name):
    module_object = import_module(abs_module_path)

    target_class = getattr(module_object, class_name)

    return target_class




item = "neighbors"
mymodule= dynamic_import('sklearn.neighbors',"KNeighborsClassifier")

model = mymodule()


