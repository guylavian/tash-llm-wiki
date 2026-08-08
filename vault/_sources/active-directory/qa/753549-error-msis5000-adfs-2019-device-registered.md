---
title: "Error MSIS5000 ADFS 2019 Device registered"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/753549/error-msis5000-adfs-2019-device-registered
question_id: 753549
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Error MSIS5000 ADFS 2019 Device registered

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/753549/error-msis5000-adfs-2019-device-registered (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have a problem with ADFS 2019. I've configured the device registration and the authentication.     

I configured AAD connect for the writeback device and the hybrid Azure AD join.    

I joined a computer to the domain.     

I get the ms-organization-access and MS-Organization-P2P-Access certificates in computer/my.    

I see the device in Azure and the workstation certificate in the AD on premises (OU = device registered).    

The output of the dsregcmd /status command is shown below. I don't see any particular error.    

I can connect to myapp portal without authentication (SSO).     

However, I can't connect to an internal application hosted on IIS.     

I receive form based authentication from ADFS.     

If I disable this method to leave only device registered, I have the following error in the browser: MSIS5000    

On the other hand, if I connect with a workplace join (work or school account no active directory = Azure AD registered), everything works perfectly.    

The ms-organization-access certificate is in user/my and when connecting to the application I have a prompt to select it (which can be removed if you configure the browser).    

I modified the WIASupportedUserAgents to manage Edge and Firefox, I add the ADFS service url in the intranet zone, I turn off extended protection.    

I tested other solutions found on the internet (like configuring Windows Hello by certificate, works), but nothing resolve the problem.    

In the past, I had done the same configuration on a 2016 server, no problem.     

The 2019 servers are up to date and the WIN 10 is in version 21h2.     

I configured windows hello by certificate I can connect to my app, the certificates and log are good.    

But like device registered method, passport authentication on an internal app does nothing. I have the basic form.    

In the ADFS server logs I also have event 144: No certificate could be found on the Device Registration Service object that can be used as the issuing certificate    

I gave more rights to the service account, same problem.     

Restarting ADFS prevents messages for 30 min from time to time.    

I also have event 1021 (can be corrected because I don't see it coming back anymore): OAuth Exceptions token    

I think the browser does not send the certificate because in computer/my store or that ADFS cannot read it.    

I do not know what to do. Have you encountered this error? is this a bug?    

Regards.     

Error List    

Sur le navigateur (si je laisse que le device registration méthode et passeport)    

Activity ID: 46ad5b76-2bfd-4092-0f00-0080000000f2    

Error details: MSIS5000 : échec de l'authentification du certificat d'appareil.    

Node name: 6e07f77e-70b8-4a75-b3b8-6808d97211f0    

Error time: Mon, 28 Feb 2022 14:32:20 GMT    

Cookie: enabled    

User agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62    

DRS/Admin = Event 144    

No certificate could be found on the Device Registration Service object that can be used as the issuing certificate.    

AD FS/Admin = Event 1021    

Erreur rencontrée lors de la demande de jeton OAuth.     

Microsoft.IdentityServer.Web.Protocols.OAuth.Exceptions.OAuthInvalidGrantException: MSIS9424 : réception d'une demande de support JWT OAuth non valide. Le certificat de périphérique utilisé pour la signature de la demande de support JWT doit être inscrit avec la clé de transport. ---> Microsoft.IdentityServer.Web.Protocols.OAuth.Exceptions.OAuthInvalidGrantException: MSIS9424 : réception d'une demande de support JWT OAuth non valide. Le certificat de périphérique utilisé pour la signature de la demande de support JWT doit être inscrit avec la clé de transport.    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateDeviceObject(DRDevice device)    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.CreateUserToken()    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateJWTBearer()    

   --- Fin de la trace de la pile d'exception interne ---    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateJWTBearer()    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateCore()    

Microsoft.IdentityServer.Web.Protocols.OAuth.Exceptions.OAuthInvalidGrantException: MSIS9424 : réception d'une demande de support JWT OAuth non valide. Le certificat de périphérique utilisé pour la signature de la demande de support JWT doit être inscrit avec la clé de transport.    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateDeviceObject(DRDevice device)    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.CreateUserToken()    

   à Microsoft.IdentityServer.Web.Protocols.OAuth.OAuthToken.OAuthJWTBearerRequestContext.ValidateJWTBearer()    

dsregcmd /status    

+----------------------------------------------------------------------+    

| Device State                                                         |    

+----------------------------------------------------------------------+    

AzureAdJoined : YES    

EnterpriseJoined : NO    

DomainJoined : YES    

DomainName : LAB40    

Device Name : Win10Cli1.lab.xxxx.fr    

+----------------------------------------------------------------------+    

| Device Details                                                       |    

+----------------------------------------------------------------------+    

DeviceId : 5b78dc8e-bc07-4791-8ea1-c7471cdc9fe3    

Thumbprint : AF7D2FF4F1E1E8C0D2BBC5BBEB3593C5CA3CD3D3    

DeviceCertificateValidity : [ 2022-02-27 16:59:58.000 UTC -- 2032-02-27 17:29:58.000 UTC ]    

KeyContainerId : dc857ed4-cb57-4461-9a18-ccadbeecb698    

KeyProvider : Microsoft Software Key Storage Provider    

TpmProtected : NO    

DeviceAuthStatus : SUCCESS    

+----------------------------------------------------------------------+    

| Tenant Details                                                       |    

+----------------------------------------------------------------------+    

TenantName : RÚpertoire par dÚfaut    

TenantId : be1cfaf9-863d-47fb-xxxxxxxxxxxx    

Idp : login.windows.net    

AuthCodeUrl : https://login.microsoftonline.com/be1cfaf9-863d-47fb-xxxxxxxxxxx/oauth2/authorize    

AccessTokenUrl : https://login.microsoftonline.com/be1cfaf9-863d-47fb-xxxxxxxxx/oauth2/token    

MdmUrl :    

MdmTouUrl :    

MdmComplianceUrl :    

SettingsUrl :    

JoinSrvVersion : 2.0    

JoinSrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/device/    

JoinSrvId : urn:ms-drs:enterpriseregistration.windows.net    

KeySrvVersion : 1.0    

KeySrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/key/    

KeySrvId : urn:ms-drs:enterpriseregistration.windows.net    

WebAuthNSrvVersion : 1.0    

WebAuthNSrvUrl : https://enterpriseregistration.windows.net/webauthn/be1cfaf9-863d-47fb-xxxxx/    

WebAuthNSrvId : urn:ms-drs:enterpriseregistration.windows.net    

DeviceManagementSrvVer : 1.0    

DeviceManagementSrvUrl : https://enterpriseregistration.windows.net/manage/be1cfaf9-863d-47fb-xxxxxxx/    

DeviceManagementSrvId : urn:ms-drs:enterpriseregistration.windows.net    

+----------------------------------------------------------------------+    

| User State                                                           |    

+----------------------------------------------------------------------+    

NgcSet : YES    

NgcKeyId : {D4C239CE-6D30-40D3-B87E-Fxxxxxxx}    

CanReset : DestructiveOnly    

WorkplaceJoined : NO    

WamDefaultSet : YES    

WamDefaultAuthority : organizations    

WamDefaultId : https://login.microsoft.com    

WamDefaultGUID : {B16898C6-A148-4967-9171-xxxxxxxx} (AzureAd)    

+----------------------------------------------------------------------+    

| SSO State                                                            |    

+----------------------------------------------------------------------+    

AzureAdPrt : YES    

AzureAdPrtUpdateTime : 2022-02-28 14:20:19.000 UTC    

AzureAdPrtExpiryTime : 2022-03-14 14:20:31.000 UTC    

AzureAdPrtAuthority : https://login.microsoftonline.com/be1cfaf9-863d-47fb-xxxxxxxxx    

EnterprisePrt : YES    

EnterprisePrtUpdateTime : 2022-02-28 14:20:22.000 UTC    

EnterprisePrtExpiryTime : 2022-03-14 14:20:22.000 UTC    

EnterprisePrtAuthority : https://adfs.lab. xxxxx.fr:443/adfs    

+----------------------------------------------------------------------+    

| Diagnostic Data                                                      |    

+----------------------------------------------------------------------+    

AadRecoveryEnabled : NO    

Executing Account Name : LAB\A.Alonso, A.Alonso@jayjay6734  .xxxxxx.fr    

KeySignTest : PASSED    

+----------------------------------------------------------------------+    

| IE Proxy Config for Current User                                     |    

+----------------------------------------------------------------------+    

Auto Detect Settings : YES    

Auto-Configuration URL :    

Proxy Server List :    

Proxy Bypass List :    

+----------------------------------------------------------------------+    

| WinHttp Default Proxy Config                                         |    

+----------------------------------------------------------------------+    

Access Type : DIRECT    

Avec les droits ADMIN cette partie en plus    

+----------------------------------------------------------------------+    

| Ngc Prerequisite Check                                               |    

+----------------------------------------------------------------------+    

IsDeviceJoined : YES    

IsUserAzureAD : NO    

PolicyEnabled : NO    

PostLogonEnabled : YES    

DeviceEligible : YES    

SessionIsNotRemote : YES    

CertEnrollment : none    

PreReqResult : WillNotProvision    

For more information, please visit https://www.microsoft.com/aadjerrors

## Answers

_No answers on this thread._
