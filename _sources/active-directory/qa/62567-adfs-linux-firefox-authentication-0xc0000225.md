---
title: "ADFS - Linux Firefox authentication - 0xC0000225"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/62567/adfs-linux-firefox-authentication-0xc0000225
question_id: 62567
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS - Linux Firefox authentication - 0xC0000225

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/62567/adfs-linux-firefox-authentication-0xc0000225 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm facing an issue related only to Firefox client on Linux OS when they authenticate on the ADFS (NTLM protocol).

Issue happens since server were restarted.

When they try to authenticate using Firefox on Linux, I see following authentication result :

```
An account failed to log on.

    Subject:
        Security ID:        NULL SID
        Account Name:       -
        Account Domain:     -
        Logon ID:       0x0

    Logon Type:         3

    Account For Which Logon Failed:
        Security ID:        NULL SID
        Account Name:       (here user samaccountname or UPN)
        Account Domain:     

    Failure Information:
        Failure Reason:     An Error occured during Logon.
        Status:         0xC0000225
        Sub Status:     0x0

    Process Information:
        Caller Process ID:  0x0
        Caller Process Name:    -

    Network Information:
        Workstation Name:   WORKSTATION
        Source Network Address: -
        Source Port:        -

    Detailed Authentication Information:
        Logon Process:      
        Authentication Package: NTLM
        Transited Services: -
        Package Name (NTLM only):   -
        Key Length:     0

    This event is generated when a logon request fails. It is generated on the computer where access was attempted.

    The Subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.

    The Logon Type field indicates the kind of logon that was requested. The most common types are 2 (interactive) and 3 (network).

    The Process Information fields indicate which account and process on the system requested the logon.

    The Network Information fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.

    The authentication information fields provide detailed information about this specific logon request.
        - Transited services indicate which intermediate services have participated in this logon request.
        - Package name indicates which sub-protocol was used among the NTLM protocols.
        - Key length indicates the length of the generated session key. This will be 0 if no session key was requested.
```

ADFS works correctly using following Linux client : Google Chrome.  

No issues from Microsoft browser version (Firefox, Chrome, IE, Edge).

It's only related to the ADFS. When Linux users connect to other website using same authentication protocols (NTLM/Negotiate) from Linux Firefox, it's works.

Does anyone ever faced this message?

I'm thinking about ExtendProtectionTokenCheck, which have currently "require" value instead of "Allow".

ADFS Version : 4.0 (Windows Server 2016)  

Firefox version : 68.11.0esr

Thank you for your help,

Charles

## Answers

_No answers on this thread._
