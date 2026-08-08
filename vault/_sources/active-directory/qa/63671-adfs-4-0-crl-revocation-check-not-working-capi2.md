---
title: "ADFS 4.0 CRL Revocation Check not working (CAPI2)."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/63671/adfs-4-0-crl-revocation-check-not-working-capi2
question_id: 63671
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 4.0 CRL Revocation Check not working (CAPI2).

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/63671/adfs-4-0-crl-revocation-check-not-working-capi2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an ADFS 4.0 server,     

however, when trying to perform the Certificate Revocation Checks, i notice that the CAPI2 is trying to get to the internet without using the winhttp proxy settings. Unfortunately, our company policy is that no device can have direct internet access, and all must pass through a HTTP Proxy server.     

I already tried following explained at the end of this document https://learn.microsoft.com/en-us/troubleshoot/browsers/description-of-cryptography-api-proxy-from-crl    

If you do not want to set a proxy for each logged-on user, you can set up a machine-wide proxy by setting the ProxySettingsPerUser key to 0.    

TABLE 2    

Registry Key HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\InternetSettings\ProxySettingsPerUser    

Type REG DWORD    

Value    

0: per-machine proxy    

1 or no value: per-user    

Blockquote    

netsh winhttp show proxy looks fine but the CRL Checks still dont work.    

I know we can disable the revocation check via the following PowerShell cmdlet, but i would really appreciate a better solution and letting ADFS perform the CRL check.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-30*

Hi Alex-5595  

¿Did you try with this command, to import internet explorer setting to machine (you should check exceptions for local access without proxy)?  

netsh winhttp import proxy source=ie

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-28*

Hi as for that we use a extra account for adfs service we had to set up proxy settings for this sa. changing to machine proxy didnt work either.  

thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-08-11*

Hello Piaudonn, there these error messages

```
+ System 

  - Provider 

   [ Name]  Microsoft-Windows-CAPI2 
   [ Guid]  {5bbca4a8-b209-48dc-a8c7-b23d3e5216fb} 

   EventID 53 

   Version 0 

   Level 2 

   Task 53 

   Opcode 2 

   Keywords 0x4000000000000036 

  - TimeCreated 

   [ SystemTime]  2020-08-10T12:40:27.774475300Z 

   EventRecordID 108 

  - Correlation 

   [ ActivityID]  {35C62FE3-8389-4820-8800-0080010000CF} 

  - Execution 

   [ ProcessID]  2412 
   [ ThreadID]  720 

   Channel Microsoft-Windows-CAPI2/Operational 

   Computer xxxxxxxxxxxxxxxxxxxxxxx

  - Security 

   [ UserID]  S-1-5-21-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

- UserData 

  - CryptRetrieveObjectByUrlWire 

  - URL http://crl3.digicert.com/DigiCertGlobalRootCA.crl 

   [ scheme]  http 

  - Object 

   [ type]  CONTEXT_OID_CRL 
   [ constant]  2 

   Timeout PT15S 

  - Flags 

   [ value]  202005 
   [ CRYPT_RETRIEVE_MULTIPLE_OBJECTS]  true 
   [ CRYPT_WIRE_ONLY_RETRIEVAL]  true 
   [ CRYPT_LDAP_SCOPE_BASE_ONLY_RETRIEVAL]  true 
   [ CRYPT_PROXY_CACHE_RETRIEVAL]  true 

  - AuxInfo 

   [ maxUrlRetrievalByteCount]  104857600 
   [ fProxyCacheRetrieval]  true 

  - AdditionalInfo 

  - NetworkConnectivityStatus 

   [ value]  1 
   [ _SENSAPI_NETWORK_ALIVE_LAN]  true 

  - Action 

   [ name]  Call_WinHttpSendRequest 
  - Error The server name or address could not be resolved 

   [ value]  2EE7 

  - EventAuxInfo 

   [ ProcessName]  Microsoft.IdentityServer.ServiceHost.exe 

  - CorrelationAuxInfo 

   [ TaskId]  {15140D67-0627-40B3-8D5E-137AD20679F2} 
   [ SeqNumber]  6 

  - Result 

   [ value]  2EE7
```

and

```
- Result The revocation function was unable to check revocation because the revocation server was offline. 

   [ value]  80092013
```

Its like CAPI2 ignores the proxy settings.
