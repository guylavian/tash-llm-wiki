---
title: "Exchange 2016 Authenticated Relay"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126212/exchange-2016-authenticated-relay
question_id: 126212
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Authenticated Relay

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126212/exchange-2016-authenticated-relay (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using an old Exchange 2016 Server as an internal SMTP relay for things on-prem that don't play well with O365.  

I am trying to configure a connector so that it requires authentication but acts like an anonymous relay.  

Example, upon connecting from anywhere, you do the usual SMTP auth but at the point where you enter the from email address you can put anything.  

At the moment it requires the from address to be the one that is listed on the authenticated users AD account.  

I have already tried adding the ms-Exch-SMTP-Accept-Any-Sender permission manually to the connector but still no joy.  

Can anyone suggest anything?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-15*

Hi @David W   ,    

I agree with what Andy said.    

You could follow what Andy said above to restrict senders by creating a transport rule. Mail sent by users other than the specified sender will be deleted. Regarding the restriction by message id, according to my test, usually the message id of the mail is a string of random GUID plus the format of @yourdomain.com. If you choose to use this method for restriction, please send a test mail in advance and check the message header. Screenshot below is how to create a transport rule to restriction by message id. Please pay attention to the "-" in the format of message id.    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-14*

If you could focus on the sender or message header ( The app may generate a message ID or something similar that has the same partial data in each message),    

then you could create a transport rule and allow anonymous relay -  Dropping messages from that Citrix Farm Sever IPs unless it matches those patterns    

Example    

    

or

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-14*

You can't have an anonymous relay and require auth on the same connector. Those are two opposing concepts.
