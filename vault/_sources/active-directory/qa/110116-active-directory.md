---
title: "Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/110116/active-directory
question_id: 110116
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/110116/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,  

I have set password expire days as 180 days but user password get expire within 90 days. whenever I run net user xxxx /domian command it showing password will expire in 90 days. Please help me to set password expire days as 180 Days   

Server 2016 Standard Edition.  

Thanks   

Yogesh

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-02*



## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-29*

Hi,    

There are 2ways to set the password policy in AD :    

One is to configure it through GPO :Default domain policy     

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-policy    

    

One is the FGPP (only for users and groups):    

https://learn.microsoft.com/en-us/archive/blogs/canitpro/step-by-step-enabling-and-using-fine-grained-password-policies-in-ad    

    

When using “net user samAccountName /domain“, the value returned by “Password expires” doesn’t take in consideration the fine grained policies.    

It only shows the domain password policy.    

    

You can considered the following Powershell command to confirm the password expired date.    

Get-ADUser -filter {Enabled -eq $True -and PasswordNeverExpires -eq $False} –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" |    

Select-Object -Property "Displayname",@{Name="ExpiryDate";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}}    

    

Get-ADUserResultantPasswordPolicy USERNAME

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-28*

Hi,  

You have to edit the password policy applied on impacted users in order to set the value 180 days for Maximum password age settings.  

To set password policy , you can use GPO default domain policy or Fine Grained Password Policy:  

password-policy-active-directory  

fine-grained-password-policy-best-practices  

Please don't forget to mark this reply as answer if it help you to fix your issue
