---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena

Guide complet dans `README.md`. Résumé :

## Commandes

| Depuis opencode | Depuis le terminal |
|---|---|
| `/new-challenge <nom>` | `bash scripts/new-challenge <nom>` |
| `/run-challenge <nom>` | `bash scripts/run-challenge <nom>` |

## Structure

```
challenges/<nom>/
├── challenge.md       # consigne donnée à chaque agent
├── models.json        # modèles à tester (id, label, provider)
├── leaderboard.json   # résultats comparés (généré par run)
└── runs/<slug>/       # résultats par modèle (généré)
    ├── output.md
    ├── screenshot.png
    └── meta.json
```

Le slug est le model ID avec les `/` remplacés par `-`.

## Workflow

1. `/new-challenge mon-truc` → crée les fichiers
2. Éditer `challenge.md` (consigne) et `models.json` (modèles)
3. `/run-challenge mon-truc` → exécute
4. Consulter `challenges/mon-truc/leaderboard.json`

## Liste des modèles

Les IDs sont ceux de `opencode models`. Exemple :
```
openrouter/anthropic/claude-sonnet-4
openrouter/openai/gpt-4o
openrouter/deepseek/deepseek-chat
opencode/deepseek-v4-flash-free
```
