---
title: "How to configure ADFS as Service Provider and get  MSISAuth ADFS Cookies?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/36014/how-to-configure-adfs-as-service-provider-and-get
question_id: 36014
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# How to configure ADFS as Service Provider and get  MSISAuth ADFS Cookies?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/36014/how-to-configure-adfs-as-service-provider-and-get (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm on ADFS 4.0 (Windows Server 2016).  

-  I have an application A which doesn't want to use the ADFS login page.  

-  I have an application B declared as "Relying Party Trust" for the ADFS.  

-  I configure my App A as "Claims Provider Trust".   

-  The App A creates and signs a SAMLResponse  

-  The App A POST the signed SAMLResponse to ADFS /adfs/ls/idpinitiatedsignon  

-  ADFS check the SAMLResponse and redirect the user to the idpinitiatedsignon and says "your are connected".  

-  When I try to go to App B, I have to authenticate my user to ADFS  

-  When I check the cookies, I see SamlSession, MSISIPSelectionPersistent, MSISAuthenticated and MSISLoopDetectionCookie.  

-  Is there a way to get the ADFS MSISAuth Cookie with this flow?   

In the logs I have these messages :   

-  A warning : SSO token is null or empty. Cannot write SSO token to Cookies.  

-  An error : The supplied Claims Provider Trust property https://myidp.app.A from session cookie is not valid  

Thank you in advance for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-29*

Thanks @Cedric D   , we are seeing the same error in the logs and I don't see MSISAuth cookie being set. My understanding is, MSIS cookie is needed only when ADFS is the IDP. We are trying the below flow    

ADFS 5.0 (Windows Server 2019).    

Claim provider trust --> Oracle Identity Federation and ADFS 5.0 (External ADFS)    

Relying Party trust --> Custom Application    

User logs into Identity Provider and Initiates SAML assertion request to ADFS, ADFS need to trust session as OIF is configured as Claim Provider and forward the request to Custom application which is configured relying party. We are seeing additional login page from ADFS before the request is forwarded to custom application    

When I check the cookies, I see SamlSession, MSISAuthenticated and MSISLoopDetectionCookie and error logs are     

-  A warning : SSO token is null or empty. Cannot write SSO token to Cookies.    

-  An error : The supplied Claims Provider Trust property Provider ID from session cookie is not valid    

Same flow works seamless when OIF is replaced by another ADFS    

As per the documentation    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff849212(v=ws.10)?redirectedfrom=MSDN    

OIF can be configured as IDP and ADFS can act as SP. Please note OIF doesnt create MSIS cookie

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-23*

Hello @abhinay agathamudi   ,     

It appears that the only way to get the MSISAuth Cookie is to authenticate with ADFS login page.    

Finally, we implemented the OBO flow : https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow    

-  The App A make a SOAP request to ADFS usernamemixed endpoint and receveid a JWT token for App A    

-  The App A request a token for App B (OBO flow)    

-  The App A send the received access token to the App B    

I hope that will help you!    

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-21*

@Cedric D   , Did you manage to get the solution for the requirement. I have similar requirement

## Answer (community) — community member

*upvotes: 0 · updated: 2020-06-16*

Hi @Pierre Audonnet - MSFT       

The App A has it own login page.    

It's a portal wich allows access to other apps.     

The App A wants to use ADFS for authentication but doesn't want to use ADFS login page. It's a request from the Project Owner.     

1st try: By API    

-  First I checked if there is ADFS API to do this. Apparently not.     

2nd try: With SOAP resquest    

-  Then I use the adfs/services/trust/13/usernamemixed url to send the login/pwd from the App and get a SAML Assertion.     

The App B is is access by a link in App A.    

In ADFS, I created a relying party trust for App A and App B.    

It works but there isn't ADFS cookies (no MSISAuth). When the user goes from the portal App A to App B there is no SSO.    

3rd try: With a SAMLResponse    

-  Because the App A is a portal, the PO wants to try this pattern :     

App A (SP) <> ADFS (IdP) then App A (IdP) <> ADFS (SP) - ADFS (IdP) <> App B (SP)    

Here a diagram to explain the use case.
