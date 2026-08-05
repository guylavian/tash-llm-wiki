---
title: "How to make printers installed by GPO/GPP have server-side settings?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380817/how-to-make-printers-installed-by-gpo-gpp-have-ser
question_id: 380817
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How to make printers installed by GPO/GPP have server-side settings?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380817/how-to-make-printers-installed-by-gpo-gpp-have-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Windows Server 2019 domain controller which has some network printers installed using TCP/IP Port 9100 and publishes all of those printers as shares. The important thing to note is that while it's only 3 different physical printers, those 3 exist with 9 different names and settings on the server and therefore as shares. The differences are which paper bin to use and if to print portrait or not by default per printer.  

All of those 9 different logical printers need to be available at the clients, therefore a GPO/GPP exists to make them available. While that works in genau, the printers are available using their expected names, the server side settings corresponding for each name are NOT used. Instead, all of those printers seem to have been installed with their default settings and therefore behave differently than expected when actually used. While changing those settings per client to correspond with expected behaviour and server side name makes things work, that's obviously not the goal when having an automatism like GPO/GPP available as well.  

So, what do I need to do to get exactly the settings the share itself have? At least by default, so users might change those for good reasons or even disallowing the user to change the relevant settings. Though, the important thing is to at least start with a 1:1 copy of the settings the share have.  

Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2022-05-25*

Best regards

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-17*

Hi, is everything ok?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-13*

Hi,  

Haven't received your message in a few days, was your issue resolved?  

Best regards

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-04*

Hi,  

First of all, could you please provide the models of these 3 different printers?  

When you deployed these 3 printers, what settings did you make? And, which of these settings must be displayed on the client side 1:1?  

Additionally, is it possible provide a screenshot and attach a description, which will help us to troubleshoot.  

Best Regards
