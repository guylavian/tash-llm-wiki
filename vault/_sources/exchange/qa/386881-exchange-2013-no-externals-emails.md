---
title: "Exchange 2013 no externals emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/386881/exchange-2013-no-externals-emails
question_id: 386881
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 no externals emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/386881/exchange-2013-no-externals-emails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On premise domain controller running Windows 2012r2  

Exchange will not receive external emails  

No firewall on and AV removed  

Error from Microsoft Remote Connectivity Analyer:  

Test Details  

  

Performing Outbound SMTP Test  

The outbound SMTP test failed.  

Test Steps  

  

Attempting reverse DNS lookup for IP address xx.xxx.xxx.xx.  

The Microsoft Connectivity Analyzer successfully resolved IP address xx.xxx.xxx.xx via reverse DNS lookup.  

Additional Details  

  

Performing Real-Time Black Hole List (RBL) Test  

Your IP address wasn't found on any of the block lists selected.  

Test Steps  

  

Performing Sender ID validation.  

Sender ID validation failed.  

Test Steps  

  

Attempting to find the SPF record using a DNS TEXT record query.  

The SPF record was found.  

Additional Details  

SPF record found: "v=spf1 ip4:xxx.xx.xxx.xx/xx ip4:xxx.xx.xxx.xx/xx ip4:xxx.xx.xxx.xx/xx~all"  

  

Parsing the SPF record and evaluating mechanisms and modifiers.  

SPF record evaluation resulted in a Sender ID failure.  

Test Steps  

  

Evaluating IP address mechanism: "+ip4:xxx.xx.xxx.xx/xx"  

Additional Details  

  

Evaluating IP address mechanism: "+ip4:xxx.xx.xxx.xx/xx"  

Additional Details  

  

Evaluating IP address mechanism: "+ip4:xxx.xx.xxx.xx/xx"  

Additional Details  

  

Evaluating All mechanism: "~all"  

All mechanisms indicated a negative status.  

Additional Details  

Status: SoftFail

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-10*

Hi @James Meader  ,    

By "Exchange will not receive external emails", my understanding is that the inbound messages cannot be received. But the test results of the Microsoft Remote Connectivity Analyer is showing "The outbound SMTP test failed.", so could you help confirm what exactly is the issue you are encountering, cannot receive mails from external users or cannot send mails out?    

If incoming emails cannot be received, may I know if it's affecting all messages or only emails from some particular domains cannot be received? Any errors if you run the "Inbound SMTP Email" test?     

https://testconnectivity.microsoft.com/tests/InboundSMTP/input    

Also as suggested by Andy, please contact the external senders to see if they have received any NDR which included the clues for troubleshooting.    

Besides, you may run the get-messagetrackinglog command for a problematic message at your end and check if there's any output. This can help narrow down if the message has reached your Exchange:    

```
Get-TransportService | Get-MessageTrackingLog -MessageSubject  -Sender  -Recipients  -Start  -End  |select timestamp,EventID,Source,ConnectorID |sort-object Timestamp
```

By the way, considering that it's a public forum, I've removed the ip addesses included in your original post in order to protect the personal information. If you need to share more details in your replies in future, it's recommended to remove any personal data like domain name, email addresses, etc for privacy concerns.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
