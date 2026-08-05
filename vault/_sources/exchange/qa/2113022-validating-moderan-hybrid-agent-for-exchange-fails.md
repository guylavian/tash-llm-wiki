---
title: "Validating Moderan hybrid agent for Exchange fails with \"The remote server returned an error: (401) Unauthorized\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2113022/validating-moderan-hybrid-agent-for-exchange-fails
question_id: 2113022
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Validating Moderan hybrid agent for Exchange fails with "The remote server returned an error: (401) Unauthorized"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2113022/validating-moderan-hybrid-agent-for-exchange-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently our Modern Full Hybrid configuration is failing when trying to rerun the HCW get all functionality working again.  I have exhausted all I know to try to this point.  I have rerun the wizard many times trying two different credentials both having Global and Domain Admin, Organization rights.   I have followed several articles that point to this issue to no success. Including reset the endpoint password in AD and Exchange online admin center, Deleting the endpoint connection manually, disabling windows extended protection, reviewed and bypassed conditional access policies for MFA, as well as testing using "Test-HybridConnectivity -TestO365Endpoints" which did not find any issues.  I have also updated Azure AD connect to the latest version just to cover that basis. See attached logs and screenshots for additional information.  Here are a few articles I used/referenced:

 

https://learn.microsoft.com/en-us/exchange/hybrid-deployment/hybrid-agent

 

https://www.alitajran.com/mailbox-replication-service-was-unable-to-connect-to-the-remote-server/

 

https://learn.microsoft.com/en-us/exchange/hybrid-configuration-wizard

 

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/security-best-practices/exchange-extended-protection?view=exchserver-2019#extended-protection-and-modern-hybrid-configuration

 

https://learn.microsoft.com/en-us/answers/questions/1615304/hybrid-agent-setup-failing-on-validating-hybrid-ag

 

We are running Exchange 2019 update 14 or 15.2.1544.11 on a patched 2022 Server.  All exchange roles are on this server.

## Answers

_No answers on this thread._
