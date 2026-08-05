---
title: "Issue with Slow OWA Login After Migrating from Exchange 2013 to Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2103925/issue-with-slow-owa-login-after-migrating-from-exc
question_id: 2103925
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with Slow OWA Login After Migrating from Exchange 2013 to Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2103925/issue-with-slow-owa-login-after-migrating-from-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, I recently migrated from Exchange Server 2013 to Exchange Server 2016. After the migration, I'm experiencing some issues with OWA on one of my Exchange servers.   

When I try to log in to OWA using localhost on this server, it takes a long time to log in. Despite installing the latest Security Updates and updating the Client Access Server (CAS), the issue persists. Has anyone else encountered a similar issue after a migration, and what steps did you take to resolve it? Thanks in advance!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-16*

Hi @Moshiur (Moshiur Khan)  ,

Welcome to the Microsoft Q&A platform!

Based on your description, it is not uncommon to encounter OWA issues after migrating from Exchange Server 2013 to Exchange Server 2016. Here are a few steps you can take to troubleshoot and potentially resolve the issue:

 

-  Since you are experiencing delays when logging into OWA using localhost, there may be some network delays or DNS resolution issues. Make sure the server's network configuration is correct and there are no issues with the DNS settings.

 

-  Check Event Viewer on the Exchange server for any warnings or errors that may give you more insight into what is causing the delay. Look for events related to OWA, IIS, or authentication.

 

-  Sometimes, an IIS reset can resolve issues with OWA. You can do this by running iisreset from an elevated command prompt.

 

-  Verify that the authentication settings for OWA are configured correctly. Incorrect settings can cause delays in the logon process.

 

-  Make sure the OWA virtual directory URL is set correctly. You can check and configure these settings using the Exchange Management Shell.

 

-  Use performance counters to monitor the performance of the server. This can help determine if the issue is related to resource utilization.

 

-  Make sure you have installed the latest cumulative updates for Exchange Server 2016. There have been issues in the past that were resolved by installing the latest updates.

 

-  If the issue is specific to a certain mailbox, try migrating the mailbox to another database and see if the issue persists.

 

-  Create a new test mailbox and see if you experience the same delay when logging into OWA. This can help determine if the issue is related to the mailbox or server configuration.

 

-  Make sure your SSL certificate is configured correctly and is not expired. Certificate issues can sometimes cause delays in the logon process.

 

-  If you use a load balancer, make sure it is configured correctly and there are no issues with the load balancing configuration.

 

-  Check if your antivirus or firewall is causing the delay. Sometimes these can interfere with the OWA logon process.

 

These are some general steps that can help you diagnose and possibly resolve the issue. If the issue persists, it may be helpful to provide more details about your environment and any specific error messages you see. This can help narrow down the cause of the delay.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
