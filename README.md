# Maleria detection

***Simulation link: https://maleria.herokuapp.com/***

### Overview
This project aims to classify the maleria desiese based on the cell image. There are two types of cell image used here
one is <code>Parasite</code> and another is non parasite ie. <code>Uninfected</code>. The model is trained using the 
<code> Deep Convolutional nueral network</code> with other layers. Model has achieved **<code>97%</code>** of accuracy on test dataset
for both type of label ie. Parasite and Uninfected.

### Model achitecture
<pre><code>
________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
conv2d_20 (Conv2D)          (None, 48, 48, 64)        4864      
                                                                
conv2d_21 (Conv2D)          (None, 48, 48, 64)        102464    
                                                                
batch_normalization_6 (Batc  (None, 48, 48, 64)       256       
hNormalization)                                                 
                                                                
max_pooling2d_6 (MaxPooling  (None, 24, 24, 64)       0         
2D)                                                             
                                                                
dropout_6 (Dropout)         (None, 24, 24, 64)        0         
                                                                
conv2d_22 (Conv2D)          (None, 24, 24, 128)       73856     
                                                                
conv2d_23 (Conv2D)          (None, 24, 24, 128)       147584    
                                                                
conv2d_24 (Conv2D)          (None, 24, 24, 128)       147584    
                                                                
batch_normalization_7 (Batc  (None, 24, 24, 128)      512       
hNormalization)                                                 
                                                                
max_pooling2d_7 (MaxPooling  (None, 12, 12, 128)      0         
2D)                                                             
                                                                
dropout_7 (Dropout)         (None, 12, 12, 128)       0         
                                                                
conv2d_25 (Conv2D)          (None, 12, 12, 256)       295168    
                                                                
conv2d_26 (Conv2D)          (None, 12, 12, 256)       590080    
                                                                
conv2d_27 (Conv2D)          (None, 12, 12, 256)       590080    
                                                                
conv2d_28 (Conv2D)          (None, 12, 12, 256)       590080    
                                                                
conv2d_29 (Conv2D)          (None, 12, 12, 256)       590080    
                                                                
batch_normalization_8 (Batc  (None, 12, 12, 256)      1024      
hNormalization)                                                 
                                                                
max_pooling2d_8 (MaxPooling  (None, 6, 6, 256)        0         
2D)                                                             
                                                                
flatten_2 (Flatten)         (None, 9216)              0         
                                                                
dropout_8 (Dropout)         (None, 9216)              0         
                                                                
dense_4 (Dense)             (None, 512)               4719104   
                                                                
dense_5 (Dense)             (None, 1)                 513       
                                                                
=================================================================
Total params: 7,853,249
Trainable params: 7,852,353
Non-trainable params: 896
_________________________________________________________________
</code></pre>

### Folder arrangement
<pre><code>
├───home
│   ├───migrations
│   │   └───__pycache__
│   ├───model.hd5
│   │   ├───assets
│   │   └───variables
│   └───__pycache__
├───MaleriaDetection
│   └───__pycache__
├───media
├───static
│   └───Dataset
│       ├───Test
│       │   ├───Parasite
│       │   └───Uninfected
│       └───Train
│           ├───Parasite
│           └───Uninfected
├───staticfiles
└───templates
</code></pre>

Thank you
