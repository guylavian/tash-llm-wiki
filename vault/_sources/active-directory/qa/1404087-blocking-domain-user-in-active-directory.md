---
title: "Blocking domain user in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1404087/blocking-domain-user-in-active-directory
question_id: 1404087
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Blocking domain user in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1404087/blocking-domain-user-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have a problem with a user blocked by the domain. Every time the user goes to sleep due to inactivity and wakes up, I enter the password of the account connected to AD, it automatically locks the account, and when the user logs out and logs in again, the account is not blocked. The user enters the password correctly, has access to the Internet and receives the appropriate address, password reset did not help. Does anyone know why this is happening?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-02*

Hello NAKAYAMA Takashi,

Thank you for posting in Q&A forum.

I enter the password of the account connected to AD, it automatically locks the account,  

A: Please confirm if the AD account is actually locked out. In such case, did you unlock the account for this AD account?  

If the problem occurs on multiple AD users or multiple AD machines.  

If this account is locked actually.  

1.Check if you can see multiple Event ID 4771(Kerberos authentication) or 4776 (NTLM authentication) via Security log on DC/PDC.  

2.Check if you can see Event ID 4740 via Security log on DC/PDC.

3.Find the locked account, and for this domain user account, if you can see Event ID 4771 or 4776 and Event ID 4740 related this domain account, can you see which machine lock the user account via 4776 or 4740?

If so, logon the machine locked out this account to try to check the reason.

• Check Credential Management to see if the user's old credentials are cached (Control Panel)

• Check whether the network disk is mounted with the wrong password

• Check if the user started the service with the wrong password, run scheduled tasks, etc

• Are there other third-party programs that cache incorrect passwords for users  

• Other apps or programs that remembered or cached the wrong credential for users.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
