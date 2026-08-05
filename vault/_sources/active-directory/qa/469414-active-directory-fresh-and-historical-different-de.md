---
title: "Active Directory - fresh and \"historical\" - different default permissions on user/computer objects"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/469414/active-directory-fresh-and-historical-different-de
question_id: 469414
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory - fresh and "historical" - different default permissions on user/computer objects

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/469414/active-directory-fresh-and-historical-different-de (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

i recently got some problems with the security of user objects after the "printernightmare mitigation".  

So i looked through some of the users and their security settings.  

Some users differ from others and even after a reset and a new "inheritance" - they are still not set the same.  

So i decided to built a new 2019 DC in my test lab to compare the security on a fresh DC with mine.  

The differ in various ways.  

Is the security ever "patched" and are there recommendations what to change if you change the forest to a higher level?  

Best regards  

Stephan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-20*

Just to share: I just found out that it only affects a few accounts that had admincount=1 once.  

So i wrote this script to find out which users have the "wrong/different" setting. I now "restore defaults" on the user accounts in phases. But it seems to be OK.  

```
Import-Module ActiveDirectory
$allusers = Get-ADUser -Filter * -Searchbase "OU=Users,DC=domain,DC=local" -Properties DistinguishedName
ForEach ($User in $allusers)
    {
    $ACLs = Get-ACL -path "AD:$user" | select -ExpandProperty Access
    ForEach ($ACL in $ACLs)
        {
        If ($ACL.IdentityReference -eq "NT AUTHORITY\Authenticated Users")
            {
            If ($ACL.ActiveDirectoryRights -like "*GenericRead*")
                {
                Write-Host $user " betroffen"
                }
            }
        }
    }
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-12*

Hello @StephanG  ,    

Thank you for posting here.    

Hope the information provided by Thameur-BOURBITA is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-07-09*

Hi,  

It's recommended to remove all unnecessary permissions added on Unit organisation level or on objects level, especially , on high privileged accounts.  Active Directory Access Control List – Attacks and Defense  

You can based on default permission when as you did in order remove all unnecessary permissions, it's a good approach.  

Please don't forget to mark helpful reply as answer
