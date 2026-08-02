---
title: "Multiple ECP & OWA link for different mail domains in 1 exchange server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1624472/multiple-ecp-owa-link-for-different-mail-domains-i
question_id: 1624472
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# Multiple ECP & OWA link for different mail domains in 1 exchange server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1624472/multiple-ecp-owa-link-for-different-mail-domains-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys,

Recently i setup a Microsoft Exchange 2019 in Windows server 2022.

Now I configured 2 accepted domains in the exchange 2019 (which the mails are working fine inbound and outbound).  

abc.com - Ex. mail user: ******@abc.com

xyz.com - Ex. mail user: ******@xyz.com

the issue I am facing is, when i tried to go to my browser and type mail.abc.com/owa - and i tried to log in as ******@xyz.com its allowing it to log in.

Is there any possibility that I can create separate ECP & OWA external links for both different mail domains? or is there any option to block xyz.com mail to disallow them to signed in on  mail.abc.com/owa and only allows them to sign in on mail.xyz.com/owa which is their own domain?  

I am using only 1 exchange server.  

DNS RECORDS - for 1st domain (abc.com)

mail.abc.com.	14400 - A - "Public Ip"

autoconfig.abc.com. 14400 - A - "Public Ip"

autodiscover.abc.com. 14400 - CNAME - mail.abc.com

abc.com. 14400 - MX - Priority: 0 - Destination: mail.abc.com

abc.com. 14400 - TXT - v=spf1 ip4:"Public Ip" -all

DNS RECORDS - for 2nd domain (xyz.com)

mail.xyz.com. 14400 - CNAME - mail.abc.com

autodiscover.xyz.com. 14400 - CNAME - mail.abc.com

xyz.com. 14400 - MX - Priority: 0 - Destination: mail.abc.com

xyz.com. 14400 - TXT - v=spf1 mx ip4:"Public Ip" -all  

I hope you can enlighten me on this.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-03-20*

Hi @GDT,

You can refer to this link to create additional OWA/EAC virtual directories:

https://techcommunity.microsoft.com/t5/exchange-team-blog/configuring-multiple-owa-ecp-virtual-directories-on-the-exchange/ba-p/611217

But to me it is also not possible to prevent users from signing into another domain.

You may probably need to setup some rules to restrict ip addresses in IIS.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
