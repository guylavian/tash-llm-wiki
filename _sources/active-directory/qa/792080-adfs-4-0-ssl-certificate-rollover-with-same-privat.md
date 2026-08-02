---
title: "ADFS 4.0 SSL certificate rollover with same private key"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/792080/adfs-4-0-ssl-certificate-rollover-with-same-privat
question_id: 792080
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ADFS 4.0 SSL certificate rollover with same private key

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/792080/adfs-4-0-ssl-certificate-rollover-with-same-privat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

Last year I ordered a new SSL certificate with a lifetime of 2 years (cheaper).  

Since certificates are only be valid for one year, it was necessary to renew it now after one year, but with the option to keep the same private key, I just received a new .cer file from my certifier.  

So I created a new pfx file with the private key, the .cer file and the ca bundle file like in the years before.  

But when importing the pfx file with certutil I get an error message now:  

certutil -importpfx example_com.pfx AT_KEYEXCHANGE  

CertUtil: -importPFX-Befehl ist fehlgeschlagen: 0x80070056 (WIN32: 86 ERROR_INVALID_PASSWORD)  

CertUtil: Das angegebene Netzwerkkennwort ist falsch.  

The password in the pfx file is for sure ok, I successfully tried to import the certificate on a computer where it was not installed before.  

So it is necessary to only import the .cer file, but how is this possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-26*

Hello  

I tried it with an empty password without success.  

Then I tried to create the PFX file with another OpenSSL Version on another computer  

("OpenSSL 1.1.1l  24 Aug 2021" instead of "OpenSSL 3.0.2 15 Mar 2022").  

With this OpenSSL version it was suddenly successful.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-04-11*

Hi,  

Thank you for posting question to Microsoft Q&A forum.  

After researching, I found below two threads that contain the similar issue as yours.  

The issue was resolved by a blank password. You can have a try to see if it helps.  

https://stackoverflow.com/questions/2452301/windows-asks-for-p12-password-when-installing-p12-key-generated-by-openssl  

https://stackoverflow.com/questions/48068526/cannot-install-mitmproxy-certificate-on-windows-10  

Best regards,  

If the Answer is helpful, please click "Accept Answer" and upvote it. Thanks.
