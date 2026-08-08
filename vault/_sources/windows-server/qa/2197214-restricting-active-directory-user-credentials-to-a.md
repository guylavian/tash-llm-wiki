---
title: "Restricting Active Directory user credentials to a particular group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197214/restricting-active-directory-user-credentials-to-a
question_id: 2197214
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# Restricting Active Directory user credentials to a particular group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197214/restricting-active-directory-user-credentials-to-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts 

I am using Windows Server 2022 RADIUS server as external Authentication server with our  wiFi cNMS. There are two SSIDs with WPA2/EAP authentication for two different groups Alpha and Beeta

I have created various users in Active Directory.

My intention  is to restrict users to their dedicated group only. i.e the users created for group Alpha should not be able to connect with  the SSID meant for group Beeta with their credentials

Kindly let me know if their is a way

Regards

Avanindra Kumar Mishra

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-02*

Sure! To restrict Active Directory user credentials to specific groups for Wi-Fi access, you can utilize group-based access control. Ensure that each user is assigned to their respective group (Alpha or Beeta) in Active Directory. Then, configure RADIUS server policies to allow access based on group membership. This way, users will only be able to connect to the SSID designated for their group.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-02*

Thanks Rosy

It works perfectly

Regrds

Avanindra K Mishra

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-26*

You're welcome! If you have any further questions, feel free to contact us anytime. We're glad to help and you can mark this as the answer. Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-26*

Thanks a lot, it is working

Regards

Avanindra K Mishra
