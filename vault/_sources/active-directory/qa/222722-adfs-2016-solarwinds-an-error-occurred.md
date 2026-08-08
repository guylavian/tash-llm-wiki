---
title: "ADFS 2016, Solarwinds  An error occurred"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222722/adfs-2016-solarwinds-an-error-occurred
question_id: 222722
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 2016, Solarwinds  An error occurred

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222722/adfs-2016-solarwinds-an-error-occurred (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When trying to use ADFS for single sign on to Solarwinds samanage we get a response that states "An error occurred." In event viewer we get the error

"The verification of the SAML message signature failed.  

Message issuer: http://adfs.matc.net/adfs/services/trust  

Exception details:  

MSIS7085: The server requires a signed SAML authentication request but no signature is present. "

Solarwinds provides us with no certificate to load into our side, and they are saying they are getting no information on their end from our server. Below is our configuration. We have confirmed with Solarwinds support they say everything "looks correct"

General configuration  

Property Value  

AccessControlPolicyName Permit everyone  

AccessControlPolicyParameters  

AdditionalWSFedEndpoint  

AllowedAuthenticationClassReferences  

AllowedClientTypes Public, Confidential  

AlwaysRequireAuthentication false  

AutoUpdateEnabled false  

ClaimsProviderName  

ConflictWithPublishedPolicy false  

DelegationAuthorizationRules  

DeviceAuthenticationMethod  

EnableJWT false  

Enabled false  

EncryptClaims true  

EncryptedNameIdRequired false  

EncryptionCertificateRevocationCheck CheckChainExcludeRoot  

Identifier https://app.samanage.com/saml/ManhattanTech, https://manhattantech.samanage.com/saml/ManhattanTech, https://support.manhattantech.edu/saml/ManhattanTech  

ImpersonationAuthorizationRules  

IssueOAuthRefreshTokensTo AllDevices  

LastMonitoredTime 2020-12-08T23:15:55.0773285+00:00  

LastPublishedPolicyCheckSuccessful True  

LastUpdateTime 2020-12-02T21:23:03.1497473+00:00  

MetadataUrl https://manhattantech.samanage.com/saml/metadata  

MonitoringEnabled false  

Name Solarwinds  

NotBeforeSkew 0  

Notes  

ObjectIdentifier 306344b2-2b28-eb11-911e-005056932dd7  

OrganizationInfo  

ProtocolProfile WsFed-SAML  

ProxyEndpointMappings  

ProxyTrustedEndpoints  

PublishedThroughProxy false  

RefreshTokenProtectionEnabled true  

RequestMFAFromClaimsProviders false  

ResultantPolicy RequireFreshAuthentication:False IssuanceAuthorizationRules: { Permit everyone }  

SamlResponseSignature AssertionOnly  

ScopeGroupId  

ScopeGroupIdentifier  

SignatureAlgorithm http://www.w3.org/2001/04/xmldsig-more#rsa-sha256  

SignedSamlRequestsRequired false  

SigningCertificateRevocationCheck CheckChainExcludeRoot  

TokenLifetime 0  

WSFedEndpoint  

IssuanceAuthorizationRules  

Rule name Rule

--  

IssuanceTransformRules  

Rule name Rule  

SendEmail @RuleTemplate = "LdapClaims" c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] => issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/claims/EmailAddress"), query = ";mail;{0}", param = c.Value);  

Moidfyclaim @RuleTemplate = "MapClaims" c:[Type == "http://schemas.xmlsoap.org/claims/EmailAddress"] => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress");  

AdditionalAuthenticationRules  

Rule name Rule

--  

SamlEndpoints  

Property Value  

Saml endpoint 1  

Binding POST  

BindingUri urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST  

Index 0  

IsDefault true  

Location https://manhattantech.samanage.com/saml/ManhattanTech  

Protocol SAMLAssertionConsumer  

ResponseLocation  

Saml endpoint 2  

Binding POST  

BindingUri urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST  

Index 1  

IsDefault false  

Location https://manhattantech.samanage.com/saml/ManhattanTech  

Protocol SAMLAssertionConsumer  

ResponseLocation  

Saml endpoint 3  

Binding POST  

BindingUri urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST  

Index 3  

IsDefault false  

Location https://app.samanage.com/saml/ManhattanTech  

Protocol SAMLAssertionConsumer  

ResponseLocation  

ClaimsAccepted  

Property Value

--  

EncryptionCertificate  

Property Value

--  

RequestSigningCertificate  

Property Value  

Request signing certificate 1  

Subject CN=*.samanage.com  

Issuer CN=R3, O=Let's Encrypt, C=US  

Version 3  

NotBefore 2020-12-06T13:00:50+00:00  

NotAfter 2021-03-06T13:00:50+00:00  

Thumbprint 9D6D6FC9E50873C851CB65757FE2A43FF7FF3ABE  

SerialNumber 032E7755EEA7002F5A52C169A6E02278BD7B  

FriendlyName RSA

If anyone has any idea to try, or if anyone else is using ADFS with Solarwinds and can share their configuration we would find that very helpful.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-14*

It seems that there is something missing on the application's side. When you navigate to https://manhattantech.samanage.com/login and click on Single Sign-On you get an HTTP redirect to: https://adfs.matc.net/adfs/ls?SAMLRequest=fVLdT4MwEP9XeOsTMJDJbICEbDFZshmzTR98MbdyCElpsVf8%2BO8tLIszUft2vd%2FXXZsRdLLn5WAbtcPXAcl6JREa22q11IqGDs0ezVsr8GG3yVljbU88DDtQDVgLyqJoAqcCCl4wELoLR8lwe%2B4fXJ95KyfcKhhVvzWgqinowIpAoZ2qUBLz1qucPaf1IrmG5OincZT4SSVq%2F3i8iv0bEPG8Tt1JwEGJBlwrGnPkLJ7FkT%2BL%2FCg5zCI%2BT%2Fl88cS8RzQ02cbBjHkfnVTEx4g5G4ziGqglrqBD4lbwfbndcAfkcF7CJaX%2Fn9MbbbXQkhXZiOZTOlOM4%2F4%2BLZ0WS6E1A9ksvGRlp5e5cy7r1b2Wrfj0Sin1%2B9IgWMyZ4yDzbrVxmn%2FnioJoumkrv56gHDtoZVlVBolYWJxcf36B4gs%3D&RelayState=https%3A%2F%2Fmanhattantech.samanage.com%2F.  

This has a SAMLRequest query string, a RelayState query string, but it is missing the Signature query string. You need to modify the app to send that.
