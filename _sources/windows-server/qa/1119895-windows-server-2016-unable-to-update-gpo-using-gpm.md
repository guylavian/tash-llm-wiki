---
title: "Windows Server 2016: Unable to update GPO using GPMC (OU) and Invoke-GPUpdate command after security update KB5018411"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1119895/windows-server-2016-unable-to-update-gpo-using-gpm
question_id: 1119895
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows Server 2016: Unable to update GPO using GPMC (OU) and Invoke-GPUpdate command after security update KB5018411

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1119895/windows-server-2016-unable-to-update-gpo-using-gpm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one Domain Controller Server (Windows Server 2019) and 5 Domain Members Server (Windows Server 2016). I have recently installed the windows update security patch as following:    

DC Server (Windows Server 2019): KB5005112    

Member Servers (Windows Server 2016): KB5018411    

After installing these update, every time I try to to update my group policy through GPMC at my DC Server (Right click on Member Servers OU and select Group Policy Update), it gives the access denied (8007005) error for all my Member Servers. Even the Invoke-GPUdpdate command in Powershell gave the same access denied error. I suspect this is because the recently installed updates have disabled my DCOM    

I have used to following method to bypass the disabled DCOM and resolve this issue on both my DC Server and Member Servers: In registry path HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\AppCompat, add a Dword "RequireIntegrityActivationAuthenticationLevel" and set its value to 0x00000000 (restart server afterwards).    

However I'm just wondering, after the March 2023 security updates later where DCOM will be permanently disabled with no way of bypassing it anymore, will this same GPMC access denied 8007005 error issue arise again?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-19*

I'm just wondering, could this issue be due to different Windows Server version between Domain Controller Server (2019) and Member Server (2016)? Because I have a colleague who uses Windows Server 2016 for both his Domain Controller Server and Member Server, but he did not face this issue after update KB5018411

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-08*

Dear HaniaLian-msft,    

Thank you for your response. Apologies as I am a bit confuse with your answer. Based on your highlight from Microsoft "It will keep the DCOM hardening enabled and remove the ability to disable it"    

According to my understanding, DCOM 'hardening' enabled basically means the DCOM will be disabled, and the ability to disable this hardening will be permanently removed. This means that DCOM will be permanently hardened (disabled).    

This is the reason for my action to add 'RequireIntegrityActivationAuthenticationLevel' Dword in registry and set it to 0x00000000, in order to disable the DCOM hardening.    

Kindly correct me if I'm wrong

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-08*

Hi.    

According to this official document, DCOM will remain enabled on 2023/3/14, and the ability to disable it will be removed:    

https://support.microsoft.com/en-us/topic/kb5004442-manage-changes-for-windows-dcom-server-security-feature-bypass-cve-2021-26414-f1400b52-c141-43d2-941e-37ed901c769c    

    

So DCOM will not be permanently disabled, and there is a high probability that you will not need to set group policy again to bypass disabled DCOM.    

Hope the information is helpful.    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
