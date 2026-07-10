---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena

## Commandes

| Commande | Action |
|---|---|
| `/new-challenge <nom>` | Crée un nouveau challenge |
| `/run-challenge <nom>` | Exécute un challenge sur tous les modèles |

Depuis le terminal :

```bash
bash scripts/new-challenge <nom>       # créer
bash scripts/run-challenge <nom>       # exécuter (timeout 3min)
bash scripts/run-challenge <nom> 300   # timeout 5min
```

## Structure d'un challenge

```
challenges/<nom>/
├── challenge.md       # la tâche à accomplir
├── models.json        # modèles à tester
├── leaderboard.json   # résultats agrégés (généré)
└── runs/
    └── <model-slug>/  # résultats par modèle (généré)
        ├── output.md
        ├── screenshot.png
        └── meta.json
```

Le `slug` est le model ID avec les `/` remplacés par `-`.

## Workflow

1. `bash scripts/new-challenge mon-truc`
2. Éditer `challenges/mon-truc/challenge.md` (la consigne)
3. Configurer `challenges/mon-truc/models.json` (les modèles)
4. `bash scripts/run-challenge mon-truc`
5. Lire `challenges/mon-truc/leaderboard.json`

## Tarifs

Les prix des modèles sont dans `scripts/pricing.json` ($/M tokens).
