---
title: "In Active Directory how do i get the number of joined computers and disjoined computers list?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1857672/in-active-directory-how-do-i-get-the-number-of-joi
question_id: 1857672
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# In Active Directory how do i get the number of joined computers and disjoined computers list?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1857672/in-active-directory-how-do-i-get-the-number-of-joi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Active Directory Disjoined computers from the domain are still on computer container. how do i know which computer has been disjoined and which one is actively being used. and i want to get the total numbers of computers that are join to the domain and computers that have been disjoined or formatted?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-09*

Hi,

The computer object will be disabled after the domain computer leaves the domain. You can get the disabled computers by running the PowerShell command below

```
Get-ADComputer -Filter {Enabled -eq "False"}
```

To get the domain computers , run

```
Get-ADComputer -Filter {Enabled -eq "True"}
```

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
