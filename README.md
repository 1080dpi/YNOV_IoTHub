Welcome to YNOV IoT Labs
===================

Dans le cadre des cours IoT sur le campus YNOV Lyon, nous avons réalisés un petit projet qui consiste à prendre en main "l'architecture" IoT, c'est à dire, développer un équipement (que nous nommerons Device) qui consomme une REST API et qui envoie les données collectés dans le Cloud Azure. 
Ces données sont collecter dans le cloud grâce à IoTHub qui permet de recevoir les données et également gérer notre Device : envoie de message, mise à jour, etc...
Les données collectées sont ensuite envoyées à Stream Analytics pour analyser les données et powerBI pour créer de jolie Dashboard plus parlant.

----------


Installation
-------------

Le projet a était développé en  **Python2.7** et le Device accueil un serveur web **Django**. vous aurez donc besoin de certains pré-requis pour déployer le projet.

> **Pré-requis :**
*Bien évidement, je ne vais pas ré-inventer la roue... je vous renverrais donc souvent vers les liens d'installation déjà existant.* 

> - Installation de python2.7 : 
	> https://www.python.org/downloads/release/python-2712/
> - Installation de Django :
	> https://docs.djangoproject.com/fr/1.10/topics/install/
> - Installation des SDK Azure : 
	> https://github.com/Azure/azure-iot-sdk-python/


---------
Un fois les pré-requis installés, vous pouvez télécharger le projet :

    git xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

####**Création du Device :**
Avant de configurer l'équipement, il est nécessaire de créer l'équipement dans IoTHub pour obtenir deux données :

 - la <u> ConnectionString </u> : qui permet de lier l'équipement à l'IoTHub.
 - le <u> deviceId </u> : qui permet d'identifier l'équipement.

Mais comment faire ça !!!!

Pour faire dans la simplicité, je vous conseille de suivre ce lien qui vous expliquera comment faire avec [Device Explorer](https://github.com/Azure/azure-iot-sdk-csharp/tree/master/tools/DeviceExplorer#create-device).
  


####**Configuration :**

Pour la configuration, c'est relativement simple. nous allons modifier deux lignes dans deux fichiers :

**<u>Pour configurer votre équipement</u>** : 

Ouvrez le fichier <i><b> iothubconnect.py </b></i> et remplacez les deux lignes suivantes avec les données de votre Device : 

    connectionString='[YOURCONNECTIONSTRING]'
    deviceId = '[YOURDEVICEID]'

**<u>Pour configurer l'interface de management </u>** : 

Ouvrez le fichier <i><b> device_management.py </b></i> et remplacez les deux lignes suivantes avec les données de votre Device : 

    connectionString='[YOURCONNECTIONSTRING]'
    deviceId = '[YOURDEVICEID]'

####**Mise en production :**

Une fois les changements établis, lancer le serveur web python : 

    python manage.py runserver

Enjoy US !