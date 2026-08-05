---
title: "ADFS Primary Authentication Methods per Relying Party Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/28369/adfs-primary-authentication-methods-per-relying-pa
question_id: 28369
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Primary Authentication Methods per Relying Party Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/28369/adfs-primary-authentication-methods-per-relying-pa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Per AD FS documentation:     

I should be able to configure primary authentication method per Relying Party Trust.  Some applications we want to log in to with certificate, and some with username and password.  It appears that this was removed in ADFS 2016.  Was the functionality completely removed or is this still achievable through a different menu or Powershell command?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 2 · updated: 2020-05-20*

It was never removed. It was never there.    

The only option per relaying party trust is to enforce re-authentication. There is even a screen shot in the document you post that clearly shows that it is the only option.    

There is a long running thread here with all the info: https://social.technet.microsoft.com/Forums/en-US/e0f81720-6450-44ce-a530-6b9136b39b58/authentication-method-for-per-relying-trust?forum=ADFS#0626dd1a-6a6a-48ab-89d9-f191505eab49.    

In case that link goes offline, here is the content:    

tl;dr This was never taken out from the GUI or from the PowerShell module. It was never in the GUI nor in the PowerShell module.    

It was NOT possible in 2012 R2, it is not possible in 2016, it is not possible in 2019. There must be a confusion there. I am not sure where it is coming from.    

The primary authentication policy was and still is a farm-wide settings and the only option available at the RP level was to force re-authentication. And that is what the documentation that has been pointed out three times says: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-authentication-policies#to-configure-primary-authentication-per-relying-party-trust "Users are required to provide credentials each time at sign in." Please have a look. And the previous version of that document back in 2017 also states the same: https://web.archive.org/web/20170829040751/https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-authentication-policies     

This is what it looks like in the GUI in Windows Server 2012 R2:    

    

That said. You can configure your application trusing ADFS to request for a specific authentication method. But this setting is on the application side. NOT at the ADFS level. For example, if you have an application using WS-Federation on IIS, you can configure the web.config file in such way that the redirect to ADFS will have the authentication method embeded to it:    

```
  
   
   

```

In the example above, the authentication method will be urn:oasis:names:tc:SAML:2.0:ac:classes:TLSClient and as long as this method is enabled in the global authentication policy at the farm level, the user will be prompted to pick a certificate for authentication (that is what this URI is about, TLS auth). But it could have been asking for form based authentication with the URI: urn:oasis:names:tc:SAML:2.0:ac:classes:Password (although password based one is the less secure, you could configure your app that way as long as form based is enabled on the global policy).     

For SAML2 applications, the authentication method can be asked in the RequestedAuthnContext section of the SAML request:    

```
  
urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport  
    

```

Of course that would work only for the SP-Initiated flow.    

Those two methods are to be deployed on the application side. NOT at the ADFS level. And it is documented that way.    

Now if you feel that it does not work for you and you'd rather change how the product works, you can channel your feedback to the product group using this channel: https://windowsserver.uservoice.com/forums/304621-active-directory/suggestions/35823295-specify-primary-authentication-method-per-relying you see the request already exists but does not have a lot of votes. If that goes up, it might change in the next version.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-08*

You shared a screenshot from 2012 R2. Is there a similar setting in 2019 anywhere? I have an app that sometimes is used by shared devices so I want it to prompt for credentials every time. The only non-shared devices are using WIA so prompting every time is fine.
