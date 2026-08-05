---
title: "[Windows server 2022] Can't add new users in GPO \"Allow remote desktop services\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1331795/windows-server-2022-cant-add-new-users-in-gpo-allo
question_id: 1331795
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# [Windows server 2022] Can't add new users in GPO "Allow remote desktop services"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1331795/windows-server-2022-cant-add-new-users-in-gpo-allo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone.

We have a problem, since last week we can't add users to the 'GPO - Allow remote desktop services'.

 I've tried looking for evidence in 'local security policy --> local policy --> assign user rights --> allow remote desktop services to connect but I can't add the users. 

Blocked by the error "this setting is incompatible with computers running windows 2000 service pack 1 or later".

2023-07-17_16h19_06.png

Does someone already encounter this ?

Thanks by advance for your replies

A.S

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-04*

Hello again, 

The GPO is out, we don't need it for our purpose.

So I focused on finding the cause of the problem and here's what I can say :

-  Users using remote office are all part of  'Remote Office Users Group', even the problematic account.

-  In the 'Local Group Security' all users from remote group are present except the problematic account 

(users were added manually one by one and not the remote group itself).

In this case I can't add new user to the local group security because of the grey key 'Add user or group'.

Is there any way to possibly add the user differently or some setting in the registrery that can help  ?

Thanks by advance the replies

A.S

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-18*

@Wesley Li-MSFT  

Thanks for your response.

Another error appeared while creating new GPO, 'Network name not found'.

2023-07-18_11h57_26.png

I was thinking about the Fsmo roles on the server, so I checked with 'netdom query fsmo' but everything seems fine.

2023-07-18_12h08_15.png

Thanks by advance for your replies

A.S

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-07-18*

Hello

The error message "this setting is incompatible with computers running Windows 2000 Service Pack 1 or later" indicates that the Group Policy setting you are trying to configure is not supported on computers running Windows 2000 SP1 or later versions. The setting in question, "Allow remote desktop services," is likely specific to an older version of Windows and is not applicable to newer versions.

In Windows 2000 and later versions, Remote Desktop Services (RDS) or Remote Desktop Protocol (RDP) has undergone significant changes and improvements. To enable or configure remote desktop access on newer Windows versions (e.g., Windows Server 2008 or later, Windows 10, Windows 8.1, etc.), you should use the appropriate and compatible settings.

Here's how you can enable Remote Desktop access on Windows Server 2008 or later:

Using Group Policy Management Console (GPMC):

a. Open the Group Policy Management Console (GPMC) on a domain controller or a computer with the Remote Server Administration Tools (RSAT) installed.

b. Navigate to the appropriate GPO that is linked to the Organizational Unit (OU) containing the target computers.

c. Edit the GPO and go to the following path:

Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Connections

d. Look for the setting "Allow users to connect remotely using Remote Desktop Services" and set it to "Enabled."

Using Local Group Policy Editor on a Single Computer:

a. Press Win + R, type gpedit.msc, and press Enter to open the Local Group Policy Editor.

b. Navigate to the following path:

Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Connections

c. Locate the setting "Allow users to connect remotely using Remote Desktop Services" and set it to "Enabled."

After making the changes in Group Policy, the Remote Desktop feature should be enabled on the targeted computers. Make sure you apply the GPO to the correct OUs or use the Local Group Policy Editor on the individual computers where you want to allow Remote Desktop connections.

If the response is helpful, please click "Accept Answer" and upvote it.
