---
title: "ADFS Saml  Configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/148916/adfs-saml-configuration
question_id: 148916
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Saml  Configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/148916/adfs-saml-configuration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have questions regarding ADFS SAML configuration.  

I have been charged with setting up ADFS SAML and connecting our system with clarity safetyzone.  

I am using Using windows serv 2019 platform for the servers. I have created a test environment that has a domain controller, server with ADCS, and another server with ADFS.  I have a certificate created within the ADCS server and I installed ADFS on the respective server.  I verified after installation of the role and configuring an adfs administrator that the adfs administrator can sign into the  https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx,  I created a windows test account and logged into the adfs server for testing purposes and when navigating to the https://sts.contoso.com/adfs/ls/ and attempting to sign in with that user, I get an error:  

An error occurred  

An error occurred. Contact your administrator for more information.  

Error details  

Activity ID: f68cc99a-b6e5-40dc-1a00-0080000000e5Error details: MSIS7065: There are no registered protocol handlers on path /adfs/ls/ to process the incoming request.Node name: 85253664-435b-4d04-8775-d4b96854cb12Error time: Mon, 02 Nov 2020 20:11:16 GMTCookie: enabledUser agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36  

I have everyone permitted for intranet access in the Access Control Policies.    

Am i missing something?  Once i can verify that a standard user can login, then i can move on to the step of setting up the appropriate claims/trusts.  

Does anyone have experience with this and maybe even experience with the Clarity Safety Zone platform?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-05*

Yep. Many ways to do it. But the easiest way in our context (with having issues with the default rules) would be to adapt our custom rules such as:  

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
  => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = regexreplace(c.Value, "(?[^\\]+)\\(?.+)", "${user}"), ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent");
```

Make sure you mark the post as answered in case someone experience the same challenges that they can easily find a solution.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-04*

Hey thank you very much for the help yesterday.  They came back to me saying there are no longer any errors however, they wondered if there was a way to pass just the username and not the domain\user.  Can this be done?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-04*

Heres what i got
