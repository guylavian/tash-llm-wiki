---
title: "One Outlook client will not connect to MS Exchange mail account when several other clients do."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191136/one-outlook-client-will-not-connect-to-ms-exchange
question_id: 1191136
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# One Outlook client will not connect to MS Exchange mail account when several other clients do.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191136/one-outlook-client-will-not-connect-to-ms-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have five email accounts hosted by Microsoft on Exchange. I access these accounts on a Windows 11 desktop running Outlook and Office Pro 2021, an iPhone, an iPad, and one laptop running Windows 11 and Office Pro 2021. These accounts and email clients have been working well for more than two years. 

This week, I prepared a new laptop and installed an image of the existing working laptop (same make and model) and updated the licenses for Windows, office, and other software. Other than Outlook, everything works perfectly and the image saved me many hours of configuring software. Email messages (received and sent) up to the date of the image are showing but Outlook will not retrieve new email. A small message at the bottom says, "Password Needed" but when clicked, the screen flashes briefly and nothing happens. When I attempt to edit or add one of the working email accounts (only three were configured on the source image) the Outlook wizard searches for a long time, and finally indicates that the account cannot be found. (Problems like keyboard and password errors have been checked and triple-checked.) Outlook appears to be connected to the Internet (as the entire laptop is) but I can't authenticate that it is. It may not make any difference, however, because one of the configuration options sends me to a browser and my Microsoft account, where the same thing happens: Even online via a browser, Microsoft indicates that it cannot find the email address or the password is wrong. At the very same time, I can send and receive test email on all of the several devices I mentioned above using the same email addresses and passwords. The web 365 version of Outlook works well also. I have tried too many solutions to recount here but one that may be relevant is that I did a full online repair of Office Pro 2021 with no change in behavior.

I'm sorry for the long post. I have not encountered a problem quite like this in several decades of working with Outlook.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-26*

I was unable to find a solution and ended up reinstalled Office Pro 2021. This necessitated reconfigured all of the email accounts and relocating the OST and PST account backup systems for each one. In the end, the 40 minutes I was hoping to save by using the existing configuration was lost many times over.
