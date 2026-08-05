---
title: "Hosted Exchange not using second Send Connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309693/hosted-exchange-not-using-second-send-connector
question_id: 309693
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hosted Exchange not using second Send Connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309693/hosted-exchange-not-using-second-send-connector (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,   

For some reason my Hosted Exchange servers are not using the second Send Connector I added.   

Default Send Connector   

Enabled   

Route through smart host: mx01.ourcompany.com   

Authentication: None Scoping: * (Cost 10)   

Source Server: EX01 + EX02   

Customer Send Connector   

Enabled   

Route through smart host: mx01.customer.com   

Authentication: None Scoping: customer.com (Cost 1)   

Source Server: EX01 + EX02   

Both smarthost systems on the other end are identical, except IP. Port 25 is open and tested.   

Everything is set up so it should work but for some reason it only pick the Default Send Connector.   

Hopefully someone can help me out.   

Kind regards.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-12*

Hi @Bodis HS   ,    

If the settings are all correct, I think you could do a test:    

-  Changing the Customer Send Connector to your company's.     

-  Changing the Scoping of the Customer to *.    

Also you can run this command and compare the difference of them:    

```
Get-SendConnector -Identity "ConnectorName" | FL
```

And you could recreate two Send Connectors to test.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
