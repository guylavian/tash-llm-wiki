---
title: "FSMO behaviour"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200450/fsmo-behaviour
question_id: 200450
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# FSMO behaviour

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200450/fsmo-behaviour (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I would like to know what is the difference between these two articles:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/fsmo-transfer-seizure-process    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

One article mentions it applies to Server 2012R2, and the other article mentions that it applies to  Windows Server 2019, Windows Server Standard 2016, Windows Server Essentials 2016, Windows Server Datacenter 2016.    

I have Server 2012 R2. Is there any difference in FSMO operations of 2012R2 vs 2016/2019? For example, FMSO behaviour in shutdown process.    

Please let me know which article applies to Server 2012R2.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

Hi，  

Thank you for posting in our forum  

You can refer to the following article, maybe it will help you  

https://stealthbits.com/blog/what-are-fsmo-roles-active-directory/  

https://www.techopedia.com/definition/25793/flexible-single-master-operation-fsmo  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-16*

There's really no difference in FSMO operation 2012 R2 vs Server 2019. These ones may help.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to Accept as answer if the reply is helpful--
