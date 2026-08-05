---
title: "Deny download & allow view of attachments with OWA 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199201/deny-download-allow-view-of-attachments-with-owa-2
question_id: 199201
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Deny download & allow view of attachments with OWA 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199201/deny-download-allow-view-of-attachments-with-owa-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have created a new mailbox policy and disabled the following property (Set-OwaMailboxPolicy -name NewPolicy DirectFileAccessOnPublicComputersEnabled $false) to deny download & allow only view the attachments with OWA 2016 (Exchange 2016 On-Premise). But once we apply the policy to end user, he could not view the attachments (we tried to view Word / excel / pdf files with different browsers). As a security recommendation we have to implement this policy. How can we fix the issue and allow view permission & deny download?  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Thank You Andy & Kael  

OOS is already in place and used by OneDrive. So we will use / configure the same URL with Exchange.  

As of now we have 2 X Exchange servers in same Datacenter. Later we may have other servers in DR or may have some hybrid configuration. So we will apply the settings at server level, what do you think?   

Thank You.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-16*

@LMS       

Hi,    

Agree with Andy,you need to install an Office Online Server to enable previewing attachments in OWA.    

By default, the following file types are displayed using Office Online Server:    

Word documents (doc, docx, dotx, dot, dotm extensions)    

Excel documents (xls, xlsx, xlsm, xlm, xlsb extensions)    

PowerPoint documents (ppt, pptx, pps, ppsx, potx, pot, pptm, potm, ppsm extensions)    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
