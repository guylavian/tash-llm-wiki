---
title: "Ensuring Compliance with Active Directory for 500 Users: Licensing and Security Considerations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3888713/ensuring-compliance-with-active-directory-for-500
question_id: 3888713
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Ensuring Compliance with Active Directory for 500 Users: Licensing and Security Considerations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3888713/ensuring-compliance-with-active-directory-for-500 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, 

Could you please provide clarification regarding the following query raised by one of our customers? 

01. The customer has a total of 500 users: 250 are on-premises users, and the remaining 250 are remote users. 

02. There is a single file server located on-premises. 

03. The client wants all 500 users to be managed through Active Directory, with file server access also controlled via Active Directory. 

04. We have set up a Windows Server 2022 VM on an XCP-ng hypervisor, where Active Directory is configured. This VM is activated using an SPLA license. 

05. Does the client need any additional licenses to remain compliant while using Active Directory and the on-premises file server for 500 users, as outlined in point 1? 

06. The VM is currently behind an SDN VyOS firewall. Could you suggest any other firewall options to enhance security and manage the entire setup? Additionally, the client needs 250 certificate-based VPNs for their remote users.

Due to cost concerns, the client does not want to use Azure or AWS. 

Thank you for your assistance.

Compliments,

HJ

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-03-27*

Hi,

My name is Igor, it's a pleasure for me to help others and I'll try to help you. I am merely a fellow user trying to provide insight and information that may be helpful to others. I answer during my free time, so some delays are possible.

 It is more effective to ask such questions at Q&A forum    https://docs.microsoft.com/en-us/answers/index.... 

It is oriented to admins and corporate users, and this forum - to home users so local experts may have no corresponding knowledge, sorry.
