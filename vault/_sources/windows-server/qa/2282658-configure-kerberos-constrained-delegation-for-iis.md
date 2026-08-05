---
title: "configure kerberos-constrained delegation for IIS using ApplicationPoolIdentity"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2282658/configure-kerberos-constrained-delegation-for-iis
question_id: 2282658
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# configure kerberos-constrained delegation for IIS using ApplicationPoolIdentity

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2282658/configure-kerberos-constrained-delegation-for-iis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to configure kerberos-constrained delegation for an ASP.NET Core app hosted in IIS using ApplicationPoolIdentity (not a service account).

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-06-11*

Hello,

Thank you for posting question on Microsoft Windows forum!

 Based on your query of configuring kerberos-constrained delegation for an ASP.NET Core app hosted in IIS using ApplicationPoolIdentity ,not a service account. you need to focus on ensuring the Application Pool Identity is properly trusted for delegation, which involves creating an SPN and setting delegation trust in Active Directory. Since you're using Application Pool Identity, you'll need to configure the SPN for the IIS server itself rather than a specific service account. The followings are some suggested steps for that.

1.Determine the Application Pool Identity:

-  Open IIS Manager and navigate to your application's pool.

-  Click "Advanced Settings" and find the "Identity" setting.

-  Note down the identity. It will likely be in the format IIS AppPool\YourApplicationPoolName

2.Register the SPN:

-  Open a command prompt as an administrator.

-  Use the setspn tool to register an SPN for the IIS server, reflecting the Application Pool Identity.

-  setspn -S HTTP/your.website.domain.com IIS AppPool\YourApplicationPoolName

-  This SPN will allow the Application Pool Identity to impersonate users when interacting with downstream service.

3.Configure Delegation in Active Directory:

-  Open Active Directory Users and Computers.

-  Find and right-click the account representing the IIS server's machine account (typically the server's FQDN).

-  Select "Properties."

-  Go to the "Delegation" tab.

-  Choose "Trust this computer for delegation to specified services only".

-  Select "Use Kerberos only".

-  Click "OK" to save the changes. 

4.Verify SPN and Delegation:

-  Use the setspn tool again to verify that the SPN has been successfully registered.

-  Test your application to ensure Kerberos delegation is working as expected. 

It is absolutely critical important to test it out thoroughly in the testing environment to make sure everything proceeds smoothly before deploying it in production environment.  

You can refer to the following articles for more information.

-  https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/configure-kerberos-constrained-delegation

-  https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-9.0&tabs=visual-studio

-  https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/iis-80-using-aspnet-35-and-aspnet-45

-  https://learn.microsoft.com/en-us/entra/identity/app-proxy/application-proxy-back-end-kerberos-constrained-delegation-how-to

Hope the above information is helpful!
