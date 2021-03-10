from django.shortcuts import render,redirect
import pickle
import os
from . models import Prediction

# Create your views here.

def index(request):
    res = Prediction.objects.all()
    return render(request,"index.html",{'res':res})
def test(request):
    ppw = int(request.POST['ppw'])
    pn = int(request.POST['pn'])
    mi = int(request.POST['mi'])
    appm = int(request.POST['appm'])
    modulepath = os.path.dirname(__file__)
    model = pickle.load(open(os.path.join(modulepath,'taxi.pkl'),'rb'))
    res = str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
    # return render(request,"index.html",{'res':res})
    pre = Prediction(ppw=str(ppw),pn=str(pn),mi=str(mi),appm=str(appm),result=res) #ORM
    pre.save()
    return redirect('index')
