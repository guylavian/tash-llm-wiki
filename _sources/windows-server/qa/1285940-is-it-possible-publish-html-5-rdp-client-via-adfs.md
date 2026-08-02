---
title: "Is it possible publish html 5 rdp client via Adfs and webApp poxy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1285940/is-it-possible-publish-html-5-rdp-client-via-adfs
question_id: 1285940
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Is it possible publish html 5 rdp client via Adfs and webApp poxy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1285940/is-it-possible-publish-html-5-rdp-client-via-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

I do not find any instructions. how to publish my html5 rdp client  https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-web-client-admin via adfs on premise and webapp proxy.

When i publish this way: https://web.archive.org/web/20180619155432/http://blog.tmurphy.org/2015/06/securing-rd-gateway-with-web.html

I get the standart autentification form from html5 rdp client which not working

Please help me

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-18*

Hello Sergei,

Thank you for your question and for reaching out with your question today.

This task is relatively complex and is not easy to describe within a forum like this.  The basic task list is as follows:

-  Ensure that you fulfil the following conditions before configuring RD Gateway through Web Application Proxy:

Install and configure AD FS for Windows Server 2012 on a Windows Server. Verify that the AD FS services work by accessing the AD FS sign-in page (https://<ADFS Compute FQDN>/adfs/ls/ idpinitiatedsignon.htm).

Install and configure the Web Application Proxy on a Windows Server which has the same domain as the AD FS server.

Make sure that you install the remote desktop services and perform all the steps for seamless logon with RD Gateway. For more details, refer to the Microsoft documentation.

-  Create a relying party trust for RD Gateway.

-  Publish the RD Gateway behind the Web Application Proxy

-  Modify your Remote Desktop Service (RDS) collections.

-  Set group policies on the Active Directory Domain Services computer.

-  Test the configuration.

More details can be found here:

https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/vip/cloud/vip-integrations-v127046077-d2278e2955/Symantec-VIP-Integration-Guide-for-Microsoft-Active-Directory-Federation-Services-(AD-FS)/remote-desktop-gateway-configuration-tasks-v120501072-d2328e4657.html

If the reply was helpful, please don’t forget to upvote or accept as answer.
