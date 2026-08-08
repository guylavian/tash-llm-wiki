---
title: "LDAP user not found"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/916979/ldap-user-not-found
question_id: 916979
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-cpp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# LDAP user not found

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/916979/ldap-user-not-found (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using following LDAP query to find a user using ldap_search_s(). But it does not return any results.  

(&(objectCategory=User)(|(sAMAccountName=<User Name>)))

Where as below powershell command with same user name returns results  

Get-ADUser -LDAPFilter "(&(objectCategory=User)(|(sAMAccountName=<User Name>)))"

The name contains \. I am not sure if it is significant. I am not sure whether i need to add something extra during search  

DistinguishedName : CN=LastName\, FirstName.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-13*

Hello All,

It is possible to enable some logging on the client, but normal users (including administrators) don't have the access rights to modify the most specific configuration location.

Assuming that the ADWS web client is being hosted by PowerShell.exe, then these elements can be added to the PowerShell.exe.config file:

```
<configuration>
  <configSections>
    <section 
       name="Microsoft.ActiveDirectory" 
       type="Microsoft.ActiveDirectory.Management.ConfigurationHandler, Microsoft.ActiveDirectory.Management, Version=10.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"/>
    <section 
      name="Trace" 
      type="Microsoft.ActiveDirectory.Management.TraceElement, Microsoft.ActiveDirectory.Management, Version=10.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"/>
  </configSections>
  <Microsoft.ActiveDirectory>
    <Trace level="Verbose" />
  </Microsoft.ActiveDirectory>
  <system.diagnostics>  
    <trace>  
      <listeners>  
        <add name="Gary" type="System.Diagnostics.ConsoleTraceListener" />  
      </listeners>  
    </trace>  
  </system.diagnostics>  
</configuration>
```

The settings are slightly documented here: https://learn.microsoft.com/en-us/dotnet/api/microsoft.activedirectory.management.configurationhandler

When PowerShell is next started, the ActiveDirectory module cmdlets should display debugging output in the console window:

> PS C:\Users\Gary\Home\2022> Get-ADUser -Server localhost -SearchBase "dc=home,dc=org" -Filter *
> 
> [13/07/2022 19:27:04] powershell: 6212: level=Verbose: logFile=
> [13/07/2022 19:27:04] 10: ADProvider: Verbose: Entering InitializeDefaultDrives
> [13/07/2022 19:27:04] 10: ADProvider: Verbose: Entering GetRootDSE
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: GetEntry: Entering
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: AddEntry: Adding Entry , Key: 4e242830-3927-43f1-9d0a-b7cc0803054c:389
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: AddRef: new count = 1
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: Constructor AdwsConnection 0x16A44E3
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: AuthType is Negotiate
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: calling DsGetDcName for server  with flags 1074790416
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: Delete: ref count = 1
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: Release: Releasing object new count = 0
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: DeleteEntry: removing entry 4e242830-3927-43f1-9d0a-b7cc0803054c:389 from sessioncache
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: FindEntryInServerList: Found 1 session(s) in cache with key: 4e242830-3927-43f1-9d0a-b7cc0803054c:389
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: FindEntryInServerList. Found a cached session entry:
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: Delete: ref count is 0, destroying object
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: AdwsConnection Dispose 0x16A44E3
> [13/07/2022 19:27:04] 10: ADProvider: Error: InitializeDefaultDrives:Ignoring exception while initializing default drive, exception = Microsoft.ActiveDirectory.Management.ADServerDownException: Unable to find a default server with Active Directory Web Services running. ---> Microsoft.ActiveDirectory.Management.ADException: Unable to find a default server with flags: 'MinimumDirectoryServiceVersion:Windows2000 | ADWS | ReturnDnsName'.
>    --- End of inner exception stack trace ---
>    at Microsoft.ActiveDirectory.Management.AdwsConnection.DiscoverServerName(Boolean forceDiscovery)
>    at Microsoft.ActiveDirectory.Management.AdwsConnection.CreateEndpointAddress(String configName)
>    at Microsoft.ActiveDirectory.Management.AdwsConnection.InitializeChannelTChannel
>    at Microsoft.ActiveDirectory.Management.AdwsConnection.SearchAnObject(ADSearchRequest request)
>    at Microsoft.ActiveDirectory.Management.AdwsConnection.Search(ADSearchRequest request)
>    at Microsoft.ActiveDirectory.Management.ADWebServiceStoreAccess.Microsoft.ActiveDirectory.Management.IADSyncOperations.Search(ADSessionHandle handle, ADSearchRequest request)
>    at Microsoft.ActiveDirectory.Management.ADObjectSearcher.GetRootDSE(ICollection`1 propertyList, Boolean propertyNamesOnly) &gt;    at Microsoft.ActiveDirectory.Management.Provider.ADProvider.GetRootDSE(ADSessionInfo sessionInfo, ICollection`1 propertiesToRetrieve)
>    at Microsoft.ActiveDirectory.Management.Provider.ADProvider.InitializeDefaultDrives()
> [13/07/2022 19:27:04] 10: ADProvider: Verbose: Leaving InitializeDefaultDrives
> [13/07/2022 19:27:04] 10: ADCmdletBase: Info: Entering BeginProcessing
> [13/07/2022 19:27:04] 10: CmdletSubroutinePipeline: Info: Invoking Method: Boolean ADGetCmdletBaseBeginCSRoutine() on Target: Microsoft.ActiveDirectory.Management.Commands.GetADUser
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: GetEntry: Entering
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: AddEntry: Adding Entry , Key: localhost:389
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: AddRef: new count = 1
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: Constructor AdwsConnection 0x70D1BE
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: GetEntry: Entering
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: FindEntryInServerList: Found 1 session(s) in cache with key: localhost:389
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: FindEntryInServerList. Found a cached session entry: localhost
> [13/07/2022 19:27:04] 10: ADSessionCache: Info: AddRef: new count = 2
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: AuthType is Negotiate
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: calling DsGetDcName for server localhost with flags 1074790416
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: Endpoint: net.tcp://localhost:9389/ActiveDirectoryWebServices/Windows/Resource
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: PortNumber is 389
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: AdwsConnection 0x70D1BE: WS-T Get request message:
> [13/07/2022 19:27:04] 10: AdwsConnection: Verbose: <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing" xmlns:addata="http://schemas.microsoft.com/2008/1/ActiveDirectory/Data" xmlns:ad="http://schemas.microsoft.com/2008/1/ActiveDirectory" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
>     <s:Header>
>         <a:Action s:mustUnderstand="1">http://schemas.xmlsoap.org/ws/2004/09/transfer/Get</a:Action>
>         <ad:instance>ldap:389</ad:instance>
>         <ad:objectReferenceProperty>11111111-1111-1111-1111-111111111111</ad:objectReferenceProperty>
>     </s:Header>
>     <s:Body />
> </s:Envelope>
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: AutoReconnect is enabled
> [13/07/2022 19:27:08] 10: AdwsConnection: Warning: IChannelFactory.Close thrown exception: System.ServiceModel.CommunicationObjectFaultedException: The communication object, System.ServiceModel.Channels.ServiceChannel, cannot be used for communication because it is in the Faulted state.
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: Forcing rediscovery of server name
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: calling DsGetDcName for server localhost with flags 1074790417
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: Endpoint: net.tcp://localhost:9389/ActiveDirectoryWebServices/Windows/Resource
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: AdwsConnection 0x70D1BE: WS-T Get request message:
> [13/07/2022 19:27:08] 10: AdwsConnection: Verbose: <s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing" xmlns:addata="http://schemas.microsoft.com/2008/1/ActiveDirectory/Data" xmlns:ad="http://schemas.microsoft.com/2008/1/ActiveDirectory" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
>     <s:Header>
>         <a:Action s:mustUnderstand="1">http://schemas.xmlsoap.org/ws/2004/09/transfer/Get</a:Action>
>         <ad:instance>ldap:389</ad:instance>
>         <ad:objectReferenceProperty>11111111-1111-1111-1111-111111111111</ad:objectReferenceProperty>
>     </s:Header>
>     <s:Body />
> </s:Envelope>
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: Delete: ref count = 2
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: Release: Releasing object new count = 1
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: Delete: ref count = 1
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: Release: Releasing object new count = 0
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: DeleteEntry: removing entry localhost:389 from sessioncache
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: FindEntryInServerList: Found 1 session(s) in cache with key: localhost:389
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: FindEntryInServerList. Found a cached session entry: localhost
> [13/07/2022 19:27:12] 10: ADSessionCache: Info: Delete: ref count is 0, destroying object
> [13/07/2022 19:27:12] 10: AdwsConnection: Verbose: AdwsConnection Dispose 0x70D1BE
> [13/07/2022 19:27:12] 10: AdwsConnection: Warning: IChannelFactory.Close thrown exception: System.ServiceModel.CommunicationObjectFaultedException: The communication object, System.ServiceModel.Channels.ServiceChannel, cannot be used for communication because it is in the Faulted state.
> [13/07/2022 19:27:12] 10: ADCmdletBase: Info: Exiting BeginProcessing
> Get-ADUser : Unable to contact the server. This may be because this server does not exist, it is currently down, or it
> does not have the Active Directory Web Services running.
> At line:1 char:1
> + Get-ADUser -Server localhost -SearchBase "dc=home,dc=org" -Filter *
> + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>     + CategoryInfo          : ResourceUnavailable: (:) [Get-ADUser], ADServerDownException
>     + FullyQualifiedErrorId : ActiveDirectoryServer:0,Microsoft.ActiveDirectory.Management.Commands.GetADUser

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

Hello

Thank you for your question and reaching out. I can understand you are having issues related to Ldap search

Please enter correct DN if you have special characters in user name , and After adding the backslash,  

I had incorrectly entered the DN of the particular LDAP user. I had failed to escape the comma in CN=Smith\, John.

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-08*

I did manage to get the ADWS logging enabled using this article, however, the entries are case sensitive and there are typo in the article.  These are the commands I added to enable the logging:    

```
  

```

This is the powershell command I ran:    

```
Get-ADUser -LDAPFilter "(&(objectCategory=User)(|(sAMAccountName=reynolds, gary)))"
```

Logging details:    

```
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] PreparePageSearch: entering  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] PreparePageSearch: set mode for LdapQuery to Paged  
DirectoryActionImplementation: [8/07/2022 1:11:44 PM] [e] NextQueryPage: retrieving a page  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] GetNextPageSearchResults: entering  
LdapSessionPoolImplementation: [8/07/2022 1:11:44 PM] [e] GetReservedConnection: entering, instance=NTDS  
ConnectionPool: [8/07/2022 1:11:44 PM] [e] GetReservedConnection: entering, instance=NTDS  
ConnectionPool: [8/07/2022 1:11:44 PM] [e] GetReservedConnection: incrementing pool use count, instance=NTDS  
ReservationToken: [8/07/2022 1:11:44 PM] [e] UpdateLastUsedTime: new last used time is 8/07/2022 3:11:44 AM  
ConnectionPool: [8/07/2022 1:11:44 PM] [e] GetReservedConnection: got reserved connection, instance=NTDS, new pool count=1, new entry count=1  
LdapSessionPoolImplementation: [8/07/2022 1:11:44 PM] [e] GetReservedConnection: got connection from token, instance=NTDS  
LdapAdaptor: [8/07/2022 1:11:44 PM] [e] Constructor entered  
LdapAdaptor: [8/07/2022 1:11:44 PM] [e] Constructor complete  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] GetNextPageSearchResults: filter is '(&(&(objectCategory=User)(|(sAMAccountName=reynolds, gary)))(objectClass=user)(objectCategory=person))', base DN is 'DC=w2k12,DC=local', scope is 'Subtree'  
DirectoryUtilities: [8/07/2022 1:11:44 PM] [e] GetTimeRemaining: remaining time is 00:02:00  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] GetNextPageSearchResults: client-requested server time limit=00:02:00, using 00:02:00  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] AddInControlsToRequest: adding 1 controls to System.DirectoryServices.Protocols.SearchRequest  
DirectoryDataAccessImplementation: [8/07/2022 1:11:44 PM] [e] AddInControlsToRequest: adding type=1.2.840.113556.1.4.801, criticality=True
```

While the ADWS has changed the filter by adding additional indexes, it doesn't do any additional searches, which doesn't explain why the powershell command works, are you able to share the details of the commands you ran and the details of the user account attributes?    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-08*

Hi @Renjith vr       

I think there are two parts to your question,     

-  What is the filter required for the ldap_search_s function    

-  Why does the Powershell Get-ADUser work    

I'm not sure I can answer question 2, as powershell uses the ADWS service and I've haven't been able to get any details from the network traces as the traffic is encrypted.  But I'm making the assumption that powershell command and the ADWS may do some additional processing to find the object or its using the GC to search the forest.  If you do want to get more details on this, it might be worth raising another question with the windows-server-powershell tag and see if any of the powershell expert have more insights.    

But I can provide some additional information for Question 1.    

With the ldap_search_s() function make sure you define the scope parameter as LDAP_SCOPE_SUBTREE to search the entire domain, if the object exists in a different domain in the same forest, you will need to complete a few additional steps,  find and connect to a DC with GC and find the root DN of the forest and then use the ldap_search_s against that connection and root DN.  Also if the object you are searching for has been deleted you will need to use the ldap_search_ext_s function and include the delete & restore server side controls to find the object.    

Filter Syntax:    

It looks like you are trying to search using the user's displayname rather than the samaccountname in your filter.  The displayname and samaccountname values are normally different, also the samaccountname does not contain any punctuation characters.     

This is an example user:    

```
DN> CN=Reynolds\, Gary,OU=test1,DC=w2k12,DC=local  
  > cn: Reynolds, Gary  
  > sn: Reynolds  
  > givenName: Gary  
  > distinguishedName: CN=Reynolds\, Gary,OU=test1,DC=w2k12,DC=local  
  > displayName: Reynolds, Gary  
  > name: Reynolds, Gary  
  > sAMAccountName: greynolds  
  > userPrincipalName: greynolds@w2k12.local
```

As you can see the samaccountname is different to the displayname, so you will need to use a different filter based on the attribute you are searching.      

Your filter:    

(&(objectCategory=User)(|(sAMAccountName=<user name>)))    

You can optimize your filter as you have extra logic operator that is not required.  This would be a better filter based on a samaccountname search:    

```
(&(objectCategory=User)(sAMAccountName=greynolds))
```

You can optimize the filter further by including an additional index:    

```
(&(objectcategory=user)(objectclass=user)(samaccountname=greynolds))
```

If you want to search for the display name then filter would look like this:    

```
(&(objectcategory=user)(objectclass=user)(displayname=reynolds, gary))
```

There is no need to escape the comma in the search value, as this will be passed as clear text to the server to process.  The disadvantage of this filter is that the displayname must be an exact match of the search value, any difference in spelling the search will fail.     

You could use an Ambiguous Name Resolution (ANR) based filter which will search a number of attributes for the specified value, which will search all attributes that have the ANR_INDEX flag set on the searchflags attribute.  You can use the AD: Schema Attributes ANR Indexed in NetTools to list the attributes that will be included in the ANR search.    

```
(ANR=reynolds, gary)
```

Again, this assumes that the search value is an exact match for the value, if you want to search for reynolds or gary, then use this ANR filter:    

```
(|(anr=reynolds)(anr=gary))
```

I hope that helps.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-07*

So this is an escape character (forward slash) and causes problem with the ldap_search function. I'd recommend removing the \ from the user object.
