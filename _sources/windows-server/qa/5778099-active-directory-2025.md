---
title: "Active Directory  2025"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5778099/active-directory-2025
question_id: 5778099
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-system-management-components"]
answer_author_roles: ["Independent Advisor"]
---
# Active Directory  2025

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5778099/active-directory-2025 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I would like to ask about Active Directory Domain Services (AD DS) on Windows Server 2025.

If domain-joined client computers are running different Windows versions and builds (for example Windows 10 1903–22H2 and multiple Windows 11 versions), can this cause inconsistent Group Policy behavior?

In my environment, some computers successfully apply Group Policies, while others do not, even though they are in the same OU.

Does the difference in Windows client versions/builds affect Group Policy processing, compatibility, or policy application?

Thank you.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-02-17*

Hello WIND_AM,

Thank you for posting question on Microsoft Windows Forum!

Based on your query of  whether difference in Windows client versions/builds affecting Group Policy processing, compatibility, or policy application. 

While Active Directory is designed to be backward compatible, the mix of Windows 10 (especially older builds like 1903) and Windows 11 creates several layers of potential inconsistency in how Group Policy Objects (GPOs) are processed and applied.

Administrative Template (ADMX) Discrepancies might be considered to be the main suspect here. GPOs rely on ADMX files to define which registry keys should be changed. Windows 11 introduces new settings that simply do not exist in Windows 10 1903. If you configure a policy using the Windows 11 ADMX templates, an older Windows 10 machine may see that setting as "Extra Registry Settings" or ignore it entirely because it does not have the corresponding client-side extension to handle it. On the other hand, Windows Server 2025 and recent Windows 11 builds have hardened security defaults that older versions (like Windows 10 1903) do not share. Newer versions of Windows might require SMB signing by default. If a legacy client has a different security handshake requirement, it might fail to even read the GPO files from the SYSVOL share.

Another point worth mentioning here is some policies require client-side extensions (CSEs) that must exist and be working on the client. If a CSE is missing, broken, or behaves differently between OS builds, that class of settings will apply on those machines. The Group Policy engine invokes CSEs on the client to do the work.

The following articles are useful for your further reference regarding your concerns.

-  https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/client-side-processing-of-group-policy

-  https://learn.microsoft.com/en-us/windows/client-management/understanding-admx-backed-policies

Hope the above information is helpful! If it helps you getting more insight into the issue, it is appreciated to accept the answer. Should you have more questions, feel free to leave a message.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-02-17*

Inconsistent Group Policy behavior can indeed occur when domain-joined client computers are running different Windows versions and builds. Each version of Windows may have variations in how Group Policy is processed and applied, which can lead to discrepancies in policy application across different machines, even if they are in the same Organizational Unit (OU).

Group Policy processing is designed to be cumulative and inherited, but differences in client versions can affect compatibility and the specific settings that are available or applicable. For instance, certain Group Policy settings may not be supported or behave differently on older versions of Windows compared to newer ones. This can result in some computers successfully applying Group Policies while others do not, depending on their Windows version and build.

To mitigate these issues, it's essential to ensure that all client machines are running compatible versions of Windows that support the Group Policy settings you intend to apply. Regular updates and maintaining a consistent environment can help reduce the likelihood of inconsistent behavior.

References:

-  Group Policy overview for Windows Server

-  Group Policy processing
