---
title: "ADFS Down-Level hybrid azure ad join Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/974181/adfs-down-level-hybrid-azure-ad-join-error
question_id: 974181
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Down-Level hybrid azure ad join Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/974181/adfs-down-level-hybrid-azure-ad-join-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,    

I have deployed adfs 2019 and have configured adfs and ad connect to support down-level server OS like 2012 R2 when it comes to device registration    

I also installed workplace join as per MS instructions to do hybrid domain join servers 2012 R2, when i try to join the machine via workplace join manually ( which in normal times it runs automatically via scheduled task) I get the following error    

Error Message: Failed to navigate to: <the URL>    

now when i manually try to reach the URL it hits ADFS logon page and when you logon it gives the following error    

An error occurred    

No valid strong authentication method found. Contact your administrator to configure and enable appropriate strong authentication provider.    

Error details    

Activity ID: 67f43414-6e34-455d-a0cc-2cb82ce95230    

Relying party: Microsoft Office 365 Identity Platform Worldwide    

Error details: No strong authentication method found for the request from urn:federation:MicrosoftOnline.    

Node name: 4066cac6-cd58-4c0a-8c63-51154783a79e    

Error time: Fri, 19 Aug 2022 12:24:43 GMT    

Proxy server name: ***    

Cookie: enabled    

User agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36    

what strong authentication device join for down-level servers need ?    

what am i missing here?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-29*

I did adjust the internal DNS so request from inside goes directly to adfs and consider it intranet authentication requests. but from 2019 sso is working now but not 2012 R2 same browser. bellow is the error from workplace join    

    

I am running out of any idea and losing my mind as to what is missing in here. even MS support is not helpful and keep telling me to do everything i have already tried. and configured.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-25*

Sure, thanks for looking into this. I am missing something here. bellow are the logs. also when I try to use workplace join to join the 2012R2 it gives the following error,     

    

    

and when I go directly to that Hybrid Azure AD Join service authentication url and login it says     

For Security Reasons we need more info to log you in.     

I Have MFA setup because of the initial error that i posted in my question above, but i also configured trusted locations to bypass MFA in azure.     

Bellow are the logs you requested:    

IssuanceAuthorizationRules           :  => issue(Type = "http://schemas.microsoft.com/authorization/claims/permit", Value = "true");    

IssuanceTransformRules               : @RuleName = "Issue UPN"    

                                       c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]  

                                        => issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/claims/UPN"), query = "samAccountName={0};userPrincipalName;{1}", param = regexreplace(c.Value, "(?<domain>[^\]+)\(?<user>.+)", "${user}"), param = c.Value);  

```
@RuleName = "Query objectguid and msdsconsistencyguid for custom ImmutableId claim"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]  
                                    => add(store = "Active Directory", types = ("http://schemas.microsoft.com/ws/2016/02/identity/claims/objectguid", "http://schemas.microsoft.com/ws/2016/02/identity/claims/msdsconsistencyguid"), query = "samAccountName={0};objectGUID,mS-DS-ConsistencyGuid;{1}", param =   
                                   regexreplace(c.Value, "(?[^\\]+)\\(?.+)", "${user}"), param = c.Value);  
                                     
                                   @RuleName = "Check for the existence of msdsconsistencyguid"  
                                   NOT EXISTS([Type == "http://schemas.microsoft.com/ws/2016/02/identity/claims/msdsconsistencyguid"])  
                                    => add(Type = "urn:federation:tmp/idflag", Value = "useguid");  
                                     
                                   @RuleName = "Issue msdsconsistencyguid as Immutable ID if it exists"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2016/02/identity/claims/msdsconsistencyguid"]  
                                    => issue(Type = "http://schemas.microsoft.com/LiveID/Federation/2008/05/ImmutableID", Value = c.Value);  
                                     
                                   @RuleName = "Issue objectGuidRule if msdsConsistencyGuid rule does not exist"  
                                   c1:[Type == "urn:federation:tmp/idflag", Value =~ "useguid"]  
                                    && c2:[Type == "http://schemas.microsoft.com/ws/2016/02/identity/claims/objectguid"]  
                                    => issue(Type = "http://schemas.microsoft.com/LiveID/Federation/2008/05/ImmutableID", Value = c2.Value);  
                                     
                                   @RuleName = "Issue nameidentifier"  
                                   c:[Type == "http://schemas.microsoft.com/LiveID/Federation/2008/05/ImmutableID"]  
                                    => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Value = c.Value, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified");  
                                     
                                   @RuleName = "Issue accounttype for domain-joined computers"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value =~ "-515$", Issuer =~ "^(AD AUTHORITY|SELF AUTHORITY|LOCAL AUTHORITY)$"]  
                                    => issue(Type = "http://schemas.microsoft.com/ws/2012/01/accounttype", Value = "DJ");  
                                     
                                   @RuleName = "Issue AccountType with the value USER when it is not a computer account"  
                                   NOT EXISTS([Type == "http://schemas.microsoft.com/ws/2012/01/accounttype", Value == "DJ"])  
                                    => add(Type = "http://schemas.microsoft.com/ws/2012/01/accounttype", Value = "User");  
                                     
                                   @RuleName = "Issue issuerid when it is not a computer account"  
                                   c1:[Type == "http://schemas.xmlsoap.org/claims/UPN"]  
                                    && c2:[Type == "http://schemas.microsoft.com/ws/2012/01/accounttype", Value == "User"]  
                                    => issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/issuerid", Value = regexreplace(c1.Value, "(?i)(^([^@]+)@)(?(frostypuppy\.com))$", "http://${domain}/adfs/services/trust/"));  
                                     
                                   @RuleName = "Issue issuerid for DJ computer auth"  
                                   c1:[Type == "http://schemas.microsoft.com/ws/2012/01/accounttype", Value == "DJ"]  
                                    => issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/issuerid", Value = "http://frostypuppy.com/adfs/services/trust/");  
                                     
                                   @RuleName = "Issue onpremobjectguid for domain-joined computers"  
                                   c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value =~ "-515$", Issuer =~ "^(AD AUTHORITY|SELF AUTHORITY|LOCAL AUTHORITY)$"]  
                                    && c2:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer =~ "^(AD AUTHORITY|SELF AUTHORITY|LOCAL AUTHORITY)$"]  
                                    => issue(store = "Active Directory", types = ("http://schemas.microsoft.com/identity/claims/onpremobjectguid"), query = ";objectguid;{0}", param = c2.Value);  
                                     
                                   @RuleName = "Pass through primary SID"  
                                   c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid", Value =~ "-515$", Issuer =~ "^(AD AUTHORITY|SELF AUTHORITY|LOCAL AUTHORITY)$"]  
                                    && c2:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/primarysid", Issuer =~ "^(AD AUTHORITY|SELF AUTHORITY|LOCAL AUTHORITY)$"]  
                                    => issue(claim = c2);  
                                     
                                   @RuleName = "Pass through claim - insideCorporateNetwork"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2012/01/insidecorporatenetwork"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Pass Through Claim - Psso"  
                                   c:[Type == "http://schemas.microsoft.com/2014/03/psso"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Issue Password Expiry Claims"  
                                   c1:[Type == "http://schemas.microsoft.com/ws/2012/01/passwordexpirationtime"]  
                                    => issue(store = "_PasswordExpiryStore", types = ("http://schemas.microsoft.com/ws/2012/01/passwordexpirationtime", "http://schemas.microsoft.com/ws/2012/01/passwordexpirationdays", "http://schemas.microsoft.com/ws/2012/01/passwordchangeurl"), query = "{0};", param = c1.Value);  
                                     
                                   @RuleName = "Pass through claim - authnmethodsreferences"  
                                   c:[Type == "http://schemas.microsoft.com/claims/authnmethodsreferences"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Pass through claim - multifactorauthenticationinstant"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2017/04/identity/claims/multifactorauthenticationinstant"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Pass through claim - certificate authentication - serial number"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/serialnumber"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Pass through claim - certificate authentication - issuer"  
                                   c:[Type == "http://schemas.microsoft.com/2012/12/certificatecontext/field/issuer"]  
                                    => issue(claim = c);  
                                     
                                   @RuleTemplate = "PassThroughClaims"  
                                   @RuleName = "Auth Method References"  
                                   c:[Type == "http://schemas.microsoft.com/claims/authnmethodsreferences"]  
                                    => issue(claim = c);  
                                     
                                   @RuleTemplate = "PassThroughClaims"  
                                   @RuleName = "InsideCorpNet"  
                                   c:[Type == "http://schemas.microsoft.com/ws/2012/01/insidecorporatenetwork"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Keep Users Signed In"  
                                   c:[Type == "https://schemas.microsoft.com/2014/03/psso"]  
                                    => issue(claim = c);  
                                     
                                   @RuleName = "Auth Method Claim Rule"  
                                   c:[Type == "http://schemas.microsoft.com/claims/authnmethodsreferences"]  
                                    => issue(claim = c);
```

DelegationAuthorizationRules         :     

ImpersonationAuthorizationRules      :     

AdditionalAuthenticationRules        :     

AllowedAuthenticationClassReferences : {wiaormultiauthn}    

ClientCredentialType : Windows    

Enabled              : False    

FullUrl              : https://adfs service domain/adfs/services/trust/2005/windowsmixed    

Proxy                : False    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/2005/windowsmixed    

Version              : wstrust2005    

ClientCredentialType : ClientCertificate    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/2005/certificatemixed    

Proxy                : True    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/2005/certificatemixed    

Version              : wstrust2005    

ClientCredentialType : Username-Password-Clear    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/2005/usernamemixed    

Proxy                : True    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/2005/usernamemixed    

Version              : wstrust2005    

ClientCredentialType : Kerberos    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/2005/kerberosmixed    

Proxy                : False    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/2005/kerberosmixed    

Version              : wstrust2005    

ClientCredentialType : Kerberos    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/13/kerberosmixed    

Proxy                : False    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/13/kerberosmixed    

Version              : wstrust13    

ClientCredentialType : ClientCertificate    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/13/certificatemixed    

Proxy                : True    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/13/certificatemixed    

Version              : wstrust13    

ClientCredentialType : Username-Password-Clear    

Enabled              : True    

FullUrl              : https://adfs service domain/adfs/services/trust/13/usernamemixed    

Proxy                : True    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/13/usernamemixed    

Version              : wstrust13    

ClientCredentialType : Windows    

Enabled              : False    

FullUrl              : https://adfs service domain/adfs/services/trust/13/windowsmixed    

Proxy                : False    

Protocol             : WS-Trust    

SecurityMode         : Mixed    

AddressPath          : /adfs/services/trust/13/windowsmixed    

Version              : wstrust13

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-25*

Well, I just try in my lab with the documents I pointed to (and a Windows 7 though) and it worked. So, let's review the config. Do you mind sharing the outputs of the following commands:    

```
Get-AdfsRelyingPartyTrust -Identifier urn:federation:MicrosoftOnline | Select-Object *Rules,AllowedAuthenticationClassReferences
```

And this one:    

```
Get-AdfsEndpoint | Where-Object {$_.AddressPath -like "*mixed"}
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-24*

I have already configured that claim. that claim should by pass the MFA is its configured right ?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-23*

I think you are missing the `wiaormultiauthn` claim. The following documentation describe how to enable it: https://learn.microsoft.com/en-us/azure/active-directory/devices/hybrid-azuread-join-manual#configure-federation-service-for-downlevel-devices    

I would also review the rest as you might have missed something else too? Check this out: https://learn.microsoft.com/en-us/azure/active-directory/devices/troubleshoot-hybrid-join-windows-legacy
