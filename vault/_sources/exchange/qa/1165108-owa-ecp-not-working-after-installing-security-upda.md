---
title: "OWA, ECP not working after installing security update for CU23 on Exch 2013 DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165108/owa-ecp-not-working-after-installing-security-upda
question_id: 1165108
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# OWA, ECP not working after installing security update for CU23 on Exch 2013 DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165108/owa-ecp-not-working-after-installing-security-upda (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Getting "something went wrong" on ecp, owa after installing security update for CU23 on 2 node Exch 2013 DAG.

Any suggestions?

Thanks.

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-01-29*

Hi

the remediation steps listed here may help:

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-stops-working-after-update

Hope this helps,

Thanks

Michael Durkan

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-06*

Hi @create share  ,

After removing the updates, owa/ecp started working. KB5019076 is not installed on the servers. I was installing Exchange Server 2013 CU23 SU19 (KB5022188) when this problem occurred. Both of these updates are not available under windows updates inside the server. Is it normal?

Yes, this could happen based on my experience. And regarding these two updates you mentioned, SUs are cumulative, so you only need to install the latest one (KB5022188), which is exactly the update you were trying to install. 

How can we properly install updates on Exchange 2013 2 Node DAG on Windows 2012 Std without corrupting owa/ecp? Should the updates be not installed if they are not available under windows updates inside the servers?

Generally, you can follow the steps below to install updates in DAG:

-  Put a DAG member in maintenance mode.

-  Install the update. 

-  Take the DAG member out of maintenance mode and put it back into production.

-  Repeat the above steps on other DAG members.

If something does not work properly after updates, see Repair failed installations of Exchange Cumulative and Security updates.

As regards to your concern about the necessity to install these SUs, it's always officially recommended to install all the updates to protect your Exchange environment.  

And you can use the Exchange Server Health Checker script to check if any of your Exchange Servers are behind on updates (CUs, SUs, or manual actions). More details, hopefully you can find the article below helpful:

Released: January 2023 Exchange Server Security Updates

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-01-30*

If its a Security Update, then yes its absolutely recommended to install it. Especially Exchange updates given the amount of vulnerabilities it has and the issues it could cause your organization if exploited.

I'm assuming its KB5019076 that you are installing, and that's important as it fixes vulnerabilities around Elevation of Privilege and Information Disclosure.

You'd be better off trying to fix the ECP/OWA issues after installing the update.
