---
title: "Exchange Server — pages 441-480"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0441-0480
family: exchange
documentKind: "doc"
abstract: "Exchange 2016 CU20 Active Directory schema changes No changes are made to the Active Directory schema in Exchange 2016 in CU20. Exchange 2016 CU19 Active Directory schema changes This section summarizes the changes that are made to the Active Directory schema when you install Ex"
---

# Exchange Server — pages 441-480

<!-- p.441 -->

Exchange 2016 CU20 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU20.

Exchange 2016 CU19 Active Directory schema
changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange 2016 CU19. This section includes the following subsections:

     Classes modified by Exchange 2016 CU19
     Attributes added by Exchange 2016 CU19

Classes modified by Exchange 2016 CU19
This section contains the classes modified in Exchange 2016 CU19.

                                                                                    ﾉ     Expand table

 Class                                Change                   Attribute/Class

 ms-Exch-Auth-Auth-Server             add: mayContain          msExchCoexistenceDomains

Attributes added by Exchange 2016 CU19
This section contains the attributes added in Exchange 2016 CU19.

     ms-Exch-Coexistence-Domains

Exchange 2016 CU18 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU18.

Exchange 2016 CU17 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU17.

<!-- p.442 -->

Exchange 2016 CU16 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU16.

Exchange 2016 CU15 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU15.

Exchange 2016 CU14 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU14.

Exchange 2016 CU13 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU13.

Exchange 2016 CU12 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU12.

However, a reduction in Active Directory permissions is made: The AdminSDHolder object on the
domain is updated to remove the "Allow" ACE that grants the "Exchange Trusted Subsystem" group
the "Write DACL" right on the "Group" inherited object types. For more information, see KB
4490059   .

Exchange 2016 CU11 Active Directory schema
changes
No changes are made to the Active Directory schema in Exchange 2016 in CU11.

Exchange 2016 CU10 Active Directory schema
changes

<!-- p.443 -->

No changes are made to the Active Directory schema in Exchange 2016 in CU10.

Exchange 2016 CU9 Active Directory schema changes
No changes are made to the Active Directory schema in Exchange 2016 in CU9.

Exchange 2016 CU8 Active Directory schema changes
No changes are made to the Active Directory schema in Exchange 2016 in CU8.

Exchange 2016 CU7 Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange 2016 CU7. This section includes the following subsections:

     Classes added by Exchange 2016 CU7
     Classes modified by Exchange 2016 CU7
     Attributes added by Exchange 2016 CU7
     Attributes modified by Exchange 2016 CU7
     Object IDs added by Exchange 2016 CU7

Classes added by Exchange 2016 CU7
This section contains the classes added in Exchange 2016 CU7.

                                                                                      ﾉ   Expand table

 Class                                                                Change

 ms-Exch-Http-Delivery-Connector                                      ntdsSchemaAdd

Classes modified by Exchange 2016 CU7
This section contains the classes modified in Exchange 2016 CU7.

                                                                                      ﾉ   Expand table

 Class                             Change                       Attribute/Class

 Mail-Recipient                    add: mayContain              msExchImmutableSid

Attributes added by Exchange 2016 CU7

<!-- p.444 -->

This section contains the attributes added in Exchange 2016 CU7.

     ms-Exch-Immutable-Sid

Attributes modified by Exchange 2016 CU7
This section contains the classes modified in Exchange 2016 CU7.

                                                                                        ﾉ   Expand table

 Class                                     Change                     Attribute/Class

 ms-Exch-Group-Security-Flags              ntdsSchemaModify           replace: mapiId: 36111

Object IDs added by Exchange 2016 CU7
The following attribute object IDs are added when you install Exchange 2016 CU7:

     1.2.840.113556.1.5.7000.62.50214
     1.2.840.113556.1.4.7000.102.52161

Exchange 2016 CU6 Active Directory schema changes
No changes are made to the Active Directory schema in Exchange 2016 CU6.

Exchange 2016 CU5 Active Directory schema changes
No changes are made to the Active Directory schema in Exchange 2016 CU5.

Exchange 2016 CU4 Active Directory schema changes
No changes are made to the Active Directory schema in Exchange 2016 CU4.

Exchange 2016 CU3 Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange 2016 CU3. This section includes the following subsections:

     Classes modified by Exchange 2016 CU3
     Attributes added by Exchange 2016 CU3
     Global catalog attributes added by Exchange 2016 CU3
     Object IDs added by Exchange 2016 CU3

<!-- p.445 -->

Classes modified by Exchange 2016 CU3
This section contains the classes modified in Exchange 2016 CU3.

                                                                                     ﾉ   Expand table

 Class                     Change                    Attribute/Class

 Mail-Recipient            add: mayContain           msExchUGEventSubscriptionLink

 Top                       add: mayContain           msExchUGEventSubscriptionBL

Attributes added by Exchange 2016 CU3
This section contains the attributes added in Exchange 2016 CU3.

       ms-Exch-UG-Event-Subscription-Link
       ms-Exch-UG-Event-Subscription-BL

Global catalog attributes added by Exchange 2016 CU3
This section contains the global catalog attributes added in Exchange 2016 CU3.

       ms-Exch-UG-Event-Subscription-Link
       ms-Exch-UG-Event-Subscription-BL

Object IDs added by Exchange 2016 CU3
The following attribute object IDs are added when you install Exchange 2016 CU3:

       1.2.840.113556.1.4.7000.102.52159
       1.2.840.113556.1.4.7000.102.52160

Exchange 2016 CU2 Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange 2016 CU2. This section includes the following subsections:

       Classes modified by Exchange 2016 CU2
       Attributes added by Exchange 2016 CU2
       Global catalog attributes added by Exchange 2016 CU2
       Object IDs added by Exchange 2016 CU2

Classes modified by Exchange 2016 CU2

<!-- p.446 -->

This section contains the classes modified in Exchange 2016 CU2.

                                                                                        ﾉ   Expand table

 Class                          Change                  Attribute/Class

 Mail-Recipient                 add: mayContain          msExchAdministrativeUnitLink

 ms-Exch-Container              add: mayContain          msExchScopeFlags

 Top                            add: mayContain          msExchAdministrativeUnitBL

 ms-Exch-Base-Class             add: mayContain          msExchUserHoldPolicies

Attributes added by Exchange 2016 CU2
This section contains the attributes added in Exchange 2016 CU2.

       ms-Exch-Administrative-Unit-Link
       ms-Exch-Administrative-Unit-BL

Global catalog attributes added by Exchange 2016 CU2
This section contains the global catalog attributes added in Exchange 2016 CU2.

       ms-Exch-Administrative-Unit-Link
       ms-Exch-Administrative-Unit-BL

Object IDs added by Exchange 2016 CU2
The following attribute object IDs are added when you install Exchange 2016 CU2:

       1.2.840.113556.1.4.7000.102.52157
       1.2.840.113556.1.4.7000.102.52158

Exchange 2016 CU1 Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Exchange 2016 CU1. This section includes the following subsections:

       Classes added by Exchange 2016 CU1
       Classes modified by Exchange 2016 CU1
       Attributes added by Exchange 2016 CU1
       Indexed attributes added by Exchange 2016 CU1
       Global catalog attributes added by Exchange 2016 CU1
       Object IDs added by Exchange 2016 CU1

<!-- p.447 -->

Classes added by Exchange 2016 CU1
This section contains the classes added in Exchange 2016 CU1.

                                                                                          ﾉ   Expand table

 Class                                                          Change

 ms-Exch-Mailbox-Policy                                         ntdsSchemaAdd

 ms-Exch-Auth-Policy                                            ntdsSchemaAdd

Classes modified by Exchange 2016 CU1
This section contains the classes modified in Exchange 2016 CU1.

                                                                                          ﾉ   Expand table

 Class                                       Change                Attribute/Class

 ms-Exch-Mail-Storage                        add: mayContain       msExchDataEncryptionPolicyLink

 ms-Exch-Organization-Container              add: mayContain       msExchDataEncryptionPolicyLink

 Top                                         add: mayContain       msExchDataEncryptionPolicyBL

 Top                                         add: mayContain       msExchAuthPolicyBL

 Mail-Recipient                              add: mayContain       msExchAuthPolicyLink

 ms-Exch-Configuration-Unit-Container        add: mayContain       msExchAuthPolicyLink

 ms-Exch-Configuration-Unit-Container        add: mayContain       msExchMSOForwardSyncReplayList

Attributes added by Exchange 2016 CU1
This section contains the attributes added in Exchange 2016 CU1.

       ms-Exch-Data-Encryption-Policy-Link
       ms-Exch-Data-Encryption-Policy-BL
       ms-Exch-Auth-Policy-Link
       ms-Exch-Auth-Policy-BL

Indexed attributes added by Exchange 2016 CU1
This section contains the indexed attributes added in Exchange 2016 CU1.

<!-- p.448 -->

                                                                                       ﾉ   Expand table

 Attribute                                                         Search flag value

 ms-Exch-Data-Encryption-Policy-Link                               1

Global catalog attributes added by Exchange 2016 CU1
This section contains the global catalog attributes added in Exchange 2016 CU1.

     ms-Exch-Data-Encryption-Policy-Link
     ms-Exch-Data-Encryption-Policy-BL
     ms-Exch-Auth-Policy-Link

Object IDs added by Exchange 2016 CU1
The following class object IDs are added when you install Exchange 2016 CU1:

     1.2.840.113556.1.5.7000.62.50212
     1.2.840.113556.1.5.7000.62.50213

The following attribute object IDs are added when you install Exchange 2016 CU1:

     1.2.840.113556.1.4.7000.102.52151
     1.2.840.113556.1.4.7000.102.52152
     1.2.840.113556.1.4.7000.102.52155
     1.2.840.113556.1.4.7000.102.52156

Exchange 2016 RTM Active Directory schema changes
This section summarizes the changes that are made to the Active Directory schema when you install
Release to Manufacturing (RTM) version of Exchange 2016. This section includes the following
subsections:

     Classes added by Exchange 2016 RTM
     Classes modified by Exchange 2016 RTM
     Attributes added by Exchange 2016 RTM
     Global catalog attributes added by Exchange 2016 RTM
     Attributes modified by Exchange 2016 RTM
     Object IDs added by Exchange 2016 RTM
     Indexed attributes added by Exchange 2016 RTM
     Property sets modified by Exchange 2016 RTM
     MAPI IDs added by Exchange 2016 RTM
     Extended rights added by Exchange 2016 RTM

<!-- p.449 -->

  ７ Note

  No changes to the Active Directory schema were made between Exchange 2016 Preview and
  Exchange 2016 RTM.

Classes added by Exchange 2016 RTM
This section contains the classes added in Exchange 2016 RTM.

                                                                              ﾉ    Expand table

 Class                                                             Change

 Exch-Mapi-Virtual-Directory                                       ntdsSchemaAdd

 Exch-Push-Notifications-App                                       ntdsSchemaAdd

 ms-Exch-Account-Forest                                            ntdsSchemaAdd

 ms-Exch-ActiveSync-Device-Autoblock-Threshold                     ntdsSchemaAdd

 ms-Exch-Auth-Auth-Config                                          ntdsSchemaAdd

 ms-Exch-Auth-Auth-Server                                          ntdsSchemaAdd

 ms-Exch-Auth-Partner-Application                                  ntdsSchemaAdd

 ms-Exch-Client-Access-Rule                                        ntdsSchemaModify

 ms-Exch-Config-Settings                                           ntdsSchemaAdd

 ms-Exch-Encryption-Virtual-Directory                              ntdsSchemaAdd

 ms-Exch-Exchange-Transport-Server                                 ntdsSchemaAdd

 ms-Exch-Hosted-Content-Filter-Config                              ntdsSchemaAdd

 ms-Exch-Hygiene-Configuration                                     ntdsSchemaAdd

 ms-Exch-Intra-Organization-Connector                              ntdsSchemaModify

 ms-Exch-MSO-Forward-Sync-Divergence                               ntdsSchemaAdd

 ms-Exch-MSO-Sync-Service-Instance                                 ntdsSchemaAdd

 ms-Exch-Mailflow-Policy                                           ntdsSchemaAdd

 ms-Exch-Mailflow-Policy-Collection                                ntdsSchemaAdd

 ms-Exch-Malware-Filter-Config                                     ntdsSchemaAdd

 ms-Exch-Organization-Upgrade-Policy                               ntdsSchemaAdd

<!-- p.450 -->

 Class                                                                           Change

 ms-Exch-Protocol-Cfg-SIP-Container                                              ntdsSchemaAdd

 ms-Exch-Protocol-Cfg-SIP-FE-Server                                              ntdsSchemaAdd

 ms-Exch-Resource-Policy                                                         ntdsSchemaAdd

 ms-Exch-Safe-Attachment-Protection-Config                                       ntdsSchemaAdd

 ms-Exch-Smart-Links-Protection-Config                                           ntdsSchemaAdd

 ms-Exch-Team-Mailbox-Provisioning-Policy                                        ntdsSchemaAdd

 ms-Exch-Throttling-Policy                                                       ntdsSchemaModify

 ms-Exch-Unified-Policy                                                          ntdsSchemaAdd

 ms-Exch-Unified-Rule                                                            ntdsSchemaAdd

 ms-Exch-Workload-Policy                                                         ntdsSchemaAdd

Classes modified by Exchange 2016 RTM
This section contains the classes modified in Exchange 2016 RTM.

                                                                                            ﾉ    Expand table

 Class                                Change            Attribute/Class

 Exch-Accepted-Domain                 add: mayContain   msExchOfflineOrgIdHomeRealmRecord

 Exch-Base-Class                      add: mayContain   msExchCapabilityIdentifiers

 Exch-Base-Class                      add: mayContain   msExchObjectID

 Exch-Base-Class                      add: mayContain   msExchProvisioningTags

 Exch-Configuration-Unit-             add: mayContain   msExchArchiveRelease
 Container

 Exch-Configuration-Unit-             add: mayContain   msExchMailboxRelease
 Container

 Exch-Exchange-Server                 add: mayContain   msExchArchiveRelease

 Exch-Exchange-Server                 add: mayContain   msExchMailboxRelease

 Exch-MDB-Availability-Group          add: mayContain   msExchEvictedMembersLink

 Exch-OAB                             add: mayContain   msExchLastUpdateTime

 Exch-OWA-Mailbox-Policy              add: mayContain   msExchConfigurationXML

<!-- p.451 -->

Class                             Change            Attribute/Class

Exch-OWA-Virtual-Directory        add: mayContain   msExchConfigurationXML

Exch-On-Premises-Organization     add: mayContain   msExchTrustedDomainLink

Exch-Organization-Container       add: mayContain   msExchMaxABP

Exch-Organization-Container       add: mayContain   msExchMaxOAB

Exch-Organization-Container       add: mayContain   pFContacts

Exch-Team-Mailbox-Provisioning-   add: mayContain   msExchConfigurationXML
Policy

Group                             add:              msExchMailStorage
                                  auxiliaryClass

Mail-Recipient                    add: mayContain   msExchLocalizationFlags

Mail-Recipient                    add: mayContain   msExchRoleGroupType

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Altitude

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Latitude

Mail-Recipient                    add: mayContain   ms-DS-GeoCoordinates-Longitude

Mail-Recipient                    add: mayContain   msExchRecipientSoftDeletedStatus

Mail-Recipient                    add: mayContain   msExchWhenSoftDeletedTime

Mail-Recipient                    add: mayContain   msExchHomeMTASL

Mail-Recipient                    add: mayContain   msExchMailboxMoveSourceArchiveMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveSourceMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveTargetArchiveMDBLinkSL

Mail-Recipient                    add: mayContain   msExchMailboxMoveTargetMDBLinkSL

Mail-Recipient                    add: mayContain   ms-exch-group-external-member-count

Mail-Recipient                    add: mayContain   ms-exch-group-member-count

Mail-Recipient                    add: mayContain   msExchGroupExternalMemberCount

Mail-Recipient                    add: mayContain   msExchGroupMemberCount

Mail-Recipient                    add: mayContain   msExchShadowWhenSoftDeletedTime

Mail-Recipient                    add: mayContain   msExchPublicFolderMailbox

Mail-Recipient                    add: mayContain   msExchPublicFolderSmtpAddress

<!-- p.452 -->

Class                            Change            Attribute/Class

Mail-Recipient                   add: mayContain   msExchAuxMailboxParentObjectIdLink

Mail-Recipient                   add: mayContain   msExchStsRefreshTokensValidFrom

Mail-Recipient                   add: mayContain   msDS-ExternalDirectoryObjectId

Mail-Recipient                   add: mayContain   msExchGroupSecurityFlags

Mail-Recipient                   add: mayContain   msExchMultiMailboxDatabasesLink

Ms-Exch-Organization-Container   add: mayContain   ms-exch-organization-flags-2

Top                              add: mayContain   msExchMultiMailboxDatabasesBL

Top                              add: mayContain   msExchMultiMailboxLocationsBL

Top                              add: mayContain   msExchAccountForestBL

Top                              add: mayContain   msExchTrustedDomainBL

Top                              add: mayContain   msExchAcceptedDomainBL

Top                              add: mayContain   msExchHygieneConfigurationMalwareBL

Top                              add: mayContain   msExchHygieneConfigurationSpamBL

Top                              add: mayContain   msExchEvictedMembersBL

Top                              add: mayContain   msExchOABGeneratingMailboxBL

Top                              add: mayContain   msExchAuxMailboxParentObjectIdBL

ms-Exch-Accepted-Domain          add: mayContain   msExchHygieneConfigurationLink

ms-Exch-Accepted-Domain          add: mayContain   msExchTransportResellerSettingsLinkSL

ms-Exch-Account-Forest           possSuperiors     msExchContainer

ms-Exch-Account-Forest           add: mayContain   msExchPartnerId

ms-Exch-Active-Sync-Device       add: mayContain   msExchDeviceClientType

ms-Exch-Availability-Address-    add: mayContain   msExchFedTargetAutodiscoverEPR
Space

ms-Exch-Base-Class               add: mayContain   msExchDirsyncAuthorityMetadata

ms-Exch-Base-Class               add: mayContain   msExchDirsyncStatusAck

ms-Exch-Base-Class               add: mayContain   msExchEdgeSyncConfigFlags

ms-Exch-Base-Class               add: mayContain   msExchHABRootDepaPreviewentLink

ms-Exch-Base-Class               add: mayContain   msExchDefaultPublicFolderMailbox

<!-- p.453 -->

Class                         Change            Attribute/Class

ms-Exch-Base-Class            add: mayContain   msExchForestModeFlag

ms-Exch-Base-Class            add: mayContain   msExchELCMailboxFlags

ms-Exch-Base-Class            add: mayContain   msExchCanaryData0

ms-Exch-Base-Class            add: mayContain   msExchCanaryData1

ms-Exch-Base-Class            add: mayContain   msExchCanaryData2

ms-Exch-Base-Class            add: mayContain   msExchCorrelationId

ms-Exch-Base-Class            add: mayContain   msExchTenantCountry

ms-Exch-Base-Class            add: mayContain   msExchConfigurationXML

ms-Exch-Base-Class            add: mayContain   msExchMultiMailboxGUIDs

ms-Exch-Base-Class            add: mayContain   msExchMultiMailboxLocationsLink

ms-Exch-Coexistence-          add: mayContain   msExchCoexistenceOnPremisesSmartHost
Relationship

ms-Exch-Coexistence-          add: mayContain   msExchCoexistenceSecureMailCertificateThumbprint
Relationship

ms-Exch-Coexistence-          add: mayContain   msExchCoexistenceTransportServers
Relationship

ms-Exch-Configuration-Unit-   add: mayContain   msExchDirsyncStatus
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchIsDirsyncStatusPending
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchDirSyncServiceInstance
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchOrganizationUpgradePolicyLink
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchManagementSiteLinkSL
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchOrganizationUpgradePolicyLinkSL
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchRelocateTenantCompletionTargetVector
Container

ms-Exch-Configuration-Unit-   add: mayContain   msExchRelocateTenantFlags
Container

<!-- p.454 -->

Class                           Change            Attribute/Class

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantSafeLockdownSchedule
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantSourceForest
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantStartLockdown
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantStartRetired
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantStartSync
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantStatus
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantTargetForest
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchRelocateTenantTransitionCounter
Container

ms-Exch-Configuration-Unit-     add: mayContain   msExchSyncCookie
Container

ms-Exch-Control-Point-Config    add: mayContain   msExchRMSOnlineCertificationLocationUrl

ms-Exch-Control-Point-Config    add: mayContain   msExchRMSOnlineKeySharingLocationUrl

ms-Exch-Control-Point-Config    add: mayContain   msExchRMSOnlineLicensingLocationUrl

ms-Exch-Custom-Attributes       add: mayContain   msExchExtensionCustomAttribute1

ms-Exch-Custom-Attributes       add: mayContain   msExchExtensionCustomAttribute2

ms-Exch-Custom-Attributes       add: mayContain   msExchExtensionCustomAttribute3

ms-Exch-Custom-Attributes       add: mayContain   msExchExtensionCustomAttribute4

ms-Exch-Custom-Attributes       add: mayContain   msExchExtensionCustomAttribute5

ms-Exch-Domain-Content-Config   add: mayContain   msExchContentByteEncoderTypeFor7BitCharsets

ms-Exch-Domain-Content-Config   add: mayContain   msExchContentPreferredInternetCodePageForShiftJis

ms-Exch-Domain-Content-Config   add: mayContain   msExchContentRequiredCharSetCoverage

ms-Exch-Exchange-Server         add: mayContain   msExchWorkloadManagementPolicyLink

ms-Exch-Exchange-Server         add: mayContain   msExchMalwareFilteringDeferAttempts

<!-- p.455 -->

Class                            Change            Attribute/Class

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringDeferWaitTime

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringFlags

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringPrimaryUpdatePath

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringSecondaryUpdatePath

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringUpdateFrequency

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringUpdateTimeout

ms-Exch-Exchange-Server          add: mayContain   msExchMalwareFilteringScanTimeout

ms-Exch-Fed-OrgId                add: mayContain   msExchFedDelegationTrustSL

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamCountryBlockList
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamLanguageBlockList
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamNotifyOutboundRecipients
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamDigestFrequency
Config

ms-Exch-Hosted-Content-Filter-   add: mayContain   msExchSpamQuarantineRetention
Config

ms-Exch-MDB                      add: mayContain   msExchCalendarLoggingQuota

ms-Exch-MRS-Request              add: mayContain   msExchMailboxMoveSourceMDBLinkSL

ms-Exch-MRS-Request              add: mayContain   msExchMailboxMoveStorageMDBLinkSL

ms-Exch-MRS-Request              add: mayContain   msExchMailboxMoveTargetMDBLinkSL

ms-Exch-MSO-Sync-Service-        add: mayContain   msExchMSOForwardSyncNonRecipientCookie
Instance

ms-Exch-MSO-Sync-Service-        add: mayContain   msExchMSOForwardSyncRecipientCookie
Instance

ms-Exch-MSO-Sync-Service-        add: mayContain   msExchMSOForwardSyncReplayList
Instance

ms-Exch-MSO-Sync-Service-        add: mayContain   msExchAccountForestLink
Instance

ms-Exch-MSO-Sync-Service-        add: mayContain   msExchActiveInstanceSleepInterval
Instance

<!-- p.456 -->

Class                       Change            Attribute/Class

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchPassiveInstanceSleepInterval
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncDaemonMaxVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncDaemonMinVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncServiceInstanceNewTenantMaxVersion
Instance

ms-Exch-MSO-Sync-Service-   add: mayContain   msExchSyncServiceInstanceNewTenantMinVersion
Instance

ms-Exch-Mail-Gateway        add: mayContain   msExchHomeMDBSL

ms-Exch-Mail-Gateway        add: mayContain   msExchHomeMTASL

ms-Exch-Mail-Storage        add: mayContain   msExchPreviousArchiveDatabase

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxExpiration

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxOwners

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxSharePointLinkedBy

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxSharePointUrl

ms-Exch-Mail-Storage        add: mayContain   msExchTeamMailboxShowInClientList

ms-Exch-Mail-Storage        add: mayContain   msExchCalendarLoggingQuota

ms-Exch-Mail-Storage        add: mayContain   msExchArchiveDatabaseLinkSL

ms-Exch-Mail-Storage        add: mayContain   msExchDisabledArchiveDatabaseLinkSL

ms-Exch-Mail-Storage        add: mayContain   msExchHomeMDBSL

ms-Exch-Mail-Storage        add: mayContain   msExchMailboxMoveTargetMDBLinkSL

ms-Exch-Mail-Storage        add: mayContain   msExchPreviousArchiveDatabaseSL

ms-Exch-Mail-Storage        add: mayContain   msExchPreviousHomeMDBSL

ms-Exch-Mail-Storage        add: mayContain   msExchMailboxContainerGuid

ms-Exch-Mail-Storage        add: mayContain   msExchUnifiedMailbox

ms-Exch-Mail-Storage        add: mayContain   msExchUserCulture

ms-Exch-Mailflow-Policy     add: mayContain   msExchImmutableId

<!-- p.457 -->

Class                             Change            Attribute/Class

ms-Exch-Malware-Filter-Config     add: mayContain   msExchMalwareFilterConfigExternalSenderAdminAddress

ms-Exch-Malware-Filter-Config     add: mayContain   msExchMalwareFilterConfigInternalSenderAdminAddress

ms-Exch-OAB                       add: mayContain   msExchOffLineABServerSL

ms-Exch-OAB                       add: mayContain   msExchOABGeneratingMailboxLink

ms-Exch-OWA-Mailbox-Policy        add: mayContain   msExchOWASetPhotoURL

ms-Exch-OWA-Virtual-Directory     add: mayContain   msExchOWASetPhotoURL

ms-Exch-Organization-Container    add: mayContain   msExchOrganizationFlags2

ms-Exch-Organization-Container    add: mayContain   msExchUMAvailableLanguages

ms-Exch-Organization-Container    add: mayContain   msExchWACDiscoveryEndpoint

ms-Exch-Organization-Container    add: mayContain   msExchAdfsAuthenticationRawConfiguration

ms-Exch-Organization-Container    add: mayContain   msExchServiceEndPointURL

ms-Exch-Private-MDB               add: mayContain   msExchMailboxDatabaseTransportFlags

ms-Exch-Public-Folder             add: mayContain   msExchPublicFolderEntryId

ms-Exch-Resource-Policy           add: mayContain   msExchCustomerExpectationCritical

ms-Exch-Resource-Policy           add: mayContain   msExchDiscretionaryCritical

ms-Exch-Resource-Policy           add: mayContain   msExchInternalMaintenanceCritical

ms-Exch-Resource-Policy           add: mayContain   msExchUrgentCritical

ms-Exch-Routing-Group-Connector   add: mayContain   msExchHomeMTASL

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigFlags
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigFromAddress
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalBody
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalSenderAdminAddress
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilterConfigInternalSubject
Protection-Config

ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilteringScanTimeout
Protection-Config

<!-- p.458 -->

 Class                             Change            Attribute/Class

 ms-Exch-Safe-Attachment-          add: mayContain   msExchMalwareFilteringUpdateFrequency
 Protection-Config

 ms-Exch-Site-Connector            add: mayContain   msExchHomeMTASL

 ms-Exch-Smart-Links-Protection-   add: mayContain   msExchAddressRewriteExceptionList
 Config

 ms-Exch-Smart-Links-Protection-   add: mayContain   msExchSpamFlags
 Config

 ms-Exch-Tenant-Perimeter-         add: mayContain   msExchTransportResellerSettingsLinkSL
 Settings

 ms-Exch-Throttling-Policy         add: mayContain   msExchThrottlingPolicyFlags

 ms-Exch-Throttling-Policy         add: mayContain   msExchAnonymousThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchEASThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchEWSThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchGeneralThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchIMAPThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchOWAThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchPOPThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchPowershellThrottlingPolicyStateEx

 ms-Exch-Throttling-Policy         add: mayContain   msExchRCAThrottlingPolicyStateEx

 ms-Exch-Transport-Rule            add: mayContain   msExchTransportRuleImmutableId

 ms-Exch-Transport-Rule            add: mayContain   msExchImmutableId

 ms-Exch-Transport-Settings        add: mayContain   msExchTranspoPreviewaxRetriesForLocalSiteShadow

 ms-Exch-Transport-Settings        add: mayContain   msExchTranspoPreviewaxRetriesForRemoteSiteShadow

 ms-Exch-Transport-Settings        add: mayContain   msExchConfigurationXML

 ms-Exch-Virtual-Directory         add: mayContain   msExchMRSProxyFlags

 ms-Exch-Virtual-Directory         add: mayContain   msExchMRSProxyMaxConnections

Attributes added by Exchange 2016 RTM
This section contains the attributes added in Exchange 2016 RTM.

<!-- p.459 -->

ms-DS-GeoCoordinates-Altitude
ms-DS-GeoCoordinates-Latitude
ms-DS-GeoCoordinates-Longitude
ms-Exch-Accepted-Domain-BL
ms-Exch-Account-Forest-BL
ms-Exch-Account-Forest-Link
ms-Exch-ActiveSync-Device-AutoBlock-Duration
ms-Exch-ActiveSync-Device-Autoblock-Threshold-Incidence-Duration
ms-Exch-ActiveSync-Device-Autoblock-Threshold-Incidence-Limit
ms-Exch-ActiveSync-Device-Autoblock-Threshold-Type
ms-Exch-Adfs-Authentication-Raw-Configuration
ms-Exch-Anonymous-Throttling-Policy-State-Ex
ms-Exch-Archive-Database-Link-SL
ms-Exch-Auth-App-Secret
ms-Exch-Auth-Application-Identifier
ms-Exch-Auth-Auth-Server-Type
ms-Exch-Auth-Authorization-Url
ms-Exch-Auth-Certificate-Data
ms-Exch-Auth-Certificate-Thumbprint
ms-Exch-Auth-Flags
ms-Exch-Auth-Issuer-Name
ms-Exch-Auth-Issuing-Url
ms-Exch-Auth-Linked-Account
ms-Exch-Auth-Metadata-Url
ms-Exch-Auth-Realm
ms-Exch-Aux-Mailbox-Parent-Object-Id-BL
ms-Exch-Aux-Mailbox-Parent-Object-Id-Link
ms-Exch-Canary-Data-0
ms-Exch-Canary-Data-1
ms-Exch-Canary-Data-2
ms-Exch-Content-Byte-Encoder-Type-For-7-Bit-Charsets
ms-Exch-Content-Preferred-Internet-Code-Page-For-Shift-Jis
ms-Exch-Content-Required-Char-Set-Coverage
ms-Exch-Correlation-Id
ms-Exch-Customer-Expectation-Critical
ms-Exch-Customer-Expectation-Overloaded
ms-Exch-Customer-Expectation-Underloaded
ms-Exch-Default-Public-Folder-Mailbox
ms-Exch-Device-Client-Type
ms-Exch-Dir-Sync-Service-Instance
ms-Exch-Dirsync-Authority-Metadata
ms-Exch-Dirsync-Status
ms-Exch-Dirsync-Status-Ack

<!-- p.460 -->

ms-Exch-Disabled-Archive-Database-Link-SL
ms-Exch-Discretionary-Critical
ms-Exch-Discretionary-Overloaded
ms-Exch-Discretionary-Underloaded
ms-Exch-EAS-Throttling-Policy-State-Ex
ms-Exch-EWS-Throttling-Policy-State-Ex
ms-Exch-Edge-Sync-Config-Flags
ms-Exch-Encryption-Throttling-Policy-State-Ex
ms-Exch-Extension-Custom-Attribute-1
ms-Exch-Extension-Custom-Attribute-2
ms-Exch-Extension-Custom-Attribute-3
ms-Exch-Extension-Custom-Attribute-4
ms-Exch-Extension-Custom-Attribute-5
ms-Exch-External-Directory-Object-Class
ms-Exch-Fed-Delegation-Trust-SL
ms-Exch-Forest-Mode-Flag
ms-Exch-General-Throttling-Policy-State-Ex
ms-Exch-Group-External-Member-Count
ms-Exch-Group-Member-Count
ms-Exch-Home-MDB-SL
ms-Exch-Home-MTA-SL
ms-Exch-Hosted-Content-Filter-Config-Link
ms-Exch-Hygiene-Configuration-Link
ms-Exch-Hygiene-Configuration-Malware-BL
ms-Exch-Hygiene-Configuration-Spam-BL
ms-Exch-IMAP-Throttling-Policy-State-Ex
ms-Exch-Internal-Maintenance-Critical
ms-Exch-Internal-Maintenance-Overloaded
ms-Exch-Internal-Maintenance-Underloaded
ms-Exch-Is-Dirsync-Status-Pending,
ms-Exch-Localization-Flags
ms-Exch-MRS-Proxy-Flags
ms-Exch-MRS-Proxy-Max-Connections
ms-Exch-MSO-Forward-Sync-Divergence-Count
ms-Exch-MSO-Forward-Sync-Divergence-Related-Object-Link
ms-Exch-MSO-Forward-Sync-Divergence-Timestamp
ms-Exch-Mailbox-Database-Transport-Flags
ms-Exch-Mailbox-Move-Source-Archive-MDB-Link-SL
ms-Exch-Mailbox-Move-Source-MDB-Link-SL
ms-Exch-Mailbox-Move-Storage-MDB-Link-SL
ms-Exch-Mailbox-Move-Target-Archive-MDB-Link-SL
ms-Exch-Mailbox-Move-Target-MDB-Link-SL
ms-Exch-Mailflow-Policy-Countries

<!-- p.461 -->

ms-Exch-Mailflow-Policy-Keywords
ms-Exch-Mailflow-Policy-Publisher-Name
ms-Exch-Mailflow-Policy-Transport-Rules-Template-Xml
ms-Exch-Mailflow-Policy-Version
ms-Exch-Malware-Filter-Config-Alert-Text
ms-Exch-Malware-Filter-Config-External-Body
ms-Exch-Malware-Filter-Config-External-Sender-Admin-Address
ms-Exch-Malware-Filter-Config-External-Subject
ms-Exch-Malware-Filter-Config-Flags
ms-Exch-Malware-Filter-Config-From-Address
ms-Exch-Malware-Filter-Config-From-Name
ms-Exch-Malware-Filter-Config-Internal-Body
ms-Exch-Malware-Filter-Config-Internal-Sender-Admin-Address
ms-Exch-Malware-Filter-Config-Internal-Subject
ms-Exch-Malware-Filter-Config-Link
ms-Exch-Malware-Filtering-Defer-Attempts
ms-Exch-Malware-Filtering-Defer-Wait-Time
ms-Exch-Malware-Filtering-Flags
ms-Exch-Malware-Filtering-Primary-Update-Path
ms-Exch-Malware-Filtering-Scan-Timeout
ms-Exch-Malware-Filtering-Secondary-Update-Path
ms-Exch-Malware-Filtering-Update-Frequency
ms-Exch-Malware-Filtering-Update-Timeout
ms-Exch-Management-Site-Link-SL
ms-Exch-Multi-Mailbox-GUID
ms-Exch-Multi-Mailbox-Locations-Link
ms-Exch-OAB-Generating-Mailbox-BL
ms-Exch-OAB-Generating-Mailbox-Link
ms-Exch-OWA-Set-Photo-URL
ms-Exch-OWA-Throttling-Policy-State-Ex
ms-Exch-Off-Line-AB-Server-SL
ms-Exch-Organization-Flags-2
ms-Exch-Organization-Upgrade-Policy-BL
ms-Exch-Organization-Upgrade-Policy-Date
ms-Exch-Organization-Upgrade-Policy-Enabled
ms-Exch-Organization-Upgrade-Policy-Link
ms-Exch-Organization-Upgrade-Policy-Link-SL
ms-Exch-Organization-Upgrade-Policy-MaxMailboxes
ms-Exch-Organization-Upgrade-Policy-Priority
ms-Exch-Organization-Upgrade-Policy-Source-Version
ms-Exch-Organization-Upgrade-Policy-Status
ms-Exch-Organization-Upgrade-Policy-Target-Version
ms-Exch-POP-Throttling-Policy-State-Ex

<!-- p.462 -->

ms-Exch-Powershell-Throttling-Policy-State-Ex
ms-Exch-Previous-Archive-Database
ms-Exch-Previous-Archive-Database-SL
ms-Exch-Previous-Home-MDB-SL
ms-Exch-Public-Folder-EntryId
ms-Exch-Public-Folder-Mailbox
ms-Exch-Public-Folder-Smtp-Address
ms-Exch-RCA-Throttling-Policy-State-Ex
ms-Exch-RMS-Computer-Accounts-Link-SL
ms-Exch-RMSOnline-Certification-Location-Url
ms-Exch-RMSOnline-Key-Sharing-Location-Url
ms-Exch-RMSOnline-Licensing-Location-Url
ms-Exch-Recipient-SoftDeleted-Status
ms-Exch-Relocate-Tenant-Completion-Target-Vector
ms-Exch-Relocate-Tenant-Flags
ms-Exch-Relocate-Tenant-Safe-Lockdown-Schedule
ms-Exch-Relocate-Tenant-Source-Forest
ms-Exch-Relocate-Tenant-Start-Lockdown
ms-Exch-Relocate-Tenant-Start-Retired
ms-Exch-Relocate-Tenant-Start-Sync
ms-Exch-Relocate-Tenant-Status
ms-Exch-Relocate-Tenant-Target-Forest
ms-Exch-Relocate-Tenant-Transition-Counter
ms-Exch-Resource-Type
ms-Exch-RoleGroup-Type
ms-Exch-Service-End-Point-URL
ms-Exch-Shadow-When-Soft-Deleted-Time
ms-Exch-Spam-Add-Header
ms-Exch-Spam-Asf-Settings
ms-Exch-Spam-Asf-Test-Bcc-Address
ms-Exch-Spam-Country-Block-List
ms-Exch-Spam-Digest-Frequency
ms-Exch-Spam-False-Positive-Cc
ms-Exch-Spam-Flags
ms-Exch-Spam-Language-Block-List
ms-Exch-Spam-Modify-Subject
ms-Exch-Spam-Notify-Outbound-Recipients
ms-Exch-Spam-Outbound-Spam-Cc
ms-Exch-Spam-Quarantine-Retention
ms-Exch-Spam-Redirect-Address
ms-Exch-Sts-Refresh-Tokens-Valid-From
ms-Exch-Sync-Cookie
ms-Exch-Sync-Service-Instance-New-Tenant-Max-Version

<!-- p.463 -->

     ms-Exch-Sync-Service-Instance-New-Tenant-Min-Version
     ms-Exch-Team-Mailbox-Expiration
     ms-Exch-Team-Mailbox-Expiry-Days
     ms-Exch-Team-Mailbox-Owners
     ms-Exch-Team-Mailbox-SharePoint-Linked-By
     ms-Exch-Team-Mailbox-SharePoint-Url
     ms-Exch-Team-Mailbox-Show-In-Client-List
     ms-Exch-Tenant-Country
     ms-Exch-Throttling-Policy-Flags
     ms-Exch-Transport-MaxRetriesForLocalSiteShadow
     ms-Exch-Transport-MaxRetriesForRemoteSiteShadow
     ms-Exch-Transport-Reseller-Settings-Link-SL
     ms-Exch-Transport-Rule-Immutable-Id
     ms-Exch-Trusted-Domain-BL
     ms-Exch-Trusted-Domain-Link
     ms-Exch-UG-Member-BL
     ms-Exch-UG-Member-Link
     ms-Exch-Urgent-Critical
     ms-Exch-Urgent-Overloaded
     ms-Exch-Urgent-Underloaded
     ms-Exch-WAC-Discovery-Endpoint
     ms-Exch-When-Soft-Deleted-Time
     ms-Exch-Workload-Classification
     ms-Exch-Workload-Management-Is-Enabled
     ms-Exch-Workload-Management-Policy
     ms-Exch-Workload-Management-Policy-BL
     ms-Exch-Workload-Management-Policy-Link
     ms-DS-External-Directory-Object-Id
     ms-Exch-Group-Security-Flags
     ms-Exch-Multi-Mailbox-Locations-BL
     ms-Exch-Multi-Mailbox-Databases-Link
     ms-Exch-Multi-Mailbox-Databases-BL

Global catalog attributes added by Exchange 2016 RTM
The following global catalog attributes are added by Exchange 2016 RTM:

     ms-Exch-Archive-Database-Link-SL
     ms-Exch-Correlation-Id
     ms-Exch-Default-Public-Folder-Mailbox
     ms-Exch-Device-Client-Type
     ms-Exch-Dirsync-Authority-Metadata
     ms-Exch-Dirsync-Status

<!-- p.464 -->

ms-Exch-Dirsync-Status-Ack
ms-Exch-Disabled-Archive-Database-Link-SL
ms-Exch-Edge-Sync-Config-Flags
ms-Exch-EvictedMembers-Link
ms-Exch-EvictedMembers-BL
ms-Exch-Extension-Custom-Attribute-1
ms-Exch-Extension-Custom-Attribute-2
ms-Exch-Extension-Custom-Attribute-3
ms-Exch-Extension-Custom-Attribute-4
ms-Exch-Extension-Custom-Attribute-5
ms-Exch-Group-External-Member-Count
ms-Exch-Group-Member-Count
ms-Exch-HAB-Root-DepaPreviewent-Link
ms-Exch-Home-MDB-SL
ms-Exch-Home-MTA-SL
ms-Exch-Is-Dirsync-Status-Pending
ms-Exch-Localization-Flags
ms-Exch-Mailbox-Container-Guid
ms-Exch-Mailbox-Move-Source-Archive-MDB-Link-SL
ms-Exch-Mailbox-Move-Source-MDB-Link-SL
ms-Exch-Mailbox-Move-Storage-MDB-Link-SL
ms-Exch-Mailbox-Move-Target-Archive-MDB-Link-SL
ms-Exch-Mailbox-Move-Target-MDB-Link-SL
ms-Exch-Offline-OrgId-Home-Realm-Record
ms-Exch-Previous-Archive-Database
ms-Exch-Previous-Archive-Database-SL
ms-Exch-Previous-Home-MDB-SL
ms-Exch-RMS-Computer-Accounts-Link-SL
ms-Exch-Recipient-SoftDeleted-Status
ms-Exch-Relocate-Tenant-Completion-Target-Vector,
ms-Exch-Relocate-Tenant-Flags
ms-Exch-Relocate-Tenant-Safe-Lockdown-Schedule
ms-Exch-Relocate-Tenant-Source-Forest
ms-Exch-Relocate-Tenant-Start-Lockdown
ms-Exch-Relocate-Tenant-Start-Retired
ms-Exch-Relocate-Tenant-Start-Sync
ms-Exch-Relocate-Tenant-Status
ms-Exch-Relocate-Tenant-Target-Forest
ms-Exch-Relocate-Tenant-Transition-Counter
ms-Exch-RoleGroup-Type
ms-Exch-Sync-Cookie
ms-Exch-Team-Mailbox-Expiration
ms-Exch-Team-Mailbox-Expiry-Days

<!-- p.465 -->

        ms-Exch-Team-Mailbox-Owners
        ms-Exch-Team-Mailbox-SharePoint-Linked-By
        ms-Exch-Team-Mailbox-SharePoint-Url
        ms-Exch-Team-Mailbox-Show-In-Client-List
        ms-Exch-Unified-Mailbox
        ms-Exch-When-Soft-Deleted-Time

Attributes modified by Exchange 2016 RTM
This section contains the attributes modified in Exchange 2016 RTM.

                                                                                         ﾉ   Expand table

 Attribute         Change                      Value

 Exch-             rangeUpper                  15254
 Configuration-
 Unit-Container

 Exch-Mailflow-    rangeUpper                  256000
 Policy-
 Transport-
 Rules-Template-
 Xml

 Mail-Recipient    Replace: mayContain             msExchUGMemberLink

 Ms-exch-schema-   rangeUpper                  15292
 version-pt

 Top               Replace: mayContain             msExchUGMemberBL

 ms-Exch-          replace: searchFlags        9
 Accepted-
 Domain-Name

 ms-Exch-          replace: searchFlags        9
 Archive-GUID

 ms-Exch-Bypass-   replace: searchFlags        19
 Audit

 ms-Exch-          ntdsSchemaAdd                   attributeID: 1.2.840.113556.1.4.7000.102.51992
 Coexistence-On-                               isMemberOfPartialAttributeSet: FALSE (not in global catalog)
 Premises-Smart-                                   searchFlags: 0 (no index)
 Host

 ms-Exch-          ntdsSchemaAdd                   attributeID: 1.2.840.113556.1.4.7000.102.51991
 Coexistence-                                  isMemberOfPartialAttributeSet: FALSE (not in global catalog)
 Secure-Mail-                                      searchFlags: 0 (no index)

<!-- p.466 -->

Attribute        Change                           Value

Certificate-
Thumbprint

ms-Exch-         rangeUpper                       1024
Coexistence-
Secure-Mail-
Certificate-
Thumbprintms-
Exch-Sync-
Cookie

ms-Exch-         ntdsSchemaAdd                    attributeID: 1.2.840.113556.1.4.7000.102.51990
Coexistence-                                      isMemberOfPartialAttributeSet: FALSE (not in global catalog)
Transport-                                        searchFlags: 0 (no index)
Servers

ms-Exch-ELC-     replace: attributeSecurityGuid   F6SzsVXskUGzJ7cuM+OK8g==
Mailbox-Flags

ms-Exch-         isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-1

ms-Exch-         isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-2

ms-Exch-         isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-3

ms-Exch-         isMemberOfPartialAttributeSet:   TRUE
Extension-
Custom-
Attribute-4

ms-Exch-         isMemberOfPartialAttributeSet    TRUE
Extension-
Custom-
Attribute-5

ms-Exch-Group-   ntdsSchemaModify                 isMemberOfPartialAttributeSet: TRUE MAPIID:36066
External-
Member-Count

ms-Exch-Group-   ntdsSchemaModify                 replace:
Member-Count                                      isMemberOfPartialAttributeSetisMemberOfPartialAttributeSet:
                                                  TRUE MAPIID: 36067

<!-- p.467 -->

 Attribute         Change                          Value

 ms-Exch-HAB-      replace:                        TRUE
 Root-             isMemberOfPartialAttributeSet
 DepaPreviewent-
 Link

 ms-Exch-MSO-      rangeUpper                      20480
 Forward-Sync-
 Non-Recipient-
 Cookie

 ms-Exch-MSO-      rangeUpper                      20480
 Forward-Sync-
 Recipient-
 Cookie

 ms-Exch-          replace: searchFlags            19
 Mailbox-Audit-
 Enable

 ms-Exch-          rangeUpper                      38880
 Malware-
 Filtering-
 Update-
 Frequency

 ms-Exch-Role-     rangeUpper                      8192
 Entries

 ms-Exch-Schema-   rangeUpper                      15137
 Version-Pt

 ms-Exch-Schema-   rangeUpper                      15281
 Version-Pt

 ms-Exch-Smtp-     Replace: rangeUpper             1024
 Receive-Tls-
 Certificate-
 Name

 ms-Exch-Smtp-     replace: rangeUpper             1024
 TLS-Certificate

 ms-Exch-Sync-     rangeUpper                      262144
 Cookie

Object IDs added by Exchange 2016 RTM
The following class object IDs are added when you install Exchange 2016 RTM:

<!-- p.468 -->

     1.2.840.113556.1.5.7000.62.50161
     1.2.840.113556.1.5.7000.62.50162
     1.2.840.113556.1.5.7000.62.50163
     1.2.840.113556.1.5.7000.62.50164
     1.2.840.113556.1.5.7000.62.50165
     1.2.840.113556.1.5.7000.62.50166
     1.2.840.113556.1.5.7000.62.50167
     1.2.840.113556.1.5.7000.62.50170
     1.2.840.113556.1.5.7000.62.50171
     1.2.840.113556.1.5.7000.62.50172
     1.2.840.113556.1.5.7000.62.50173
     1.2.840.113556.1.5.7000.62.50174
     1.2.840.113556.1.5.7000.62.50176
     1.2.840.113556.1.5.7000.62.50177
     1.2.840.113556.1.5.7000.62.50178
     1.2.840.113556.1.5.7000.62.50187
     1.2.840.113556.1.5.7000.62.50188
     1.2.840.113556.1.5.7000.62.50189
     1.2.840.113556.1.5.7000.62.50190
     1.2.840.113556.1.5.7000.62.50191
     1.2.840.113556.1.5.7000.62.50192
     1.2.840.113556.1.5.7000.62.50202
     1.2.840.113556.1.5.7000.62.50203
     1.2.840.113556.1.5.7000.62.50204
     1.2.840.113556.1.5.7000.62.50205

The following attribute object IDs are added when you install Exchange 2016 RTM:

     1.2.840.113556.1.4.2183
     1.2.840.113556.1.4.2184
     1.2.840.113556.1.4.2185
     1.2.840.113556.1.4.7000.102.51773
     1.2.840.113556.1.4.7000.102.51774
     1.2.840.113556.1.4.7000.102.51775
     1.2.840.113556.1.4.7000.102.51786
     1.2.840.113556.1.4.7000.102.51787
     1.2.840.113556.1.4.7000.102.51788
     1.2.840.113556.1.4.7000.102.51789
     1.2.840.113556.1.4.7000.102.51790
     1.2.840.113556.1.4.7000.102.51791
     1.2.840.113556.1.4.7000.102.51792
     1.2.840.113556.1.4.7000.102.51794
     1.2.840.113556.1.4.7000.102.51795
     1.2.840.113556.1.4.7000.102.51796

<!-- p.469 -->

1.2.840.113556.1.4.7000.102.51797
1.2.840.113556.1.4.7000.102.51798
1.2.840.113556.1.4.7000.102.51799
1.2.840.113556.1.4.7000.102.51800
1.2.840.113556.1.4.7000.102.51801
1.2.840.113556.1.4.7000.102.51805
1.2.840.113556.1.4.7000.102.51806
1.2.840.113556.1.4.7000.102.51807
1.2.840.113556.1.4.7000.102.51808
1.2.840.113556.1.4.7000.102.51809
1.2.840.113556.1.4.7000.102.51810
1.2.840.113556.1.4.7000.102.51811
1.2.840.113556.1.4.7000.102.51812
1.2.840.113556.1.4.7000.102.51813
1.2.840.113556.1.4.7000.102.51814
1.2.840.113556.1.4.7000.102.51815
1.2.840.113556.1.4.7000.102.51816
1.2.840.113556.1.4.7000.102.51818
1.2.840.113556.1.4.7000.102.51819
1.2.840.113556.1.4.7000.102.51820
1.2.840.113556.1.4.7000.102.51821
1.2.840.113556.1.4.7000.102.51822
1.2.840.113556.1.4.7000.102.51823
1.2.840.113556.1.4.7000.102.51824
1.2.840.113556.1.4.7000.102.51826
1.2.840.113556.1.4.7000.102.51827
1.2.840.113556.1.4.7000.102.51829
1.2.840.113556.1.4.7000.102.51830
1.2.840.113556.1.4.7000.102.51832
1.2.840.113556.1.4.7000.102.51833
1.2.840.113556.1.4.7000.102.51836
1.2.840.113556.1.4.7000.102.51837
1.2.840.113556.1.4.7000.102.51838
1.2.840.113556.1.4.7000.102.51839
1.2.840.113556.1.4.7000.102.51840
1.2.840.113556.1.4.7000.102.51851
1.2.840.113556.1.4.7000.102.51852
1.2.840.113556.1.4.7000.102.51859
1.2.840.113556.1.4.7000.102.51860
1.2.840.113556.1.4.7000.102.51861
1.2.840.113556.1.4.7000.102.51862
1.2.840.113556.1.4.7000.102.51863
1.2.840.113556.1.4.7000.102.51864

<!-- p.470 -->

1.2.840.113556.1.4.7000.102.51865
1.2.840.113556.1.4.7000.102.51866
1.2.840.113556.1.4.7000.102.51867
1.2.840.113556.1.4.7000.102.51868
1.2.840.113556.1.4.7000.102.51869
1.2.840.113556.1.4.7000.102.51870
1.2.840.113556.1.4.7000.102.51871
1.2.840.113556.1.4.7000.102.51872
1.2.840.113556.1.4.7000.102.51873
1.2.840.113556.1.4.7000.102.51874
1.2.840.113556.1.4.7000.102.51875
1.2.840.113556.1.4.7000.102.51876
1.2.840.113556.1.4.7000.102.51877
1.2.840.113556.1.4.7000.102.51878
1.2.840.113556.1.4.7000.102.51879
1.2.840.113556.1.4.7000.102.51880
1.2.840.113556.1.4.7000.102.51881
1.2.840.113556.1.4.7000.102.51882
1.2.840.113556.1.4.7000.102.51883
1.2.840.113556.1.4.7000.102.51914
1.2.840.113556.1.4.7000.102.51915
1.2.840.113556.1.4.7000.102.51916
1.2.840.113556.1.4.7000.102.51917
1.2.840.113556.1.4.7000.102.51918
1.2.840.113556.1.4.7000.102.51919
1.2.840.113556.1.4.7000.102.51920
1.2.840.113556.1.4.7000.102.51921
1.2.840.113556.1.4.7000.102.51922
1.2.840.113556.1.4.7000.102.51923
1.2.840.113556.1.4.7000.102.51924
1.2.840.113556.1.4.7000.102.51925
1.2.840.113556.1.4.7000.102.51926
1.2.840.113556.1.4.7000.102.51927
1.2.840.113556.1.4.7000.102.51928
1.2.840.113556.1.4.7000.102.51929
1.2.840.113556.1.4.7000.102.51930
1.2.840.113556.1.4.7000.102.51931
1.2.840.113556.1.4.7000.102.51932
1.2.840.113556.1.4.7000.102.51933
1.2.840.113556.1.4.7000.102.51934
1.2.840.113556.1.4.7000.102.51935
1.2.840.113556.1.4.7000.102.51936
1.2.840.113556.1.4.7000.102.51937

<!-- p.471 -->

1.2.840.113556.1.4.7000.102.51938
1.2.840.113556.1.4.7000.102.51939
1.2.840.113556.1.4.7000.102.51940
1.2.840.113556.1.4.7000.102.51941
1.2.840.113556.1.4.7000.102.51942
1.2.840.113556.1.4.7000.102.51943
1.2.840.113556.1.4.7000.102.51944
1.2.840.113556.1.4.7000.102.51945
1.2.840.113556.1.4.7000.102.51946
1.2.840.113556.1.4.7000.102.51947
1.2.840.113556.1.4.7000.102.51948
1.2.840.113556.1.4.7000.102.51949
1.2.840.113556.1.4.7000.102.51950
1.2.840.113556.1.4.7000.102.51951
1.2.840.113556.1.4.7000.102.51952
1.2.840.113556.1.4.7000.102.51953
1.2.840.113556.1.4.7000.102.51954
1.2.840.113556.1.4.7000.102.51955
1.2.840.113556.1.4.7000.102.51993
1.2.840.113556.1.4.7000.102.51994
1.2.840.113556.1.4.7000.102.51995
1.2.840.113556.1.4.7000.102.51996
1.2.840.113556.1.4.7000.102.51997
1.2.840.113556.1.4.7000.102.51998
1.2.840.113556.1.4.7000.102.52001
1.2.840.113556.1.4.7000.102.52002
1.2.840.113556.1.4.7000.102.52003
1.2.840.113556.1.4.7000.102.52004
1.2.840.113556.1.4.7000.102.52005
1.2.840.113556.1.4.7000.102.52006
1.2.840.113556.1.4.7000.102.52007
1.2.840.113556.1.4.7000.102.52008
1.2.840.113556.1.4.7000.102.52011
1.2.840.113556.1.4.7000.102.52012
1.2.840.113556.1.4.7000.102.52013
1.2.840.113556.1.4.7000.102.52014
1.2.840.113556.1.4.7000.102.52015
1.2.840.113556.1.4.7000.102.52016
1.2.840.113556.1.4.7000.102.52017
1.2.840.113556.1.4.7000.102.52018
1.2.840.113556.1.4.7000.102.52019
1.2.840.113556.1.4.7000.102.52020
1.2.840.113556.1.4.7000.102.52021

<!-- p.472 -->

1.2.840.113556.1.4.7000.102.52022
1.2.840.113556.1.4.7000.102.52023
1.2.840.113556.1.4.7000.102.52024
1.2.840.113556.1.4.7000.102.52029
1.2.840.113556.1.4.7000.102.52030
1.2.840.113556.1.4.7000.102.52031
1.2.840.113556.1.4.7000.102.52032
1.2.840.113556.1.4.7000.102.52033
1.2.840.113556.1.4.7000.102.52034
1.2.840.113556.1.4.7000.102.52035
1.2.840.113556.1.4.7000.102.52036
1.2.840.113556.1.4.7000.102.52037
1.2.840.113556.1.4.7000.102.52039
1.2.840.113556.1.4.7000.102.52040
1.2.840.113556.1.4.7000.102.52041
1.2.840.113556.1.4.7000.102.52042
1.2.840.113556.1.4.7000.102.52043
1.2.840.113556.1.4.7000.102.52044
1.2.840.113556.1.4.7000.102.52045
1.2.840.113556.1.4.7000.102.52046
1.2.840.113556.1.4.7000.102.52047
1.2.840.113556.1.4.7000.102.52048
1.2.840.113556.1.4.7000.102.52049
1.2.840.113556.1.4.7000.102.52050
1.2.840.113556.1.4.7000.102.52051
1.2.840.113556.1.4.7000.102.52052
1.2.840.113556.1.4.7000.102.52053
1.2.840.113556.1.4.7000.102.52054
1.2.840.113556.1.4.7000.102.52055
1.2.840.113556.1.4.7000.102.52056
1.2.840.113556.1.4.7000.102.52057
1.2.840.113556.1.4.7000.102.52058
1.2.840.113556.1.4.7000.102.52059
1.2.840.113556.1.4.7000.102.52060
1.2.840.113556.1.4.7000.102.52061
1.2.840.113556.1.4.7000.102.52062
1.2.840.113556.1.4.7000.102.52063
1.2.840.113556.1.4.7000.102.52064
1.2.840.113556.1.4.7000.102.52065
1.2.840.113556.1.4.7000.102.52109
1.2.840.113556.1.4.7000.102.52110
1.2.840.113556.1.4.7000.102.52126
1.2.840.113556.1.4.7000.102.52127

<!-- p.473 -->

     1.2.840.113556.1.4.7000.102.52128
     1.2.840.113556.1.4.7000.102.52129
     1.2.840.113556.1.4.7000.102.52130

Indexed attributes added by Exchange 2016 RTM
The following table lists the attributes that are added to the list of indexed attributes when you install
Exchange 2016 RTM.

                                                                                        ﾉ   Expand table

 Attribute                                                                    Search flag value

 ms-DS-GeoCoordinates-Altitude                                                1

 ms-DS-GeoCoordinates-Latitude                                                1

 ms-DS-GeoCoordinates-Longitude                                               1

 ms-Exch-Accepted-Domain-Name                                                 9

 ms-Exch-Archive-GUID                                                         9

 ms-Exch-Auth-Application-Identifier                                          1

 ms-Exch-Auth-Issuer-Name                                                     1

 ms-Exch-Bypass-Audit                                                         9

 ms-Exch-Default-Public-Folder-Mailbox                                        19

 ms-Exch-Device-Client-Type                                                   1

 ms-Exch-Extension-Custom-Attribute-1                                         1

 ms-Exch-Extension-Custom-Attribute-2                                         1

 ms-Exch-Extension-Custom-Attribute-3                                         1

 ms-Exch-Extension-Custom-Attribute-4                                         1

 ms-Exch-Extension-Custom-Attribute-5                                         1

 ms-Exch-Home-MDB-SL                                                          1

 ms-Exch-Home-MTA-SL                                                          1

 ms-Exch-Is-Dirsync-Status-Pending                                            1

 ms-Exch-Mailbox-Audit-Enable                                                 19

 ms-Exch-Mailbox-Database-Transport-Flags                                     16

<!-- p.474 -->

Attribute                                          Search flag value

ms-Exch-Mailbox-Move-Source-Archive-MDB-Link-SL    1

ms-Exch-Mailbox-Move-Source-MDB-Link-SL            1

ms-Exch-Mailbox-Move-Target-Archive-MDB-Link-SL    1

ms-Exch-OWA-Set-Photo-URL                          16

ms-Exch-Organization-Upgrade-Policy-Link           1

ms-Exch-Organization-Upgrade-Policy-Link-SL        1

ms-Exch-Previous-Archive-Database-SL               8

ms-Exch-Previous-Home-MDB-SL                       8

ms-Exch-Provisioning-Tags                          1

ms-Exch-Public-Folder-EntryId                      24

ms-Exch-Public-Folder-Mailbox                      24

ms-Exch-Public-Folder-Smtp-Address                 24

ms-Exch-Recipient-SoftDeleted-Status               27

ms-Exch-Relocate-Tenant-Completion-Target-Vector   8

ms-Exch-Relocate-Tenant-Flags                      8

ms-Exch-Relocate-Tenant-Safe-Lockdown-Schedule     8

ms-Exch-Relocate-Tenant-Source-Forest              9

ms-Exch-Relocate-Tenant-Start-Lockdown             8

ms-Exch-Relocate-Tenant-Start-Retired              8

ms-Exch-Relocate-Tenant-Start-Sync                 8

ms-Exch-Relocate-Tenant-Status,                    9

ms-Exch-Relocate-Tenant-Target-Forest              9

ms-Exch-Relocate-Tenant-Transition-Counter         8

ms-Exch-Sync-Cookie                                8

ms-Exch-Team-Mailbox-Expiration                    16

ms-Exch-Team-Mailbox-Expiry-Days                   16

ms-Exch-Team-Mailbox-Owners                        16

<!-- p.475 -->

 Attribute                                                                   Search flag value

 ms-Exch-Team-Mailbox-SharePoint-Linked-By                                   16

 ms-Exch-Team-Mailbox-SharePoint-Url                                         16

 ms-Exch-Team-Mailbox-Show-In-Client-List                                    16

 ms-Exch-Transport-Rule-Immutable-Id                                         1

 ms-Exch-When-Soft-Deleted-Time                                              17

Property sets modified by Exchange 2016 RTM
The following property sets are modified when you install Exchange 2016 RTM:

     Exchange-Information

MAPI IDs added by Exchange 2016 RTM
The following MAPI IDs are added when you install Exchange 2016 RTM:

     36066
     36067

Extended rights added by Exchange 2016 RTM
The following table lists the extended rights that are added when you install Exchange 2016 RTM.
Installing Exchange 2016 RTM doesn't modify any existing extended rights.

                                                                                       ﾉ   Expand table

 Identifier                                                   Values

 CN=ms-Exch-SMTP-Accept-XProxyFrom,CN=Extended-Rights,        changetype: ntdsSchemaAdd
 <ConfigurationContainerDN>                                   displayName: Accept XProxyFrom
                                                              objectClass: controlAccessRight
                                                              rightsGuid: 5bee2b72-50d7-49c7-ba66-
                                                              39a25daa1e92
                                                              validAccesses: 256

<!-- p.476 -->

What changes in Active Directory when
Exchange is installed?
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

When you install Exchange Server 2016 or Exchange Server 2019, changes are made to your
Active Directory forest and domains to store information about the Exchange servers,
mailboxes, and other Exchange-related objects in your organization.

Three steps are required to prepare Active Directory for Exchange:

   1. Extend the Active Directory schema

   2. Prepare Active Directory containers, objects, and other items

   3. Prepare Active Directory domains

After all three steps are done, your Active Directory forest is ready for Exchange. This topic
explains what Exchange does at each step of Active Directory preparation.

You can make these changes before you install the first Exchange 2016 or Exchange 2019
server in the organization by running the /PrepareSchema, /PrepareAD, and
/PrepareAllDomains or /PrepareDomains commands using Exchange command line Setup. For
instructions, see Prepare Active Directory and domains for Exchange. Or, these changes are
automatically made for you during the installation of the first Exchange server using the
Exchange Setup wizard. For instructions, see Install Exchange Mailbox servers using the Setup
wizard.

Extend the Active Directory schema
Extending the Active Directory schema adds and updates classes, attributes, and other items.
These changes are needed so that Exchange can create containers and objects to store
information about the Exchange organization. Because Exchange makes a lot of changes to the
Active Directory schema, there's a topic dedicated to this step. To see all of the changes made
to the schema, see Active Directory schema changes in Exchange Server.

After the schema has been extended by running the /PrepareSchema command, the
_/PrepareAD command, or installing the first Exchange server using the Exchange Setup wizard,
the schema version is set in the ms-Exch-Schema-Version-Pt attribute. To verify that the Active
Directory schema was extended successfully, you can check the value stored in this attribute.
For more information, see Exchange Active Directory versions.

<!-- p.477 -->

Prepare Active Directory containers, objects, and
other items
With the schema extended, the next step is to add all of the containers, objects, attributes, and
other items that Exchange uses to store information in Active Directory. Most of the changes
made in this step are applied to the entire Active Directory forest. A smaller set of changes are
made only to the local Active Directory domain where the /PrepareAD command was run (or
where the first Exchange server was installed using the Exchange Setup wizard).

Exchange makes the following changes to the Active Directory forest:

     The Microsoft Exchange container is created under CN=Services,CN=Configuration,DC=
     <root domain> if it doesn't already exist.

     The following containers and objects are created under CN=<organization
     name>,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=<root domain> if
     they don't already exist:

        CN=Address Lists Container

        CN=AddressBook Mailbox Policies

        CN=Addressing

        CN=Administrative Groups

        CN=Approval Applications

        CN=Auth Configuration

        CN=Availability Configuration

        CN=Client Access

        CN=Connections

        CN=ELC Folders Container

        CN=ELC Mailbox Policies

        CN=ExchangeAssistance

        CN=Federation

        CN=Federation Trusts

        CN=Global Settings

<!-- p.478 -->

  CN=Hybrid Configuration

  CN=Mobile Mailbox Policies

  CN=Mobile Mailbox Settings

  CN=Monitoring Settings

  CN=OWA Mailbox Policies

  CN=Provisioning Policy Container

  CN=Push Notification Settings

  CN=RBAC

  CN=Recipient Policies

  CN=Remote Accounts Policies Container

  CN=Retention Policies Container

  CN=Retention Policy Tag Container

  CN=ServiceEndpoints

  CN=System Policies

  CN=Team Mailbox Provisioning Policies

  CN=Transport Settings

  CN=UM AutoAttendant Container (Exchange 2016 only)

  CN=UM DialPlan Container (Exchange 2016 only)

  CN=UM IPGateway Container (Exchange 2016 only)

  CN=UM Mailbox Policies (Exchange 2016 only)

  CN=Workload Management Settings

The following containers and objects are created under CN=Transport Settings,CN=
<Organization Name>,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=
<root domain> if they don't already exist:

  CN=Accepted Domains

  CN=ControlPoint Config

<!-- p.479 -->

  CN=DNS Customization

  CN=Interceptor Rules

  CN=Malware Filter

  CN=Message Classifications

  CN=Message Hygiene

  CN=Rules

  CN=MicrosoftExchange329e71ec88ae4615bbc36ab6ce41109e

Permissions are set throughout the configuration partition in Active Directory.

The Rights.ldf file is imported. This file adds permissions that are needed to install
Exchange and configure Active Directory.

The Microsoft Exchange Security Groups organizational unit (OU) is created in the root
domain of the forest, and permissions are assigned to it.

The following groups are created within the Microsoft Exchange Security Groups OU if
they don't already exist:

  Compliance Management

  Delegated Setup

  Discovery Management

  Exchange Servers

  Exchange Trusted Subsystem

  Exchange Windows Permissions

  ExchangeLegacyInterop

  Help Desk

  Hygiene Management

  Managed Availability Servers

  Organization Management

  Public Folder Management

<!-- p.480 -->

        Recipient Management

        Records Management

        Server Management

        View-Only Organization Management

     The new management role groups (which appear as universal security groups (USGs) in
     Active Directory) that were created in the Microsoft Exchange Security Groups OU are
     added to the otherWellKnownObjects attribute stored on the CN=Microsoft
     Exchange,CN=Services,CN=Configuration,DC=<root domain> container.

     In Exchange 2016 only, the Unified Messaging Voice Originator contact is created in the
     Microsoft Exchange System Objects container of the root domain.

     Only the domain where the /PrepareAD command was run (or where the first Exchange
     server was installed using the Exchange Setup wizard) is prepared for Exchange. For
     information about what's done to prepare an Active Directory domain for Exchange, see
     the next section.

Prepare Active Directory domains
The final step of preparing Active Directory for Exchange is to prepare the Active Directory
domains where Exchange servers will be installed or where mailbox-enabled users will be
located (all domains in the forest using the /PrepareAllDomains command, specific domains
using the /PrepareDomains command, or installing the first Exhange server using the Exchange
Setup Wizard). This step is done automatically in the domain where the PrepareAD command
was run (or where the first Exchange server was installed using the Exchange Setup wizard).

Exchange makes the follwing changes to the Active Directory domains:

     The Microsoft Exchange System Objects container is created in the root domain partition
     in Active Directory if it doesn't already exist.

     Permissions are set on the Microsoft Exchange System Objects container for the Exchange
     Servers, Organization Management, and Authenticated Users security groups.

     Modifying the Default Domain Controllers GPO to grant "Manage Auditing and Security
     Log policy" rights to Exchange Enterprise Servers.

     The Exchange Install Domain Servers domain global group is created in the current
     domain and placed in the Microsoft Exchange System Objects container.
