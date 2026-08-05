---
title: "Block NTLM and NTLMv2 totally, only enable Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1658781/block-ntlm-and-ntlmv2-totally-only-enable-kerberos
question_id: 1658781
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Block NTLM and NTLMv2 totally, only enable Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1658781/block-ntlm-and-ntlmv2-totally-only-enable-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear PPL. 

I would like to totally shut down NTLMv2 in our Domain. I would like only Kerberos as our Accounts Authentications. 

Should I just change GPO of Default Domain Policy on AD: 

Network security: Restrict NTLM: Incoming NTLM traffic: to Deny All accounts? 

or 

It's better to set the Network Security: Restrict NTLM: Audit Incoming NTLM traffic policy setting and then review the Operational log to understand what authentication attempts are made to the member servers, and then what client applications are using NTLM.

Which one should I use? 

I dont need to set anything particular for enabling Kerberos right? 

Thanks,

Namless

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-22*

Hello,

Thank you for posting in Q&A forum.

If you are sure that there are no applications or clients that rely on NTLMv2 in your environment, simply enable "Network Security: Restrict NTLM: Incoming NTLM Traffic: Deny All Accounts". This setting blocks all authentication requests using NTLMv2, forcing clients to authenticate using Kerberos. This is the most straightforward method for ensuring that all clients and servers in the domain are fully prepared to transition seamlessly to a pure Kerberos environment.

If you are unsure whether there are applications or clients in your environment that rely on NTLMv2, you can first enable the "Network Security: Restrict NTLM: Audit incoming NTLM traffic" policy setting. This will not block NTLMv2 traffic but will log all attempts to authenticate using NTLMv2 in the Operations Log. By analyzing these logs, you can identify which client applications, servers, or services still rely on NTLMv2, so you can make targeted adjustments or updates.

In modern Windows domain environments, Kerberos is typically enabled by default and the preferred authentication protocol. As long as your domain functional level, client operating system, and applications support Kerberos, and your network architecture (such as DNS configuration, time synchronization, etc.) meets the basic requirements for Kerberos, you generally can use Kerberos without additional configuration.

It is recommended to refer to the following link for a more detailed description:

How to Disable NTLM Authentication in Windows Domain | Windows OS Hub (woshub.com)

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
