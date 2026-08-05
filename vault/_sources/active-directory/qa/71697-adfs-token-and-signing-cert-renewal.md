---
title: "ADFS Token and Signing cert renewal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/71697/adfs-token-and-signing-cert-renewal
question_id: 71697
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Token and Signing cert renewal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/71697/adfs-token-and-signing-cert-renewal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys!  

I'm doing my first cycle of token certs renewal. At this moment I have 2 for both, Primary and Secondary. Everything seems to be just fine.  

I'm trying to be ahead of the game and tried to replace the RP configuration in advance. I did it for my first RP and replaced the old cert with the new one (signing) and everything worked just fine! Hell yeah, so easy!!!  

So I decided to move to the second RP and for my surprise it did not work. So I tried one more RP and same thing! I did the forth and omg same thing.  

So now I'm confuse but I did some research and looks like the RP must have be able to "read/understand/work" with those 2 certs, Primary and Secondary. Is this really the case?  

I have about 10 RP/applications and 1 I need the vendor to perform the change. Some I can do it on the Operating System (Linux) changing the config file and some others I really need to access the UI and change it over there, of course authenticated. So 9 are on premises and 1 is like a SaaS.  

That said, how am I supposed to perform this configuration/rollout?  

If the cert expires, I will not be able to login on the application/RP to change the configuration to the newer cert.  

Please, some advise, guidance, lesson learned is very welcome!  

Thanks!

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
