---
title: "New Domain Controller Promotion Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1499793/new-domain-controller-promotion-error
question_id: 1499793
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# New Domain Controller Promotion Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1499793/new-domain-controller-promotion-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

I got the AD Forest. Ii contains one DC - WinServer 2012R2.  

Forest Level/Domain Level - 2012R2.  

What happened to this domain before me is not known.
Now I try add second DC (Windows Server 2016). And I'm getting the error:  

"

```
ADprep failure -->
Microsoft.DirectoryServices.Deployment.ADPrepLdapException:Ther is no such an object.
Extended error message: 8333. Server Message: 0000208D: NameErr: DSID-03100238, problem 2001 
(NO_OBJECT), data 0, best match of:
'CN-FIle Replication Services,CN-System,DC=MyDomain,DC=lan'
Adprep was unable to change security descriptor on object CN=Domain System Volume (SYSVOL share),CN=File Replication Service,CN=System,DC=domain,DC=com
[Status/Consequence]
ADPREP was unable to merge the existing security descriptor with the new access control entry (ACE).
[User Action]
Check the log file ADPrep.log in the C:\WINDOWS\debug\adprep\logs\20120530165523 directory for more information.
```

"  

In the ADPrep log I see this error:

```
The ADPrep encountered an error.Error Code: 0x20. Extended error code: 0x208d.
```

SYSVOL replication was migrated from FRS to DFSR some time ago (before I came). This migration has status 3 - Eliminated.  

I tried to find an object to which error message refers (CN=Domain System Volume (SYSVOL share) in ADSI, but there is no such an object,  there is  only object 'CN=File Replication Service,CN=System,DC=domain,DC=com' without any child objects  

What can I do to repair this error? Why ADPrep tries to change this object, although FRS eliminated allready?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-19*

Hi @Евгений Котляревский, 

About metadata cleanup. A don't see any "dead" host and DC's, so I'm not clear, what I should to clean up. Can you clarify this?

It was just a suggestion to check.

About registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\parametersValue SysvolReady.  

It is equal "1". What value should be?

It was just a suggestion to check. Value should be 1.

-  Can you please check the ADDS event logs on the DC and share any error that might show up in the recent past?

-  Sorry I haven't seen any confirmation from your side that you are running under Domain Admins, Enterprise Admins and Schema Admins context on the new DC server. Please open PS and run:

```
whoami /groups | ? {$_ -match " Admins"}
```

-  Can you attach somehow the content or the ADPrep.log, perhaps it will give more idea about the issue.

-  Can you run netdom query fsmo and check all roles are on the existing DC?

-  Can you show the schema version you have running? For Windows server 2012R2 it should be 69.

```
Get-ItemProperty 'AD:\CN=Schema,CN=Configuration,DC=contoso,DC=local' -Name objectVersion
```

-  Are you trying to add the DC from the wizard? Can you Run as Administrator manually in a CMD  adprep /forestprep? You can copy and run on a DC or run it like this:

```
adprep.exe /forestprep /forest yourforest.com /user yourEAuser /userdomain yourdomain.com /password yourpwd
```

  I believe Adprep.exe is included in the \Support\Adprep folder of the operating system disk. Copy here the full error please.

-  Can you ensure the both DC and new server have the latest updates and service packs?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-18*

Hi @Евгений Котляревский

If you want promote your first domain controller under Windows 2016 in existing forest you have two methods to upgrade schema:

-   use a admin account member of enterprise admins schema admins to promote to be able to upgrade automatically schema.

-  Upgrade  manually schema by running the command `adprep forestprep` on the domain controller with schema master role.
Installation actions and required administrative levels
Adprep - forestprep and domainprep

Please don't forget to accept helpful answer

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-18*

Hello Евгений Котляревский,
Thank you for posting in Q&A forum.  

Try to fix this issue, please check if you are in the Domain Admins and Enterprise Admins groups.

Here is a link with troubleshooting ADPREP Errors  
https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/troubleshooting-adprep-errors/ba-p/395869
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-18*

Hello,

I tried to find an object to which error message refers (CN=Domain System Volume (SYSVOL share) in ADSI, but there is no such an object, there is only object 'CN=File Replication Service,CN=System,DC=domain,DC=com' without any child objects

This is normal.

Ensure you are running with the right permissions, Domain Admin, EA...

Determine if the existing domain controller  has inconsistent objects (https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc785298(v=ws.10)?redirectedfrom=MSDN).

Check if you need to perform a metadata cleanup (https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816907(v=ws.10))

Check to make sure SYSVOL is shared, check the next value, if not set it to 1. 

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\parameters`  

Value `SysvolReady` = 1  

Please check what is the migration state using: 

```
Dfsrmig /getmigrationstate
```

Also check to see if the you get any errors with this command:

```
Dcdiag /e /test:sysvolcheck /test:advertising
```
