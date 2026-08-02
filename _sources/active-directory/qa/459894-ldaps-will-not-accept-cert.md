---
title: "LDAPS will not accept cert"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/459894/ldaps-will-not-accept-cert
question_id: 459894
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAPS will not accept cert

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/459894/ldaps-will-not-accept-cert (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been working on this issue for three days now and no matter what I do, I can not get this LDAP issue fixed.  

We have a brand new domain controller in our org, and all I want to do is enable LDAPS authentication. This should be a simple process and for whatever reason it is not.  

Using Nettools, it clearly shows that port 636 is open on this DC, so it's not a network issue.  

I do, however, constantly get error 1220 in the event log:  

```
LDAP over Secure Sockets Layer (SSL) will be unavailable at this time because the server was unable to obtain a certificate. 

Additional Data 
Error value:
8009030e No credentials are available in the security package
```

I do however very clearly have certificates installed on the server and they are on my local machine I'm testing from too. It just doesn't work. I've tried installing the AD CS role, nothing. Right now i'm using self signed certs and CAs from openssl on another machine, and even that won't work. The server just will not use the cert i'm providing for LDAPS.  

Keep in mind, my testing is done from mmc.exe as this server is running datacenter 2019 core (no desktop)  

Here's some errors I get with these certs:  

```
This root certificate appears to be trusted by the remote computer. To ensure this root certificate is valid on the remote computer, verify this root certificate on that computer.
```

It should be? How do I verify this without a GUI  

```
This CA Root certificate is not trusted because it is not in the Trusted Root Certification Authorities store.
```

Okay but it IS in the trusted root certification authorities store. What?  

I even followed this guide step by step, nothing. https://help.hostingcontroller.com/Enterprise/default.aspx  

I should add, this is the bind error I get:  

```
ld = ldap_sslinit("dc-prime.compasshealthcenter.net", 636, 1);
Error 81 = ldap_set_option(hLdap, LDAP_OPT_PROTOCOL_VERSION, 3);
Error 81 = ldap_connect(hLdap, NULL);
Server error: 
Error : Fail to connect to dc-prime.compasshealthcenter.net.
```

Genuinely no idea what to do next. Any help is heavily appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-11*

Hi Riley,  

The error  ERR: 0x40 - The revocation status of the certificate or one of the certificates in the certificate chain is unknown,  happens when the revocation test is unable to connect and\or download the CRL specified in the CRL Distribution Point specified in the dc-prime certificate.  

Confirm that the CRL URL accessible from the workstation connecting to the server.  

Check out this article that could help with the troubleshooting https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-02*

Hello @Anonymous  ,    

Thank you for posting here.    

Hope the information above provided by GaryNebbett is helpful to you.    

If it is a sign-self cert:    

"Isssue by" and "Issue to" is the same.    

"Issuer" and "Subject" is the same.    

Certificate Chain is only one.    

For example, in my lab:    

    

    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-01*

Hello @Anonymous  ,    

In the "certutil -verify" output, the certificate seems to have an issuer of "CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net" and a subject of "CN=DC-PRIME.compasshealthcenter.net" (i.e. a similar but different name) and the main problem seems to be that certutil can't find a certificate with a subject name of "CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net".    

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-01*

UPDATE 1:  

I went thru the processes of removing all extraneous certs from my testing, removing the CA roles, restarting, and adding them back. Now I am able to connect with NetTools, but there's a cert chain issue it seems and I'm not sure how to resolve this. Heres the error:  

```
Verifying the Certificate Chain
Building certificate chain
 Certificate chain count: 1
 Certificate Chain 0
  Element Count: 1
  CertContext [0][0]
  Subject Name: DC-PRIME.compasshealthcenter.net
  SAN: DC-PRIME.compasshealthcenter.net
  Not Before: 1/07/2021  14:44
  Not After: 1/07/2022  14:44
   Certificate has Errors: 0x1000040
ERR: 0x40 - The revocation status of the certificate or one of the certificates in the certificate chain is unknown
ERR: 0x1000000 - The revocation status of the certificate or one of the certificates in the certificate chain is either offline or stale
   Certificate Status: 0x02
     0x2 - A key match issuer certificate has been found for this certificate
  ERR: Revocation check: Failed, Error: 0x80092013
   Revocation Server offline
ERR: Issues with the certicate chain, see above
ERR: Certificate verification would have failed for this connection
Error: ldap_sslinit failed with error: Error: (0x51) Cannot contact the LDAP server
```

If I export this key to my personal computer and run certutil -verify I get the following:  

```
Issuer:
    CN=dc-prime.compasshealthcenter.net
    DC=compasshealthcenter
    DC=net
  Name Hash(sha1): 55758060d1c853dbf76f17adb6e8a46007e2a017
  Name Hash(md5): 6c0e7ec0c8de04cb788a0592ab2c7124
Subject:
    CN=DC-PRIME.compasshealthcenter.net
  Name Hash(sha1): 81305be4b49289dd287b505b300ec5e107485203
  Name Hash(md5): f195def40686f8e61f3c8b7c7f5b9dca
Cert Serial Number: 1200000002e7565ff3f4f3b9d0000000000002

dwFlags = CA_VERIFY_FLAGS_CONSOLE_TRACE (0x20000000)
dwFlags = CA_VERIFY_FLAGS_DUMP_CHAIN (0x40000000)
ChainFlags = CERT_CHAIN_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT (0x40000000)
HCCE_LOCAL_MACHINE
CERT_CHAIN_POLICY_BASE
-------- CERT_CHAIN_CONTEXT --------
ChainContext.dwErrorStatus = CERT_TRUST_REVOCATION_STATUS_UNKNOWN (0x40)
ChainContext.dwErrorStatus = CERT_TRUST_IS_OFFLINE_REVOCATION (0x1000000)
ChainContext.dwErrorStatus = CERT_TRUST_IS_PARTIAL_CHAIN (0x10000)
SimpleChain.dwErrorStatus = CERT_TRUST_REVOCATION_STATUS_UNKNOWN (0x40)
SimpleChain.dwErrorStatus = CERT_TRUST_IS_OFFLINE_REVOCATION (0x1000000)
SimpleChain.dwErrorStatus = CERT_TRUST_IS_PARTIAL_CHAIN (0x10000)

CertContext[0][0]: dwInfoStatus=2 dwErrorStatus=1000040
  Issuer: CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net
  NotBefore: 7/1/2021 9:44 AM
  NotAfter: 7/1/2022 9:44 AM
  Subject: CN=DC-PRIME.compasshealthcenter.net
  Serial: 1200000002e7565ff3f4f3b9d0000000000002
  SubjectAltName: Other Name:DS Object Guid=04 10 13 80 36 ee b9 20 0b 45 b7 e8 c3 43 b9 80 4b 5b, DNS Name=DC-PRIME.compasshealthcenter.net
  Template: DomainController
  Cert: 092eb7929b8eac83c44c3ae8e71b0034e176c23b
  Element.dwInfoStatus = CERT_TRUST_HAS_KEY_MATCH_ISSUER (0x2)
  Element.dwErrorStatus = CERT_TRUST_REVOCATION_STATUS_UNKNOWN (0x40)
  Element.dwErrorStatus = CERT_TRUST_IS_OFFLINE_REVOCATION (0x1000000)
  Application[0] = 1.3.6.1.5.5.7.3.2 Client Authentication
  Application[1] = 1.3.6.1.5.5.7.3.1 Server Authentication

Exclude leaf cert:
  Chain: da39a3ee5e6b4b0d3255bfef95601890afd80709
Full chain:
  Chain: 092eb7929b8eac83c44c3ae8e71b0034e176c23b
Missing Issuer: CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net
  Issuer: CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net
  NotBefore: 7/1/2021 9:44 AM
  NotAfter: 7/1/2022 9:44 AM
  Subject: CN=DC-PRIME.compasshealthcenter.net
  Serial: 1200000002e7565ff3f4f3b9d0000000000002
  SubjectAltName: Other Name:DS Object Guid=04 10 13 80 36 ee b9 20 0b 45 b7 e8 c3 43 b9 80 4b 5b, DNS Name=DC-PRIME.compasshealthcenter.net
  Template: DomainController
  Cert: 092eb7929b8eac83c44c3ae8e71b0034e176c23b
A certificate chain could not be built to a trusted root authority. 0x800b010a (-2146762486 CERT_E_CHAINING)
------------------------------------
Incomplete certificate chain
Cannot find certificate:
    CN=dc-prime.compasshealthcenter.net, DC=compasshealthcenter, DC=net

ERROR: Verifying leaf certificate revocation status returned The revocation function was unable to check revocation because the revocation server was offline. 0x80092013 (-2146885613 CRYPT_E_REVOCATION_OFFLINE)
CertUtil: The revocation function was unable to check revocation because the revocation server was offline.

CertUtil: -verify command completed successfully.
```

Any idea what's gone wrong here? How do I identify what the revocation server is? From what I understand, that's the CA server I just installed and it's very clearly online.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-01*

Hello @Anonymous  ,    

The LDAP server does not need just a suitable certificate - it also needs the private key that matches the certificate. From what you have written, it seems possible that a missing private key is part of the problem.    

Gary
