---
title: "New AD CS 2022 Issuing won't start because the revocation server is offline, but all troubleshooting steps have passed successfully."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003508/new-ad-cs-2022-issuing-wont-start-because-the-revo
question_id: 1003508
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# New AD CS 2022 Issuing won't start because the revocation server is offline, but all troubleshooting steps have passed successfully.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003508/new-ad-cs-2022-issuing-wont-start-because-the-revo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm currently in the process of standing up a Root CA and an Issuing CA in Windows Server 2022. The Root CA setup went fine, and I have both CA server publish their certificates and CRLs to an IIS server as per Microsoft’s documentation, but I'm having an issue with the Issuing CA server. After a reboot of the server, I could not start the AD CS service with the error: "The revocation function was unable to check revocation because the revocation server was offline. 0x80092013 (-2146885613 CRYPT_E_REVOCATION_OFFLINE)."  Looking into Event Viewer, I am shown multiple Event IDs 48 and 100 with the error: “Revocation status for a certificate in the chain for CA certificate 1 for Issuing CA could not be verified because a server is currently unavailable.  The revocation function was unable to check revocation because the revocation server was offline. 0x80092013 (-2146885613 CRYPT_E_REVOCATION_OFFLINE).”     

To begin my troubleshooting, I ran the command “certutil -setreg ca\CRLFlags +CRLF_REVCHECK_IGNORE_OFFLINE” so I could get the service running. I have doubled check both CDP and AIA locations and verified that there is no typo. Both CA servers have full access to the directory and IIS server where they publish these certificates. I have checked pkiview.msc, and all statuses show OK on both tiers.     

    

I have also tried reissuing the Issuing CA certificate with no luck. And following this [link][2] I have tried and confirmed each step of this troubleshooting guide.    

Running the command “certutil -f -urlfetch -verify "Issuing_Cert.crt" gives this output below:    

```
Issuer:  
    CN=RootCA  
    DC=###  
    DC=###  
    DC=###  
  Name Hash(sha1): 11b88de194daf1aa86ad8181262f59e944da9b01  
  Name Hash(md5): 10f669401ff14aa501f6c1828b54e88e  
Subject:  
    CN=IssuingCA  
    DC=###  
    DC=###  
    DC=###  
  Name Hash(sha1): cec2a6328c3ccd124af25610cc2513825b952532  
  Name Hash(md5): 49e408f9d701676c219bbeae2851f4a5  
Cert Serial Number: 2b00000007f3c3bf591575b554000000000007  
  
dwFlags = CA_VERIFY_FLAGS_ALLOW_UNTRUSTED_ROOT (0x1)  
dwFlags = CA_VERIFY_FLAGS_IGNORE_OFFLINE (0x2)  
dwFlags = CA_VERIFY_FLAGS_FULL_CHAIN_REVOCATION (0x8)  
dwFlags = CA_VERIFY_FLAGS_CONSOLE_TRACE (0x20000000)  
dwFlags = CA_VERIFY_FLAGS_DUMP_CHAIN (0x40000000)  
ChainFlags = CERT_CHAIN_REVOCATION_CHECK_CHAIN (0x20000000)  
HCCE_LOCAL_MACHINE  
CERT_CHAIN_POLICY_BASE  
-------- CERT_CHAIN_CONTEXT --------  
ChainContext.dwInfoStatus = CERT_TRUST_HAS_PREFERRED_ISSUER (0x100)  
  
SimpleChain.dwInfoStatus = CERT_TRUST_HAS_PREFERRED_ISSUER (0x100)  
  
CertContext[0][0]: dwInfoStatus=102 dwErrorStatus=0  
  Issuer: CN=RootCA, DC=###, DC=###, DC=###  
  NotBefore: 9/9/2022 10:34 AM  
  NotAfter: 9/8/2027 10:34 AM  
  Subject: CN=Issuing CA, DC=###, DC=###, DC=###  
  Serial: 2b00000007f3c3bf591575b554000000000007  
  Template: SubCA  
  Cert: 05ccadb7ce4f6f1c92eedb59748163a7532037dd  
  Element.dwInfoStatus = CERT_TRUST_HAS_KEY_MATCH_ISSUER (0x2)  
  Element.dwInfoStatus = CERT_TRUST_HAS_PREFERRED_ISSUER (0x100)  
  ----------------  Certificate AIA  ----------------  
  Verified "Certificate (0)" Time: 0 61f97870555401f3f4b9f152f4c1d40fe5e3b87b  
    [0.0] http://pki. #########/pki/rootca.crt  
  
  ----------------  Certificate CDP  ----------------  
  Verified "Base CRL (04)" Time: 0 72031475f7b9257a6052ced3e22368269fc35ad3  
    [0.0] http://pki. #########/pki/rootca.crl  
  
  ----------------  Base CRL CDP  ----------------  
  No URLs "None" Time: 0 (null)  
  ----------------  Certificate OCSP  ----------------  
  No URLs "None" Time: 0 (null)  
  --------------------------------  
    CRL 04:  
    Issuer: CN=RootCA, DC=###, DC=###, DC=###  
    ThisUpdate: 9/9/2022 8:56 AM  
    NextUpdate: 9/9/2023 9:16 PM  
    CRL: 72031475f7b9257a6052ced3e22368269fc35ad3  
  
CertContext[0][1]: dwInfoStatus=10c dwErrorStatus=0  
  Issuer: CN=RootCA, DC=###, DC=###, DC=###  
  NotBefore: 9/7/2022 4:15 PM  
  NotAfter: 9/7/2032 4:25 PM  
  Subject: CN=RootCA, DC=###, DC=###, DC=###  
  Serial: 291dd20f48c5bea24e43e065f0c1cac3  
  Template: CA  
  Cert: 61f97870555401f3f4b9f152f4c1d40fe5e3b87b  
  Element.dwInfoStatus = CERT_TRUST_HAS_NAME_MATCH_ISSUER (0x4)  
  Element.dwInfoStatus = CERT_TRUST_IS_SELF_SIGNED (0x8)  
  Element.dwInfoStatus = CERT_TRUST_HAS_PREFERRED_ISSUER (0x100)  
  ----------------  Certificate AIA  ----------------  
  No URLs "None" Time: 0 (null)  
  ----------------  Certificate CDP  ----------------  
  No URLs "None" Time: 0 (null)  
  ----------------  Certificate OCSP  ----------------  
  No URLs "None" Time: 0 (null)  
  --------------------------------  
  
Exclude leaf cert:  
  Chain: 5e9ce809c8f8728ec1a65b2cad97ad21ef61f30d  
Full chain:  
  Chain: 786a3a4a2e027fbba6caa443cd090f0cb8800a55  
------------------------------------  
Verified Issuance Policies: None  
Verified Application Policies: All  
Cert is a CA certificate  
Leaf certificate revocation check passed  
CertUtil: -verify command completed successfully.
```

If someone could let me know what I might be missing so I can run this service with CRL list checking back on, that would be great.  [2]: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc774550(v=ws.10)?redirectedfrom=MSDN

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-02-15*

Hi, it's most likeky that crl files on the root CA server have been expired. To update them, proceed with the following steps:

1.       Start Offline Root CA

2.       Open Administrative Command Prompt

3.       Type Certutil –crl

4.       Copy new crl files to a file share

5.       Go to Enterprise subordinate CA

6.       Copy new crl files from file share to PKI folder and System32\Certenroll

7.       Type certutil –dspublish *.crl (one by one)

Good luck, 

Thomas
