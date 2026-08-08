---
title: "Exchange Online - New GAL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165520/exchange-online-new-gal
question_id: 1165520
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online - New GAL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165520/exchange-online-new-gal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our organisation recently split into two divisions/companies. Both companies currently share the same M365 tenant and same physical hypverV hosts but have their own on-prem AD/vm's.  

To provide company separation, within Outlook, we setup a new GAL/OAB/Address Book Policy etc using company attribute filtering. See below:  

New-GlobalAddressList -Name "CompanyA GAL" -IncludedRecipients AllRecipients -ConditionalCompany "CompanyA"

Set-GlobalAddressList -Identity "CompanyA GAL"

New-OfflineAddressBook -Name "CompanyA OAB" -AddressLists "CompanyA GAL"

New-AddressList -Name "CompanyA Users" -IncludedRecipients AllRecipients -ConditionalCompany "CompanyA"

New-AddressBookPolicy -Name "CompanyA ABP" -AddressLists "CompanyA Users" -OfflineAddressBook "CompanyA OAB" -GlobailAddressList "CompanyA GAL"-RoomList "\All Rooms" 

This has worked but now the users in CompanyA can no longer see any Distribution Groups or Contacts. The Groups and Contacts objects in AD do not have the company attribute. How do i go about creating New-AddressList for CompanyA groups and contacts and add them to the CompanyA ABP?  

Thanks in advance.

## Answers

_No answers on this thread._
