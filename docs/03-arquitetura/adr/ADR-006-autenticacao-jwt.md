# ADR-006 — Autenticação por telefone com JWT e refresh token rotativo

| Campo | Valor |
|-------|-------|
| Estado | ✅ Aceite |
| Data | 2026-11-08 |
| Decisor | Dono do produto + equipa |
| Relacionado | [stack.md](../stack.md) |

## Contexto

Web e app autenticam-se na mesma API; o identificador é o telefone (RF-01.02); são exigidos bloqueio por tentativas e OTP (RNF-021, RNF-025).

## Decisão

**Access token JWT curto (15 min)** + **refresh token opaco rotativo (30 dias)** guardado em hash na BD. Web: tokens em cookies `HttpOnly` via rotas do Next.js. App: tokens no `expo-secure-store`. Palavras-passe com **Argon2id**.

## Alternativas consideradas

| Alternativa | Porque não |
|-------------|------------|
| Sessões só em cookie no servidor | Pouco prático para a app nativa |
| Fornecedor externo (Auth0, Firebase) | Custo, dependência externa e login por telefone/SMS pago |

## Consequências

- Revogação possível (refresh tokens na BD; logout e recuperação invalidam-nos)
- Uma tabela `sessao` (refresh tokens) a acrescentar ao modelo em M5-05
- Papel (`utilizador`/`admin`) e equipa no token para autorização rápida, sempre revalidados nas escritas (RN-13)
