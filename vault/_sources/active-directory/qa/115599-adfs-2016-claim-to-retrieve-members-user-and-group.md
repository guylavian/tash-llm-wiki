---
title: "ADFS 2016 - Claim to retrieve members (user and group) cross forest of an AD group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/115599/adfs-2016-claim-to-retrieve-members-user-and-group
question_id: 115599
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2016 - Claim to retrieve members (user and group) cross forest of an AD group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/115599/adfs-2016-claim-to-retrieve-members-user-and-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey everyone,  

I'm trying to figure out a way to send all the members from an AD group INCLUDING nested groups from a different forest.  

So let's say I am authenticated with DOMAINA\USER1 and I am a member of DOMAINA\GROUPA which itself is a member of DOMAINB\GROUPA then when I query DOMAINB with a claim it should be able to retrieve my DOMAINA\USER1 from DOMAINB\GROUPA.  

So far I can only retrieve users member of DOMAINB\GROUPA but not groups like DOMAINA\GROUPA in it  

Rule1:  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid", Issuer == "AD AUTHORITY"]  

 => add(store = "Active Directory", types = ("http://TESTDOMAIN/phase1"), query = "objectSid={0};distinguishedName;TESTDOMAIN\username", param = c.Value);  

Rule2:  

c:[Type == "http://TESTDOMAIN/phase1"]  

=> add(store = "Active Directory", types = ("http://TESTDOMAIN/phase2"), query = "(member:1.2.840.113556.1.4.1941:={0});distinguishedName;TESTDOMAIN\username", param = c.Value);  

Rule3:  

c:[Type == "http://TESTDOMAIN/phase4"]  

 => issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/role", Value = c.Value);  

Any ideas how I can manage that?  

Thanks!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-07*

In theory we can build such rules. But in practice there are several challenges...    

The user doesn't exist on the other side. So we can't use the DN (distinguishedName) of the user but we need to build the Foreign Security Principal DN from the user's SID. For example the DN should be something like:    

    

and not    

    

Not a big deal I know but that matters.    

Then the 1.2.840.113556.1.4.1941 operator will need the group DN not the user's DN as in your scenario it is not the user member of the group in the other forest but one of its group it is a member of. So you would have to enumerate all the users' groups, get their SIDs, craft the Foreign Security Principal DN and then send the LDAP queries (one for each group) with the aforementioned operator. We could do some filtering if not all the groups have to be considered in you know in advance which groups should be queried on the other side. Or, you could use the operator with the user's Foreign Security Principal DN if the user were to be a direct member of the groups in the trusted forest. Then you need only one query.    

And finally, the biggest issue in my opinion, is still about the operator 1.2.840.113556.1.4.1941. It is EXTERMLY inefficient and greedy. In large environments (i.e. an environment with a lot of objects) such an operator can bring DCs to 100% CPU for few seconds (minutes) and take a very long time to get done (could be minutes too), which is not only a terrible user experience (the browser is idled on the user's side) and you impact all applications using domain controllers if you hit one of these perf issues.    

So even if we can make it work, it would not scale.
