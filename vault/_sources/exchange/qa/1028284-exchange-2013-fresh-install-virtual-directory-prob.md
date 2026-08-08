---
title: "Exchange 2013 fresh install - virtual directory problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1028284/exchange-2013-fresh-install-virtual-directory-prob
question_id: 1028284
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 fresh install - virtual directory problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1028284/exchange-2013-fresh-install-virtual-directory-prob (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

Previously my company used Exchange 2013 CU23 on premise (3 physical servers Windows server 2008 R2 , 1 DAG)    

We recently migrated to Microsoft 365, the migration completed successfully , all of our mailboxes have been in the cloud.    

We removed 2 of 3 servers , DAG , mailbox databases ... keep only 1 physical server (stand alone) , 1 mailbox database.    

I want to decommission the last physical Exchange server but this document said that I should keep at least 1 Exchange server on premise so I decide to install one more on virtual machine (Windows server 2012 R2) since the workload is almost completely shifted to Exchange Online, then I can decommission the last physical Exchange server.    

After Exchange installation completed , I can access to "https://vmexchange.mydomain.com/ecp" --> servers --> virtual directories --> owa (Default Web Site) --> authentication , view something bla bla    

Then I restart server for the first time after exchange installed and problem happens    

After server restart I cannot go to owa (Default Web Site) --> authentication anymore , this is error    

    

The same happen with ecp , oab , ... on new vm server only, this is owa virtual directory setting (as default , cause I haven't change anything yet)    

```
RunspaceId                                          : d7c0f836-95ec-4827-ac8d-b38629d74067  
DirectFileAccessOnPublicComputersEnabled            : True  
DirectFileAccessOnPrivateComputersEnabled           : True  
WebReadyDocumentViewingOnPublicComputersEnabled     : True  
WebReadyDocumentViewingOnPrivateComputersEnabled    : True  
ForceWebReadyDocumentViewingFirstOnPublicComputers  : False  
ForceWebReadyDocumentViewingFirstOnPrivateComputers : False  
WacViewingOnPublicComputersEnabled                  : True  
WacViewingOnPrivateComputersEnabled                 : True  
ForceWacViewingFirstOnPublicComputers               : False  
ForceWacViewingFirstOnPrivateComputers              : False  
RemoteDocumentsActionForUnknownServers              : Block  
ActionForUnknownFileAndMIMETypes                    : Allow  
WebReadyFileTypes                                   : {.xlsx, .pptx, .docx, .xls, .rtf, .ppt, .pps, .pdf, .dot, .doc}  
WebReadyMimeTypes                                   : {application/vnd.openxmlformats-officedocument.presentationml.pre  
                                                      sentation, application/vnd.openxmlformats-officedocument.wordproc  
                                                      essingml.document, application/vnd.openxmlformats-officedocument.  
                                                      spreadsheetml.sheet, application/vnd.ms-powerpoint,  
                                                      application/x-mspowerpoint, application/vnd.ms-excel,  
                                                      application/x-msexcel, application/msword, application/pdf}  
WebReadyDocumentViewingForAllSupportedTypes         : True  
WebReadyDocumentViewingSupportedMimeTypes           : {application/msword, application/vnd.ms-excel,  
                                                      application/x-msexcel, application/vnd.ms-powerpoint,  
                                                      application/x-mspowerpoint, application/pdf, application/vnd.open  
                                                      xmlformats-officedocument.wordprocessingml.document, application/  
                                                      vnd.openxmlformats-officedocument.spreadsheetml.sheet, applicatio  
                                                      n/vnd.openxmlformats-officedocument.presentationml.presentation}  
WebReadyDocumentViewingSupportedFileTypes           : {.doc, .dot, .rtf, .xls, .ppt, .pps, .pdf, .docx, .xlsx, .pptx}  
AllowedFileTypes                                    : {.rpmsg, .xlsx, .xlsm, .xlsb, .vstx, .vstm, .vssx, .vssm, .vsdx,  
                                                      .vsdm, .tiff, .pptx, .pptm, .ppsx, .ppsm, .docx...}  
AllowedMimeTypes                                    : {image/jpeg, image/png, image/gif, image/bmp}  
ForceSaveFileTypes                                  : {.html, .swf, .spl, .htm, .dir, .dcr}  
ForceSaveMimeTypes                                  : {Application/x-shockwave-flash, Application/octet-stream,  
                                                      Application/futuresplash, Application/x-director, text/html}  
BlockedFileTypes                                    : {.vsmacros, .msh2xml, .msh1xml, .ps2xml, .ps1xml, .mshxml,  
                                                      .gadget, .mhtml, .psc2, .psc1, .msh2, .msh1, .aspx, .xml, .wsh,  
                                                      .wsf...}  
BlockedMimeTypes                                    : {application/x-javascript, application/javascript,  
                                                      application/msaccess, x-internet-signup, text/javascript,  
                                                      application/xml, application/prg, application/hta,  
                                                      text/scriplet, text/xml}  
RemoteDocumentsAllowedServers                       : {}  
RemoteDocumentsBlockedServers                       : {}  
RemoteDocumentsInternalDomainSuffixList             : {}  
FolderPathname                                      :  
Url                                                 : {}  
LogonFormat                                         : FullDomain  
ClientAuthCleanupLevel                              : High  
LogonPagePublicPrivateSelectionEnabled              : False  
LogonPageLightSelectionEnabled                      : False  
IsPublic                                            : False  
FilterWebBeaconsAndHtmlForms                        : UserFilterChoice  
NotificationInterval                                : 120  
DefaultTheme                                        :  
UserContextTimeout                                  : 60  
ExchwebProxyDestination                             :  
VirtualDirectoryType                                :  
OwaVersion                                          : Exchange2013  
ServerName                                          : IDCEXC008  
InstantMessagingCertificateThumbprint               :  
InstantMessagingServerName                          :  
RedirectToOptimalOWAServer                          : True  
DefaultClientLanguage                               : 0  
LogonAndErrorLanguage                               : 0  
UseGB18030                                          : False  
UseISO885915                                        : False  
OutboundCharset                                     : AutoDetect  
GlobalAddressListEnabled                            : True  
OrganizationEnabled                                 : True  
ExplicitLogonEnabled                                : True  
OWALightEnabled                                     : True  
DelegateAccessEnabled                               : True  
IRMEnabled                                          : True  
CalendarEnabled                                     : True  
ContactsEnabled                                     : True  
TasksEnabled                                        : True  
JournalEnabled                                      : True  
NotesEnabled                                        : True  
RemindersAndNotificationsEnabled                    : True  
PremiumClientEnabled                                : True  
SpellCheckerEnabled                                 : True  
SearchFoldersEnabled                                : True  
SignaturesEnabled                                   : True  
ThemeSelectionEnabled                               : True  
JunkEmailEnabled                                    : True  
UMIntegrationEnabled                                : True  
WSSAccessOnPublicComputersEnabled                   : True  
WSSAccessOnPrivateComputersEnabled                  : True  
ChangePasswordEnabled                               : True  
UNCAccessOnPublicComputersEnabled                   : True  
UNCAccessOnPrivateComputersEnabled                  : True  
ActiveSyncIntegrationEnabled                        : True  
AllAddressListsEnabled                              : True  
RulesEnabled                                        : True  
PublicFoldersEnabled                                : True  
SMimeEnabled                                        : True  
RecoverDeletedItemsEnabled                          : True  
InstantMessagingEnabled                             : True  
TextMessagingEnabled                                : True  
ForceSaveAttachmentFilteringEnabled                 : False  
SilverlightEnabled                                  : True  
PlacesEnabled                                       : False  
WeatherEnabled                                      : True  
AllowCopyContactsToDeviceAddressBook                : True  
AnonymousFeaturesEnabled                            : True  
IntegratedFeaturesEnabled                           : True  
DisplayPhotosEnabled                                : True  
SetPhotoEnabled                                     : True  
PredictedActionsEnabled                             : False  
UserDiagnosticEnabled                               : False  
ReportJunkEmailEnabled                              : True  
WebPartsFrameOptionsType                            : SameOrigin  
AllowOfflineOn                                      : AllComputers  
SetPhotoURL                                         :  
InstantMessagingType                                : None  
Exchange2003Url                                     :  
FailbackUrl                                         :  
Name                                                : owa (Default Web Site)  
InternalAuthenticationMethods                       : {Basic, Fba}  
MetabasePath                                        : IIS://IDCEXC008.mydomain.com/W3SVC/1/ROOT/owa  
BasicAuthentication                                 : True  
WindowsAuthentication                               : False  
DigestAuthentication                                : False  
FormsAuthentication                                 : True  
LiveIdAuthentication                                : False  
AdfsAuthentication                                  : False  
OAuthAuthentication                                 : False  
DefaultDomain                                       :  
GzipLevel                                           : Low  
WebSite                                             : Default Web Site  
DisplayName                                         : owa  
Path                                                : C:\Program Files\Microsoft\Exchange  
                                                      Server\V15\FrontEnd\HttpProxy\owa  
ExtendedProtectionTokenChecking                     : None  
ExtendedProtectionFlags                             : {}  
ExtendedProtectionSPNList                           : {}  
AdminDisplayVersion                                 : Version 15.0 (Build 1497.2)  
Server                                              : IDCEXC008  
InternalUrl                                         : https://idcexc008.mydomain.com/owa  
ExternalUrl                                         :  
ExternalAuthenticationMethods                       : {Fba}  
AdminDisplayName                                    :  
ExchangeVersion                                     : 0.10 (14.0.100.0)  
DistinguishedName                                   : CN=owa (Default Web  
                                                      Site),CN=HTTP,CN=Protocols,CN=IDCEXC008,CN=Servers,CN=Exchange  
                                                      Administrative Group (FYDIBOHF23SPDLT),CN=Administrative  
                                                      Groups,CN=First Organization,CN=Microsoft  
                                                      Exchange,CN=Services,CN=Configuration,DC=mydomain,DC=com  
Identity                                            : IDCEXC008\owa (Default Web Site)  
Guid                                                : b0848d1e-fc3a-477a-a1fc-48c1c89cd18e  
ObjectCategory                                      : mydomain.com/Configuration/Schema/ms-Exch-OWA-Virtual-Directory  
ObjectClass                                         : {top, msExchVirtualDirectory, msExchOWAVirtualDirectory}  
WhenChanged                                         : 9/29/2022 12:10:42 PM  
WhenCreated                                         : 9/29/2022 12:10:42 PM  
WhenChangedUTC                                      : 9/29/2022 5:10:42 AM  
WhenCreatedUTC                                      : 9/29/2022 5:10:42 AM  
OrganizationId                                      :  
Id                                                  : IDCEXC008\owa (Default Web Site)  
OriginatingServer                                   : mydc.mydomain.com  
IsValid                                             : True  
ObjectState                                         : Changed
```

I have installed latest Windows updates , Exchange security update , reinstall Exchange many times.    

Please give me some advice

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

Hi @KyleXu-MSFT   ,    

This is `Test-ServiceHealth` on new exchange server:    

```
Role                    : Mailbox Server Role  
RequiredServicesRunning : True  
ServicesRunning         : {IISAdmin, MSExchangeADTopology, MSExchangeDelivery, MSExchangeIS,  
                          MSExchangeMailboxAssistants, MSExchangeRepl, MSExchangeRPC, MSExchangeServiceHost,  
                          MSExchangeSubmission, MSExchangeThrottling, MSExchangeTransportLogSearch, W3Svc, WinRM}  
ServicesNotRunning      : {}  
  
Role                    : Client Access Server Role  
RequiredServicesRunning : True  
ServicesRunning         : {IISAdmin, MSExchangeADTopology, MSExchangeMailboxReplication, MSExchangeRPC,  
                          MSExchangeServiceHost, W3Svc, WinRM}  
ServicesNotRunning      : {}  
  
Role                    : Unified Messaging Server Role  
RequiredServicesRunning : True  
ServicesRunning         : {IISAdmin, MSExchangeADTopology, MSExchangeServiceHost, MSExchangeUM, W3Svc, WinRM}  
ServicesNotRunning      : {}  
  
Role                    : Hub Transport Server Role  
RequiredServicesRunning : True  
ServicesRunning         : {IISAdmin, MSExchangeADTopology, MSExchangeEdgeSync, MSExchangeServiceHost,  
                          MSExchangeTransport, MSExchangeTransportLogSearch, W3Svc, WinRM}  
ServicesNotRunning      : {}
```

Check about Computer Management on my new created Exchange, I confirm all permission are correct as yours.    

I created a new mailbox hosted on my new Exchange database, I can login to "https://vmexchange.mydomain.com/owa" successfully (ignore certificate warning)    

I old Exchange server is using a SAN cert (will expire soon) , but I don't think certificate is the issue.    

This is a fresh Exchange installation , after installation completed , I can login EAC "https://vmexchange.mydomain.com/ecp" with my domain admin account (new exchange server is using self signed cert)    

Go to --> servers --> virtual directories --> owa (Default Web Site) --> authentication , view something bla bla    

Of course , the installation process ask for restart after that, so I restart server and then :    

I still can login EAC "https://vmexchange.mydomain.com/ecp" with my domain admin account (new exchange server is using self signed cert)    

Go to --> servers --> virtual directories --> owa (Default Web Site) --> general --> ok    

Go to --> servers --> virtual directories --> owa (Default Web Site) --> authentication --> get error    

I can edit virtual directories settings by EMS , I just wonder why a fresh Exchange install can get this error.    

Actually the last Exchange server is kept for nothing.    

My case is closer to scenario 2, I still need to manage my users from on-premises (password synchronization for ex) , I'm worried that uninstall all Exchange on-premises servers may delete Exchange attributes such as authOrig dLMemRejectPerms dLMemSubmitPerms msExchRequireAuthToSendTo etc from AD schema (I still need these attributes)    

I plan to keep Active Directory Federation Services (AD FS) , also have to keep directory synchronization since it is a prerequisite.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

@Jack Chuong       

First, in the Scenario one you could uninstall all Exchange on-premises servers, if you don't need to use ADFS and AAD Connect for local AD.    

About this issue, based on my searching, there exist may thing could cause this issue, I would suggest you take steps below to narrow down this one:    

Make sure all need services running on your Exchange server, run command below on your Exchange server:    

```
Test-ServiceHealth
```

Crete a new mailbox hosted on your new Exchange database. Then assign permission below to this mailbox from ADUC:    

    

Then use this new create admin account to logon ECP with this link: https://localhost/ecp/?ExchClientVer=15    

Check about Computer Management on your new created Exchange, make sure all permission are correct:    

    

    

At last, make sure new created Exchange server and old one use the same certificate.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
