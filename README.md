## Inception_Transfer_learning
This Project uses knowledge gained by imagenet weights and transfer learning from it to build your custom Image Classifier. This work also demonstrate how you can used pretrained network and transfer it's learning to get good results with even very less training data.
Instructions:

Download the ImageNet graph for tensorflow from "https://drive.google.com/file/d/1nz0hs_hwexv98OWbB80M0e67IVeBApy5/view?usp=sharing" and keep in Model folder if you do not have it already KEEP THE NAME OF GRAPH AS "classify_image_graph_def.pb"


Keep atleast 10 images in Each class for training. For best results give resized images of 250 * 250 or 512 * 512 
it automatically scales and do the transformation needed for model
Read retrain.py (Find Resize ) you can see all the various agumentation you can apply by reading documentation inside it.

For Retraining 

 --how_many_training_steps : No. of epocs you want to train (by default)
 --output_graph : where you want to keep the output graph of transfer learning
 --model_dir : provide the name of folder where "imagenet" (or the graph on which you want to do transfer learning)  graph is saved. It should have name "classify_image_graph_def.pb"
 --output_labels : give the name of the file in which name of the classes to be saved ( you need to provide this at classification time, keep it "retrained_labels.txt" to avoid any change in CheckClassify)
 --image_dir : provide the image directory in which training images are saved (keep each class in seperate folder with class name[label] as folder name)

> python retrain.py --bottleneck_dir=./bottlenecks --how_many_training_steps 4000 --model_dir=./Model --output_graph=./retrained_graph.pb --output_labels=./retrained_labels.txt --image_dir ./Train_Images

For Testing / Classification

1) for single image 
> python classifier.py <address of image>

2) For many images
 
 keep all the images needed to be classified in one folder
 by default JPG/JPEG images are only used but if you want to use it for other extension too then open CheckClassify.py and find "findit()" there comment is written for adding png , you can change 
 it according to your need.
 
 keep the retrained graph obtained by retraining (inside the folder provided in --output_graph argument of retrain.py) with name "retrained_graph.pb" in same folder as CheckClassify.py or You have
 to change the address in CheckClassify.py (search in file "#weight address" and replace "retrained_graph.pb" with the address of your weight)
 
 keep the labels obtained by retraining (inside the folder provided in --output_labels argument of retrain.py) with name "retrained_labels.txt" in same folder as CheckClassify.py or You have
 to change the address in CheckClassify.py (search in file "#label address" and replace "retrained_labels.txt" with the address of your label file)
 
 Keep the images needed for Test in "Test_Images" folder in same directory as CheckClassify.py or change in "CheckClassify.py" file root_dir variable
 
 > python CheckClassify.py
 
 Output : Inside test directory folders with class names are made and images predicted in the respective class are copied.
 
 For Changing Threshold you can make changes in CheckClassify.py Classifier() 
