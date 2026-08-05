---
title: "ADFS Claimset Powershell Syntax For Oracle Cloud SSO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167434/adfs-claimset-powershell-syntax-for-oracle-cloud-s
question_id: 167434
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Claimset Powershell Syntax For Oracle Cloud SSO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167434/adfs-claimset-powershell-syntax-for-oracle-cloud-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Morning Technet!    

I am working on Integrating SSO via ADFS with Oracle Cloud Services. I am using direction from Oracle as outlined in the following documentation provided by Oracle:    

https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/sharedidm/cloud_sso_idp_configuration/ADFS3.0/ADFS3.0__IdPConfig_CloudSP.html    

The issue I'm running into is that my Infrastructure team has provided the ADFS Servers themselves as Windows Server 2016 Core servers, Oracle is only providing GUI instructions on completing the setup, and of course there are no remote management GUI tools for ADFS.     

In the above link, I've parsed the powershell for adding the trust with the required options as identified under the header "    

Adding Oracle Cloud SP as a Trusted Relying Party" as being    

Add-AdfsRelyingPartyTrust -Name "Oracle Connect" -MetadataURL "%path to metadata.xml%" -RequestMFAFromClaimsProviders "False" -AccessControlPolicyName "Permit Everyone" -SignatureAlgorithm 'https://www.w3.org/2001/04/xmldsig-more#rsa-sha256'    

However, I'm having some difficulty putting together the syntax for the steps under the header "Configure Claims Using Email Address"     

So far I get that I have to create two claims rules and then assign them to the relaying party trust, but am a little confused by the command line syntax for the rules, and the Microsoft Learn have been a little ambigious.    

From examples, I believe this is the syntax I should have in the rules file for matching LDAP email to Email per the first requested rule from the Oracle docs:    

c:[Type == " http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress ", Issuer == "AD AUTHORITY"]    

=> issue(store = "AD LDS", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"), query = "sAMAccountName={0};mail", param = regexreplace(c.Value, "(?<domain>[^\]+)\(?<user>.+)", "${user}"));    

And that this is the syntax I should have in the rules file for Transforming the incoming claim    

c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]    

 => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",     

Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType,     

Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"]     

= "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress");    

I'm wondering if someone with more experience in this arena would be willing to review and offer advice on this as it feels like I may still be missing something here. Thanks!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-14*

If you want to do in PowerShell what's described here: https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/sharedidm/cloud_sso_idp_configuration/ADFS3.0/ADFS3.0__IdPConfig_CloudSP.html#section5  

You can do the following...  

-  Create a text file with the following content as in: https://gist.github.com/piaudonn/d343cb99c90e55fdc89e73929d8f0604  

-  Then run the following cmdLet (with <file> being the full path of the text file created above):      Set-AdfsRelyingPartyTrust -TargetName "Oracle Connect" -IssuanceTransformRulesFile <file>

Let us know how it goes!
