---
title: "Removing the last Exchange 2019 server in client's organization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1081125/removing-the-last-exchange-2019-server-in-clients
question_id: 1081125
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Removing the last Exchange 2019 server in client's organization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1081125/removing-the-last-exchange-2019-server-in-clients (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Following the instructions here https://learn.microsoft.com/en-gb/Exchange/manage-hybrid-exchange-recipients-with-management-tools  to turn of my client's last Exchange 2019 server. On step 3, under Permanently shutting down your last Exchange Server, when I run Remove-FederationTrust "Microsoft Federation Gateway" I get the error:    

 Can't remove federation trust "Microsoft Federation Gateway" It's in use by the following organization(s):    

CN=Federation,CN=XXXXX,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=XXXXXXXXX,DC=local    

-  CategoryInfo : InvalidOperation: (Microsoft Federation Gateway:ADObjectId) [Remove-FederationTrust], Or    

gsStillUsingThisTrustException    

All previous steps in the article have completed successfully.     

What do I need to do to complete the cleanup before turning off (not uninstalling) their last server?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-13*

Hi @LilyLi2-MSFT   and @Amit Singh  ,    

Thank you for your help. Deleting the entry through ADSI did indeed fix the issue, so I could complete the rest of the steps. Appreciate the help.     

/Paul

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-10*

Also you can look this article - https://social.technet.microsoft.com/wiki/contents/articles/54559.how-to-remove-last-exchange-server-in-organization.aspx

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-09*

This issue can occur if outdated or obsolete registry entries are present in Active Directory Domain Services (AD DS), and these registry entries point to deleted instances.    

For example, this issue can occur if you run the Hybrid Configuration Wizard on Exchange 2013 after a previous Exchange 2010-based federation trust was incorrectly or incompletely removed.    

Check this article for more help - https://learn.microsoft.com/en-us/exchange/troubleshoot/hybrid-configuration-wizard-errors/running-hybrid-configuration-wizard-fails
