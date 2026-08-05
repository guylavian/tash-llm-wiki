---
title: "Azure files with JOIN to ON PREM AD - Kerberos Key Rotation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1284563/azure-files-with-join-to-on-prem-ad-kerberos-key-r
question_id: 1284563
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-files", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Azure files with JOIN to ON PREM AD - Kerberos Key Rotation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1284563/azure-files-with-join-to-on-prem-ad-kerberos-key-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

we are using Azure Files with integration to our ON PREM Active Directory. JOIN of the storage account into our Active Directory was done using the AzFiles Hybrid Powershell modules. Everything works without any problems and is productive.

During the join 2 Kerberos keys are generated in the storage account - kerb1/2 e.g. With the function "Update-AzStorageAccountADObjectPassword " new keys can be generated and applied to the domain object: 

Example:

Update-AzStorageAccountADObjectPassword `

        -RotateToKerbKey kerb2 `

        -ResourceGroupName "<your-resource-group-name-here>" `

        -StorageAccountName "<your-storage-account-name-here>" `

 

In the documentation I find the following about this: 

"This action will change the password for the AD object from kerb1 to kerb2. This is intended to be a two-stage process: rotate from kerb1 to kerb2 (kerb2 will be regenerated on the storage account before being set), wait several hours, and then rotate back to kerb1 (this cmdlet will likewise regenerate kerb1)."

I understand that during the update kerb1 will be replaced by a updated kerb2 and thus the password of the domain object will be changed. 

However, it is unclear to me why I should wait for a few hours and then go back to a new kerb1. What is the background?

## Answers

_No answers on this thread._
