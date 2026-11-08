# Especificação dos Casos de Uso — GiraBairro

| Campo | Valor |
|-------|-------|
| Task | M2-02 (#30) |
| Versão | 1.0 — 2026-11-08 |
| Âmbito | Casos de uso Must do fluxo central + autenticação (13 UC). Os restantes são CRUD simples cobertos pelas user stories |
| Base | [Catálogo de UC](README.md), [RN](../../01-requisitos/regras-negocio.md), [US](../../01-requisitos/user-stories.md) |

Convenções: **FP** = fluxo principal; **FA** = fluxo alternativo; **FE** = fluxo de excepção. "Sistema" = GiraBairro.

---

## UC01 — Criar conta

| | |
|---|---|
| **Actor** | PER-01 / PER-02 |
| **Pré-condições** | Sem sessão iniciada |
| **Pós-condições** | Conta criada; sessão iniciada; termos aceites registados |
| **RF / RN / US** | RF-01.01–03 · RNF-020, RNF-021, RNF-026 · US-001 |

**FP**
1. O actor abre "Criar conta" (TEL-02).
2. Preenche nome completo, telefone, palavra-passe, confirmação e aceita os termos.
3. O sistema valida o formato do telefone e a política de palavra-passe.
4. O sistema verifica que o telefone não existe (RF-01.03).
5. O sistema cria a conta com a palavra-passe em hash e inicia sessão.
6. O sistema encaminha para "Registar equipa" (UC04).

**FA/FE**
- **FE1 (passo 4)** Telefone já registado → mensagem "Este número já está registado" com ligação para "Iniciar sessão"/"Recuperar palavra-passe".
- **FE2 (passo 3)** Dados inválidos → assinala os campos; nada é gravado.
- **FE3 (passo 2)** Termos não aceites → botão "Registar" desactivado.

## UC03 — Recuperar palavra-passe

| | |
|---|---|
| **Actor** | PER-02 / PER-03; **secundário:** Gateway SMS |
| **Pré-condições** | Conta existente |
| **Pós-condições** | Nova palavra-passe; sessões anteriores invalidadas |
| **RF / RN / US** | RF-01.07 · RNF-025 · US-003 |

**FP**
1. O actor escolhe "Recuperar palavra-passe" e indica o telefone.
2. O sistema gera um código de 6 dígitos válido 10 min e envia-o por SMS.
3. O actor introduz o código e a nova palavra-passe.
4. O sistema valida o código, actualiza a palavra-passe e termina as outras sessões.

**FA/FE**
- **FA1 (passo 1)** Telefone inexistente → o sistema responde da mesma forma (não revela se a conta existe).
- **FE1 (passo 4)** Código errado → até 3 tentativas; depois o código é invalidado.
- **FE2 (passo 2)** Falha do gateway SMS → mensagem "Tente mais tarde"; erro registado (RNF-044).
- **FE3** Mais de 3 pedidos por hora para o mesmo telefone → bloqueado (RNF-027).

## UC04 — Registar equipa

| | |
|---|---|
| **Actor** | PER-02 (passa a PER-03) |
| **Pré-condições** | Sessão iniciada; o utilizador não administra nenhuma equipa (RN-18) |
| **Pós-condições** | Equipa criada e activa; utilizador associado como responsável (RF-02.02); contacto principal criado |
| **RF / RN / US** | RF-02.01–05, 02.09 · RN-01, RN-18 · US-005, US-006 |

**FP**
1. O actor abre "Registar equipa" (TEL-04).
2. Indica nome, província, município, bairro (listas encadeadas) e contacto principal (nome, telefone, função).
3. Opcionalmente carrega emblema e descrição.
4. O sistema verifica duplicado: mesmo nome normalizado no mesmo bairro (RF-02.09).
5. O sistema cria a equipa, o vínculo de responsável e o contacto principal.
6. O sistema abre o dashboard (TEL-05).

**FA/FE**
- **FE1 (pré)** Já administra uma equipa → acesso negado com ligação para a sua equipa.
- **FE2 (passo 4)** Duplicado → mensagem com ligação para a equipa existente.
- **FE3 (passo 3)** Emblema > 2 MB ou formato inválido → rejeitado; a equipa pode ser criada sem emblema.

## UC08 — Solicitar jogo

| | |
|---|---|
| **Actor** | PER-03 (equipa desafiante) |
| **Pré-condições** | Sessão iniciada; equipa activa; adversária activa e diferente da própria (RN-19) |
| **Pós-condições** | Solicitação "Pendente"; notificação à desafiada (RF-10.01) |
| **RF / RN / US** | RF-05.03–04, 05.11 · RN-19 · US-012 |

**FP**
1. O actor escolhe "Solicitar jogo" no perfil/cartão de outra equipa (inclui UC07).
2. Preenche data, hora, campo/local, mandante/visitante (opcional) e observação (opcional) — TEL-12.
3. O sistema valida que a data/hora é futura.
4. O sistema grava a solicitação "Pendente" e regista auditoria.
5. O sistema notifica a desafiada e mostra a solicitação em "Enviadas" (TEL-13).

**FA/FE**
- **FE1 (passo 3)** Data passada → erro no campo.
- **FE2 (pré)** Adversária suspensa → botão indisponível.
- **FE3** Limite de 20 solicitações/dia atingido (RNF-027) → mensagem.
- **FA1** O actor cancela a solicitação enquanto "Pendente" → UC10.

## UC09 — Responder a solicitação

| | |
|---|---|
| **Actor** | PER-03 (equipa desafiada; ou desafiante quando recebe uma proposta de alteração) |
| **Pré-condições** | Solicitação "Pendente" ou "Alteração proposta" dirigida à equipa do actor |
| **Pós-condições** | Aceite → **Jogo "Agendado"** com identificador único; Recusada; ou "Alteração proposta" |
| **RF / RN / US** | RF-05.05–08, RF-06.01 · RN-05 · US-013, US-014 |

**FP — aceitar**
1. O actor abre "Recebidas" (TEL-13) e escolhe uma solicitação.
2. Escolhe "Aceitar".
3. O sistema muda a solicitação para "Aceite", cria o **Jogo** (Agendado) com os dados acordados e regista auditoria.
4. O sistema notifica as duas equipas (RF-05.07, RF-10.02).

**FA**
- **FA1 — recusar (passo 2):** escolhe "Recusar" (motivo opcional) → solicitação "Recusada"; desafiante notificada; nenhum jogo.
- **FA2 — propor alteração (passo 2):** indica nova data/hora/local → "Alteração proposta"; a **outra** equipa passa a ser quem responde (repete UC09 do lado dela).
- **FE1** A data proposta já passou quando se tenta aceitar → aceitação bloqueada; sugere propor alteração.
- **FE2** A solicitação foi cancelada entretanto → mensagem "Solicitação já não está disponível".

## UC10 — Cancelar solicitação ou jogo

| | |
|---|---|
| **Actor** | PER-03 (qualquer das duas equipas) |
| **Pré-condições** | Solicitação "Pendente"/"Alteração proposta" enviada pelo actor, ou Jogo "Agendado" do actor |
| **Pós-condições** | "Cancelada"/"Cancelado" com motivo; notificação; eventual falta (RN-24) |
| **RF / RN / US** | RF-05.09, RF-10.03 · RN-24 · US-015 |

**FP**
1. O actor escolhe "Cancelar" (TEL-13 ou TEL-15) e indica o motivo (obrigatório para jogos).
2. Se faltar menos de 24 h para o jogo, o sistema avisa que contará como falta e pede confirmação.
3. O sistema cancela, regista auditoria e notifica a outra equipa.
4. Se < 24 h, o sistema regista **falta confirmada** da equipa que cancelou (RN-24).

**FE**
- **FE1** O jogo já começou → cancelamento indisponível (passa a comparência/UC11).

## UC11 — Registar comparência

| | |
|---|---|
| **Actor** | PER-03 |
| **Pré-condições** | Jogo "Agendado" do actor; hora do jogo já passou; ≤ 7 dias depois (RN-23) |
| **Pós-condições** | Comparência da equipa do actor declarada; se declarou falta da adversária, inicia o prazo de 48 h (RN-16) |
| **RF / RN / US** | RF-06.03–05, RF-07.01–07 · RN-06, RN-07, RN-16, RN-23 · US-017, US-018 |

**FP**
1. O actor abre o jogo (TEL-15) e escolhe "Registar comparência" (TEL-16).
2. O sistema mostra o estado já declarado pela adversária (se existir).
3. O actor escolhe "A nossa equipa compareceu" ou "A nossa equipa não compareceu" e, se compareceu, indica se a adversária **compareceu** ou **faltou**; observação opcional.
4. O sistema grava a declaração da equipa do actor (separada da adversária — RN-06) e regista auditoria.
5. O sistema notifica a adversária (RF-10.05).
6. O sistema avalia a coerência:
   - ambas declararam presença → comparência **Validada** para ambas;
   - o actor declarou falta da adversária → a adversária fica com **falta declarada**, prazo de 48 h (UC11b);
   - o actor declarou que a sua equipa não compareceu → **falta confirmada** da equipa do actor (auto-declaração).

**FE**
- **FE1 (pré)** Antes da hora ou após 7 dias → acção indisponível (excepção: UC22).
- **FE2** Declarações contraditórias (ambas dizem que a outra faltou) → ambas as comparências "Em análise"; caso para o administrador (UC17) — RF-07.05.

## UC11b — Responder a falta declarada

| | |
|---|---|
| **Actor** | PER-03 (equipa acusada) |
| **Pré-condições** | A adversária declarou a falta desta equipa há < 48 h |
| **Pós-condições** | Falta **confirmada** (concorda) ou caso **em análise** (contesta) |
| **RF / RN / US** | RF-07.05, 07.09 · RN-07, RN-16 · US-018 |

**FP**
1. O actor recebe notificação e abre o jogo.
2. Escolhe "Concordo — faltámos" ou "Contesto — comparecemos" (com observação).
3. Concorda → falta confirmada; indicadores e ranking recalculados.
4. Contesta → comparências "Em análise"; caso aberto para o administrador (UC17).

**FA**
- **FA1** Sem resposta em 48 h → o sistema (UC19) confirma a falta.

## UC12 — Submeter resultado

| | |
|---|---|
| **Actor** | PER-03 |
| **Pré-condições** | Jogo do actor, hora já passou, ≤ 7 dias (RN-23); nenhuma das equipas tem falta confirmada |
| **Pós-condições** | Submissão gravada; resultado "Aguardando", "Confirmado" ou "Divergente" |
| **RF / RN / US** | RF-06.06–11, RF-08.01–04, 08.08–09 · RN-08, RN-09 · US-020, US-021 |

**FP**
1. O actor abre "Registar resultado" (TEL-17), vê os nomes das equipas A e B.
2. Indica os golos de A e de B e submete.
3. O sistema guarda a submissão da equipa do actor (histórico de versões — RF-08.08).
4. Se a adversária ainda não submeteu → "Aguardando submissão adversária"; notifica-a.
5. Se já submeteu e os valores são **iguais** → **Confirmado**; jogo "Concluído"; ranking recalculado (RF-09.09); notifica ambas.
6. Se são **diferentes** → **Divergente**; inicia prazo de 72 h (RN-20); notifica ambas (RF-08.05).

**FA**
- **FA1 — corrigir (antes da confirmação):** o actor edita a sua submissão; volta ao passo 3 (RF-06.11).
- **FE1** Golos negativos ou não numéricos → erro de validação.
- **FE2** Resultado já confirmado → edição indisponível; só reabertura pelo administrador (RN-21).

## UC13 — Resolver divergência / solicitar análise

| | |
|---|---|
| **Actor** | PER-03 |
| **Pré-condições** | Resultado "Divergente" |
| **Pós-condições** | Confirmado (por correcção) ou "Em análise administrativa" |
| **RF / RN / US** | RF-08.05–07 · RN-20 · US-022 |

**FP**
1. O actor abre TEL-18 e vê as duas submissões lado a lado com o aviso de divergência.
2. Escolhe "Editar o nosso resultado" → UC12 FA1; se coincidir → Confirmado.

**FA**
- **FA1** Escolhe "Solicitar análise" (com observação) → "Em análise administrativa"; caso aberto (UC17).
- **FA2** Passam 72 h sem acordo → UC19 abre o caso automaticamente.

## UC14 — Consultar ranking

| | |
|---|---|
| **Actor** | PER-01 / PER-03 |
| **Pré-condições** | — |
| **Pós-condições** | — (só leitura) |
| **RF / RN / US** | RF-09 · RN-10, RN-11, RN-14, RN-15 · US-023, US-024 |

**FP**
1. O actor abre "Ranking" (TEL-19); por defeito vê o **município** da sua equipa (ou o geral, se visitante).
2. Pode filtrar por geral, província, município ou bairro.
3. O sistema lista posição, emblema, nome, estrelas (ou "Nova"), Pts, V/E/D, comparência.
4. O actor pode abrir "Como funcionam as estrelas?" (texto público da RN-11) ou o perfil de uma equipa.

## UC17 — Analisar caso e corrigir registo

| | |
|---|---|
| **Actor** | PER-05 |
| **Pré-condições** | Caso aberto (divergência de resultado, comparência contestada/contraditória, pedido de reabertura) |
| **Pós-condições** | Caso resolvido; registo corrigido com justificação; auditoria; ranking recalculado |
| **RF / RN / US** | RF-11.03–05, RF-08.07 · RN-12, RN-20, RN-21 · US-030 |

**FP**
1. O actor abre a lista de casos (TEL-22), ordenada por antiguidade.
2. Abre um caso: vê jogo, submissões/declarações das duas equipas, histórico e contactos.
3. Decide (ex.: resultado 2–1; falta confirmada/anulada) e escreve a **justificação** (obrigatória).
4. O sistema aplica a decisão, marca o caso "Resolvido", grava auditoria (quem, quando, valores, motivo) e recalcula o ranking.
5. O sistema notifica as duas equipas.

**FA**
- **FA1 — reabrir resultado confirmado:** a pedido de uma equipa até 7 dias após a confirmação (RN-21) → resultado "Em análise administrativa" → passos 2–5.
- **FE1** Pedido de reabertura após 7 dias → rejeitado com mensagem.

## UC19 — Expirar prazos (automático)

| | |
|---|---|
| **Actor** | Relógio do sistema (tarefa agendada, p. ex. a cada 15 min) |
| **Pré-condições** | — |
| **Pós-condições** | Faltas sem resposta confirmadas; divergências expiradas em análise |
| **RF / RN** | RN-16, RN-20, RF-10.04 |

**FP**
1. O sistema procura faltas declaradas há ≥ 48 h sem resposta → confirma-as; recalcula ranking; notifica.
2. Procura resultados "Divergentes" há ≥ 72 h → passa-os a "Em análise administrativa"; abre caso; notifica.
3. Procura jogos que começam dentro de 24 h sem lembrete → envia lembrete (UC18).
4. Cada acção automática fica auditada com autor "sistema".
