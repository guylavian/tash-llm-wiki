---
title: "why after removing User from Active Directory still have access to sql server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/921430/why-after-removing-user-from-active-directory-stil
question_id: 921430
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# why after removing User from Active Directory still have access to sql server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/921430/why-after-removing-user-from-active-directory-stil (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i'm new to the use of active directory group to grant access to sql server.     

for POC purpose, i have some users added to 'local' active directory group and i have created a login for this group in my sql server instance.    

as far as testing goes, users are able to access the sql resource.     

When I remove a user from AD group, the user is still able to login to sql server.     

As per my understanding , user should not be able to login to sql.    

We used windows authentication for each individuals and now we are trying to get on board with use of AD group for granting access on sql server.    

one of the benefits we counted was that ultimately, user management will be taken care only on AD end & not in Sql server. -- for example  - a new developer needs access to db, we can add them to AD group. or when a developer leaves, they can be removed from AD group & hence all db access will be removed.    

But the later is not happening.    

Why is this happening, what concept am i missing.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-07-11*

Logon is only checked during logon to SQL Server.   Removing a person's access while that user is still logged on, does not disconnect the user.    

Users can be members of multiple groups.  If you granted multiple groups access to SQL Server, the user almost certainly has access using a different group.      

Also, it can take up to 1 hour (as a default) for AD updates to be replicated to all domain servers and take effect.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-07-11*

Hi  @Vijayvargia, Sudipta  ,    

You have to remove this user from the database to remove permissions for this user, in logins may still have the user account    

Use `xp_logininfo` tp check permission path    

https://social.msdn.microsoft.com/Forums/en-US/885be589-7fb9-492d-80ca-e0d435212474/ad-user-removed?forum=sqlsecurity    

-------------    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-07-11*

Another way to investigate how the user gets access is by running:    

```
EXECUTE AS LOGIN = 'YourDomain\YourUser'  
   go  
   SELECT * FROM sys.login_token  
   go  
   REVERT
```
