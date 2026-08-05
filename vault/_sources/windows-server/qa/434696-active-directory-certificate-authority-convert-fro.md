---
title: "active directory certificate authority - convert from sha1 to sha2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/434696/active-directory-certificate-authority-convert-fro
question_id: 434696
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# active directory certificate authority - convert from sha1 to sha2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/434696/active-directory-certificate-authority-convert-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello,  

we have our Certificate authority installed and configured since Windows Server 2003, and now, it's in Windows Server 2012 R2. And its cryptographic algorithms use SHA1. Which is considered as weak encryption.   

And all the generated certificates are not accepted for almost all systems (modern webbrowsers, systems...)  

We would like to know, if converting to SHA2 (256), would impact the already delivered certificates or not?  

Thank you in advance,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-17*

Hello @Anonymous       

Thank you so much for your precious help    

Our CA is KSP...    

I'll proceed with changing to SHA2 during this week and keep you updated,     

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-16*

@Anonymous    @Vadims Podāns   thank you both for your answers, especially @Anonymous       

I just would like to know, how can i know, what service provider is used now?    

I found on internet, that i should use some commands:    

certutil -csplist    

certutil -csptest    

and other commands, but none of them said precisely what provider we have?    

thank you in  advance for your help

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-15*

Hello @LotfiBOUCHERIT-4930,  

Thank you for posting here.  

Hope the information provided by Crypt32 is helpful to you.  

Q: We would like to know, if converting to SHA2 (256), would impact the already delivered certificates or not?  

A: From the following article, we can see:  

What about certificates that have already been issued?   

We are NOT going to revoke any CA certificates that have already been issued so existing certificates will remain unaffected.  

Certificate Services – Migrate from SHA1 to SHA2 (SHA256)  

https://www.petenetlive.com/KB/Article/0001243  

Reference  

Migrate Windows CA from CSP to KSP and from SHA-1 to SHA-256: Part 1  

https://devblogs.microsoft.com/scripting/migrate-windows-ca-from-csp-to-ksp-and-from-sha-1-to-sha-256-part-1/  

Hope the information above is also helpful.  

Should you have any question or concern, please feel free to let us know.  

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.  

Best Regards,  

Daisy Zhou  

============================================  

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-06-14*

If it is root CA, then its own SHA1 signature is acceptable, because clients use explicit/direct trust. What is not acceptable -- to use SHA1 in certificates that use implicit/indirect trust through chain. Since your CA was migrated from original Windows Server 2003, you have to migrate the key from legacy CSP to modern KSP in order to utilize SHA2 signatures as outlined in the following article: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn771627(v=ws.11). You cannot use SHA2 until you migrate keys to KSP.    

there are instructions, on how to force CA to use modern signatures:    

```
certutil -setreg ca\csp\CNGHashAlgorithm SHA256
```
