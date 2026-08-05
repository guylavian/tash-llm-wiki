---
title: "Root CA missing in CDP folder in Active Directory Sites and Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2117181/root-ca-missing-in-cdp-folder-in-active-directory
question_id: 2117181
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Root CA missing in CDP folder in Active Directory Sites and Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2117181/root-ca-missing-in-cdp-folder-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

In my 2-tier PKI my offline root CA isn't showing in CDP folder. When I executed those commands in PowerShell as administrator it showed no errors:  

certutil.exe -dspublish -f "C:\CertData\ADDB Labs Certificate Authority.crt" RootCA

certutil.exe -addstore -f root "C:\CertData\i-win1_ADDB Labs Certificate Authority.crt"

certutil.exe -addstore -f root "C:\CertData\ADDB Labs Certificate Authority.crl"

but when I verified and saw that my root ca is not present in CDP AD Sites and Services, I tried to execute this command in cmd as admin from C:\CertData :  

-  certutil -f -dspublish "ADDB Labs Certificate Authority.crl"  

and got this error:  

ldap:///CN=ADDB Labs Certificate Authority,CN=i-win1,CN=CDP,CN=Public Key Services,CN=Services,DC=UnavailableConfigDN?certificateRevocationList?base?objectClass=cRLDistributionPoint?certificateRevocationList ldap: 0xa: LDAP_REFERRAL: 0000202B: RefErr: DSID-03100835, data 0, 1 access points ref 1: 'unavailableconfigdn' CertUtil: -dsPublish command FAILED: 0x8007202b (WIN32: 8235 ERROR_DS_REFERRAL).  

What may be the cause? Here is my config on root ca:  

certutil.exe -getreg CA\CRLPublicationURLs

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\ADDB Labs Certificate Authority\CRLPublicationURLs:

  CRLPublicationURLs REG_MULTI_SZ =

```
0: 64:C:\Windows\system32\CertSrv\CertEnroll\%3%8%9.crl

CSURL_SERVERPUBLISHDELTA -- 40 (64)

1: 8:ldap:///CN=%7%8,CN=%2,CN=CDP,CN=Public Key Services,CN=Services,%6%10

CSURL_ADDTOCRLCDP -- 8

2: 0:http://%1/CertEnroll/%3%8%9.crl

3: 6:http://pki.addb.labs.com/CertData/%3%8%9.crl

CSURL_ADDTOCERTCDP -- 2

CSURL_ADDTOFRESHESTCRL -- 4
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-10*

Hello Ania D,

Thank you for posting in Q&A forum.  

Did you mean root CA certificate is not in the Configuration partition on the Domain Controller?  

If so, you can try to copy the root CA certificate to Domain Controller and try the commands.

Note: If the path in the CMD is not the current path of the root CA certificate file, please use the full path of the root CA certificate:

certutil -dspublish -f <the full path of the certificate>

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
