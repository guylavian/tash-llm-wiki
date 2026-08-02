---
title: "ADFS wont start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/651493/adfs-wont-start
question_id: 651493
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# ADFS wont start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/651493/adfs-wont-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have run into an issue with ADFS.  A month ago I updated the Certificate for ADFS and everything was working fine.  Just recently ADFS wont start.      

When i start it    

The event viewer log expresses something is wrong with the SSL certificate.    

When i run commands via powershell such as get-ADFSCertificate and Set-ADFSCertificate, i get the same errors in the screenshot.  I am unable to start or manipulate ADFS in any way.  I tried restoring to an earlier checkpoint when i know the issue wasnt occurring and I get the same errors.  Therefore it seems the issue is relating to the certificate but i am unsure why since i installed in to the server via mmc, similar to how this article mentions:    

https://nolabnoparty.com/en/adfs-3-0-replace-ssl-certificate/    

Any assistance would be appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-12-04*

It could be the Windows firewall port 1500 is blocked as indicated in the PS output. You may try to check it by temporarily enabled via Windows firewall console or PS as below  

```
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```
