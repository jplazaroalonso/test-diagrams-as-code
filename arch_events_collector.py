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
from diagrams.aws.analytics import DataLakeResource


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

with Diagram("Event Driven Collector", show=True, filename="architecture_events_collector", direction="LR", graph_attr=graph_attr):
   


        
       
 
        
   

    with Cluster ('Pub/Sub - SNS'):
        TOPIC01=SimpleNotificationServiceSnsTopic('TOPIC01')
        TOPIC02=SimpleNotificationServiceSnsTopic('TOPIC02')
        TOPIC03=SimpleNotificationServiceSnsTopic('TOPIC03')
        TOPIC04=SimpleNotificationServiceSnsTopic('TOPIC04')
        TOPIC05=SimpleNotificationServiceSnsTopic('TOPIC05')
        TOPIC06=SimpleNotificationServiceSnsTopic('TOPIC06')
                       
               
    with Cluster('Publisher'):
            APP01=Custom('APP01', quarkusimg)
            APP02=Custom('APP02', quarkusimg)
            APP03=Custom('APP03', quarkusimg)
            APP04=Custom('APP04', quarkusimg)
            APP05=Custom('APP05', quarkusimg)
            APP06=Custom('APP06', quarkusimg)
            
             
            
            

               
    with Cluster('Suscriber'):
     
            COLLECTOR=Custom('APP02', quarkusimg)
    
    with Cluster('DATA Lake'):
        DLAKE=DataLakeResource('')
    
    APP01 >> Edge(color='darkred') >> TOPIC01
    APP02 >> Edge(color='darkred') >> TOPIC02
    APP03 >> Edge(color='darkred') >> TOPIC03
    APP04 >> Edge(color='darkred') >> TOPIC04
    APP05 >> Edge(color='darkred') >> TOPIC05
    APP06 >> Edge(color='darkred') >> TOPIC06
    
    TOPIC01 >> Edge(color='darkred') >> COLLECTOR
    TOPIC02 >> Edge(color='darkred') >> COLLECTOR
    TOPIC03 >> Edge(color='darkred') >> COLLECTOR
    TOPIC04 >> Edge(color='darkred') >> COLLECTOR
    TOPIC05 >> Edge(color='darkred') >> COLLECTOR
    TOPIC06 >> Edge(color='darkred') >> COLLECTOR
    
    COLLECTOR >> Edge(color='darkred') >> DLAKE
    