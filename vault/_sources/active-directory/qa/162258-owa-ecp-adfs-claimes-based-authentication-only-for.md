---
title: "OWA/ECP ADFS Claimes based authentication only for certain servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162258/owa-ecp-adfs-claimes-based-authentication-only-for
question_id: 162258
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# OWA/ECP ADFS Claimes based authentication only for certain servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162258/owa-ecp-adfs-claimes-based-authentication-only-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm currently working on a migration from Exchange Server 2013 to 2019.    

The customer wants to enable ADFS Claimes based Auth for OWA/ECP only for those 2019 Servers.    

is this supported/possible?    

According to the docs https://learn.microsoft.com/en-us/Exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

We have to set organization wide parameters and also enable ADFS auth on VDIRS.    

Any help would be appreciated!    

Kind Regards    

Christian Schindler

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-27*

Hello,  

thanks for your answers. Regarding the supported statement: if clients only connect through 2019 and proxy to 2013, would it then be supported?  

Cheers  

Christian

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

Hi @Schindler Christian   ,    

If after the migration is complete, you do not uninstall Exchange 2013 and maintain the coexistence state, then you need to enable ADFS for all Exchange organizations, not only for Exchange 2019 .    

If you uninstall Exchange 2013 after migration, only Exchange 2019 will exist. It is achievable, you can follow the steps in the link you provided. If you want to set up a specified server, please enter the url entered during the setting process as the address of a special server, and when configuring Exchange for ADFS, please configure it on the specific server.    

It should be noted that the "steps 4a: Create relying party trusts in AD FS for Outlook on the web and the EAC" and "4b: Create custom claim rules in AD FS for Outlook on the web and the EAC" need to be executed twice. Respectively for OWA and ECP. Then configure the Exchange organization to use AD FS authentication.     

Then run the following command lines to configure the authentication method of ECP and OWA's virtual directory. It should be noted that, please configure ECP first, and then configure OWA.     

Finally, please run the IISRESET in CMD start as administrator to restart the IIS.    

```
Get-EcpVirtualDirectory | Set-EcpVirtualDirectory -AdfsAuthentication $true -BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication $false -OAuthAuthentication $false -WindowsAuthentication $false  
Get-OwaVirtualDirectory | Set-OwaVirtualDirectory -AdfsAuthentication $true -BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication $false -OAuthAuthentication $false -WindowsAuthentication $false
```

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
