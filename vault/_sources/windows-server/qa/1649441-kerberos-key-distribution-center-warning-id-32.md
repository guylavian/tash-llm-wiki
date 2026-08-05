---
title: "Kerberos-Key-Distribution-Center warning ID 32"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1649441/kerberos-key-distribution-center-warning-id-32
question_id: 1649441
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos-Key-Distribution-Center warning ID 32

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1649441/kerberos-key-distribution-center-warning-id-32 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

Our DC will have a warning 32 on the Kerberos-Key-Distribution-Center:

`The Key Distribution Center (KDC) uses a certificate without KDC Extended Key Usage (EKU) which can result in authentication failures for device certificate logon and smart card logon from non-domain-joined devices. Enrollment of a KDC certificate with KDC EKU (Kerberos Authentication template) is required to remove this warning.`

Our device didn't use smartcard or device certificate to login, any idea?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-09*

Hello Chong,  

Thank you for posting in Q&A forum.  

How many Domain Controllers are there in your domain? Do you see the same event ID on all the DCs in your domain?

Please check if you have an internal Windows CA server in your domain? If so, you can check if there is KDC certificate in Certificates - Local Computer\Personal store.

If you have Windows CA and there is such certificate (issued using Kerberos Authentication certificate template) on DC, you can try to request such Kerberos certificate on DC, then check if there is still this warning on DC.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
