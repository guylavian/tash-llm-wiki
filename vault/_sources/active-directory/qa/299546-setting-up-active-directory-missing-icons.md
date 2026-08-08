---
title: "Setting up Active Directory - Missing Icons"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299546/setting-up-active-directory-missing-icons
question_id: 299546
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Setting up Active Directory - Missing Icons

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299546/setting-up-active-directory-missing-icons (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There everyone  

I am new to active directory and I am currently setting up a small server for my business at home. Myself and my colleague will both have a computer (client) in which we log into the domain with.  

The server (currently running windows server 2016) is up and running, Active directory has been installed and user profiles and shares have been set (upon login it connects the home folder to a L drive, all working fine)  

The two client PCs are both running windows 10 and have been added to the domain.  

I am however having a slight issue, where upon logging into the domain with AD user and password, there are no desktop icons, just text shortcuts. When using file explorer there are no folder icons, and no navigation pane which is usually on the left hand side (normally would display this pc, network etc) Also when hovering over icons in the start menu a black box appears where there would normally be an icon.  

I can only assume I have missed something when setting up the group policies etc, however if anyone has come across this issue before I would be grateful for a fix.  

Many thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi everyone  

thanks for your responses   

I will try these out and get back to you over the weekend!  

Chris

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi,  

Sounds like issues with the IconCache in your new server installation.  

Try the following steps  

To Rebuild icon cache follow the steps:  

a.       

Open Folder Options to select (dot) Show hidden files and folders.  

b.       

Open a Windows Explorer Window.  

c.        

Go to C:\Users(User Name)\AppData\Local  

d.       

Right-click on  

IconCache.db and click on Delete.   

e.        

Click on Yes to confirm the deletion.  

NOTE:  

This deletes the file to the Recycle Bin. It is safe to empty the Recycle Bin when finished.  

f.        

Close the Window.  

g.       

Empty the Recycle Bin.  

h.       

Restart the computer.  

i.         

When you go back, you will notice the Size of the IconCache.db file is smaller, and the Date Modified is now the current date.  

j.         

The icon cache has been rebuilt.  

or another possible remedy set up a BAT script and run this.  

-  TASKKILL /f /im explorer.exe  

-  CD /d %userprofile%\AppData\Local  

-  DEL IconCache.db /a  

-  START explorer.exe  

-  EXIT  

This happens if the installation has had hic-cup, or you've installed software that may have corrupted the IconCache.db, so this is just a way of reloading the IconCache.db instead of doing a full re-installation of the server.  

Hope this helps  

Best regards  

Ulv

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-05*

Hi,  

Thank you for your question. Did you update your DC to the latest version? Also have you made any changes in the GPOs? specially in the Default Domain policy.  

Please reply to the questions so we could able to find a solution soon.  

Stay safe.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hi,  

To know the issue more clearly, would you please share a screenshot of the issue?(Please hide the private information)  

Are there any issues if you logon with a local user?  

For the policies, i would check all the policies on the client by command :  

For the user policies :just run the command as the logon user : gpresult /h report.html  

For the computer policies, run the command as the administrator: gpresult /h report2.html  

Then check if any policies related.  

Best Regards,
