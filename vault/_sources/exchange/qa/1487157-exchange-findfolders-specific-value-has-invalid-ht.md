---
title: "exchange FindFolders: specific value has invalid HTTP Header Characters"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1487157/exchange-findfolders-specific-value-has-invalid-ht
question_id: 1487157
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "office-exchange-other-l1"]
---
# exchange FindFolders: specific value has invalid HTTP Header Characters

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1487157/exchange-findfolders-specific-value-has-invalid-ht (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  I recently started hitting a bug, and any suggestions on how to work around this would be greatly appreciated.

There were no changes to the code in the past 12 months+, and suddenly the application is breaking at this line:

 

var ewsClient = new ExchangeService();  

ewsClient.Url = new Uri("https://outlook.office365.com/EWS/Exchange.asmx");  

ewsClient.Credentials = new OAuthCredentials(authResult.AccessToken);  

ewsClient.ImpersonatedUserId =  

new ImpersonatedUserId(ConnectingIdType.SmtpAddress, mailbox);  

//Include x-anchormailbox header  

ewsClient.HttpHeaders.Add("X-AnchorMailbox", mailbox);

 

var folders = ewsClient.FindFolders(WellKnownFolderName.Inbox, new FolderView(10));

 

This last line throws an error:

Specified value has invalid HTTP Header characters.  

Parameter name: name

Thank you!

## Answers

_No answers on this thread._
