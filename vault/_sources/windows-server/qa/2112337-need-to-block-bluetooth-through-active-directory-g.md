---
title: "Need to block Bluetooth through Active Directory Group Policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2112337/need-to-block-bluetooth-through-active-directory-g
question_id: 2112337
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Need to block Bluetooth through Active Directory Group Policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2112337/need-to-block-bluetooth-through-active-directory-g (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Need to block Bluetooth in Windows client machines, through Windows 2008 R2 Server Active Directory Group Policy. I have managed to block WiFi Hotspot now I need bluetooth

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-28*

Hello，

Thank you for posting in the Microsoft Community forum.

You can try deleting the OBject EXchange (OBEX) communication protocol profile to disable Bluetooth.
Reference: Disabling Bluetooth and Infrared Beaming | Microsoft Learn

I hope this helps.

Best regards

Jacen

——————————————————————————————————

If the Answer is helpful, please click "Accept Answer" and upvote it.
