---
title: "Direct connection to ECP and OWA to mailbox Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327604/direct-connection-to-ecp-and-owa-to-mailbox-exchan
question_id: 327604
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Direct connection to ECP and OWA to mailbox Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327604/direct-connection-to-ecp-and-owa-to-mailbox-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day!  

Installed Exchange 2013 server with only mailbox role.  

Connecting to OWA and ECP to this server directly does not work:  

https://mailboxserver/owa and https://mailboxserver/ecp.  

I normally connect to ECP and OWA through the CAS server.  

Question: on a server with only the mailbox role, should a direct connection to ECP and OWA via the web work?   

Or from CAS only?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-24*

Hi, @Pavel       

By default, the request to access ECP/OWA is proxied through the CAS server to the mailbox server.    

As described in this document: Client Access server    

The Client Access server in Exchange 2013 functions much like a front door, admitting all client requests and routing them to the correct active Mailbox database.    

In addition, it is supported and recommended to install the Mailbox role and the CAS role on the same server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
