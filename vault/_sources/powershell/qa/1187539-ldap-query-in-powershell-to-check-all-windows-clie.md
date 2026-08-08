---
title: "LDAP query in PowerShell to check all Windows clients that are authenticate against LDAP in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187539/ldap-query-in-powershell-to-check-all-windows-clie
question_id: 1187539
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP query in PowerShell to check all Windows clients that are authenticate against LDAP in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187539/ldap-query-in-powershell-to-check-all-windows-clie (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning to migrate our current domain (LDAP) to a new domain (LDAPS) in our company. 

All of the clients in our site authenticated against LDAP AD. Now we want to block LDAP auth, and migrate all clients to a new domain using LDAPS. 

Is there a LDAP query in PowerShell to check all Windows/Linux clients authenticate against LDAP within AD?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-08*

The AD won't have the information you're looking for.

This is old and the EventIDs have probably changed: https://serverfault.com/questions/193100/log-ldap-access-of-the-active-directory

Here's another way (more recent): https://www.manageengine.com/products/active-directory-audit/how-to/how-to-monitor-active-directory-ldap-logs.html#:~:text=With%20ADAudit%20Plus%201%20Enable%20LDAP%20auditing%20Open,2012%29%20Number%20of%20daily%20unsecure%20LDAP%20bind%20

I'm sure you'll find other information on this subject. But know that the security log can fill rapidly. Keep any eye on it!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-08*

I want to check or list the users (and their PC name) that are authenticated right now for my Windows domain using ldap query in PowerShell. 

Below query did not return a response. 

$ldapFilter = "(&(objectClass=computer)(lastLogonTimestamp>=1))"

$computers = Get-ADComputer -LDAPFilter $ldapFilter

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-08*

Hello

If a understand correct, you are looking for this.

```
$ldapFilter = "(&(objectClass=computer)(lastLogonTimestamp>=1))"
$computers = Get-ADComputer -LDAPFilter $ldapFilter
```

If not, please, explain what u expect from a result.

Regards
