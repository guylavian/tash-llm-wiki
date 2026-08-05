---
title: "ADCS Migration from Windows 2008r2 to Windows 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/64232/adcs-migration-from-windows-2008r2-to-windows-2019
question_id: 64232
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADCS Migration from Windows 2008r2 to Windows 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/64232/adcs-migration-from-windows-2008r2-to-windows-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi experts,  

I would like to ask the following on the topic migrating ADCS from 2008R2 to 2019. I have run couple of articles like the one as below:-  

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-the-active-directory-certificate-service/ba-p/697674  

Let me briefly explain on the current structure in the environment of ours  

1 Root CA which is not joined domain - Windows 2008R2  

4 Issuing suboordinate CA - Windows 2008R2  

The final result of the ADCS structure will be as below:-  

Root CA and the issuing subordinate CA will be migrated to Windows 2019  

Since they are many clients are relying to the certificates which was rolled out. Are we able to migrate all the servers from Windows 2008 R2 to Windows 2019 without the need to reissue the cert to the clients? As there are tons of web apps and services which are relying on the certificates.  

I would like to have this deployment in order so that there will not issues of certificate where the chains will be broken. The objectives are as below:-  

CA name will be the same  

IP address of the CA server will be different  

Hostname of the CA server will be different.  

I was advised to perform the root CA migration first then followed by the 4 suboordinate issuing CA. Is that a good idea?  

Another question is since the root CA server name and the IP address will be different, how are we going to tell the issuing CA that the root CA server name and IP address is being changed? Also when we migrate the subordinate issuing CA, how are we going to tell the other suboordinate CA and root CA that this issuing CA server name and ip address is being changed. What are the configuration that is to take place  

Thank you  

Peter

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-08-11*

Are we able to migrate all the servers from Windows 2008 R2 to Windows 2019 without the need to reissue the cert to the clients?

yes. Though, keep in mind that straight in-place updgrade from Windows Server 2008 R2 to Windows Server 2019 is not supported. You have to upgrade to Windows Server 2012 R2 first. If you set up a new box and migrate CA to new box, you can do straight migration.

I was advised to perform the root CA migration first then followed by the 4 suboordinate issuing CA. Is that a good idea?

the order of migrated CAs is not relevant at all. Though, I would suggest to migrate offline root first, to get some practice.

I strongly recommend to make a full backup of existing CAs to roll back in case of failure.

Another question is since the root CA server name and the IP address will be different, how are we going to tell the issuing CA that the root CA server name and IP address is being changed?

you don't need to tell issuing CAs anything since your root is workgroup member, and domain CAs are not capable to communicate with workgroup CAs. Under this statement I assume that root CA doesn't host CRLs and they are published somewhere to domain-joined web server. If your root CA is hosting CRLs (has installed IIS) and issuing CAs connect to root CA to fetch CRLs, then you have to update root CA DNS records.

Also when we migrate the subordinate issuing CA, how are we going to tell the other suboordinate CA and root CA that this issuing CA server name and ip address is being changed.

Issuing CAs don't communicate between each other, so there is nothing to change.

I strongly recommend to follow official ADCS migration guide and not use blog posts. Blog posts often (even Microsoft ones) contain errors, may not cover important details. Referenced ADCS migration guide is most complete and fully correct. I used it for decade and it never failed.

In the case if you feel that you are not ready to migrate your PKI alone, I would suggest to engage consulting company to assist you with migration process.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-11*

Hi Peter,  

Thank you so much for posting here.  

1, "Are we able to migrate all the servers from Windows 2008 R2 to Windows 2019 without the need to reissue the cert to the clients?"  

After migration from Windows 2008 R2 to Windows 2019, there is no need to reissue the certificates to the clients. When migrating a CA, the computer name of the target computer can differ from the computer name of the source computer, but the CA name must stay the same.  

By default, Active Directory Certificate Services (AD CS) is configured with certificate revocation list (CRL) distribution point extensions that include the CA computer host name in the path. This means any certificates issued by the CA before migration may contain certificate validation paths that contain the old host name. These paths may no longer be valid after the migration. To avoid revocation checking errors, the new CA must be configured to publish CRLs to the old (pre-migration) path as well as the new paths.  

2, "I was advised to perform the root CA migration first then followed by the 4 suboordinate issuing CA. Is that a good idea?"  

Yes, we could perform the root CA migration first and then follow by the issuing CA. It is suggested that we would migrate CA during downtime. And if possible, to avoid any issues, we could do the test in test environment first.   

3, "Another question is since the root CA server name and the IP address will be different, how are we going to tell the issuing CA that the root CA server name and IP address is being changed? Also when we migrate the subordinate issuing CA, how are we going to tell the other suboordinate CA and root CA that this issuing CA server name and ip address is being changed."  

As mentioned, it 'd better migrate CA during the downtime. After the migration, we will perform some steps for post-migration and then veriry PKI hierarchy health. If it works properly after migration, everything seems fine.   

Here we would like to share with you the below document. Hope it will be helpful.   

Performing the Upgrade or Migration  

(We could kindly search the title for this document. There is issue to add the link of the document here. Thanks so much for your understanding.)  

Thank you so much for your support.  

Best regards,  

Hannah Xiong
