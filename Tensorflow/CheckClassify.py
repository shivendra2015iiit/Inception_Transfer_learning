import numpy as np
import tensorflow as tf
import os
from shutil import copyfile
import shutil

import re
#Change find it function to run for .png or .jpeg file too
def findit(string):
    b=re.search(".*\.jpg",string,re.IGNORECASE)
    c=re.search(".*\.jpeg",string,re.IGNORECASE)
    # uncomment line below for png files to be included and add "or d in if statement line 13"
    # d = re.search(".*\.jpeg",string,re.IGNORECASE)
    if b or c:
        return True
    else:
        return False

def classifier(address):
    # Read in the image_data
    image_data = tf.gfile.FastGFile(address, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("./retrained_labels.txt")]                        #label address (change it if you changed default settings)



    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        try:
            predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            #most certain
            certainity=True
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))
                if (certainity==True):
                    certainity=False
                    return human_string



        except Exception as e:
            return "Error"

def main():
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("./retrained_labels.txt")]

    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:               #Weight address (change it if you changed default settings)
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')



    # Give path to image directory

     # change address of to image directory needed to checked >> remember to keep '/' at the end

    root_dir = "/home/intern_eyecare/shivendra/Inception_Transfer_learning/Test_Image/"

    directories=[]
    for i in range(len(label_lines)):
        directories.append(root_dir+"/"+label_lines[i])
        if os.path.exists(directories[i]):
            shutil.rmtree(directories[i])
        os.makedirs(directories[i])

#Change find it function to run for .png file too line 9

    for filename in os.listdir(root_dir):
        if(findit(filename)):
            label_returned=classifier(root_dir+filename)
            if ( label_returned!="Error"):
                print("copying to ",)
                copyfile(root_dir+filename,root_dir+"/"+label_returned+"/"+filename)
            else:
                print("Error")







if __name__=="__main__":
    main()
