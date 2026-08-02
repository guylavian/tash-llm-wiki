---
title: "Would like to know how to get ADFS pass domain\\username to Sharepoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/349211/would-like-to-know-how-to-get-adfs-pass-domainuser
question_id: 349211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Would like to know how to get ADFS pass domain\username to Sharepoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/349211/would-like-to-know-how-to-get-adfs-pass-domainuser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was given a Sharepoint 2013 server (on windows server 2012 r2) and an ADFS server (Windows server 2019). I followed the guide here:  

https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/implement-saml-based-authentication-in-sharepoint-server.

I am able to use email address to authenticate. Here's the current scenario.  

-  Open https://myapp-mycompany.com.my from client browser  

-  Auto redirects to ADFS page https://adfs.mycompany.com.my/adfs/ls/ for authentication using email  

-  Once authenticated redirects back to Sharepoint with the email address as the login credential

I want to pass domain\username to Sharepoint rather than email address. How do i achieve this?  

Take note I'm new to ADFS and would appreciate the plain language.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

Here's the settings. It's practically the same based on the guide above.

On the AD FS server, start PowerShell and run the following script:

STEP 1: Create the relying party

Name of the Relying Party

$name = "myserver-TrustedIdentityProvider"

Unique identifier of the Relying Party (in SharePoint it's referred to as the realm)

$identifier = "urn:myserver:mycompany.com.my"

Authority that authenticates users

$identityProvider = "Active Directory"

SharePoint URL where user is redirected upon successful authentication

$redirectURL = "https://myapp-mycompany.com.my/_trust/"

Allow everyone to use this relying party

$allowEveryoneRule = '=> issue (Type = "http://schemas.microsoft.com/authorization/claims/permit", value = "true");'

Create the Relying Party

Add-ADFSRelyingPartyTrust -Name $name -Identifier $identifier -ClaimsProviderName $identityProvider -Enabled $true -WSFedEndpoint $redirectURL -IssuanceAuthorizationRules $allowEveryoneRule -Confirm:$false

STEP 2: Add claim rules to the relying party

Rule below configured relying party to issue 2 claims in the SAML token: email and role

$claimsRule = @"  

@RuleTemplate = "LdapClaims"  

@RuleName = "AD"  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

=> issue(  

store = "Active Directory",  

types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.microsoft.com/ws/2008/06/identity/claims/role"),  

query = ";mail,tokenGroups,UPN(fullDomainQualifiedName);{0}",  

param = c.Value);  

"@

Apply the rule to the Relying Party

Set-ADFSRelyingPartyTrust -TargetName $name -IssuanceTransformRules $claimsRule

================================================================================================

Configure SharePoint to trust AD FS

Define claim types

$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming  

$role = New-SPClaimTypeMapping "http://schemas.microsoft.com/ws/2008/06/identity/claims/role" -IncomingClaimTypeDisplayName "Role" -SameAsIncoming

Public key of the AD FS signing certificate

$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\adfs.cer")

Unique realm (corresponds to the unique identifier of the AD FS Relying Party)

$realm = "urn:myserver:mycompany.com.my"

Set the AD FS URL where users are redirected to authenticate

$signinurl = "https://adfs.mycompany.com.my/adfs/ls/"

Create a new SPTrustedIdentityTokenIssuer in SharePoint

New-SPTrustedIdentityTokenIssuer -Name "myserver-TrustedIdentityProvider" -Description "myserver-TrustedIdentityProvider" -Realm $realm -ImportTrustCertificate $signingCert -ClaimsMappings &email,$role -SignInUrl $signinurl -IdentifierClaim $email.InputClaimType

$rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\adfs.cer")  

New-SPTrustedRootAuthority -Name "myserver-TrustedRootAuthority" -Certificate $rootCert

This script extends an existing web application to set AD FS authentication on a new zone

URL of the default zone of the web application

$webAppDefaultZoneUrl = "http://myserver"

URL of the SharePoint site federated with ADFS

$trustedSharePointSiteUrl = "https://myapp-mycompany.com.my"  

$sptrust = Get-SPTrustedIdentityTokenIssuer "myserver-TrustedIdentityProvider"  

$ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust  

$wa = Get-SPWebApplication $webAppDefaultZoneUrl  

New-SPWebApplicationExtension -Name "myserver-TrustedIdentityProvider" -Identity $wa -SecureSocketsLayer -Zone Intranet -Url $trustedSharePointSiteUrl -AuthenticationProvider $ap

Create self certificate for the web extension site

New-SelfSignedCertificate -DnsName "myserver-mycompany.com.my" -CertStoreLocation "cert:\LocalMachine\My"

## Answers

_No answers on this thread._
