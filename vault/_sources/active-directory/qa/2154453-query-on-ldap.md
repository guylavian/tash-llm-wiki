---
title: "Query on LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154453/query-on-ldap
question_id: 2154453
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Query on LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154453/query-on-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I want to generate an LDAP CSR request. I have the following text file, which I will save with the .inf extension (i.e., ldap.inf). From the command prompt, I will execute the following command:

```
certreq -new ldap.inf ldapcsr.req
```

Once I have the certificate, I will run the following command on the same VM where I generated the CSR request:

```
certreq -accept C:\Temp\cert.crt
```

Do I need to include the SAN name ldap.contoso.com? Which of the following is correct? (Please refer the last line in my text file)

```
_continue_ = "&dns=ldap.contoso.com&dns=dc01.contoso.com&dns=dc02.contoso.com&dns=dc03.contoso.com"

or 

 _continue_ = "&dns=dc01.contoso.com&dns=dc02.contoso.com&dns=dc03.contoso.com"
```

Are the following lines correctly added in my text file?

```
Subject = "CN=ldap.contoso.com" ; Replace with the FQDN of the DC 
C = US 
ST = MYST 
L = MYL 
O = Contoso, Inc.
```

My Text File

```
;----------------- request.inf -----------------
;----- requested on ALL DCs-----

[Version]

Signature="$Windows NT$

[NewRequest]

Subject = "CN=ldap.contoso.com" ; replace with the FQDN of the DC
C = US
ST = MYST
L = MYL
O = Contoso, Inc.
KeySpec = 1
KeyLength = 2048
; Can be 1024, 2048, 4096, 8192, or 16384.
; Larger key sizes are more secure, but have
; a greater impact on performance.
Exportable = TRUE
MachineKeySet = TRUE
SMIME = False
PrivateKeyArchive = FALSE
UserProtected = FALSE
UseExistingKeySet = FALSE
ProviderName = "Microsoft RSA SChannel Cryptographic Provider"
ProviderType = 12
RequestType = PKCS10
KeyUsage = 0xa0

[EnhancedKeyUsageExtension]

OID=1.3.6.1.5.5.7.3.1 ; Server Authentication
OID=1.3.6.1.5.5.7.3.2 ; Client Authentication

[Extensions]
; If your client operating system is Windows Server 2008, Windows Server 2008 R2, Windows Vista, or Windows 7
; SANs can be included in the Extensions section by using the following text format. Note 2.5.29.17 is the OID for a SAN extension.

2.5.29.17 = "{text}"
_continue_ = "&dns=ldap.contoso.com&dns=dc01.contoso.com&dns=dc02.contoso.com&dns=dc03.contoso.com"
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-05*

Can i use like this.

Subject = "CN=ldap.contoso.com"m C = US, OU=Domain Controllers, ST = MYST, L = MYL, O = Contoso, Inc.,"

continue = "&dns=ldap.contoso.com&dns=dc01.contoso.com&dns=dc02.contoso.com&dns=dc03.contoso.com"

```
;----------------- request.inf -----------------
;----- requested on ALL DCs-----

[Version]

Signature="$Windows NT$

[NewRequest]

Subject = "CN=ldap.contoso.com"m C = US, OU=Domain Controllers, ST = MYST, L = MYL, O = Contoso, Inc.," ;
KeySpec = 1
KeyLength = 2048
; Can be 1024, 2048, 4096, 8192, or 16384.
; Larger key sizes are more secure, but have
; a greater impact on performance.
Exportable = TRUE
MachineKeySet = TRUE
SMIME = False
PrivateKeyArchive = FALSE
UserProtected = FALSE
UseExistingKeySet = FALSE
ProviderName = "Microsoft RSA SChannel Cryptographic Provider"
ProviderType = 12
RequestType = PKCS10
KeyUsage = 0xa0

[EnhancedKeyUsageExtension]

OID=1.3.6.1.5.5.7.3.1 ; Server Authentication
OID=1.3.6.1.5.5.7.3.2 ; Client Authentication

[Extensions]
; If your client operating system is Windows Server 2008, Windows Server 2008 R2, Windows Vista, or Windows 7
; SANs can be included in the Extensions section by using the following text format. Note 2.5.29.17 is the OID for a SAN extension.

2.5.29.17 = "{text}"
_continue_ = "&dns=ldap.contoso.com&dns=dc01.contoso.com&dns=dc02.contoso.com&dns=dc03.contoso.com"
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-02-04*

Follow https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
