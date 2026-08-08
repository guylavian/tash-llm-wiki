---
title: "The new ActiveSync mobile device has not been quarantined by Exchange 2019 CU12 and is not visible in the user's mailbox."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166119/the-new-activesync-mobile-device-has-not-been-quar
question_id: 1166119
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# The new ActiveSync mobile device has not been quarantined by Exchange 2019 CU12 and is not visible in the user's mailbox.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166119/the-new-activesync-mobile-device-has-not-been-quar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody!

We have a policy set up on Exchange 2019 CU12- All new ActiveSync mobile devices, or when re-registering an existing account on the source devices, add the device to quarantine and send a message to the helpplesk group that appruvate the account on the mobile device.

This morning, the user was setting up mail on a newly purchased new ActiveSync mobile device (at the same time, he did not delete his account on the old mobile device, but simply deleted the mail client).

But, for some reason, the new mobile device connected to the mail server and was not quarantined, and moreover, this mobile device is not visible in the user's mailbox, and the old device remained in the mailbox.

But the main question is how could it happen that a new mobile device with the same account was not quarantined and immediately connected to the mail without being displayed in the user's mailbox?

A small detail is the head of the helpdesk and he has a group with a couple of ways to appruve himself - but still I don't see this device in his mailbox and he didn't appruve himself.

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-24*

Hello All
We have added a mobile device to a mailbox, and it appears under 'Mobile Devices' within the mailbox. For testing purposes, I deleted the mobile device from the mailbox and then reconfigured it on the same mobile device. The configuration is working fine on the mobile, and the user can send and receive emails on this device. However, this device is not visible under the 'Mobile Devices' section of the mailbox; it's showing as if there are no devices associated with the mailbox

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi @Cobion ,

Do you set Device Access Rules here?

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
