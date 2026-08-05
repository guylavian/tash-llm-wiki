---
title: "ADFS service does not start due to certificate expiry"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187991/adfs-service-does-not-start-due-to-certificate-exp
question_id: 2187991
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS service does not start due to certificate expiry

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187991/adfs-service-does-not-start-due-to-certificate-exp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts,

We are not able to restart adfs service after activating new SSL certificate with "Set-AdfsSslCertificate -Thumbprint 'XXXXXXXXXXXACF1D94XXXXXXXXXXXXXXXXX" command. Below is the error we receive:

on powershell:

"Set-AdfsSslCertificate : Could not connect to net.tcp://localhost:1600/policy. The connection attempt lasted for a time span of 00:00:02.0287450. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:1600. 

At line:1 char:1 

-  Set-AdfsSslCertificate -Thumbprint 'ACF ... 

- 

```
+ CategoryInfo          : OpenError: (:) [Set-AdfsSslCertificate], EndpointNotFoundException 

    + FullyQualifiedErrorId : Could not connect to net.tcp://localhost:1600/policy. The connection attempt lasted for a time span of 00:00:02.0287450. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:1600. ,Micr 

   osoft.IdentityServer.Management.Commands.SetSslCertificateCommand"
```

on event viewer and server manager:

There was an error in enabling endpoints of Federation Service. Fix configuration errors using PowerShell cmdlets and restart the Federation Service. 

Additional Data 

Exception details: 

System.ArgumentNullException: Value cannot be null.

Parameter name: certificate

   at System.IdentityModel.Tokens.X509SecurityToken..ctor(X509Certificate2 certificate, String id, Boolean clone, Boolean disposable)

   at Microsoft.IdentityServer.Service.Configuration.MSISSecurityTokenServiceConfiguration.Create(Boolean forSaml, Boolean forPassive)

   at Microsoft.IdentityServer.Service.Policy.PolicyServer.Service.ProxyPolicyServiceHost.ConfigureWIF()

   at Microsoft.IdentityServer.Service.SecurityTokenService.MSISConfigurableServiceHost.Configure()

   at Microsoft.IdentityServer.Service.Policy.PolicyServer.Service.ProxyPolicyServiceHost.Create()

   at Microsoft.IdentityServer.ServiceHost.STSService.StartProxyPolicyStoreService(ServiceHostManager serviceHostManager)

   at Microsoft.IdentityServer.ServiceHost.STSService.OnStartInternal(Boolean requestAdditionalTime)

Would you please help?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-03*

Thanks Neuvi, I have asked the question again in Q&A forum.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-03*

Hi yavuzdiler,

Thank you for posting on the Microsoft Community Forum.

From the description above, I understand that your question is about ADFS.

Since there are no developers working with ADFS on this forum. For quick and efficient handling of your problem, I recommend asking your question again in the Q&A forum, where a dedicated technician will give you a professional and efficient answer.

Here is the link to the Q&A forum.

Q&A - Microsoft Q&A

Click the "Ask a question" button at upper right corner to ask your question, and select "ADFS" tag and other tags related to your productions.

I hope the above information is helpful.

If you have any questions or concerns, please feel free to let us know.

All the best

Neuvi Jiang
