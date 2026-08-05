---
title: "Exchange Powershell: Wrong LDAP coding"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/736683/exchange-powershell-wrong-ldap-coding
question_id: 736683
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Exchange Powershell: Wrong LDAP coding

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/736683/exchange-powershell-wrong-ldap-coding (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

$filter="{((((Company -eq 'XXXXXXXX') -and ((Title -eq 'Hauswirtschaft') -or (user.objectid -eq '2a424d65-88f1-49b5-87d8-2008c28e85b5')))) -and (-not(Name -like 'SystemMailbox{')) -and (-not(Name -like 'CAS_{')) -and (-not(RecipientTypeDetailsValue -eq 'MailboxPlan')) -and (-not(RecipientTypeDetailsValue -eq 'DiscoveryMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'PublicFolderMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'ArbitrationMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'AuditLogMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'AuxAuditLogMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'SupervisoryReviewPolicyMailbox')))}

When using

Get-Recipient -RecipientPreviewFilter $filter | ft displayname, company, department, title

Ist says

for recipient preview is neither a valid OPath filter nor a valid LDAP filter. Use the '-RecipientPreviewFilter' parameter with either an existing  

OPath filter string or with a valid LDAP filter string.  

-  CategoryInfo: InvalidArgument: (:) [Get-Recipient], ArgumentException  

-  FullyQualifiedErrorId: [Server=AM6PR08MB3655,RequestId=8bbcdb0f-7d08-4939-ae05-300a9aa36b0c,TimeStamp=15.02.2022 17:11:16] [FailureCategory=Cmdlet-ArgumentException] 1B362B53,Microsoft.Recip.ExientTasks.Management  

recipient  

-  PSComputer name: outlook.office365.com

What is wrong with the filter?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-02-15*

According to the on-line Get-Recipient web information (get-recipient) the -RecipientPreviewFilter uses LDAP syntax.    

Also, in your -RecipientPreviewFilter value you begin that string with "{((((Company -eq 'XXXXXXXX') and end it with 'SupervisoryReviewPolicyMailbox')))} -- and that's missing the terminating double-quote. You also include opening "{" and closing "}" characters surrounding the unterminated string. Those "{" and "}" are unnecessary.    

You also have a user.objectid in your filter string. I'm assuming you mean only to use objectid.    

If the on-line help for the Get-Recipient cmdlet is incorrect, and an OPATH filter is acceptable, I'd start by removing the "{" and "}" characters, adding the missing trailing double-quote, and using 'objectid' instead of 'user.objectid'.    

You should also review the usable properties in OPATH queries (recipientfilter-properties) because "objectid" isn't in that list.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-16*

Hi @Chris P      

I agree with the suggestions, the user.objectid is not a valid filterable recipient property. You may check if it should be ExchangeGuid or Guid.    

```
$filter="((((Company -eq 'XXXXXXXX') -and ( (Title -eq 'Hauswirtschaft') -or (ExchangeGuid -eq '2a424d65-88f1-49b5-87d8-2008c28e85b5')))) -and (-not(Name -like 'SystemMailbox{')) -and (-not(Name -like 'CAS_{')) -and (-not(RecipientTypeDetailsValue -eq 'MailboxPlan')) -and (-not(RecipientTypeDetailsValue -eq 'DiscoveryMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'PublicFolderMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'ArbitrationMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'AuditLogMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'AuxAuditLogMailbox')) -and (-not(RecipientTypeDetailsValue -eq 'SupervisoryReviewPolicyMailbox')))"
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
