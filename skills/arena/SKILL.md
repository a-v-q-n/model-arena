---
name: arena
description: Arena d'évaluation — crée et exécute des challenges sur plusieurs modèles en parallèle
---

# Arena — Test d'agents

Structure d'un challenge :

```
challenges/<name>/
├── challenge.md         # instruction donnée à chaque agent
├── models.json          # modèles à tester
└── runs/
    ├── <model-id>/      # résultat d'un modèle
    │   ├── output.md
    │   ├── screenshot.png
    │   └── meta.json
    └── leaderboard.json # comparatif agrégé
```

## Créer un challenge

```
scripts/new-challenge <name>
```

Ça crée `challenges/<name>/` avec `challenge.md` et `models.json` prêts à remplir.

## Exécuter un challenge

Le workflow est le suivant :

1. Lis `challenges/<name>/challenge.md` et `challenges/<name>/models.json`
2. Pour chaque modèle listé dans `models.json`, lance **un sub-agent en parallèle** via le Task tool
3. Chaque sub-agent reçoit les instructions ci-dessous
4. Une fois tous terminés, agrège dans `leaderboard.json`

### Template pour le sub-agent (à adapter)

```
Tu participes à un challenge d'agents.

## Tâche
{contenu de challenge.md}

## Instructions de sortie
1. Complète la tâche ci-dessus du mieux possible
2. Sauvegarde ton travail et tes livrables dans challenges/{name}/runs/{model.id}/
3. Crée challenges/{name}/runs/{model.id}/output.md avec :
   - le résumé de ce que tu as produit
   - les choix techniques que tu as faits
   - les fichiers/dossiers créés
4. Si applicable, prends une capture d'écran du résultat avec playwright MCP
   et sauvegarde-la dans challenges/{name}/runs/{model.id}/screenshot.png
5. Ne modifie rien en dehors de challenges/{name}/runs/{model.id}/
```

### Après tous les sub-agents

Génère `challenges/{name}/runs/leaderboard.json` :

```json
{
  "challenge": "nom",
  "timestamp": "2026-07-10T...",
  "results": [
    {
      "model": "model.id",
      "time_seconds": 123,
      "files_created": ["..."],
      "screenshot": true
    }
  ]
}
```

## Configuration des modèles

Les modèles sont déclarés dans `challenges/<name>/models.json`. Chaque entrée peut préciser le provider et le pricing pour le calcul de coût.

Les agents sont pré-configurés dans `opencode.json` sous `agent.*`. Le sub-agent utilise l'agent configuré avec le modèle correspondant au moment de l'appel. Pour alterner entre modèles, le skill adapte la config avant chaque lancement.

## Tarifs (scripts/pricing.json)

Les coûts sont calculés à partir de `scripts/pricing.json` en fonction des tokens utilisés. Le fichier contient les prix par modèle (`input` et `output` en $/M tokens).
