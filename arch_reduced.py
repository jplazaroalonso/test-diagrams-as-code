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
   
    "bgcolor": "white"
}

with Diagram("Basic Application Architecture", show=True, filename="architecture_reduced", direction="TB", graph_attr=graph_attr):
   

    with Cluster ('Access'):
        Perimeter=WAF('')
        agw = APIGateway('API GW')
        
    with Cluster ('Wallet'):
        WALLET=Custom('WALLET', android_iosimg)
   
    with Cluster ('APP'):
        APP=Custom('MOBILE', android_iosimg)
   
    with Cluster ('Game'):
        GAME=Custom('GAME', gameimg)
        
    with Cluster ('Bucket'):
        bucket = S3('S3-Bucket')
        
    with Cluster ('Observability'):
        OBS=[XRay('Trace') , Cloudwatch('CloudWatch')]
        
       
 
        
   
    with Cluster ('Database') :
        DB=Aurora('Aurora')
        NOSQL=DDB('NoSQL')
        
    with Cluster ('Notificaciones') :
        NOTIFICACIONES=SNS('SNS')

    with Cluster ('Monitoring'):
        GRAFANA=Custom('GRAFANA', grafanaimg)

    with Cluster ('Pub/Sub - SNS'):
        PUBSUB=SimpleNotificationServiceSnsTopic('TOPIC')
                       
    with Cluster ('Security'):
        with Cluster('SEC-TOOLS'):
            SEC=Custom('',securityimg)   
            with Cluster('OAUTH'):
                AUTH=[Custom('',oauthimg), Amplify(''),Cognito('')]
           
   
    with Cluster ('Security Providers'):
        Providers=Custom('',identityProviderimg)   
        with Cluster('Auth'):
            APPLE=Custom('APPLE', securityappleimg)
            GOOGLE=Custom('APPLE', securitygoogleimg)
    SEC >> Edge(color='RED',style="dotted")>> Providers
 
   
    with Cluster ('Kubernetes'):
        EKS= ElasticKubernetesService('EKS')
        
               
        with Cluster('MS-APP Pod'):
            AppPod=Pod('POD MS-APP')  
            with Cluster('MS-Backend'):
                APP01=Custom('clientManager', quarkusimg)
                APP02=Custom('operations', quarkusimg)
                APP03=Custom('Notifications', quarkusimg)
                APP04=Custom('Sites', quarkusimg)
                
        with Cluster('MS-APP SUPORT'):
             
            AppPod2=Pod('POD MS-SUPPORT')  
            with Cluster('MS-Backend'):

                APP05=Custom('Resources', quarkusimg)
                APP06=Custom('Forms', quarkusimg)
       
        AppPod >>Edge(color='black',style="dotted")>> OBS
        AppPod2 >>Edge(color='black',style="dotted")>> OBS
       

        agw >> Edge(color='darkgreen', label='https') >> APP01
        agw >> Edge(color='darkgreen', label='https') >> APP02
        agw >> Edge(color='darkgreen', label='https') >> APP03
        agw >> Edge(color='darkgreen', label='https') >> APP04
        agw >> Edge(color='darkgreen', label='https') >> APP05
        agw >> Edge(color='darkgreen', label='https') >> APP06
              
        APP01 >>Edge(color='red')>> DB
        APP02 >>Edge(color='red')>> DB
        APP03 >>Edge(color='red')>> DB
        APP04 >>Edge(color='red')>> DB
        APP05 >>Edge(color='red')>> DB
        APP06 >>Edge(color='red')>> DB
        APP01 >>Edge(color='red')>> PUBSUB
        PUBSUB >>Edge(color='green')>> APP02
        APP02 >>Edge(color='red')>> PUBSUB
        PUBSUB >>Edge(color='green')>> APP03
        

        APP03 >>Edge(color='red')>> NOTIFICACIONES
        
        AppPod >>Edge(color='red')>> bucket
 
    WALLET >> Edge(color='darkgreen') >> Perimeter
    Perimeter >> Edge(color='darkgreen') >> agw
     
    GAME >> Edge(color='darkgreen') >> Perimeter 
    
    
   
    
    agw >> Edge(color='darkred') >> SEC
   
    


  
       
    OBS >> Edge(color='red') >> GRAFANA
    
    
    NOTIFICACIONES >> Edge(color='darkred') >> APP