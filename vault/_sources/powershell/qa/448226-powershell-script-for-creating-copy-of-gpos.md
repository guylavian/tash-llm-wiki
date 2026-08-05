---
title: "Powershell script for creating copy of GPOs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/448226/powershell-script-for-creating-copy-of-gpos
question_id: 448226
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Powershell script for creating copy of GPOs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/448226/powershell-script-for-creating-copy-of-gpos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Team, could you please help with the script to copy the existing GPOs and create a copy of the GPO with PowerShell script for creating copy of the multiple GPOs for testing

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-24*

Hi,    

You can link the GPO to a specified OU using the New-GPLink cmdlet.    

```
$sourceGPO = "TestGPO"  
$targetGPO = "test_productionGPOname"  
$ou = "OU=test, DC=contoso, DC=com"  
Copy-GPO -SourceName $sourceGPO -TargetName $targetGPO  
New-GPlink -Name $targetGPO -target $ou -LinkEnabled Yes
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-23*

Hi @jay k  ,    

You can accomplish this by using the Copy-GPO PowerShell cmdlet, here's a couple of examples on how to copy a Group Policy with PowerShell:    

Copy one GPO    

```
Copy-GPO -SourceName "TestGpo1" -SourceDomain "test.contoso.com" TargetName "TestGpo1" -TargetDomain "sales.contoso.com"
```

Copy all GPOs    

```
Get-GPO -All -Domain "sales1.contoso.com" | ForEach-Object {$_ | Copy-GPO -TargetName ($_.DisplayName) -TargetDomain "sales2.contoso.com" -CopyAcl -MigrationTable "C:\Temp\tables\MigrationTable.migtable"}
```

----------    

If the reply was helpful please don't forget to `upvote` and/or `accept as answer`, thank you!    

Best regards,    

Leon
