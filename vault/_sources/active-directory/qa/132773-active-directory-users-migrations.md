---
title: "Active Directory users migrations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132773/active-directory-users-migrations
question_id: 132773
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory users migrations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132773/active-directory-users-migrations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody,  

We are a huge facility with number of OUs under our domain.   

I would like to move the users who have logged in, in last 7 days moved to a different folder. Basically there is a OU name extended leave (people who are on leave) and there is one named Office Staff. I would like to move all active users ( users who have logged in, in past 7 days)  from extended leave to Office Staff.  

I was tried running different scripts but didn't get a exact solution for it. It would be great if someone can help me out here.   

Thank you :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-21*

The LastLogonTime is an object the doesn't exist in the AD. It's produced by PowerShell based on the value found in the user's LastLogonTimestamp property.  

Have a look at one of the AD users that has never logged on using ADSIEdit or ldp.exe and see what the value is.  

Also, I gave you a couple of links that explain how to use the property. It's important to note that if you have more than one DC the property isn't replicated immediately. It may be 9 to 14 days after a user logs on before other DC's receive the updated information. If you need to be sure of the date you'll have to check every DC (even remote ones, and perhaps deal with DCs that are inaccessible at the time you run the script).  

If the LastLogonTimestamp is present on a user that has never logged on, you should be able to retrieve that property and convert it to a DateTime object using something like this:  

[datetime]::FromFileTime( $_.lastLogonTimestamp )

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-21*

Hi,    

Assume the OUs named Extended Leave and Office Staff are $ExtendedLeave and $OfficrStaff    

```
Get-ADUser -Filter * -SearchBase $ExtendedLeave -Properties LastLogonDate | Where-Object { $_.LastLogonDate.AddDays($NumberDays) -gt $CurrentDate } | Move-ADObject -TargetPath $OfficrStaff
```

Best Regards,    

Ian    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-20*

Hi,  

You can use the following script to move all users logged in past 7 days to a target OU:  

```
Import-Module ActiveDirectory
#Number of Days to check back.
$NumberDays=7

#Organizational Unit to search
$targetOU='OU=Users,OU=Camtac,OU=Canada,DC=linamar,DC=com'

#Move user to target OU
GET-ADUSER -filter *  -properties LastLogonDate | where { $_.LastLogonDate.AddDays($NumberDays) -lt $CurrentDate } | move-ADobject -TargetPath $targetOU
```

Don't forget to mark this reply as answer if it help you to fix your issue
