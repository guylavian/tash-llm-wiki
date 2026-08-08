---
title: "ADCS - I have problem with export private key .pfx and date of expiron certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/795305/adcs-i-have-problem-with-export-private-key-pfx-an
question_id: 795305
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# ADCS - I have problem with export private key .pfx and date of expiron certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/795305/adcs-i-have-problem-with-export-private-key-pfx-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I made new certification templates for certificate request, but if I have checked "Allow private key to be exported" I can not export this cert with private key. And I have set "Validity period" at 5 years, but they generate validation at 2 years.    

What am I doing wrong?    

This is how it looks:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-31*

Hi  

I can't see the bottom of the certificate dialog, but it doesn't look like the private key is available. The dialog should show a key below the date if the private key is present.  

The validity duration in the template is only honoured if the issuing CA has an expiry date greater than the template duration, i think it's double. It's likely that the issuing CA certificate has less than 5 years remaining.  

Gary.
