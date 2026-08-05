---
title: "Can ADFS SSO work with both NLB and ALB?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5843588/can-adfs-sso-work-with-both-nlb-and-alb
question_id: 5843588
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Can ADFS SSO work with both NLB and ALB?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5843588/can-adfs-sso-work-with-both-nlb-and-alb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When ADFS is configured for SSO on a system with multiple SQL servers that has NLB and ALB enabled, the user continues to get a repeated login screen

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-30*

Yes, AD FS SSO can work in environments that use both network load balancers (NLB) and application load balancers (ALB), but repeated login prompts indicate an SSO/authentication flow problem rather than an incompatibility with the load balancers.

From the provided context, repeated prompts are typically caused by AD FS not being able to complete or persist an SSO session correctly, or by the application/auth request forcing re‑authentication. Use these checks:

-  Verify AD FS is healthy and sign‑in works directly

-  Enable and test IdP‑initiated sign‑on internally:

```
Set-AdfsProperties -EnableIdPInitiatedSignonPage $true
```

-  From inside the network, browse to:
     `https://<FederationInstance>/adfs/ls/idpinitiatedsignon`

-  Sign in with a valid user.

-  If this fails, follow the “Users can't log in the target site or service” section to check:

-  AD FS service status in Server Manager → Tools → Services → “Active Directory Federation Services” is Running.

-  Endpoints are enabled in AD FS Management Console → Service → Endpoints.

-  Check whether the issue is at the AD FS sign‑in page or at the application

-  If the error URL shows the AD FS service name (for example `fs.contoso.com`), troubleshoot AD FS itself as above.

-  If the error URL shows the application or its IP, troubleshoot the relying party / application configuration.

-  Check for unexpected NTLM/forms prompts (looping logon screens)
   Repeated login prompts often mean Windows Integrated Authentication (WIA) is not working as expected:

-  On client browsers (Internet Options):

-  Advanced → ensure Enable Integrated Windows Authentication is enabled.

-  Security → Local intranet → Sites → Advanced → ensure the AD FS URL is listed.

-  Security → Local intranet → Custom level → Automatic logon only in Intranet zone.

-  On AD FS, verify WIA settings:

-  Check `WindowsIntegratedFallbackEnabled`:

```
Get-ADFSGlobalAuthenticationPolicy | fl WindowsIntegratedFallbackEnabled
```

-  If True, forms‑based auth is expected for non‑WIA clients.

-  Ensure the browser user agent is in `WIASupportedUserAgents`:

```
Get-ADFSProperties | Select -ExpandProperty WIASupportedUserAgents
```

       Add missing user agents and update with `Set-ADFSProperties -WIASupportedUserAgents $wiaStrings` as shown in the context.

-  Check the authentication request from the application

-  If the application or ALB is sending auth requests that explicitly demand forms auth or fresh login, AD FS will keep prompting:

-  For WS‑Federation, see if the request includes `wauth= urn:oasis:names:tc:SAML:1.0:am:password` (forces password prompt).

-  For SAML, see if `samlp:AuthnContextClassRef` is `urn:oasis:names:tc:SAML:2.0:ac:classes:Password`.

-  For Microsoft Online Services, the `PromptLoginBehavior` setting can cause repeated prompts; adjust via:

```
Connect-MgGraph -scopes Domain.ReadWrite.All, Directory.ReadWrite.All
     $tdo= Get-MgDomainFederationConfiguration -DomainID 
     Update-MgDomainFederationConfiguration -DomainId  -InternalDomainFederationId $tdo.Id -PromptLoginBehavior 
     Disconnect-MgGraph
```

-  Validate relying party and client configuration
   If the application is configured as a relying party or via Application Groups:

-  Retrieve relying party and client settings and compare with what the app actually sends:

```
$rp = Get-AdfsWebApiApplication ResourceID
     # For public client
     $client = Get-AdfsNativeClientApplication ClientName
     # Or for confidential client
     $client = Get-AdfsServerApplication ClientName
```

-  Confirm that:

-  Relying party ID matches `$rp.Identifier`.

-  Relying party redirect URI matches `$rp.WSFedEndpoint` or `$rp.SamlEndpoints`.

-  Client ID matches `$client.ClientId`.

-  Client redirect URI matches `$client.RedirectUri`.

-  For OAuth requests, ensure parameters match AD FS configuration:
     `https://sts.contoso.com/adfs/oauth2/authorize?response_type=code&client_id=ClientID&redirect_uri=https://www.TestApp.com&resource=https://www.TestApp.com`

-  Consider load balancer behavior
   While not detailed in the context, repeated prompts in an NLB/ALB scenario are commonly triggered by:

-  Requests not consistently hitting the same AD FS node (no session affinity) while using cookies bound to a specific node.

-  Name resolution or routing misconfiguration between internal NLB and perimeter/WAP as described in the AD FS farm design guidance.
     Ensure the federation service name (for example `fs.contoso.com`) resolves consistently and that WAP or other proxies correctly forward to the AD FS farm.

If IdP‑initiated sign‑on works reliably and the prompts only occur when going through the application, focus on the relying party configuration and the authentication request parameters rather than NLB/ALB themselves.

References:

-  Troubleshoot SSO issues with Active Directory Federation Services (AD FS)

-  Legacy AD FS Federation Server Farm Using SQL Server
