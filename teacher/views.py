from django.shortcuts import render
import pandas as pd
from django.http import HttpResponseRedirect
import csv

# Create your views here.
def show(request):
    lst=[x for x in range(2,20,2)]
    df=pd.read_csv(r'D:\djangop\stud.csv')
    return render(request,'first.html',{"even":lst,"name":df})
def stuentry(request):
    if request.method=='POST':
        stu_dict=request.POST
        with open(r'D:\djangop\stud.csv','a') as st:
            Val=csv.writer(st)
            L=[]
            for x in stu_dict:
                if x=="rollno":
                    L.append(stu_dict[x])
                if x=="name":
                    L.append(stu_dict[x])

            Val.writerow(L)

    return render(request,'stuentry.html')
