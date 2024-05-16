---
title: "Projet de Traitement d'Images avec Azure, TensorFlow et OpenAI"
author:
  - Thelma LUM
  - Mohamed YAHIAOUI
  - Franck malève Takuete
date: "2024-05-14"
geometry:
  - top=20mm
  - left=20mm
  - right=10mm
  - bottom=10mm
  - heightrounded
bibliography: [biblio.bib]
---

## Bibliographie
- Documentation officielle de TensorFlow : [https://www.tensorflow.org](https://www.tensorflow.org)
- Documentation officielle de TensorFlow Hub : [https://www.tensorflow.org/hub](https://www.tensorflow.org/hub)
- Documentation officielle d'OpenAI : [https://beta.openai.com/docs](https://beta.openai.com/docs)
- Documentation officielle d'Azure Cognitive Services : [https://docs.microsoft.com/fr-fr/azure/cognitive-services/](https://docs.microsoft.com/fr-fr/azure/cognitive-services/)


## Introduction
Ce projet  a pour objectif de créer un programme capable de traiter des images de manière avancée. En combinant différentes technologies comme Azure Cognitive Services, OpenAI GPT-3 et TensorFlow, ce programme permet de sélectionner une image, d'analyser son contenu, d'appliquer des effets artistiques et enfin de générer une description du contenu détecté.

## Contexte et Objectifs

### Azure Cognitive Services
Azure Cognitive Services est une suite de services cloud offerts par Microsoft, permettant d'intégrer des fonctionnalités d'intelligence artificielle dans les applications. Dans ce projet, nous utiliserons le service Computer Vision pour analyser les images et en extraire des informations telles que les objets identifiés et les scènes représentées.

### TensorFlow
TensorFlow est une bibliothèque open-source de machine learning développée par Google. Dans ce projet, nous l'utiliserons pour implémenter le transfert de style, une technique permettant de transférer le style artistique d'une image à une autre.

### OpenAI GPT-3
OpenAI GPT-3 est un modèle de langage de grande échelle, capable de générer du texte de haute qualité sur une variété de sujets. Nous exploiterons ce modèle pour recontextualiser le contenu des images, en générant du texte descriptif basé sur leur contenu visuel.

## Méthodologie et Déroulement

### Prérequis
- Clés d'accès aux services Azure Cognitive Services et OpenAI GPT-3.
- Installation des bibliothèques Python nécessaires (azure-cognitiveservices-vision-computervision, tensorflow, transformers).

### Étapes du Projet
1. **Sélection d'une Image** : Mise en place d'une interface utilisateur permettant à l'utilisateur de choisir une image à traiter.
2. **Analyse de l'Image avec Azure Cognitive Services** : Utilisation du service Computer Vision pour identifier les éléments présents dans l'image.
3. **Transfert de Style avec TensorFlow** : Implémentation d'un algorithme de transfert de style pour appliquer des effets artistiques à l'image.
4. **Génération de Texte avec OpenAI GPT-3** : Utilisation de GPT-3 pour générer un texte descriptif basé sur le contenu visuel de l'image.
5. **Affichage des Résultats** : Présentation des informations extraites de l'image et du texte généré à l'utilisateur.

## Exemple d'Utilisation
Le script `projet-Image.py` permet de sélectionner une image, d'analyser son contenu à l'aide des services Azure Cognitive Services, d'appliquer un effet de transfert de style avec TensorFlow, de générer un texte descriptif avec OpenAI GPT-3, et d'afficher les résultats obtenus.

## Architecture et Bibliothèques Utilisées
- **Azure Cognitive Services** : Utilisé pour l'analyse de contenu d'image.
- **TensorFlow** : Utilisé pour le transfert de style.
- **TensorFlow Hub** : Utilisé pour charger le modèle de transfert de style pré-entraîné.
- **OpenAI GPT-3** : Utilisé pour générer du texte descriptif.
- **Tkinter** : Utilisé pour l'interface utilisateur permettant de sélectionner une image.
- **os** : Utilisé pour les opérations liées aux fichiers et aux répertoires.
- **yaml** : Utilisé pour charger les clés d'API à partir d'un fichier YAML.
- **openai** : Utilisé pour l'accès à l'API OpenAI GPT-3.
- **azure.cognitiveservices.vision.computervision** : Utilisé pour l'accès à l'API Azure Cognitive Services Computer Vision.
- **msrest.authentication** : Utilisé pour l'authentification auprès des services Azure Cognitive Services.

## Installation

### 1. Clonez ce dépôt sur votre machine locale

```
git clone <URL_du_dépôt>
```

### 2. Installez les paquets Python requis

```
pip install -r requirements.txt
```

### 3. Configurez les clés API

- Créez un fichier `keys.yaml` dans le répertoire `private`.
- Ajoutez vos clés d'API Azure Cognitive Services et OpenAI GPT-3 au fichier `keys.yaml` dans le format suivant 

```yaml
azure_endpoint: "YOUR_AZURE_ENDPOINT"
azure_key: "YOUR_AZURE_KEY"
openai_key: "YOUR_OPENAI_KEY"
```

Remplacez `VOTRE_ENDPOINT_AZURE`, `VOTRE_CLE_AZURE` et `VOTRE_CLE_OPENAI` par vos propres clés d'API.

## Comment exécuter le script

Pour exécuter le script `projet-Image.py`, assurez-vous d'être dans le répertoire contenant le fichier et exécutez la commande suivante dans votre terminal :

```
python projet-Image.py
```

## Problèmes rencontrés lors de la mise en place du programme

### Erreur de "too many positional arguments" lors de l'application du transfert de style
Lors de l'application du transfert de style à une image à l'aide du module TensorFlow Hub, une erreur "too many positional arguments" est survenue. Cela suggère que nous avons passé trop d'arguments de position lors de l'appel de la fonction `hub_module`. Il est probable que nous ayons inclus des arguments inutiles dans cet appel. Nous devons réviser l'appel à la fonction `hub_module` pour nous assurer que nous passons le bon nombre d'arguments.

### Erreur de "Scalar tensor has no `len()`"
Une autre erreur rencontrée était "Scalar tensor has no `len()`". Cette erreur survient lorsqu'on essaie d'utiliser la fonction `len()` sur un tenseur scalaire. Un tenseur scalaire ne contient qu'une seule valeur, donc il n'a pas de dimension à vérifier avec `len()`. Pour résoudre cette erreur, nous devons examiner les endroits où nous utilisons la fonction `len()` et nous assurer qu'elle est utilisée correctement sur des tenseurs appropriés.

## Conclusion

Ce projet démontre les possibilités offertes par l'intégration de différentes technologies pour le traitement d'images et la génération de texte. En combinant les services cloud avec des bibliothèques open-source, il est possible de créer des systèmes puissants capables d'analyser, transformer et interpréter des données visuelles de manière automatique et intelligente.