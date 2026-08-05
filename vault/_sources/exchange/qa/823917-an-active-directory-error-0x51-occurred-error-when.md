---
title: "An Active Directory error 0x51 occurred\" error when you run the \"Setup /PrepareAD\" command in  Exchange server 2013."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/823917/an-active-directory-error-0x51-occurred-error-when
question_id: 823917
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
---
# An Active Directory error 0x51 occurred" error when you run the "Setup /PrepareAD" command in  Exchange server 2013.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/823917/an-active-directory-error-0x51-occurred-error-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts  

Can someone from you give an idea how to fix this issue in Exchange ? . We are currently upgrading the CU version of our exchange 2013 Mailbox and CAS server. From CU8 to CU23. Prepare schema is all goods but after performing PrepareAD setup we encountered an error. please see the exact error below.   

we have 6 Exchange server 2013 - CU8   

3 CAS   

3 Mailbox server  

Error:  

The following error was generated when "$error.Clear();  

 initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions  

Was run: Microsoft.Exchange.Data.directory.Suitability DirectoryException: an active directory error 0x51 occured when trying to check the suitability of server DC1.domain.local Error: Active directory response: The LDAP server is unavailable. System.DirectoryServices.Protocol.ldapException: The LDAP server is unavailable.  

  at System.DirectoryServices.Protocols.LdapConnection.Connect()  

   at System.DirectoryServices.Protocols.LdapConnection.BindHelper(NetworkCredential newCredential, Boolean needSetCredential)  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.BindWithLogging()  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.TryBindWithRetry(Int32 maxRetries, ADErrorRecord& errorRecord)  

   --- End of inner exception stack trace ---  

   at Microsoft.Exchange.Data.Directory.TopologyDiscovery.SuitabilityVerifier.CheckIsServerSuitable(String fqdn, Boolean isGlobalCatalog, NetworkCredential credentials, String& writableNC)  

   at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, ADObjectId domain, String serverName, Int32 port, NetworkCredential credential)  

   at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, NetworkCredential networkCredential, String serverName, Int32 port)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.GetConnection(String preferredServer, Boolean isWriteOperation, String optionalBaseDN, ADObjectId& rootId, ADScope scope)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.GetReadConnection(String preferredServer, String optionalBaseDN, ADObjectId& rootId, ADRawEntry scopeDeteriminingObject)  

   at Microsoft.Exchange.Data.Directory.ADGenericReader.GetNextResultCollection(Type controlType, DirectoryControl& responseControl)  

   at Microsoft.Exchange.Data.Directory.ADPagedReader`1.GetNextResultCollection()      at Microsoft.Exchange.Data.Directory.ADGenericPagedReader`1.GetNextPage()  

   at Microsoft.Exchange.Data.Directory.ADGenericPagedReader`1.<GetEnumerator>d__0.MoveNext()      at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.<FindByAccountName>d__3`1.MoveNext()  

   at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.FindByAccountNameT  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-18*

Our exchange server is 2016 CU22. We meet the same problem when try to install CU23.

On new server we try to install exchange 2019 cu14, again the same issue.

We have two domain controller, one PDC and another global catalog. 

Both seems work well. AD explorer has no problem to connect to DC.

No clue what's the reason.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-25*

Hi   

We are currently CU8 version of exchange 2013. it seems the first link solution cannot be fix the issue. however, since the detected DC that are not communicating on our exchange when tried to perform PrepareAD setup is no longer be using. So it is possible to resolve our issue by decommissioning the old writable DC then cleaning up metadata? as describe on the 2nd link

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-24*

Hi Homer,  

Please check. I hope it helps.  

https://support.microsoft.com/en-us/topic/-an-active-directory-error-0x51-occurred-error-when-you-run-the-setup-preparead-command-from-a-dc-in-exchange-2013-5db561d1-ba63-01d0-baf6-5baa7cc31bb5   

Symptoms  

This issue occurs in a domain that has no global catalog servers. This issue occurs after you apply Cumulative Update 5 or a later version of cumulative update for Microsoft Exchange Server 2013 (Cumulative Update 6 or Cumulative Update 7). When this issue occurs, you receive the following error messages:  

[Time_Point_1] [2] [ERROR] An Active Directory error 0x51 occurred when trying to check the suitability of server 'domain_controller_name'. Error: 'Active directory response: The LDAP server is unavailable.'  

[Time_Point_2] [2] [ERROR] The LDAP server is unavailable.  

Note This issue will not occur if you upgrade the domain controller (DC) to a global catalog.  

Cause  

This issue occurs because of a change that introduces DC stickiness for writable sessions into Cumulative Update 5 for Exchange Server 2013.  

Resolution  

To resolve this issue, install Cumulative Update 8 for Exchange Server 2013.  

Additional information:  

https://social.technet.microsoft.com/Forums/en-US/eaca0528-da9a-42b4-b223-512297c40cad/active-directory-error-0x51-occurred-when-trying-to-check-the-suitability-of-server?forum=exchange2010
