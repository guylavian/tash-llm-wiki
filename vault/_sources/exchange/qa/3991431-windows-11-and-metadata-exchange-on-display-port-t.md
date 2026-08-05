---
title: "Windows 11 and metadata exchange on Display Port to HDMI conversion HDR; is uni-directional Display Port to HDMI Required?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3991431/windows-11-and-metadata-exchange-on-display-port-t
question_id: 3991431
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows 11 and metadata exchange on Display Port to HDMI conversion HDR; is uni-directional Display Port to HDMI Required?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3991431/windows-11-and-metadata-exchange-on-display-port-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows 11 HDR on 2 monitors

Has anyone ever gotten Win 11 HDR to work on more than one monitor?

There are a lot of asks for help threads in the Microsoft Community forum with folks asking how to get HDR to work on Windows with multiple monitors (on my LG TV the visual difference is quite large, but thus far have not been able to get it to work on two duplicated outputs on my ASUS Phoenix NVIDIA GeForce RTX 3050 to the same LG TV PhysX right now are:

-  HDMI --> LG TV

-  DP (DisplayPort) --> Passive HDMI/DP cable --> Anthem AVM 70 Processor --> LG TV via HDMI ARC

-  (yes the AVM 70 is HDR 10 capable (and even Dolby Vision capable) - but not G-sync capable

It is notable in https://support.microsoft.com/en-us/windows/display-requirements-for-hdr-video-in-windows-192f362e-1245-e14d-3d3f-4b3fc606b80f that DP 1.4 is required. According to my research DP 1.4 is not uni-directional with a passive cable (yes, my cables are good quality); I have gotten native HDMI --> LG TV with DP disabled to work with HDR to the LG TV so either: (HDMI display only)

-  Win 11 HDR never works with Duplicated ports or

-  Requires an active cable for DP 1.4 to HDMI conversions to support uni-directional metadata (leading theory based on https://g.co/gemini/share/aaf60ae2f112 )

-  NVIDIA RTX cards afaik tend never to have multiple HDMI ports (don't ask me why but it sucks)

Windows HDR setup screen indicates my setup today is not HDR streaming capable but is HDR capable. The NVIDIA Control Panel says turn Windows HDR on lol.

My working theory is that Windows is trying to read the HDR metadate for an HDR 10+ Flag but this is not going to happen in a DP to HDMI passive cable setup (https://g.co/gemini/share/aaf60ae2f112) . I'm too lazy to write the code for this but if anyone has the code for this I would be interested in getting that (esp. if Python) I have been unable to verify in the windows HDR spec if uni-directional DP 1.4 is required.

I am posting this mainly to help other folks and will update once I get an uni-directional DP/HDMI)I cable I will update the thread; I am also interested to understand the theory here,

I was not planning to add a bunch of Sysinfo here as i already have HDR working on a single HDMI port on this system.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-04*

Hi, dansker1234

Welcome to the Microsoft Community 

Thanks for your feedback. I read the information you provided. 

The solution and additional information you provided are very detailed and I appreciate your enthusiasm in sharing them. This information will help other users who are troubled by the same problem. 

I look forward to your continued updates to this thread. If you post subsequent updates, I will mark your answer as the answer, so that when other users search for "how to solve HDR problems with multiple monitors", your solution will be more searched for. 

Best regards 

Brian - Microsoft Community Support Specialist
