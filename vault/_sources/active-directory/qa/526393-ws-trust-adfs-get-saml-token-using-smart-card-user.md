---
title: "WS-Trust ADFS get SAML token using smart card user certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/526393/ws-trust-adfs-get-saml-token-using-smart-card-user
question_id: 526393
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# WS-Trust ADFS get SAML token using smart card user certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/526393/ws-trust-adfs-get-saml-token-using-smart-card-user (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have a non-browser application that we would like to add SSO (single sign on) support thru ADFS Federation (i.e. WS-Trust) for smart card users when accessing OneDrive.  We want to use ADFS Certificate authentication method, i.e. using smart card user's certificate.  MS .NET WS-Trust has WSTrustChannelFactory that allows setting of user's certificate via Credentials.ClientCertificate.Certificate  but this seems to only handle non-smart card user's certificate (e.g. PFX w/ private key).  The private key for smart card user is on the card.  Does WSTrustChannelFactory have support for smart card user certificate?  If so, how would it sign the SOAP request because private key is in the card.  Does it expect to pass the corresponding smart card user certificate PFX file?  

Regards,  

Eliza

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-30*

Not a dev here, but this works in PowerShell:    

```
...  
$WSTrustChannelFactory = New-Object -TypeName System.ServiceModel.Security.WSTrustChannelFactory -ArgumentList $WS2007HttpBinding, $EndpointAddress   
$WSTrustChannelFactory.TrustVersion = [System.ServiceModel.Security.TrustVersion]::WSTrust13   
$WSTrustChannelFactory.Credentials.ClientCertificate.SetCertificate(  
    [System.Security.Cryptography.X509Certificates.StoreLocation]::CurrentUser,  
    [System.Security.Cryptography.X509Certificates.StoreName]::My,  
    [System.Security.Cryptography.X509Certificates.X509FindType]::FindByThumbprint,  
    "713D3D9273566CE53131FB9F1C6A16F09CB0E71D")  
$Channel = $WSTrustChannelFactory.CreateChannel()   
$RequestSecurityToken = New-Object -TypeName System.IdentityModel.Protocols.WSTrust.RequestSecurityToken -Property @{   
    RequestType = [System.IdentityModel.Protocols.WSTrust.RequestTypes]::Issue   
    AppliesTo = "urn:microsoft:adfs:claimsxray"  
    KeyType = [System.IdentityModel.Protocols.WSTrust.KeyTypes]::Bearer   
    TokenType = "urn:oasis:names:tc:SAML:2.0:assertion"  
}   
$RequestSecurityTokenResponse = New-Object -TypeName System.IdentityModel.Protocols.WSTrust.RequestSecurityTokenResponse   
#need to implement error mgmt  
$Token = $Channel.Issue($RequestSecurityToken, [ref] $RequestSecurityTokenResponse)
```

I skipped a big chuck of initialization at the beggining but essentially calling SetCertificate with the thumbprint of a certificate store in a smartcard works just fine. It prompts me for the PIN and then move along...
