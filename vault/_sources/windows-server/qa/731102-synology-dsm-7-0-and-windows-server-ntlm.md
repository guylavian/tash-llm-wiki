---
title: "Synology DSM 7.0 and Windows Server NTLM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/731102/synology-dsm-7-0-and-windows-server-ntlm
question_id: 731102
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Synology DSM 7.0 and Windows Server NTLM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/731102/synology-dsm-7-0-and-windows-server-ntlm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

as I know, in DSM 7.0 only NTLMv2 is supported by default.    

I have Windows Server 2012 with Local Security Policy Network security: LAN Manager authentication level sets as Send NTLM response only    

Here is the Microsoft explanation: Client devices use NTLMv1 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level    

My question is, why I can`t connect to Synology using SMB if Synology DSM 7.0 is a server with NTMLv2 support and Windows Server 2012 should use NTLMv2 session security if the server supports it, because Windows Server 2012 Local Security Policy Network security: LAN Manager authentication level is set as Send NTLM response only (in according to Microsoft explanation: Client devices use NTLMv1 authentication, and they use NTLMv2 session security if the server supports it)?    

When I enable NTLMv1 authentication in Synology DSM 7.0 SMB settings, everything works fine.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-24*

you should try this in your Synology NAS,  

Configure settings for legacy devices

Warning: Enabling NTLMv1 is insecure and could make your Synology NAS vulnerable to attacks.

Most legacy devices (e.g., IP cameras, multi-functional printers, multimedia players) only support SMB1 and NTLMv1, and do not allow the customization of NTLM settings. For better security, we recommend replacing legacy devices or contacting the device manufacturers to request support for NTLMv2.

As a last resort, you can go to DSM > Control Panel > File Services > SMB > Advanced Settings > Others to tick Enable NTLMv1 Authentication. This will lower the security level but allow legacy devices to authenticate via NTLMv1.

https://kb.synology.com/es-mx/DSM/tutorial/I_cannot_access_shared_folders_from_WinXP_computer

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-14*

Hello @Jakub Żylak       

For certain application you will need to set up the policy as "Send NTLMv2 response only\ refuse LM & NTLM" for this security policy "Network security: LAN Manager authentication" in Local Security Settings > Local Policies > Security Options.    

At the same time, 3rd Party applications will also have specific settings to transmit only using NTLMv1 or not, for which I would recommend you to promp your question or contact the software manufacturer (Synology) for assitance.    

Hope this helps with your query,    

--    

--If the reply is helpful, please Upvote and Accept as answer--
