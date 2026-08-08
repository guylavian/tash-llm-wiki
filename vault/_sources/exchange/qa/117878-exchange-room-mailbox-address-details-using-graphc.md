---
title: "Exchange Room mailbox address details using GraphClient"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/117878/exchange-room-mailbox-address-details-using-graphc
question_id: 117878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange Room mailbox address details using GraphClient

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/117878/exchange-room-mailbox-address-details-using-graphc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to fetch room mailbox details from exchange using GraphClient. And I'm getting successful response from the following API    

```
var place = await graphClient.Places["roomaddress@microsoft.com"]  
    .Request()  
    .GetAsync();
```

But the below address details always shown as null in this response. What's the issue might be?     

    

Response is given below.    

    

Any help is appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-20*

(1) First you need to use the set-place Exchange Powershell cmdlet to set the values for your exchange online mailbox and update its metadata info. Related documentation - https://learn.microsoft.com/en-us/powershell/module/exchange/set-place?view=exchange-ps    

(2) Now make the Graph API call and it works for me.    

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)
