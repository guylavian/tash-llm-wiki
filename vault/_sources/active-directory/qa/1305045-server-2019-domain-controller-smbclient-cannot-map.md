---
title: "Server 2019 Domain Controller SMBclient cannot map NetApp Drives"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1305045/server-2019-domain-controller-smbclient-cannot-map
question_id: 1305045
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Server 2019 Domain Controller SMBclient cannot map NetApp Drives

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1305045/server-2019-domain-controller-smbclient-cannot-map (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am supporting Windows again after many years. This client I'm assigned to has Domain Controllers running 2008r2 and 2012r2 and they want Azure AD Connect Password Hash Sync. The minimum requirement for this is a functional level of 2016.

I installed a new Server 2019 instance, migrated the FSMO roles, and ensured all DCs are replicating to each other. I created a new domain user and ran the logon script that maps a few network drives from an old NetApp FAS2552 running Ontapp 8.2.2.7. This was successful.

After applying patches and rebooting, the new DC will no longer connect the drives. I believe it has something to do with KDC changes made in November 2022, but I'm not sure.

I added another Server 2019 instance to the network, logged in locally, and connected the NetApp drives successfully. Then I installed Windows Security Updates, and after a reboot the drives failed the same way as they do on the new DC.

After digging around, I found a couple of things:

This article

And a random bit about some Registry changes:

reg add HKLM\system\currentcontrolset\services\kdc /v KrbtgtFullPacSignature /t REG_DWORD /d 0 /f

reg add HKLM\system\currentcontrolset\services\kdc /v ApplyDefaultDomainPolicy /t REG_DWORD /d 0 /f

reg add HKLM\system\currentcontrolset\services\netlogon\parameters /v RequireSignorSeal /t REG_DWORD /d 0 /f

These changes worked on the test instance and the NetApp drives connected again. So long as the %logonserver% is one of the old Domain Controllers.

These changes do not work on the new domain controller, and when any client uses it as their %logonserver%, the drives fail to connect.

I'm getting ready to uninstall Windows Security updates to see if the NetApp drives connect again. Then inform the client their environment cannot be patched until they upgrade their NetApp OS to support AES KDC auth.

Any help is much appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-14*

Hello Dave,

Thank you for your question and for reaching out with your question today.

It seems that you are facing issues with connecting network drives after applying Windows security updates on your new Domain Controller running Server 2019. The changes you found regarding KDC and registry settings can sometimes resolve such issues, but they don't seem to be working in your case.

One possible reason for the network drive connection failure could be compatibility issues between the NetApp FAS2552 running Ontapp 8.2.2.7 and the updated KDC authentication mechanism used by the new Domain Controller. As you mentioned, upgrading the NetApp OS to support AES KDC authentication might be necessary for proper compatibility.

In this situation, your plan to uninstall the Windows security updates to check if the drives connect again is a reasonable step. This will help you determine if the updates are indeed causing the problem.

To address the issue in the long term, consider the following steps:

-  Upgrade the NetApp FAS2552 OS: Contact NetApp support to inquire about the compatibility of your current NetApp OS version with the updated KDC authentication mechanism. They should be able to guide you on the necessary upgrade process to ensure compatibility.

-  Update the functional level of your domain: Once the NetApp OS upgrade is completed, you can proceed with raising the functional level of your domain to 2016 or higher. This will enable you to utilize Azure AD Connect Password Hash Sync as desired.

-  Test network drive connections: After completing the NetApp OS upgrade and raising the functional level, thoroughly test the network drive connections on all domain controllers to ensure they function correctly.

-  Apply Windows security updates: Once you have confirmed that the network drive connections are working properly, you can proceed with applying Windows security updates to maintain the security and stability of your domain.

I used AI provided by ChatGPT to formulate part of this response. I have verified that the information is accurate before sharing it with you.

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
