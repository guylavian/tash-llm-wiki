---
title: "Domain Controller Group Policy has Red \"x\" on audit policy settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/293317/domain-controller-group-policy-has-red-x-on-audit
question_id: 293317
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controller Group Policy has Red "x" on audit policy settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/293317/domain-controller-group-policy-has-red-x-on-audit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have auditing for Logon events enabled on my Domain Controller Group policy. But, when I run RSOP.msc I see red "X"s on all the audit policies. If I look at properties on the logon event, then look as the precedence tab, I see this error "The policy engine did not attempt to configure the setting. For more information, see %windir%\security\logs\winlogon.log on the target machine." I looked at this directory on the DC, but it doesn't exist. There are no logon events being logged by the DCs either. How can I troubleshoot this issue? Thanks! ![73027-image.png][1] [1]: /api/attachments/73027-image.png?platform=QnA

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-02*

Hi,    

This issue occurs if the "Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" policy setting is enabled in Windows Vista or in Windows Server 2008. The policy setting can be enabled by using Group Policy or it can be enabled manually by modifying the registry.    

To resolve this issue, use one of the following methods, as appropriate for your situation.    

    

For more information , you can refer to :    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/windows-security/security-auditing-settings-not-applied-when-deploy-domain-based-policy    

Similar case for your reference:    

https://social.technet.microsoft.com/Forums/lync/en-US/fde42cfc-bb74-4e11-8b60-c1a3cb5d80ed/rsop-the-policy-engine-did-not-attempt-to-configure-the-setting?forum=winserverGP
