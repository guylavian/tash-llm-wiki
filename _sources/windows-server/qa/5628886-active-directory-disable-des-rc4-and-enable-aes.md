---
title: "Active directory: disable DES/RC4 and enable AES"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5628886/active-directory-disable-des-rc4-and-enable-aes
question_id: 5628886
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Active directory: disable DES/RC4 and enable AES

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5628886/active-directory-disable-des-rc4-and-enable-aes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For security reasons, I want to disable the risky DES/RC4 protocols and enable AES via GPO. I've been checking the events on my domain controllers and I don't find any 4769 events. Does this mean I'm ready to enable AES?  

Thanks

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-11-22*

Good morning Jaro,

I hope you are doing well. 

Have you found the answer useful? If everything is okay, don't forget to share your experience with the issue by accepting the answer. Should you need more information, free free to leave a message. Happy to help! :)

Domic Vo.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-11-19*

Hello Jaro,

The absence of Event ID 4769 doesn't indicate AES readiness; it just suggests no RC4 tickets are currently logged, possibly due to disabled auditing or no RC4 usage. Your environment is not prepared for disabling DES/RC4 until you verify that all domain-joined systems and user accounts explicitly support AES. So, check the 'msDS-SupportedEncryptionTypes' attribute on computer and user objects in Active Directory using PowerShell commands like Get-ADComputer and Get-ADUser to confirm AES-128 and AES-256 values are present. Without this, enabling AES via GPO will cause authentication failures for any asset lacking AES capability. 

I hope you're clear with the instruction. Should you have any questions, feel free to leave a message. If everything is OK, don't forget to accept the answer to share your experience with the issue and help build the community. Thank you!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-11-19*

To disable DES and RC4 protocols and enable AES in Active Directory, you should first ensure that your environment supports AES encryption. The absence of Event ID 4769 in your domain controllers indicates that there may not be any Kerberos tickets being issued with RC4 encryption, which is a positive sign. However, it does not necessarily confirm that your environment is fully ready for AES.

You should verify the following:

-  User Accounts: Ensure that the user accounts that will be using Kerberos authentication have AES attributes enabled. This can be checked in Active Directory by navigating to the user object and verifying that the options for AES 128-bit and AES 256-bit encryption are enabled.

-  Group Policy Settings: Confirm that the Group Policy Object (GPO) settings for Kerberos encryption types allow AES. This can be done by checking the policy under Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Configure encryption types allowed for Kerberos.

-  Trust Relationships: If your environment includes trusts with other domains, ensure that those trusts also support AES encryption.

Once you have confirmed these settings and that your environment is ready, you can proceed to disable DES and RC4 and enable AES encryption via GPO.

References:

-  Remove the highly insecure DES encryption from the User accounts - Microsoft Engage Center (Services Hub)

-  Linux accounts can't get AES-encrypted tickets in AD DS

-  Upgrade Domain Controllers to Windows Server 2012 R2 and Windows Server 2012

-  Disable the AllowNT4Crypto setting on all affected domain controllers
