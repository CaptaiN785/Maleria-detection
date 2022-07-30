import os
from django.shortcuts import render, HttpResponse
from django.core.files.storage import default_storage
import numpy as np
import tensorflow
from PIL import Image

## Loading the model for prediction
try:
    model = tensorflow.keras.models.load_model("home/model.hd5")
    print("Model loaded successfully.")
except:
    print("Unable to load model.")


# Create your views here
def index(request):
    context = {'result':None}
    if request.method == "POST":
        file = request.FILES['uploaded_image']
        filename = default_storage.save(file.name, file)
        fileurl = default_storage.path(filename)
        # print(Predict(fileurl))
        result = Predict(fileurl)
        context['result'] = result
        os.remove(fileurl)

    return render(request, 'index.html', context=context)





def Predict(image_path):

    label = {0:"Parasite", 1:"Uninfected"}

    
    img = Image.open(image_path).resize((96, 96), Image.ANTIALIAS)
    img = np.array(img)/255.0
    # model.predict(img[None,:,:])
    # print(img.shape)

    # img = cv.resize(img, (96, 96), interpolation=cv.INTER_AREA)/255.0
    
    img = np.expand_dims(img, 0)
    # print("Shape of array is : ", img.shape)
    result = model.predict(img)
    return label[np.round(result[0][0])]