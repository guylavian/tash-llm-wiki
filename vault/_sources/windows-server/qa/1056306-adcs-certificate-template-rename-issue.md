---
title: "ADCS Certificate template rename issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1056306/adcs-certificate-template-rename-issue
question_id: 1056306
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# ADCS Certificate template rename issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1056306/adcs-certificate-template-rename-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, everyone!    

I've decided to rename previously created certificate template. In the Certificate Templates Console I've chosen the template and right-click->Change Names.     

I've left Template name intact and changed Template display Name - that was my intent, in order to allow subsequent autoenrollment of the previously issued certificates.    

I am using Get-CertificateTemplate cmdlet from PSPKI module to get template info and what I see confuses me (please pay attention to the OID value).    

Before rename:    

Name             : TESTSmartcardLogon    

DisplayName : TEST Smartcard Logon    

OID                : TEST Smartcard Logon (1.3.6.1.4.1.311.21.8.7291409.13903173.7816371.15015920.7385279.16.9821269.13536056)    

After rename:    

Name             : TESTSmartcardLogon    

DisplayName : TEST New Smartcard Logon    

OID                : TEST Smartcard Logon (1.3.6.1.4.1.311.21.8.7291409.13903173.7816371.15015920.7385279.16.9821269.13536056)    

DisplayName field has clearly been updated by the procedure. But the OID field still contains old Display Name. WTF???     

I've crawled all over the PKI container in my AD Configuration partition with the ADSI Editor and was unable to find anything.     

There is 'cn' attribute with value 'TESTSmartcardLogon' (which I believe is mapped to the 'Name' field at the Get-CertificateTemplate output).    

There is 'DisplayName' attribute with value 'TEST New Smartcard Logon' (which is clearly mapped to the 'DisplayName' field).    

And finally there is 'msPKI-Cert-Template-OID' attribute with value '1.3.6.1.4.1.311.21.8.7291409.13903173.7816371.15015920.7385279.16.9821269.13536056'. Until today I believed that the OID field at the Get-CertificateTemplate output was constructed as a concatenation of string values of the two attributes - DisplayName and OID. Now it seems I'm wrong.    

And my question is - how do we get this OID value at the Get-CertificateTemplate output? Where on earth this information (old DisplayName) could be dug from? Is there any sort of local cache on the CA itself? I'm at loss. Any input would be much appreciated.

## Answers

_No answers on this thread._
