---
title: "Detect and remediate RC4 usage in Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5765900/detect-and-remediate-rc4-usage-in-kerberos
question_id: 5765900
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Detect and remediate RC4 usage in Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5765900/detect-and-remediate-rc4-usage-in-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

Scenario: server with Windows Server 2022 STD (domain controller) 

Computers with windows 11 Pro.

I've been analyzing the system logs and in the security logs I found entries: 

Event ID 4768, which is for the requested Kerberos authentication ticket (TGT). 

Event ID 4769, which is for the requested Kerberos service ticket. 

I cleared the security log.

I logged into the server with my administrator account and found entries 4768 and 4769. 

I assume the result will be identical next Monday when users log into their domain accounts on their computers. 

Although I have read various articles on this subject, and because I am technically hesitant to implement what I have read, I ask you to clarify me,  what I should actually do in the  windows server 2022 domain controller and on the PCs (Windows 11 Pro).

Thanks in advence

Best Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2026-02-07*

To address RC4 usage in your Windows Server 2022 domain controller and Windows 11 Pro PCs, you should follow these steps:

-  Audit RC4 Usage: Since you've already identified Event IDs 4768 and 4769 in the security logs, continue monitoring these events to check for RC4 usage. You can use PowerShell scripts like `List-AccountKeys.ps1` and `Get-KerbEncryptionUsage.ps1` to help automate this process and identify which encryption types are being used.

-  Limit or Disable RC4 Usage: If you want to reduce or eliminate RC4 usage, you can create a Group Policy Object (GPO) to configure the allowed encryption types for Kerberos. Here’s how to do it:

-  Open the Group Policy Management Console.

-  Create a new GPO and edit it.

-  Navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options.

-  Find the policy setting Network security: Configure encryption types allowed for Kerberos and specify the desired encryption types (e.g., only allow AES-SHA1).

-  Apply the GPO to the appropriate Organizational Units (OUs) or groups.

-  Monitor Authentication Events: After applying the GPO, monitor authentication events to ensure that no unexpected failures occur. You can continue using the PowerShell scripts to verify that RC4 is no longer being used.

-  Identify Authentication Failures: If you disable RC4, be prepared to identify any authentication failures. Look for Event ID 4769 with error code `0xE`, which indicates that the encryption type is not supported. This will help you troubleshoot any issues that arise after the changes.

By following these steps, you can effectively manage and remediate RC4 usage in your environment.

References:

-  Detect and remediate RC4 usage in Kerberos

-  Detect and remediate RC4 usage in Kerberos
