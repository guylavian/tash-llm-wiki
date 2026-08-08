---
title: "Active Directory Mail-enabled Security group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/375640/active-directory-mail-enabled-security-group
question_id: 375640
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Mail-enabled Security group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/375640/active-directory-mail-enabled-security-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way from me to populate ADUser Attribute (Company ) for the members of a security group using powershell.   

Thanks,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-29*

Hi,    

You can try this    

```
Get-ADGroupMember $group | Set-ADUser -Company "ABC"
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-28*

this is what i'm working with:   

get-ADGroup " GroupName" | sort -property Company | foreach { set-ADUser $_ -Company ABC}.  

Is that correct?
