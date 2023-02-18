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
from diagrams.aws.security import Cognito
from diagrams.aws.database import  DDB
from diagrams.aws.mobile import Appsync, Amplify
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship


quarkusimg= './my-resources/quarkus.png'
grafanaimg='./my-resources/grafana.png'
android_iosimg='./my-resources/Android-IOS.png'
gameimg='./my-resources/gameicon.png'
rest_img='./my-resources/RESTful-API.png'
livelinkimg='./my-resources/livelink.gif'
securityimg='./my-resources/Security.png'
securityappleimg='./my-resources/apple.png'
securitygoogleimg='./my-resources/google.png'
oauthimg='./my-resources/oauth.png'
identityProviderimg='./my-resources/identityProvider.png'

graph_attr = {
   
    "bgcolor": "transparent"
}

with Diagram("Notifications", show=True, filename="architecture_notifications", direction="LR", graph_attr=graph_attr):
    with Cluster ('MS'):
        APP03=Custom('Notifications', quarkusimg)
        
    with Cluster ('Notificaciones') :
        NOTIFICACIONES=SNS('SNS')
        with Cluster ('Endpoints') :
             Endpoints = Database(  name="End Points" )
        
             PUBSUB=SimpleNotificationServiceSnsTopic('TOPIC')

    with Cluster ('Devices'):
        with Cluster ('Mobile'):
            DEVICE=Custom('Device', android_iosimg)
            
    
    
    Endpoints >> Relationship(color='darkgreen') >> NOTIFICACIONES
    NOTIFICACIONES >> Edge(color='darkred', label='notification') >> PUBSUB
    PUBSUB >> Edge(color='darkred', label='notification') >> DEVICE
    APP03 >> Edge(color='darkgreen') >> NOTIFICACIONES