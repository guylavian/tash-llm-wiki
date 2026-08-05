---
title: "Logon type mismatch in domain controller and machine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/895138/logon-type-mismatch-in-domain-controller-and-machi
question_id: 895138
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Logon type mismatch in domain controller and machine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/895138/logon-type-mismatch-in-domain-controller-and-machi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I logon to a domain computer (RDP)  in the event viewer the logon type is 10, but for the same logon, in the Domain Controller the logon type is 3.    

Why all the logon types in DC are 3?!

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-21*

Hi there,    

I suppose this is not a Mismatch as 10 indicates RemoteInteractive.A user logged on to this computer remotely using Terminal Services or Remote Desktop.    

The Logon Type for Logon Number 3 is Network: Used to access a Windows resource (e.g., shared folder) from a system on the network.    

One example is when a computer has a mapped drive to another computer share.    

You can read more about this from the below article  https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc787567(v=ws.10)    

-----------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-06-20*

I wouldn't read too much into this.    

3 = Network The security principal is logging using a network.    

10 = RemoteInteractive A terminal server session that is both remote and interactive.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
