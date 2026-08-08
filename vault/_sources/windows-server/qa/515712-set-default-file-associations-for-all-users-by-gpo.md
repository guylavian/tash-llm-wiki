---
title: "Set Default File Associations for All Users By GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/515712/set-default-file-associations-for-all-users-by-gpo
question_id: 515712
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Set Default File Associations for All Users By GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/515712/set-default-file-associations-for-all-users-by-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can I set the default file associations for all users by GPO?  

This should have a simple answer but unfortunately none of the guides currently available online work for Windows Server 2019. So, I am here asking for a definitive set of steps that I can use to set a user's default applications.  

-  The user is a member of an Active Directory domain.  

-  The user is logging on to a Windows Server 2019 Remote Desktop Session Host.  

-  The user has a User Profile Disk.  

The main problem is that it is not possible to change a user's file associations by editing the registry as this only causes the Window's defaults to be reset and the user must manually pick the correct program. Also, exporting a user's file associations then trying to apply that XML to other users doesn't work and also only results in the new user having to pick the correct programs again.  

This should be simple thing so let's get a final - working - answer on this. How do you set the default associations?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-23*

Hi, I'm currently working on the same issue on my network.   

The problem i've run into at the moment is i've got 3 GPOs  

1 Machine GPO - File Association Global - This applies all default applications except PDF via the .txt file in File Explorer Options.   

2 User GPO - File Association Ops - This applies .pdf to utilise PDF Architect as the default application  

                   - File Association Sales - This applies .pdf to utilise Adobe Reader as the default application.

The Machine GPO works but it has to be a .txt file instead of .xml for some reason regardless that Windows's DISM command exports it as .xml it won't work if it isn't a .txt file.   

If I could find a way to get this to work it would be golden.
