---
title: "Exchange 2019 CU6 and Exchange Online free/busy one way availability."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108027/exchange-2019-cu6-and-exchange-online-free-busy-on
question_id: 108027
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 2019 CU6 and Exchange Online free/busy one way availability.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108027/exchange-2019-cu6-and-exchange-online-free-busy-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!    

Exchange 2019 CU6 and Exchange Online free/busy one way availability.    

Users from O365 are unable to view free/busy info of OnPrem users.    

Full classic hybrid mode.    

Federation enabled.    

Not sure what to do next/    

Please help.    

HCW finished with an error HCW8064    

Performed all the steps from https://learn.microsoft.com/en-us/exchange/configure-oauth-authentication-between-exchange-and-exchange-online-organizations-exchange-2013-help?redirectedfrom=MSDN    

Test-OAuthConnectivity from OnPrem is ok.    

When trying to perform Test-OAuthConnectivity from Exchange Online Powershell session I've got the following error:    

System.Net.WebException: The remote server returned an error: (500) Internal Server Error.    

                       at System.Net.HttpWebRequest.GetResponse()  

                       at Microsoft.Exchange.Monitoring.TestOAuthConnectivityHelper.SendExchangeOAuthRequest(ADUser use  

                    r, String orgDomain, Uri targetUri, String& diagnosticMessage, Boolean appOnly, Boolean useCachedTo  

                    ken, Boolean reloadConfig)  

I also got an error when performing Get-OrganizationRelationship | Test-OrganizationRelationship -UserIdentity OnPremUser    

STEP 5: Getting organization relationship setting from remote partner...    

RESULT: Unable to retrieve organization relationships from remote organization.    

RESULT: Error.    

LAST STEP: Writing results...    

SerializationData : {0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0...}    

RunspaceId        : 4fdd7f5f-698a-4d31-8c70-ffdbdf4a6874    

Identity          :    

Id                : AutodiscoverServiceCallFailed    

Status            : Ошибка    

Description       : The Autodiscover call failed.    

IsValid           : True    

ObjectState       : New    

Tried this one with no luck https://support.microsoft.com/en-us/kb/2752387    

Here is current config (actual domain change to contoso).    

Get-HybridConfiguration    

RunspaceId                : aeb78195-474a-4042-bf3d-e8ab15bef47c    

ClientAccessServers       : {}    

EdgeTransportServers      : {}    

ReceivingTransportServers : {MXM}    

SendingTransportServers   : {MXM}    

OnPremisesSmartHost       : mxm.contoso.ru    

Domains                   : {contoso.ru}    

Features                  : {FreeBusy, MoveMailbox, Mailtips, MessageTracking, OwaRedirection, OnlineArchive, SecureMai    

                            l, Photos}  

ExternalIPAddresses       : {}    

TlsCertificateName        : <I>CN=GlobalSign RSA OV SSL CA 2018, O=GlobalSign nv-sa, C=BE<S>CN=*.contoso.ru,     

ServiceInstance           : 0    

AdminDisplayName          :    

ExchangeVersion           : 0.20 (15.0.0.0)    

Name                      : Hybrid Configuration    

DistinguishedName         : CN=Hybrid Configuration,CN=Hybrid Configuration,CN=contoso,CN=Microsoft Exchange,CN=Services,C    

                            N=Configuration,DC=contoso,DC=local  

Identity                  : Hybrid Configuration    

Guid                      : 702d7df7-9e4a-462f-b133-12f89bcc8e8c    

ObjectCategory            : contoso.local/Configuration/Schema/ms-Exch-Coexistence-Relationship    

ObjectClass               : {top, msExchCoexistenceRelationship}    

WhenChanged               : 24.09.2020 14:00:52    

WhenCreated               : 20.09.2020 0:18:47    

WhenChangedUTC            : 24.09.2020 11:00:52    

WhenCreatedUTC            : 19.09.2020 21:18:47    

OrganizationId            :    

Id                        : Hybrid Configuration    

OriginatingServer         : contoso-AD.contoso.local    

IsValid                   : True    

ObjectState               : Unchanged    

Get-IntraOrganizationConfiguration (online side)    

OnlineDiscoveryEndpoint                     : https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc    

OnlineTargetAddress                         : contosoru.mail.onmicrosoft.com    

OnPremiseTargetAddresses                    : {contoso.ru}    

OnPremiseDiscoveryEndpoint                  :    

OnPremiseWebServiceEndpoint                 :    

DeploymentIsCompleteIOCReady                :    

HasNonIOCReadyExchangeCASServerVersions     :    

HasNonIOCReadyExchangeMailboxServerVersions :    

Get-IntraOrganizationConfiguration (OnPrem side)    

OnlineDiscoveryEndpoint                     :    

OnlineTargetAddress                         :    

OnPremiseTargetAddresses                    : {}    

OnPremiseDiscoveryEndpoint                  : https://mxm.contoso.ru/autodiscover/autodiscover.svc    

OnPremiseWebServiceEndpoint                 : https://mxm.contoso.ru/ews/exchange.asmx    

DeploymentIsCompleteIOCReady                : True    

HasNonIOCReadyExchangeCASServerVersions     : False    

HasNonIOCReadyExchangeMailboxServerVersions : False    

Get-IntraOrganizationConnector |fl (online)    

SerializationData    : {0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0...}    

RunspaceId           : 20f7bc95-d985-4c9f-88be-1ca6d60eb066    

TargetAddressDomains : {contoso.ru}    

DiscoveryEndpoint    : https://mxm.contoso.ru/autodiscover/autodiscover.svc    

TargetSharingEpr     :    

Enabled              : True    

AdminDisplayName     :    

ExchangeVersion      : 0.20 (15.0.0.0)    

Name                 : HybridIOC - 550d3715-58c4-4079-af8e-b45162205800    

DistinguishedName    : CN=HybridIOC - 550d3715-58c4-4079-af8e-b45162205800,CN=Intra Organization Connectors,CN=Configur    

                       ation,CN=contosoru.onmicrosoft.com,CN=ConfigurationUnits,DC=EURPR05A010,DC=PROD,DC=OUTLOOK,DC=COM  

Identity             : HybridIOC - 550d3715-58c4-4079-af8e-b45162205800    

ObjectCategory       : EURPR05A010.PROD.OUTLOOK.COM/Configuration/Schema/ms-Exch-Intra-Organization-Connector    

ObjectClass          : {top, msExchIntraOrganizationConnector}    

WhenChanged          : 25.09.2020 13:25:05    

WhenCreated          : 24.09.2020 19:19:21    

WhenChangedUTC       : 25.09.2020 10:25:05    

WhenCreatedUTC       : 24.09.2020 16:19:21    

ExchangeObjectId     : 14c000b9-f420-4273-b7bd-c41569de88d8    

OrganizationId       : EURPR05A010.PROD.OUTLOOK.COM/Microsoft Exchange Hosted Organizations/contosoru.onmicrosoft.com - EU    

                       RPR05A010.PROD.OUTLOOK.COM/ConfigurationUnits/contosoru.onmicrosoft.com/Configuration  

Id                   : HybridIOC - 550d3715-58c4-4079-af8e-b45162205800    

Guid                 : 14c000b9-f420-4273-b7bd-c41569de88d8    

OriginatingServer    : AM6PR05A10DC001.EURPR05A010.PROD.OUTLOOK.COM    

IsValid              : True    

ObjectState          : Unchanged    

Get-IntraOrganizationConnector |fl (OnPrem)    

RunspaceId           : 351e931b-be37-4ec6-a819-3cdf611f8ca4    

TargetAddressDomains : {contosoru.mail.onmicrosoft.com}    

DiscoveryEndpoint    : https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc    

Enabled              : True    

AdminDisplayName     :    

ExchangeVersion      : 0.20 (15.0.0.0)    

Name                 : HybridIOC - 2c0c0d83-c6ab-462b-98ab-2401a8bc502d    

DistinguishedName    : CN=HybridIOC - 2c0c0d83-c6ab-462b-98ab-2401a8bc502d,CN=Intra Organization Connectors,CN=contoso,CN=    

                       Microsoft Exchange,CN=Services,CN=Configuration,DC=contoso,DC=local  

Identity             : HybridIOC - 2c0c0d83-c6ab-462b-98ab-2401a8bc502d    

Guid                 : f259c62c-753d-47bf-8328-b31fbe39ee90    

ObjectCategory       : contoso.local/Configuration/Schema/ms-Exch-Intra-Organization-Connector    

ObjectClass          : {top, msExchIntraOrganizationConnector}    

WhenChanged          : 25.09.2020 13:25:18    

WhenCreated          : 24.09.2020 19:19:20    

WhenChangedUTC       : 25.09.2020 10:25:18    

WhenCreatedUTC       : 24.09.2020 16:19:20    

OrganizationId       :    

Id                   : HybridIOC - 2c0c0d83-c6ab-462b-98ab-2401a8bc502d    

OriginatingServer    : contoso-AD.contoso.local    

IsValid              : True    

ObjectState          : Unchanged

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Hi!  

I've stopped this project.  

Moved test mailboxes back to OnPrem and canceled subscription.  

Thanks for help everyone.  

Best regards, Alex.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-02*

During my research I found this excellent article https://techcommunity.microsoft.com/legacyfs/online/media/2019/01/FB_Errors.FixesV6.pdf    

And №6 looks familiar,but not exactly the same:    

6    

Exception Proxy web request failed. , inner exception: The request failed with HTTP status 401: Unauthorized diagnostics: 2000005;reason= "The user specified by the user-context in the token is ambiguous." ;error_category="invalid_user" LID: 43532Cloud to On-Premises, OAUTH usedDuplicate users1)Use LDP.exe or Active Directory Users and Computers snap-in with a custom LDAP query to find the object with the duplicate UPN / SMTP /SIP address.For example, this would be the LDAP filter for user with UPN: @corp.contoso.com, SMTP: user@Company portal   .com, SIP: user@Company portal   .com (|(userPrincipalName=@corp.contoso.com)(proxyAddresses=SMTP:user@Company portal   .com)(proxyAddresses=sip:user@Company portal   .com))     

For more information of using LDP.exe or Active Directory Users and Computers to find AD objects, see this. Once you find the on-premises user with the duplicate address, either change the address for that on premises user or delete the duplicate    

But I can't understand what does it mean.    

I've got users with @Company portal   .com on both sides OnPrem and Online.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

I'm moved back to Classic Configuration.    

Fixed 'Unable to retrieve organization relationships from remote organization'     

My mistake -  TargetAutodiscoverEpr was pointing to EWS instead of Autodoscover at OrganizationRelationship    

Got some progress, no 500 error in IISLog    

Now I'm getting     

2020-10-01 11:45:23 192.168.70.2 POST /autodiscover/autodiscover.svc/WSSecurity &CorrelationID=<empty>;&cafeReqId=287f6ba3-5da3-41f8-92f9-e105fb84e5be; 443 - 52.97.244.45 TestOrganizationRelationship/1.1 - 401 0 0 106    

At the HttpProxy it looks like this:    

2020-10-01T09:55:24.651Z,69c0c712-85ed-458b-a815-44bd17ca06fe,15,2,659,4,,Autodiscover,autodiscover.contoso.ru,/autodiscover/autodiscover.svc/WSSecurity,,,false,,contoso.ru,Smtp~tester3@Company portal   .ru,TestOrganizationRelationship/1.1,52.97.244.45,MXM,401,401,ProtocolError,POST,Proxy,mxm.contoso.local,15.02.0659.000,IntraForest,WSSecurityRequest-SMTP,,,,7637,,,,0,6,,0,,0,,0,0,,0,12,0,0,0,1,5,0,,,,0,12,0,5,6,6,6,12,,,,BeginRequest=2020-10-01T09:55:24.639Z;CorrelationID=<empty>;ProxyState-Run=None;FEAuth=BEVersion-1942127251;RoutingEntry=DatabaseGuid:1ddd6ccf-be67-4cff-8809-6fe9619d437f%40contoso.local%40contoso.local Server:mxm.contoso.local+1942127251@637364095730545592;BeginGetRequestStream=2020-10-01T09:55:24.645Z;OnRequestStreamReady=2020-10-01T09:55:24.646Z;BeginGetResponse=2020-10-01T09:55:24.646Z;OnResponseReady=2020-10-01T09:55:24.651Z;EndGetResponse=2020-10-01T09:55:24.651Z;ProxyState-Complete=WaitForServerResponse;SharedCacheGuard=0;EndRequest=2020-10-01T09:55:24.651Z;S:ServiceLatencyMetadata.AuthModuleLatency=0,WebExceptionStatus=ProtocolError;ResponseStatusCode=401;WebException=System.Net.WebException: The remote server returned an error: (401) Unauthorized    System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)    в Microsoft.Exchange.HttpProxy.ProxyRequestHandler.<>c__DisplayClass199_0.<OnResponseReady>b__0();,,|RoutingDB:1ddd6ccf-be67-4cff-8809-6fe9619d437f,,,CafeV1

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

That's funny.   

I performed Modern Hybrid configuration and got exactly the same HCW8064 error.  

So looks like I've got WSSecurity issue anyway.  

But setting WSSecurityAuthentication $False and $True doesn't help.  

Tried both frontend and backend virtual directories.  

Error "POST /EWS/Exchange.asmx/WSSecurity &CorrelationID=<empty>;&cafeReqId=6fc67b6a-7ca7-436f-92f0-f25788c279d2; 443 - 52.97.244.45 TestOrganizationRelationship/1.1 - 500 0 0 74"  

is present when performing Test-OrganizationRelationship -UserIdentity  

Test-OrganisationRelationship now fails on step 4:  

STEP 4: Getting organization relationship settings from remote partner...  

RESULT: Unable to retrieve organization relationships from remote organization.  

RESULT: Error.  

PS "Application  not found or OnPremisesPublishing is not enabled for your tenant" error has gone.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

Hi @Rubberduck3000   , please try using the ExRCA tool to test the free busy in your environment: https://testconnectivity.microsoft.com/tests/o365    

Below are some links discussed the similar issue as yours:    

Office 365 users can't see free/busy of on-premises users  AND  HCW error OAuth HCW8064    

This error prompted me to perform an IISreset on all on-prem Exchange servers, even tho ExRCA showed everything was fine. After finishing, I ran the OrganizationRelationship test on "O365 to On-prem" again and this time it completed successfully! Checking with my O365 mailbox now showed Free/Busy information of on-prem mailboxes.    

I have to restart IIS services on Exchange server, and after that HCW didn't return any error.    

Office 365 - Exchange Online - Free/Busy Query from Exchange Online Mailbox to On Premises Exchange Fails    

Get-AutodiscoverVirtualDirectory -server | Set-AutodiscoverVirtualDirectory -WSSecurityAuthentication $true    

Get-WebServicesVirtualDirectory -server | Set-WebServicesVirtualDirectory -WSSecurityAuthentication $true    

Next, either do a IISReset or just recycle the following AppPools from IIS Manager:    

MSExchangeAutodiscoverAppPool    

MSExchangeServicesAppPool    

Problem fixed. Run "Test-OrganizationRelationship" from Exchange Online PowerShell and it would work now. And now if you do the free/busy test, it should work.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
