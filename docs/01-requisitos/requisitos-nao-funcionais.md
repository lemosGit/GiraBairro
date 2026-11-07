# Requisitos Não Funcionais — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M1-05 (#20) |
| Versão | 1.0 — 2026-11-08 |
| Estado | Rascunho para validação (M1-10) |
| Base | [personas.md](personas.md) (contexto de uso), [visao.md](visao.md) (restrições) |

Cada RNF tem **código**, **persona** e uma **métrica verificável** (testada em M9-03). A prioridade MoSCoW é definida na M1-07.

## 1. Desempenho e uso de dados

| Código | Requisito | Persona | Métrica / critério de verificação | Prioridade |
|--------|-----------|---------|-----------------------------------|------------|
| RNF-001 | As páginas públicas (início, pesquisa, perfil, ranking) devem carregar rapidamente em rede móvel lenta. | PER-01 | LCP ≤ 3 s em perfil "Slow 4G" do Lighthouse, num Android de gama baixa emulado | Must |
| RNF-002 | O peso inicial de cada página deve ser reduzido para poupar dados. | PER-01, PER-03 | ≤ 500 KB transferidos na 1.ª visita a qualquer página (sem imagens de emblema); ≤ 150 KB em visitas seguintes | Should |
| RNF-003 | Os emblemas devem ser comprimidos e redimensionados no servidor. | PER-01, PER-03 | Miniaturas ≤ 30 KB; original ≤ 2 MB aceite no upload (JPG/PNG/WebP) | Should |
| RNF-004 | As operações do dia do jogo (comparência, resultado) devem responder rapidamente. | PER-03 | p95 da API ≤ 800 ms com 100 utilizadores simultâneos | Must |
| RNF-005 | O ranking deve ser actualizado pouco depois de um resultado/comparência ser confirmado. | PER-01, PER-03 | Ranking reflecte a alteração em ≤ 60 s | Should |

## 2. Usabilidade e acessibilidade

| Código | Requisito | Persona | Métrica / critério de verificação | Prioridade |
|--------|-----------|---------|-----------------------------------|------------|
| RNF-010 | A interface é **web responsiva, mobile-first**. | Todas | Todas as telas utilizáveis a 360 px de largura sem scroll horizontal | Must |
| RNF-011 | Interface integralmente em **português**, com datas no formato dd/mm/aaaa e hora 24 h. | Todas | 0 textos em inglês na revisão de UI | Must |
| RNF-012 | Registar comparência e resultado deve exigir poucos passos. | PER-03 | ≤ 3 toques a partir da notificação/agenda até submeter | Must |
| RNF-013 | Registo de conta e de equipa rápidos. | PER-02 | Utilizador novo completa conta + equipa em ≤ 3 min no teste de usabilidade (M4-06) | Should |
| RNF-014 | Acessibilidade básica. | Todas | Contraste WCAG 2.1 AA; alvos de toque ≥ 44 px; campos com rótulos; Lighthouse Accessibility ≥ 90 | Should |
| RNF-015 | Mensagens de erro claras e accionáveis. | Todas | Cada erro de validação indica o campo e como corrigir (revisão de UI) | Must |
| RNF-016 | Os estados (solicitação, jogo, comparência, resultado) devem ser sempre visíveis com texto e cor. | PER-03 | Badge de estado em TEL-13/14/15/18; não depende só da cor | Must |

## 3. Segurança e privacidade

| Código | Requisito | Persona | Métrica / critério de verificação | Prioridade |
|--------|-----------|---------|-----------------------------------|------------|
| RNF-020 | Palavras-passe guardadas com hash forte. | PER-02, PER-03, PER-05 | Argon2id ou bcrypt (custo ≥ 12); nunca em texto | Must |
| RNF-021 | Política mínima de palavra-passe. | PER-02 | ≥ 8 caracteres; bloqueio temporário após 5 tentativas falhadas em 15 min | Must |
| RNF-022 | Toda a comunicação por HTTPS. | Todas | TLS 1.2+; HSTS activo em produção | Must |
| RNF-023 | Autorização no servidor: um responsável só altera a sua equipa e os seus jogos. | PER-03 | Testes automáticos de acesso negado (403) para todos os endpoints de escrita (RN-13) | Must |
| RNF-024 | Telefones dos contactos com visibilidade controlada. | PER-04 | Conforme decisão 3 (M1-11); nunca indexáveis por motores de busca (`noindex` nos dados de contacto) | Must |
| RNF-025 | Recuperação de palavra-passe segura. | PER-02, PER-03 | Código de 6 dígitos, validade ≤ 10 min, máx. 3 tentativas | Must |
| RNF-026 | Dados pessoais mínimos e conformidade com a Lei de Protecção de Dados Pessoais (Lei n.º 22/11, Angola). | Todas | Termos e política de privacidade aceites no registo (TEL-02); exportação/eliminação de conta a pedido | Should |
| RNF-027 | Protecção contra abuso. | PER-05 | Rate limiting: ≤ 10 pedidos/min de login por IP/telefone; ≤ 20 solicitações de jogo/dia por equipa | Should |

## 4. Fiabilidade, auditoria e dados

| Código | Requisito | Persona | Métrica / critério de verificação | Prioridade |
|--------|-----------|---------|-----------------------------------|------------|
| RNF-030 | Todas as alterações a jogos, comparências e resultados ficam registadas (quem, quando, valor anterior, novo valor, motivo). | PER-05 | 100 % das operações de escrita nessas entidades geram registo de auditoria (RN-12) | Must |
| RNF-031 | Registos de auditoria são imutáveis. | PER-05 | Sem endpoint de edição/eliminação; só inserção | Must |
| RNF-032 | Disponibilidade do serviço. | Todas | ≥ 99 % mensal (excluindo manutenção anunciada) | Should |
| RNF-033 | Cópias de segurança. | PER-05 | Backup diário da BD, retenção 30 dias, restauro testado 1×/mês (M10-03) | Must |
| RNF-034 | Datas e horas guardadas em UTC e mostradas no fuso de Angola (WAT, UTC+1). | Todas | Testes de conversão; jogo às 16:00 aparece 16:00 em todas as telas | Must |
| RNF-035 | Consistência das submissões concorrentes. | PER-03 | Duas submissões simultâneas do mesmo jogo não corrompem o estado (testes de concorrência) | Must |

## 5. Manutenção, portabilidade e operação

| Código | Requisito | Persona | Métrica / critério de verificação | Prioridade |
|--------|-----------|---------|-----------------------------------|------------|
| RNF-040 | Compatibilidade de navegadores. | Todas | Chrome Android (2 últimas versões), Samsung Internet, Opera Mini (modo básico: leitura), Firefox, Edge, Safari iOS 15+ | Must |
| RNF-041 | API documentada em OpenAPI. | Equipa | `openapi.yaml` válido e servido em `/docs` (M3-05, M5-11) | Should |
| RNF-042 | Cobertura de testes do backend. | Equipa | ≥ 70 % de linhas nos módulos de negócio (M6-13) | Should |
| RNF-043 | CI obrigatório em cada PR. | Equipa | Lint + testes a passar antes do merge (M5-10) | Must |
| RNF-044 | Logs estruturados e monitorização de erros. | PER-05 | Erros 5xx registados com identificador de pedido; alerta em > 1 % de erros em 5 min | Should |
| RNF-045 | Escalabilidade do piloto. | Todas | Suporta 500 equipas, 10 000 jogadores e 2 000 jogos/mês sem degradação de RNF-004 | Should |
| RNF-046 | Notificações internas entregues de forma fiável. | PER-03 | 100 % dos eventos de RF-10 geram notificação; lembretes enviados ≥ 24 h antes do jogo | Must |

## 6. Resumo por persona

| Persona | RNF mais relevantes |
|---------|---------------------|
| PER-01 Visitante | RNF-001, 002, 003, 010, 011, 040 |
| PER-02 Utilizador sem equipa | RNF-013, 020, 021, 025, 026 |
| PER-03 Responsável da equipa | RNF-004, 005, 012, 016, 023, 035, 046 |
| PER-04 Responsável de contacto | RNF-024, 026 |
| PER-05 Administrador | RNF-027, 030, 031, 033, 044 |
