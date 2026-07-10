---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena

Tous les chemins sont **relatifs à la racine du projet** (là où se trouvent `challenges/` et `scripts/`).

## Convention de nommage

Les dossiers de challenge sont automatiquement préfixés par la date : `YYYY-MM-DD-<name>`.
Exemple : `new-challenge hello-world` → `challenges/2026-07-10-hello-world/`

## Créer un challenge

Quand l'utilisateur dit "j'ai une idée de challenge" (ou équivalent) :

1. **Demande** ce qu'il veut tester. Laisse-le décrire le brief en quelques phrases.
2. **Pose 2-3 questions** pour clarifier : contexte, format attendu, critères de succès.
3. **Montre les modèles disponibles** : exécute `opencode models` et affiche les résultats. Demande "lesquels veux-tu tester ?"
4. **Génère un nom** à partir du brief (snake_case).
5. **Crée le challenge** avec le script :
   ```bash
   bash scripts/new-challenge <nom>
   ```
   Cela crée `challenges/YYYY-MM-DD-<nom>/` avec `challenge.md`, `models.json` et `runs/`.
6. Propose : "Je lance le test tout de suite ?"

## Lancer un challenge

Quand l'utilisateur dit "lance le challenge" (ou équivalent) :

1. **Liste les challenges** disponibles : `ls challenges/`
2. **Demande lequel** s'il y en a plusieurs.
3. **Exécute** avec la commande :
   ```bash
   bash scripts/run-challenge <nom-complet-avec-date>
   ```
4. **Affiche le résultat** et donne l'URL du récap : https://model-arena.avqn.ch/recap/?c=<nom>
   (en local : `npm run dev` puis http://localhost:4321/recap/?c=<nom>).

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

Les prix par modèle sont dans `scripts/pricing.json` ($/M tokens). Le script `run-challenge` estime automatiquement le coût de chaque run à partir des tokens consommés.

## Statistiques

Le script `run-challenge` capture automatiquement pour chaque modèle :
- **Durée** d'exécution (secondes)
- **Tokens** consommés (input, output, cache) via `opencode stats --models`
- **Coût estimé** à partir de `pricing.json`
- **Capture d'écran** du résultat HTML

Tout est enregistré dans `runs/<slug>/meta.json` et publié par le site (page récap du challenge).

## Le site

Le repo porte un site Astro (model-arena.avqn.ch, déployé au push sur `main`) :
- **Home `/`** — la liste des challenges, rendue au build.
- **Récap `/recap/?c=<nom>`** — UN template pour tous les challenges : il fetch côté client
  `challenge.md` + `leaderboard.json` et rend consigne, cartes de résultats (durée, tokens, coût),
  lecture comparée et livrables (capture, iframe, output.md). Rien n'est généré par challenge.

Les `runs/` sont versionnés : ce sont eux que le site publie. En local : `npm run dev`.

## Structure d'un challenge

```
challenges/YYYY-MM-DD-<name>/
├── challenge.md         # instruction donnée à chaque agent
├── models.json          # modèles à tester
├── leaderboard.json     # comparatif agrégé
└── runs/
    ├── <model-slug>/
    │   ├── index.html   # résultat du modèle
    │   ├── output.md    # log de l'agent
    │   ├── screenshot.png
    │   └── meta.json    # durée, tokens, coût
    └── ...
```
