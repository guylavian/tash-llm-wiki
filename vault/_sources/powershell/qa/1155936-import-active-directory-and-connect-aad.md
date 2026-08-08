---
title: "Import-Active Directory and Connect-aad"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155936/import-active-directory-and-connect-aad
question_id: 1155936
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Import-Active Directory and Connect-aad

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155936/import-active-directory-and-connect-aad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello is it possible to pull active directory data and Azure AD the connect-aad at the same time in a script if so how. I have this script where I would like to pull the status of hybrid pending joined devices to a spreadsheet if it is possible.    

```
$Start = Get-date  
  
$t = '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);'  
add-type -name win -member $t -namespace native  
[native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle, 0)  
  
import-module ActiveDirectory  
  
$maxPassAge = (Get-ADDefaultDomainPasswordPolicy).MaxPasswordAge.Days  
  
$ouList = 'OU=Users 7,OU=BOS,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=BOS,DC=test,DC=test1,DC=com',  
'OU=Users 7,OU=DC,DC=Test,DC=test1,DC=com','OU=Users 7 Laptop,OU=DC,DC=Test,DC=test1,DC=com',  
'OU=Users 7,OU=DEL,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=DEL,DC=Test,DC=test1,DC=com',  
'OU=Users 7,OU=HBG,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=HBG,DC=Test,DC=test1,DC=com',  
'OU=Users 7,OU=NRK,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=NRK,DC=test,DC=test1,DC=com',  
'OU=Users 7,OU=PHL,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=PHL,DC=Test,DC=test1,DC=com',  
'OU=Users 7,OU=PIT,DC=Test,DC=test1,DC=com','OU=Users Laptop 7,OU=PIT,DC=Test,DC=test1,DC=com',  
'OU=Users Project 7,OU=PIT,DC=Test,DC=test1,DC=com','OU=Users 7,OU=RIC,DC=Test,DC=test1,DC=com',  
'OU=Users Laptop 7,OU=RIC,DC=Test,DC=test1,DC=com','OU=Users 7,OU=TTN,DC=Test,DC=test1,DC=com',  
'OU=Users Laptop 7,OU=TTN,DC=Test,DC=test1,DC=com','OU=Users 7,OU=WNY,DC=Test,DC=test1,DC=com',  
'OU=Users Laptop 7,OU=WNY,DC=Test,DC=test1,DC=com','OU=Users Departed,OU=PIT,DC=Test,DC=test1,DC=com'  
  
  
$properties = @(  
	@{ N = 'First Name'; E = { $_.GivenName } },  
	'Initials',  
	@{ N = 'Last Name'; E = { $_.surname } },  
	@{ N = 'Username'; E = { $_.Samaccountname } },  
	'DisplayName',  
	@{ N = 'Email Address'; E = { $_.emailaddress } },  
	@{ N = 'Office ID'; E = { $_.physicaldeliveryofficename } },  
        @{ N = 'Site Code'; E = { $_.clientSiteCode } },  
	@{ N = 'Office Phone'; E = { $_.telephonenumber } },  
	@{ N = 'Password Last Set'; E = { $_.PasswordLastSet } },  
	@{ N = 'Locked Out'; E = { $_.LockedOut } },  
	@{ N = 'Expiration Date'; E = { (Get-Date $_.PasswordLastSet).AddDays($maxPassAge) } },  
	@{ N = 'PasswordLifeLeft'; E = { if ($_.PasswordExpired) { 0 } Else { $maxPassAge - ((Get-Date) - $_.PasswordLastSet).Days } } },  
	'Description',  
    @{ N = 'Group Membership'; E = {($_.MemberOf | % { Get-ADGroup $_ | Select -ExpandProperty Name} | Sort) -join '; '}},   
	'MobilePhone',  
	'Fax',  
	@{ N = 'Second Office Phone'; E = { $_.otherTelephone } },  
	'Whencreated',  
	'Whenchanged',  
	'BillingMatterID',  
	'Clientbio',  
	'Clientvcard',  
	'Homephone',  
	'Title',  
	'Info',  
    'clientPayStatus',  
    'StreetAddress',  
    'City',  
    'State',  
    'PostalCode',  
    @{ N = 'Country'; E = { $_.co } },  
    @{ N = 'Manager'; E = {%{(Get-ADUser $_.Manager -properties DisplayName).DisplayName}}},  
    'Company',  
    'Department',  
    @{ N = 'Smart Device Type'; E = { $_.clientSmartDeviceType } },  
    @{ N = 'Time Keeper ID'; E = { $_.clientTimeKeeperID } },  
    @{ N = 'Personal Email'; E = { $_.homeEmailAddress } },  
    @{ N = 'Equitrac ID'; E = { $_.pager } },  
    'Division',  
    @{ N = 'Practice Group'; E = { $_.customAttribute3 } },  
    @{ N = 'Dial Code'; E = { $_.customAttribute1 } },  
    'DistinguishedName',  
    'clientPrivateMobile',  
    'clientPronoun',  
    'clientSecondaryOffice',  
    'clientAux1',  
    'clientAux2',  
    'clientCellNum',  
    'clientLinkedin',  
    'clientNoMobileSig',  
    'clientNoReplySig',  
    'customAttribute2',  
    'customAttribute15',	  
    'extensionAttribute1',  
    'extensionAttribute2',  
    'extensionAttribute3',  
    'extensionAttribute5',  
    'extensionAttribute15',  
    'personalTitle',  
    'homeDirectory',  
    'homedrive',  
    'homeMDB',  
    'homePhone',  
    'msExchOWAPolicy',  
    'objectGUID',  
    'objectSid',  
    @{ N = 'Logon Script'; E = { $_.scriptPath } },  
    'targetAddress',  
    'virtualStaff',  
    'TrustedForDelegation',  
    'TrustedToAuthForDelegation',  
    @{ L = 'Show In Address Book'; E = {$_.showinAddressbook -join ";"}},  
    @{ L = 'Public Delegates BL'; E = {$_.publicDelegatesBL -join ";"}},   
    @{ L = 'Proxy Addresses'; E = {$_.ProxyAddresses -join ";"}},  
    'ProtectedFromAccidentalDeletion',  
    @{ N = 'Assigned Workstation'; E = { $_.clientAssignedWorkstation } },  
    @{ N = 'Assigned Workstation 1'; E = { $_.clientAssignedWorkstation1 } },  
    @{ N = 'Assigned Workstation 2'; E = { $_.clientAssignedWorkstation2 } },  
    @{ N = 'Hybrid Joined Pending'; E = {Get-MsolDevice -All -IncludeSystemManagedDevices | where {($_.DeviceTrustType -eq 'Domain Joined') -and (-not([string]($_.AlternativeSecurityIds)).StartsWith("X509:"))}Get-MsolDevice -All -IncludeSystemManagedDevices | where {($_.DeviceTrustType -eq 'Domain Joined') -and (-not([string]($_.AlternativeSecurityIds)).StartsWith("X509:"))} | Select DisplayName,Enabled,DeviceTrustType,DirSyncEnabled,LastDirSyncTime}}	  
)  
$userproperties='physicaldeliveryofficename,telephonenumber,mobilephone,fax,othertelephone,emailaddress,initials,description,passwordlastset,lockedout,whencreated,whenchanged,PasswordExpired,memberof,billingmatterid,clientbio,clientvcard,homephone,title,info,clientpaystatus,streetaddress,city,state,postalcode,co,manager,company,department,clientSmartDeviceType,clientTimeKeeperID,homeEmailAddress,pager,division,customAttribute3,customAttribute1,distinguishedname,clientPrivateMobile,clientPronoun,clientSecondaryOffice,clientAux1,clientAux2,clientCellNum,clientLinkedin,clientNoMobileSig,clientNoReplySig,customAttribute2,extensionAttribute1,extensionAttribute2,extensionAttribute3,extensionAttribute5,extensionAttribute15,personalTitle,homeDirectory,homeMDB,homePhone,msExchOWAPolicy,objectGUID,objectSid,scriptPath,targetAddress,clientAssignedWorkstation,displayname,clientAssignedWorkstation1,customAttribute15,homedrive,virtualStaff,TrustedForDelegation,TrustedToAuthForDelegation,showInAddressbook,publicDelegatesBL,proxyAddresses,ProtectedFromAccidentalDeletion,clientAssignedWorkstation2,clientSiteCode' -split ','  
	  
$ouList |   
	ForEach {  
		Get-ADUser -Filter * -properties $userproperties -SearchBase $_ | where {($_.givenname -ne $null) -and ($_.surname -ne $null)}   
	} | Sort-Object -Unique |  
	Select $properties |    
                Export-Csv 'Y:\HelpDesk\AssetInfo\adusers1.csv' -NotypeInformation  
  
$Time = (Get-Date) - $Start  
$Time
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.    

According to this article https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-import-export-config    

To import previously exported settings:    

-  Install Azure AD Connect on a new server.    

-  Select the Customize option after the Welcome page.    

-  Select Import synchronization settings. Browse for the previously exported JSON settings file.    

-  Select Install.    

And when it comes to connecting the Azure AD, I believe it will be easier or you to check this article https://learn.microsoft.com/en-us/powershell/module/azuread/connect-azuread?view=azureadps-2.0 on your end.    

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
