# Indeed not Indeed

Ce projet a été dévloppé durant l'unité DSIA-4203C à ESIEE Paris. Celui-ci avait pour but de scrapper le site de notre choix et de stocker les données récupérés dans une base de données mongo. Il fallait ensuite mettre en place une application flask étant capable de communiquer avec cette base de données. Cette application marchera au sein d'un container créer en utilisant docker-compose.

## Table des matières
1. [Getting Started](#getting-started)  
    1.1 [Prerequisites](#prerequisites)  
    1.2 [Installing and Running](#installing-and-running)  
    1.3 [The app doesn't run ?](#the-app-doesnt-run-)
2. [User Guide](#user-guide)  
    2.1 [Home Page](#home-page)  
    2.2 [Search Page](#search-page)  
    2.3 [Graph Page](#graph-page)
3. [Reference Guide](#reference-guide)
    3.1 [Crawling Ex Nihilo](#crawling-ex-nihilo)
    3.2 [Why Elasticsearch ?](#why-elasticsearch-)

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

## L'application ne marche pas ?

Docker va vous aider à trouver le problème. Il vous faut simplement accéder aux logs du service lancé ainsi : 
```
docker-compose logs -f --tail=20 <service_name>
```

Vous pouvez ainsi remplacer *<service_name>* par $web$, ou $mongo$, vous pourrez ainsi voir où se trouve l'erreur qui sera alors facile à régler.


## Technologies utilisées

* [Flask](http://flask.pocoo.org/) - Framework python utilisé pour développer des application web
* [Scrapy](https://scrapy.org/) - Utilisé afin de récupérer les données sur le site de Indeed
* [MongoDB](https://www.mongodb.com/) - Une base de données NoSql utilisée pour stocker les données
* [Docker](https://www.docker.com/) - Utilisé pour la facilité de déploiement de notre projet

## Guide utilisateur

### Page d'accueil
La page d'accueil n'affiche que le titre de la page ainsi qu'une barre de recherche. Il faut y taper le nom du métier que vous voulez rechercher.

### Page de résultat
Après avoir effectué une recherche, il n'y a 



### Search Page
If you want to find specific reviews or users, you found the perfect page !  
‌‌‌‌‌‌

![Search Page](img/search-page.gif)

### Graph Page
Calling to the secret plot lover in you, here are a few plots to get a global view of grade distribution of reviews
‌‌‌‌‌‌

![Graph Page](img/graph-page.gif)


## Reference guide

### Crawling Ex Nihilo

If you'd like to populate the database yourself, here are the commands you'll need to run:

Start the container:
```bash
$ docker-compose up -d
```
Then, run each crawler individually:
```bash
$ docker-compose exec app scrapy crawl tripadvisor_attraction
# Crawls names for every g_value (tripadvisor attraction id) listed in json file
$ docker-compose exec app scrapy crawl tripadvisor_attraction_review
# Crawls places listed in json file, using attraction names scrapes before
$ docker-compose exec app scrapy crawl tripadvisor_user
# Crawls all users who left a review on places scraped above (this will take a while)
$ docker-compose exec app scrapy crawl tripadvisor_review
# Crawls the first ten reviews of all users present in the database (this will take even longer !)
```
_You may want to stop crawling users at a certain point et carry on with reviews_

If you want to know what g_values and d_values are, check out the comments in `tripadvisor_crawler/items.py`. If you wish to modify their starting values, you must change `tripadvisor_crawler/spiders/g_values.json` and `tripadvisor_crawler/spiders/d_values_by_attraction.json`

### Why Elasticsearch ?

We chose elastic for a more understanding search. With it we can adapt to grammar (for instance words with and without an 's' at the end), or even better, spelling errors ! As is demonstrated with the two page gifs where `magnifique` and `magnifike` give the same output.
We used elasticsearch in the search page (obviously) and for the first type of graph because of its 'intelligence' while searching. Elsewhere we simply used mongo.

