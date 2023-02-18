from platform import node
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.database import Aurora
from diagrams.aws.compute import ElasticKubernetesService
from diagrams.aws.network import VPC
from diagrams.aws.management import  Cloudwatch
from diagrams.custom import Custom
from diagrams.aws.mobile import APIGatewayEndpoint, APIGateway
from diagrams.k8s.compute import Pod

from diagrams.onprem.container import Docker
from diagrams.onprem.client import Users
from diagrams.k8s.compute import Pod
from urllib.request import urlretrieve

from diagrams.aws.devtools import XRay

from diagrams.aws.storage import S3
from diagrams.firebase.base import Firebase
from diagrams.firebase.develop import Authentication
from diagrams.aws.integration import  SNS ,SimpleNotificationServiceSnsTopic
from diagrams.aws.security import WAF


quarkusimg= './my-resources/quarkus.png'
grafanaimg='./my-resources/grafana.png'
android_iosimg='./my-resources/Android-IOS.png'
gameimg='./my-resources/gameicon.png'
rest_img='./my-resources/RESTful-API.png'
livelinkimg='./my-resources/livelink.gif'
securityimg='./my-resources/Security.png'
securityappleimg='./my-resources/apple.png'
securitygoogleimg='./my-resources/google.png'
sidecarimg='./my-resources/sidecar.png'

graph_attr = {
   
    "bgcolor": "transparent"
}

with Diagram("Sidecar Pattern", show=True, filename="Sidecar_pattern", direction="TB", graph_attr=graph_attr):
   
        with Cluster ('Wallet'):
            WALLET=Custom('WALLET', android_iosimg)
               
        with Cluster('MS-APP Pod'):
            AppPod=Pod('POD MS-APP') 
            with Cluster('Isolated Container'):
                Sidecar= Custom('',sidecarimg)
                
            with Cluster('Isolated Container'):
                APP01=Docker('App-01')
                APP02=Docker('App-02')
                APPN=Docker('App-n')
                
        WALLET >>Edge(color='green')>> Sidecar
        Sidecar >>Edge(color='red')>> APP01
        Sidecar >>Edge(color='red')>> APP02
        Sidecar >>Edge(color='red')>> APPN
     