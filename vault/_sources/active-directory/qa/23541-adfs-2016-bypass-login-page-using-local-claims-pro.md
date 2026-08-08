---
title: "ADFS 2016 - Bypass Login Page using Local Claims Provider"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/23541/adfs-2016-bypass-login-page-using-local-claims-pro
question_id: 23541
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADFS 2016 - Bypass Login Page using Local Claims Provider

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/23541/adfs-2016-bypass-login-page-using-local-claims-pro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,     

I am on ADFS 2016 and I would like to bypass ADFS login page and use RESTful API to authenticate users stored in an LDAP Directory (Declared as Local Claims Provider).    

-  SAML 2.0 : apparently not possible to use REST API. =>Can you confirm this fact, please?    

-  OpenID Connect : only ROPC (Resource Owner Password Credentials) seems OK.     

https://learn.microsoft.com/fr-fr/windows-server/identity/ad-fs/overview/ad-fs-openid-connect-oauth-flows-scenarios#resource-owner-password-credentials-grant-flow-not-recommended    

With ROPC, I can obtain an Access and an ID Token using AD Account Store.    

But I can't use my Local Claims Provider to authenticate users.     

Do you know if there is a specific configuration or parameter to do this?    

My configuration :     

-  ADFS 2016    

-  LDAP Local Claims Provider    

-  OpenID Connect with ROPC flow    

-  Note : With an authorization Code flow, I'm redirected to ADFS Login page where I can choose my Local Claims Provider and the authentication is OK.    

Thanks by advance for your help.

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2020-04-22*

In SAML, you can do this with the SAML bearer assertion flow.    

But note that this requires federation.    

As per this:    

"All passive authorization protocols that are supported by AD FS, including SAML, WS-Federation, and OAuth are also supported for identities that are stored in LDAP directories.    

The WS-Trust active authorization protocol is also supported for identities that are stored in LDAP directories."    

So if you want to use an API, you need to do this via WS-Trust.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-06*

Hello @rbrayb       

Finally, I succeeded the first step! Now, I can get the SAML Assertion based from the LDAP Local Claims Provider.    

Here the steps to get a SAML Assertion with the endpoint /adfs/services/trust/2005/usernamemixed :     

1- Setup an Organisational Account Suffix for the Local Claims Provider    

```
Set-AdfsLocalClaimsProviderTrust -TargetName "MY LDAP DIRECTORY" -OrganizationalAccountSuffix @("test.com")
```

Note : The username must contain the Organisational Account Suffix. Use the email adresse as AnchorClaimLdapAttribute for instance.    

2- In the SOAP Request, set the username wich contains the Organisational Account Suffix    

```
  
********@test.com**  
**PASSWORD**  

```

3- The ADFS use the LDAP Local Claims Provider to authenticate the user and returns a SAML Assertion     

But I always have some issues with the next step:     

I try your link to get the access token but it works only with Azure. The grant types urn:ietf:params:oauth:grant-type:saml1_1-bearer and  urn:ietf:params:oauth:grant-type:saml2-bearer are not supported in ADFS 4.0/2016 (as explain in this link : https://social.technet.microsoft.com/Forums/en-US/47dc854e-eabf-44ee-b012-df71fa2c1da4/implement-rfc-7522-saml-bearer-for-oauth-on-our-adfs-v3?forum=ADFS )    

Maybe I can try to obtain the access token with the grant type urn:ietf:params:oauth:grant-type:jwt-bearer and use the OBO flow for the next step: https://learn.microsoft.com/fr-fr/windows-server/identity/ad-fs/overview/ad-fs-openid-connect-oauth-flows-scenarios#on-behalf-of-flow    

First I have to obtain an access token from the SAML assertion.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2020-04-29*

Have a look at this.    

There are some parameters you may not have?    

I'm not aware of any SAML specific parameters for LDAP.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-27*

Thanks for your answer, @rbrayb   .    

I tried the SAML bearer assertion flow, but it seems that the endpoint /adfs/services/trust/2005/usernamemixed works only with Azure AD.    

So I tried this endpoint /adfs/services/trust/13/UsernameMixed with this request :    

```
  
  
      
        http://docs.oasis-open.org/ws-sx/ws-trust/200512/RST/Issue  
        https://adfs.test.local/adfs/services/trust/13/UsernameMixed  
          
              
                **USERNAME**  
                **PASSWORD**  
              
          
      
      
          
              
                  
                    **https://mysite.identifier**  
                  
              
            http://docs.oasis-open.org/ws-sx/ws-trust/200512/Bearer  
            http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue  
            urn:oasis:names:tc:SAML:2.0:assertion  
          
      

```

-  With an USERNAME/PASSWORD from the Active Directory, It works and I get my SAML Response.     

-  But with the USERNAME/PASSWORD from my Local LDAP Directory, I have the following error : ID3242: The security token could not be authenticated or authorized.    

When I check the ADFS logs :     

Token Type:     

http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName     

%Error message:     

USERNAME-The user name or password is incorrect     

I tried with the DN of the account but same error, even if I have set only my Local LDAP Directory as unique claimsProvider for the application with this command :     

```
Set-AdfsRelyingPartyTrust -TargetName "myClaimAPP" -ClaimsProviderName @("MY LDAP DIRECTORY")
```

With the classic SP-initiated flow it works well (I have only my LDAP Directory form).    

I suppose that it must have a special parameter to had in the SOAP Request ou maybe a configuration in SAML to use the LDAP Local Claims Provider instead of the Active Directory but I can't find anything.     

Do you have any idea, please?
