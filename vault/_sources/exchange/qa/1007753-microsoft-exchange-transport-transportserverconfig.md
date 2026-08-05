---
title: "Microsoft.Exchange.Transport.TransportServerConfiguration. Microsoft Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1007753/microsoft-exchange-transport-transportserverconfig
question_id: 1007753
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Microsoft.Exchange.Transport.TransportServerConfiguration. Microsoft Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1007753/microsoft-exchange-transport-transportserverconfig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All, thank you for reading first of all. we have exchange server 2019 with Aug-2022 CU12    

and two servers exchange 2016. however, Exch2019 is the frontend and transport server as we disabled the service on the other two exch2016 servers.     

however, when I restart the Transport service I get the following warning in event logs. after 3 tries, the service will start.     

any ideas or help would be appreciated.     

Event ID 16019    

Active Directory directory service encountered an error for Microsoft.Exchange.Transport.TransportServerConfiguration. Microsoft Exchange will retain the existing configuration, if available. Exception details: Microsoft.Exchange.Data.Directory.ADInvalidServiceCredentialException: Active Directory operation failed on . The supplied credential for 'NT AUTHORITY\NETWORK SERVICE' is invalid. ---> System.DirectoryServices.Protocols.LdapException: The supplied credential is invalid.    

  at System.DirectoryServices.Protocols.LdapConnection.BindHelper(NetworkCredential newCredential, Boolean needSetCredential)    

  at Microsoft.Exchange.Data.Directory.PooledLdapConnection.BindWithLogging(String callerInfo)    

  at Microsoft.Exchange.Data.Directory.PooledLdapConnection.BindWithRetry(String callerInfo, Int32 maxRetries)    

  --- End of inner exception stack trace ---    

  at Microsoft.Exchange.Data.Directory.PooledLdapConnection.BindWithRetry(String callerInfo, Int32 maxRetries)    

  at Microsoft.Exchange.Data.Directory.LdapConnectionPool.CreateOneTimeConnection(NetworkCredential networkCredential, ADServerInfo serverInfo, LocatorFlags connectionFlags)    

  at Microsoft.Exchange.Data.Directory.TopologyProvider.PopulateDomainNamingContexts(String partitionFqdn)    

  at Microsoft.Exchange.Data.Directory.TopologyProvider.GetRootDomainNamingContext(String partitionFqdn)    

  at Microsoft.Exchange.Data.Directory.ADDataSession.GetNamingContext(ADNamingContext adNamingContext)    

  at Microsoft.Exchange.Data.Directory.ADDataSession.GetRootDomainNamingContext(String callerFilePath, Int32 callerFileLine, String memberName)    

  at Microsoft.Exchange.Data.Directory.ADObject.ValidateSingleADObjectLinkValue(ADPropertyDefinition propertyDefinition, ADObjectId value, List`1 errors)       at Microsoft.Exchange.Data.Directory.ADObject.ValidateRead(List`1 errors)    

  at Microsoft.Exchange.Data.ConfigurableObject.ValidateRead()    

  at Microsoft.Exchange.Data.Directory.ADDataSession.ObjectsFromEntriesTResult    

  at Microsoft.Exchange.Data.Directory.ADDataSession.InternalFindTResult    

  at Microsoft.Exchange.Data.Directory.ADDataSession.FindTResult    

  at Microsoft.Exchange.Data.Directory.ADDataSession.FindTResult    

  at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADTopologyConfigurationSession.FindServerByFqdn(String serverFqdn, String callerFilePath, Int32 callerFileLine, String memberName)    

  at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADTopologyConfigurationSession.FindLocalServer(String callerFilePath, Int32 callerFileLine, String memberName)    

  at Microsoft.Exchange.Transport.TransportServerConfiguration.GetNotificationRootId()    

  at Microsoft.Exchange.Data.Directory.ADNotificationAdapter.<>c__DisplayClass9_0`1.<TryRegisterChangeNotification>b__0()    

  at Microsoft.Exchange.Data.Directory.ADNotificationAdapter.RunADOperation(ADOperation adOperation, Int32 retryCount)

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-15*

Hi @EG.Reddy  ,    

Welcome to the Microsoft Q&A platform!    

Do you mean to restart the Transport service on Exchange 2016?  After 3 attempts, will the service start normally?    

Are the three servers installed in the same domain?    

Based on your description, it seems that the transport server configuration is abnormal.    

You can refer to the following documentation：    

MSExchangeTransport 16019 | Microsoft Learn (Note: Related to Exchange 2010).     

front-end-microsoft-exchange-transport-service-stops    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
