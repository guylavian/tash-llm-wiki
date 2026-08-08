---
title: "Exchange 2019 Send Connector Issues After Installing 2nd Mailbox Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336147/exchange-2019-send-connector-issues-after-installi
question_id: 336147
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 Send Connector Issues After Installing 2nd Mailbox Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336147/exchange-2019-send-connector-issues-after-installi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently installed a second Exchange 2019 Mailbox Server. Using EAC, I exported the  Go Daddy Ceritificate from the 1st Exchange Mailbox Server and Imported to the 2nd Exchange Mailbox server.  Again using EAC, I added the services IMAP, POP, IIS and SMTP to the certificate and received a warning regarding overwriting a thumbprint (I think). I clicked on cancel but too late as the certificate included all 4 services.   

Within about 5 minutes I noticed the smart connector queue on my Edge Transport server (which now includes the new server) was not routing emails to the mailbox servers. I immediately removed the Go Daddy Certificate from the second Exchange server and re-imported it but this time when adding services I left off the SMTP service.   

This did not resolve the issue with my smart connector queue.   

I have to shutdown the second exchange server in order for the Smart Connector Queue to route email to the Mailbox servers.  

I think I need to include the SMTP service on the  certificate for the second exchange server and then verify the certificate has the correct thumbprint on the second exchange server.  

Does the Go Daddy certificate on the second Exchange Server require the SMTP service?   

Is there something else I am missing in configuring the Send Connectors?   

Please advise.  

Thank you,

## Answers

_No answers on this thread._
