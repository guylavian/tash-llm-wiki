---
title: "Import bulk contacts in Active Directory w/ powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/823841/import-bulk-contacts-in-active-directory-w-powersh
question_id: 823841
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Import bulk contacts in Active Directory w/ powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/823841/import-bulk-contacts-in-active-directory-w-powersh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I manage multiple domains in my organization. The domain and forest level are server 2016. We have a one-way Azure AD sync to Office 365.   

I get the question about not seeing one another's email addresses in the Office 365 GAL. I know I can add them in manually one by one.   

What I'm looking to do is take all of the "enabled" adusers from one domain and import them into other domain as a "contact". Is there a powershell script that would do that. Basically, I would run two separate scripts one to export all "enabled" adusers into a csv and the second script would convert the adusers into a contact in the of domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-26*

Hi KeithHampshire-3198,    

Please use this PowerShell script to export all active AD users into a CSV:    

Get-ADObject -Filter 'objectClass -eq "contact"' -Properties *|select name,@{e={"$($_.memberof)"};l="Member Of"}|Export-csv  Contacts.csv -NoTypeInformation    

You may then import contacts from your csv to AD easily with a powershell script. Here the example I've used to bulk import:    

Powershell    

Import-Module ActiveDirectory    

$Users = Import-CSV C:\path\to\users.csv    

foreach($User in $Users){    

  $Params = @{    

    SamAccountName = $User.SamAccountName  

    Description = $User.Description  

    Name = "$($User.GivenName) $($User.Surname)"  

    DisplayName = "$($User.GivenName) $($User.Surname)"  

    GivenName = $User.GivenName  

    Surname = $User.Surname  

    Department = $User.Department  

    Company = $User.Company  

    EmailAddress = $User.EmailAddress  

    UserPrincipalName = "$($User.SamAccountName)@keyman  .com"  

    AccountPassword = (ConvertTo-SecureString $User.AccountPassword -AsPlainText -Force)  

    Path = "OU=$($User.OU),DC=domain,DC=com"  

    Enabled = $true  

    ChangePasswordAtLogon = $true  

  }    

  New-ADUser @Params    

}    

-----------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-25*

@Keith Hampshire      

I guess you need this script, it will export user mailbox from Exchange server:    

```
Get-Mailbox -ResultSize unlimited |where{$_.RecipientTypeDetails -eq "UserMailbox"} | select Name,PrimarySmtpAddress | Export-Csv c:\temp\1.csv -NoTypeInformation
```

Then, you could copy this CSV file to another Exchange server, then run command below to export those mailbox as mail contact:    

```
Import-Csv c:\temp\1.csv | foreach {New-MailContact -Name $_.Name -ExternalEmailAddress $_.PrimarySmtpAddress}
```

Please note, if there exists same username on those Exchange servers, you will get issue when creating mail contact. Because this username has been used.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-23*

Yes, everything is separate. Three different AD forest. Three different O365 tenants. All of the domains are not in the same tenant. No, each Exchange organization does not create multiple GALs.  

Example: I manage domain01, domain02 and domain03. All are separate with their own AD forest and O365 tenant. Nothing federated (nothing touches so to speak).
