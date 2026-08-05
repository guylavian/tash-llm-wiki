---
title: "Exchange autodiscover redirect to O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147877/exchange-autodiscover-redirect-to-o365
question_id: 147877
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange autodiscover redirect to O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147877/exchange-autodiscover-redirect-to-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have on-premise Exchange server in our site and don't have O365 mailboxes.     

Recently, some of our mailboxes are trying to connect to O365 which cause mailboxes disconnected and unable to create new mailbox profile on client. Meanwhile, OWA can work well.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-11-03*

@RICK-0238     

What's the detailed version of your Outlook? You can check from File > Office Account > About Outlook.    

For Outlook 2016 version 16.0.6741.2017 and later versions, Outlook will attempt to retrieve Autodiscover from O365 as priority. As AshokM-8240 mentioned, you can try to use the ExcludeExplicitO365Endpoint to skip this step:    

-  Go to Register Editor and find the following location:    

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\AutoDiscover    

-  Create a DWORD value for ExcludeExplicitO365Endpoint and change the value to "1":    

    

You can check the article provided by AshokM-8240 for more details.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
