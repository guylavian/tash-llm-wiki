---
title: "[ADFS][SAML][Response][Signature] ADFS doesn't send a signature block in the Response message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/483078/adfs-saml-response-signature-adfs-doesnt-send-a-si
question_id: 483078
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [ADFS][SAML][Response][Signature] ADFS doesn't send a signature block in the Response message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/483078/adfs-saml-response-signature-adfs-doesnt-send-a-si (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have configured my ADFS to send a signature in the Response message.  

I have set my relying party like this (see below)  

The authentication works fine and I can log into my SP.  

However, the Response message doesn't contain the Signature block.

I tried with keyclock and it woks fine, I can see the Signature block in the Response message.

When I setup my SP to require a response signature, obviously I get an error since I don't have the block in the Reponse message.

What is the correct ADFS configuration to get the Signature block sent in the Response message please ?

Thanks for your help, it's driving me crazy.

```
PS C:\Users\user01> Get-AdfsRelyingPartyTrust -name "XXXX"

AllowedAuthenticationClassReferences : {}
EncryptionCertificateRevocationCheck : None
PublishedThroughProxy                : False
SigningCertificateRevocationCheck    : None
WSFedEndpoint                        : 
AdditionalWSFedEndpoint              : {}
ClaimsProviderName                   : {}
ClaimsAccepted                       : {}
EncryptClaims                        : True
Enabled                              : True
EncryptionCertificate                : 
Identifier                           : YYYY
NotBeforeSkew                        : 0
EnableJWT                            : False
AlwaysRequireAuthentication          : False
Notes                                : 
OrganizationInfo                     : 
ObjectIdentifier                     : 731cfe19-5fe3-eb11-9afb-0050568f44bf
ProxyEndpointMappings                : {}
ProxyTrustedEndpoints                : {}
ProtocolProfile                      : WsFed-SAML
RequestSigningCertificate            : {[Subject]
                                         CN=ZZZZ, OU=adfsClient, O=TTTT, L=Paris, S=France, C=FR

                                       [Issuer]
                                         CN=ZZZZ, OU=adfsClient, O=TTTT, L=Paris, S=France, C=FR

                                       [Serial Number]
                                         44ECB0E72927002223D1E196D1019C7A6A4650C6

                                       [Not Before]
                                         20/07/2021 16:13:13

                                       [Not After]
                                         20/07/2022 16:13:13

                                       [Thumbprint]
                                         C52F394C2415805A889E767398165BB087125805
                                       }
EncryptedNameIdRequired              : False
SignedSamlRequestsRequired           : False
SamlEndpoints                        : {Microsoft.IdentityServer.Management.Resources.SamlEndpoint}
SamlResponseSignature                : MessageOnly
SignatureAlgorithm                   : http://www.w3.org/2000/09/xmldsig#rsa-sha1
TokenLifetime                        : 0
AllowedClientTypes                   : Public, Confidential
IssueOAuthRefreshTokensTo            : AllDevices
RefreshTokenProtectionEnabled        : True
RequestMFAFromClaimsProviders        : False
ScopeGroupId                         : 
ScopeGroupIdentifier                 : 
DeviceAuthenticationMethod           : 
Name                                 : XXXX
AutoUpdateEnabled                    : False
MonitoringEnabled                    : False
MetadataUrl                          : 
ConflictWithPublishedPolicy          : False
IssuanceAuthorizationRules           : 
IssuanceTransformRules               : @RuleName = "Transform Domain User to User"
                                       c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
                                        => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = regexreplace(c.Value, 
                                       "(?[^\\]+)\\(?.+)", "${user}"), ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = 
                                       "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified");

DelegationAuthorizationRules         : 
LastPublishedPolicyCheckSuccessful   : 
LastUpdateTime                       : 01/01/1900 00:00:00
LastMonitoredTime                    : 01/01/1900 00:00:00
ImpersonationAuthorizationRules      : 
AdditionalAuthenticationRules        : 
AccessControlPolicyName              : Permit everyone
AccessControlPolicyParameters        : 
ResultantPolicy                      : RequireFreshAuthentication:False
                                       IssuanceAuthorizationRules:
                                       {
                                         Permit everyone
                                       }
```

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-07-21*

Your current setting is:  

```
SamlResponseSignature                : MessageOnly
```

Your token should look like this:  

```

    http://sts.piesec.ca/adfs/services/trust
    
    
        
            
            
            
                
                    
                    
                
                
                468jLaLACn76HmOmmT+Hmk7eYauelXjBAOfbvpATJeE=
            
        
        Lfb8xVVAJSp8RvZXCgl5PEEgEMABE+nPC0OiTCHKYjrKWb/Wv0mwl7VREHQKsuyYkaWLKFOfKiAfplm3mnifkb3gzQUL5eQ50OTmQZPoVh0ek+l0HIVyKgvgnRafVaSggd3VXHYqEVBQ8TyZj+8aWtWgb6lTBqQWlhjts+hIQrSp6+JyAywY97RadjzEjvspG+6tq3opiFnKovvGEYzSRlalalalafAxOc9b8oREQfKPfTiEcpQQ50VlDZPe4c2uJLxP/G5ToqevL03vkPGiN/x2gnegQfyPPOQILYinkEKAEJZKRaZYRm6if1KLoollLFP+YNgr5v1ioViq8fccPRUIQ==
        
            
                MIIC1jCCAb.....
            
        
    
    
        
    
    
        http://sts.piesec.ca/adfs/services/trust
        
            ******@piesec.ca
            
                
            
        
        
            
                urn:microsoft:adfs:claimsxray
            
        
        
            
                urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
            
        
    

```

If you set it to AssertionOnly, it will look like this:  

```

 http://sts.piesec.ca/adfs/services/trust
 
 
 
 
 http://sts.piesec.ca/adfs/services/trust
 
 
 
 
 
 
 
 
 
 
 lTXjO3tFhSooIiNkcIk3zvUzSvvZLoH8bxaMx/yLIXE=
 
 
 SONPW4T9bK5as5vlalalala7dbLYECjSlNwwLT7/q4g+Mr+mPydZ5QpuHMf1lU9QGZk/ZfpwVCCJ1q5/7B+n1KQSv3IHR+5hiH28oOtim5fBvLpYQNB24BVySGO9Veip3w54EKIRAIjWXCi/qpcKWK9Ehcv3N76BmNk5rhTDYh3lZ2py09h0mIH+R6RsrRPWc1j6g9LKAyOZXJi2SfqJfFh1SzC9qVkntnQx4bJ3XtuPJa34I+F7eqMNZYJxNf3N6dM3WisukLhtPeVPwdKGH9XAYZwHB6gJpmlc1gnQXjKLtABYLEas+fqrtd+zZkC+wDORJXBRrx94vj7JbCbVfZPT5w==
 
 
 MIIC1jCCAb....
 
 
 
 
 ******@piesec.ca
 
 
 
 
 
 
 urn:microsoft:adfs:claimsxray
 
 
 
 
 urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
 
 
 

```

And if you set it with MessageAndAssertion it will look like this:  

```

 http://sts.piesec.ca/adfs/services/trust
 
 
 
 
 
 
 
 
 
 
 rfGjlXiUiQ4dMiH+OcjevAFrcQ8wvs5CSvhMJniU4Jw=
 
 
 ijHl1KoBuQFB+PWmwgKPzm1IneIhpgZWxRf4NEHyZwhhq0KW+HrnFBb/ruYHBngsz1wN3vpnqRGD45+75BX8ShiFXx+1J+u/HpO5b8Q2kXghCwkDhE1fjvNC8vpq1VfZdOoM1IPSuzZ6886/dOHq1FqmwfjLk6nDcYFmTa22ksQLs88e2Pz1Dth0F8/+c85K+KjMRTsIAi1UlLfNV0jVjIgjDVDxlLJGm0TQmFGZMvFXVlkR7Dmq9/DlvUmC1B2htiyRhcL92FPFBm6l1ZgFYyk/x2MmJZuUSJpkRp0PMvjZT4Dn3th4LbENAuTQTAz9AC8FHtNfXqrRMWEmOLxEBQ==
 
 
 MIIC1jCCAb6gA....
 
 
 
 
 
 
 
 http://sts.piesec.ca/adfs/services/trust
 
 
 
 
 
 
 
 
 
 
 aEwUzRFwmjoUm0TAvOurfE8N/EVFXgb6kYfWizTiDyQ=
 
 
 N34C0GMoW3bdb6SgTghoseu6tHOt+R/lalallalala/vefRP/BxS0YsOusZD5ZPWMOP4hr1moc/YnAFYhnxilaz+ktDiCB2IYjL8K3gKHYYv6JU2wXj+XwQxGziyxq2RBdw6f3fmX4GmSO9NLikhs3vnn9FIK9K3Po8lGOlOqiDGUk+85Zq1T3L7g+a8vDTGxJIa4NH4wPvg0gwoLwHKF96PwhRD8rjPPdAHiiOJftrJK2PgC6lqxFF92bU5K82D13xTmw+W6jZM4kQhiKfcmByuJYhwAjYdwnnQE7TbwYoKdo235/Ug7q/cRePAyTKcMDITeviWVt4d5dBS6Q==
 
 
 MIIC1jCCAb6gAwIBA.....
 
 
 
 
 ******@piesec.ca
 
 
 
 
 
 
 urn:microsoft:adfs:claimsxray
 
 
 
 
 urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
 
 
 

```

So I can't repro as I always have a signature block. Granted, not the same stuff which signed depending on the setting. How did you extract the token?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-20*

I changed back the signatureAlgorith to sha256 instead of sha1.  

Same result.  

Still no Signature block in the Response message.  

I just got :  

```

    http://QQQQQ/adfs/services/trust
    
        
    
    
        http://QQQQQ/adfs/services/trust
        
            user01
            
                
            
        
        
            
                https://RRRR:8081/platform-5.3.x
            
        
        
            
                urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
            
        
    

```
