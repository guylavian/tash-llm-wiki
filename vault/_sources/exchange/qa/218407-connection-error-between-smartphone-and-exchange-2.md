---
title: "Connection error between smartphone and exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218407/connection-error-between-smartphone-and-exchange-2
question_id: 218407
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Connection error between smartphone and exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218407/connection-error-between-smartphone-and-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After migrating from the exchange server 2016 to the new exchange 2019, it was never possible to connect mobile devices to the new exchange server. the error is as follows (very ambiguous):  

An ActiveSync session is being attempted with the server.  

Errors were encountered while testing the Exchange ActiveSync session.  

Test Steps  

Attempting to send the OPTIONS command to the server.  

Testing of the OPTIONS command failed. For more information, see Additional Details.  

Additional Details  

An HTTP 500 response was returned from Unknown.  

HTTP Response Headers:  

request-id: 01104fdf-f2a9-421a-b686-d0322cd65b26  

I have tried several solutions in this and other forums but I have not been successful. Can you help me?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-01-13*

@Kai Yao      

Hi,    

Thank you for your help.    

Finally, after several researches, I came to the conclusion that solving the problem involves creating new databases and moving accounts.    

When updating the exchange 2019 (CU8), in the middle of the process there was an error that interrupted the update, causing the Exchange to stop working.    

It was only after several attempts that I was able to proceed with the update and complete it.    

Perhaps for that reason there was a problem with the access permissions to the databases. Because if I create new databases and move the mail accounts, the problem goes away.    

The connectivity between smartphones and the server is perfect (the error 500) is no longer in Microsoft Connectivity Analyzer (testconnectivity.microsoft.com).    

Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-01-05*

@Paulo Ferreira    

Hi,

Would you please tell us what solutions have you tried so far?

Sorry I need to ask the following questions in order to get some more information:  

1.Have you decommissioned the Exchange 2016 server and configured the DNS records to point to the Exchange 2019 server?  

2.Do you have connecting problems with OWA or Outlook for windows clients?  

3.What error message do you get on mobile devices when trying to connect to the server?

And here are some suggestions:  

1.Have you tried connecting internally with the mobile devices?  

2.If you create a new mailbox for test on the Exchange 2019 server, would it still fail the activesync test?  

If so, was the error message same as "An HTTP 500 response was returned from Unknown"?  

3.Check if "Basic Authentication" is enabled on the activesync virtual directory.  

  

4.Recreate the activesync virtual directory via the following commands:

```
Remove-ActiveSyncVirtualDirectory -Identity "Microsoft-Server-ActiveSync (Default Web Site)"  
New-ActiveSyncVirtualDirectory -WebSiteName "Default Web Site" -ExternalUrl https://www.contoso.com/Microsoft-Server-ActiveSync -InternalUrl https://www.contoso.com/Microsoft-Server-ActiveSync  

Remove-ActiveSyncVirtualDirectory -Identity “Microsoft-Server-ActiveSync (Exchange Back End)”  
New-ActiveSyncVirtualDirectory -WebSiteName “Exchange Back End”
```

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-05*

@Kai Yao      

Hi.    

In answers to your questions:    

1 . Yes.    

2 . No. I have no connectivity issues between Outlook and Exchange. Outlook on the web, also works normally.    

3 . Error on moblie devices: "Account information could not be verified"    

In reply to your suggestions:    

1 . I tried to connect internally and the error is the same.    

2 . I already created a new mailbox and the error is the same.    

3 . "Basic Authentication" is enabled    

What I've also tried to do:    

In some forums they report that it may be a problem with account permissions, however I have already tried to put "Inherited Permissions" in two accounts and the problem remained.    

And now my question:    

If I recreate these virtual directories (ActiveSyncVirtualDirectory), will there be a lack of connection between Outlook clients and Exchange? In my company, there are over a hundred email accounts associated with employees, who depend on this service to work.    

Thank you.
