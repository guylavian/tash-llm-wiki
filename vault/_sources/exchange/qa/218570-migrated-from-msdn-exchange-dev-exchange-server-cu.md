---
title: "[Migrated from MSDN Exchange Dev]Exchange server CU19 upgrade failed with \"User does not have permissions but is a member of Enterprise Admins\" error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218570/migrated-from-msdn-exchange-dev-exchange-server-cu
question_id: 218570
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev]Exchange server CU19 upgrade failed with "User does not have permissions but is a member of Enterprise Admins" error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218570/migrated-from-msdn-exchange-dev-exchange-server-cu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange server CU19 upgrade failed with "User does not have permissions but is a member of Enterprise Admins" error  

[Original post]  

Hi Guys,  

Single exchange server organization.  

Trying to run the CU19 setup from exchange server and got this error message -  

Error:  

Active Directory must be prepared with 'Setup /PrepareAD'. However, the current user account doesn't have the permissions required even though it's a member of the 'Enterprise Admins' group. Check whether this is a valid user account.  

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.AdUpdateRequired.aspx  

I followed one article (https://supertekboy.com/2017/09/20/error-running-preparead-user-does-not-have-permissions-but-is-a-member-of-enterprise-admins/) and added 'Exchange servers' group to following but that didnt fix my problem.  

Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User Rights Assignment  

Under User Rights Assignments double-click Manage auditing and security log.  

​​​​​​​  

I am already member of all the highest priviledge groups like DA, EA, Organization Management but still facing this.  

Do i need to run schema command on AD server???  

ANY HELP/SUGGESTION IS HIGHLY APPRECIATED, THANK YOU

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-10*

Please check if you are the member of schema admin group.  

CMD run as administrator and the run the command.  

Cheers!
