---
title: "ADFS - No strong authentication method found for the request from Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/744973/adfs-no-strong-authentication-method-found-for-the
question_id: 744973
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS - No strong authentication method found for the request from Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/744973/adfs-no-strong-authentication-method-found-for-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm running Windows Server 2019 ADFS migrated from old version of ADFS. Everything is working fine, but we had to remove/disable the 3rd party MFA vendor we had. So I disabled the vendor's tool from the Authentication Methods in ADFS console and removed the program. We did this because we federated our ADFS with company, so instead of I'm authenticating using my own ADFS/AD local domain, I'm using the company and everything is done by them, including the MFA - I have 2 Claims Provider Trusts because of this.    

But, we have 1 RP that does not work with that config so are still using the local AD, but now we noticed after login it is showing an error about "No valid strong authentication method found".    

It seems to be general, because I tested other RPs and using the local AD and same issue.    

How can I get rid of this and just authenticate even without MFA, just using the username and password?    

See attached my current config for Authentication Methods.    

"No valid strong authentication method found. Contact your administrator to configure and enable appropriate strong authentication provider."    

Event ID 364    

```
"**Exception details:   
Microsoft.IdentityServer.Web.NoValidStrongAuthenticationMethodException: No strong authentication method found for the request from https://MY-RP.COM.  
   at Microsoft.IdentityServer.Web.Authentication.AuthenticationPolicyEvaluator.EvaluatePolicy(Boolean& isLastStage, AuthenticationStage& currentStage, Boolean& strongAuthRequried)  
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.GetAuthMethodsFromAuthPolicyRules(PassiveProtocolHandler protocolHandler, ProtocolContext protocolContext)  
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.GetAuthenticationMethods(PassiveProtocolHandler protocolHandler, ProtocolContext protocolContext)  
   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)**"
```

Thanks!!    

176508-config.png

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

I don't see any requirement in the rules. Then I guess it might be the actual application requesting a specific authentication method (in the redirect the app sends to the user).  

It is possible for an application to request a specific authentication method or even MFA. Could you share what the redirect URL looks like when you hit the app and are redirected to ADFS?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-28*

Sure @Pierre Audonnet - MSFT   - this is the output from one of my RP:    

Get-ADFSRelyingPartyTrust -Name "RP"    

```
AllowedAuthenticationClassReferences : {}  
EncryptionCertificateRevocationCheck : CheckChainExcludeRoot  
PublishedThroughProxy                : False  
SigningCertificateRevocationCheck    : CheckChainExcludeRoot  
WSFedEndpoint                        :  
AdditionalWSFedEndpoint              : {}  
ClaimsProviderName                   : {Company Global}  
ClaimsAccepted                       : {}  
EncryptClaims                        : True  
Enabled                              : True  
EncryptionCertificate                :  
Identifier                           : {https://rp.domain.com}  
NotBeforeSkew                        : 0  
EnableJWT                            : False  
AlwaysRequireAuthentication          : False  
Notes                                : Notes for the RP  
OrganizationInfo                     :  
ObjectIdentifier                     : IDENTIFIER  
ProxyEndpointMappings                : {}  
ProxyTrustedEndpoints                : {}  
ProtocolProfile                      : WsFed-SAML  
RequestSigningCertificate            : {}  
EncryptedNameIdRequired              : False  
SignedSamlRequestsRequired           : False  
SamlEndpoints                        : {Microsoft.IdentityServer.Management.Resources.SamlEndpoint}  
SamlResponseSignature                : AssertionOnly  
SignatureAlgorithm                   : http://www.w3.org/2001/04/xmldsig-more#rsa-sha256  
TokenLifetime                        : 0  
AllowedClientTypes                   : Public  
IssueOAuthRefreshTokensTo            : NoDevice  
RefreshTokenProtectionEnabled        : True  
RequestMFAFromClaimsProviders        : False  
ScopeGroupId                         :  
ScopeGroupIdentifier                 :  
DeviceAuthenticationMethod           :  
Name                                 : RP  
AutoUpdateEnabled                    : False  
MonitoringEnabled                    : False  
MetadataUrl                          :  
ConflictWithPublishedPolicy          : False  
IssuanceAuthorizationRules           : @RuleName = "1-Get User Groups"  
                                       c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]  
                                        => add(store = "Active Directory", types = ("http://test.com/phase1"), query =  
                                       "mail={0};memberOf;DOMAIN\user", param = c.Value);  
  
                                       @RuleName = "2-Remove OU"  
                                       c:[Type == "http://test.com/phase1"]  
                                        => add(Type = "http://test.com/phase2", Value = RegExReplace(c.Value,  
                                       ",[^\n]*", ""));  
  
                                       @RuleName = "3-Remove the CN="  
                                       c:[Type == "http://test.com/phase2"]  
                                        => add(Type = "http://schemas.xmlsoap.org/claims/Group", Value =  
                                       RegExReplace(c.Value, "^CN=", ""));  
  
                                       @RuleName = "4-Filter Group_RO and Grant Access"  
                                       c:[Type == "http://schemas.xmlsoap.org/claims/Group", Value =~ "^(?i)Group_RO$"]  
                                        => issue(Type = "http://schemas.microsoft.com/authorization/claims/permit",  
                                       Value = "PermitUsersWithClaim");  
  
                                       @RuleTemplate = "Authorization"  
                                       @RuleName = "Permit_Group_RO"  
                                       c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid",  
                                       Value =~ "^(?i)S-1-5-21-290840851-546066832-394647578-5115$"]  
                                        => issue(Type = "http://schemas.microsoft.com/authorization/claims/permit",  
                                       Value = "PermitUsersWithClaim");  
  
  
IssuanceTransformRules               : @RuleName = "1-Get the Local DOMAIN username"  
                                       c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]  
                                        => add(store = "Active Directory", types = ("DOMAIN"), query =  
                                       "mail={0};sAMAccountName;DOMAIN\user", param = c.Value);  
  
                                       @RuleName = "2-Send LOCAL domain username as NameID"  
                                       c:[Type == "DOMAIN"]  
                                        => issue(Type =  
                                       "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer  
                                       = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType =  
                                       c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimpro  
                                       perties/format"] = "urn:oasis:names:tc:SAML:1.1:nameid-format:DOMAIN");  
  
                                       @RuleTemplate = "LdapClaims"  
                                       @RuleName = "Send NameID"  
                                       c:[Type ==  
                                       "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname",  
                                       Issuer == "AD AUTHORITY"]  
                                        => issue(store = "Active Directory", types =  
                                       ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier"), query  
                                       = ";sAMAccountName;{0}", param = c.Value);  
  
  
DelegationAuthorizationRules         :  
LastPublishedPolicyCheckSuccessful   :  
LastUpdateTime                       : 12/31/1899 7:00:00 PM  
LastMonitoredTime                    : 12/31/1899 7:00:00 PM  
ImpersonationAuthorizationRules      :  
AdditionalAuthenticationRules        :  
AccessControlPolicyName              :  
AccessControlPolicyParameters        :  
ResultantPolicy                      :
```

We have another "Application Groups" using OAuth, but I was not able to run the same command on that. This one is also facing the same issue.    

Get-AdfsApplicationGroup -Name "OAuth Application"    

```
ApplicationGroupIdentifier : Application-Test  
Description                : OAuth test application  
Name                       : OAuth-Test  
Enabled                    : True  
Applications               : {OAuth-Test - Server application, OAuth-Test - Web API}
```

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-02-28*

You might still have the rules to trigger MFA enabled on your Relying Party trust.  

Can you show us the output of a `Get-ADFSRelyingPartyTrust` for this failing relying party trust?
