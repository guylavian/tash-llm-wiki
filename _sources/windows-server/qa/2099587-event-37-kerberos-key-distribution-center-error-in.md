---
title: "Event 37 - Kerberos-Key-distribution-Center error in Windows Server 2022 DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2099587/event-37-kerberos-key-distribution-center-error-in
question_id: 2099587
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Event 37 - Kerberos-Key-distribution-Center error in Windows Server 2022 DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2099587/event-37-kerberos-key-distribution-center-error-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Our domain is Win2008R2 and just promo 2 x Win2022 DC into our AD environment. We checked all DCs replication is OK and plan to remove Win2008 DC from the AD. However, we found both Win2022 DCs have many KDC error 37. 

Seems it have a patch "https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041 " for this error. But we installed the latest patch on the DC already. It still has many 37 error.

Any impact of this error and how can I fix it? 

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-09*

Hello

Thank you for posting in Q&A forum.

Here are the Known issues about event 37. you can try to install patch to fixed it, if not see event ID 37 after a week. It means your environment is fine.

Symptom After installing Windows updates released November 9, 2021, or later on domain controllers (DCs), some customers might see the new audit Event ID 37 logged after certain password setting or change operations such as:

-  Update or Repair failover cluster's CNO or VCO

-  Reset a user's password from the Active Directory Users and Computers (dsa.msc) console

-  Create a new user from the Active Directory Users and Computers (dsa.msc) console

-  Change password for third-party, domain-joined devices

If you do not see Event ID 37 after installing Windows updates released November 9, 2021, or later for a week and PacRequestorEnforcement is either ‘1’ or ‘2’, then your environment is not affected. If you set PacRequestorEnforcement = 1, Event ID 37 is logged as a warning, but password change requests will succeed and will not affect users. If you set PacRequestorEnforcement = 2, password change requests will fail and will cause the operations listed above to also fail. This issue has been addressed in the following updates:

Workaround

-  Windows 11 - KB5011563

-  Windows Server 2022 - KB5011558

-  Windows 10, version 20H2, Windows 10 version 21H1, and Windows 10, version 21H2 - KB5011543

-  Windows 10, version 1809 and Windows Server 2019 - KB5011551

-  Windows 10, version 1607 and Windows Server 2016 - KB5012596

-  Windows Server 2012 R2 - KB5012670

-  Windows Server 2012 - KB5012666

-  Windows Server 2008 R2 - KB5012649

-  Windows Server 2008 SP2 - KB5012632

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-09*

Hello

Thank you for posting in Q&A forum.

Here are the Known issues about event 37. you can try to install patch to fixed it, if not see event ID 37 after a week. It means your environment is fine.

Symptom After installing Windows updates released November 9, 2021, or later on domain controllers (DCs), some customers might see the new audit Event ID 37 logged after certain password setting or change operations such as:

-  Update or Repair failover cluster's CNO or VCO

-  Reset a user's password from the Active Directory Users and Computers (dsa.msc) console

-  Create a new user from the Active Directory Users and Computers (dsa.msc) console

-  Change password for third-party, domain-joined devices

If you do not see Event ID 37 after installing Windows updates released November 9, 2021, or later for a week and PacRequestorEnforcement is either ‘1’ or ‘2’, then your environment is not affected. If you set PacRequestorEnforcement = 1, Event ID 37 is logged as a warning, but password change requests will succeed and will not affect users. If you set PacRequestorEnforcement = 2, password change requests will fail and will cause the operations listed above to also fail. This issue has been addressed in the following updates:

Workaround

-  Windows 11 - KB5011563

-  Windows Server 2022 - KB5011558

-  Windows 10, version 20H2, Windows 10 version 21H1, and Windows 10, version 21H2 - KB5011543

-  Windows 10, version 1809 and Windows Server 2019 - KB5011551

-  Windows 10, version 1607 and Windows Server 2016 - KB5012596

-  Windows Server 2012 R2 - KB5012670

-  Windows Server 2012 - KB5012666

-  Windows Server 2008 R2 - KB5012649

-  Windows Server 2008 SP2 - KB5012632

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it.
