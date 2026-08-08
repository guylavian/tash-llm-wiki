---
title: "Exchange 2016 geolocation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/281854/exchange-2016-geolocation
question_id: 281854
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 geolocation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/281854/exchange-2016-geolocation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to see the geolocation of where users are signing on from? It would be helpful alert to see if an account has been compromised. A suspicious user would probably be logging on from somewhere outside of our operating area. This is for premise/server based exchange not office365 or other cloud exchange solutions.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-22*

Thank you for the answers. I wish it let me accept both answers but it does not. Thanks again for the help and pointers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-22*

Hi @will smith   ,  

I agree with what Andy said.  

According to my research, we could know the IP address of the client login through the IIS log, but the on-premiese Exchange itself cannot be set to check for remote login and issue a warning.

In addition, I found two ways to restrict mailbox login, if it meets your needs, you can try to set:  

1.You can restrict specific mailboxes to only log in on specified computers. But it should be noted that, according to my test, if this setting is made, the specific mailbox will not be able to log in through OWA, and can only be logged in to the Outlook client on the designated computer. Please refer to the settings in the screenshot below to set up in ADUC.  

2.We can use the IP Address and Domain Restrictions function in IIS to restrict the mailbox to only log in to a specific IP or a specified IP range.  

  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
