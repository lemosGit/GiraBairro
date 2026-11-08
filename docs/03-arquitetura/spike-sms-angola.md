# Spike — SMS/OTP em Angola

| Campo | Valor |
|-------|-------|
| Task | M3-08 (#45) |
| Data | 2026-11-08 |
| Tipo | Investigação documental (sem testes de envio) |
| Âmbito | Envio do **código de recuperação de palavra-passe** (RF-01.07, RNF-025). WhatsApp e SMS de notificações ficam fora do MVP (decisão 10) |

## 1. Pergunta

Que fornecedor usar para enviar OTP por SMS para números angolanos (Unitel, Africell, Movicel) de forma fiável e a custo baixo?

## 2. Resultados

> ⚠️ Preços **retirados das páginas públicas dos fornecedores** (algumas recolhidas há 1 a 4 meses) — variam até ~20× entre fornecedores e **têm de ser confirmados por cotação** antes da escolha.

| Fornecedor | Tipo | Preço indicado | Notas |
|------------|------|----------------|-------|
| **KambaSMS** | Local, focado em OTP para Angola | 5 000 Kz / 50 OTP · 22 000 Kz / 200 · 85 000 Kz / 800 (pré-pago, em kwanzas) | API REST com geração e verificação de OTP (6 dígitos, 5 min, 3 pedidos/h) — coincide com RNF-025; cobre Unitel, Movicel e Africell |
| **BulkGate** | Agregador europeu | Unitel ≈ €0,0116 · Africell ≈ €0,1156 / SMS | Sender ID alfanumérico com aprovação de ~4 semanas |
| **BudgetSMS** | Agregador | Unitel ≈ €0,035 · Africell ≈ €0,126 | Recomenda rotas "High Quality" para OTP |
| **ASPSMS** | Agregador | Unitel ≈ €0,04 · Movicel ≈ €0,09 | Descontos por volume |
| **Unimatrix** | Agregador | ≈ $0,11 (Unitel) | Transaccional e promocional ao mesmo preço |
| **eSMSAfrica** | Agregador africano | Rota local ≈ $0,098 · internacional ≈ $0,196 | |
| **SMSPM** | Agregador | Unitel ≈ €0,258 | Oferece também gateway Android com SIM local (€0,01) — **não recomendado** para produção |
| **Twilio** | Global | (consultar) | Suporta sender ID alfanumérico em Angola; a página de directrizes menciona pré-registo — confirmar |

### Regras de sender ID em Angola

- Várias fontes indicam que **não há registo prévio obrigatório** de sender ID alfanumérico, mas os operadores podem **substituir** o remetente (numéricos são trocados por um alfanumérico genérico).
- O sender ID deve conter o **nome da marca** (ex.: `GiraBairro`); IDs genéricos são proibidos.
- A Twilio refere "pré-registo" na sua página para Angola — por confirmar se se aplica.

## 3. Análise

| Critério | Peso | Local (KambaSMS) | Agregador (BulkGate/BudgetSMS) | Global (Twilio) |
|----------|:---:|:---:|:---:|:---:|
| Cobertura dos 3 operadores | Alto | ✅ declarada | ✅ (Africell mais cara) | ✅ |
| Custo por OTP | Médio | ≈ 100–110 Kz | Baixo na Unitel, alto na Africell | Provavelmente o mais alto |
| Pagamento | Médio | **Kwanzas**, pré-pago | Euro/cartão internacional | Dólar/cartão |
| Funcionalidade de OTP pronta | Baixo | ✅ (gera e verifica) | ❌ (só envio) | ✅ (Verify) |
| Dependência / risco do fornecedor | Médio | Fornecedor pequeno | Médio | Baixo |

No volume do piloto (dezenas a centenas de recuperações por mês) o custo é pequeno em qualquer opção; o factor decisivo é a **taxa de entrega** em cada operador e a **forma de pagamento**.

## 4. Recomendação

1. **Implementar a interface `EnviadorSMS`** em `app/integrations/sms.py` (ver [padrão do backend](padrao-backend.md)) com:
   - `ConsolaSMS` (dev: imprime o código no log);
   - um adaptador por fornecedor, escolhido por `SMS_FORNECEDOR` ([ambientes](ambientes.md)).
2. **A geração e verificação do OTP ficam na nossa API** (tabela `codigo_recuperacao`, RNF-025), mesmo que o fornecedor ofereça OTP — assim trocar de fornecedor não muda o fluxo nem os dados.
3. **Fornecedor inicial:** pedir cotação a **KambaSMS** (pagamento em kwanzas, foco em Angola) e a **um agregador** (BulkGate ou BudgetSMS) como alternativa/redundância.
4. **Teste em staging (antes de M9-05):** enviar 20 OTP para números de cada operador (Unitel, Africell, Movicel) e medir taxa de entrega e tempo. Escolher o fornecedor com ≥ 95 % de entrega em < 30 s.
5. **Sender ID:** `GiraBairro`.

## 5. Próximos passos

| Acção | Responsável | Quando |
|-------|-------------|--------|
| Pedir cotações (KambaSMS + 1 agregador) | Dono do produto | Antes de M5-06 |
| Implementar `EnviadorSMS` + `ConsolaSMS` | Backend | M5-06 |
| Adaptador do fornecedor escolhido + teste de entrega por operador | Backend | Staging (M10-01) |

## Fontes

- [KambaSMS — SMS OTP and Transactional SMS API](https://liners.com/kambasms)
- [BulkGate — preços SMS Angola](https://www.bulkgate.com/en/pricing/sms/ao/angola/)
- [BudgetSMS — SMS Gateway Angola](https://www.budgetsms.net/sms-gateway-pricing/ao/angola/)
- [ASPSMS — Angola](https://www.aspsms.com/en/networks/angola/)
- [Unimatrix — Angola SMS Pricing](https://www.unimtx.com/sms/ao)
- [eSMSAfrica — Africa SMS Pricing Index](https://esmsafrica.io/sms-pricing)
- [SMSPM — Send SMS to Angola](https://smspm.com/en/country/send-sms-angola/)
- [Messaggio — Unitel Angola](https://messaggio.com/operators/unitel/)
- [Twilio — Angola SMS guidelines](https://www.twilio.com/en-us/guidelines/ao/sms)
- [Twilio — International support for Alphanumeric Sender ID](https://support.twilio.com/hc/en-us/articles/223133767-International-support-for-Alphanumeric-Sender-ID)
- [Link Mobility — Sender ID Angola](https://docs.linkmobility.com/regulatory-guidelines/sender-id/angola)
- [SMS.to — Sender ID registration by country](https://support.sms.to/en/support/solutions/articles/43000562659)
- [SureSMS — SMS Rules for Angola](https://suresms.com/en/country-rules/angola/)
