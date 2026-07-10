import { defineConfig } from "astro/config";
import { createReadStream, existsSync, statSync } from "node:fs";
import { extname, join, normalize } from "node:path";

// Vitrine de l'arène : home (liste des challenges, rendue au build) + récap (template
// client-side). En prod, nginx sert challenges/ brut à côté de dist/ ; en dev, ce mini
// plugin reproduit le même contrat depuis le dossier du repo.

const TYPES = {
  ".json": "application/json; charset=utf-8",
  ".md": "text/plain; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
  ".css": "text/css",
  ".js": "text/javascript",
};

function serveChallenges() {
  return {
    name: "serve-challenges",
    configureServer(server) {
      server.middlewares.use("/challenges", function (req, res, next) {
        const pathname = decodeURIComponent(new URL(req.url, "http://localhost").pathname);
        const rel = normalize(pathname).replace(/^[/\\]+/, "");
        if (rel.split(/[/\\]/).includes("..")) return next();
        let file = join(process.cwd(), "challenges", rel);
        if (existsSync(file) && statSync(file).isDirectory()) file = join(file, "index.html");
        if (!existsSync(file) || !statSync(file).isFile()) return next();
        res.setHeader("Content-Type", TYPES[extname(file)] ?? "application/octet-stream");
        if (req.method === "HEAD") return res.end();
        createReadStream(file).pipe(res);
      });
    },
  };
}

export default defineConfig({
  site: "https://model-arena.avqn.ch",
  output: "static",
  build: { format: "directory" },
  vite: { plugins: [serveChallenges()] },
});
