---
title: "Domain controller: LDAP server channel binding token requirements' is set to 'Always' (DC Only)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2073529/domain-controller-ldap-server-channel-binding-toke
question_id: 2073529
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controller: LDAP server channel binding token requirements' is set to 'Always' (DC Only)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2073529/domain-controller-ldap-server-channel-binding-toke (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working on vulnerability issues related to the Domain Controller. The LDAP server channel binding token requirements were set to 'Always' (DC Only).

To analyze the issue, I changed the setting to 'When Supported' instead of 'Always'. Additionally, I enabled the following settings to generate more logs for auditing.

Via GPO:

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Domain controller: LDAP server channel binding token requirements – Set to 'When Supported'

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Restrict NTLM: Audit Incoming NTLM Traffic – Set to 'Enable auditing for all accounts'

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers – Set to 'Audit all'

Manually set the following registry settings and rebooted the server:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Diagnostics /v "16 LDAP Interface Events" /t REG_DWORD /d 2`

`HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\Parameters`

-  Value Name: `LogLevel`

-  Value Type: `REG_DWORD`

-  Value: `1`

However, none of the expected events (3039, 3040, 3041, 2886, 2887, 2888, 2889) are being generated.

Kindly advise. Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-20*

Hello

Thank you for posting in Q&A forum.

For enable event 3039 3040 3041 2886 2887 2888 2889, if policy has been set, you can check if registry value at client side is correct as below link shows:

The mapping between LDAP Signing Policy settings and registry settings are included as follows:

-  Policy Setting: "Domain controller: LDAP server signing requirements"

-  Registry Setting: LDAPServerIntegrity

-  DataType: DWORD

-  Registry Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters

The mapping between LDAP Channel Binding Policy settings and registry settings are included as follows:

-  Policy Setting: "Domain controller: LDAP server channel binding token requirements"

-  Registry Setting: LdapEnforceChannelBinding

-  DataType: DWORD

-  Registry Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters  

2020, 2023, and 2024 LDAP channel binding and LDAP signing requirements for Windows (KB4520412) - Microsoft Support

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it.
