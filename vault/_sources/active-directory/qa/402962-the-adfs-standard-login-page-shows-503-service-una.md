---
title: "The ADFS standard login page shows 503 service unavailable"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/402962/the-adfs-standard-login-page-shows-503-service-una
question_id: 402962
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# The ADFS standard login page shows 503 service unavailable

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/402962/the-adfs-standard-login-page-shows-503-service-una (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ADFS running on Windows 2019 in a cluster containing two hosts.    

After changing the certificate for SSL and Service-Communications using the following commands:     

Set-AdfsSslCertificate –Thumbprint XXX    

Set-AdfsCertificate -CertificateType "Service-Communications" –Thumbprint XXX    

Restarted the adfs service     

The login page shows now:    

    

In the event log of ADFS I can see the following:    

There was an error in enabling endpoints of Federation Service. Fix configuration errors using PowerShell cmdlets and restart the Federation Service.     

Additional Data     

Exception details:     

Failed to start endpoint:    

https://+:49443/adfs/portal/    

https://+:443/adfs/portal/    

System.Net.HttpListenerException (0x80004005): Access is denied    

   at System.Net.HttpListener.AddAllPrefixes()    

   at System.Net.HttpListener.Start()    

   at Microsoft.IdentityServer.WebHost.HttpListenerBase.Start(UInt32 contextPoolSize)    

   at Microsoft.IdentityServer.ServiceHost.STSService.StartListener(Type listener, Int32 port, Int32 clientPort, Boolean passiveEnabled, Boolean oAuthEnabled, Boolean enablePasswordUpdate, String path)    

The adfssrv service is running with a gmsa account and was not changed.    

Any idea why "Access is denied" is happening after a certificate change?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-31*

If anyone is still having issues with this, I would check the following:

HTTP Error 503. The Service is unavailable

Cause #1: Invalid base address entered in the SAML login redirection page field.

Solution #1: Make sure your base addresses match your application and ADFS. For example, if ADFS was assigned `https://sso.contosso.com/` your application should reflect the same address, `https://sso.contosso.com/`. 

Cause #2: The ADFS services are not running.

Solution #2: Check your service account has up-to-date credentials and start or restart your ADFS services.

Cause #3: Not pointing to the correct resource endpoint, specifically `/ls`.

Solution#3: Make sure your address is also pointing to the correct resources, `/adfs/ls`.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

I updated the certificate, followed all steps, ensured the adfs service account has Read permissions set correctly on the certificate.   

I am still getting the below error:  

Service Unavailable

HTTP Error 503. The service is unavailable.  

Any help would be appreciated,   

TIA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-26*

Thanks for you reply :-)  

I was checking the permission of the certificate and everything was correctly set.   

For me the event log entry with: System.Net.HttpListenerException (0x80004005): Access is denied was not really true.  

In another tutorial (for exchange of certificate) I found the hint with Set-AdfsAlternateTlsClientBinding and after setting the same certificate everything was fine.
