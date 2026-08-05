---
title: "HQ site and Branch site domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090035/hq-site-and-branch-site-domain-controllers
question_id: 1090035
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# HQ site and Branch site domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090035/hq-site-and-branch-site-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone. Just want to ask help and advice regarding in setting up 2 different domain controllers in 2 different regional sites but share the same forest.    

We have an existing Domain controller in our HQ site and we are planning to expand our business to another region and that will serve as our Branch Office.    

I dont want our employees from the Branch office to authenticate from our HQ site eveyrtime they login so i want to make a DC fir Branch Office only.    

So my question is can i make a PDC in my Branch office and retain the PDC from my HQ site? So in short 2 PDC from 2 different regional sites is that possible?    

Can someone suggest a youtube tutorial on this one?    

Sorry not very good in servers    

Thank you all and more power!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-20*

i ran the command ipconfig /all from a user client machine. and any user client machine i tested it gives me the same result for the DNS Servers.    

see image above

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-20*

when you type in ipconfig /all i wonder why my secondary DC    

What is this being run on? Also seems to be chopped off, please post the full result (ipconfig /all) as well as it's role.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-15*

Ok, that's fine but there will always only be a single PDC Emulator per domain.    

https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/f96ff8ec-c660-4d6c-924f-c0dbbcac1527    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-15*

You could only have one PDC Emulator per domain. Seems you're asking about adding a child domain so you could follow along here.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
