---
title: "Error sending and receiving emails in Exchange 2010 and 2016 coexistence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1442152/error-sending-and-receiving-emails-in-exchange-201
question_id: 1442152
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error sending and receiving emails in Exchange 2010 and 2016 coexistence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1442152/error-sending-and-receiving-emails-in-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

These are the versions of the exchange servers:

Exchange 2016 CU23  - 15.1 Build (2507.6)

Exchange 2010  SP3    - 14.3.0513 Build(123.4)

The problem is sending and receiving emails in Exchange 2016.

Creating the send and receive connector in Ex2016:

Send
Receive
Message

Ex2010
Internet
OK

Internet
Ex2010
OK

Ex2016
Internet
4.4.7 Queue Expired

Internet
Ex2016
4.4.7 Queue Expired

Ex2010
Ex2016
4.4.7 Queue Expired

Ex2016
Ex2010
OK

Without connector to send and by default receive in Ex2016:

Send
Receive
message

Ex2010
Internet
OK

Internet
Ex2010
OK

Ex2016
Internet
OK

Internet
Ex2016
4.4.7 Queue Expired

Ex2010
Ex2016
4.4.7 Queue Expired

Ex2016
Ex2010
OK

Perform tests with Microsoft Remote Connectivity Analyzer. The test mail arrives and passes the tests.Also with Chektls and without problems

Reading on the internet, there are more problems in Ex2010, I was thinking if this problem is corrected by recreating the connectors as done in Exchange 2003 - 2010

Reviewing the RND message in a little detail, I realize that it only checks the message in Ex2010 and does not ask in Ex2016 if the mailbox exists. I have created test mailboxes on both servers and I can access them in OWA, that is where I have these problems sending and receiving emails

Ex2010   in 10   MX    Ex2010.contoso.com

Ex2016   in 20   MX    Ex2016.contoso.com

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-29*

It sounds like the Mail scanner is not configured to allow the 2016 server to send through it.

Does sending through the 2016 server generate an NDR? If so, what is the exact error?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-28*

Hello Luis Alberto,

Welcome to our forum!

Did you see the error code “4.4.7 Queue Expired” in the queue viewer? If so, is there any more information included which might be helpful for further investigation? Could you please provide detailed NDR information for further troubleshooting? And have you made any changes to the default receive connectors on Exchange 2016?

In addition, it is recommended that you use the command Get-MessageTrackingLog  to view message tracking log to see if there is any information that can help pinpoint the problem. 

```
Get-TransportService|Get-MessageTrackingLog -MessageSubject  -Sender  -Recipients  |ft timestamp,EventID,ClientHostname,ServerHostname,Source,ConnectorID -autosize
```

Besides, noted that you are now having two MX records pointed to both Exchange 2010 and Exchange 2016, could you try leaving only one MX record point to Exchange 2016 and check the result?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
