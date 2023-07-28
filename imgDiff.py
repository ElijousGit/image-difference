from PIL import Image as im
import streamlit as st
import pandas as pd
import torch
import torchvision.transforms as transforms
import tensorflow as tf
import numpy as np

path = './images/img_pair_'
images = ['1', '2', '3']

def imgToTfTensor(image):  
        # Define a transform to convert PIL 
        # image to a Torch tensor
        transform = transforms.Compose([
            transforms.PILToTensor()
        ])
        # Greyscale the image to make it easier for comparing
        greyscale = image.convert('L')

        # Convert pytorch tensor to tensorflow tensor
        pytorch_tensor = transform(greyscale)
        np_tensor = pytorch_tensor.numpy()
        tf_tensor = tf.convert_to_tensor(np_tensor)
        return tf_tensor

def imgDiff(preimage, postimage):
    
    # Convert both images into tensorflow tensors
    preTensor = imgToTfTensor(preimage)
    postTensor = imgToTfTensor(postimage)

    # Subtract difference and print difference
    difference = tf.reduce_sum(preTensor - postTensor).numpy()
    return difference


# Define first (pre) and second (post) image paths
data = []
for i in range(len(images)):
    imagepair = path + images[i]
    print(imagepair)
    preimage = im.open(imagepair + '/pre.jpg')
    postimage = im.open(imagepair + '/post.jpg')

    difference = imgDiff(preimage, postimage)
    data.append([str(i + 1), difference])
    print(data)
df = pd.DataFrame(data, columns=["image#", "difference"])
st.write(df)