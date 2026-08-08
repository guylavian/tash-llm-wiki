---
title: "Exchange 2016 ndr taking too long to return"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185035/exchange-2016-ndr-taking-too-long-to-return
question_id: 185035
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange 2016 ndr taking too long to return

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185035/exchange-2016-ndr-taking-too-long-to-return (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sirs,  

I have an exchange 2016 setup only for internal use and there's no send connector configured.  

on the outlook client side, I have setup 2 mail accounts one with exchange and to other with an external POP and SMTP that we use for sending emails outside the domain.  

the problem I'm facing is that when the users send an email to the outside world using the exchange account by mistake.  

the NDR reply from the exchange server takes about 2 days to get back and the users assume that their email was sent. to find out after 2 days that they sent from the wrong account.  

I tried to modify the parameters in the edgeTransport.exe.config file and the parameters in ECA with no luck.  

is there's a way to make exchange NDR reply immediately? or is there's a way to deny users from sending email from exchange on outlook?  

thank you so much for your support

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-12-04*

@Elias Chamoun       

Agree with AndyDavid, you also can use message tracking log to see the mail flow for that message:    

```
Get-TransportService|Get-MessageTrackingLog -MessageSubject  -Sender  -Recipients  |select timestamp,EventID,Source,ConnectorID|sort-object Timestamp
```

You can try to create the mail flow rule as AndyDavid mentioned to block messages sent to the external. It works well in my environment:    

    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
