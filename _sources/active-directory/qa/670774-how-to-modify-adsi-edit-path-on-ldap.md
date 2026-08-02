---
title: "How to Modify adsi edit path on LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/670774/how-to-modify-adsi-edit-path-on-ldap
question_id: 670774
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How to Modify adsi edit path on LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/670774/how-to-modify-adsi-edit-path-on-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'd like to ask on how to modify adsiedit connection settings on Path: ?    

When opening Connection Settings. We have 4 sites which consist with 4DC. Each DC is replicated through DFSR. The 3DC CONNECTION Settings path is targeted to its DC while the 4th DC path is pointing to 1, 2, 3 DC depends when you freshly opened the adsiedit management console.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-21*

Hi @Los Omnalacab       

I'm not sure if you are asking how to change the connection path or why a specific connection path is selected.    

To answer the first part, how to change the path, the Computer and Connection Point sections of the dialog can be used to change the Path to reflect your selections.    

The default domain controller that is shown in the dialog, will be based on the AD Sites and Services configuration and which IP addresses are assigned to an AD site.  You can you this option in NetTools to determine which AD site an IP address has been assigned to and this option to determine which sites that DC have been assigned to.     

Gary.
