---
title: "Active Directory Lightweight Directory Services could not be initialized. 1811 JET_errFileNotFound, File not found"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357275/active-directory-lightweight-directory-services-co
question_id: 357275
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Lightweight Directory Services could not be initialized. 1811 JET_errFileNotFound, File not found

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357275/active-directory-lightweight-directory-services-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI ,  

ADAM instance cannot be restarted after windows reboot and below error is observed in Logs  

Active Directory Lightweight Directory Services could not be initialized.   

The directory service cannot recover from this error.   

User Action   

Restore the local directory service from backup media.   

Additional Data   

Error value:  

-1811 JET_errFileNotFound, File not found  

Thanks for any help

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-16*

Hi ,  

I have followed above steps mentioned in my previous comment and able to resolve it.  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-15*

Hi,    

Would you please tell more information about the restore operation?    

Did the backup a system backup or full server backup?    

How may DCs do you have? Were all of them failed?    

If you still have good DCs in your domain, it is not suggested to restore the DC from backup.    

You can consider demote the problematic one from domain, and then promote again (with a different name and IP address ).    

If you can't demote it successfully, you can perform a metadata cleanup:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

Best Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-15*

Hi ,  

Noticed that adamntds.dit file is missing after 2016 server reboot !  

I have a backup of 3 days old  but that was taken before seizing the schema master to new servers.  

Now if i restore this backup , should i have old servers running because schema master is old server on that backup   

Thanks
