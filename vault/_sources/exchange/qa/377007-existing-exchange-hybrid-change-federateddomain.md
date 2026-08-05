---
title: "existing Exchange Hybrid change FederatedDomain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/377007/existing-exchange-hybrid-change-federateddomain
question_id: 377007
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# existing Exchange Hybrid change FederatedDomain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/377007/existing-exchange-hybrid-change-federateddomain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have an existing Exchange Hybrid-deployment (with Ex2013 OnPrem) in production use for some time and everything in collaboration works fine.    

But we have a relict: The FederatedDomain is a domain name (abc.de), we are not using anymore since a company rebranding. abc.de should be removed everywhere (mail addresses, papers, websites, DNS, ...)    

-  current Azure/EXO verified domains: abc.de (old), xyz.de (new)    

-  current EX-mail adresses: example@xyz  .de    

In Get-FederationInformation, Get-FederatedOrganizationIdentifier and Get-FederationTrust there is abc.de still listed.    

In my understanding newly created Exchange-Hybrid-deployments don't create the FederationTrust anymore, and are using OAuth for FreeBusy.    

We have no FreeBusy-sharing with external organizations except of Microsoft 365 with our cloud-mailboxes.    

Can I delete the old domain via Remove-FederatedDomain and Remove-FederationTrust. And afterwards simply running Hybrid Configuration Wizard again?    

This support article points in this direction: running-hybrid-configuration-wizard-fails    

I'm thankful for every replay.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-30*

Hi @Anonymous   ,    

Yes, you could. The Exchange Federation Trust is automatically created when you running the  Exchange Hybrid Configuration Wizard (HCW). Then you could run the command to check the  federated domain again.    

If there are any related errors during the operation, you can share them here.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-10*

Thank you, it worked as planned.
