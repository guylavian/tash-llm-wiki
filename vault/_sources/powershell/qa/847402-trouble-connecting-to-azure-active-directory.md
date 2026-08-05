---
title: "Trouble connecting to Azure Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/847402/trouble-connecting-to-azure-active-directory
question_id: 847402
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
---
# Trouble connecting to Azure Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/847402/trouble-connecting-to-azure-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings...  

I am trying to authenticate my credentials using Azure Active Directory to write files to Azure File Share from my windows server. I am using the below cmdlet  

cmdlet:  

```
Install-Module AzureAD
Import-Module AzureAD
Connect-AzureAD
Get-AzureADUser
```

Error:  

```
Connect-AzureAD : The term 'Connect-AzureAD' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
```

Not sure what all packages are required and where do I find them.  

The below cmdlet shows what I have installed but when I search for the string `AzureAD` nothing is returned.  

```
(Get-Module -ListAvailable AzureAD*).path
```

I tried installing module `MSOnline` and no luck.  

```
install-module MSOnline
```

Thank you

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-06-08*

Hi @Raj D   ,     

Alternatively, could you please try using Microsoft Graph PowerShell instead to see if you can install and get Azure AD users list? Here is complete list of Azure Graph cmdlets for you reference.    

Steps:    

Install Graph Module    

Authenticate to MS Graph using `Connect-MgGraph -Scopes User.ReadWrite.All`    

To get user list, use following cmdlet `Get-MgUser`    

Hope this helps.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-25*

Hello @Raj D   ,    

Thanks for your query.    

The issue is that Cloud Shell provide a function which overrides the default Connect-AzureAD so that it uses the custom authentication mechanism Cloud Shell uses to avoid you having to re-enter credentials.    

FYI: https://learn.microsoft.com/en-us/answers/questions/788725/39connect-azuread39-is-not-recognized-as-a-name-of.html    

Best regards,    

Leila    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.
