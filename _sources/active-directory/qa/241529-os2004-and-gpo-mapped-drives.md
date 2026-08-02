---
title: "OS2004 and GPO Mapped Drives"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/241529/os2004-and-gpo-mapped-drives
question_id: 241529
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OS2004 and GPO Mapped Drives

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/241529/os2004-and-gpo-mapped-drives (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Has anyone figured out GPO settings on 2004 to get our preferred mapped drives to connect on sign-on/startup?  

We haven't gone to 2004 solely because users cannot see the two mapped drives that all users need when signing on.  

This GPO has worked in all other OS's up to 2004, so we are hanging on to 1909 because of this.  

Any help would be greatly appreciated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-25*

Hi,    

Thanks for sharing here!    

Based on my understanding, it is a user configuration , for the GPO security scope, the computers should also have the read permission.    

You can run the gpresult /h report command to check if here are any errors .    

Also, try to access the shared folder by :\servername\shared folder, will it be success?    

If it was not related to the GPO configuration , please refer to the following link , hope it will helpful:    

https://answers.microsoft.com/en-us/windows/forum/windows_10-networking/after-updating-to-windows-10-v2004-cannot-map/cf7eeb62-f794-465c-8693-7e543a907dae?auth=1    

https://learn.microsoft.com/en-us/answers/questions/65556/windows-10-version-2004-mapped-drive-issue.html    

https://learn.microsoft.com/en-us/answers/questions/87133/error-on-map-network-drives-build-2004.html    

Best Regards,
