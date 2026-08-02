---
title: "ADCS errors after migrating the service to new servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189308/adcs-errors-after-migrating-the-service-to-new-ser
question_id: 2189308
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# ADCS errors after migrating the service to new servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189308/adcs-errors-after-migrating-the-service-to-new-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a 2-tier PKI Certificate Authority ADCS infrastructure in 2 domains that I am migrating from Windows 2012R2 servers to Windows 2022 Servers. I am following the article (https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-active-directory-certificate-service-from/ba-p/2328766?WT.mc_id=modinfra-27462-abartolo).  After migrating the offline Root CA and Enterprise Issuing CA in the one domain by restoring the backup and registry from the original servers, I am receiving the following error and I cannot start the CA Service. I receive the error.: The revocation function was unable to check revocation because the revocation server was offline. 0x80092013 (-2146885613 CRYPT_E_REVOCATION_OFFLINE). 

I had to execute "certutil –setreg ca\CRLFlags +CRLF_REVCHECK_IGNORE_OFFLINE" to get past this but I need to resolve the CRL file issue.  I published a new CRL file from the new offline Root CA and copied it to the C:\Windows\System32\CertSrv\CertEnroll folder on the Issuing Server but it didn't resolve the problem.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-11*

Hello Steve March1,  

Thank you for your reply.  

You can check the AIA and CDP configurations via root CA Properties and registry on root CA.  

For more information, please check the part: Perform Post Installation Configuration for Root CA-->Configure the AIA and CDP  

AD CS Step by Step Guide: Two Tier PKI Hierarchy Deployment - TechNet Articles - United States (English) - TechNet Wiki (microsoft.com)  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-10*

Thanks for the response.    

-  They are all in C:\Windows\system32\CertSrv\CertEnroll on the Issuing CA.  

-  I checked "Publish Delta CRLs to this location" and I have less errors in PKIVIEW.MSC now.  But I am still getting errors AIA Location and CDP Location of the Root CA when I run PKIVEW.MSC on the issuing server.  The error is "Unable to Download" and location is still using the crt for the old Root CA.  How do I change this location to use the new Root CA's hostname?  

-   I was missing the CRT of the Root CA in the Enroll folder of the issuing server.  After I copied that over, that problem is now resolved.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-10*

Hello Steve March1,  

Thank you for your reply.  

The issue you mentioned one problem that are difficult to troubleshoot or solve. However, you can try to check information below.  

1.What locations did you configure for AIA and CDP?   

For example:   

local disk location (C:\Windows\system32\CertSrv\CertEnroll)   

LDAP location   

http location  

2.Which entry displayed error "unable to download" via PKIview.msc.? You should check it.  

On the root CA or issuing CA?  

LDAP entry or Http entry on PKIview.msc?  

2.Usually, the issue may be caused by wrong configurations on CA properties (if its CRL on root CA, you can check the CRL setting on root CA, if its CRL on issuing CA, you can check CRL setting on issuing CA).

-  Or you need to check shared permissions and NTFS permissions on shared folder on IIS server that hosted http location.  

4.Have you put all the .crt files and .crl files about root CA and issuing CA to http location on IIS server?  

You can check them based on the link below.  

AD CS Step by Step Guide: Two Tier PKI Hierarchy Deployment - TechNet Articles - United States (English) - TechNet Wiki (microsoft.com)  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Thank you for your response.  

-  It is only functioning because I ran "certutil –setreg ca\CRLFlags +CRLF_REVCHECK_IGNORE_OFFLINE" to get past the revocation check but I need to resolve the CRL file issue and the CRL problem still exists.  

-  I get the CRL error when I try to start the issuing CA service.  PKIview reports errors as well that I cannot resolve.  PKIView reports "unable to download" on both root CA and issuing sub CA.  

-  I have migrated both offline root CA and Enterprise issuing CA.  The issuing CA will not start properly do to the error described in my posts.  

-  Yes but with a number of issues described.   I am receiving the following error when I try to start the CA Service: The revocation function was unable to check revocation because the revocation server was offline. 0x80092013 (-2146885613 CRYPT_E_REVOCATION_OFFLINE).  

Thank you for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Hello Steve March1,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description above, I understand now you can start the CA service in new CA server, am I right?  

2.Where did you see "the CRL file issue"? Via PKIview.msc console or any location? On Root CA or issuing CA?  

3.Would you please describe the detailed the CRL file issue so that we can provide further help?

4.Have you finished the 2-tier PKI migration?  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
