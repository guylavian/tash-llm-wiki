---
title: "Currently on my Domain Controller I can access to Advanced Audit Policy configurations>Audit Policies>  A severe error occurred"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278352/currently-on-my-domain-controller-i-can-access-to
question_id: 2278352
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# Currently on my Domain Controller I can access to Advanced Audit Policy configurations>Audit Policies>  A severe error occurred

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278352/currently-on-my-domain-controller-i-can-access-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon, lately when I went to my Group Policy manager on my Windows Server 2019, I go to Computer Configuration > Policies> Windows Settings > Advanced Audit Policy > Audit Policy

A severe error occurred

A severe error occurred which has caused Advanced Audit Configuration to unload. The specified domain either does not exist or could not be contacted. (Exception from HRESULT: 0x8007054B)

  at Microsoft.AuditPolicy.SnapIn.AuditPolicyGPHandlerClass.OpenAuditPolicyGPO (String bstrLdapPath)

  at Microsoft.AuditPolicy.SnapIn.GroupPolicyObject..ctor (String ldapPath

  at Microsoft.AuditPolicy.SnapIn.SnapInSettings..ctor (String ldapPath)

  at Microsoft.AuditPolicy.SnapIn.AuditPolicySnapIn.OnInitialize()

Somebody have a expering this behavior

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-26*

Hello,

   Thank you for posting question on Microsoft Windows forum!

   Based on your provided error message "The specified domain either does not exist or could not be contacted. (Exception from HRESULT: 0x8007054B)" which might indicate a problem with domain connectivity or DNS resolution when configuring advanced audit policies. You can try the following steps for finding the potential causes and solutions to the issue.

-  Checking DNS setting: Ensure the domain controller's DNS server records are correctly configured and accessible. You can use tools like nslookup to verify DNS resolution.

-  Firewall: Check for any firewalls or network restrictions that might be blocking communication between the client machine and the domain controller by running below commands   ping <domain_controller_IP> as well as its FQDN    Test-NetConnection <DC_IP> -Port 53 to verify DNS server accessibility.

-  Domain Controller Availability: Ensure the domain controller is online and accessible by running the command nltest /dsgetdc:<domain name>   

-  Netlogon Service: Restart the Netlogon service on the domain controller.    

-  In case, you use Advanced Audit Policy Configuration settings, you should enable the Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings policy setting under Local Policies\Security Options. This will prevent conflicts between similar settings by forcing basic security auditing to be ignored.      For more information https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772710(v=ws.10)?redirectedfrom=MSDN

Hope the above information is helpful!
