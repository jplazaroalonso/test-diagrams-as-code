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

with Diagram("Event Driven", show=True, filename="architecture_events", direction="LR", graph_attr=graph_attr):
   


        
       
 
        
   

    with Cluster ('Pub/Sub - SNS'):
        PUBSUB=SimpleNotificationServiceSnsTopic('TOPIC')
                       
               
    with Cluster('Publisher'):
            APP01=Custom('APP01', quarkusimg)
            
            

               
    with Cluster('Suscriber'):
     
            APP02=Custom('APP02', quarkusimg)
    
    APP01 >> Edge(color='darkred') >> PUBSUB
    PUBSUB >> Edge(color='darkred') >> APP02