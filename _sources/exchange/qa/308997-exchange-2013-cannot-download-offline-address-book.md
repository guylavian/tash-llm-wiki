---
title: "Exchange 2013 - cannot download offline address book"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/308997/exchange-2013-cannot-download-offline-address-book
question_id: 308997
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 - cannot download offline address book

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/308997/exchange-2013-cannot-download-offline-address-book (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, My environment : 3 Exchange 2013 servers (Mailbox + CAS roles) CU23 in 1 DAG    

Last week, after applied security update KB5000871 , MS Outlook cannot download offline address book anymore, users get error "8004010F". Global address book is ok, so new created users can be found when using OWA , cannot be found when using MS Outlook.    

Test-Email AutoConfiguration doesn't show OAB in result    

    

I look into OAB virtual directory (in ECP) and see that "External Url" is empty , I filled "External Url", should I restart IIS to make it effect ?     

```
Get-OfflineAddressBook | fl  
  
  
RunspaceId                       : 9340cbfd-0d61-41f5-b6bb-582269ad7a88  
Server                           :  
GeneratingMailbox                : mydomain.com/Users/SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}  
AddressLists                     : {\Default Global Address List}  
Versions                         : {Version4}  
IsDefault                        : True  
PublicFolderDatabase             :  
PublicFolderDistributionEnabled  : False  
GlobalWebDistributionEnabled     : False  
WebDistributionEnabled           : True  
ShadowMailboxDistributionEnabled : False  
LastTouchedTime                  : 3/11/2021 2:44:47 AM  
LastRequestedTime                :  
LastFailedTime                   :  
LastNumberOfRecords              : 1693  
LastGeneratingData               : MailboxGuid: 06796656-9c16-4fa8-8b33-a3b06b770a60; DatabaseGuid:  
                                   72ba4b24-0ef1-4e32-b395-4be833144954; Server: ex.mydomain.com  
MaxBinaryPropertySize            : 32768  
MaxMultivaluedBinaryPropertySize : 65536  
MaxStringPropertySize            : 3400  
MaxMultivaluedStringPropertySize : 65536  
ConfiguredAttributes             : {OfficeLocation, ANR, ProxyAddresses, ANR, PhoneticGivenName, ANR, GivenName, ANR,  
                                   PhoneticSurname, ANR, Surname, ANR, Account, ANR, PhoneticDisplayName, ANR,  
                                   DisplayNameUnicode, ANR, ExternalMemberCount, Value, TotalMemberCount, Value,  
                                   ModerationEnabled, Value, DelivContLength, Value, MailTipTranslations, Value,  
                                   ObjectGuid, Value, IsOrganizational, Value...}  
DiffRetentionPeriod              : 30  
Schedule                         : {Sun.5:00 AM-Sun.5:15 AM, Mon.5:00 AM-Mon.5:15 AM, Tue.5:00 AM-Tue.5:15 AM,  
                                   Wed.5:00 AM-Wed.5:15 AM, Thu.5:00 AM-Thu.5:15 AM, Fri.5:00 AM-Fri.5:15 AM, Sat.5:00  
                                   AM-Sat.5:15 AM}  
VirtualDirectories               : {ex\OAB (Exchange Back End)}  
AdminDisplayName                 :  
Identity                         : \Default Offline Address Book  
IsValid                          : True  
ExchangeVersion                  : 0.20 (15.0.0.0)  
Name                             : Default Offline Address Book  
DistinguishedName                : CN=Default Offline Address Book,CN=Offline Address Lists,CN=Address Lists  
                                   Container,CN=First Organization,CN=Microsoft  
                                   Exchange,CN=Services,CN=Configuration,DC=mydomain,DC=com  
Guid                             : 650a2e7c-5e15-439b-bba4-848d83976b9e  
ObjectCategory                   : mydomain.com/Configuration/Schema/ms-Exch-OAB  
ObjectClass                      : {top, msExchOAB}  
WhenChanged                      : 3/11/2021 2:44:46 AM  
WhenCreated                      : 3/19/2013 2:56:20 PM  
WhenChangedUTC                   : 3/10/2021 7:44:46 PM  
WhenCreatedUTC                   : 3/19/2013 7:56:20 AM  
OrganizationId                   :  
Id                               : \Default Offline Address Book  
OriginatingServer                : dc.mydomain.com  
ObjectState                      : Unchanged
```

I did some search and found some guide said that "GlobalWebDistributionEnabled" , "WebDistributionEnabled" should be set to True and "VirtualDirectories" should be said to null. Should I do this ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi Lucas,  

I tried command to generation of OAB and verified the OAB generation is normal under the path %ExchangeInstallPath%\ClientAccess\OAB\<ObjectGuid>  

]2

This happen to all users, not specific user.  

I will try “GlobalWebDistributionEnabled” and “VirtualDirectories” and feedback later , but I have a concern about Autodiscover virtual directory url , here is my settings :

```
Get-ClientAccessServer | FL *iden*,*uri*  

Identity                       : ex01  
AutoDiscoverServiceInternalUri : https://webmail.mydomain.com/Autodiscover/Autodiscover.xml  

Identity                       : ex02  
AutoDiscoverServiceInternalUri : https://webmail.mydomain.com/Autodiscover/Autodiscover.xml  

Identity                       : ex03  
AutoDiscoverServiceInternalUri : https://webmail.mydomain.com/Autodiscover/Autodiscover.xml  

Get-AutoDiscoverVirtualDirectory | fl identity,internalurl,externalurl  

Identity    : ex01\Autodiscover (Default Web Site)  
InternalUrl :  
ExternalUrl :  

Identity    : ex02\Autodiscover (Default Web Site)  
InternalUrl :  
ExternalUrl :  

Identity    : ex03\Autodiscover (Default Web Site)  
InternalUrl :  
ExternalUrl :
```

Should I Set-AutoDiscoverVirtualDirectory interal and external url for 3 exchange servers ? I read some docs said that they shoud be null by default.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

I tried :  

set oab virtualdirectory url  

    Get-OabVirtualDirectory | fl Identity,url

```
Identity    : ex01\OAB (Default Web Site)
InternalUrl : https://webmail.mydomain.com/OAB
ExternalUrl : https://webmail.mydomain.com/OAB

Identity    : ex02\OAB (Default Web Site)
InternalUrl : https://webmail.mydomain.com/OAB
ExternalUrl : https://webmail.mydomain.com/OAB

Identity    : ex03\OAB (Default Web Site)
InternalUrl : https://webmail.mydomain.com/OAB
ExternalUrl : https://webmail.mydomain.com/OAB
```

Restart IIS website , recycle MSExchangeOABAppPool on 3 exchange servers  

Try Updating OAB using the cmdlet: Update-OfflineAddressBook “Default Offline Address Book” on 3 exchange servers  

Try restart Microsoft Exchange Mailbox Assistant service on 3 exchange servers  

Nothing works.  

Remains solutions :  

Use cmdlet "Set-OfflineAddressBook" to set "GlobalWebDistributionEnabled" , "WebDistributionEnabled"  

Create a new Offline address book and assign it to all the databases  

Please give me some advice, thank you very much.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

I have only 1 Default Offline Address Book and it is configured for all mailbox databases  

```
Get-OfflineAddressBook

Name                                    Versions                                AddressLists
----                                    --------                                ------------
Default Offline Address Book            {Version4}                              {\Default Global Address List}

Get-MailboxDatabase | fl *iden*,*address*

Identity           : Mailbox Database 1
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 2
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 3
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 4
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 5
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 6
OfflineAddressBook : \Default Offline Address Book

Identity           : Mailbox Database 7
OfflineAddressBook : \Default Offline Address Book
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-11*

```
Open the Exchange Management Shell.
Run the Get-OfflineAddressBook cmdlet to obtain a list of available offline address books.
Run the Set-MailboxDatabase cmdlet to configure the offline address book for the database.
```
