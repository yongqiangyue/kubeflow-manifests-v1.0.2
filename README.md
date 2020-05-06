# Kubeflow一键安装

国内由于镜像网络问题，Kubeflow 通常安装都是各种磕磕碰碰，以一颗为广大人民谋福利的心，这里提供国内镜像版(阿里云镜像/dockerhub)的一键安装：

kubeflow版本为v1.0.2，对应支持的k8s集群见[链接](https://www.kubeflow.org/docs/started/k8s/overview/)。

#### 安装步骤

**1.生成yaml**
```
python run.py
```

**2.启动**
```
cd yaml
kubectl apply -f .
```

*注：如果需要用local-path文件夹下的yaml文件生成：`kubectl apply -f local-path-storage.yaml`*
*注：Persistent Volume Claims are in Pending State
[链接](https://www.kubeflow.org/docs/started/k8s/kfctl-k8s-istio/#persistent-volume-claims-are-in-pending-state)
# cd storage.yaml
# kubectl apply -f .
*

**3.查看结果**
```
kubectl get pod -nkubeflow
```
