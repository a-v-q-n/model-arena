# Model Arena 🏟️

Compare des modèles d'IA sur des challenges concrets.

```
scripts/new-challenge <nom>     créer un challenge
scripts/run-challenge <nom>     exécuter sur tous les modèles
scripts/run-challenge <nom> 300 avec timeout 5min
```

Depuis opencode : `/new-challenge` et `/run-challenge`.

---

## Guide pas à pas

### 1. Créer un challenge

```bash
bash scripts/new-challenge creer-une-api
```

Ça crée `challenges/creer-une-api/` avec deux fichiers prêts à remplir.

### 2. Écrire la consigne (`challenge.md`)

C'est le prompt donné à chaque agent. Sois précis :

````markdown
# Créer une API REST

## Contexte
Tu dois créer une API de gestion de tâches (Todo API) en Node.js.

## Consigne
- Dossier `challenges/creer-une-api/runs/<model>/`
- Un seul fichier : `server.js`
- Framework Express, stockage en mémoire
- Routes : GET /todos, POST /todos, DELETE /todos/:id
- Le serveur écoute sur le port 3000

## Critères
- L'API répond correctement sur chaque route
- Code propre et lisible
- Gestion des erreurs (todo inexistant → 404)

## Format de sortie attendu
Un fichier `server.js` prêt à être lancé avec `node server.js`.
````

> 💡 **Conseil** : plus la consigne est précise, plus les résultats sont comparables.

### 3. Configurer les modèles (`models.json`)

Liste les modèles à tester. Le script les lance un par un.

```json
{
  "models": [
    {
      "id": "openrouter/anthropic/claude-sonnet-4",
      "provider": "openrouter",
      "label": "Claude Sonnet 4"
    },
    {
      "id": "openrouter/openai/gpt-4o",
      "provider": "openrouter",
      "label": "GPT-4o"
    },
    {
      "id": "openrouter/deepseek/deepseek-chat",
      "provider": "openrouter",
      "label": "DeepSeek Chat"
    }
  ]
}
```

**Trouver les IDs disponibles** : `opencode models`

| Champ | Rôle |
|---|---|
| `id` | Identifiant du modèle (utilisé par `opencode run --model`) |
| `label` | Nom affiché dans le leaderboard |
| `provider` | Fournisseur (info seulement) |

### 4. Lancer

```bash
bash scripts/run-challenge creer-une-api
```

Le script :
- lance **séquentiellement** chaque modèle
- capture la sortie complète de l'agent
- prend une capture d'écran s'il trouve un `.html`
- génère le leaderboard

### 5. Lire les résultats

```
challenges/creer-une-api/
├── challenge.md
├── models.json
├── leaderboard.json         ← résultats comparés
└── runs/
    ├── openrouter-anthropic-claude-sonnet-4/
    │   ├── output.md         ← tout ce que l'agent a fait
    │   ├── screenshot.png    ← capture si HTML
    │   └── meta.json         ← durée, métadonnées
    └── openrouter-openai-gpt-4o/
        ├── output.md
        └── meta.json
```

Contenu de `leaderboard.json` :

```json
{
  "challenge": "creer-une-api",
  "timestamp": "2026-07-10T20:00:00Z",
  "results": [
    { "model": "openrouter/anthropic/claude-sonnet-4",
      "slug": "openrouter-anthropic-claude-sonnet-4",
      "label": "Claude Sonnet 4",
      "duration_seconds": 45,
      "screenshot": false },
    { "model": "openrouter/openai/gpt-4o",
      "slug": "openrouter-openai-gpt-4o",
      "label": "GPT-4o",
      "duration_seconds": 52,
      "screenshot": false }
  ]
}
```

---

## Résumé

```bash
bash scripts/new-challenge mon-challenge
# → édite challenge.md + models.json
bash scripts/run-challenge mon-challenge
# → résultats dans challenges/mon-challenge/leaderboard.json
```
