---
title: "FSMO issues can't demote properly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1052972/fsmo-issues-cant-demote-properly
question_id: 1052972
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# FSMO issues can't demote properly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1052972/fsmo-issues-cant-demote-properly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am unable to correct entries in adsiedit and get the following text for this command.    

ldifde -f Infra_DomainDNSZones.ldf -d "CN=Infrastructure,DC=DomainDnsZones,DC=mydomain,DC=Local" -l fSMORoleOwner    

Results in Word    

dn: CN=Infrastructure,DC=DomainDnsZones,DC=MyDomain,DC=local    

changetype: add    

fSMORoleOwner:     

 CN=NTDS Settings\0ADEL:90ac7dd3-e0ad-4f1a-adf7-bc80829142ea,CN=OLD DOMAIN CONTROLLER\0AD    

 EL:72213d36-d6c3-40bf-986b-6550bb04688e,CN=Servers,CN=Default-First-Site,CN=Si    

 tes,CN=Configuration,DC=MyDomainName,DC=local    

ldifde -f Infra_ForestDNSZones.ldf -d "CN=Infrastructure,DC=ForestDnsZones,DC=mydomain,DC=Local" -l fSMORoleOwner    

Results in Word after clearing entry using adsiedit and now operation failed error code:0x20ae    

The Role owner attribute could not be read when try to enter correct info    

Currently FSMORoleOwner <not set> as I cleared it when trying to change it    

dn: CN=Infrastructure,DC=ForestDnsZones,DC=MyDomain,DC=local    

changetype: add

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

You have not addressed the issue. This is not my exact issue but as you will see is related.    

https://social.technet.microsoft.com/forums/en-US/39e8b5e2-4ea1-40ff-863a-e3cdc8e409ae/how-to-correct-fsmoroleowner-attribute-dsquery-shows-incorrect-adsi-shows-correct?forum=winserverDS

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-18*

based on my subject "FSMO issues can't demote properly" I am not sure why you are asking.    

Ok, with this limited info the simplest solution may be to remove problem one from network, sieze roles (if needed) to another healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove remnants    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

then rebuild failed one if that's the goal.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

I am sorry DSP but based on my subject "FSMO issues can't demote properly" I am not sure why you are asking.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

The remnants only show in adsiedit and when using the commands I posted

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-18*

Not sure what you're trying to do? If the PDC emulator has failed then you could seize roles to another healthy one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform some cleanup prior to rebuild    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
