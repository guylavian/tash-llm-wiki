---
title: "Adding and Showing Active Directory Sites in GP Management ?!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181731/adding-and-showing-active-directory-sites-in-gp-ma
question_id: 1181731
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Adding and Showing Active Directory Sites in GP Management ?!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181731/adding-and-showing-active-directory-sites-in-gp-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have been searching for this about a week now and could not find a single reference.

Using Powershell how to add Active Directory Sites to the Group Policy Management window, as can be seen below.

I can add GPO link the the sites but not able to find how to show them in the window.

```
New-GPO -Name "Home"
Get-GPO -Name "Home" | New-GPLink -Target "dc=home,dc=lab" -LinkEnabled Yes -Enforced Yes -ErrorAction Stop
Get-GPO -Name "Home" | New-GPLink -Target $workstationSite-LinkEnabled Yes -Enforced Yes -ErrorAction Stop
Get-GPO -Name "Home" | New-GPLink -Target $serverSite -LinkEnabled Yes -Enforced Yes -ErrorAction Stop
```

Anyone knows how to achieve this ?

Thank You

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-21*

Hi @touqeeranjum  

Click on show sites , then you select target site. Once done , you will able to get the list of linked GPO on this sites as mentioned below:

Please don't forget to mark helpful answer as accepted
