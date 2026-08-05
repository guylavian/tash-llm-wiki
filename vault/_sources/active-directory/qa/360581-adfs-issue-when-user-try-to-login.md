---
title: "ADFS Issue when user try to login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/360581/adfs-issue-when-user-try-to-login
question_id: 360581
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Issue when user try to login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/360581/adfs-issue-when-user-try-to-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are looking to make an SAAS application to work with our ADFS server.  

But we are facing some errors when trying to log as a AD use with theses tree errors:

Error 1

Échec de la validation du jeton.

Données supplémentaires

Type de jeton :  

http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName  

%Message d'erreur :  

hidden-Le nom d’utilisateur ou le mot de passe est incorrect

Détails de l'exception :  

System.IdentityModel.Tokens.SecurityTokenValidationException: ***hidden**** ---> System.ComponentModel.Win32Exception: Le nom d’utilisateur ou le mot de passe est incorrect  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

--- Fin de la trace de la pile d'exception interne ---  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)

System.ComponentModel.Win32Exception (0x80004005): Le nom d’utilisateur ou le mot de passe est incorrect  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)

End Error 1

Error 2

Une erreur s'est produite lors du traitement d'une demande de jeton. Les données de cet événement possèdent probablement l'identité de l'appelant (application) qui a effectué cette demande. Elles incluent des informations Activity ID que vous pouvez renvoyer vers des événements d'erreur ou d'avertissement afin de diagnostiquer le problème qui a entraîné cette erreur.

Données supplémentaires

Appelant :

Utilisateur OnBehalfOf :

Utilisateur ActAs :

Partie de confiance cible :  

http://hidenfsname/adfs/services/trust

Identité du périphérique :

Action utilisateur :  

Utilisez les données Activity ID de ce message pour rechercher et associer les données aux événements du journal d'événements à l'aide de l'observateur d'événements. Cet Activity ID est également affiché en tant qu'informations supplémentaires dans la page d'erreur lorsqu'une erreur se produit dans l'application Web passive de fédération.

End Error 2

Error 3

Une erreur s'est produite au cours d'une demande passive de fédération.

Données supplémentaires

Nom de protocole :  

wsfed

Partie de confiance :  

urn:hidden

Détails de l'exception :  

Microsoft.IdentityServer.AuthenticationFailedException: hidden-Le nom d’utilisateur ou le mot de passe est incorrect ---> System.IdentityModel.Tokens.SecurityTokenValidationException: hidden ---> System.ComponentModel.Win32Exception: Le nom d’utilisateur ou le mot de passe est incorrect  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

--- Fin de la trace de la pile d'exception interne ---  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

à Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

à Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)  

à Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)    --- Fin de la trace de la pile d'exception interne ---    à Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)  

à Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestBearerToken(MSISRequestSecurityToken signInRequest, Uri& replyTo, IList`1& identityClaimCollection)  

à Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.RequestSingleSignOnToken(ProtocolContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

à Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSsoSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken, SecurityToken& ssoSecurityToken)  

à Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponseCoreWithSecurityToken(WSFederationSignInContext context, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

à Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.BuildSignInResponse(WSFederationSignInContext federationPassiveContext, SecurityToken securityToken, SecurityToken deviceSecurityToken)  

à Microsoft.IdentityServer.Web.Protocols.WSFederation.WSFederationProtocolHandler.Process(ProtocolContext context)  

à Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

à Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

System.IdentityModel.Tokens.SecurityTokenValidationException: hidden ---> System.ComponentModel.Win32Exception: Le nom d’utilisateur ou le mot de passe est incorrect  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

--- Fin de la trace de la pile d'exception interne ---  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateTokenInternal(UsernameAuthenticationContext usernameAuthenticationContext, SecurityToken token)  

à Microsoft.IdentityServer.Service.Tokens.MsisLocalCpUserNameSecurityTokenHandler.ValidateToken(SecurityToken token)  

à Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.GetEffectivePrincipal(SecurityTokenElement securityTokenElement, SecurityToken deviceSecurityToken, SecurityTokenHandlerCollection securityTokenHandlerCollection)  

à Microsoft.IdentityServer.Web.WSTrust.SecurityTokenServiceManager.Issue(RequestSecurityToken request, IList`1& identityClaimSet, List`1 additionalClaims)  

à Microsoft.IdentityServer.Web.Protocols.PassiveProtocolHandler.SubmitRequest(MSISRequestSecurityToken request, IList`1& identityClaimCollection)

System.ComponentModel.Win32Exception (0x80004005): Le nom d’utilisateur ou le mot de passe est incorrect  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserHandle(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, SafeCloseHandle& tokenHandle, SafeLsaReturnBufferHandle& profileHandle)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUserInfo(SafeHGlobalHandle pLogonInfo, Int32 logonInfoSize, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String authenticationType, String issuerName)  

à Microsoft.IdentityServer.Tokens.LsaLogonUserHelper.GetLsaLogonUser(String domain, String username, String password, DateTime& nextPasswordChange, DateTime& lastPasswordChange, String issuerName)  

à Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.ValidateUser(IAuthenticationContext context)

End Error 3

Can someone help with this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-19*

Hello,  

No boddy have idea?  

Regards
