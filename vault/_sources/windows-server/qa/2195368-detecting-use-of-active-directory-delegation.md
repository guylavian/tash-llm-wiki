---
title: "Detecting use of active directory delegation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195368/detecting-use-of-active-directory-delegation
question_id: 2195368
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 7
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Detecting use of active directory delegation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195368/detecting-use-of-active-directory-delegation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All!

I am currently trying to investigate how certain unconstrained delegations are used in our active directory enviroment. Since the system owners can't explain where its delegating to, i cannot remediate this without knowing how to set this up properly, to not harm the production enviroments. 

Do any of you have information on how to investigate where a user/device, configured with unconstrained delegation, is using this delegation right?

Ideally, i would like to see which SPNs they are presenting the delegated credentials too.

I tried looking in our Active directory event log, without any luck, maybe i am looking for the wrong thing or dont know how to filter.

Since we have Defender for identity, i tried looking for delegated logins via advanced hunting i the security portal, without any luck.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-09*

Hi Daisy

Thanks for the reply. 

We know where the unconstrained delegations is enabled and used, but not how its used. 

The issue is detecting how its used.

In the double-hop problem, User A connects to server B, which should further authenticate to server C, hence delegation on server B is required,

In my scenario, i know User A and server B, but have problems finding how and when server B is using its unconstrained delegation and identifying server C.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-09*

Hello Troels Linderoth,  

Thank you for posting in Microsoft Community forum.  

You can view and delete the delegated permissions based on the links below  

Active Directory Delegation Overview (netwrix.com)

Active Directory: How to View or Delete Delegated Permissions | Microsoft Learn

Delegating Administrative Permissions in Active Directory | Windows OS Hub (woshub.com)

Detecting Delegated Permissions in Active Directory (netwrix.com)  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
