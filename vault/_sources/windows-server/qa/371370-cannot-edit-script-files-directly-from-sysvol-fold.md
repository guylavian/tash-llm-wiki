---
title: "Cannot edit script files directly from SYSVOL folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/371370/cannot-edit-script-files-directly-from-sysvol-fold
question_id: 371370
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Cannot edit script files directly from SYSVOL folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/371370/cannot-edit-script-files-directly-from-sysvol-fold (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We recently changed our PDC and when we access the scripts folder under SYSVOL using a domain admin account, whenever we try to change a script we are getting Access Denied error.  

I have given Domain Admins group full permissions + ownership but problem persists. We did not use to have such problem using old DC server before.  

To be fair we are able to launch Notepad as admin and open a batch file and be able to edit but its more convenient for us if we are able to do it directly.   

Will await your replies. Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-27*

Hi,  

Before going further, would you please tell how many DCs do you have?  

Did all of them have the same issue?  

When you check the permission on the sysvol folder, did you confirm the share permission?  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-26*

Might try run as admin `cmd.exe` then from this elevated session start notepad.exe  

--please don't forget to Accept as answer if the reply is helpful--
