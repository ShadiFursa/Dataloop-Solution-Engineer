# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:09:29 2021

@author: Admin
"""
import dtlpy as dl
import os
from datetime import datetime
from random import randrange


#log in to dataloop platform
dl.login()
#create a project for part 2 of the task
project = dl.projects.create(project_name='Part-2')
#create a dataset for the part 2 project
dataset = project.datasets.create(dataset_name='my-Dataset')
#create labels
labels = [
    dl.Label(tag='Class1', color=(34, 6, 231)),
    dl.Label(tag='Class2', color=(38, 12, 105)),
    dl.Label(tag='Class2', color=(102, 17, 231))
    
]
#add labels to dataset
dataset.add_labels(label_list=labels)

#path to the directory with the images
path="/path/to/dir/here"

i=0
#iterate throught images in the directory and upload them to the dataset
for img in os.listdir(path):
    now=datetime.now()
    item=dataset.items.upload(os.path.join(path, img))
    item.metadata['user'] = dict() 
    item.metadata['user']['UTM'] = now.strftime("%m/%d/%Y, %H:%M:%S") #add upload timestamp for each image
    item = item.update() # update metadata
    builder = item.annotations.builder() #create builder
    if i <2: #add Class1 classification to the first two images
        builder.add(annotation_definition = dl.Classification(label="Class1"))
    else: #add Class2 classification to the rest
        builder.add(annotation_definition = dl.Classification(label="Class2"))
    if i==4: # choose the 5th image that is uploaded and add point annotation
        for j in range(0,5):
            x=randrange(274)
            y=randrange(182)
            builder.add(annotation_definition=dl.Point(x=x,
                                           y=y,
                                           label='key'))
    item.annotations.upload(builder) # update the image annotation and/or classification
    i+=1


dl.logout()