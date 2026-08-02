---
title: "how to fix microsoft.exchange.clients.owa2.server.core.owainvalidtimezoneexception"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1655872/how-to-fix-microsoft-exchange-clients-owa2-server
question_id: 1655872
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# how to fix microsoft.exchange.clients.owa2.server.core.owainvalidtimezoneexception

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1655872/how-to-fix-microsoft-exchange-clients-owa2-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Ever since updating to outlook new a few weeks ago, i've been getting the following message microsoft.exchange.clients.owa2.server.core.owainvalidtimezoneexception.

please help

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-16*

Dear @Dirk48544  ,

I had the exact same error message while trying to open the new outlook app on my laptop.

Here's how I fixed it:

Open your internet browser and type in "Outlook Login". Open up the Microsoft Page and then log in with your email account and password. Now you should be able to access your account including all the apps such as Excel, Word etc.

In the top right corner, you should see your profile picture, if you have one and next to it you can find the settings.

Click on them and then click on the first option on the left side called General Settings.

There you should find the option called language and time where you can change your time zone.

In my case the setting was at UTC+0, while it actually should have been UTC+1. Just type in the city where you live if you're unsure. Click on save, then close everything and log off from your account.

Close your browser, restart your computer and then try to open up the outlook app and voila it hopefully worked for you as well!
