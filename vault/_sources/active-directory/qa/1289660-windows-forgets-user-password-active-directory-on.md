---
title: "Windows forgets user password (Active Directory) on unlocking, but logging on via Other User with same credentials logs in fine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289660/windows-forgets-user-password-active-directory-on
question_id: 1289660
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows forgets user password (Active Directory) on unlocking, but logging on via Other User with same credentials logs in fine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289660/windows-forgets-user-password-active-directory-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have a strange issue that randomly affects some users, with one repeatably facing the issue. The PC is a Windows 10 Pro device attached to Active Directory (Windows Server 2016) on our LAN (the occassional one via VPN). The users will try to unlock their workstations with their AD credentials, however it will tell them their username or password is incorrect. However, if they change to Other user and enter the same username (domain\username) and password, they will unlock and login fine. This is a bit of a nuisance for the users and I'd like to try and get to the bottom of it if possible.

Does anybody have any suggestions?

Thanks in advance.  

Regards,

Shane

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-23*

Hello Shane,

Thank you for your question and for reaching out with your question today.

This is happening because the remembered username is not including the domain.  Therefore, it will not authenticate and when entered manually, it will.  In order to resolve this issue you need to ensure that Windows 10 remembers not only the username, but also the domain to which it is connecting.

-  Type gpedit.msc into Run box, Enter.

-  Navigate to the following group policy object:

Computer Configuration\Administrative Templates\System\Logon

-  Find the entry "Block user from showing account details on sign-in" and "Do not enumerate connected users on domain-joined computer" and "Enumerate local users on domain-joined computers" in the right pane.

-  Configure "Block user from showing account details on sign-in" and "Do not enumerate connected users on domain-joined computer" as "Not configured" or "Disabled".

-  If you want to list all local user account, you can set "Enumerate local users on domain-joined computers" policy as "Enabled".

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
