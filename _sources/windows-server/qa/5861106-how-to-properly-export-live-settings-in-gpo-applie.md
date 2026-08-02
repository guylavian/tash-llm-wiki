---
title: "How to properly export live settings in GPO applied to a machine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5861106/how-to-properly-export-live-settings-in-gpo-applie
question_id: 5861106
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Q&A User"]
---
# How to properly export live settings in GPO applied to a machine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5861106/how-to-properly-export-live-settings-in-gpo-applie (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I needed to get which of the following settings, and with which values, are applied live on a server. The needed settings are : 

SeInteractiveLogonRight

SeRemoteInteractiveLogonRight

SeDenyInteractiveLogonright

SeDenyRemoteInteractiveLogonRight

It seems I'm achieving it by doing : 

Secedit /Export /Areas User_Rights /cfgSecedit /Export /Areas User_Rights /cfg c:\undirectorio\gpo.txt

Later by checking the file I achieve my goal.

I normally check too this other command file generated : 

Secedit /Export /Areas SECURITYPOLICY /cfg Secedit /Export /Areas SECURITYPOLICY /cfg c:\undirectorio\gpo.txt

They seem to give me what I need even when for instance "SeDenyInteractiveLogonright" is set in the local gpo and set too in a gpo applied to the OU where the server belongs. The behavior is the expected one. I get in the secedit output the value set in active directory GPO in the OU.

So, my question basically is... is this way the correct one of achieving my goal of getting dump in a plain text file the live settings of the policy applied to the virtual machine?. I can have only a local gpo or could have a local gpo (with default values or not) and later n number of gpo applied at different levels in active directory (site, domain, ou... etc...). So the real question is, my secedit command should give me what I'm trying to get and then to have live seetings in the machine (after all gpo at differrent levels are applied) ?.

I have seen too that there is a flag /mergedpolicy but it seems to just output then those values that I have applied at local policy and too at active directory policy?. Am I wrong?.

Best regards

Thank you so much,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-04-16*

By the way, when you say : 

--When used, it exports the merged view of domain and local policy security settings. It is not limited to “only values that exist in both local and AD policy”; it is intended to output the merged result--

You mean that if for instance 4 gpo (local and some other) are applied to a vm in the case that for instance SeInterativeLoginright is configured in all of them with a different user in each, with the /mergedpolicy I would see 4 users in that setting instead of the one which would be the one applied (from the winning gpo)?.

Cheers,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-04-16*

Thank you so much for your answer but I'm not really sure what do you mean exactly in point 6 when you say : 

"and optionally `/mergedpolicy` if exporting from a custom DB with `/db"`

I want to dump live applied settings... for example : 

-  Machine 1 has a local gpo

-  Machine 1 has appied another (for example) 3 active directory gpo at ou level or site or domain... or whatever....

The result of all that gpo after being applied, prioritized the corresponding way etc... is that SeDenyRemoteInteractiveLoginright has two users and a group. And for instance that SeInteractiveLoginright has 2 users.

I'm trying to see that with secedit. Am I doing it correctly if I do then : 

secedit /export /areas user_rights /cfg C:\undirectorio\gpo.txt

Thank you!!!!!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-04-16*

Sorry this was repeated and I don't really know how to remove it...
