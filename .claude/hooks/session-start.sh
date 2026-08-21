#!/usr/bin/env bash
# Hook SessionStart — accueil de session (locale ou cloud). En cloud : signature de commit neutralisée,
# deps installées, plugin de méthode amorcé ; partout : annonce de la branche et de la gate.
set -uo pipefail
emit() {
  jq -nc --arg c "$1" '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:$c}}' 2>/dev/null \
    || printf '%s\n' "$1"
}
git rev-parse --git-dir >/dev/null 2>&1 || { emit "🚀 model-arena (hors dépôt git)."; exit 0; }
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"
git config --local commit.gpgsign false 2>/dev/null || true

# Méthode en session cloud : le plugin avqn-dev (marketplace publique a-v-q-n/skills) s'amorce ici —
# l'auto-install déclaré dans .claude/settings.json ne se déclenche pas dans la VM. Idempotent.
# Docker : le binaire est là, pas le démon — on le lance si le repo a des services à conteneuriser.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  if claude plugin list 2>/dev/null | grep -q 'avqn-dev@avqn'; then
    claude plugin marketplace update avqn >&2 2>&1 || true
  else
    claude plugin marketplace add a-v-q-n/skills >&2 2>&1 || true
    claude plugin install avqn-dev@avqn >&2 2>&1 || true
  fi
  if ls compose*.y*ml docker-compose*.y*ml >/dev/null 2>&1 && ! docker info >/dev/null 2>&1; then
    (dockerd >/tmp/dockerd.log 2>&1 &) ; sleep 3
  fi
fi

if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && [ -f package.json ]; then
  ( cd "$CLAUDE_PROJECT_DIR" && npm install --no-audit --no-fund ) >&2 || true
fi
base="Dis ce que tu veux faire. Gate : \`npm run gate\`. Méthodo (brancher/TDD/PR/CI/FF merge) : plugin avqn-dev (/avqn-dev:dev)."
if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  emit "🚀 model-arena — tu es sur \`$branch\`. Bascule sur ta branche de session (\`git switch -c claude/<mission>\`) avant de coder. $base"
else
  emit "🚀 model-arena — session isolée sur la branche \`$branch\`. $base"
fi
exit 0
