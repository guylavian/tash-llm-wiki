---
title: "Exchange Classic Hybrid Network ports and protocols."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/101080/exchange-classic-hybrid-network-ports-and-protocol
question_id: 101080
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Classic Hybrid Network ports and protocols.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/101080/exchange-classic-hybrid-network-ports-and-protocol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been looking at the networking requirements for Exchange classic Hybrid to Office 365. It's not clear to me:  

-  What each port (443,80,25,587) is required for ?  

Specifically what is being sent out of our organization over port 80 for example? We presented the documentation from Microsoft to our security teams and they laughed at the lack of detail! :|   

The documentation is not explicit on the network flows.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-09-21*

You wouldnt open port 80  :)     

Where do you see that requirement for Hybrid?    

https://learn.microsoft.com/en-us/exchange/hybrid-deployment-prerequisites    

All you need is 25 and 443.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-22*

An update guys and thanks all who have responded:   

So a Microsoft Field Engineer came back to me and indicated   

"TCP port  80 egress is needed for auto-discovery from on premise Exchange to EOP.  Regardless, when the client (outlook) talks to on-premise exchange and needs to discover a mailbox/calendar the Exchange server will use port 80 for auto-discovery."  

I asked was this port 80 from client to EOL directly and he indicated that it was actually the Exchange Backend connection to EOL that needs this. I'm confused as I can't find anything to back this up.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-22*

Hi @DarraghOShaughnessy-6524 , between Office 365 and your on-prem Exchange server, you need to have port 443 and port 25 available.     

You can have port 25 go directly to the internal Exchange server or you can go through an Edge server which helps you limit the inbound traffic to only the Office 365 IP address ranges list in this official document: Office 365 URLs and IP address ranges    

As for port 443, your system needs to be reverse proxied to Office 365 so that the hybrid connection can be fully established. Office 365 needs a web services connection to your internal systems so that it can create move requests.     

All outbound communication is on either port 25 or port 443. Port 80 is not used between your on-prem Exchange server and Office 365.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
