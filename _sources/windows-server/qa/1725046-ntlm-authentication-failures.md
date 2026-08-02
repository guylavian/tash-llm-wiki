---
title: "NTLM authentication failures"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1725046/ntlm-authentication-failures
question_id: 1725046
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# NTLM authentication failures

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1725046/ntlm-authentication-failures (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I need your help to understand the NTLM authentication level again. I am quite confused with NTLM authentication levels.

I have Server-A configured to 'Send NTLMv2 response only\refuse LM & NTLM', and DomainController-A configured to 'Send NTLMv2 response only\refuse LM'. Everything works as expected with these settings. 

However, when I changed DomainController-A's setting to 'Send NTLMv2 response only\refuse LM & NTLM', authentication started failing from Server-A. I don't understand why authentication fails since Server-A was already configured to send NTLMv2 responses.

Thanks.

Regards,

Raj

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-24*

Hello,

Thank you for posting in Q&A forum.

Based on your description, the possible reason for the authentication failure is that although Server A is configured to send only NTLMv2 responses, after setting it to "Send NTLMv2 response only\refuse LM & NTLM", some applications or services running on Server A may not be able to send NTLMv2 responses that fully comply with the enhanced NTLMv2 specification expected by DomainController-A, and the service is falling back to NTLM. If Server A does not generate an NTLMv2 response that DomainController-A accepts under this stricter configuration, authentication will fail.

To troubleshoot and resolve the issue, consider the following steps:

-  Check the event logs: Check the event logs on Server A and Domain Controller A for any specific NTLM or authentication-related errors or warnings that may provide more insight into the cause of the authentication failure.

-  Network capture: Use a network capture tool such as Wireshark to capture the authentication traffic between Server A and Domain Controller A. Analyze the captured packets to view the negotiations and responses exchanged during the authentication attempt.

-  Test with default settings: Consider temporarily reverting the NTLM settings of DomainController-A to "Send NTLMv2 response only\refuse LM" to see if authentication resumes working. This helps confirm if the stricter settings on DomainController-A ("Reject LM and NTLM") are indeed the cause of the problem.

For more information about NTLM authentication levels please refer to the following links:

Network security LAN Manager authentication level - Windows 10 | Microsoft Learn

NTLM Overview | Microsoft Learn

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
