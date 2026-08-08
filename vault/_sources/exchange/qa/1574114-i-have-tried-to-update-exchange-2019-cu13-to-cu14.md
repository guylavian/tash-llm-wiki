---
title: "I have tried to update Exchange 2019 CU13 to CU14"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1574114/i-have-tried-to-update-exchange-2019-cu13-to-cu14
question_id: 1574114
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# I have tried to update Exchange 2019 CU13 to CU14

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1574114/i-have-tried-to-update-exchange-2019-cu13-to-cu14 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have tried to update Exchange 2019 CU13 to CU14 and each time I get this error "system.unauthorizedaccessexception:Certificate with fingerprint XXXXXXXX".
It is clearly specified that the problem is "Insufficient right to grant access to the network service to the certificate with the fingerprint".
I'd like to resolve this problem as quickly as possible as we're working on a major update.
The setup.exe was run as the domain administrator.
Configuration:
Active Directory on server 2022 up to date
Exchange 2019 (CU13) on Server 2022 up to date
PKI on server 2022 up to date
Thanks to all.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-26*

As suggested by Wandi Ding, running the Exchange Server Health Checker can provide additional insights into the issue.
Microsoft documentation on insufficient permissions to prepare Active Directory for Exchange Server: https://learn.microsoft.com/en-us/exchange/insufficient-permissions-to-prepare-active-directory-adupdaterequired-exchange-2013-help
Exchange setup fails due to insufficient permissions: https://techcommunity.microsoft.com/t5/exchange/cumulative-update-fails-due-to-certificate-permissions/td-p/2276862
If you're using a third-party certificate, consider the following:
Check that the user account running setup.exe has the required permissions to access the certificate.

-  Some users have reported success by replacing the third-party certificate with a temporary self-signed certificate generated using Exchange Management Shell (EMS). However, this is a workaround, so proceed with caution:

-  Create a self-signed certificate with EMS. Access the Exchange Management Shell (EMS) as an administrator. Execute the following command, replacing `ServerName` with your actual server name.

`New-SelfSignedCertificate -FriendlyName "Exchange Server Self-Signed" -CertStoreLocation "LocalMachine" -KeyUsage DigitalSignature,KeyEncipherment -KeyAlgorithm RSA -Subject "CN=ServerName"`
Using the appropriate management tools, bind the self-signed certificate to Exchange Server services (such as SMTP and IIS).
Retry the Exchange Server upgrade with the self-signed certificate installed.
After a successful update, revert to the original third-party certificate and reconfigure the services to use it.

Remember to delete the self-signed certificate once it's no longer needed.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-26*

Hi @DOUDUDE,

Based on the error message you provided, the issue appears to be related to insufficient permissions to access the certificate using the given fingerprint.Please run Health Checker first to see if we can get more information. Besides, have you tried checking the certificate? If the Exchange Server Authentication certificate has expired, use a script or manual renewal, fix the certificate issues and then try to update again. In addition to this, based on some feedback from other users, if your certificate is a third-party certificate, you could try replacing the third-party certificate with a self-signed certificate created through EMS to complete the installation. Once completed, swapped back to the normal third-party certificate and put the IIS and SMTP services back on the original certificate.

Hope the above information is helpful to you！

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
