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
   
    "bgcolor": "transparent"
}

with Diagram("Perimeter Security", show=True, filename="perimeter security", direction="LR", graph_attr=graph_attr):
   

    with Cluster ('Access'):
        Perimeter=WAF('WAF')
        agw = APIGateway('API GW')
        
    with Cluster ('Wallet'):
        WALLET=Custom('WALLET', android_iosimg)
        GAME=Custom('GAME', gameimg)
   

        
                      
    with Cluster ('Security'):
        with Cluster('SEC-TOOLS'):
            SEC=Custom('',securityimg)   
            with Cluster('SEC'):
                AUTH=[Custom('OAUTH',oauthimg), Amplify('AMPLIFY'),Cognito('COGNITO')]
   
    with Cluster ('Security Providers'):
        Providers=Custom('',identityProviderimg)   
        with Cluster('Auth'):
            APPLE=Custom('APPLE', securityappleimg)
            GOOGLE=Custom('APPLE', securitygoogleimg)
    SEC >> Edge(color='RED',style="dotted")>> Providers
   
    
    WALLET >> Edge(color='darkgreen') >> Perimeter
    Perimeter >> Edge(color='darkgreen') >> agw
     
    GAME >> Edge(color='darkgreen') >> Perimeter 
    
    
   
    
    agw >> Edge(color='darkred') >> SEC
   