---
title: "How does a windows 10 machine discover the ADFS RA for WHFB certificates?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/359708/how-does-a-windows-10-machine-discover-the-adfs-ra
question_id: 359708
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# How does a windows 10 machine discover the ADFS RA for WHFB certificates?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/359708/how-does-a-windows-10-machine-discover-the-adfs-ra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Query/technical details...  

Hybrid AADJ setup with certificate trust (we use RDP quite a bit).  

NDES/SCEP setup with intune for AAD joined devices. Certificates are getting pushed pushed out to ad joined devices correctly.   

On premise ADFS 4 (server 2019) setup for on premise certificate deployment of the hybrid devices. Using GPO to enable certificate trust for WHFB.  

I'm stuck on the dsregcmd /status output of adfsraisready : no. Which means the windows 10 machine is not getting it's WHFB certificate from ADFS to kick start the process.  

What I'm trying to find out is if there's any info on how the win10 machine discovers the ADFS RA settings. Have redone the config a few times and sanity checked but I keep getting the same result and just not sure what to start tracing.  

Any clues as to which direction to head would be useful.

## Answers

_No answers on this thread._
