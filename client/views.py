from django.http import HttpResponse
from django.shortcuts import render
import subprocess
import os
# import json


def login(request):
    output = ""
    if request.method == "POST":
        cluster = request.POST['cluster']
        namespace = request.POST['namespace']
        secret_name = request.POST['secret_name']
        secret_type = request.POST['secret_type']
        key = request.POST.getlist('data_key')
        value = request.POST.getlist('data_value')
        myfiles = request.FILES.getlist('input_file')
        for f in myfiles:
            handle_uploaded_file(f)
        if cluster == "momo-on-prem":
            url_cert = os.environ.get('MOMO_ON_PREM_CERT')
        if cluster == "devops":
            url_cert = os.environ.get('DEVOPS_CERT')
        if url_cert:
            for i, val in enumerate(key):
                encrypted = subprocess.check_output(["echo -n "+value[i]+" | kubeseal --cert "+url_cert+" --raw --from-file="+key[i]+"=/dev/stdin --namespace "+namespace+" --name "+secret_name+""], shell=True)
                output = output + key[i]+": "+encrypted.decode("utf-8")+"\n"
            for f in myfiles:
                encrypted = subprocess.check_output(["kubeseal --cert "+url_cert+" --raw --from-file=media/files/"+f.name+" --namespace "+namespace+" --name "+secret_name+""], shell=True)
                output = output + f.name+": "+encrypted.decode("utf-8")+"\n"
                os.remove("media/files/"+f.name)
        return render(request, 'client/encrypt.html', {"output" : output})
    return render(request, 'client/encrypt.html')

def handle_uploaded_file(f):
    # path = settings.MEDIA_ROOT+"/photos/"+f.name
    path = "media/files/" + f.name
    file = open(path, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
    file.close()
    