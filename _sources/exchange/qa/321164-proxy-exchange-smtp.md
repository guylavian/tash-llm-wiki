---
title: "Proxy Exchange SMTP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321164/proxy-exchange-smtp
question_id: 321164
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Proxy Exchange SMTP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321164/proxy-exchange-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, I am beginning an Exchange migration and I am looking over design options.  I would like to establish some kind of proxy server in the DMZ to handle the submission of email over TCP:587 by Exchange users.  I've looked over IIS ARR and WAP a bit, but these seem focused on HTTP based services like EWS, OWA, OAB, ActiveSync, etc..  

It appears that the non-domain joined Edge Transport server may be an option for this, but it appears to handle all mail flow and offer anti-SPAM features.  We use a Barracuda appliance for this and I am not looking to replace that.  Can the Edge Transport server only proxy inbound TCP:587 SMTP submission from authenticated Exchange users?  

Regards,  

Adam Tyler

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-25*

@Lucas Liu-MSFT       

anonymous userDavid     

So I took this about as far as I can and I suspect that you both are correct, it isn't possible to accept authenticated email over TCP:587 with an Edg Transport server.    

I did deploy one in the lab and configured edge sync successfully.  Test-EdgeSynchronization completes and states the SyncStatus as "Normal".  As expected it created the necessary TCP:25 SMTP connectors between itself and the back end Exchange MBX server.  What I was curious to know is what happens if I manually create a new receive connector directly on the Edge Transport server designed to use authentication for ExchangeUsers.  So I did that and was able to make TCP:587 connections using OpenSSL from the CLI to interact with the SMTP service.    

First problem I ran into was authentication, I couldn't seem to use a Domain User account like I would expect.  I was hoping the EdgeSync magic of pulling in the AD user database from the back end MBX server would allow this still (AD LDS).  I did take this a step farther and created a local user account in the local user database of the Non-domain joined EdgeSync server.  Low and behold, I was actually able to authenticate during the SMTP process!  Local accounts isn't ideal, but I was making progress.  When I actually tried to submit an email for relay however I got an error stating that the from address was invalid for the user I was authenticated with.    

So, hmm..  Sort of at a stopping point with this implementation.  It does look like I am going to need to find a different mechanism for forwarding TCP:587 traffic directly to an MBX server.  Perhaps some kind of a reverse proxy device from a third party in the DMZ.    

Regards,    

Adam Tyler

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-19*

Hi @AdamTyler-3751   ,    

Agree with what Andy said.    

If we installed the Edge tranpsort servers, all mail coming from the Internet or going to the Internet flows through the Edge transport server. We can't restrict it to only process mail on a specific port.    

For more information: Mail flow and the transport pipeline    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
