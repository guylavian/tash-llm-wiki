---
title: "Enabling Network Discovery via GPO does not work when Windows Firewall turned on"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/734773/enabling-network-discovery-via-gpo-does-not-work-w
question_id: 734773
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Enabling Network Discovery via GPO does not work when Windows Firewall turned on

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/734773/enabling-network-discovery-via-gpo-does-not-work-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environment: Windows domain  

I'm trying to turn on network discovery and I've created a computer-targeted GPO  

I create a test OU and put one computer in said OU and apply GPO to the computer. I then run gpupdate /force on the targeted machine and restart the computer. I then run gpresult /scope computer /v and confirm that the GPO is being applied.  

But when i go on the computer client the network discovery and file sharing is turn off (control panel).  

It seems that when the firewall on client is off the network is on and viceversa when the firewall is on this rule is off.  

I’ve:  

-  enable LLTDIO and RSPNDR  

-  enable the preset configuration of the firewall for network discovery and file and print sharing

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-05*

Hello, someone found a solution to the problem of the UP Firewall in the domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-16*

all allowed correctly but still doesn't work

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-15*

Might doble check these ones are allowed.  

Network Discovery (LLMNR-UDP-In)  

Network Discovery (NB-Datagram-In)  

Network Discovery (NB-Name-In)  

Network Discovery (Pub-WSD-In)  

Network Discovery (SSDP-In)  

Network Discovery (UPnP-In)  

Network Discovery (WSD Events-In)  

Network Discovery (WSD EventsSecure-In)  

Network Discovery (WSD-In)  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-15*

correct, is totally unmanaged but the policies are applied correctly

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-14*

Will they stay on if turned on here?
