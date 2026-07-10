# Model Arena 🏟️

Arène pour tester des agents opencode sur des challenges, comparer les modèles, et mesurer leurs performances.

## Structure

```
├── challenges/
│   └── <nom>/
│       ├── challenge.md       # la tâche à accomplir
│       ├── models.json        # modèles à tester
│       ├── leaderboard.json   # résultats agrégés
│       └── runs/              # résultats par modèle
│           └── <model-slug>/
│               ├── output.md
│               ├── screenshot.png
│               └── meta.json
├── skills/arena/SKILL.md
├── scripts/
│   ├── new-challenge          # créer un challenge
│   ├── run-challenge          # exécuter un challenge
│   └── pricing.json           # tarifs des modèles
└── opencode.json
```

## Usage

```bash
# Créer un challenge
bash scripts/new-challenge mon-test

# Éditer le challenge
$EDITOR challenges/mon-test/challenge.md
$EDITOR challenges/mon-test/models.json

# Lancer
bash scripts/run-challenge mon-test

# Voir les résultats
cat challenges/mon-test/leaderboard.json
```

Depuis opencode :
```
/new-challenge mon-test
/run-challenge mon-test
```

Les modèles disponibles sont listés par `opencode models`.
