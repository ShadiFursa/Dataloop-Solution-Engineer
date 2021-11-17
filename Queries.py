# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:32:22 2021

@author: Admin
"""
import dtlpy as dl

#login to the dataloop platform
dl.login()

# get a project 
project = dl.projects.get(project_name='Part-2')

#get the dataset you want to run queries on
dataset = project.datasets.get(dataset_name='my-Dataset')

#create a filter
filters = dl.Filters()

#filter only items with Class1 label
filters.add_join(field='label', values=['Class1'], operator=dl.FILTERS_OPERATIONS_IN)

#get the filtered items from the dataset
pages = dataset.items.list(filters=filters)


#print the number of items in the dataset
print('Number of items in dataset: {}'.format(pages.items_count))


#print the items in the dataset
for page in pages:
        for item in page:
                item.print()
                
print(" \n This is Section The 2nd Query")


filters = dl.Filters()
filters.add(field='annotated', values=True)


#filter onlt the items with point annotation
filters.add_join(field='type', values='point')

#get all the filtered items from the dataset
pages = dataset.items.list(filters=filters)

#print the number of items in the dataset
print('Number of items in dataset: {}'.format(pages.items_count))


for page in pages:
        for item in page:
            item.print()
            # get the annotations on the filtered items
            annotations = item.annotations.list()
            for annotation in annotations:
                print("\n", annotation)