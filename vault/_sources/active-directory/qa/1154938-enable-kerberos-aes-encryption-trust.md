---
title: "Enable Kerberos AES Encryption - Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1154938/enable-kerberos-aes-encryption-trust
question_id: 1154938
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Enable Kerberos AES Encryption - Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1154938/enable-kerberos-aes-encryption-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,    

We have a two-way trust with 2 domain.    

I would like to enable Kerberos AES encryption int the trust.    

From what I read, windows XP workstations and 2003 servers do not support AES and will be affected by the change. I think we don't have any more in our environment but I'm not 100% sure.    

-  Is this statement correct?    

-  Is there a way to monitor if there will be an impact in my environment? Events in the DC Logs to confirm that oldest protocol is not use anymore?    

Thanks you very much!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-06*

Hello,    

-  Yes, it is.    

-  Yes, one the event log, you can see the error.    

Be careful, it's the same problem with higher version XP and 2003.    

More information here : https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos    

Please remember to "Accept Answer" if any answer/reply helped, so that others in the community facing similar issues can easily find the solution.
