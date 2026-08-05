---
title: "Users not able to authenicate to domain controller after windows updates?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/709768/users-not-able-to-authenicate-to-domain-controller
question_id: 709768
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Users not able to authenicate to domain controller after windows updates?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/709768/users-not-able-to-authenicate-to-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After updating my server 2019 domain controllers (DC1, DC2), users are not able to authenticate. I did a snapshot prior to the updates in VMware, but every 24 hours I am having to revert back to that same snapshot over and over again so users can authenticate again. I even went as far as disabling the "windows update" service all together on both domain controllers.     

Here are the updates that were used:  

-  Microsoft Defender KB2267602  

-  Windows Malicious Software Removal Tool x64 KB890830  

-  .NET Frameworks 3.5, 4.7.2 and 4.8 for Windows Server 2019 KB5009718  

-  Cumulative Update for Windows Server 2019 (1809) for x64-based Systems KB5009557

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2022-01-25*

Cumulative Update for Windows Server 2019 (1809) for x64-based Systems KB5009557  

You'll also want to install the out of band fix for the problematic Jan11th update.  

https://support.microsoft.com/en-us/topic/january-18-2022-kb5010791-os-build-17763-2458-out-of-band-43697313-d8e0-4918-b6df-7f64d4d9a8cd  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-01-25*

KB5010791 replaces KB5009557 so it would no longer be applicable.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-26*

In progress.... I'll keep you posted...

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-26*

You certainly can but KB5010791 replaces KB5009557 so it isn't required.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-25*

I'm going to leave KB5009557 in "Pending" for now if this is the update that is the issue.  

I did download and installed the KB5010791 on the domain controller, so we will wait and see. By tomorrow (24hrs) I'll know if this patch worked. I did notice after installing the KB5010791 patch and doing a reboot, I still see KB5009557 sitting there in pending. Shouldn't that KB have gone away?  

Thanks I hope this works.
