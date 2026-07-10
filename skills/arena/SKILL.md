---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena — Test d'agents

## Commandes

| Commande | Action |
|---|---|
| `/new-challenge <nom>` | Crée un nouveau challenge |
| `/run-challenge <nom>` | Exécute un challenge sur tous les modèles |

Depuis le terminal (en dehors d'opencode) :

```bash
bash scripts/new-challenge <nom>        # créer
bash scripts/run-challenge <nom>        # exécuter
bash scripts/run-challenge <nom> 300    # avec timeout 5min
```

## Structure d'un challenge

```
challenges/<nom>/
├── challenge.md      # la tâche à accomplir par chaque agent
├── models.json       # modèles à tester (id, provider, label)
└── runs/             # généré par run-challenge
    ├── <model-id>/
    │   ├── output.md       # sortie complète de l'agent
    │   ├── screenshot.png  # capture d'écran (si applicable)
    │   └── meta.json       # durée, présence capture
    └── leaderboard.json    # comparatif
```

## Workflow

1. **Créer** : `/new-challenge mon-truc`
2. **Éditer** `challenges/mon-truc/challenge.md` avec la consigne précise
3. **Configurer** `challenges/mon-truc/models.json` avec les modèles dispo
4. **Lancer** : `/run-challenge mon-truc`
5. **Analyser** les résultats dans `challenges/mon-truc/runs/leaderboard.json`

## Notes

- Le script `run-challenge` lance les modèles **séquentiellement**
- Les résultats incluent : temps d'exécution, capture d'écran, sortie brute
- Pour les modèles payants, configure les bons IDs dans `models.json` (la commande `opencode models` liste les modèles disponibles)
- Les tarifs sont dans `scripts/pricing.json` pour le calcul de coût
