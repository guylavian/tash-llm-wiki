---
title: "ldapsearch syntax"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/98350/ldapsearch-syntax
question_id: 98350
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# ldapsearch syntax

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/98350/ldapsearch-syntax (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to perform a demo using LDAP.  

I am not an LDAP expert neither a Linux expert, but I was able to install ldapsearch on a Linux box and (copying from several sites) to perform a query like the following one:  

ldapsearch -x -b "DC=mydomain,DC=local" -H ldap://192.168.1.1 -D "CN=Administrator,CN=Users,DC=mydomain,DC=local" -W "objectclass=user" -W sAMAccountname  

It works, but the result includes either the AD users and other objects.  

Can anybody please help me refining the query so that I can list all the AD users and nothing else?  

A guide to use ldapsearch to query Active Directory would be really apreciated....  

Regards  

marius

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-22*

Hi,@Marius - Roma       

Thank you for the update.    

The grammatical problem you mentioned may be beyond the scope of knowledge of our forum. Specific to the user's grammar, I recommend you to find a senior engineer. They can give you more professional help.    

reference:https://support.microsoft.com/en-in/hub/4343728/support-for-business    

Thank you for your understanding and support    

Best wishes    

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-20*

Many thanks.  

I suspect that my question was unclear.  

I want to list only users.  

With my original query I see few information (name, dn and sAMAccountname) either of users and of computers and of some groups.  

If I remove the trailing "-W sAMAccountname" I see a lot of additional information about all the same objects.  

What I need, instead, is listing information about only users ("John Doe", "Jane Doe" and so on) without computers and groups.  

How should I enter the query?  

Regards  

marius

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-18*

This is not the correct syntax.  

ldapsearch -x -b "DC=mydomain,DC=local" -H ldap://192.168.1.1 -D "CN=Administrator,CN=Users,DC=mydomain,DC=local" -W "objectclass=user" -W sAMAccountname  

remove the trailing "-W sAMAccountname  

The final query would be:  

```
ldapsearch -x -b "DC=mydomain,DC=local" -H ldap://192.168.1.1 -D "CN=Administrator,CN=Users,DC=mydomain,DC=local" -W "objectclass=user"
```
