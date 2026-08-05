---
title: "Windows Admin Center Active Directory Minimum Permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299747/windows-admin-center-active-directory-minimum-perm
question_id: 299747
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows Admin Center Active Directory Minimum Permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299747/windows-admin-center-active-directory-minimum-perm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Admin Center active directory requires you to connect to a DC for it to appear. As far as we can tell you must be a domain admin, however there are plenty of scenaiors like helpdesk where WAC would be useful to update user information without those users having domain admin rights. Is it possible to use WAC active directory extension without having domain admin rights?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-05*

After doing my own research, your answer should have been "you need to configure a JEA endpoint on the domain controller" and provide documentation for what minimum permissions and how to configure the JEA endpoint so that users can manage active directory without being a domain admin. That documentation doesn't exist as far as I can tell, so I guess I may need to write an article on it.    

https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/plan/user-access-options#role-based-access-control

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-05*

@Anonymous   thank you for your reply but I don't think you read my request at all. I don't care about the Windows Admin Center roles, I care about the  minimum Local Server permissions for Windows Admin Server users to connect to a Domain Controller to run the Active Directory Extension without needing to be Domain Admin

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hello Justin @Justin Grote       

Windows Admin Center supports the following end-user roles:    

    

Reference article:    

 User access options with Windows Admin Center    

Configure User Access Control and Permissions    

Best Regards    

Karlie    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
