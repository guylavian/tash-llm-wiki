---
title: "Change to Kerberos Encryption for Active Directory : RC4 to AES"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5845233/change-to-kerberos-encryption-for-active-directory
question_id: 5845233
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Change to Kerberos Encryption for Active Directory : RC4 to AES

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5845233/change-to-kerberos-encryption-for-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I am looking for information regarding the issue "Change to Kerberos Encryption for Active Directory : RC4 to AES"

We are using AD managed services and MS will deploy the patch on the domain controllers. I am wondering what patches must the WIndows clients and servers need to that the authentication work seamlessly ?

Thank you for your help

Regards

Bernard

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2026-03-31*

Hi BernardP,

While Windows operating systems have natively supported AES encryption for many years, you must ensure all clients and member servers have at least the November 2022 cumulative updates installed. These specific patches address vulnerabilities in how Kerberos handles Privilege Attribute Certificate signatures and are required for seamless authentication when your domain controllers are patched and configured to reject RC4. As long as your machines are up to date with these or any newer standard cumulative updates, no separate, standalone patch is required to make the transition work.

The transition to AES relies heavily on your environment configurations. You need to verify that your Group Policy settings explicitly allow AES. Navigating to Computer Configuration, Windows Settings, Security Settings, Local Policies, and Security Options, you must ensure the policy for configuring allowed Kerberos encryption types has both AES128_HMAC_SHA1 and AES256_HMAC_SHA1 enabled. In the Windows Registry, this correlates to the SupportedEncryptionTypes DWORD located at HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters, which should ideally be set to a value like 2147483640 to ensure modern encryption is supported.

You must also audit your Active Directory service accounts before the domain controllers enforce the new restrictions. The msDS-SupportedEncryptionTypes attribute dictates the ciphers an account can negotiate, and any legacy accounts hardcoded only for RC4 will experience immediate authentication failures. To identify which systems or applications are still relying on older encryption, you should actively monitor your domain controller logs for Security Event ID 4769. Filtering these events for a ticket encryption type of 0x17 will reveal exactly which accounts are requesting RC4 tickets, giving you time to update their attributes or configurations to AES before the patch deployment finalizes.

Hope this answer brought you some useful information. If it did, please hit “accept answer”. Should you have any questions, feel free to leave a comment.

VP

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-31*

For seamless Kerberos authentication when moving from RC4 to AES on domain controllers, all participating devices (domain controllers, member servers, and Windows clients) must share at least one common Kerberos encryption type.

Key points from the current changes:

-  Domain controller behavior after the updates

-  Updates released on or after November 8, 2022 change how domain controllers choose encryption types.

-  Domain controllers now strictly honor:

-  The `msds-SupportedEncryptionTypes` attribute on accounts, and

-  The `DefaultDomainSupportedEncTypes` registry value on the DCs.

-  If `msds-SupportedEncryptionTypes` is not set or is 0, the DC assumes a default of `0x27` (DES, RC4, AES session keys) or uses the `DefaultDomainSupportedEncTypes` registry value.

-  Recommended configuration on domain controllers

-  The `DefaultDomainSupportedEncTypes` registry key is under:

-  `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\KDC`

-  Default value: `0x27` (DES, RC4, AES session keys).

-  For stronger security, the recommendation is:

-  `0x3C` to allow AES-encrypted tickets and AES session keys, or

-  `0x38` for AES-only environments where RC4 is not used.

-  Requirements for Windows clients and member servers

-  Windows computers automatically set their own `msds-SupportedEncryptionTypes` based on the local policy “Network security: Configure encryption types allowed for Kerberos”.

-  To ensure seamless authentication when DCs prefer AES over RC4:

-  Ensure supported Windows versions are fully updated so they support AES-SHA1.

-  Configure the Kerberos encryption types on clients/servers to include AES (for example via the security policy mentioned above).

-  No special “extra” patch beyond normal security/quality updates is required on clients, but they must:

-  Support AES-SHA1, and

-  Be configured to allow AES in their Kerberos encryption types.

-  Accounts that do not auto-configure encryption types

-  User accounts, group managed service accounts, and other non-computer accounts do not automatically get `msds-SupportedEncryptionTypes` set.

-  For these accounts, domain controllers fall back to `DefaultDomainSupportedEncTypes` unless `msds-SupportedEncryptionTypes` is explicitly configured.

-  If moving to AES-only or AES-preferred, ensure that:

-  `DefaultDomainSupportedEncTypes` includes AES, and

-  Any accounts with explicitly set `msds-SupportedEncryptionTypes` also include AES.

-  How to verify and detect issues

-  First step to prepare the environment is to verify that all devices share a common Kerberos encryption type.

-  After installing the DC updates, devices that do not share a common encryption type can be detected by:

-  Checking the Event Log on domain controllers for `Microsoft-Windows-Kerberos-Key-Distribution-Center` Event ID 27, which indicates disjoint encryption types between clients and servers/services.

-  RC4 deprecation and future changes

-  RC4 is being phased out due to security risks (for example, Kerberoasting attacks).

-  Microsoft plans to disable RC4 as the default assumed supported encryption type for AD domain controllers by the end of Q2 2026.

-  Guidance for preparing for RC4 disablement and detecting/remediating RC4 usage is provided in:

-  “Detect and remediate RC4 usage in Kerberos”.

-  “How to manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833”.

Practical summary for clients/servers:

-  Keep all Windows clients and servers on supported versions with current security updates.

-  Ensure their Kerberos policy allows AES (and RC4 only if still required for legacy interoperability).

-  On domain controllers, configure `DefaultDomainSupportedEncTypes` to a value that includes AES (preferably `0x3C` or `0x38`), and verify that no account has an incompatible `msds-SupportedEncryptionTypes`.

-  Use Event ID 27 on DCs to identify any devices that cannot negotiate a common encryption type after the DC patches are deployed.

References:

-  KB5021131: How to manage the Kerberos protocol changes related to CVE-2022-37966

-  Detect and remediate RC4 usage in Kerberos

-  How to manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833
