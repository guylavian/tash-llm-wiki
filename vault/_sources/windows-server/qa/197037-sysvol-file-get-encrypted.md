---
title: "SYSVOL file get Encrypted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197037/sysvol-file-get-encrypted
question_id: 197037
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SYSVOL file get Encrypted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197037/sysvol-file-get-encrypted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Expert , We have faced ransomware attack , it encrypted out SysVol folder and File on Active Directory Server ( Windows Server 2012 Standard), is there any recovery option in which we can only restore SysVol folder and file as other folders are working fine. Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

we have three DC . one primary , two secondary.  

all sysvol folder are encrypted.  

we have system state backup of DC.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-14*

Hi,  

Before going further, would you please confirm the following questions ?  

How many DCs do you have ? All the sysvol folder on all the DCs have been encrypted, right?  

Did you back up the DCs?  

If you have backup for the DC, i would recommend you delete the sysvol folder , and restore the sysvol folder  from the backup.(Copy the sysvol folder from the backup)  

Best Regards,
