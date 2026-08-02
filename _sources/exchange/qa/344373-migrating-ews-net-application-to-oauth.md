---
title: "Migrating EWS-.NET-application to OAuth"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/344373/migrating-ews-net-application-to-oauth
question_id: 344373
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Migrating EWS-.NET-application to OAuth

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/344373/migrating-ews-net-application-to-oauth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we are trying to migrate an existing ews-application to OAuth-authentification. The application is a windows .net-service, which exports mails from the exchange server/Office 365-mailbox, so we need an authentification without user interaction (user and password are given in the app config).    

We've tried to implement the oauth-authentication according to the documentation at https://learn.microsoft.com/de-de/exchange/client-developer/exchange-web-services/how-to-authenticate-an-ews-application-by-using-oauth, but ran into errors when getting the token.    

Here is an example code how we try to get the token:    

```
var pcaOptions = new Microsoft.Identity.Client.PublicClientApplicationOptions  
{  
    ClientId = "...",  
    TenantId = "..."  
};  
  
Microsoft.Identity.Client.IPublicClientApplication app = Microsoft.Identity.Client.PublicClientApplicationBuilder.CreateWithApplicationOptions(pcaOptions).Build();  
  
System.Net.NetworkCredential ncCredentials = new System.Net.NetworkCredential("user-mail", "password");  
  
Microsoft.Identity.Client.AuthenticationResult aResult = await appDMMail.AcquireTokenByUsernamePassword(new string[] { "https://outlook.office365.com/EWS.AccessAsUser.All" }, ncCredentials.UserName, ncCredentials.SecurePassword).ExecuteAsync();  
  
Microsoft.Exchange.WebServices.Data.ExchangeService exService = new Microsoft.Exchange.WebServices.Data.ExchangeService();  
exService.Url = new Uri("https://outlook.office365.com/EWS/Exchange.asmx");  
  
exService.Credentials = new Microsoft.Exchange.WebServices.Data.OAuthCredentials(aResult.AccessToken);  
  
Microsoft.Exchange.WebServices.Data.NameResolutionCollection nrcMailbox = exService.ResolveName("...");
```

When executing the code, we always get an MsalClientException-exception when calling AcquireTokenByUsernamePassword: "Federated service at https://autologon.microsoftazuread-sso.com/proalpha.com/winauth/trust/2005/usernamemixed?client-request-id=... returned error: Authentication Failure".    

When replacing the "AcquireTokenByUsernamePassword" method with "AcquireTokenInteractive" (in a .net-windows-test-application), we get a login window as expected, but after entering the credentials, we get another error: "AADSTS50020: User account '...' from identity provider 'live.com' does not exist in tenant 'Microsoft Services' and cannot access the application '...'(<description>) in that tenant. The account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Azure Active Directory user account."    

The message displays the correct user and app id/description.    

I've used the same user and password that is used for configuring/registrating the app in the Azure AD. Login with this credentials in a browser does always work without errors.    

Can you give me a hint, what am i doing wrong here? Am i missing something in the app registration? The application has no verified publisher at the moment, could this perhaps cause the authentication failure? What else can i check?    

Any help would be very appreciated, thank you!    

Best regards,    

Daniel

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-04-07*

It sounds like you have used a (MSA) Microsoft Account (rather then the Office365) account to create the application registration, because the publisher isn't verified you won't be able to use it in your Office365 tenant https://learn.microsoft.com/en-us/azure/active-directory/develop/publisher-verification-overview. What you need to do is logon with the Office365 account and create your Application registration in the Tenant itself and consent to it there.      

Generally if you have ADFS and your try to use ROPC (resource owner password credential)https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth-ropc then MSAL will try to do and Active ADFS authentication which basically is a SOAP authentication request with the username and password against to your OnPrem ADFS server (vs a Passive auth which is a forms based authentication against ADFS).  To make things easier from an Auth perspective have you considered using ClientCredentials flow https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow. This will simplify your authentication greatly and should make it more secure as you nolonger have a username and password, if your concerned about the app having access to mailboxes it shouldn't you can scope the access using application policies https://techcommunity.microsoft.com/t5/exchange-team-blog/application-access-policy-support-in-ews/ba-p/2110361#:~:text=Background,on%20behalf%20of%20a%20user.&text=Using%20an%20application%20access%20policy,an%20inclusion%20or%20exclusion%20list.
