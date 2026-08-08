---
title: "Wap Connection issue to ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/746565/wap-connection-issue-to-adfs
question_id: 746565
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Wap Connection issue to ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/746565/wap-connection-issue-to-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm getting this error when the WAP tries to connect to the ADFS server when installing the Certificate.  

when I run get-Webapplicationproxyapplicaition command I get Web Application Proxy could not connect to the AD FS configuration storage and could not load the configuration Make sure that the Web Application Proxy server can connect to the AD FS server if not run Install-WebApplicationProxy.  

Run Install-WebApplicaitionProxy get this error An error occurred when attempting to establish a trust relationship with the federation service. The underlying connection was closed. Could not establish a trust relationship.  The WAP server can resolve the ADFS server.  

How can I fix this issue?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

Then check the other points. Make sure they use the safe TLS/SSL cipher on both side: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-protocols-in-ad-fs make sure you enable SchUseStrongCrypto on both. Have disable the legacy stuff on both etc...    

And make sure you can reach the revocation endpoints of your ADFS TLS certificates from your WAP Server.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-28*

ADFS 3 on server2012 R2. Yes I am using the FQDN of the farm.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

Oh, is that a duplicated post with https://learn.microsoft.com/en-us/answers/questions/749961/adfs-wap-connection-issue-to-adfs-server.html ? Well this one has slighly more information.    

It could be an issue with the TLS crypto suite, with SNI, with firewall doing inspection etc... Hard to say for now.     

What version of AD FS are you using?    

Also, you need to use the FQDN of the farm to join the WAP (not the FQDN o the server). Are you doing that?
