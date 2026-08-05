---
title: "How to use Active Directory user photos as account logon image in Windows clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/353218/how-to-use-active-directory-user-photos-as-account
question_id: 353218
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to use Active Directory user photos as account logon image in Windows clients 

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/353218/how-to-use-active-directory-user-photos-as-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Apply to:　Windows 7, Windows 8, Windows 10

The purpose of this Step-by-Step Guide is to use Active Directory user photos in Windows clients.  

This guide contains instructions for user photos in Active Directory and steps to use it as a account logon image.

User photos are stored in the attributes of the user accounts in Active Directory.　The photos can be used by applications like Outlook, Skype for Business (Lync) or SharePoint to display the picture of currently logged-in user in their interface.

There are three steps to use Active Directory user photos in Windows clients:

• Import photos into Active Directory  

• Assign registry key permissions through Group Policy  

• Deploy a logoff script through Group Policy  

• Check the result  

Step One: Import photos into Active Directory  

Following PowerShell command can be used to complete the goal.

$ADphoto = [byte[]](Get-Content<path to file>-Encoding byte)  

Set-ADUser<username>-Replace @{thumbnailPhoto=$ADphoto}

Just remember to provide an exact path to the image file and the user’s name, for example in my lab:  

  

If you want to Set up photo for users in batch, a CSV file named photos.csv need to be prepared as following format:  

AD_user, path_to_file  

User1,C:\Photos\user1.jpg  

User2, C:\Photos\user2.jpg  

User3, C:\Photos\user3.jpg  

Then the PowerShell command should be :

Import-Csv C:\Photos\photos.csv |%{Set-ADUser -Identity $_.AD_user -Replace @{thumbnailPhoto=([byte[]](Get-Content $_.path_to_file -Encoding byte))}}

In my lab:

  

  

Note: the path for the photos and csv file can be either a local path or a UNC path as in the screenshot.

Then you can check if the thumbnailPhoto attribute of the user has been set.  

Open the Active Directory Users and Computers tool and make sure that Advanced Features options on the View menu is checked.  

Right click the user and select the properties, then select the attribute Editor tag, check if the thumbnailPhoto attribute shows any value. If you see <not set>, it means there is no photo configured. Here are screenshots for your reference:  

  

  

Note:  

There is also one key point – the photo stored in the thumbnailPhoto attribute cannot be bigger than 100 kB, and the recommended size is 96 x 96 pixels.  

Here is the most beautiful picture to be used in my lab.  

Step Two. Add registry key permissions through Group Policy  

Create a new GPO on the domain level.  

  

Note: Assign the change account picture permission to users through the registry key. If users don't have the permissions, the scripts in step 3 would not work.  

The registry key is under: MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AccountPicture\Users

Edit the GPO under Computer Configuration>Windows Settings>Security Settings>Registry as following:  

Right click the Registry entry, and click Add Key:  

  

Navigate to: MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AccountPicture\Users  

  

Give FULL permission to users:  

  

  

Click OK and close the Group Policy Management Editor.  

To update Group policy, we need to restart the computers.

Step Three. Deploy a logoff script through Group Policy

For the script, you can refer to this one.  

Note: This script is used to export the photo stored in the thumbnailPhoto attribute and saves it on your machine, in a specified folder (in this case: C:\ProgramData\AccountPictures{User SID}).

Copy the script content to your notepad and saved as filename.ps1; Put it into a shared folder. Users should have permission to read it.

Edit the GPO we created before.  

Navigate to User Configuration>Windows Settings>Scripts  

Double click the logoff  

Click add option, enter the path of the script as following:  

  

Click the option Show files, copy the file to the location:  

  

Update the group policy : log off and login again.

Last, check the result. **  

If the policy was applied, you will see the result on the clients where the users will logon to:  

The photo stored in the thumbnailPhoto attribute would be exported to into a specified folder on your machine. **(C:\ProgramData\AccountPictures{User SID})  

New registry keys will also be created under MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AccountPicture\Users{User SID} in the Windows registry, with paths to these photos.  

And you will see the photo we configured on the logon image.  

If you also want to use the photos, have a try!

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2022-02-23*

For everyone who struggles with this tutorial:  

-  There is easier way then scripting to import pictures into AD. https://www.codetwo.com/freeware/active-directory-photos/ - it's free and (at least for me) it worked out-of-the-box  

-  Script from step "Three" isn't working with "just" copy-paste. In this script line $image_base uses different environment variable then what we need. On Classic Shell forum script has line $image_base = $env:public + "\AccountPictures" what means that it points on C:\Users\Public. That's why this line has to be replaced with $image_base = $env:ALLUSERSPROFILE + "\AccountPictures". With that changes (at least for me) it worked in first try.  

-  I suggest simple \Domain Controller\netlogon as a place to put script  

-  In GPO it's better to place this script into "Powershell scripts" instead of "Scripts".

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-04-11*

Hi There @Anonymous       

Nice article. I have followed it and I can see the photos added to the program data\account pictures. I can also see the registry entries have been made but still the photo isn't being shown at login.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-30*

I can see the picture in the small avatar within the start menu - however it won't show up at login. Any idea whats missing on my systems?

PS: the script linked in the article is not accessible anymore. I took an alternate version from here:

https://woshub.com/how-to-set-windows-user-account-picture-from-active-directory/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-20*

It works as far as copying the script to Logoff folder. Access Denied.  

Which permissions do I need? Cant seem to find the correct one.  

Edit:  

Found the solution. Don't use UNC network path. Open folder locally and paste the file.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-17*

@Anonymous   I have followed your step however I am not able to view the image on my computer ?     

-  I can see the images in registry but not in (C:\ProgramData\AccountPictures{User SID})    

-  I have enable the default account picture in the GPO which we have created.
