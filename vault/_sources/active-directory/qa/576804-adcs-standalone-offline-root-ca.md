---
title: "ADCS Standalone Offline Root CA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/576804/adcs-standalone-offline-root-ca
question_id: 576804
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# ADCS Standalone Offline Root CA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/576804/adcs-standalone-offline-root-ca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is it possible to have ****only one ADCS Standalone Offline Root CA for multiple Forests and Domains**** ?

I have 3 separate AD Forests -- contoso.com, fabrikam.com and testlab.com. All these are separate AD forest with no AD Forest/Domain trust between them. Also, there is no need for Cross-Forest certficate and authentication.

I shall have 3 separate domain-joined Enterprise Issuing CAs in each of these 3 forests.

But, my question is regarding the Standalone Offline Root CA which shall be in a workgroup and not joined to any AD Domain or Forest.

Can I use only one Standalone Offline Root CA ? Is this possible instead of having 3 separate Standalone Offline Root CAs for 3 forests ?

If YES -- how ? Can you please refer to some Microsoft articles/whitepapers or Deployment Guides ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-06*

Hi @Monimoy Sanyal       

This thread might be helpful for you https://learn.microsoft.com/en-us/answers/questions/369400/consolidating-existing-adcs-deployment-cross-fores.html    

----------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-05*

Question 1:  

AFAIK, if you don't publish the AIA / CDP through LDAP, you don't need the DSConfigDN parameter.

Personally, i would only configure using a HTTP URL and remove the LDAP for the RootCA

Question 2:  

Here is a good article on where to publish the AIA / CDP  

https://social.technet.microsoft.com/wiki/contents/articles/18590.recommended-windows-ca-publication-urls-flags-two-tier-small-scale-internal-cas.aspx

You can use multiple HTTP URL on the RootCA and on the Issuing CA. But the client will query AIA / CDP in order... so the client that will need to call the 3rd URL may have some latency.

Another point, When the web server that publish the CDP / AIA is in the same domain as the IssuingCA Server, when the CRL is published by the CA Server, it copy automatically to the Web Server. But in your case, the CDP / AIA location will probably not be accessible by the 3 Issuing CA using Windows integrated authentication. In that case, you must find a way to copy the CRT / CRL to the web Server automatically when the CRL is published.

The command lines on the RootCA and Issuing CA should look like this...

Root CA  

certutil -setreg CA\CACertPublicationURLs "1:C:\Windows\system32\CertSrv\CertEnroll\%1_%3%4.crt\n2:http://pki.contoso.com/CertEnroll/%1_%3%4.crt\n2:http://pki.fabrikam.com/CertEnroll/%1_%3%4.crt\n2:http://pki.testlab.com/CertEnroll/%1_%3%4.crt"  

certutil -setreg CA\CRLPublicationURLs "1:C:\Windows\system32\CertSrv\CertEnroll\%3%8%9.crl\n2:http://pki.contoso.com/CertEnroll/%3%8%9.crl\n2:http://pki.fabrikam.com/CertEnroll/%3%8%9.crl\n2:http://pki.testlab.com/CertEnroll/%3%8%9.crl"

Contoso Issuing CA  

certutil -setreg CA\CACertPublicationURLs "1:C:\Windows\system32\CertSrv\CertEnroll\%1_%3%4.crt\n2:http://pki.contoso.com/CertEnroll/%1_%3%4.crt"  

certutil -setreg CA\CRLPublicationURLs "65:C:\Windows\system32\CertSrv\CertEnroll\%3%8%9.crl\n6:http://pki.contoso.com/CertEnroll/%3%8%9.crl

Fabrikam Issuing CA  

certutil -setreg CA\CACertPublicationURLs "1:C:\Windows\system32\CertSrv\CertEnroll\%1_%3%4.crt\n2:http://pki.fabrikam.com/CertEnroll/%1_%3%4.crt"  

certutil -setreg CA\CRLPublicationURLs "65:C:\Windows\system32\CertSrv\CertEnroll\%3%8%9.crl\n6:http://pki.fabrikam.com/CertEnroll/%3%8%9.crl

Testlab Issuing CA  

certutil -setreg CA\CACertPublicationURLs "1:C:\Windows\system32\CertSrv\CertEnroll\%1_%3%4.crt\n2:http://pki.testlab.com/CertEnroll/%1_%3%4.crt"  

certutil -setreg CA\CRLPublicationURLs "65:C:\Windows\system32\CertSrv\CertEnroll\%3%8%9.crl\n6:http://pki.testlab.com/CertEnroll/%3%8%9.crl

But AFAIK, it's not possible on the Root CA to show only contoso URL for contoso issuing CA, the Fabrkam URL for Fabrikam issuing CA and the Testlab URL for the Testlab Issuing CA

hth

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-04*

Hi cthivierge --- First, thanks for your response. Additionally, I have also referred to these 2 links:  

****** Test Lab Guide: Deploying an AD CS Two-Tier PKI Hierarchy ******

>> https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831348(v=ws.11)  

>> https://social.technet.microsoft.com/wiki/contents/articles/15037.ad-cs-step-by-step-guide-two-tier-pki-hierarchy-deployment.aspx

I have already checked the link you have shared earlier. About this link, I have 2 questions:

Question 1:  

On the Standaloneoffline root CA when I type the following commands, how will it set 3 different records in the registry ?  

a --- certutil.exe –setreg CA\DSConfigDN CN=Configuration,DC=contoso,DC=com  

b --- certutil.exe –setreg CA\DSConfigDN CN=Configuration,DC=fabrikam,DC=com  

c --- certutil.exe –setreg CA\DSConfigDN CN=Configuration,DC=testlab,DC=com stion

Question 2  

"use only HTTP URL for the CDP and AIA extensions. Then you can import the Root CA certificates into AD with certutil.exe -f -dspublish rootca.cer RootCA. "  

Even if I use HTTP URL for CDP and AIA extensions, the certificate issued by the Offline Root CA will show all 3 HTTP urls; isn't it ?  

My intention is to show only contoso.com HTTP URL in the CDP & AIA of contoso Root CA Certificate.  

My intention is to show only fabrikam.com HTTP URL in the CDP & AIA of fabrikam contoso Root CA Certificate.  

My intention is to show only testlab.com HTTP URL in the CDP & AIA of testlab Root CA Certificate.

All of these --- are they possible with only one Standalone Offline Root CA ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-04*

This question has already been asked several years ago but it's still accurate  

https://social.technet.microsoft.com/Forums/ie/en-US/ba286eda-76c1-45d1-838f-a9bfa1aaf9ef/offline-root-ca-for-two-separate-domains?forum=winserversecurity  

hth
