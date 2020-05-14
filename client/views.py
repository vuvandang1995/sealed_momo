from django.http import HttpResponse
from django.shortcuts import render
import subprocess
import os
import json



def login(request):
    if request.method == "POST":
        # print(request.POST)
        # MyLoginForm = LoginForm(request.POST)
        # if MyLoginForm.is_valid():
        #     cluster = MyLoginForm.cleaned_data['cluster']
        #     namespace = MyLoginForm.cleaned_data['namespace']
        #     # useless_cat_call = subprocess.check_output(["echo -n fasd | kubeseal --cert http://172.16.9.221/sealed-controller/v1/cert.pem --raw --from-file=/dev/stdin --namespace bar --name mysecret"], shell=True)
        #     # return render(request, 'client/encrypt.html', {"ketqua" : useless_cat_call.decode("utf-8")})
        #     # return render(request, 'client/encrypt.html', {"ketqua" : useless_cat_call.decode("utf-8")})
        #     print(cluster)
        cluster = request.POST['cluster']
        namespace = request.POST['namespace']
        secret_name = request.POST['secret_name']
        secret_type = request.POST['secret_type']
        list_envs = json.loads(request.POST['list_envs'])
        if cluster == "momo-on-prem":
            url_cert = os.environ.get('MOMO_ON_PREM_CERT')
        if cluster == "devops":
            url_cert = os.environ.get('DEVOPS_CERT')
        
        for data in list_envs:
            encrypted = subprocess.check_output(["echo -n "+next(iter(data.values()))+" | kubeseal --cert "+url_cert+" --raw --from-file="+next(iter(data))+"=/dev/stdin --namespace "+namespace+" --name "+secret_name+""], shell=True)
            
            print(next(iter(data))+":"+encrypted.decode("utf-8"))
    return render(request, 'client/encrypt.html')