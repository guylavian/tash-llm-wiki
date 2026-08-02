---
title: "Protect data and infrastructure documentation — pages 281-295"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0281-0295
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0281-0295
family: sccm
documentKind: "doc"
abstract: "Client event logs Article • 01/12/2024 Applies to: Configuration Manager (current branch) On a Configuration Manager client to which you deploy a BitLocker management policy, use the Windows Event Viewer to view BitLocker client event logs. Go to Applications and Services Logs,"
---

# Protect data and infrastructure documentation — pages 281-295

<!-- p.281 -->

Client event logs
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

On a Configuration Manager client to which you deploy a BitLocker management policy,
use the Windows Event Viewer to view BitLocker client event logs. Go to Applications
and Services Logs, Microsoft, Windows, MBAM for both Admin and Operational event
logs.

Admin

2: VolumeEnactmentFailed
An error occurred while applying MBAM policies.

Error code: -2144272219
Details: BitLocker Drive Encryption only supports Used Space Only encryption on thin
provisioned storage.

This error occurs if you try to use BitLocker to encrypt a virtual machine that's running
Windows 10 version 1803 or earlier. Earlier versions of Windows 10 don't support full
disk encryption. BitLocker management policies enforce full disk encryption.

Error code: -2147024774

Details: The data area passed to a system call is too small.

To resolve this issue, restart the computer.

4: TransferStatusDataFailed
An error occurred while sending encryption status data.

8: SystemVolumeNotFound
The system volume is missing. SystemVolume is needed to encrypt the operating system
drive.

<!-- p.282 -->

9: TPMNotFound
The TPM hardware is missing. TPM is needed to encrypt the operating system drive with
any TPM protector.

10: MachineHWExempted
The computer is exempted from Encryption. Machine's hardware status: Exempted

11: MachineHWUnknown
The computer is exempted from encryption. Machine's hardware status: Unknown

12: HWCheckFailed
Hardware exemption check failed.

13: UserIsExempted
The user is exempt from encryption.

14: UserIsWaiting
The user requested an exemption.

15: UserExemptionCheckFailed
User exemption check failed.

16: UserPostponed
The user postponed the encryption process.

17: TPMInitializationFailed
TPM initialization failed. The user rejected the BIOS changes.

18: CoreServiceDown
Unable to connect to the MBAM Recovery and Hardware service.

<!-- p.283 -->

Error code: -2147024809
Details: The parameter is incorrect.

This error occurs if the website isn't HTTPS, or the client doesn't have a PKI cert.

20: PolicyMismatch
The BitLocker management policy is in conflict or corrupt.

21: ConflictingOSVolumePolicies
Detected OS volume encryption policies conflict. Check BitLocker policies related to OS
drive protectors.

22: ConflictingFDDVolumePolicies
Detected fixed data drive volume encryption policies conflict. Check BitLocker policies
related to fixed data drive protectors.

27: EncryptionFailedNoDra
An error occurred while encrypting. A data recovery agent (DRA) protector is required in
FIPS mode for pre-Windows 8.1 machines.

34: TpmLockOutResetFailed
Failed to reset TPM lockout.

36: TpmOwnerAuthRetrievalFailed
Failed to retrieve TPM OwnerAuth from MBAM services.

37: WmiProviderDllSearchPathUpdateFailed
Failed to update the DLL search path for WMI provider.

38: TimedOutWaitingForWmiProvider
Agent stopping. Timed-out waiting for MBAM WMI provider instance.

<!-- p.284 -->

Operational

1: VolumeEnactmentSuccessful
The BitLocker management policies were applied successfully.

3: TransferStatusDataSuccessful
The encryption status data was sent successfully.

19: CoreServiceUp
Successfully connected to the MBAM Recovery and Hardware service.

28: TpmOwnerAuthEscrowed
The TPM OwnerAuth is escrowed.

29: RecoveryKeyEscrowed
The BitLocker recovery key for the volume is escrowed.

30: RecoveryKeyReset
The BitLocker recovery key for the volume is updated.

31: EnforcePolicyDateSet
The enforce policy date...is set for the volume

32: EnforcePolicyDateCleared
The enforce policy date...has been cleared for the volume.

33: TpmLockOutResetSucceeded
Successfully reset TPM lockout.

35: TpmOwnerAuthRetrievalSucceeded

<!-- p.285 -->

Successfully retrieved TPM OwnerAuth from MBAM services.

39: RemovableDriveMounted
Removable drive was mounted.

40: RemovableDriveDismounted
Removable drive was unmounted.

41: FailedToEnactEndpointUnreachable
Failure to connect to the MBAM Recovery and Hardware service prevented BitLocker
management policies from being applied successfully to the volume.

42: FailedToEnactLockedVolume
Locked volume state prevented BitLocker management policies from being applied
successfully to the volume.

43: TransferStatusDataFailedEndpointUnreachable
Failure to connect to the MBAM Compliance and Status service prevented the transfer of
encryption status data.

See also
For more information on using these logs, see BitLocker event logs.

For more troubleshooting information, see Troubleshoot BitLocker.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.286 -->

Server event logs
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the Windows Event Viewer to view event logs for the following BitLocker
management server components in Configuration Manager:

      Recovery service on the management point
      Self-service portal
      Administration and monitoring website

On a server hosting one or more of these components, open the Event Viewer. Then go
to Applications and Services Logs, Microsoft, Windows, and expand MBAM-Web. By
default, there are Admin and Operational event logs.

The following sections contain messages and troubleshooting information for event IDs
that can occur with the BitLocker management server components.

Admin

1: WebAppSpnError
Application: {SiteName}{VirtualDirectory} is missing the following Service Principal
Names (SPNs):{ListOfSpns} Register the required SPNs on the account:
{ExecutionAccount}.

For integrated Windows Authentication to succeed, necessary SPNs need to be in place.
This message indicates that the SPN required for the application isn't correctly
configured. Details contained in this event should provide more information.

100: AdminServiceRecoveryDbError
Possible error messages:

      GetMachineUsers: An error occurred while getting user information from the
      database.
      GetRecoveryKey: an error occurred while getting recovery key from the database.
      GetRecoveryKey: an error occurred while getting user information from the
      database.

<!-- p.287 -->

     GetRecoveryKeyIds: an error occurred while getting recovery key Ids from the
     database.
     GetTpmHashForUser: An error occurred while getting TPM hash data from the
     recovery database.
     GetTpmHashForUser: An error occurred while getting TPM hash data from the
     recovery database.
     QueryDriveRecoveryData: An error occurred while getting drive recovery data from
     the database.
     QueryRecoveryKeyIdsForUser: An error occurred while getting recovery key Ids
     from the database.
     QueryVolumeUsers: An error occurred while getting user information from the
     database.

This message is logged whenever there's an exception while communicating with the
recovery database. Read through the information contained in the trace to get specific
details about the exception.

101: AdminServiceComplianceDbError
Possible error messages:

     GetRecoveryKey: An error occurred while logging an audit event to the compliance
     database.
     GetRecoveryKeyIds: An error occurred while logging an audit event to the
     compliance database.
     GetTpmHashForUser: An error occurred while logging an audit event to the
     compliance database.
     QueryRecoveryKeyIdsForUser: An error occurred while logging an audit event to
     the compliance database.
     QueryDriveRecoveryData: An error occurred while logging an audit event to the
     compliance database.

This message is logged whenever there's an exception while communicating with the
compliance database. Read through the information contained in the trace to get
specific details about the exception.

102: AgentServiceRecoveryDbError
This message indicates an exception when the service tries to communicate with the
recovery database. Read through the message contained in the event to get specific
information about the exception.

<!-- p.288 -->

Verify that the MBAM app pool account has required permissions to connect to the
recovery database.

103: AgentServiceError
Possible error messages:

     Unable to detect client machine account or data migration user account.

     Whenever a call is made to the PostKeyRecoveryInfo , IsRecoveryKeyResetRequired ,
     CommitRecoveryKeyRest , or GetTpmHash web methods, it retrieves the caller context
     to obtain caller credentials. If the caller context is null or empty, the service logs
     this message.

     Account verification failed for caller identity.

     This message is logged if the web method is expecting the caller to be a computer
     account and it's not. It can also be caused if the web method is expecting the caller
     to be a user account, and it's not a user account or a member of a data migration
     group account.

104: StatusServiceComplianceDbConfigError
The compliance database connection string in the registry is empty.

This message is logged whenever the compliance db connection string is invalid. Verify
the value at the registry key HKLM\Software\Microsoft\MBAM
Server\Web\ComplianceDBConnectionString .

105: StatusServiceComplianceDbError
This error indicates that the websites or web services were unable to connect to the
compliance database. Verify that the IIS app pool account can connect to the database.

106: HelpdeskError
Known errors and possible causes:

     The request to URL caused an internal error.

     An unhandled exception was raised in the application for the administration and
     monitoring website (helpdesk). Review the log entries in the Admin event log to
     find the specific exception.

<!-- p.289 -->

     An error occurred while obtaining execution context information. Unable to verify
     Service Principal Name (SPN) registration.

     During the initial helpdesk website load operation, it checks the SPN. To verify the
     SPN, it requires account information, IIS Sitename, and ApplicationVirtualPath
     corresponding to the helpdesk website. It logs this error message when one or
     more of these attributes are invalid or missing.

     An error occurred while verifying Service Principal Name (SPN) registration.

     This message indicates that a security exception is thrown when verifying the SPN.
     Refer to the exception contained in the event details.

107: SelfServicePortalError
Known errors and possible causes:

     An error occurred while getting recovery key for a user

     Indicates that an unexpected exception was thrown when a request was made to
     retrieve a recovery key. Refer to the exception message in the event details. If
     tracing is enabled on the helpdesk app, refer to trace data to obtain detailed
     exception messages.

     An error occurred while obtaining execution context information. Unable to verify
     Service Principal Name (SPN) registration

     During an initial load operation, the self-service portal retrieves account
     information, IIS Sitename, and ApplicationVirtualPath for the self-service website to
     verify the SPN. This error message is logged when one or more of these attributes
     are invalid.

     An error occurred while verifying Service Principal Name (SPN) registration.
     EventDetails:{ExceptionMessage}

     This message indicates that a security exception was thrown while verifying the
     SPN. Refer to the exception contained in the event details.

108: DomainControllerError
Known errors and possible causes:

     An error occurred while resolving domain name {DomainName}, a memory
     allocation failure occurred.

<!-- p.290 -->

     To resolve domain name, it calls the DsGetDcName Windows API. This message is
     logged when this API returns ERROR_NOT_ENOUGH_MEMORY , which indicates a memory
     allocation failure.

     Could not invoke DsGetDcName method

     This message indicates that the DsGetDcName API is unavailable on the host.

109: WebAppRecoveryDbError
Known errors and possible causes:

     An error occurred while reading the configuration of the Recovery database. The
     connection string to the Recovery database is not configured.

     This message indicates that recovery database connection string information at
     HKLM\Software\Microsoft\MBAM Server\Web\RecoveryDBConnectionString is invalid.

     Verify the given registry key value.

If you see any of the following messages, verify whether the app pool credentials from
the IIS server can make a connection to the recovery database:

     DoesUserHaveMatchingRecoveryKey: an error occurred while getting recovery key
     Ids for a user.
     QueryDriveRecoveryData: an error occurred while getting drive recovery data.
     QueryRecoveryKeyIdsForUser: an error occurred while getting recovery key Ids for
     a user.
     An error occurred while getting TPM password hash from the Recovery database.

110: WebAppComplianceDbError
Known errors and possible causes:

     An error occurred while reading the configuration of the Compliance database. The
     connection string to the Compliance database is not configured.

     This message indicates that compliance database connection string information at
     HKLM\Software\Microsoft\MBAM Server\Web\ComplianceDBConnectionString is invalid.

     Verify the value of this registry key.

If you see any of the following messages, verify whether the app pool credentials from
the IIS server can make a connection to the compliance database:

<!-- p.291 -->

     GetRecoveryKeyForCurrentUser: an error occurred while logging an audit event to
     the Compliance database.
     QueryRecoveryKeyIdsForUser: an error occurred while logging an audit event to
     the Compliance database.
     QueryRecoveryKeyIdsForUser: an error occurred while logging an audit event to
     the compliance database.

111: WebAppDbError
These errors indicate one of the following two conditions

     MBAM websites/webservices were unable to either connect to compliance or
     recovery database
     MBAM websites/webservices execution account (app pool account) could not run
     the GetVersion stored procedure on compliance or recovery database

The message contained in the event provides more details about the exception.

Verify that the app pool account can connect to the compliance or recovery databases.
Confirm that it has permissions to run the GetVersion stored procedure.

112: WebAppError
An error occurred while verifying Service Principal Name (SPN) registration.

To verify the SPN, it queries Active Directory to retrieve a list of SPNs mapped execution
account. It also queries the ApplicationHost.config to get the website bindings. This
error message indicates that it couldn't communicate with Active Directory, or it couldn't
load the ApplicationHost.config file.

Verify that the app pool account has permissions to query Active Directory or the
ApplicationHost.config file. Also verify the site binding entries in the

ApplicationHost.config file.

Operational

4: PerformanceCounterError
An error occurred while retrieving a performance counter.

<!-- p.292 -->

The trace message contains the actual exception message, some of which are listed
here:

        ArgumentNullException: This exception is thrown if the category, counter, or
        instance of requested Performance counter is invalid.
        System.InvalidOperationException: categoryName is an empty string ("").
        counterName is an empty string("").
        The read/write permission setting requested is invalid for this counter.
        The category specified does not exist (if readOnly is true).
        The category specified is not a .NET Framework custom category (if readOnly is
        false).
        The category specified is marked as multi-instance and requires the performance
        counter to be created with an instance name.
        instanceName is longer than 127 characters.
        categoryName and counterName have been localized into different languages.
        System.ComponentModel.Win32Exception: An error occurred when accessing a
        system API.
        System.UnauthorizedAccessException: Code that is executing without
        administrative privileges attempted to read a performance counter.

The message in the event provides more details on the exception.

For the System.UnauthorizedAccessException , verify that the app pool account has
access to performance counter APIs.

200: HelpDeskInformation
The administration website application successfully found and connected to a supported
version of the recovery/compliance database.

Indicates successful connection to the recovery or compliance database from the
helpdesk website.

201: SelfServicePortalInformation
The self-service portal application successfully found and connected to a supported
version of the recovery/compliance database.

Indicates successful connection to the recovery or compliance database from the self-
service portal.

202: WebAppInformation

<!-- p.293 -->

Application has its SPNs registered correctly.

Indicates that the SPNs required for the helpdesk website are correctly registered
against the executing account.

See also
For more information on using these logs, see BitLocker event logs.

For more troubleshooting information, see Troubleshoot BitLocker.

For more information on installing these websites, see Set up BitLocker reports and
portals.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.294 -->

Non-compliance codes
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

WMI on the client provides the following non-compliance codes. It also describes the
reasons why a particular device reports as non-compliant.

There are various methods to view WMI. For example, use the following PowerShell
command:

     PowerShell

     (Get-WmiObject -Class mbam_Volume -Namespace
     root\microsoft\mbam).ReasonsForNoncompliance

      Tip

     If the device is compliant, this command doesn't return anything.

     You can also check the Compliant attribute of this class, which is 1 if the device is
     compliant.

                                                                                    ﾉ    Expand table

 Non-compliance          Reason for non-compliance
 code

 0                       Cipher strength not AES 256.

 1                       BitLocker policy requires this volume to be encrypted, but it isn't.

 2                       BitLocker policy requires this volume to not be encrypted, but it is.

 3                       BitLocker policy requires this volume use a TPM protector, but it doesn't.

 4                       BitLocker policy requires this volume use a TPM+PIN protector, but it
                         doesn't.

 5                       BitLocker policy doesn't allow non-TPM machines to report as compliant.

 6                       Volume has a TPM protector, but the TPM isn't visible.

 7                       BitLocker policy requires this volume use a password protector, but it
                         doesn't have one.

<!-- p.295 -->

 Non-compliance          Reason for non-compliance
 code

 8                       BitLocker policy requires this volume not use a password protector, but it
                         has one.

 9                       BitLocker policy requires this volume use an auto-unlock protector, but it
                         doesn't have one.

 10                      BitLocker policy requires this volume not use an auto-unlock protector, but
                         it has one.

 11                      BitLocker detects a policy conflict, which prevents it from reporting this
                         volume as compliant.

 12                      A system volume is needed to encrypt the OS volume, but it isn't present.

 13                      Protection is suspended for the volume.

 14                      Auto-unlock protector is unsafe unless the OS volume is encrypted.

 15                      Policy requires minimum cypher strength is XTS-AES-128 bit, actual cypher
                         strength is weaker.

 16                      Policy requires minimum cypher strength is XTS-AES-256 bit, actual cypher
                         strength is weaker.

Feedback
Was this page helpful?      Yes       No

Provide product feedback
