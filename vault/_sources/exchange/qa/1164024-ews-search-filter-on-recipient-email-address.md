---
title: "EWS search filter on recipient email address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164024/ews-search-filter-on-recipient-email-address
question_id: 1164024
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# EWS search filter on recipient email address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164024/ews-search-filter-on-recipient-email-address (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the phase of implementing the EWS online library to read the inbox items. We need your assistance in below items.

1/ We have a requirement where we have to filter out the to email address since last 5 days. We have tried to implement the searchfilter on DisplayTo property.

But that property is not working well.

e.g 

Case1: In some emails in the inbox, the To: contains display name 1668 but the email address is ******@eat2eat.com. 

In this case, if we pass 1668 then we get the items BUT if we filter by actual email address ******@eat2eat.com on 'DisplayTo' property not working.

Case2: In to emails have the email alias e.g. 'THE RITZ-CARLTON, MILLENIA SINGAPORE' and the email address of this alias is ******@eat2eat.com

In this case, filter on 'DisplayTo' property for email ******@eat2eat.com is not working. But if we add the filter 'THE RITZ-CARLTON, MILLENIA SINGAPORE'

on 'DisplayTo' property then we get the result set.

So could you kindly help us,

a) How we can filter the actual email address and retrieve the result set?

b) How we can add another filter to add date since last 5 days?

Kindly advise.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-26*

The DisplayTo property generally won't contain the EmailAddress it only contains the display name portion of the email address.  In some circumstances eg external sender where they didn't have the displayName it may contain the email address but in a Exchange org's where the name of the recipient can always be resolved in the GAL generally you wouldn't expect the email address to be part of the DisplayTo property. I would suggest a Mapi editor like OutlookSpy or MFCMapi would be helpful as that allways you to view the property values on items.

An AQL/KQL query is probably a better option [https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-perform-an-aqs-search-by-using-ews-in-exchange eg 

```
to:"******@eat2eat.com" AND received:>01/22/2023
```
