---
title: "WAP ADFS and Exchange server OWA = something went wrong outside firewall."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/267818/wap-adfs-and-exchange-server-owa-something-went-wr
question_id: 267818
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# WAP ADFS and Exchange server OWA = something went wrong outside firewall.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/267818/wap-adfs-and-exchange-server-owa-something-went-wr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, been working out the steps to secure exchange server on my test network before tackling it in real life. Used this how to.    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

Test network is domain controller, ADFS server, exchange server, WAP server, all windows 2019. It's all newly installed and updated.     

Prior to making changes to exchange server (part6), WAP and ADFS worked with exchange server (double login, ADFS login and then Exchange login.) after changing Exchange OWA and ECP login to ADFS, i get Something went wrong error. (i am using edge in a inPrivate window)    

:-(    

Something went wrong    

We can't get that information right now. Please try again later.    

X-ClientId: A5ECFAA84B9049B9A6FB9EE0AF1BE4B8    

request-id 0c43f21a-f6b3-4e3c-bd00-6cf5fc301259    

X-OWA-Error Failed to load script: https://mail.MyDomain.com/owa/prem/15.2.792.3/scripts/boot.owaframe.0.mouse.js?bo=1    

X-OWA-Version 15.2.792.3    

X-FEServer MAILX    

X-BEServer MAILX    

Date:2/10/2021 6:41:18 PM    

If i refresh the page, the web address changes to https://mail.mydomain.com/    

interesting point is if i attempt to go to OWA on internal network, it works fine.     

Basically i have run out of ideas.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-12*

Confirming...  

godaddy DNS has both ADFS and mail DNS entries. 443 and 80 are forwarded to WAP.  WAP is connecting to ADFS and Exchange, because when i enter mail.MyDomain.com i get the ADFS login, (am i correct in assuming that comes from ADFS?) Then when i login in, i was getting the OWA login screen. (Until i changed exchange to ADFS login.)  

Does godaddy need a WAP entry?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-12*

Do you meet all the firewall requirements? With all the port forwarding, I am wondering...  

https://www.petenetlive.com/KB/Article/0001546  

Firewall Requirements  

The WAP server either needs a Static public IP address that is registered in public DNS to the URLS you will be pointing to it, or HTTPS port forwarding form the firewalls outside IP address to the internal IP of the WAP server, (if you don’t have spare public IP addresses).  

WAP Server requires TCP Port 443 (HTTPS) open TO it from the outside world.  

WAP Server requires TCP Port 443 (HTTPS) open FROM it to BOTH the exchange server and the ADFS Server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-11*

Exchange is 2019 Version 15.2  

it's on windows 2019 fully patched.  

one small correction to your recap. WAP /ADFS was working prior to me making the changes on exchange server. Gave me ADFS login page and then the exchange login page. OWA would then load. After changes to exchange server it no longer work in any form outside fire wall.  

Thanks

RunspaceId : 804765a5-173e-4d79-b593-b0086e22135e  

AdminEnabled : True  

OwaOptionsEnabled : True  

Name : ecp (Default Web Site)  

InternalAuthenticationMethods : {Adfs}  

MetabasePath : IIS://Mailx.test.MyDomain.com/W3SVC/1/ROOT/ecp  

BasicAuthentication : False  

WindowsAuthentication : False  

DigestAuthentication : False  

FormsAuthentication : False  

LiveIdAuthentication : False  

AdfsAuthentication : True  

OAuthAuthentication : False  

DefaultDomain :  

GzipLevel : Low  

WebSite : Default Web Site  

DisplayName : ecp  

Path : E:\microsoft\exchange server\v15\FrontEnd\HttpProxy\ecp  

ExtendedProtectionTokenChecking : None  

ExtendedProtectionFlags : {}  

ExtendedProtectionSPNList : {}  

AdminDisplayVersion : Version 15.2 (Build 792.3)  

Server : MAILX  

InternalUrl : https://mailx.test.MyDomain.com/ecp  

ExternalUrl :  

ExternalAuthenticationMethods : {Fba}  

AdminDisplayName :  

ExchangeVersion : 0.10 (14.0.100.0)  

DistinguishedName : CN=ecp (Default Web Site),CN=HTTP,CN=Protocols,CN=MAILX,CN=Servers,CN=Exchange  

Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=First  

Organization,CN=Microsoft  

Exchange,CN=Services,CN=Configuration,DC=test,DC=MyDomain,DC=com  

Identity : MAILX\ecp (Default Web Site)  

Guid : c4a8de1c-6d0e-4985-a5d0-5ff8831fc571  

ObjectCategory : test.MyDomain.com/Configuration/Schema/ms-Exch-ECP-Virtual-Directory  

ObjectClass : {top, msExchVirtualDirectory, msExchECPVirtualDirectory}  

WhenChanged : 2/9/2021 4:34:33 PM  

WhenCreated : 2/3/2021 4:48:20 PM  

WhenChangedUTC : 2/10/2021 12:34:33 AM  

WhenCreatedUTC : 2/4/2021 12:48:20 AM  

OrganizationId :  

Id : MAILX\ecp (Default Web Site)  

OriginatingServer : DC1.test.MyDomain.com  

IsValid : True  

ObjectState : Changed

RunspaceId : 804765a5-173e-4d79-b593-b0086e22135e  

DirectFileAccessOnPublicComputersEnabled : True  

DirectFileAccessOnPrivateComputersEnabled : True  

WebReadyDocumentViewingOnPublicComputersEnabled : True  

WebReadyDocumentViewingOnPrivateComputersEnabled : True  

ForceWebReadyDocumentViewingFirstOnPublicComputers : False  

ForceWebReadyDocumentViewingFirstOnPrivateComputers : False  

WacViewingOnPublicComputersEnabled : True  

WacViewingOnPrivateComputersEnabled : True  

ForceWacViewingFirstOnPublicComputers : False  

ForceWacViewingFirstOnPrivateComputers : False  

RemoteDocumentsActionForUnknownServers : Block  

ActionForUnknownFileAndMIMETypes : Allow  

WebReadyFileTypes : {.xlsx, .pptx, .docx, .xls, .rtf, .ppt, .pps, .pdf, .dot, .doc}  

WebReadyMimeTypes : {application/vnd.openxmlformats-officedocument.presentationml.pre  

sentation, application/vnd.openxmlformats-officedocument.wordproc  

essingml.document, application/vnd.openxmlformats-officedocument.  

spreadsheetml.sheet, application/vnd.ms-powerpoint,  

application/x-mspowerpoint, application/vnd.ms-excel,  

application/x-msexcel, application/msword, application/pdf}  

WebReadyDocumentViewingForAllSupportedTypes : True  

WebReadyDocumentViewingSupportedMimeTypes : {application/msword, application/vnd.ms-excel,  

application/x-msexcel, application/vnd.ms-powerpoint,  

application/x-mspowerpoint, application/pdf, application/vnd.open  

xmlformats-officedocument.wordprocessingml.document, application/  

vnd.openxmlformats-officedocument.spreadsheetml.sheet, applicatio  

n/vnd.openxmlformats-officedocument.presentationml.presentation}  

WebReadyDocumentViewingSupportedFileTypes : {.doc, .dot, .rtf, .xls, .ppt, .pps, .pdf, .docx, .xlsx, .pptx}  

AllowedFileTypes : {.rpmsg, .xlsx, .xlsm, .xlsb, .vstx, .vstm, .vssx, .vssm, .vsdx,  

.vsdm, .tiff, .pptx, .pptm, .ppsx, .ppsm, .docx...}  

AllowedMimeTypes : {image/jpeg, image/png, image/gif, image/bmp}  

ForceSaveFileTypes : {.svgz, .html, .xml, .swf, .svg, .spl, .htm, .dir, .dcr}  

ForceSaveMimeTypes : {Application/x-shockwave-flash, Application/octet-stream,  

Application/futuresplash, Application/x-director,  

application/xml, image/svg+xml, text/html, text/xml}  

BlockedFileTypes : {.settingcontent-ms, .printerexport, .appcontent-ms, .appref-ms,  

.vsmacros, .website, .msh2xml, .msh1xml, .diagcab, .webpnp,  

.ps2xml, .ps1xml, .mshxml, .gadget, .theme, .psdm1...}  

BlockedMimeTypes : {application/x-javascript, application/javascript,  

application/msaccess, x-internet-signup, text/javascript,  

application/prg, application/hta, text/scriplet}  

RemoteDocumentsAllowedServers : {}  

RemoteDocumentsBlockedServers : {}  

RemoteDocumentsInternalDomainSuffixList : {}  

FolderPathname :  

Url : {}  

LogonFormat : FullDomain  

ClientAuthCleanupLevel : High  

LogonPagePublicPrivateSelectionEnabled : False  

LogonPageLightSelectionEnabled : False  

FreCardsEnabled : True  

InternalSPMySiteHostURL :  

ExternalSPMySiteHostURL :  

WacEditingEnabled : True  

DropboxAttachmentsEnabled : True  

BoxAttachmentsEnabled : True  

OneDriveAttachmentsEnabled : True  

GoogleDriveAttachmentsEnabled : True  

ClassicAttachmentsEnabled : True  

ReferenceAttachmentsEnabled : True  

SaveAttachmentsToCloudEnabled : True  

ThirdPartyAttachmentsEnabled : True  

IsPublic : False  

ExternalDownloadHostName :  

InternalDownloadHostName :  

FilterWebBeaconsAndHtmlForms : UserFilterChoice  

NotificationInterval : 120  

DefaultTheme :  

UserContextTimeout : 60  

ExchwebProxyDestination :  

VirtualDirectoryType :  

OwaVersion : Exchange2013  

ServerName : MAILX  

InstantMessagingCertificateThumbprint :  

InstantMessagingServerName :  

RedirectToOptimalOWAServer : True  

DefaultClientLanguage : 0  

LogonAndErrorLanguage : 0  

UseGB18030 : False  

UseISO885915 : False  

OutboundCharset : AutoDetect  

GlobalAddressListEnabled : True  

OrganizationEnabled : True  

ExplicitLogonEnabled : True  

OWALightEnabled : True  

DelegateAccessEnabled : True  

IRMEnabled : True  

CalendarEnabled : True  

ContactsEnabled : True  

TasksEnabled : True  

JournalEnabled : True  

NotesEnabled : True  

RemindersAndNotificationsEnabled : True  

PremiumClientEnabled : True  

SpellCheckerEnabled : True  

SearchFoldersEnabled : True  

SignaturesEnabled : True  

ThemeSelectionEnabled : True  

JunkEmailEnabled : True  

UMIntegrationEnabled : True  

WSSAccessOnPublicComputersEnabled : True  

WSSAccessOnPrivateComputersEnabled : True  

ChangePasswordEnabled : True  

UNCAccessOnPublicComputersEnabled : True  

UNCAccessOnPrivateComputersEnabled : True  

ActiveSyncIntegrationEnabled : True  

AllAddressListsEnabled : True  

RulesEnabled : True  

PublicFoldersEnabled : True  

SMimeEnabled : True  

RecoverDeletedItemsEnabled : True  

InstantMessagingEnabled : True  

TextMessagingEnabled : True  

ForceSaveAttachmentFilteringEnabled : False  

SilverlightEnabled : True  

PlacesEnabled : False  

WeatherEnabled : True  

LocalEventsEnabled : False  

InterestingCalendarsEnabled : True  

AllowCopyContactsToDeviceAddressBook : True  

AnonymousFeaturesEnabled : True  

IntegratedFeaturesEnabled : True  

DisplayPhotosEnabled : True  

SetPhotoEnabled : True  

PredictedActionsEnabled : False  

UserDiagnosticEnabled : False  

ReportJunkEmailEnabled : True  

WebPartsFrameOptionsType : SameOrigin  

AllowOfflineOn : AllComputers  

SetPhotoURL :  

InstantMessagingType : None  

Exchange2003Url :  

FailbackUrl :  

Name : owa (Default Web Site)  

InternalAuthenticationMethods : {Adfs}  

MetabasePath : IIS://Mailx.Test.MyDomain.com/W3SVC/1/ROOT/owa  

BasicAuthentication : False  

WindowsAuthentication : False  

DigestAuthentication : False  

FormsAuthentication : False  

LiveIdAuthentication : False  

AdfsAuthentication : True  

OAuthAuthentication : False  

DefaultDomain :  

GzipLevel : Low  

WebSite : Default Web Site  

DisplayName : owa  

Path : E:\microsoft\exchange server\v15\FrontEnd\HttpProxy\owa  

ExtendedProtectionTokenChecking : None  

ExtendedProtectionFlags : {}  

ExtendedProtectionSPNList : {}  

AdminDisplayVersion : Version 15.2 (Build 792.3)  

Server : MAILX  

InternalUrl : https://mailx.Test.MyDomain.com/owa  

ExternalUrl :  

ExternalAuthenticationMethods : {Fba}  

AdminDisplayName :  

ExchangeVersion : 0.10 (14.0.100.0)  

DistinguishedName : CN=owa (Default Web  

Site),CN=HTTP,CN=Protocols,CN=MAILX,CN=Servers,CN=Exchange  

Administrative Group (FYDIBOHF23SPDLT),CN=Administrative  

Groups,CN=First Organization,CN=Microsoft  

Exchange,CN=Services,CN=Configuration,DC=test,DC=MyDomain,DC=com  

Identity : MAILX\owa (Default Web Site)  

Guid : 79dd3416-2f2a-46c6-89f2-90c22c98da22  

ObjectCategory : test.MyDomain.com/Configuration/Schema/ms-Exch-OWA-Virtual-Direc  

tory  

ObjectClass : {top, msExchVirtualDirectory, msExchOWAVirtualDirectory}  

WhenChanged : 2/9/2021 4:35:44 PM  

WhenCreated : 2/3/2021 4:48:14 PM  

WhenChangedUTC : 2/10/2021 12:35:44 AM  

WhenCreatedUTC : 2/4/2021 12:48:14 AM  

OrganizationId :  

Id : MAILX\owa (Default Web Site)  

OriginatingServer : DC1.test.MyDomain.com  

IsValid : True  

ObjectState : Changed

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-11*

More info.  

When i go to https://mail.MyDomain.com/ecp/?ExchClientVer=15, login as exchange admin, i actually get into exchange admin center.   

When i go to https://mail.MyDomain.com/ecp login as a user, eventually i end up with the page opening with headers, but with no information.  

These are the scripts I used on the exchange server to set for ADFS  

Set-EcpVirtualDirectory -Identity "mailx\ecp (default web site)" -AdfsAuthentication $true -BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication $false -WindowsAuthentication $false  

Set-owaVirtualDirectory -Identity "mailx\owa (default web site)" -AdfsAuthentication $true -BasicAuthentication $false -DigestAuthentication $false -FormsAuthentication $false -WindowsAuthentication $false  

ADFS ssl  

Set-OrganizationConfig -AdfsIssuer https://adfs.MyDomain.com.com/adfs/ls/ -AdfsAudienceUris "https://mail.thegeko.com/owa/","https://mail.MyDomain.com/ecp/" -AdfsSignCertificateThumbprint "A77AF0C4E3F92E847730250A75694B12AEF0B29B"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-11*

Hi @20345484      

What's your Exchange server and CU version?    

According to your information above, you have finished all the configurations list in the official document you shared above. After that, you failed login to both Exchange OWA and ECP from external and get the error information above right? Please correct me if I have any misunderstanding about your question.    

Could you please share the configuration of your OWA and ECP virtual directories? Please remember to remove your personal information    

```
Get-EcpVirtualDirectory | FL  
Get-OwaVirtualDirectory | FL
```

In addition, we could also check the application log on the server to get any related error logs when login failed.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
