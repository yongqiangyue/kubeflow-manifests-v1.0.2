#coding:utf-8

import os

files = os.listdir("./kustomize")

for fname in files:
    filename = "./kustomize/%s"%(fname)
    cmd = "kubectl kustomize %s"%(filename)
    print(cmd)
    with os.popen(cmd) as fr:
        with open("./yaml/%s.yaml"%fname,"w") as fw:
            data = fr.read()
            print(data)
            fw.write(data)
