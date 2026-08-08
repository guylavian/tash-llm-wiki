---
title: "ldap question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/589324/ldap-question
question_id: 589324
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# ldap question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/589324/ldap-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have 6 DC's in 4 different locations.  

Can someone tell me what this ldap message means? I get this on almost 4 time each minutes and in each event we see the name of one of our 4 domain controllers  

Event 1535:  

Internal event: The LDAP server returned an error.   

Additional Data   

Error value:  

0000208D: NameErr: DSID-03100213, problem 2001 (NO_OBJECT), data 0, best match of:  

	'CN=DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domainname,DC=local'  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-14*

Hi @GaryReynolds-8098 Thanks for your reply,  

That's right the extended logging has been enabled, but I just wonder what this Error value:  

0000208D means?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-13*

Hi   

Have a look at this ldap-interface-event-on-one-server-onlypost it suggests that the events are caused because extended logging has been enabled on that DC.  

Gary
