---
title: "Moving Exchange 2010 domain into our 0365 Tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1001175/moving-exchange-2010-domain-into-our-0365-tenant
question_id: 1001175
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Moving Exchange 2010 domain into our 0365 Tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1001175/moving-exchange-2010-domain-into-our-0365-tenant (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As part of acquiring Exchange server 2010 domain, we needs to add the domain(Exchange 2010 domain) to the 365 domain (Tenant) so email redirections are filtered via o365 tenant.    

How this can be done?    

Adding domain to 365 tenant is going to stop mailflow?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

Verify your domain in Office 365. It requires you to add a TXT record in your DNS zone.    

Now for the post-migration cleanup, switch your domain’s MX record to point to Office 365. After the TTL passes, emails will be routed directly to Office 365. You can delete your migration batch and decommission the on-premises servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-12*

Hi @Saurabh Singh   ,

Step by step guidance: Add a domain to Microsoft 365

Adding domain to 365 tenant is going to stop mailflow?

After you finish setup, the MX record for your domain is updated to point to Microsoft 365 and all email for your domain will start coming to Microsoft 365. Make sure you've added users and set up mailboxes in Microsoft 365 for everyone who gets email on your domain!

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-11*

I’m checking how the things are going on about this issue?    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-09*

Hi Saurabh,    

There will be a migration process and it will be to add the domain or migrate the domain to O365, adding mx records and updating it to point it to the O365 via the DNS provider. Excellent article over here for the process - update-mx-records-to-office-365    

Also this article is good for understanding the routing - transport-routing    

Hope this helps.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
