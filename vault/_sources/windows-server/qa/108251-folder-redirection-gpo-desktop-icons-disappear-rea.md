---
title: "Folder Redirection GPO - Desktop Icons disappear/reappear when desktop refreshed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108251/folder-redirection-gpo-desktop-icons-disappear-rea
question_id: 108251
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Folder Redirection GPO - Desktop Icons disappear/reappear when desktop refreshed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108251/folder-redirection-gpo-desktop-icons-disappear-rea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2012r2 domain  

-1 Domain Controller (JC-DC01)  

-1 File Server (JC-File)  

-150-175 users  

-Mixed environment of Windows7 and Windows10, about 50/50  

-Offline Files enabled  

-DNS set to DC only  

-Gigabit infrastructure

Here are the scenarios…

The user logs in.  

All icons and programs seem to be fine on the “desktop”.  

Network folder (U: Private) is connected.

Issue #1  

If there is a file on the “desktop”, and the user opens it.  

• It may open with no problem.  

-  OR -  

• A error message might appear. See pic #1.

Issue #2  

If there is a file “created and saved” to the “desktop”.  

• It may save to desktop.  

-  OR -  

• An error message might appear.

Issue #3  

The “desktop” icons simply disappear.  

Except for the “Recycle Bin”, “This PC”, and “user folder”.

• Usually can right click and select “Refresh” and the icons reappear.  

-  OR -  

• An error message appears. If I select “OK”, then the icons may reappear.  

-  OR -  

• I have to sign off or reboot to make icons reappear.

Issue #4  

All Icons are on the desktop as they should be.  

Right click and select “Refresh”.  

All icons disappear.  

Same as #3.

Issue #5  

Open up “Documents” folder.  

Select a file.  

• It may open with no problem.  

-  OR -  

• A error message might appear.  

• Select “OK” and it might open up.  

-  Or -  

• Same error message may appear again.

I can provide any questions asked, and I'm extremely motivated to remove this issue from the environment.

## Answer (community) — community member

*upvotes: 2 · updated: 2020-10-01*

I'm having almost the exact same problem (similar setup, similar results) and would love to see a resolution. One thing I'm noticing is that in my events viewer on the AD server, I'm seeing the user logging off of the domain in rapid succession when this happens (like 5 times in a row, less than a second apart). Also, it seems to happen only when a program creates temp files in the same directory as the file being opened (Desktop, Documents), especially with Microsoft Office products (Word, Excel, Publisher).

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-25*

One revelation was discovered -     

During the GPO creation, the dreaded 'Grant user exclusive rights to 'Desktop' and 'Documents' were checked.  This has since been disabled, "gpupdate /force" ran, and I do realize that this will not retroactively affect any user folder.    

Current GPO settings - it was purposefully kept as simple as possible, with the exception that the 'Grant' box was check unknowingly by installer tech.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-05*

I am still testing this but so far it looks like turning off Access Based Enumeration for that particular share seems to have fixed the issue.   

We have 4 users out of about 40 that were having the same issues as you described. Desktop icons would disappear when creating new documents or just at random.  

I disabled Access based Enumeration of the server that is hosting the share (no reboot needed)  

I tested again and it was still occurring, however after a reboot of the client device the issue seems to have been resolved for each of the affected users.  

I would like someone else to confirm this works for them. Good luck!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

Hi@Philip Gardner      

Thank you for posting in our forum    

If offline files are disabled icons are not available when a user is not on the LAN, this is by design. If they are redirected can you actually see a users desktop folder in the redirected location? Is it mirroring what the user is experiencing? Would be pretty east to test all of this with a VM od a desktop to see what is really going on.    

What exactly are the icons for that they need access to? Local programs? File share locations? Other?     

Hope this information can help you    

Best wishes    

Vicky
