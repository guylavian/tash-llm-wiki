---
title: "Accepted domains in Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208868/accepted-domains-in-exchange-server
question_id: 208868
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Accepted domains in Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208868/accepted-domains-in-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I've some confusion to understand concept of accepted domain in Exchange server because of conflicting statements mentioned on Microsoft article.    

https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains?view=exchserver-2019    

According to the above article link it says Accepted domains are the SMTP name spaces (also known as address spaces) that you configure in an Exchange organization to receive email messages.    

However, in below article link it says An accepted domain is any SMTP namespace for which a Microsoft Exchange Server 2013 organization sends or receives email.    

https://learn.microsoft.com/en-us/exchange/accepted-domains-exchange-2013-help    

So as you can see that one article says Accepted domains are responsible for only receiving email messages but another article says Accepted domains are responsible for sending or receiving email messages both.    

Please help me to get clarity and understand  the correct concept as well as correct functionality of Accepted domains with examples and authentic reference article. Please explain why there is conflict in both articles.    

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-24*

@G-ONE      

Accepted domains are the SMTP name spaces (also known as address spaces) that you configure in an Exchange organization to receive email messages.     

In fact, it doesn't said "only used to receive email".    

The mainly function of "Accepted Domains" is to set the domain as the authoritative domain of your organization. In this way, your organization will receive email which sent to those domain after creating MX record(Your domain is the default Accepted Domain). You can also using the "Accepted Domains" to relay email for other mail server.    

Compared with the receiving function, the sending mail function is a small function for "Accepted Domains": after creating Accepted Domains, you could apply this new domain on your mailbox, then change this new email address as primary email address, in this way, you will could use this new email address to send email.    

Therefore, it is difficult to say whether this one is accurate, after all, different people have different ideas. But, all docs will be checked before posted on learn.microsoft.com.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-23*

The accepted domain is assumed to be one that you receive and send for, yes.  You would not have an accepted domain in Exchange and not also potentially send as that as well. Its not required of course, but generally that is why people set an accepted domain as its a domain your org is authoritative for ( sending and receiving) .   

In other words, you own it  :)  

You wouldn't send as a domain that you didn't also receive messages for unless you were authorized to spoof it.   

There is no conflict in those articles. Just different phrasing.  Those articles are authentic already :)
