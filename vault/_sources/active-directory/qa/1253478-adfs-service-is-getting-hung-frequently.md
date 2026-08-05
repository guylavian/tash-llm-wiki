---
title: "ADFS service is getting hung frequently."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1253478/adfs-service-is-getting-hung-frequently
question_id: 1253478
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS service is getting hung frequently.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1253478/adfs-service-is-getting-hung-frequently (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hello, 

The ADFS service is getting stuck frequently. When we are trying to reboot the service, we get an error. After rebooting the server, the service will return to normal.

During that time, the group is experiencing an error.

Event logs are mentioned. 

Event id 364 & 111

Error message 
*************

111

********

The Federation Service encountered an error while processing the WS-Trust request. 

Request type: http://schemas.microsoft.com/idfx/requesttype/issue 

Additional Data 

Exception details: 

Microsoft.IdentityServer.Service.SecurityTokenService.ADAccountValidationException: MSIS3173: Active Directory account validation failed. ---> Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapServerUnavailableException: The supplied credential is invalid.

Error code: 49

Server response message: 

 ---> System.DirectoryServices.Protocols.LdapException: The supplied credential is invalid.

   at System.DirectoryServices.Protocols.LdapConnection.BindHelper(NetworkCredential newCredential, Boolean needSetCredential)

   at Microsoft.IdentityServer.GenericLdap.Channel.ConnectionBaseFactory.GenerateConnection()

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapConnectionCache.CacheEntry.CreateConnectionHelper(String server, Boolean isGC, LdapConnectionSettings settings)

   --- End of inner exception stack trace ---

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapConnectionCache.CacheEntry.CreateConnectionHelper(String server, Boolean isGC, LdapConnectionSettings settings)

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapConnectionCache.CacheEntry.CreateConnection(String server, Boolean isGC, LdapConnectionSettings settings)

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapConnectionCache.GetConnectionCore(String server, Boolean isGC, LdapConnectionSettings settings, LdapServerConfiguration& configuration)

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapAttributeStoreReader.GetConnectionToServer()

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapAttributeStoreReader.BeginGetAttributes(Collection`1 attributes, String filter, String location, SearchScope scope, AsyncCallback callback, Object state)

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapAttributeStoreReader.BeginGetAttributes(Collection`1 attributes, String filter, AsyncCallback callback, Object state)

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapAttributeStore.QueryStore(IEnumerator`1 serverEnumerator, String userName, TypedAsyncResult`1 result, Boolean overrideLocation, Collection`1 attributesList, String filter, String location, SearchScope scope)

###########364############

Encountered error during federation passive request. 

Additional Data 

Protocol Name: 

OAuthAuthorizationProtocol 

Relying Party: 

0ce0a7ae-67dd-4ba9-897a-59254fd11c99 

Exception details: 

Microsoft.IdentityServer.Service.SecurityTokenService.ADAccountValidationException: MSIS3173: Active Directory account validation failed. ---> Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapServerUnavailableException: The supplied credential is invalid.

Error code: 49

Server response message: 

 ---> System.DirectoryServices.Protocols.LdapException: The supplied credential is invalid.

   at System.DirectoryServices.Protocols.LdapConnection.BindHelper(NetworkCredential newCredential, Boolean needSetCredential)

   at Microsoft.IdentityServer.GenericLdap.Channel.ConnectionBaseFactory.GenerateConnection()

   at Microsoft.IdentityServer.ClaimsPolicy.Engine.AttributeStore.Ldap.LdapConnectionCache.CacheEntry.CreateConnectionHelper(String server, Boolean isGC, LdapConnectionSettings settings)

   --- End of inner exception stack trace ---
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-25*

Check these two links for help - https://techcommunity.microsoft.com/t5/windows-server-for-it-pro/server-2019-adfs-ldap-errors-after-installing-january-2022-patch/m-p/3118773
https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-ad-fs-issues
