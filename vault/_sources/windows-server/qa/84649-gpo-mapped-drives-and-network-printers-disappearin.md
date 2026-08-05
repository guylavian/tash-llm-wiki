---
title: "GPO Mapped drives and network printers disappearing every few weeks on all domain PCs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/84649/gpo-mapped-drives-and-network-printers-disappearin
question_id: 84649
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO Mapped drives and network printers disappearing every few weeks on all domain PCs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/84649/gpo-mapped-drives-and-network-printers-disappearin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a Windows 2019 standard virtual server (VMware) that is functioning as a file and print server.  We have 3 mapped drives and several networked printers that are applied to each user at login through GPO.  Two of the mapped drives are data drives everyone has access to, G and V.  The other is the P drive, which is mapped to their “My Documents”.  Users’ My Documents are remapped to this server through GPO.  

Every three weeks or so as users log in, they are not getting mapped to the G or V drive but their P drive is still mapped.  When it happens, it occurs with every user and every computer on the domain.  If you are already logged in and this happens, you will still have access to the drives.  When this is occurring, you can still get to the share by navigating to it \FS\Drive 1 or \FS\Drive 2.  I actually have a shortcut that points to those and the shortcut still works when the issue occurs.  The GPO that maps the G and V drive has the same settings as the P drive, just a different location.  

Yesterday, it was also discovered that shared printers from that server are missing from the user’s printer list when this issue is occurring.  

Rebooting the “FS” server immediately resolves the issue.  The user has to log off and back on or occasionally reboot to get everything back.  

Upon reviewing the event logs from the server, there is nothing indicating any type of issue.  

There is nothing happening specifically on the days that this is occurring that I can identify as the cause of this.  

Previous to the Server 2019 FS, we had a Win 2012 R2 on Hyper-V.  I’m not sure if this started happening when we migrated to VMware or moved everything to the new Win2019 server.  It really shouldn’t matter.  It’s just a simple file and print server.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-03*

Hi,  

Thank you for posting in our forum.  

Change the group policy to Update rather than Replace the drive mapping. In the Group Policy Object (GPO) where drive maps are defined, edit User Configuration >   

Preferences > Windows Settings > Drive Maps.  

Hope this information can help you  

Best wishes  

Vicky
