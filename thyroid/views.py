from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import pickle
#from .forms import userinputForm
import numpy as np
import os

def getinput(request):
    return render(request, 'thyroid/Input.html')

def loadModel(request):
    import pickle

    f1=request.GET.get('rt3u')
    f2=request.GET.get('t4')
    f3=request.GET.get('t3')
    f4=request.GET.get('tsh')
    f5=request.GET.get('dtsh')

    my_Details=[f1,f2,f3,f4,f5]
    array = np.asarray(my_Details, dtype=np.float64)
    a = array.reshape(1, -1)
    loaded_model= pickle.load(open("C:/Users/Lenovo/PycharmProjects/FYP/thyroid/final5dtc_model.sav",'rb'))

    # try:
    #     loaded_model = pickle.load(open("C:/Users/Lenovo/PycharmProjects/FinalYearProject/thyroid/final13dtc_model.sav",'rb'))
    # except:
    #     print("File not loaded")

    print("File loaded")

    result = loaded_model.predict(a)
    lresult = result.tolist()
    abc = lresult[0] - 1
    abc
    classes = ["normal", "hyper", "hypo"]
    result = classes[abc]
    dic = {'output': result}
    #print(result)
    return render(request, 'thyroid/Output.html', dic)


