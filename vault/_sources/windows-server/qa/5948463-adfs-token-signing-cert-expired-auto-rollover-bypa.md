---
title: "ADFS Token-Signing Cert Expired (Auto-rollover bypassed) / Need safe manual rollover steps"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5948463/adfs-token-signing-cert-expired-auto-rollover-bypa
question_id: 5948463
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# ADFS Token-Signing Cert Expired (Auto-rollover bypassed) / Need safe manual rollover steps

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5948463/adfs-token-signing-cert-expired-auto-rollover-bypa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,

We have a P1 incident on ADFS. The automated token-signing certificate rollover failed to trigger, and current cert is already expired. Federated login for all integrated apps is currently down.

We need to execute a manual certificate renewal immediately. However, we must ensure we don’t disrupt the existing relying party trusts (RPT) during the process. We cannot afford to have partners' auth pipelines choke.

What is our standard operating procedure to renew this manually and sync the metadata smoothly? Do we need to disable `AutoCertificateRollover` first via PowerShell before we push the new primary cert, or can we just let it roll?

Please advise on the safest way to execute this. Loop in anyone who has done this recently.

## Answers

_No answers on this thread._
