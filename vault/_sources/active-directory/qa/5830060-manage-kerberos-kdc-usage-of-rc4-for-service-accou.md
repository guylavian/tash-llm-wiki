---
title: "manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5830060/manage-kerberos-kdc-usage-of-rc4-for-service-accou
question_id: 5830060
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5830060/manage-kerberos-kdc-usage-of-rc4-for-service-accou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

We came to know there is a enforcement comes for the rc4 kerberos , and AES will be enforced form April. We noticed if we create the registry key RC4DefaultDisablementPhase.  it will postpone the till july and wont disable rc4.  but his registry key require reboot and we have more domain controllers and downtime window is not there now. So if we deplyo the key now and when the april patch is pushed and rebooted will the registry key takes effect or it wont?

Also after the audit review how the apps team will mitigate from their end?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-20*

Hi SAGA,

Yes, if you set the `RC4DefaultDisablementPhase` registry key before April, it will still take effect after the April patch once the domain controller is rebooted. The enforcement only applies after restart, so the key will successfully postpone RC4 disablement until July. The key must be placed under `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters` and present before the patch is applied.

For the applications side, mitigation means they must stop relying on RC4 and move to AES. That requires updating service accounts and applications so their Kerberos accounts have `msDS-SupportedEncryptionTypes` set to include AES128 and AES256. Legacy systems or appliances that cannot negotiate AES will need vendor updates or reconfiguration. In short, your registry key buys time until July, but the apps team must ensure Kerberos tickets are issued with AES before the grace period ends.

Reference link: https://support.microsoft.com/en-us/topic/how-to-manage-kerberos-kdc-usage-of-rc4-for-service-account-ticket-issuance-changes-related-to-cve-2026-20833-1ebcda33-720a-4da8-93c1-b0496e1910dc

I hope you found something helpful here. If it does help to explain your question, please accept the answer, or give it a thump up to encourage my contribution. Thank you.

Harry.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-20*

The RC4DefaultDisablementPhase registry value is only read by the KDC service after the January 13, 2026 (or later) updates are installed and the domain controller is restarted. A restart is required for the setting to take effect.

Behavior from the documentation:

-  The registry key is introduced and used to gate the deployment of the Kerberos changes after the January 13, 2026 updates are installed.

-  Location: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters`

-  Value name: `RC4DefaultDisablementPhase` (REG_DWORD)

-  Values:

-  0 – No audit, no change

-  1 – Warning events logged on default RC4 usage (Phase 1 default)

-  2 – Kerberos assumes RC4 is not enabled by default (Phase 2 default)

-  “Restart required? Yes” – the KDC must be restarted (normally via OS reboot) for any change to this value to apply.

Given that:

-  If the registry value is deployed now but the domain controllers are not restarted, the setting will not be active yet.

-  When the April update is later installed and the domain controller is then rebooted, the KDC will read the existing RC4DefaultDisablementPhase value at that time.

-  Therefore, if RC4DefaultDisablementPhase is already set (for example, to 1) before the first reboot after the April update, that configured value will take effect after that reboot and will control behavior instead of the default phase for that DC.

So, deploying the registry key in advance is effective as long as the value is present before the first reboot after installing the April (or later) updates. The behavior (including postponing enforcement as documented for the configured phase) will begin only after that reboot when the KDC reads the key.

References:

-  How to manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833
