---
title: "Installing Windows LAPS over Legacy LAPS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187170/installing-windows-laps-over-legacy-laps
question_id: 2187170
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Installing Windows LAPS over Legacy LAPS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187170/installing-windows-laps-over-legacy-laps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I have a simple LAB - of 1 DC  and 1 member server (both 2019) which has had legacy LAPS installed (schema extended etc).

Now when I installed the MS update on the member server and then tried to run the permission command I got an error saying have you extended the schema.  I tried to extend the schema using the new LAPs command but got an exception error.

Now I can't find any documentation or info regarding 

1 ) In an environment where legacy LAPS has been configured, do you have to extend the schema again?

-  Do you have to run the permission command on the OU so the machines can write to the password attribute?

The LAPS has been out for a while so we should have more info.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-06*

Hello Mr Tech Person,  

Thank you for posting in Microsoft Community forum.  

Here are the answer for your reference.  

1 ) In an environment where legacy LAPS has been configured, do you have to extend the schema again?  

A1: Yes, the Windows Server Active Directory schema must be updated prior to using Windows LAPS. This action is performed by using the `Update-LapsADSchema` cmdlet.  

Because for legacy Microsoft LAPS, the update method for schema is different (below) as Windows LAPS.  

Here is the schema update method for legacy Microsoft LAPS:  

Import module AdmPwd.PS and update AdmPwdADSchema
Import-module AdmPwd.PS  

Update-AdmPwdADSchema  

We need to run these commands while logged in to the network as a schema admin.
2) Do you have to run the permission command on the OU so the machines can write to the password attribute?  

A2: Yes, read the first link below for more information.  

Get started with Windows LAPS and Windows Server Active Directory | Microsoft Learn  

Windows LAPS overview | Microsoft Learn

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
