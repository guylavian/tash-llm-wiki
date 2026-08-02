---
title: "Stop Exchange from proxying EWS between servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316904/stop-exchange-from-proxying-ews-between-servers
question_id: 316904
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Stop Exchange from proxying EWS between servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316904/stop-exchange-from-proxying-ews-between-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an application that connects to Exchange through EWS using Application Impersonation to access multiple mailboxes. This was working fine with Exchange 2016.  I have added an Exchange 2019 server to the environment, and moved most mailboxes over. The application is now pointed to the 2019 server, and having some issues.  Looking through the EWS and HTTPProxy logs,  I see that the 2019 server is proxying some of the EWS traffic to the 2016 server, and that's when the application fails. I see "ErrorNoRespondingCASInDestinationSite" and "Exchange Web Services are not currently available for this request because none of the Client Access Servers in the destination site could process the request" in the EWS logs on the 2016 server.  

Does anyone know why  Exchange 2016 would be responding this way?  

Is there a way to stop the Exchange 2019 server from proxying this traffic to the Exchange 2016 server?  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

Are you setting the X-AnchorMailbox header in your application (to the target mailbox) this is what generally has the most bearing of how EWS request will be routed
