---
title: "Exchange certificate - SMTP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1521667/exchange-certificate-smtp
question_id: 1521667
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange certificate - SMTP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1521667/exchange-certificate-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Could you please tell me why I need to install a certificate for SMTP? I don't use POP3 and IMAP clients.
Am I right, if I install a certificate for SMTP and IIS, so that the sender sets STARTTLS session, it is not enough, I must additionally on the receiving connector to install a certificate fingerprint ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-01*

You dont absolutely need to install a certificate for SMTP, but typically when you install a 3rd party certificate for IIS, you also assign that certificate to SMTP, but its not required unless you are using that 3rd party certificate for Exchange Hybrid or a secure SMTP connection with a partner or POP/IMAP.
You dont have to do anything on the receive connector unless you want it to use a specific cert and in which case you wouldset the certname on the receive connector to match a subject name on the certificate.
https://practical365.com/configuring-the-tls-certificate-name-for-exchange-server-receive-connectors/
