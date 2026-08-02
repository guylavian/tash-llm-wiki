---
title: "Powershell Active Directory Password Never Expires"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316870/powershell-active-directory-password-never-expires
question_id: 316870
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Powershell Active Directory Password Never Expires

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316870/powershell-active-directory-password-never-expires (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

 Our Org default is to not allow password never expires. However, for operational needs, admins can change this setting per account as needed. I would like to know if anyone can direct me to a powershell script to force the bit back to false. I would want to run this on specific AD OUs and not the whole tree. The thought is we can do cleanup if an admin forgets to set this bit back after the need.  

Best,  

Tash

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-17*

Hi  @Wahid, Tash       

Please check to see if this works for you.    

```
$OUs = 'OU=ou1,DC=contoso,DC=com','OU=ou22,DC=contoso,DC=com'  
foreach($OU in $OUs){  
    Get-ADUser -Filter {PasswordNeverExpires -eq $true} -SearchBase $OU  | Set-ADUser -PasswordNeverExpires $false  
}
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-16*

You can try something like this (working on a DC within your organization):  

```
$OUs ='OU=one,DC=mydomain,DC=local','OU=two,DC=mydomain,DC=local'
ForEach ($OU in $OUs){
        Get-ADUser -filter * -SearchScope $OU -properties Name, PasswordNeverExpires | 
            Where-Object { $_.passwordNeverExpires -eq "true" } | 
                Where-Object {$_.enabled -eq "true"} |              # don't worry about disabled users
                    Set-ADUser -PasswordNeverExpires:$false
}
```

If you want to include disabled users just remove that last Where-Object.  

I don't have an AD to test this, so you might have to change the test "{$.enabled -eq 'true'}" to just "{$.enabled}".
