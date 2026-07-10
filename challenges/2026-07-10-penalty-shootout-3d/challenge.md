# Penalty Shootout 3D

## Consigne

Crée un jeu de tirs au but (penalty) en 3D avec Three.js, jouable sur smartphone (écran tactile).

Le jeu doit tenir dans **un seul fichier HTML** (Three.js chargé depuis CDN).

## Spécifications

### Gameplay
- Le joueur contrôle le tireur : swipe sur l'écran pour viser (direction + hauteur), tap pour tirer
- Le gardien plonge aléatoirement (ou réagit selon la direction)
- 5 tentatives par partie
- Score affiché : buts marqués / tentatives
- Écran de victoire si ≥ 3 buts, défaite sinon

### Rendu 3D
- Low-poly stylisé (formes simples, couleurs vives)
- Terrain, but, ballon, gardien, tireur minimalistes
- Caméra placée pour une bonne vue du penalty (derrière le tireur ou de côté)
- Éclairage ambiant + directionnel

### Ambiance
- Stade avec gradins et supporters stylisés (formes géométriques)
- Couleurs vives et joyeuses
- Animations : ballon qui vole, gardien qui plonge, célébration / déception
- Petits effets visuels : herbe, lignes du terrain

### Contrôles tactiles
- Touch & drag pour viser (une flèche ou curseur directionnel)
- Tap pour déclencher le tir
- Interface adaptée mobile (boutons larges, texte lisible)

### Contraintes
- Un seul fichier HTML (tout en inline : CSS, JS, HTML)
- Three.js chargé depuis CDN (importmap ou script src)
- Fonctionne en mode paysage sur smartphone
- Pas de dépendances externes autres que Three.js

## Critères d'évaluation

- Qualité du gameplay et fun
- Rendu 3D et ambiance
- Adaptation mobile / tactile
- Robustesse (pas de bugs bloquants)
- Propreté du code

## Format de sortie attendu

Un seul fichier : `index.html` placé dans le répertoire de travail.
