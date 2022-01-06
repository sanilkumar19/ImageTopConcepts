# ImageTopConcepts

This project extracts the top concepts from any number of images supplied to the system.

## Building knowledge graphs using Object Detection

#### Step1: 
Go to https://cocodataset.org/#explore, and download 100 images for building your image database. For example, if input the “table” for exploration, many images are displayed. Select 100 images and download them to your own computer. You can choose any one keyword such as “cat”, “car”, “bowl”, “apple”, “clock”, and other words included in the COCO database. Most popular concepts are included in the following figure. After you select 100 images, put those images into one folder named “image100”. Extract all concepts from each image and build a concept pool for all 100 images. For example, if the first image has concepts “cat” and “table”, the second image has “bowl” and “banana”, and the third image has “sofa” and “chair”, the concept pool of those 3 images is {“cat”, “table”, “bowl”, “banana”, “sofa”, “chair”}.
 
![image](https://user-images.githubusercontent.com/36981925/148312627-8c960772-6a04-44b4-9d80-7495dae9b09d.png)



#### Step2:
For example, manually build one knowledge graph for one image, which can be selected from those 100 images

Image Selected – img (13):

![image](https://user-images.githubusercontent.com/36981925/148311056-79ba6453-b215-4e0f-9381-b2cb70e46db5.png)


Knowledge graph:
 
![image](https://user-images.githubusercontent.com/36981925/148311085-f784c0c7-bc75-40fc-b99b-48a1844c518e.png)


#### Step3: 
Write a computer program to construct the frequency-based knowledge matrix as shown in the subsection 3.2 of the paper “Object Detection Meets Knowledge Graphs”. This frequency-based knowledge matrix has the size of all concepts extracted in the Step1. For example, if 196 concepts are extracted from 100 images in the Step1, this frequency-based knowledge matrix’s size will be 196 x 196. Using the Equation (1) in the paper “Object Detection Meets Knowledge Graphs”, each element value of this matrix can be calculated.
