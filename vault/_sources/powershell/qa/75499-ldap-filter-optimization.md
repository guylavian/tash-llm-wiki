---
title: "LDAP filter optimization"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/75499/ldap-filter-optimization
question_id: 75499
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# LDAP filter optimization

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/75499/ldap-filter-optimization (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have the following filter to select users from multiple groups.  

As these groups all have the same parent OU path, is there any way I can simplify this filter to remove the need to remote the common parent path for each sub-group ?  

Thank you.  

(&(objectCategory=user)(|(memberOf=CN=TEST1_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST2_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST3_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST4_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST5_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)  

(memberOf=CN=TEST6_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)))

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-24*

Try this:  

```
$Parent = ',OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain'
$Query = "(&(objectCategory=user)(|(memberOf=CN=TEST1_NAMED$($Parent))(memberOf=CN=TEST2_NAMED$($Parent))(memberOf=CN=TEST3_NAMED$($Parent))(memberOf=CN=TEST4_NAMED$($Parent))(memberOf=CN=TEST5_NAMED$($Parent))
(memberOf=CN=TEST6_NAMED$($Parent)))"
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-08-24*

As far as I know:  

-  You have to specify the DN of the group in a LDAP query  

-  Wildcards are not allowed for the DN  

Maybe this is an option:  

-  Add all groups you want to query in another group and use only this group in the LDAP query  

-  Create Group "AllTestGroups_NAMED"  

-  Add the groups Test1_NAMED, Test2_NAMED, Test3_NAMED, Test4_NAMED, Test5_NAMED and Test6 _NAMED to the "AllTestGroups_NAMED"  

-  Query on "memberOf=CN=AllTestGroups_NAMED",OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)  

Maybe this is helpful.  

Regards  

Andreas Baumgarten  

(Please don't forget to Accept as answer if the reply is helpful)
