---
title: "Map drive - Group Policy Preferences - GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1397974/map-drive-group-policy-preferences-gpo
question_id: 1397974
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Map drive - Group Policy Preferences - GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1397974/map-drive-group-policy-preferences-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, i want to deploy the map drives by GPO (preference) and stop to use the login scripts to map more than 500 drives. 

I have just one issue if I do that: if one condition changes to apply this drive (example: one user account is moved from one OU to another, the user should stop to map the drive), in update mode, the drive will not be removed and the user will keep it even if he should not. If I chose the Replace Mode, the drive will be removed each time that the GPO is applied (so between 90 minutes and 120 minutes) and can cause some troubles for the user during this time. 

By logon script, the advantage is that one function remove the drive if it should be be there. What about the GPP ? How do you handle this kind of situation ? I have found some parameters in the setting “Configure Drive Maps preference extension policy processing” but it’s not working as expect. Do you know Any “native” solution to do that ?

Thank you in advance :)

Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-24*

Hello Rémi Rizzo,

Thank you for posting in Q&A forum.  

By logon script, the advantage is that one function remove the drive if it should be be there. What about the GPP ?  

A: We can remove the drive map on client manually, or you can set permission (deny read or/and deny write) on drive map shared folder.  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
