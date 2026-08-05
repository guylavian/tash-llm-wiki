---
title: "Unable to bind or log into LDAP using specific credentials"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149890/unable-to-bind-or-log-into-ldap-using-specific-cre
question_id: 149890
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to bind or log into LDAP using specific credentials

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149890/unable-to-bind-or-log-into-ldap-using-specific-cre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So this is happening with very specific user accounts. Most user accounts have no problems, but a handful are failing. Using LDP to bind, i'm getting this error:  

```
0 = ldap_set_option(ld, LDAP_OPT_ENCRYPT, 1)
res = ldap_bind_s(ld, NULL, &NtAuthIdentity, NEGOTIATE (1158)); // v.3
{NtAuthIdentity: User='firstname.lastname'; Pwd=; domain = 'domainname.local'}
Error : ldap_bind_s() failed: Invalid Credentials.
Server error: 8009030C: LdapErr: DSID-0C090588, comment: AcceptSecurityContext error, data 569, v2580
Error 0x8009030C The logon attempt failed
```

I am absolutely certain that the credentials are correct, because this is happening with my domain account. I can log into my Windows systems with no problems, including the DCs. But logging into LDAP, it fails.  

I believe this is the important detail of the error:  

```
Server error: 8009030C: LdapErr: DSID-0C090588, comment: AcceptSecurityContext error, data 569, v2580
```

This lists the errors https://ldapwiki.com/wiki/Common%20Active%20Directory%20Bind%20Errors  

But there isn't an entry for 569...  

This actually first occurred this afternoon with the built-in domain Administrator account. Our VPN services were failing because the LDAP bind utilized the built-in domain Administrator account. After spending an hour attempting to resolve it without success, i simply created an ldap user account to use with LDAP. Now a few hours later, the same issue is happening with my own domain account. What is happening here?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 2 · updated: 2020-11-04*

Hello @Nick@519  ，

Thank you for posting here.

From the description, I understand we can not bind LDAP. We can check as below:

1.If you can bind LDAP on other DC except this one, we can check if AD replication works fine.  

2.If the time is not synchronized, authentication problems may also occur.  

3.Whether you are perform bind operation on DC or client? If your domain credential is correct, we can check whether the hardware keyboard buttons are normal, type the credential on one txt file to check.  

4.Also do you provide the credential with UPN (usernam@keyman  .com) or domain\username, we can use the two one by one to see if it helps.  

5.If it is NTLM authentication method, the NTLM version may also have impact.

For more information above NTLM version, we can refer to the link below.  

Network security: LAN Manager authentication level  

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level

If all above does not work. Please confirm the following information:  

1.Whether your domain is a single forest with one domain or multiple domains?  

2.Do you have multiple DCs in this domain? If you have multiple DCs in this domain, can you bind LDAP on other DCs?  

3.Please check whether AD replication is working fine. Run repadmin /showrepl and repadmin /showrepl * /csv >showrepl.csv on PDC in this domain. If there is no error from the command result, then AD replication works fine.  

4.What LDAP tool are you using?  

5.If we use Windows built-in ldp.exe tool, how we bind LDAP (method 1 or method 2 or others)？  

Method 1  

Method 2  

Hope the information above is helpful. If anything is unclear, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-06*

I was able to resolve this.  

In Local Group Policy Editor > Local Computer Policy > Computer Configuration > Windows Settings > Security Settings > Local Policies > Users Rights Assignments > Deny access to this computer from the network  

Administrators was listed there.  

Now i need to find out how or who did this. I have auditing enabled in Event Viewer, is there a way to see who exactly made the change?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-06*

This is the current gpresult /z results, is there anything that could be causing it:

```
Microsoft (R) Windows (R) Operating System Group Policy Result tool v2.0
© 2013 Microsoft Corporation. All rights reserved.

Created on 11/5/2020 at 7:37:45 PM

RSOP data for DOMAIN\firstname.lastname on DC1 : Logging Mode
-------------------------------------------------------

OS Configuration:            Primary Domain Controller
OS Version:                  6.3.9600
Site Name:                   City
Roaming Profile:             N/A
Local Profile:               C:\Users\firstname.lastname
Connected over a slow link?: No

COMPUTER SETTINGS
------------------
    CN=DC1,OU=Domain Controllers,DC=domain,DC=local
    Last time Group Policy was applied: 11/5/2020 at 7:33:05 PM
    Group Policy was applied from:      DC1.domain.local
    Group Policy slow link threshold:   500 kbps
    Domain Name:                        DOMAIN
    Domain Type:                        Windows 2008 or later

    Applied Group Policy Objects
    -----------------------------
        Default Domain Controllers Policy
        Default Domain Policy
        ADAuditPlusMSPolicy
        Manage Engine

    The following GPOs were not applied because they were filtered out
    -------------------------------------------------------------------
        ADAuditPlusPolicy
            Filtering:  Denied (Security)

        Allow Remote Management
            Filtering:  Denied (Security)

        Local Group Policy
            Filtering:  Not Applied (Empty)

    The computer is a part of the following security groups
    -------------------------------------------------------
        BUILTIN\Administrators
        Everyone
        BUILTIN\Pre-Windows 2000 Compatible Access
        BUILTIN\Users
        Windows Authorization Access Group
        NT AUTHORITY\NETWORK
        NT AUTHORITY\Authenticated Users
        This Organization
        DC1$
        Domain Controllers
        DnsUpdateProxy
        NT AUTHORITY\ENTERPRISE DOMAIN CONTROLLERS
        Authentication authority asserted identity
        Denied RODC Password Replication Group
        RAS and IAS Servers
        ADAuditPlusMS
        System Mandatory Level

    Resultant Set Of Policies for Computer
    ---------------------------------------

        Software Installations
        ----------------------
            N/A

        Startup Scripts
        ---------------
            N/A

        Shutdown Scripts
        ----------------
            N/A

        Account Policies
        ----------------
            GPO: Default Domain Policy
                Policy:            MaxRenewAge
                Computer Setting:  7

            GPO: Default Domain Policy
                Policy:            LockoutDuration
                Computer Setting:  15

            GPO: Default Domain Policy
                Policy:            MaximumPasswordAge
                Computer Setting:  365

            GPO: Default Domain Policy
                Policy:            MinimumPasswordAge
                Computer Setting:  N/A

            GPO: Default Domain Policy
                Policy:            ResetLockoutCount
                Computer Setting:  15

            GPO: Default Domain Policy
                Policy:            MaxServiceAge
                Computer Setting:  600

            GPO: Default Domain Policy
                Policy:            LockoutBadCount
                Computer Setting:  10

            GPO: Default Domain Policy
                Policy:            MaxClockSkew
                Computer Setting:  5

            GPO: Default Domain Policy
                Policy:            MaxTicketAge
                Computer Setting:  10

            GPO: Default Domain Policy
                Policy:            PasswordHistorySize
                Computer Setting:  5

            GPO: Default Domain Policy
                Policy:            MinimumPasswordLength
                Computer Setting:  10

        Audit Policy
        ------------
            GPO: Default Domain Controllers Policy
                Policy:            AuditPolicyChange
                Computer Setting:  Success

            GPO: Default Domain Controllers Policy
                Policy:            AuditAccountManage
                Computer Setting:  Success, Failure

            GPO: Default Domain Controllers Policy
                Policy:            AuditObjectAccess
                Computer Setting:  Success

            GPO: Default Domain Controllers Policy
                Policy:            AuditDSAccess
                Computer Setting:  Success

            GPO: Default Domain Controllers Policy
                Policy:            AuditPrivilegeUse
                Computer Setting:  No Auditing

            GPO: Default Domain Controllers Policy
                Policy:            AuditProcessTracking
                Computer Setting:  Success

            GPO: Default Domain Controllers Policy
                Policy:            AuditAccountLogon
                Computer Setting:  Success, Failure

            GPO: Default Domain Controllers Policy
                Policy:            AuditLogonEvents
                Computer Setting:  Success, Failure

            GPO: Default Domain Controllers Policy
                Policy:            AuditSystemEvents
                Computer Setting:  Success

        User Rights
        -----------
            GPO: Default Domain Controllers Policy
                Policy:            SyncAgentPrivilege
                Computer Setting:  N/A

            GPO: Default Domain Controllers Policy
                Policy:            MachineAccountPrivilege
                Computer Setting:  Authenticated Users

            GPO: Default Domain Controllers Policy
                Policy:            ChangeNotifyPrivilege
                Computer Setting:  *S-1-5-80-1670033946-1058562292-2418231921-1479535664-4274663199
                                   Pre-Windows 2000 Compatible Access
                                   Authenticated Users
                                   Administrators
                                   Everyone
                                   DOMAIN\QBDataServiceUser19
                                   *S-1-5-80-797827364-3451187129-808634983-2979512460-2324440249

            GPO: Default Domain Controllers Policy
                Policy:            IncreaseBasePriorityPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            CreateTokenPrivilege
                Computer Setting:  N/A

            GPO: Manage Engine
                Policy:            SecurityPrivilege
                Computer Setting:  DOMAIN\manage.engine

            GPO: Default Domain Controllers Policy
                Policy:            TakeOwnershipPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            DenyInteractiveLogonRight
                Computer Setting:  DOMAIN\QBDataServiceUser19

            GPO: Default Domain Controllers Policy
                Policy:            RestorePrivilege
                Computer Setting:  Server Operators
                                   Backup Operators
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            DebugPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            SystemTimePrivilege
                Computer Setting:  Server Operators
                                   Administrators
                                   LOCAL SERVICE

            GPO: Default Domain Controllers Policy
                Policy:            SecurityPrivilege
                Computer Setting:  DOMAIN\Exchange Servers
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            ShutdownPrivilege
                Computer Setting:  Print Operators
                                   Server Operators
                                   Backup Operators
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            AuditPrivilege
                Computer Setting:  NETWORK SERVICE
                                   LOCAL SERVICE
                                   IIS APPPOOL\DefaultAppPool

            GPO: Default Domain Controllers Policy
                Policy:            InteractiveLogonRight
                Computer Setting:  Print Operators
                                   Server Operators
                                   Account Operators
                                   Backup Operators
                                   Administrators
                                   DOMAIN\IUSR_EXCH

            GPO: Default Domain Controllers Policy
                Policy:            CreatePagefilePrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            BatchLogonRight
                Computer Setting:  IIS_IUSRS
                                   DOMAIN\Administrator
                                   DOMAIN\IIS_WPG
                                   DOMAIN\IUSR_EXCH
                                   DOMAIN\IWAM_EXCH
                                   LOCAL SERVICE

            GPO: Default Domain Controllers Policy
                Policy:            LockMemoryPrivilege
                Computer Setting:  N/A

            GPO: Default Domain Controllers Policy
                Policy:            NetworkLogonRight
                Computer Setting:  DOMAIN\IWAM_EXCH
                                   Pre-Windows 2000 Compatible Access
                                   ENTERPRISE DOMAIN CONTROLLERS
                                   Authenticated Users
                                   Administrators
                                   Everyone
                                   DOMAIN\IUSR_EXCH
                                   DOMAIN\QBDataServiceUser19

            GPO: Default Domain Controllers Policy
                Policy:            CreatePermanentPrivilege
                Computer Setting:  N/A

            GPO: Default Domain Controllers Policy
                Policy:            SystemProfilePrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            TcbPrivilege
                Computer Setting:  N/A

            GPO: Default Domain Controllers Policy
                Policy:            ServiceLogonRight
                Computer Setting:  DOMAIN\backup.service
                                   *S-1-5-80-2567096502-4068731684-1555260761-2520130083-3392037366
                                   *S-1-5-80-1670033946-1058562292-2418231921-1479535664-4274663199
                                   DOMAIN\SQLServer2005SQLBrowserUser$DC2
                                   DOMAIN\firstname.lastname
                                   NETWORK SERVICE
                                   DOMAIN\QBDataServiceUser19
                                   IIS APPPOOL\DefaultAppPool
                                   SYSTEM
                                   *S-1-5-80-797827364-3451187129-808634983-2979512460-2324440249
                                   DOMAIN\Administrator
                                   DOMAIN\SQLServer2005SQLBrowserUser$DC3

            GPO: Default Domain Controllers Policy
                Policy:            RemoteShutdownPrivilege
                Computer Setting:  Server Operators
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            BackupPrivilege
                Computer Setting:  Server Operators
                                   Backup Operators
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            EnableDelegationPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            UndockPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            SystemEnvironmentPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            DenyServiceLogonRight
                Computer Setting:  N/A

            GPO: Default Domain Controllers Policy
                Policy:            LoadDriverPrivilege
                Computer Setting:  Print Operators
                                   Administrators

            GPO: Default Domain Controllers Policy
                Policy:            IncreaseQuotaPrivilege
                Computer Setting:  *S-1-5-80-1670033946-1058562292-2418231921-1479535664-4274663199
                                   Administrators
                                   NETWORK SERVICE
                                   LOCAL SERVICE
                                   DOMAIN\IWAM_EXCH
                                   IIS APPPOOL\DefaultAppPool
                                   *S-1-5-80-797827364-3451187129-808634983-2979512460-2324440249

            GPO: Default Domain Controllers Policy
                Policy:            ProfileSingleProcessPrivilege
                Computer Setting:  Administrators

            GPO: Default Domain Controllers Policy
                Policy:            AssignPrimaryTokenPrivilege
                Computer Setting:  *S-1-5-80-1670033946-1058562292-2418231921-1479535664-4274663199
                                   NETWORK SERVICE
                                   LOCAL SERVICE
                                   DOMAIN\IWAM_EXCH
                                   IIS APPPOOL\DefaultAppPool
                                   *S-1-5-80-797827364-3451187129-808634983-2979512460-2324440249

        Security Options
        ----------------
            GPO: Default Domain Policy
                Policy:            PasswordComplexity
                Computer Setting:  Enabled

            GPO: Default Domain Policy
                Policy:            ClearTextPassword
                Computer Setting:  Not Enabled

            GPO: Default Domain Policy
                Policy:            ForceLogoffWhenHourExpire
                Computer Setting:  Not Enabled

            GPO: Default Domain Policy
                Policy:            RequireLogonToChangePassword
                Computer Setting:  Not Enabled

            GPO: Default Domain Policy
                Policy:            TicketValidateClient
                Computer Setting:  Enabled

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59059
                ValueName:         MACHINE\System\CurrentControlSet\Control\Lsa\LmCompatibilityLevel
                Computer Setting:  2

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59013
                ValueName:         MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LDAPServerIntegrity
                Computer Setting:  1

            GPO: ADAuditPlusMSPolicy
                Policy:            @wsecedit.dll,-59104
                ValueName:         MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy
                Computer Setting:  1

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59043
                ValueName:         MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature
                Computer Setting:  1

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59044
                ValueName:         MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableSecuritySignature
                Computer Setting:  1

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59104
                ValueName:         MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy
                Computer Setting:  1

            GPO: Default Domain Controllers Policy
                Policy:            @wsecedit.dll,-59018
                ValueName:         MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal
                Computer Setting:  1

            N/A

        Event Log Settings
        ------------------
            N/A

        Restricted Groups
        -----------------
            N/A

        System Services
        ---------------
            N/A

        Registry Settings
        -----------------
            N/A

        File System Settings
        --------------------
            N/A

        Public Key Policies
        -------------------
            N/A

        Administrative Templates
        ------------------------
            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\WindowsUpdate\AU\ScheduledInstallTime
                Value:       5, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Policy
                Folder Id: Software\Policies\Microsoft\Windows NT\Terminal Services\RAUnsolicit\domain\firstname.lastname
                Value:       100, 0, 101, 0, 106, 0, 101, 0, 114, 0, 111, 0, 92, 0, 110, 0, 105, 0, 99, 0, 107, 0, 46, 0, 110, 0, 103, 0, 104, 0, 105, 0, 101, 0, 109, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\WindowsUpdate\AU\AutomaticMaintenanceEnabled
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Policy
                Folder Id: Software\Policies\Microsoft\Windows NT\Terminal Services\fAllowUnsolicitedFullControl
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\WindowsUpdate\AU\NoAutoUpdate
                Value:       0, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\WindowsUpdate\AU\ScheduledInstallDay
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\WindowsUpdate\AU\AUOptions
                Value:       4, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Policy
                Folder Id: Software\Policies\Microsoft\Windows NT\Terminal Services\fAllowUnsolicited
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Default Domain Controllers Policy
                Folder Id: Software\Policies\Microsoft\Windows\EventLog\Security\AutoBackupLogFiles
                Value:       49, 0, 0, 0
                State:       Enabled

USER SETTINGS
--------------
    CN=Firstname Lastname,OU=IT Admins,OU=Domain Users,DC=domain,DC=local
    Last time Group Policy was applied: 11/5/2020 at 7:17:08 PM
    Group Policy was applied from:      DC1.domain.local
    Group Policy slow link threshold:   500 kbps
    Domain Name:                        DOMAIN
    Domain Type:                        Windows 2008 or later

    Applied Group Policy Objects
    -----------------------------
        Redirected Folders - Domain-Users
        Drive Mapping
        Printers
        Default Domain Policy

    The following GPOs were not applied because they were filtered out
    -------------------------------------------------------------------

        Production Printer
            Filtering:  Denied (Security)

        Local Group Policy
            Filtering:  Not Applied (Empty)

        Printers - Finance
            Filtering:  Denied (Security)

    The user is a part of the following security groups
    ---------------------------------------------------
        Domain Users
        Everyone
        Event Log Readers
        Performance Monitor Users
        BUILTIN\Users
        BUILTIN\Pre-Windows 2000 Compatible Access
        BUILTIN\Administrators
        REMOTE INTERACTIVE LOGON
        NT AUTHORITY\INTERACTIVE
        NT AUTHORITY\Authenticated Users
        This Organization
        LOCAL
        Domain Admins
        Quality
        FolderRedirectDeny
        Software
        Enterprise Admins
        Authentication authority asserted identity
        Denied RODC Password Replication Group
        NetworkAdmins
        High Mandatory Level

    The user has the following security privileges
    ----------------------------------------------

        Bypass traverse checking
        Increase a process working set
        Manage auditing and security log
        Back up files and directories
        Restore files and directories
        Change the system time
        Shut down the system
        Force shutdown from a remote system
        Take ownership of files or other objects
        Debug programs
        Modify firmware environment values
        Profile system performance
        Profile single process
        Increase scheduling priority
        Load and unload device drivers
        Create a pagefile
        Adjust memory quotas for a process
        Remove computer from docking station
        Perform volume maintenance tasks
        Impersonate a client after authentication
        Create global objects
        Change the time zone
        Create symbolic links
        Enable computer and user accounts to be trusted for delegation
        Add workstations to domain

    Resultant Set Of Policies for User
    -----------------------------------

        Software Installations
        ----------------------
            N/A

        Logon Scripts
        -------------
            N/A

        Logoff Scripts
        --------------
            N/A

        Public Key Policies
        -------------------
            N/A

        Administrative Templates
        ------------------------

            GPO: Redirected Folders - Domain-Users
                Folder Id: Software\Policies\Microsoft\Windows\NetCache\SyncAtLogoff
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Redirected Folders - Domain-Users
                Folder Id: Software\Policies\Microsoft\Windows\System\Fdeploy\FolderRedirectionEnableCacheRename
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Intelsat
                Folder Id: Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\ListBox_Support_ZoneMapKey
                Value:       1, 0, 0, 0
                State:       Enabled

            GPO: Redirected Folders - Domain-Users
                Folder Id: Software\Policies\Microsoft\Windows\NetCache\SyncAtLogon
                Value:       1, 0, 0, 0
                State:       Enabled

        Folder Redirection
        ------------------
            GPO: Redirected Folders - Domain-Users
                Folder Id: Documents
                    Primary Computer Evaluation: Not evaluated because primary computer policy is not enabled
                    InstallationType:            basic
                    Grant Type:                  Not Exclusive Rights
                    Move Type:                   Contents of Local Directory moved
                    Policy Removal:              Redirect the folder back to user profile location
                    Redirecting Group:           N/A
                    Redirected Path:             \\Domain-Files\Domain-Users$\%USERNAME%\Documents
                    Configuration Control:       Group Policy

            GPO: Redirected Folders - Domain-Users
                Folder Id: Favorites
                    Primary Computer Evaluation: Not evaluated because primary computer policy is not enabled
                    InstallationType:            basic
                    Grant Type:                  Not Exclusive Rights
                    Move Type:                   Contents of Local Directory moved
                    Policy Removal:              Redirect the folder back to user profile location
                    Redirecting Group:           N/A
                    Redirected Path:             \\Domain-Files\Domain-Users$\%USERNAME%\Favorites
                    Configuration Control:       Group Policy

            GPO: Redirected Folders - Domain-Users
                Folder Id: Desktop
                    Primary Computer Evaluation: Not evaluated because primary computer policy is not enabled
                    InstallationType:            basic
                    Grant Type:                  Not Exclusive Rights
                    Move Type:                   Contents of Local Directory moved
                    Policy Removal:              Redirect the folder back to user profile location
                    Redirecting Group:           N/A
                    Redirected Path:             \\Domain-Files\Domain-Users$\%USERNAME%\Desktop
                    Configuration Control:       Group Policy

        Internet Explorer Browser User Interface
        ----------------------------------------
            N/A

        Internet Explorer Connection
        ----------------------------
            N/A

        Internet Explorer URLs
        ----------------------
            N/A

        Internet Explorer Security
        --------------------------
            N/A

        Internet Explorer Programs
        --------------------------
            N/A
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-06*

1.If you can bind LDAP on other DC except this one, we can check if AD replication works fine.

All DCs. Confirm that replication is fine.

2.If the time is not synchronized, authentication problems may also occur.

Time is synchronized. As i mentioned, it was only specific accounts, the built-in domain Administrator account and my personal domain account. I was able to figure out the problem through gpsesult /z that both accounts were set on the DCs to deny the accounts to be logged in. It was denied both on the local policy as well as GPO. I removed both from the denied policies, and now my personal domain account is fine, but the Administrator account is still having issues.

3.Whether you are perform bind operation on DC or client? If your domain credential is correct, we can check whether the hardware keyboard buttons are normal, type the credential on one txt file to check.  

**4.Also do you provide the credential with UPN (usernam@keyman  .com) or domain\username, we can use the two one by one to see if it helps.

Again, i am 100% certain that the problem is not credential related. I have been troubleshooting this with multiple computers and have altered the passwords multiple times to simple passwords like 'Nameofmycity!!'

5.If it is NTLM authentication method, the NTLM version may also have impact.

Again, this is only happening with specific accounts. At the moment, only the built-in domain Administrator account that i know of.

If all above does not work. Please confirm the following information:  

1.Whether your domain is a single forest with one domain or multiple domains?

Single forest.

2.Do you have multiple DCs in this domain? If you have multiple DCs in this domain, can you bind LDAP on other DCs?  

We have 2 DCs, neither binds.

3.Please check whether AD replication is working fine. Run repadmin /showrepl and **repadmin /showrepl /csv >showrepl.csv* on PDC in this domain. If there is no error from the command result, then AD replication works fine

There is no error. All results are successful.

4.What LDAP tool are you using?  

I'm using lpd.exe to troubleshoot, but it is failing with Freeradius and Cisco Anyconnect.

5.If we use Windows built-in ldp.exe tool, how we bind LDAP (method 1 or method 2 or others)？  

Yes, i'm using lpd.exe to troubleshoot. Both method results in the error i posted in the original post.
