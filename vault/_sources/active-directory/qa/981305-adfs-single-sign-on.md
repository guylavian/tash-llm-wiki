---
title: "ADFS Single Sign On"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/981305/adfs-single-sign-on
question_id: 981305
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Single Sign On

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/981305/adfs-single-sign-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am working in a project, where i need to create relay party trust for one of the third party application and provide SSO functionality when authenticating through ADFS

I have created the relay party trust for that application and added the Application URL and ADFS URL in the domain joined client machines Internet options -> Security -> Local Intranet - > Sites -> Advanced, When any user access the Application from the domain joined client machine, they were re directed to the ADFS and it is prompting for user name and Password for Authentication. After providing the user name and password, users can able to access the application.

The problem here is SSO is not working when users access the application from the domain joined client machines. Now the Application team is claiming there are no issues with the Application server and ADFS server is causing this problem.

Please help me to understand the below.

-   If we want to have the SSO working for any application using ADFS for authentication, Is that Application should only need to use windows integrated Authentication when sending authentication request to ADFS server ? If yes, can that application use windows integrated authentication with either WS-Fed or SAML protocols to send authentication request ?

-   To identify if there is an issue with ADFS, I have created relay party trust in the ADFS server for the test application "Microsoft Claims X-Ray tool" provided by Microsoft, From that Application i can send the authentication request to ADFS server and i was able to authenticate successfully, but i wanted to know is there an option in Microsoft Claims X-Ray tool to test the SSO behavior from the domain joined machine used to send the authentication request?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-29*

-  If the applications requested for forms and forms is enabled on the AD FS farm, then form it will be. And no Windows Integrated Authentication.    

-  I guess, I have never seen an application requesting it, but in theory it could.     

Usually the application is not requesting anything, just redirects to AD FS and is agnostic of what is happening there.    

The Single Sign-On doesn't depend only on the application. There are 3 components in an AD FS transaction.    

The application (or service provider, or relying party), needs to trust AD FS and redirect for auth (although some application might support the IDP-Initiated sign ins, but that's out of scope of this conversation, and that's old school). Usually doesn't ask for any authentication method, The Security Token Service, the AD FS farm (or Identity Provider STS etc...) will honor the authentication method requested by the app if any and if the method is supported AND enabled. Else will just follow the Authentication Policy. The client (most likely an Internet browser) will just follow the redirection from the application to go to AD FS. To do WIA, the client needs to show up with a user-agent-string that AD FS supports. And the browser needs to be able to WIA (the client needs to be domain joined to a trusted domain) and the browser setting will allow the WIA to work.    

There are also three other components playing a role here. The Service Principal Name of the farm (or SPN) has to be carried by the AD FS service account (and only on one account as duplicate SPNs make Kerberos authentication fails). The DNS record needs to be a A record, not a CNAME. And the browser needs to supported the Extended Protection (ExtendedProtectionTokenCheck). But those are not specific to AD FS, that's the same for all WIA web sites..    

But pretty much all this is in the documentation.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-29*

@Pierre Audonnet - MSFT   ,     

I understand that ADFS is taking care of authentication. Assume i have windows Authentication and Form based Authentication is already enabled in the ADFS server.    

Scenario 1 :     

Does single sign on would work if the application is requesting for forms authentication ?    

Scenario 2 :     

Does single sign on would work if the application is requesting for windows authentication ?      

I specifically wanted to understand what type of authentication should be requested by application server to ADFS for having Single sign on.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-29*

@Pierre Audonnet - MSFT       

Thank for your response.    

Credentials prompt is Windows pop Up not webform, I will check the details mentioned in the below link. Please clarify the below questions.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-iwa     

If we want to have the SSO working for any application using ADFS for authentication, Is that Application should only need to use windows integrated Authentication when sending authentication request to ADFS server ? If yes, can that application use windows integrated authentication with either WS-Fed or SAML protocols to send authentication request ?    

I have created relay party trust in the ADFS server for the test application "Microsoft Claims X-Ray tool" provided by Microsoft, From that Application i can send the authentication request to ADFS server and i was able to authenticate successfully, but i wanted to know is there an option in Microsoft Claims X-Ray tool to test the SSO behavior from the domain joined machine used to send the authentication request?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-08-25*

Few things...    

The Application URL doesn't need to be in the list of Trusted Sites or Intranet Site. The user will not try Windows Integrated Authentication with the app but only with AD FS.    

When you say the user is prompted for Username and Password, you mean in a webform? Or in a Windows popup? If that is on a webform, it might be due to one of the four:    

-  The application is specifically requesting for webform authentication (nothing you can do here else than asking the application developer not to do that.    

-  The Authentication Policy on your AD FS farm has only webform enabled, make sure the Windows Integrated Authentication is also enabled. See: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-authentication-policies     

-  If you are using a WAP (Web Application Proxy) it is possible that the client goes through the proxy instead of AD FS and therefore is prompting through a webform.    

-  The user agent string of your browser is not supported for Windows Integrated Authentication, explained here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia    

 If you have a Windows popup and NOT a webform, it could be other issues, you can check this out: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-iwa
