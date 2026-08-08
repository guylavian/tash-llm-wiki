---
title: "\"ldap queries - need the dn of the users who are authenticated via ldap protocol and their IP address\" We are migrating authentication out of AD/LDAP."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/645660/ldap-queries-need-the-dn-of-the-users-who-are-auth
question_id: 645660
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# "ldap queries - need the dn of the users who are authenticated via ldap protocol and their IP address" We are migrating authentication out of AD/LDAP.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/645660/ldap-queries-need-the-dn-of-the-users-who-are-auth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

LDAP/AD Experts,  

It might be simple for you but its challenging task for me!.

****"ldap queries - need the dn of the users who are authenticated via ldap protocol and their IP address"  

We are migrating authentication out of AD/LDAP.****

We’re looking to migrate applications that are directly using AD for employees.  

Its not specific to OU and Group but overall active directory.  

We have plenty of applications which uses AD/LDAP for authentication.  

How do I pull such data? At least need to have user details.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-02*

Hi @Dharanesha E       

To find the user and group base DN, run a query from any member server on your Windows domain.    

Finding the User Base DN    

Open a Windows command prompt.    

Type the command:    

dsquery user -name <known group name>    

In the above command, you can pull out DN users based on the known group name.    

---------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-02*

What do you mean migrating out of AD/LDAP? (specifically the AD part)  

You are removing Active Directory Domain Services from your environment? Getting rid of all the Domain Controllers? Or are you trying to identify who does LDAP Simple Binds in AD?
