# Indeed not Indeed

Ce projet a été dévloppé durant l'unité DSIA-4203C à ESIEE Paris. Celui-ci avait pour but de scrapper le site de notre choix et de stocker les données récupérés dans une base de données mongo. Il fallait ensuite mettre en place une application flask étant capable de communiquer avec cette base de données. Cette application marchera au sein d'un container créer en utilisant docker-compose.

## Table des matières
1. [Débutons](#débutons)  
    1.1 [Prérequis](#prérequis)  
    1.2 [Installation et démarrage](#installation-et-démarrage)  
    1.3 [L'application ne marche pas ?](#lapplication-ne-marche-pas-)
    1.4 [Remplir la base de données](#remplir-la-base-de-données)
2. [Technologies utilisées](#technologies-utilisées)
3. [Guide utilisateur](#guide-utilisateur)  
    3.1 [Page d'accueil](#page-daccueil)  
    3.2 [Page de résultat](#page-de-résultat)  

## Débutons 

Suivez ces instructions afin de copier une version fonctionnelle du projet sur votre machine.

### Prérequis

Tout d'abord, avant de vous lancer, vous aurez besoin d'installer docker sur votre machine. Suivez donc le lien [suivant](https://docs.docker.com/install/) afin de procéder à l'installation.
Vous aurez également besoin de télécharger sur votre machine le modul scapy de python avec la ligne de commande suivante : 
```bash
$ pip install scrapy
```


### Installation et démarrage 

1) Placez-vosu dans le repérertoire où vous souhaitez travailler sur le projet.
2) Clonez le projet avec la commande suivante : 

```bash
$ git clone https://github.com/RomainCoville/NotIndeed.git
```

Allez dans le repository :
```bash
$ cd NotIndeed/
```

Après avoir fait cela vous pouvez à présent lancer pour la première fois votre application en utilisant docker.
**Si vous avez téléchargé Docker Desktop** soyez sûr que l'application est démarrée et soit bien en marche. Si ce n'est pas le cas exécutez : 
```bash
$ docker-machine start default
```
Enfin, il  vous suffit  d'exécuter la commande suivante : 
```bash
$ docker-compose up -d
```

Une fois que l'application a fini de se construire vous pourrez utiliser l'application dans votre moteur de recherche.
Lorsque l'exécution est finit, cliquez sur le lien suivant : [http://0.0.0.0:5000/](http://0.0.0.0:5000/)

### L'application ne marche pas ?

Docker va vous aider à trouver le problème. Il vous faut simplement accéder aux logs du service lancé ainsi : 
```
docker-compose logs -f --tail=20 <service_name>
```

Vous pouvez ainsi remplacer *<service_name>* par $web$, ou $mongo$, vous pourrez ainsi voir où se trouve l'erreur qui sera alors facile à régler.

### Remplir la base de données

Lorsque vous mettez la main sur l'application, il n'y a pas beaucoup de données en base de données. Afin de tester l'application vous pouvez taper dans la barre de recherche *data* afin d'avoir un exemple de ce que peux afficher l'application.

Afin de remplir la base de données il va vous falloir utiliser le scrapper qui a été créé pour cela. Il vous faut donc exécuter la commande suivante  : 
```
scrapy crawl Job -a query=<nomDuJob>
```

Remplacer *nomDuJob* par le métier qui vous intéresse et exécuter la commande.
    
Lorsque la ligne suivante s'affiche : 
```
[scrapy.core.engine] INFO: Spider closed (finished)
```
C'est que le crawler a finit de récupérer les données et que vous pouvez retourner sur l'application à la recherche des informations qui vous intéressaient.

## Technologies utilisées

* [Flask](http://flask.pocoo.org/) - Framework python utilisé pour développer des application web
* [Scrapy](https://scrapy.org/) - Utilisé afin de récupérer les données sur le site de Indeed
* [MongoDB](https://www.mongodb.com/) - Une base de données NoSql utilisée pour stocker les données
* [Docker](https://www.docker.com/) - Utilisé pour la facilité de déploiement de notre projet

## Guide utilisateur

### Page d'accueil
La page d'accueil n'affiche que le titre de la page ainsi qu'une barre de recherche. Il faut y taper le nom du métier que vous voulez rechercher.

### Page de résultat
Après avoir effectué une recherche vous pouvez avoir de résultats possible : 
1) Une page de résultats comprennant deux  graphiques représentants la répartition du nombre d'offre en fonction du salaire associé et la répartition du nombre d'offre par rapport au type d'emploi associé (stage, CDI, ...) ainsi que des cartes représentant les intitulés, les entreprises et le lieu des offres publiés sur les 10 premières pages d'Indeed.
2)Une page *No results found!*. Celle-ci s'affiche si votre recherche est incorrect ou vide. Afin d'éviter cela deux choix s'offrent à vous :
    - Faites une recherche avec un job valide dans la barre de recherche (essayez avec *data* par exemple).
    - Si  votre recheche n'aboutit pas c'est que le métier rechercher n'est tout simplement pas encore présent dans la base de donnée, il vous faut alors la peuplée en utilisant le scapper. Pour cela nous vous conseillons de revenir plus haut dans les explications afin de comprendre comment faire, [lien](#remplir-la-base-de-données).
