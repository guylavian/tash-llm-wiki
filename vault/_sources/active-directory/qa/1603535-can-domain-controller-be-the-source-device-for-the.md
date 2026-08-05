---
title: "Can domain controller be the source device for the account locked out?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1603535/can-domain-controller-be-the-source-device-for-the
question_id: 1603535
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can domain controller be the source device for the account locked out?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1603535/can-domain-controller-be-the-source-device-for-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can domain controller be the source device for the account locked out?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-04*

Hello Kunal Kant Sahu,

Thank you for posting in Q&A forum.       

Yes, a domain controller can be the source device for an account lockout. This typically occurs when there are multiple failed authentication attempts on the domain controller itself, either due to incorrect password entry or multiple failed logon attempts. When this happens, the domain controller logs the relevant account lockout details under Event ID 4740 under the "Security" log under the Event Viewer.

If you are unable to see event ID 4740 on the domain controller. You need to enable the audit policy on the DC. “Enable Audit Account Lockout”, “Audit Login”, “Audit Logout Policy”, under “Computer Configuration” – “Policies” – “Windows Settings” – “Security Settings” – “Advanced Audit Policies” – “Login/Logout”. Also enable "Audit Account Management" in the "Account Management" section: Success. I hope the information above is helpful. If you have any question or concern, please feel free to let us know. Best Regards, Yanhong Liu 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-29*

Hi @Kunal Kant Sahu  

Yes it can. You should find the source on the event viewer on domain controller where the user has been locked.

In some cases , when the source is not windows machine (proxy , network equipement , appliance ..ect) it's possible to see also the IP of domain controller or nothing in the event viewer.

Please don't forget to accept helpful answer
