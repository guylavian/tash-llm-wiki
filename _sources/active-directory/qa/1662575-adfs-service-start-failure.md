---
title: "ADFS service start failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662575/adfs-service-start-failure
question_id: 1662575
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 2
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS service start failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662575/adfs-service-start-failure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts,

We are not able to restart adfs service after activating new SSL certificate with "Set-AdfsSslCertificate -Thumbprint 'XXXXXXXXXXXACF1D94XXXXXXXXXXXXXXXXX" command. Below is the error we receive:

on powershell:

"Set-AdfsSslCertificate : Could not connect to net.tcp://localhost:1600/policy. The connection attempt lasted for a time span of 00:00:02.0287450. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:1600.

At line:1 char:1

-  Set-AdfsSslCertificate -Thumbprint 'ACF ...

- 

```

```

-  CategoryInfo : OpenError: (:) [Set-AdfsSslCertificate], EndpointNotFoundException

-  FullyQualifiedErrorId : Could not connect to net.tcp://localhost:1600/policy. The connection attempt lasted for a time span of 00:00:02.0287450. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:1600. ,Micr

osoft.IdentityServer.Management.Commands.SetSslCertificateCommand"

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

## Answers

_No answers on this thread._
