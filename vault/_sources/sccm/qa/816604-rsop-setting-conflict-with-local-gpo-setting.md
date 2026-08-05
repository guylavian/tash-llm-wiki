---
title: "RSOP setting conflict with Local GPO setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/816604/rsop-setting-conflict-with-local-gpo-setting
question_id: 816604
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
---
# RSOP setting conflict with Local GPO setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/816604/rsop-setting-conflict-with-local-gpo-setting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, In RSOP, the setting for the below screen shot is found in for few servers where they are getting patched through SCCM ![194051-image.png][1] ![193990-image.png][2] In other servers where SCCM not able to patch are also having the similar kind of setting , but as per the SCCM team they are asking to remove the setting via the Domain GPO and set it as non configured, so that they can patch the servers after pushing SCCM client setting to the Local GPO of that servers from their end But I am able to see these servers also having Local GPO configured correctly by SCCM team It is weird case , any advice please [1]: /api/attachments/194051-image.png?platform=QnA [2]: /api/attachments/193990-image.png?platform=QnA

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-19*

Hi @ Amandayou-MSFT   

Sorry for my wrong question , which I asked because I got the information from the team wrongly .  

Actually the server is getting patched via SCCM if the GPO is met as per the setting you posted , you are correct  

Thank you for your support

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-19*

Hi @ Amandayou-MSFT   

Thank you for the clear explanation but please clarify me the question I asked earlier

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-19*

Hi @  Amandayou-MSFT   

Thank you for the reply,  

Servers getting patched through SCCM are having Local Group policy as you mentioned  

But other few servers which are not getting patched, having the same setting but the setting Specify intranet Microsoft update service location in RSOP controlled by Domain GPO.  

When I checked the Local GPO in the server, by gpedit, it is found that the setting Specify intranet Microsoft update service location set by SCCM   

My question is how setting set through Domain GPO is overridden by SCCM in Local server

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-19*

Hi @SHANMUGAMSWAMINATHAN-5167,    

these servers also having Local GPO configured correctly by SCCM team    

It is normal. In SCCM, when a domain policy is created for the Specify intranet Microsoft update service location setting, it overrides the local policy. So as we mentioned, we should not configure the Active Directory policy for client computers.    

When the software update point is created for a site, clients receive a machine policy that provides the software update point server name and configures the Specify intranet Microsoft update service location local policy on the computer.     

So if the computer is manged by SCCM, the client have local GPO configuration rather than Active Directory policy normally.     

Here is the screenshot we could refer to:    

    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
