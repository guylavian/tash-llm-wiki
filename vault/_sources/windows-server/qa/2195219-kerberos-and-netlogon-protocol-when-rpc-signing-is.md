---
title: "Kerberos and Netlogon protocol when RPC signing is used instead of RPC sealing Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195219/kerberos-and-netlogon-protocol-when-rpc-signing-is
question_id: 2195219
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Kerberos and Netlogon protocol when RPC signing is used instead of RPC sealing Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195219/kerberos-and-netlogon-protocol-when-rpc-signing-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,

My Domain Controller are updated with October 2022 Security patch. And now I am planning to update domain controller with April 2023 KB5025228 security patch as per Microsoft recommendations in phase one. I know November 8, 2022, and later Windows updates address weaknesses in the Netlogon protocol when RPC signing is used instead of RPC sealing and enforcement mode will be enable with June 2023 update please guide  what could be the best approach to update the Domain controller.

Thank you !

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-14*

Hi, Based on CVE2022-38023 Netlogon RPC signing is used instead of RPC sealing addressed since July 2023. Unfortunately  my legacy storage not allowed the RPC sealing changes and users facing failed access. But need to patch the servers with out impacting the RPC singing protocol, please suggest if any way to perform.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-01*

Hello safeersaqib,  

Thank you for posting on the Microsoft Community Forum.

Suggested method for updating domain controllers:

-  Before performing domain control updates, create a complete system backup. In this way, if there are problems during the update process, you can restore to the previous state.

-  Read the updated and published documents and related information.

-  Choose a suitable time to update the domain controller and try to avoid any impact on users.

-  Ensure that the environment where the domain controller is located meets the updated requirements, such as free disk space, stable network connection, etc.

-  Install the updates in the correct order according to the steps and suggestions provided by Microsoft.

-  After the update is completed, verify that all domain related functions, features, and security are still working properly.

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou
