---
title: "GPO doesn't apply to user of the OU that is linked to"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/311749/gpo-doesnt-apply-to-user-of-the-ou-that-is-linked
question_id: 311749
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO doesn't apply to user of the OU that is linked to

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/311749/gpo-doesnt-apply-to-user-of-the-ou-that-is-linked (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everywhere,   

So before explaining my problem I describe to you my small Active Directory environment : two DCs, one Windows Server, and an OU named "X" that contains 6 users including the user "Y".   

I tried to write a script that create a GPO that change the background wallpaper to a solid blue one, here is the script :        

```
#Get-Command -Module GroupPolicy    
    New-GPO -Name "ChangeWallpaperInBlue" -comment "Change the wallpaper to a solid blue color"     
    New-GPLink -Name "ChangeWallpaperInBlue" -Target "OU=X,DC=mydomain,DC=local"          
    Set-GPPrefRegistryValue -Name "ChangeWallpaperInBlue" -Context User -Action Replace -Key "HKEY_CURRENT_USER\Control Panel\Colors" -ValueName Background -Type String -Value "0 0 255"          
    Set-GPPrefRegistryValue -Name "ChangeWallpaperInBlue" -Context User -Action Replace -Key "HKEY_CURRENT_USER\Control Panel\Desktop" -ValueName Wallpaper -Type String -Value ""
```

I started it one the primary DC, everything worked.  

I checked in the Group Policy Mgmt, the link between the GPO and the OU "X" is ok, in the Security Filtering list Authenticated Users are there and in the Delegation tab the Authenticated Users have Read and Apply the policy rights.   

I log into my server with the "Y" username but the wallpaper didn't change.  

So to check if my user has a GPO applied, I tried differents commands :         

`gpresult /user mydomain\X \v`  and I get : `INFO: The user "sevenkingdoms.local\robb.stark" does not have RSoP data.`         

`gpupdate`  and I get :     

Computer policy could not be updated successfully. The following errors were encountered:                                                                                                                                                       The processing of Group Policy failed. Windows attempted to retrieve new Group Policy settings for this user or computer. Look in the details tab for error code and description. Windows will automatically retry this operation at the next refresh cycle. Computers joined to the domain must have proper name resolution and network connectivity to a domain controller for discovery of new Group Policy objects and settings. An event will be logged when Group Policy is successful.  

To diagnose the failure, review the event log or run GPRESULT /H GPReport.html from the command line to access information about Group Policy results.   

I opened the GPReport.html but I can find the erroe description of the error precisely, it seems like the GPO are empty in "Denied GPO"...  

What did I do wrong?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Okay thank you @Anonymous   ,     

You (and I) found the answer actually! Here it is :    

In my case, I should have link my GPO to the Users group of my OU "Y", then I  should have set GPO Status to "Computer settings enabled" and finally the "not responding" error was due to some connectivity mistakes!    

Also this command is interessant to ensure the GPO is updated everywhere    

```
Get-ADComputer -Filter * -SearchBase "OU=Computers,OU=Y,DC=mydomain,DC=local" | Foreach-Object {Invoke-GPUpdate -Computer $_.name -Force -RandomDelayInMinutes 0}
```

Thanks for your time @Anonymous   !

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-17*

Hello @Thoms Rlln  ,

Thank you for your update.

I have two ideas

-   Please check if you run the script manually on one domain-joined machine to change the background wallpaper to a solid blue one, does it work?  

    If so, it seems the script is correct.

2.Are the items under C:\Windows\SYSVOL\Domain\Policies on both DCs the same?  

Or the items under C:\Windows\SYSVOL\Domain\Policies on both DCs are the same except (the one where I created the GPO) ?

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Thank you a lot @Anonymous   for your answer,    

To answer to the first part of your response, the status of my GPO is on "Enabled" so the user AND computer configurations are enabled (I may have to change to user only actually) then I run gpresult as you suggested and I got this :    

    

No GPO applied indeed, it says empty GPO...    

Now to answer to the 3 last questions :     

-  This GPO replace the values of 2 registry keys, it replaces the value of "HKEY_CURRENT_USER\Control Panel\Colors" with the string "0 0 255" that corresponds to the blue color and it replace the value of "HKEY_CURRENT_USER\Control Panel\Desktop" with an empty string because previously it was the png of the default background.    

-  As I noticed in the beginning of my answer, the computer configuration settings is not disabled so I'll change it and see if it changes something.    

-  Finally, on the primary DC (the one where I created the GPO) the GUID appeared in the "Policies" folder but on the second DC, the GUID doesn't appear at all in the folder, I may have problem of replication between the DC...    

What do you advice me to do now?    

Ps : I tried this command     

Get-ADComputer -Filter * -SearchBase "OU=Y,DC=mydomain,DC=local" | Foreach-Object {Invoke-GPUpdate -Computer $_.name -Force -RandomDelayInMinutes 0}    

that forces the GPO on all computers in the OU but I got this results :    

Invoke-GPUpdate :  Computer "my server" is not responding. The target computer is either turned off or Remote Scheduled Tasks Management Firewall rules are disabled.    

But the corresponding rules are enabled and the computer is turned on!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-15*

Hello @Thoms Rlln  ,

Thank you for posting here.

I am sorry, I do not familar with PS command, but I will try my best to troublehsoot the GPO issue for you.

If the GPO setting is user configuration , you can logon one member server using domain "Y" account and password.

1.Then create a new folder in C drive name Folder.  

2.Open CMD (do not run as Administrator).  

3.Type gpresult /h C:\Folder\wallpaper.html and click Enter.  

4.Open wallpaper.html and check if there is corresponding GPO setting under "User Details".

If there is no such GPO setting you configured under "User Details".

To better understand our question, please confirm the following information below at your convenience.

1.What actual GPO setting did you configured?  

2.Would you please check the GPO status on both DCs?  

3.Would you please check If the GUID of corresponding the GPO is under C:\Windows\SYSVOL\Domain\Policies on both DCs?  

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
