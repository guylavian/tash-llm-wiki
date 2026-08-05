---
title: "Inconsistent LDAP filter results - ldap query works only once, second (and subsequent) runs return only one user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/848407/inconsistent-ldap-filter-results-ldap-query-works
question_id: 848407
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Inconsistent LDAP filter results - ldap query works only once, second (and subsequent) runs return only one user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/848407/inconsistent-ldap-filter-results-ldap-query-works (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I am trying to query an Active Directory tree for some users. The AD is configured with Nested Groups. I am using the LDAP_MATCHING_RULE_IN_CHAIN.  

We are using a java class that is building this LDAP queries from a key/value configuration file. everything on this side works well; below I list the 3 properties involved where I built a filter to retrieve the users that are members to one TargetGroup (the target group has only nested groups under it):  

foreign-ldap-users-of-group-search-base=DC=domainprefix,DC=domain,DC=DomainSuffix   

foreign-ldap-users-of-group-searchfilter=(&(objectCategory=Person)(objectClass=user)(sAMAccountType=805306368)(memberOf:1.2.840.113556.1.4.1941:=cn=TargetGroup,ou=Test,ou=Service,DC=domainprefix,DC=domain,DC=DomainSuffix ))   

foreign-ldap-users-of-group-attribute=cn   

*the -SearchScope SubTree is assumed by default in the java class used for querying the AD  

*when using  (sAMAccountName=u%) instead of (sAMAccountType=805306368) the results are empty, the (sAMAccountType=805306368) is not really necessary here (same behaviour with or without)  

The issue is that it has a different behavior after first run: it works exactly once meaning that at first use is working as expected returns 12 users with their properties, but beginning with second call (running the exact same query again) the result is only one user, actually the first user that is found in the sequence.  

We can't explain the behavior. Do you have some insight regarding this behavior?   

Thank You!  

Valentin M.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-17*

I found the issue in a value of "query optimization" that was used in the java class.   

There was a line in the logs for the case that was returning only one user stating: “searchLdap, property: foreign-ldap-search-optimization : set. Optimization detected so skipping second invocation of hasMoreElements.”  

So I added this property to my configuration snippet and set it to false "foreign-ldap-search-optimization=false" and now the results are consistent.  

Though I am not sure why this "optimization" was breaking the behaviour.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-14*

Hi @Vali Munteanu       

I have tested the LDAP_MATCHING_RULE_IN_CHAIN query against a Windows 2019 AD with LDP, NetTools and ADFind, in all cases they return the same number of objects on the first and subsequent runs.  Both NetTools and ADFind initiate a new LDAP connection each time a query executed, while LDP uses a same connection for all queries.  So it would appear there might be an issue with your implementation.    

I can get the samaccountname filter to work but search must be the complete name or include a wildcard    

```
(&(objectCategory=Person)(objectClass=user)(sAMAccountType=805306368)(memberof:1.2.840.113556.1.4.1941:=CN=grp1,CN=Users,DC=w2k12,DC=local)(samaccountname=greynolds))  
(&(objectCategory=Person)(objectClass=user)(sAMAccountType=805306368)(memberof:1.2.840.113556.1.4.1941:=CN=grp1,CN=Users,DC=w2k12,DC=local)(samaccountname=g*))
```

Based on your query provided I'm not sure what you are trying to achieve and there may be alternative methods to get the same information.    

If you are trying to get the complete list of all the members of a group included nested groups, then using the msds-tokenGroupNames attributes of the group object will return a complete list of all the DNs that are members, then its a simple search of the returned list of DNs to check if a user is a member.    

Or if you want to see if a user is a member of a specific group, including nested groups, then the msds-TokenGroupNames of the user object, will return the complete list of groups that the user is a member of, again a simple search of the returned list to confirm if the user is a member of a specific group.    

The downside of using the ms-TokenGroupName attribute is that it's a constructed attribute and only returned if the search scope is base.  And because it's a constructed attribute, you can't use the Attribute Scope Query control to directly query the members attributes.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-13*

Not sure why you would need the sAMAccountType if you already have objectClass=user.   The objectClass is already defining the type to a certain extent.  If it doesn't do anything, remove it.  

The main reason to use ObjectClass=User is because its an indexed field and it makes the searches much quicker when you have at least one indexed field.  

sAMAccountName would only bring back one entry even if it did work.  

The memberOf looks odd.  What are those numbers for? 1.2.840.113556.1.4.1941  

When I started with LDAP, I used Apache Directory Studio to verify searches and syntax, as it only takes one element in the wrong place to break everything.  

Keep it simple to start with.  Try the following.    

'(&(objectClass=user)(memberOf=CN=TargetGroup,OU=Test,OU=Service,DC=domainprefix,DC=domain,DC=DomainSuffix))'  

Does that work consistently?  Once that works, you can add in other attributes in a controlled manner.  

One other attribute for consideration is UserAccountControl  

The following is a "normal" user.  Enabled user with account expiry set .  

UserAccountControl:1.2.840.113556.1.4.803:=2  

https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx  

I tend to do everything with users in PowerShell now and you can test LDAP searches without having the AD CMDlets installed.  For example..  

```
$searcher=[adsisearcher] '(&(UserAccountControl:1.2.840.113556.1.4.803:=2)(memberOf=CN=groupA,OU=Test,OU=Groups,DC=xx,DC=yy,DC=zz)(objectClass=User))'
$searcher.PropertiesToLoad.AddRange(@('displayname','mail'))
$searcher.FindAll() | Select-Object @{n='displayname';e={$_.properties['displayname'][0]}},@{n='mail';e={$_.properties['mail'][0]}}
```
