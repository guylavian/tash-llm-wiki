---
title: "Functional Level / Sysvol Migration Question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/213741/functional-level-sysvol-migration-question
question_id: 213741
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Functional Level / Sysvol Migration Question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/213741/functional-level-sysvol-migration-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello - I have an Active Directory environment that is at Forest Functional Level 2003 (Domain fl of 2008R2).  Also, the sysvol migration from FRS to DFSR was partially completed and all DC's are in State 2 (REDIRECTED).   My question is.. should we complete the sysvol migration and get to the final state of 3 (eliminated), or is it required to have our Forest Functional Level to Server 2008R2 prior to completing the sysvol migration.  We're in this limbo state with sysvol (prior tech did this years ago and then left without letting anyone know).  I read an article indicating the FFL should be changed to 2008r2 prior to the sysvol migration to DFSR.  We have 4 DC's in total.. 3 are Server 2012R2 and one is Server 2008R2.  Thanks to anyone who may have experience with this and can offer any advice.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-30*

Hi,  

Thank you for posting on us.  

This article may help you  

reference:https://judeperera.wordpress.com/2019/03/19/sysvol-migration-from-frs-to-dfsr-step-by-step/  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-29*

I think its your only option. No this in of itself would not cause additional problems. I'd also confirm the required ports are flowing between sites.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-29*

Thanks for your reply.  The tech who did this got to the Redirected state and then left.  Nobody knew he did this so it's been in this state for about 1.5 to 2 years.  The health of the domain looks fine.  We were also thinking of going back to state 0 but wasn't sure if that would cause problems.  I'll have to look into it more.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-29*

The domain functional level needs to be at 2008 or higher. It should have gone fairly quickly assuming domain health is 100%. Certainly shouldn't have been years. Since it redirected state I'd suggest canceling   

`dfsrmig /setglobalstate 0`  

then confirm health is good before trying again.  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to Accept as answer if the reply is helpful--
