# Build Astro (statique) → image nginx. Construite par la CI GitHub puis pullée
# par Coolify (mode service) : le serveur ne builde jamais.
FROM node:22-alpine AS builder

WORKDIR /app

# Dépendances (lockfile figé).
COPY package.json package-lock.json ./
RUN npm ci

# Code + build (la home glob challenges/ au build).
COPY . .
RUN npm run build

# Sonde du « vert réel » : le sha du commit cuit dans dist/healthz.json.
ARG GIT_SHA=""
RUN printf '{"status":"ok","sha":"%s"}\n' "$GIT_SHA" > dist/healthz.json

# Runtime : nginx sert dist/ + challenges/ (données brutes, le repo est la donnée).
FROM nginx:alpine AS runtime
RUN apk add --no-cache curl
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
COPY challenges /usr/share/nginx/html/challenges

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/healthz.json || exit 1
