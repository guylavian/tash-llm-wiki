---
title: "ADFS 3.0 2012 R2 - I need help identifying my farm federation servers and if safe to remove old ones."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/43319/adfs-3-0-2012-r2-i-need-help-identifying-my-farm-f
question_id: 43319
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 3.0 2012 R2 - I need help identifying my farm federation servers and if safe to remove old ones.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/43319/adfs-3-0-2012-r2-i-need-help-identifying-my-farm-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I inherited our ADFS infrastructure with little documentation, and I am trying to identify how everything i working together. I have a document of the layout, so I know server named and purposes, but I immediately became confused, as the layout shows a Productionfarm behind a load balancer and a DR farm behind a DR load balancers, two totally seperate farms it appears, but when I log into one of the DR federation servers, they show they are getting all their data from the Primary Federation Server on the productionfarm.  

So I set about googling how to see the farm members on the Primary ADFS Server, and I cannot find ANYTHING to look that up, and to see what all federation servers are in the production farm. I found a powershell command but I think it started in Serevr 2016,so that was no good.  

Can anyone tell me how I can see what all servers are in the farm on the primary federation server, and also if removing a server from the farm is as simple as just removing the ADFS component in Server Manager, on the secondary server?  

Thank You so much, I am not ADFS trained, and am only taking it because I have to. I am trying to read and understand, but I am still quite confused about how the trusts and all that work. So please assume I am a total newb in your reply, especially if partof the decomission is to do cert work or share work.  

Thank You so much for any help!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-06*

Have a look here: AD Fun Services – List all the members of an ADFS farm
