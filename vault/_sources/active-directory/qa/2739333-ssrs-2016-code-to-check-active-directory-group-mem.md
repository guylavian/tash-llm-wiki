---
title: "SSRS 2016 code to check active directory group membership"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2739333/ssrs-2016-code-to-check-active-directory-group-mem
question_id: 2739333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 39
qa_tags: []
---
# SSRS 2016 code to check active directory group membership

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2739333/ssrs-2016-code-to-check-active-directory-group-mem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had a SQL server running MS SQL 2014 on a Windows 2008 R2 server for reporting services.  I had the need to be able to check if the user running certain reports belonged to a certain active directory security group.  I added the following code to my report

Public Function IsMemberOfGroup() As Boolean 

If System.Threading.Thread.CurrentPrincipal.IsInRole("Active Directory Group") Then

Return True 

Else

Return False 

End If 

End Function

Then I used a dataset filter checking the true/false state of the function.  This worked perfectly then today we upgraded to SQL Server Standard 2016 SP1 CU4 and the functionality no longer works.  When I check the value it just displays #ERROR. 

Anyone have any ideas why?

## Answer (community) — community member

*upvotes: 0 · updated: 2017-09-12*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet SQL Server Forums.

https://social.technet.microsoft.com/Forums/sqlserver/en-US/home?category=sqlserver

"MSDN SQL Server Forums"

https://social.msdn.microsoft.com/Forums/sqlserver/en-US/home?category=sqlserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
