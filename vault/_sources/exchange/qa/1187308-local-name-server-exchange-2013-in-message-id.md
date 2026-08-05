---
title: "Local name server Exchange 2013 in Message-ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187308/local-name-server-exchange-2013-in-message-id
question_id: 1187308
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Local name server Exchange 2013 in Message-ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187308/local-name-server-exchange-2013-in-message-id (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

When sending emails through an Exchange 2016 server, a MessageID is generated that contains the identifier and name of the accepted email domain (for example, ******@domain1.com) 

But when sending emails through the Exchange 2013 server, a MessageID is generated that contains the identifier and the local name of the mail server (for example, 9e7882613086427d90b9f2d6f2ec8ba1@ex01.domain2.local)

I need to hide local domain name in MessageID 

 On the Internet, it is recommended for the send connector, through which messages go to the Internet to external recipients, to register the name of the mail domain as the FQDN name, and then this FQDN name will supposedly be substituted in the MessageID instead of the local name of the Exchange server. 

https://learn.microsoft.com/en-us/answers/questions/123815/message-id-header

https://www.alitajran.com/remove-message-header-in-exchange-server/

I did this on an Exchange 2013 server but it didn't work. 

MessageID has not changed and still contains the local server name.

Maybe you need to restart some services or the entire server?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-08*

Hi @Павел Павел ,

 

Based on my understanding, the linked article you shared above is just intended to remove the internal domain or ip in other message headers, while the Message-ID is not changed. As we can see from the screenshots in the article, the message-id remains the same all the time:  

By searching, for messages created in Exchange, the value of MessageID is constant for the lifetime of the message, it cannot be modified or hidden. 

Related discussion： https://community.spiceworks.com/topic/1947958-exchange-2013-remove-internal-domain-from-message-id

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
