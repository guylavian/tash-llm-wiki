---
title: "Internal event: The LDAP server returned an error. Error value: 0000208D: NameErr: DSID-03100238, problem 2001 (NO_OBJECT)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126751/internal-event-the-ldap-server-returned-an-error-e
question_id: 126751
fetched: 2026-07-25
answer_count: 15
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Internal event: The LDAP server returned an error. Error value: 0000208D: NameErr: DSID-03100238, problem 2001 (NO_OBJECT)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126751/internal-event-the-ldap-server-returned-an-error-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Following the advice in the 2020 LDAP Channel binding and LDAP signing requirements  I changed the LdapEnforceChannelBinding to 1 and set the logging level to 2. Now I'm getting information log entries in the Directory Services log like the below. It references my 2 domain controllers which scares me a little. I've run DCDIAG and it does not come up with any errors. I've also checked replication using AD Replication Status Tool 1.0 and it also comes up clean. I just want to make sure this is not a sign of a larger problem  

Internal event: The LDAP server returned an error.   

Additional Data   

Error value:  

0000208D: NameErr: DSID-03100238, problem 2001 (NO_OBJECT), data 0, best match of:  

	'CN=DC1,CN=Servers,CN=1-Office,CN=Sites,CN=Configuration,DC=LocalDomain,DC=local'

AND  

Internal event: The LDAP server returned an error.   

Additional Data   

Error value:  

0000208D: NameErr: DSID-03100238, problem 2001 (NO_OBJECT), data 0, best match of:  

	'CN=DC2,CN=Servers,CN=2-Office,CN=Sites,CN=Configuration,DC=LocalDomain,DC=local'

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-15*

Please post the source and event ID  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-15*

Thank you for your time. It is going to be difficult for be to setup a capture on that server. But I'm glad it seems like it shouldn't be an issue. The error below is also coming up often in the Directory Services log, does it mean anything in conjunction with the original error? (random number of duplicates)  

Duplicate event log entries were suppressed.   

See the previous event log entry for details. An entry is considered a duplicate if the event code and all of its insertion parameters are identical. The time period for this run of duplicates is from the time of the previous event to the time of this event.   

Event Code:  

400005ff   

Number of duplicate entries:   

1

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-14*

You may need to do a network capture. It looks like the request is targeting some object that doesn't exist. Likely is not fatal as you said the dcdiag, repadmin comes back clean.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-14*

Thank you for your reply @Anonymous   . I did see the article but it seemed a bit dated as I'm sure more and more people will be enabling logging I thought there had to be a bit more info out there.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-14*

Maybe this one helps.  

https://social.technet.microsoft.com/Forums/windowsserver/en-US/97cef83c-9757-4aa1-8205-453eae872dd3/ldap-interface-event-on-one-server-only?forum=winserverDS  

--please don't forget to Accept as answer if the reply is helpful--
