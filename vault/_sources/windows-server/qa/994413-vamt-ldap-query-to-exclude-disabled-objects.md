---
title: "VAMT - LDAP query to exclude disabled objects"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/994413/vamt-ldap-query-to-exclude-disabled-objects
question_id: 994413
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# VAMT - LDAP query to exclude disabled objects

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/994413/vamt-ldap-query-to-exclude-disabled-objects (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I did an AD scan and it's included Disabled Computer objects - when we decommission computer we leave them Disabled for a period of time before deleting them.    

Is it possible to do an LDAP query to exclude Disabled computer objects? I've never used the LDAP query in VAMT before.    

Thanks

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2022-10-22*

Update with the answer    

Finally constructed a working query pasted exactly this (but with my DC.domain.local)    

```
LDAP://dc01.domain.local/??sub?(&(objectClass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(lastLogonTimestamp>=133000000000000000))
```

Key was to know to search for words "ldap url syntax" so I could find the descriptions of explaining what would go between the question marks if they were given, or just the question marks next to each other if not, and the fact that the word 'sub' is for the scope.    

ldap://host:port/dn?attributes?scope?filter    

becomes this after deleting the dn, attributes, and putting sub in for scope, and (filter)    

ldap://dc01.mydomain.local/??sub?(filter between parenthesis)    

Previous reploy    

VAMT is the specific problem here for me - I also have a working LDAP query very similar that I can paste into DSA.msc or PowerShell Get-ADObject and they work great but I cannot get them to work in the VAMT GUI    

e.g. this works in PowerShell    

```
Get-ADObject -LDAPFilter '(&(objectClass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(lastLogonTimestamp>=133000000000000000))'
```

but pasting the same text from between the single quotes above into the LDAP filter box in VMAT Discover Products GUI says invalid LDAP filter:    

```
(&(objectClass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(lastLogonTimestamp>=133000000000000000))
```

( lastLogonTimeStamp happens to be about a few months back ~2022-06-18 )

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-12*

Hello    

Thank you for your question and reaching out. I can understand you are  having query related  to LDAP.    

To exclude disabled computer accounts from an AD Auto Detection Query you can add the following to your query filter: (!(userAccountControl:1.2.840.113556.1.4.803:=2))    

For example, the default query filter would be:    

ADQueryFilter="(&(objectClass=computer)((!(userAccountControl:1.2.840.113556.1.4.803:=2))))"    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-06*

This LDAP filter will return all computers, including servers, that are not disabled.    

```
(&(objectclass=computer)(!useraccountcontrol:1.2.840.113556.1.4.804:=2))
```

Gary.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-05*

Hi,    

What type of deployment options you are using? You can filter the disabled computers from the scope and only allow inscope computers/servers for the License.    

Also you can setup the firewall so the disabled servers cannot communicate via the network, block the ports?    

    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.    

----    

Please don't forget to upvote and Accept as answer if the reply is helpful
