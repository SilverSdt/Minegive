# Minegive

Minegive est un générateur de **commandes Minecraft** se voulant simple et facile d’accès.
Le projet sera développé en **python**.

Lien vers le projet : [Minegive](https://github.com/SilverSdt/Minegive)

## Table des matières

- [Minegive](#minegive)
  - [Table des matières](#table-des-matières)
  - [Auteurs](#auteurs)
  - [Objectifs de version](#objectifs-de-version)
  - [Différentes méthodes et bonnes pratiques mises en place](#différentes-méthodes-et-bonnes-pratiques-mises-en-place)
    - [GitHub Milestones](#github-milestones)
    - [GitHub Issues](#github-issues)
    - [Tests unitaires](#tests-unitaires)
    - [Documentation](#documentation)
    - [Commentaires](#commentaires)
    - [PEP8](#pep8)
    - [Requirement.txt](#requirementtxt)
    - [Branches](#branches)
    - [Pull Requests](#pull-requests)
    - [Guide d'utilisation](#guide-dutilisation)
    - [Guide de création d'un environnement de développement](#guide-de-création-dun-environnement-de-développement)
  - [Features](#features)
    - [Fait](#fait)
      - [Création structure du projet](#création-structure-du-projet)
      - [Création de la classe Item](#création-de-la-classe-item)
      - [Création de la classe sélecteur](#création-de-la-classe-sélecteur)
      - [Création classe NBT](#création-classe-nbt)
    - [Non-terminé](#non-terminé)
      - [Création de sous-classe pour les catégories NBT](#création-de-sous-classe-pour-les-catégories-nbt)
      - [Création d'une classe pour les commandes](#création-dune-classe-pour-les-commandes)
    - [Non-commencé](#non-commencé)
      - [Création d'une CLI](#création-dune-cli)
      - [Création des routes de l'API](#création-des-routes-de-lapi)
      - [Containerisation de l'API](#containerisation-de-lapi)
      - [Création d'un front-end](#création-dun-front-end)
      - [Conteneurisation du front-end](#conteneurisation-du-front-end)
      - [Déploiement automatique avec actions GitHub](#déploiement-automatique-avec-actions-github)
  - [Ressenti](#ressenti)

## Auteurs

- **[Jeremy Bodart](https://jeremy.bodart.dev)**
- **[Joshua Vandaele](https://vandaele.software)**

## Objectifs de version

- **V1.0.0**: Fonctionnement avec CLI
- **V2.0.0**: Fonctionnement en mode CLI ou API
- **V3.0.0**: Fonctionnement en mode CLI ou API avec un front
- **???**: Création d'un docker pour le back et pour le front

## Différentes méthodes et bonnes pratiques mises en place

### GitHub Milestones

Les [**milestones**](https://github.com/SilverSdt/Minegive/milestones) représenteront les différentes versions de Minegive.

Cf: Objectifs de version

### GitHub Issues

Chaque tâche à effectuer est une [**Issue**](https://github.com/SilverSdt/Minegive/issues) sur github que l'on ferme avec les commits,
Ils doivent être attribués à la milestones adéquate et possiblement à un membre de l’équipe.

### Tests unitaires

Création de **tests unitaires** pour chaque fonctions et classes du programme.

Ils seront réalisés avec la bibliothèque python [**unittest**](https://docs.python.org/fr/3/library/unittest.html) et auront un répertoire attribué.

### Documentation

Le projet étant en python, la documentation pourra être générée automatiquement grâce à [**Pydoc**](https://docs.python.org/fr/3/library/pydoc.html) qui utilisera les commentaires dans le programme comme référence, génération qui sera faite à la fin de chaque version.

### Commentaires

Les commentaires suivront la formalisation de [**Pydoc**](https://docs.python.org/fr/3/library/pydoc.html), permettant la description des différentes classes, fonctions et méthodes en prenant un léger descriptif, les paramètres et leurs rôles (si il y a) et se qui est return (si il y a).

### PEP8

Le projet étant en python, nous suivons la convention de bases de ce langage qu’est [**PEP8**](https://peps.python.org/pep-0008/), en effet, celui-ci décrit les différentes bonnes pratiques qui peuvent être utilisé dans un projet.

**Exemple:**

- Convention de nommage
- Architecture du projet
- Arborescence des documents
- etc.

### Requirement.txt

Création d'un **requirements.txt** permettant de facilement permettre au potentiel futur contributeur de s’aligner sur les **versions de bibliothèque utilisé** (si utilisation de dépendance) et donc d’éviter les problèmes de différentes versions.

### Branches

Chaque feature se verra créer une **nouvelle [branche](https://github.com/SilverSdt/Minegive/branches)** afin de garantir la stabilité de la branche main pour qu’elle reste une version propre et utilisable.

### Pull Requests

Des [**pull requests**](https://github.com/SilverSdt/Minegive/pulls) seront faite afin de demander une validation externe de la qualité du programme fourni, notamment pour les merge qui sont les plus sensibles.

### Guide d'utilisation

Le **README.md** contiendra un guide permettant de simplifier les procédures de lancement du projet pour une utilisation simple.

**Note:** Finalement le README.md a été utilisé pour le compte-rendu, mais un maximum d'éléments explicatifs a quand même été implémenté.

### Guide de création d'un environnement de développement

Le **README.md** contiendra aussi un guide sur comment mettre en place son environnement de développement afin de garantir un environnement de travail sein et efficace.

**Note:** Finalement le README.md a était utilisé pour le compte-rendu.

## Features

Différentes features on était imaginé pour Minegive, cependant, toutes non pas pus être intégrées, mais voici la liste qui était prévues (faites, en cours ou pas commencées).

### Fait

Voici les features qui ont était implémentées :

#### Création structure du projet

la **[structure](https://github.com/SilverSdt/Minegive/issues/7)** suis les [**bonnes pratique**](https://medium.com/code-factory-berlin/github-repository-structure-best-practices-248e6effc405) GitHub permettant une utilisation simple tout en permettant une **uniformisation** des différents projets permettant de ne perdre personne si on travaille sur plusieurs projets différents

#### Création de la classe Item

La [**classe Item**](https://github.com/SilverSdt/Minegive/issues/3) représente un item générique de Minecraft.

Ils sont composés de :

- d'un ID
- d'un NBT
- d'un quantité

#### Création de la classe sélecteur

La [**classe Selector**](https://github.com/SilverSdt/Minegive/issues/2) représente un [**sélécteur**](https://minecraft.fandom.com/wiki/Target_selectors ) dans Minecrafts

Il existe différent **type** de sélécteur :

- **@e**: toutes les entités
- **@p**: le joueur le plus proche
- **@r**: un joueur aléatoire
- **@s**: l'entité exécutant la commande
- **@a**: tous les joueurs
- **@initiator**: le joueur qui a cliqué sur le dialogue du PNJ (_Version bedrock et éducation seulement_)

Ils possèdent chacun différents **attributs** :

- Coordonnées 3D (XYZ)
- Une distance (XYZ)
- Une limite
- Une rotation
- Un gamemode

#### Création classe NBT

La [**classe NBT**](https://github.com/SilverSdt/Minegive/issues/5) est un [**format utilisé par Minecraft afin de stocker différentes données**](https://minecraft.fandom.com/fr/wiki/Format_NBT).

La **classe ItemNBT** de base est composé comme suit :

- Dégâts
- Incassable ou non
- La liste des éléments que l'objet peut détruire (_en mode aventure_)
- Custom Model Data, permettant d'overrides le model d'un item
- Modificateurs d'attributs composé de: nom d'attribut, nom, opération, montant et [UUID](https://minecraft.fandom.com/wiki/Universally_unique_identifier)

Mais pour les blocks, le NBT est différent et rajoute les valeurs suivantes :

- la liste des blocks sur laquelle le block peut être posé.
- block entity tag
- block state tag

### Non-terminé

Certaines features ne sont pas encore fini, en voici la liste ainsi que ce qu'elles devaient faire.

#### Création de sous-classe pour les catégories NBT

Le [**NBT**](https://minecraft.fandom.com/fr/wiki/Format_NBT) est [**différents**](https://github.com/SilverSdt/Minegive/issues/6) pour les type d'item suivant :

- block
- fluid
- item
- tool
- armor

À l'heure actuelle, seulement les blocks et les items ont était fait.

#### Création d'une classe pour les commandes

La [**classe Command**](https://github.com/SilverSdt/Minegive/issues/1) permet de générer une commande, elle est créée grâce à :

- Un sélecteur
- Un item

La création de l'item n'est pas encore implémenté.

### Non-commencé

Les features suivantes non pas encore était commencées, par manque de temps ou parce que demande une avancée plus grande dans le projet

#### Création d'une CLI

Le CLI aurait permis de simplifier la création de commande en demandant les divers paramètres et en vérifiant la validité des informations saisie.

#### Création des routes de l'API

Les routes de l'API auraient permis d'appeler Minegive simplement avec une requête HTTP.

#### Containerisation de l'API

Pour le déploiement facile de l'API, une [**containarisation Docker**](https://docs.docker.com/) était prévue.

Les images suivantes étaient envisagées:

- [Python](https://hub.docker.com/_/python): image basé sur [Ubuntu](https://hub.docker.com/_/ubuntu)

#### Création d'un front-end

Le front-end aurait permit la création simple de commande avec différents paramètres avec une interface graphique permettant une création plus intuitive.

**Exemple:**

- [MapMaking](https://mapmaking.fr/give1.16/)

[**Django**](https://docs.djangoproject.com/en/5.0/) était envisagé pour le front.

Django étant à la base un framework python open source pour le développement d'application web.

#### Conteneurisation du front-end

Containeriser le front-end aurait pu se faire grâce à l'image [**Django**](https://hub.docker.com/_/django).

La conteneurisation du front fait suite logique à la conteneurisation du back.

#### Déploiement automatique avec actions GitHub

Les nouvelles [**release**](https://github.com/SilverSdt/Minegive/releases) auraient éta directement intégrées au serveur, permettant de garder à jour l'API facilement grâce a un fichier yml.

## Ressenti

L'idée de base nous a beaucoup plus. Mais notre choix de projet c'est avéré plus compliqué que prévu.

En effet, les commandes Minecraft nous ont demandé beaucoup de recherche et un long temps pour la compréhension, ce qui nous a ralentis dans notre démarche et ayant abouti à un projet non fini.

On aurait eu besoin de plus de temps ou alors partir sur les bases d'un projet déjà existant afin d'éviter se genre de problème.
