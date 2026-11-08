# Stack Tecnológica — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M3-01 (#38) |
| Versão | 1.0 — 2026-11-08 |
| Decisão | Dono do produto: **Next.js** (web) · **FastAPI** (API) · **React Native** (app) — [decisão 11](../00-gestao/actas/decisoes-mvp.md) |
| Base | [RNF](../01-requisitos/requisitos-nao-funcionais.md), [modelo de dados](../02-modelagem/dicionario-dados.md), [sequências](../02-modelagem/sequencia/README.md) |

> **Versões:** usa-se a **última versão estável** de cada ferramenta no arranque do M5, fixada nos ficheiros de lock (`pnpm-lock.yaml`, `uv.lock`). Não se fixam números aqui para o documento não envelhecer.

## 1. Visão geral

| Camada | Tecnologia | Papel |
|--------|-----------|-------|
| **Web** | Next.js (App Router) + TypeScript + Tailwind CSS | Interface web responsiva e PWA; páginas públicas renderizadas no servidor |
| **App** | React Native com **Expo** (Expo Router) + TypeScript | App Android do responsável de equipa (PER-03) |
| **API** | **FastAPI** (Python) + Pydantic + SQLAlchemy 2 + Alembic | API REST única para web e app; regras de negócio |
| **Worker** | Processo Python (APScheduler) na mesma base de código da API | Prazos 48 h / 72 h, lembretes, recálculo diferido (UC18, UC19) |
| **Base de dados** | **PostgreSQL** | Dados relacionais, `ENUM`, `JSONB`, índices parciais (M2) |
| **Ficheiros** | Armazenamento compatível com S3 (MinIO em dev) | Emblemas das equipas |
| **SMS** | Fornecedor a escolher no spike M3-08, atrás de uma interface | Código de recuperação de palavra-passe |
| **Push** | Expo Notifications (FCM) | Notificações na app (M8-06) |
| **Infra** | Docker / Docker Compose, Caddy (HTTPS), GitHub Actions | Ambientes e CI/CD (M3-07, M5, M10) |
| **Observabilidade** | Sentry (web, app, API) + logs JSON | RNF-044 |

## 2. Detalhe por camada

### 2.1 API — FastAPI

| Necessidade | Escolha | Porquê |
|-------------|---------|--------|
| Framework | FastAPI | Gera **OpenAPI automaticamente** a partir do código (RNF-041, M3-05, M5-11); validação forte com Pydantic; desempenho adequado a RNF-004 |
| Gestor de dependências | `uv` | Rápido; lockfile reprodutível |
| ORM / migrações | SQLAlchemy 2 (async) + Alembic + asyncpg | Suporte completo a PostgreSQL (`ENUM`, `JSONB`, `FOR UPDATE`, índices parciais); migrações versionadas (M5-03) |
| Autenticação | JWT de acesso curto + refresh token rotativo; hash **Argon2id** (`argon2-cffi`) | RNF-020, RNF-021; mesmo mecanismo para web e app |
| Limitação de pedidos | `slowapi` (ou middleware próprio com PostgreSQL) | RNF-027 |
| Tarefas agendadas | APScheduler num processo **worker** separado, com *advisory lock* no PostgreSQL | UC19 a cada 15 min sem duplicar execuções; evita Redis no MVP |
| Imagens | Pillow | Redimensionar/comprimir emblemas (RNF-003) |
| Testes | pytest + httpx + testcontainers (PostgreSQL real) | RNF-042; testes de concorrência (RNF-035) |
| Qualidade | ruff (lint + format) + mypy | RNF-043 |

### 2.2 Web — Next.js

| Necessidade | Escolha | Porquê |
|-------------|---------|--------|
| Renderização | **SSR/ISR** para páginas públicas (início, pesquisa, perfil, ranking); componentes cliente só onde há interacção | RNF-001 / RNF-002: menos JavaScript enviado em rede lenta |
| Estilos | Tailwind CSS | CSS final pequeno; design system (M4-04, M7-02) |
| Dados | TanStack Query + cliente **gerado do OpenAPI** (`openapi-typescript` + `openapi-fetch`) | Tipos sempre iguais ao contrato (M3-05) |
| Formulários | React Hook Form + Zod | Validação no cliente com mensagens claras (RNF-015) |
| PWA | Manifest + service worker (Serwist) | Instalável no telemóvel; cache de páginas públicas |
| Sessão | Cookies `HttpOnly` geridos por rotas do Next.js (padrão BFF) | Token fora do JavaScript do navegador |
| Testes | Vitest + Testing Library; Playwright (E2E, M9-02) | |

### 2.3 App — React Native (Expo)

| Necessidade | Escolha | Porquê |
|-------------|---------|--------|
| Base | Expo (managed) + Expo Router | Arranque rápido, builds na nuvem (EAS) sem máquina dedicada, actualizações OTA |
| Dados | TanStack Query + o **mesmo cliente gerado** do OpenAPI que a web | Reutilização de tipos e lógica de acesso |
| Token | `expo-secure-store` | Armazenamento seguro (M8-03) |
| Push | `expo-notifications` | RF-10 na app (M8-06) |
| Rede fraca | Persistência do TanStack Query + fila local de submissões | Comparência/resultado no campo com rede instável (RNF-012, M8-06) |
| Build | EAS Build → APK (testes) e AAB (Google Play) | M8-07, M10-05 |

### 2.4 Dados e ficheiros

- **PostgreSQL** gerido (produção) ou em contentor (dev/staging). Backups diários (RNF-033).
- **Emblemas** num bucket S3-compatível; a BD guarda só o URL (`equipa.emblema_url`).

## 3. Organização do repositório (monorepo)

```
GiraBairro/
├── apps/
│   ├── api/          ← FastAPI + worker (Python, uv)
│   ├── web/          ← Next.js (TypeScript, pnpm)
│   └── mobile/       ← React Native / Expo (TypeScript, pnpm)
├── packages/
│   └── api-client/   ← tipos + cliente gerados do openapi.yaml (partilhado por web e mobile)
├── docs/
├── scripts/
├── docker-compose.yml
└── pnpm-workspace.yaml
```

Um só repositório mantém o contrato (`docs/03-arquitetura/openapi.yaml`), a API e os dois clientes sincronizados no mesmo PR. Detalhe da arquitectura interna da API na M3-04.

## 4. Justificação pelos RNF

| RNF | Exigência | Como a stack responde |
|-----|-----------|-----------------------|
| RNF-001 / 002 | Páginas públicas rápidas e leves em rede lenta | SSR/ISR no Next.js, Tailwind, imagens optimizadas, cache CDN |
| RNF-003 | Emblemas comprimidos | Pillow na API + `next/image` |
| RNF-004 | p95 ≤ 800 ms | FastAPI assíncrono + asyncpg; índices do M2 |
| RNF-005 | Ranking actualizado ≤ 60 s | Recálculo na mesma transacção + tabela `estatistica_equipa` |
| RNF-010 / 012 / 016 | Mobile-first, poucos toques, estados visíveis | Web responsiva **e** app nativa para o PER-03 |
| RNF-020 / 021 / 025 | Palavras-passe, bloqueio, OTP | Argon2id, contadores na BD, OTP com expiração |
| RNF-022 | HTTPS | Caddy com certificados automáticos |
| RNF-023 | Autorização no servidor | Dependências FastAPI por rota (RN-13), testadas |
| RNF-030 / 031 | Auditoria imutável | Escrita na mesma transacção; permissões da BD só INSERT |
| RNF-034 | UTC na BD, WAT na interface | `TIMESTAMPTZ` + formatação no cliente (`Africa/Luanda`) |
| RNF-035 | Concorrência | Transacções com `SELECT … FOR UPDATE` |
| RNF-040 | Navegadores | Next.js com browserslist incluindo Samsung Internet |
| RNF-041 / 043 | OpenAPI, CI | FastAPI gera OpenAPI; GitHub Actions |
| RNF-044 | Monitorização | Sentry nos três clientes + logs JSON |
| RNF-046 | Notificações fiáveis | Notificações gravadas na BD (internas) + push na app |

## 5. Riscos da stack e mitigação

| Risco | Mitigação |
|-------|-----------|
| Duas linguagens (Python + TypeScript) | Fronteira clara pelo OpenAPI; cliente TypeScript gerado automaticamente |
| Três aplicações para manter | Monorepo, CI único, cliente partilhado; app focada no PER-03 |
| Latência para Angola | Alojamento numa região próxima (avaliada em M3-07) + CDN |
| Dependência do Expo | Expo permite *prebuild* para projecto nativo puro se necessário |

## 6. Decisões registadas

[ADR-001](adr/ADR-001-nextjs-web.md) · [ADR-002](adr/ADR-002-fastapi-api.md) · [ADR-003](adr/ADR-003-react-native-expo.md) · [ADR-004](adr/ADR-004-postgresql-sqlalchemy.md) · [ADR-005](adr/ADR-005-monorepo.md) · [ADR-006](adr/ADR-006-autenticacao-jwt.md) · [ADR-007](adr/ADR-007-calculo-ranking.md) · [ADR-008](adr/ADR-008-tarefas-agendadas.md)
