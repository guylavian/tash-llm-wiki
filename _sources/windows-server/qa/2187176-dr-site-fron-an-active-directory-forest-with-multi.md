---
title: "DR site fron an Active Directory Forest with multiple subdomains"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187176/dr-site-fron-an-active-directory-forest-with-multi
question_id: 2187176
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-dire"]
---
# DR site fron an Active Directory Forest with multiple subdomains

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187176/dr-site-fron-an-active-directory-forest-with-multi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our Active Directory infrastructure is a forest with 1 parent domain and 3 subdomains.

The there are 3 subdomains, one for the Production servers, one for pre-production and one for testing.

As an example

SERVICE.local -> hosts all infrastrucutre servers

PROD.service.local -> hosts production servers

PREPROD.service.local -> hosts all pre-production servers

TEST.service.local -> hosts all testing servers

Our idea is to create a new AD site, and place 2 new DCs on this site, one for the SERVICE.local domain, and one for the PROD.service.local domain. We don't need to protect the pre-production and testing servers.

I have already posted a related question which has been answered in this thread: https://answers.microsoft.com/en-us/windowserver/forum/all/active-directory-dr-site-with-forest-with-multiple/97e78049-a50b-42c5-9b6e-8257a0aa35d5

Now my concern is about the failback.

In a DR scenario, only the SERVICE and PROD will be online at the DR site, while the PREPROD and TEST domains will be unavailable.

If the DR situation last for long time, what will happen to the PREPROD  and TEST domains when the main site is brought back online?

Are there any potential issues in such a situation?

Regards

Gabriele

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-29*

Thank you for the reply.

I was aware of the 180 days limit in AD replication.

Apart from that, I assume that, if the downtime lasts less then 180 days, there will be no issues, then.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-28*

Hello D'Andrea Gabriele,  

Thank you for posing in Q&A forum.  

If the DR situation last for long time, what will happen to the PREPROD and TEST domains when the main site is brought back online?

A1: If the last time is shorter than 180 days, there should be no issue.  

If the last time is longer than 180 days, there will be AD replication issue in AD forest, and for such AD replication, we can fix it.  

For more information about the AD replication I mentioned and the possible resolution, please read links below.

Active Directory Replication Error 8606: Insufficient attributes were given to create an object  

Troubleshoot replication error 8606 - Windows Server | Microsoft Learn

Remove Lingering Objects that cause AD Replication error 8606 and friends  

Remove Lingering Objects that cause AD Replication error 8606 and friends - Microsoft Community Hub

Active Directory replication Event ID 1388 or 1988: A lingering object is detected  

Active Directory replication Event ID 1388 or 1988 - A lingering object is detected - Windows Server | Microsoft Learn  

Lingering Object Liquidator (LoL)  

Download Lingering Object Liquidator (LoL) from Official Microsoft Download Center

 Active Directory: Removing Lingering Objects | Microsoft Learn

Are there any potential issues in such a situation?

A2: please see A1.

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
