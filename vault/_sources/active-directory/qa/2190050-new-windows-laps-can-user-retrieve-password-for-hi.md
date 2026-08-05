---
title: "New Windows LAPS - Can User retrieve Password for his Workstation?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190050/new-windows-laps-can-user-retrieve-password-for-hi
question_id: 2190050
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# New Windows LAPS - Can User retrieve Password for his Workstation?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190050/new-windows-laps-can-user-retrieve-password-for-hi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

we're currently using the old LAPS to manage the local Administrator on our clients.

Power Users have the rights to retrieve their local Admin-PW with a Powershell-Script.

I don't find any information, if this feature would be also useable/available, if we migrate to the new Windows LAPS - so i want to ask the MS Community.

With new LAPS, is it possible to

-  let Power Users (that are, for example, in a AD-Group "Power Users") retrieve the local Admin-PW of their Workstation?

-  let Admin-Users retrieve all Passwords for all clients?

Thanks in advance,

Bastian

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-28*

Hello Bastian M.,  

Thank you for posting in Microsoft Community forum.

You can check the Extended Rights permissions on the specific OU.

Because it grants the ability to read confidential attributes (all of the Windows LAPS password attributes are marked as confidential). One way to check to see who is granted these permissions is by using the `Find-LapsADExtendedRights`

For example:

Find-LapsADExtendedRights -Identity newlaps  

Make sure the result has only the specific group you want, users in this specific group can retrieve all Passwords for all clients.

Reference:

Get started with Windows LAPS and Windows Server Active Directory | Microsoft Learn

Also, I do not find powers users group in my AD domain lab.

Active Directory security groups | Microsoft Learn

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
