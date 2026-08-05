---
title: "Domain controller using SMB1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/177097/domain-controller-using-smb1
question_id: 177097
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller using SMB1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/177097/domain-controller-using-smb1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Part of a remediation task I'm disabling SMB1 on domain controllers, i have enabled SMB1 auditing and found that there are several domain controllers trying to access another domain controller using SMB1? I have looked through the logs but can't find anything obvious, is there a reason why a domain controller behave this way?  

Thanks in advance.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-27*

the answer is simple, all SMB servers. Domain controllers are a good example, client computers and member servers use SMB to access SYSVOL and NETLOGON shares to apply group policy, so domain controllers are servers to audit. File and print servers also need to be audited.  

In my scenario I have three concerned servers: DC01 and DC02 are domain controllers, MEM01 is a file server. All of them are running Windows Server 2012 R2.  

To enable SMB v1 auditing on Windows Server 2012 R2 run the PowerShell command:  

Set-SmbServerConfiguration -AuditSmb1Access $true  

reference：https://azurecloudai.blog/2018/12/17/step-by-step-safely-disabling-smb-v1-from-your-production-environment/  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-27*

Hi,

*Part of a remediation task I'm disabling SMB1 on domain controllers, i have enabled SMB1 auditing and found that there are several domain controllers trying to access another domain controller using SMB1? *

Check if you have also disabled also smbv1 client on each domaine controller, you can refer to the following link to get more details about how disable and enable smbv1 client:

detect-enable-and-disable-smbv1-v2-v3

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-26*

SMB 445 is a requirement. For 2008 R2 and higher SMB v1 should not be needed.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections    

https://techcommunity.microsoft.com/t5/itops-talk-blog/beyond-the-edge-how-to-secure-smb-traffic-in-windows/ba-p/1447159    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

These are Windows Server 2008 R2 and 2012 R2 with 2008R2 domain/forest functional level.    

I have followed that document and it is useful for setting up auditing which i have but i can't see anything obvious on the domain controllers, there are no shares except netlogon and sysvol.    

In the screenshot the client address is the hostname of the domain controller.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-26*

What operating systems are involved? Something here may help.    

https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3    

--please don't forget to Accept as answer if the reply is helpful--
