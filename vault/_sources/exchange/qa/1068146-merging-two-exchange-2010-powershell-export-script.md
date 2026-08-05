---
title: "Merging two Exchange 2010 Powershell export scripts into one"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1068146/merging-two-exchange-2010-powershell-export-script
question_id: 1068146
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Merging two Exchange 2010 Powershell export scripts into one

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1068146/merging-two-exchange-2010-powershell-export-script (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.    

I've been trying to merge two scripts but I'm having problems and I need some help...    

I need to export specific information of my tenants mailboxes into a single CSV file but some information comes up empty on the CSV file cells and I found out that I need to use a different script to get that information, I tried to merge the two scripts but with no success and I've tried to use the "- Append" parameter to add the second script results on to the same CSV file but also with no success.    

This is the first script:    

Get-Mailbox -ResultSize Unlimited | Select-Object AddressBookPolicy, ProhibitSendQuota, SamAccountName, UserPrincipalName, WhenMailboxCreated, Alias, OrganizationalUnit, CustomAttribute1, DisplayName, PrimarySmtpAddress, RecipientType, RecipientTypeDetails, WindowsEmailAddress, WhenChanged, WhenCreated | export-csv -NoTypeInformation .\Mailboxes_filtered.csv -Delimiter ";" -Encoding unicode    

And this is the second:    

Get-Mailbox -ResultSize Unlimited | Get-MailboxStatistics | Select DisplayName, StorageLimitStatus, TotalItemSize |export-csv -NoTypeInformation .\Mailboxes_filtered.csv -Delimiter ";" -Encoding unicode    

If I try to add the second script objects into the first script, the respective cells on the CSV come up empty (except "DisplayName") and if I try to use all objects in the second script, only those three above won't show up empty on the CSV file.    

So what I really need is to merge or combine this two scripts into just one (or append the second script results into the same CSV file). I allready found out ways on this forum on how to resolve this issue but the solution is done with severall scripts and command lines using variables to store results but that won't work for me...what I really need is to get the information I need with just one script so it can be practical to use, after that I can organize the exported info on a Excel datasheet.    

Thanks in advance!

## Answers

_No answers on this thread._
