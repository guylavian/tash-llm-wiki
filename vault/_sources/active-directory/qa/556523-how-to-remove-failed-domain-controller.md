---
title: "How to remove failed Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/556523/how-to-remove-failed-domain-controller
question_id: 556523
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# How to remove failed Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/556523/how-to-remove-failed-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have couple of Windows Server 2008 R2 Domain Controller in my Domain, out of which one DC is failed & we unable to bring it back to the network.  

I came to know some articles where it has been stated to delete the DC object directly from ADUC & ADSS. I just want to understand what are the right steps to follow so we can remove the failed DC with no metadata footprint.  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-17*

Hello Raj A,  

This step-by-step guide will help you achieve it completely:  

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564  

Hope this answers your query,  

Best regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-17*

You can follow along here to do the cleanup.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
