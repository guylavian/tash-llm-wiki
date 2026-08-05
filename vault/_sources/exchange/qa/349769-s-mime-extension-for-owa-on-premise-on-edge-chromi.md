---
title: "S/mime extension for OWA (on-premise) on Edge chromium"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/349769/s-mime-extension-for-owa-on-premise-on-edge-chromi
question_id: 349769
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# S/mime extension for OWA (on-premise) on Edge chromium

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/349769/s-mime-extension-for-owa-on-premise-on-edge-chromi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have been using the S/MIME ActiveX extension on IE without issue, but I can't find a way to make it work on Edge Chromium (we have Exchange 2016 on premise).  

I've been using the gpo to install the extension on Edge Chromium but apart from the Outlook logo showing up in the extension bar, it doesn't work. I have added our server in the extension configuration but to no avail. The browser can't decode digital signatures and doesn't offer to install anything related.  

Regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-09*

Hi @CS  ,    

but I can't find a way to make it work on Edge Chromium (we have Exchange 2016 on premise)    

According to the official document below, "S/MIME in Outlook on the web in Exchange 2016 is only supported in Internet Explorer". So seems it's the expected behavior that S/MIME extension doesn't work on Edge Chromium.    

S/MIME settings for Outlook on the web in Exchange Server    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
