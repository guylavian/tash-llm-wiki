---
title: "Query list of Users in Active Directory Security Group (SG)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/219055/query-list-of-users-in-active-directory-security-g
question_id: 219055
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-tsql", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Query list of Users in Active Directory Security Group (SG)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/219055/query-list-of-users-in-active-directory-security-g (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Active Directory Security Group,  I am not completely sure on the LDAP information for this.   

I would like to write a T-SQL Query to return the list of all users in the Security Group.   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

Get Your Report in 2 Simple Steps:  

Run Netwrix Auditor → Click "Reports" → Navigate to Active Directory → "Active Directory State-in-Time" → Select "User accounts" → Click "View".  

To save the file, click the "Export" button → Select Excel format → Save as → Choose a location to save it.   

reference：https://try.netwrix.com/active-directory-export-gsn?cID=7010g000001MSaf&sID=71101474714&aID=aud-286005054959:kwd-378169896414&creative_id=339570337088&placement_id=&location_id=2840&gclid=EAIaIQobChMInK6u8-2G7gIVKJVLBR1-JQJjEAAYASAAEgLa0PD_BwE  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-05*

@SQLDev2021       

There is a AD Explorer tool which you can download and connect to it: https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer and can explore the properties.     

You need to know AD Server to connect to It using AD Explore. Use below cmd command to find AD Server.     

Pull the Groups and Members from Active Directory (AD) Using T-SQL    

Refer - https://arstechnica.com/civis/viewtopic.php?t=62769    

----------    

If this answers your query, do click “Accept Answer” and Up-Vote for the same. And, if you have any further query do let us know.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-05*

Hi @SQLDev2021       

To get a list of the users, try xp_logininfo if extended procs are enabled and the group in question is a windows group :    

EXEC master..xp_logininfo     

@acctname = '[group]',    

@1islessthan0   = 'members'    

For a quick view of which groups / roles the current user is a member of;    

select    

      [principal_id]  

    , [name]  

    , [type_desc]  

    , is_member(name) as [is_member]  

from [sys].[database_principals]    

where [type] in ('R','G')    

order by [is_member] desc,[type],[name]    

refer-    

sys.database_role_members (Transact-SQL)    

----------    

Please don’t forget to "Accept the answer" and “up-vote” wherever the information provided helps you, this can be beneficial to other community members.
