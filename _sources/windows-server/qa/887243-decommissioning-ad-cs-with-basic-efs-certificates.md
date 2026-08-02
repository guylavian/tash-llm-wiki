---
title: "Decommissioning AD CS with Basic EFS certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/887243/decommissioning-ad-cs-with-basic-efs-certificates
question_id: 887243
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Decommissioning AD CS with Basic EFS certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/887243/decommissioning-ad-cs-with-basic-efs-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to decommission an AD CS CA but it has Basic EFS certificates. My plan was to follow this: https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/decommission-enterprise-certification-authority-and-remove-objects    

Do we need to have users decrypt files before we revoke the EFS certificates?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-06-23*

Hello John52180627-5846,    

Thank you for posting here.    

Do we need to have users decrypt files before we revoke the EFS certificates?    

A: We should have users decrypt files before we revoke the EFS certificates.    

Reference:    

Hunting and Decrypting EFS Encrypted Files    

https://richardjgreen.net/hunting-decrypting-efs-encrypted-files/    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
