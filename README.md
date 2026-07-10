# Model Arena 🏟️

Arène pour tester des agents opencode sur des challenges, comparer les modèles, et mesurer leurs performances.

## Structure

```
├── challenges/           # Les challenges
│   └── <name>/
│       ├── challenge.md  # Instructions pour l'agent
│       ├── models.json   # Modèles à tester
│       └── runs/         # Résultats (généré)
├── skills/
│   └── arena/SKILL.md    # Skill pour utiliser l'arène
├── scripts/
│   ├── new-challenge     # Créer un nouveau challenge
│   └── pricing.json      # Tarifs des modèles
└── opencode.json         # Config avec agents pré-définis
```

## Usage

1. **Créer un challenge** : `bash scripts/new-challenge <nom>`
2. **Éditer** `challenges/<nom>/challenge.md` avec la tâche
3. **Configurer** `challenges/<nom>/models.json` avec les modèles
4. **Charger le skill arena** dans opencode : `/skill arena`
5. **Exécuter** le challenge via les instructions du skill
6. **Consulter** les résultats dans `challenges/<nom>/runs/`
