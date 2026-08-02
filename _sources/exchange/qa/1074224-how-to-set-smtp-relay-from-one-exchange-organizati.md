---
title: "How to set smtp relay from one exchange organization to another organization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074224/how-to-set-smtp-relay-from-one-exchange-organizati
question_id: 1074224
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# How to set smtp relay from one exchange organization to another organization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074224/how-to-set-smtp-relay-from-one-exchange-organizati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have one company A and now it is splitting into two companies A and B.    

We want to set up a relay so that when an email come from application to company B on-premise for the users who are still in Company A (mailbox not migrated to Company B) should go from B to A through relay connector using a particular DNS Namespace of company A.    

We have added company B exchange servers IPs to DNS Namespace(SMTP server) of Company B. We are using exchange 2019.    

how we can achieve this. Do we need to add Company A domain as accepted domain or we can need to connect Transport rule. how mail will flow from company B to company A using this particular DNS Namespace(SMTP server) of Company B.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-04*

@neelam Kumari      

-  Do you mean that mailbox hosted on company A (such as ******@domainA.com)?     

-  Whether there exists mailbox for this user like ******@domainB.com on company B?    

Scenario one: If there doesn't exist ******@domainB.com on company B (which means **the original recipient is ****@domainA.com), just Domain A MX record points to Domain B IP Address. About this one, why not point MX to Domain A Ip address directly?    

You can also use the Exchange external relay function to relay emails from company B to company A: Add domain A as external domain on company B, then create send connector to relay emails to domain A.    

Scenario two: If there exist ******@domainB.com on company B (Which means **the original recipient is ****@domainB.com). You could take step below to redirect emails from ******@domainB.com to ******@domainA.com    

-  Add ******@domainA.com as mail contact on company B.    

-  Create a transport rule on company B like: If the message is sent to '@domainB.com', Redirect the message to '@domainA.com'    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-14*

yes, we created the connectors but while sending mail from telnet it shows "cannot relay email from non- accepted domain"

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-07*

is it Enough if we make below connectors to relay mail from App server to company B via Company A:    

-  One receive connector on Company A and add APP server ip to the connector to receive mail from App to company A    

-  One send connector on Company A and add Company B relay server IP address to send that mail (Came from app) to relay mail from Company A to company B    

-  One receive connector on Company B and add Company A server IP address to receive mail from company A to Company B

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-07*

Here scenario is like we want to relay the email from app server to company A exchange server and then company A exchange server should relay that mail to Company B exchange server (to company B user mailboxes on Company B exchange server)
