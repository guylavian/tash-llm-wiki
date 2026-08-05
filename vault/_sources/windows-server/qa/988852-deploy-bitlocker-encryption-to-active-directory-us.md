---
title: "Deploy Bitlocker encryption to active directory Users with GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/988852/deploy-bitlocker-encryption-to-active-directory-us
question_id: 988852
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Deploy Bitlocker encryption to active directory Users with GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/988852/deploy-bitlocker-encryption-to-active-directory-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am trying to deploy bitlocker encryption automatically to active directory users through GPO. The users must have TPM enabled and it should be hardware based bitlocker encryption. I also don't want any pre boot authentication(bitlocker password). I only want to encrypt the drives of the users and the recovery key must be asked when the storage is removed and attached to other devices. It would be very helpful if anyone can Guide me to automate the encryption in GPO. Thank you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-31*

Hi Arun,    

How about Out of the box experience and enabling the Bitlocker? oem-bitlocker There are pre-reqs and some steps to enable this check the link.    

=    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-31*

Hi,    

I think you can acheive this via GPO and also you will need to test this one a device before you rollout to all the users, best practice is to test on a device, backup the recovery keys and try to decrypt the process.    

bitlocker-group-policy-settings    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
