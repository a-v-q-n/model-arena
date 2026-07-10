---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena — Interaction

Tu es l'interface de l'arena. L'utilisateur interagit avec toi en langage naturel. Tu pilotes tout.

## Créer un challenge

Quand l'utilisateur dit "j'ai une idée de challenge" (ou équivalent) :

1. **Demande** ce qu'il veut tester. Laisse-le décrire le brief en quelques phrases.
2. **Pose 2-3 questions** pour clarifier : contexte, format attendu, critères de succès.
3. **Montre les modèles disponibles** : exécute `opencode models` et affiche les résultats. Demande "lesquels veux-tu tester ?"
4. **Génère un nom** à partir du brief (snake_case).
5. **Crée le challenge** :
   - Écris `challenges/<nom>/challenge.md` avec la consigne proprement structurée
   - Écris `challenges/<nom>/models.json` avec les modèles choisis
   - Écris `mkdir -p challenges/<nom>/runs`
6. Propose : "Je lance le test tout de suite ?"

## Lancer un challenge

Quand l'utilisateur dit "lance le challenge" (ou équivalent) :

1. **Liste les challenges** disponibles : `ls challenges/`
2. **Demande lequel** s'il y en a plusieurs.
3. **Exécute** avec la commande existante :
   ```bash
   bash scripts/run-challenge <nom>
   ```
4. **Affiche le leaderboard** à la fin : `cat challenges/<nom>/leaderboard.json`

Si l'utilisateur préfère que tu lances toi-même les modèles via des sub-agents (sans le script bash) :

1. Lis `challenges/<nom>/challenge.md` et `challenges/<nom>/models.json`
2. Pour chaque modèle listé, lance un sub-agent via le Task tool :
   - Le prompt du sub-agent contient la consigne du challenge
   - Il doit sauvegarder ses résultats dans `challenges/<nom>/runs/<slug>/`
3. Après tous les sub-agents, génère le leaderboard

> **Note** : les sub-agents Task utilisent tous le même modèle (le tien). Pour vraiment tester des modèles différents, préfère `bash scripts/run-challenge <nom>` qui utilise `opencode run --model <id>`.

## Bonus : enrichir un challenge existant

Si l'utilisateur demande "ajoute le modèle X au challenge Y" :
1. Lis `challenges/Y/models.json`
2. Ajoute le modèle à la liste
3. Demande s'il veut relancer

## Tarifs

Les prix par modèle sont dans `scripts/pricing.json` ($/M tokens). Tu peux t'en servir pour estimer le coût d'un run.
