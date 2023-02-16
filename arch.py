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
quarkusimg= './my-resources/quarkus.png'
grafanaimg='./my-resources/grafana.png'
android_iosimg='./my-resources/Android-IOS.png'
gameimg='./my-resources/gameicon.png'
rest_img='./my-resources/RESTful-API.png'
livelinkimg='./my-resources/livelink.gif'
securityimg='./my-resources/Security.png'
securityappleimg='./my-resources/apple.png'
securitygoogleimg='./my-resources/google.png'


with Diagram("Basic Application Architecture", show=True, filename="architecture", direction="TB"):
  
    user= Users('User')
    
    with Cluster ('Wallet'):
        WALLET=Custom('WALLET', android_iosimg)
        
   
    with Cluster ('Game'):
        GAME=Custom('GAME', gameimg)
        
    with Cluster ('CloudWatch'):
        logs = Cloudwatch('CloudWatch')
        
    with Cluster ('Bucket'):
        bucket = S3('S3-Bucket')
        
    with Cluster ('Xray'):
        opentrace = XRay('Trace')
       
    with Cluster ('API GW'):
        agw = APIGateway('API GW')
   
    with Cluster ('Database') :
        DB=Aurora('Aurora')
        
    with Cluster ('Notificaciones') :
        NOTIFICACIONES=Firebase('Firebase')

    with Cluster ('Monitoring'):
        GRAFANA=Custom('GRAFANA', grafanaimg)
                       
    with Cluster ('Security'):
        with Cluster('SEC-TOOLS'):
           
            with Cluster('OAUTH'):
                OAUTH=Custom('',securityimg)   
            with Cluster('FIREBASE'):
                FIREBASE=Firebase('')
                with Cluster('FIREBASE'):
                    AUTH=Authentication('Authentication')
   
    with Cluster ('Security Providers'):
        with Cluster('Auth'):
            APPLE=Custom('APPLE', securityappleimg)
            GOOGLE=Custom('APPLE', securitygoogleimg)
    AUTH >> Edge(color='RED',style="dotted")>> APPLE
    AUTH >> Edge(color='RED',style="dotted")>> GOOGLE
   
    with Cluster ('Kubernetes'):
        EKS= ElasticKubernetesService('EKS')
        
        with Cluster('MS-BFF Pod'):
            BFFPod=Pod('POD MS-BFF')  
            with Cluster('MS-BFF'):
                BFF01=Custom('validateApp', quarkusimg)
                BFF02=Custom('commitTransaction', quarkusimg)
                BFF03=Custom('registroFirebase', quarkusimg)
                BFF04=Custom('gameList', quarkusimg)
                BFF05=Custom('accountsTokens', quarkusimg)
                BFF06=Custom('tokenList', quarkusimg)
                BFF07=Custom('transferToken', quarkusimg)
                BFF08=Custom('paymentTokens', quarkusimg)
                BFF09=Custom('findSites', quarkusimg)
                BFF10=Custom('accountInfo', quarkusimg)
                BFF11=Custom('updateAccount', quarkusimg)
                BFF12=Custom('findAccount', quarkusimg)
                
        
        
   
               
        with Cluster('MS-APP Pod'):
            AppPod=Pod('POD MS-APP')  
            with Cluster('MS-Back'):
                APP01=Custom('clientManager', quarkusimg)
                APP02=Custom('operations', quarkusimg)
                APP03=Custom('Notifications', quarkusimg)
                APP04=Custom('Sites', quarkusimg)
                APP05=Custom('Resources', quarkusimg)
                APP06=Custom('Forms', quarkusimg)
       
       
       
       
  
        
      

        
        

        
  
        BFFPod >>Edge(color='black',style="dotted")>> logs
        BFFPod >>Edge(color='black',style="dotted")>> opentrace

        AppPod >>Edge(color='black',style="dotted")>> logs
        AppPod >>Edge(color='black',style="dotted")>> opentrace

        
        
        BFF01 >>Edge(color='black',style="dotted")>> bucket

        agw >> Edge(color='darkgreen', label='https') >> BFF01
        agw >> Edge(color='darkgreen', label='https') >> BFF02
        agw >> Edge(color='darkgreen', label='https') >> BFF03
        agw >> Edge(color='darkgreen', label='https') >> BFF04
        agw >> Edge(color='darkgreen', label='https') >> BFF05
        agw >> Edge(color='darkgreen', label='https') >> BFF06
        agw >> Edge(color='darkgreen', label='https') >> BFF07
        agw >> Edge(color='darkgreen', label='https') >> BFF07
        agw >> Edge(color='darkgreen', label='https') >> BFF09
        agw >> Edge(color='darkgreen', label='https') >> BFF10
        agw >> Edge(color='darkgreen', label='https') >> BFF11
        
        BFF01 >> Edge(color='darkgreen') >> APP02
        BFF02 >> Edge(color='darkgreen') >> APP01
        BFF03 >> Edge(color='darkgreen') >> APP01
        BFF04 >> Edge(color='darkgreen') >> APP01
        BFF05 >> Edge(color='darkgreen') >> APP02
        BFF06 >> Edge(color='darkgreen') >> APP02
        BFF07 >> Edge(color='darkgreen') >> APP02
        BFF08 >> Edge(color='darkgreen') >> APP02
        BFF09 >> Edge(color='darkgreen') >> APP04
        BFF10 >> Edge(color='darkgreen') >> APP01
        BFF11 >> Edge(color='darkgreen') >> APP01
        BFF12 >> Edge(color='darkgreen') >> APP01

        
        APP01 >>Edge(color='red')>> DB
        APP02 >>Edge(color='red')>> DB
        APP03 >>Edge(color='red')>> DB
        APP04 >>Edge(color='red')>> DB
        APP05 >>Edge(color='red')>> DB
        APP06 >>Edge(color='red')>> DB
        APP02 >>Edge(color='black')>> APP03
        APP03 >>Edge(color='red')>> NOTIFICACIONES
        
        
       
    user >> Edge(color='darkgreen') >> GAME
    user  >> Edge(color='darkgreen') >> WALLET
    
    

 
    WALLET >> Edge(color='darkgreen', label='jwt') >> agw 

    
    GAME >> Edge(color='darkgreen', label='jwt') >> agw 
    
    
    OAUTH >> Edge(color='darkred') >> agw
    FIREBASE >> Edge(color='darkred') >> agw
    
    agw >> Edge(color='darkred') >> OAUTH
    agw >> Edge(color='darkred') >> FIREBASE
    
    
    agw >> Edge(color='darkred', label='jwt') >>  WALLET
    agw >> Edge(color='darkred', label='jwt') >>  GAME
       
    logs >> Edge(color='red') >> GRAFANA
    opentrace >> Edge(color='red') >> GRAFANA