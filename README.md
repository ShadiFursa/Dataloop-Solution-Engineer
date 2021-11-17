
# Dataloop Solution Engineer Task

## Part 1 of the Assignment: 

in the PART1 directory in this repository are the some images of what i've done in part 1

## Part 2 of the Assignment:

## Assignment.py walk through:

1) login to Dataloop Platform - once the code is run , a pop-up browser should open, once you're logged in a message that you can close the window should appear.
2) Creates a project - Make sure that there isn't a project with a similar name on the account
3) Creates a Dataset - Make sure that there isn't a dataset with a similar name in the project
4) Adds Labels to the dataset
5) uploads images from a directory to the dataset, classifies the first 2 uploaded images as "Class1" and the rest as "Class2"

### Note: The Path to the directory must be updated 

A Timestamp of upload time will be added to the metadata of each image.
One of the images will have 5 Random Point annotations labeled "key".

## Queries.py Walk through:
1) The First Query filters all the images that have "Class1" Classification.
2) The Second Query Filters all the images that have Point Annotations, and prints the annotations themself.

## Requirements: 
Please Follow instruction on : https://dataloop.ai/docs/sdk-register 

## Run the project: 
Before Running the project make sure you update the path to the folder you want to upload images from.

```
python Assignment.py
python Queries.py
```


