---
title: Projet de Traitement d'Images avec Azure, TensorFlow et OpenAI
author:
    - Thelma LUM
    - Mohamed YAHIAOUI
    - Franck malève Takuete
date: 2024-05-14
geometry:
    - top=20mm
    - left=20mm
    - right=10mm
    - bottom=10mm
    - heightrounded
bibliography: [biblio.bib]
---

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