---
title: "How to use this documentation — pages 121-160"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0121-0160
family: powershell
documentKind: "doc"
abstract: "output to Get-Member . When you pipe the output of a command to Get-Member , it reveals the structure of the object returned by the command, detailing its properties and methods. Properties: The attributes of an object. Methods: The actions you can perform on an object. To illus"
---

# How to use this documentation — pages 121-160

<!-- p.121 -->

output to Get-Member . When you pipe the output of a command to Get-Member , it reveals the
structure of the object returned by the command, detailing its properties and methods.

     Properties: The attributes of an object.
     Methods: The actions you can perform on an object.

To illustrate this concept, consider a driver's license as an analogy. Like any object, a driver's
license has properties, such as eye color, which typically includes blue and brown values. In
contrast, methods represent actions you can perform on the object. For instance, Revoke is a
method that the Department of Motor Vehicles can perform on a driver's license.

Properties
To retrieve details about the Windows Time service on your system using PowerShell, use the
Get-Service cmdlet.

 PowerShell

 Get-Service -Name w32time

The results include the Status, Name, and DisplayName properties. The Status property
indicates that the service is Running . The value for the Name property is w32time , and the value
for the DisplayName property is Windows Time .

 Output

 Status     Name                  DisplayName
 ------     ----                  -----------
 Running    w32time               Windows Time

To list all available properties and methods for Get-Service , pipe it to Get-Member .

 PowerShell

 Get-Service -Name w32time | Get-Member

The results show the first line contains one piece of significant information. TypeName
identifies the type of object returned, which in this example is a
System.ServiceProcess.ServiceController object. This name is often abbreviated to the last part
of the TypeName, such as ServiceController, in this example.

 Output

<!-- p.122 -->

     TypeName: System.ServiceProcess.ServiceController

 Name                      MemberType    Definition
 ----                      ----------    ----------
 Name                      AliasProperty Name = ServiceName
 RequiredServices          AliasProperty RequiredServices = ServicesDepend...
 Disposed                  Event         System.EventHandler Disposed(Syst...
 Close                     Method        void Close()
 Continue                  Method        void Continue()
 CreateObjRef              Method        System.Runtime.Remoting.ObjRef Cr...
 Dispose                   Method        void Dispose(), void IDisposable....
 Equals                    Method        bool Equals(System.Object obj)
 ExecuteCommand            Method        void ExecuteCommand(int command)
 GetHashCode               Method        int GetHashCode()
 GetLifetimeService        Method        System.Object GetLifetimeService()
 GetType                   Method        type GetType()
 InitializeLifetimeService Method        System.Object InitializeLifetimeS...
 Pause                     Method        void Pause()
 Refresh                   Method        void Refresh()
 Start                     Method        void Start(), void Start(string[]...
 Stop                      Method        void Stop()
 WaitForStatus             Method        void WaitForStatus(System.Service...
 CanPauseAndContinue       Property      bool CanPauseAndContinue {get;}
 CanShutdown               Property      bool CanShutdown {get;}
 CanStop                   Property      bool CanStop {get;}
 Container                 Property      System.ComponentModel.IContainer ...
 DependentServices         Property      System.ServiceProcess.ServiceCont...
 DisplayName               Property      string DisplayName {get;set;}
 MachineName               Property      string MachineName {get;set;}
 ServiceHandle             Property      System.Runtime.InteropServices.Sa...
 ServiceName               Property      string ServiceName {get;set;}
 ServicesDependedOn        Property      System.ServiceProcess.ServiceCont...
 ServiceType               Property      System.ServiceProcess.ServiceType...
 Site                      Property      System.ComponentModel.ISite Site ...
 StartType                 Property      System.ServiceProcess.ServiceStar...
 Status                    Property      System.ServiceProcess.ServiceCont...
 ToString                  ScriptMethod System.Object ToString();

Notice when you piped Get-Service to Get-Member , there are more properties than are
displayed by default. Although these additional properties aren't shown by default, you can
select them by piping to Select-Object and using the Property parameter. The following
example selects all properties by piping the results of Get-Service to Select-Object and
specifying the * wildcard character as the value for the Property parameter.

 PowerShell

 Get-Service -Name w32time | Select-Object -Property *

<!-- p.123 -->

By default, PowerShell returns four properties as a table and five or more as a list. However,
some commands apply custom formatting to override the default number of properties
displayed in a table. You can use Format-Table and Format-List to override these defaults
manually.

 Output

 Name                : w32time
 RequiredServices    : {}
 CanPauseAndContinue : False
 CanShutdown         : True
 CanStop             : True
 DisplayName         : Windows Time
 DependentServices   : {}
 MachineName         : .
 ServiceName         : w32time
 ServicesDependedOn : {}
 ServiceHandle       :
 Status              : Running
 ServiceType         : Win32OwnProcess, Win32ShareProcess
 StartType           : Manual
 Site                :
 Container           :

Specific properties can also be selected using a comma-separated list as the value of the
Property parameter.

 PowerShell

 Get-Service -Name w32time |
     Select-Object -Property Status, Name, DisplayName, ServiceType

 Output

  Status Name    DisplayName                         ServiceType
  ------ ----    -----------                         -----------
 Running w32time Windows Time Win32OwnProcess, Win32ShareProcess

You can use wildcard characters when specifying property names with Select-Object .

In the following example, use Can* as one of the values for the Property parameter to return
all the properties that start with Can . These include CanPauseAndContinue, CanShutdown, and
CanStop.

 PowerShell

<!-- p.124 -->

 Get-Service -Name w32time |
     Select-Object -Property Status, DisplayName, Can*

Notice there are more properties listed than are displayed by default.

 Output

 Status              : Running
 DisplayName         : Windows Time
 CanPauseAndContinue : False
 CanShutdown         : True
 CanStop             : True

Methods
Methods are actions you can perform on an object. Use the MemberType parameter to narrow
down the results of Get-Member to display only the methods for Get-Service .

 PowerShell

 Get-Service -Name w32time | Get-Member -MemberType Method

As you can see, there are several methods.

 Output

     TypeName: System.ServiceProcess.ServiceController

 Name                      MemberType Definition
 ----                      ---------- ----------
 Close                     Method     void Close()
 Continue                  Method     void Continue()
 CreateObjRef              Method     System.Runtime.Remoting.ObjRef Creat...
 Dispose                   Method     void Dispose(), void IDisposable.Dis...
 Equals                    Method     bool Equals(System.Object obj)
 ExecuteCommand            Method     void ExecuteCommand(int command)
 GetHashCode               Method     int GetHashCode()
 GetLifetimeService        Method     System.Object GetLifetimeService()
 GetType                   Method     type GetType()
 InitializeLifetimeService Method     System.Object InitializeLifetimeServ...
 Pause                     Method     void Pause()
 Refresh                   Method     void Refresh()
 Start                     Method     void Start(), void Start(string[] args)
 Stop                      Method     void Stop()
 WaitForStatus             Method     void WaitForStatus(System.ServicePro...

<!-- p.125 -->

You can use the Stop method to stop a Windows service. You must run this command from an
elevated PowerShell session.

 PowerShell

 (Get-Service -Name w32time).Stop()

Query the status of the Windows Time service to confirm it's stopped.

 PowerShell

 Get-Service -Name w32time

 Output

 Status     Name                 DisplayName
 ------     ----                 -----------
 Stopped    w32time              Windows Time

You might use methods sparingly, but you should be aware of them. Sometimes, you find Get-
* commands without a corresponding Set-* command. Often, you can find a method to

perform a Set-* action in this scenario. The Get-SqlAgentJob cmdlet in the SqlServer
PowerShell module is an excellent example. No corresponding Set-* cmdlet exists, but you
can use a method to complete the same task. For more information about the SqlServer
PowerShell module and installation instructions, see the SQL Server PowerShell overview.

Another reason to be aware of methods is some PowerShell users assume you can't make
destructive changes with Get-* commands, but they can actually cause severe problems if
misused.

A better option is to use a dedicated cmdlet if one exists to perform an action. For example,
use the Start-Service cmdlet to start the Windows Time service.

By default, Start-Service , like the Start method of Get-Service , doesn't return any results.
However, one of the benefits of using a cmdlet is that it often provides additional capabilities
that aren't available with a method.

In the following example, use the PassThru parameter, which causes a cmdlet that doesn't
typically produce output to generate output.

Since PowerShell doesn't participate in User Access Control (UAC), you must run commands
that require elevation, such as Start-Service , from an elevated PowerShell session.

<!-- p.126 -->

 PowerShell

 Get-Service -Name w32time | Start-Service -PassThru

 Output

 Status     Name                 DisplayName
 ------     ----                 -----------
 Running    w32time              Windows Time

  ７ Note

  When working with PowerShell cmdlets, it's important to avoid making assumptions about
  their output.

To retrieve information about the PowerShell process running on your lab environment
computer, use the Get-Process cmdlet.

 PowerShell

 Get-Process -Name powershell

 Output

 Handles    NPM(K)     PM(K)       WS(K)       CPU(s)      Id   SI ProcessName
 -------    ------     -----       -----       ------      --   -- -----------
     710        31     55692       70580         0.72    9436    2 powershell

To determine the available properties, pipe Get-Process to Get-Member .

 PowerShell

 Get-Process -Name powershell | Get-Member

When using the Get-Process command, you might notice that some properties displayed by
default are missing when you view the results of Get-Member . This behavior is because several
of the values shown by default, such as NPM(K) , PM(K) , WS(K) , and CPU(s) , are calculated
properties. You must pipe commands to Get-Member to determine their actual property names.

 Output

<!-- p.127 -->

   TypeName: System.Diagnostics.Process

Name                       MemberType      Definition
----                       ----------      ----------
Handles                    AliasProperty   Handles = Handlecount
Name                       AliasProperty   Name = ProcessName
NPM                        AliasProperty   NPM = NonpagedSystemMemorySize64
PM                         AliasProperty   PM = PagedMemorySize64
SI                         AliasProperty   SI = SessionId
VM                         AliasProperty   VM = VirtualMemorySize64
WS                         AliasProperty   WS = WorkingSet64
Disposed                   Event           System.EventHandler Disposed(Sy...
ErrorDataReceived          Event           System.Diagnostics.DataReceived...
Exited                     Event           System.EventHandler Exited(Syst...
OutputDataReceived         Event           System.Diagnostics.DataReceived...
BeginErrorReadLine         Method          void BeginErrorReadLine()
BeginOutputReadLine        Method          void BeginOutputReadLine()
CancelErrorRead            Method          void CancelErrorRead()
CancelOutputRead           Method          void CancelOutputRead()
Close                      Method          void Close()
CloseMainWindow            Method          bool CloseMainWindow()
CreateObjRef               Method          System.Runtime.Remoting.ObjRef ...
Dispose                    Method          void Dispose(), void IDisposabl...
Equals                     Method          bool Equals(System.Object obj)
GetHashCode                Method          int GetHashCode()
GetLifetimeService         Method          System.Object GetLifetimeService()
GetType                    Method          type GetType()
InitializeLifetimeService Method           System.Object InitializeLifetim...
Kill                       Method          void Kill()
Refresh                    Method          void Refresh()
Start                      Method          bool Start()
ToString                   Method          string ToString()
WaitForExit                Method          bool WaitForExit(int millisecon...
WaitForInputIdle           Method          bool WaitForInputIdle(int milli...
__NounName                 NoteProperty    string __NounName=Process
BasePriority               Property        int BasePriority {get;}
Container                  Property        System.ComponentModel.IContaine...
EnableRaisingEvents        Property        bool EnableRaisingEvents {get;s...
ExitCode                   Property        int ExitCode {get;}
ExitTime                   Property        datetime ExitTime {get;}
Handle                     Property        System.IntPtr Handle {get;}
HandleCount                Property        int HandleCount {get;}
HasExited                  Property        bool HasExited {get;}
Id                         Property        int Id {get;}
MachineName                Property        string MachineName {get;}
MainModule                 Property        System.Diagnostics.ProcessModul...
MainWindowHandle           Property        System.IntPtr MainWindowHandle ...
MainWindowTitle            Property        string MainWindowTitle {get;}
MaxWorkingSet              Property        System.IntPtr MaxWorkingSet {ge...
MinWorkingSet              Property        System.IntPtr MinWorkingSet {ge...
Modules                    Property        System.Diagnostics.ProcessModul...
NonpagedSystemMemorySize   Property        int NonpagedSystemMemorySize {g...
NonpagedSystemMemorySize64 Property        long NonpagedSystemMemorySize64...
PagedMemorySize            Property        int PagedMemorySize {get;}

<!-- p.128 -->

 PagedMemorySize64             Property       long PagedMemorySize64 {get;}
 PagedSystemMemorySize         Property       int PagedSystemMemorySize {get;}
 PagedSystemMemorySize64       Property       long PagedSystemMemorySize64 {g...
 PeakPagedMemorySize           Property       int PeakPagedMemorySize {get;}
 PeakPagedMemorySize64         Property       long PeakPagedMemorySize64 {get;}
 PeakVirtualMemorySize         Property       int PeakVirtualMemorySize {get;}
 PeakVirtualMemorySize64       Property       long PeakVirtualMemorySize64 {g...
 PeakWorkingSet                Property       int PeakWorkingSet {get;}
 PeakWorkingSet64              Property       long PeakWorkingSet64 {get;}
 PriorityBoostEnabled          Property       bool PriorityBoostEnabled {get;...
 PriorityClass                 Property       System.Diagnostics.ProcessPrior...
 PrivateMemorySize             Property       int PrivateMemorySize {get;}
 PrivateMemorySize64           Property       long PrivateMemorySize64 {get;}
 PrivilegedProcessorTime       Property       timespan PrivilegedProcessorTim...
 ProcessName                   Property       string ProcessName {get;}
 ProcessorAffinity             Property       System.IntPtr ProcessorAffinity...
 Responding                    Property       bool Responding {get;}
 SafeHandle                    Property       Microsoft.Win32.SafeHandles.Saf...
 SessionId                     Property       int SessionId {get;}
 Site                          Property       System.ComponentModel.ISite Sit...
 StandardError                 Property       System.IO.StreamReader Standard...
 StandardInput                 Property       System.IO.StreamWriter Standard...
 StandardOutput                Property       System.IO.StreamReader Standard...
 StartInfo                     Property       System.Diagnostics.ProcessStart...
 StartTime                     Property       datetime StartTime {get;}
 SynchronizingObject           Property       System.ComponentModel.ISynchron...
 Threads                       Property       System.Diagnostics.ProcessThrea...
 TotalProcessorTime            Property       timespan TotalProcessorTime {get;}
 UserProcessorTime             Property       timespan UserProcessorTime {get;}
 VirtualMemorySize             Property       int VirtualMemorySize {get;}
 VirtualMemorySize64           Property       long VirtualMemorySize64 {get;}
 WorkingSet                    Property       int WorkingSet {get;}
 WorkingSet64                  Property       long WorkingSet64 {get;}
 PSConfiguration               PropertySet    PSConfiguration {Name, Id, Prio...
 PSResources                   PropertySet    PSResources {Name, Id, Handleco...
 Company                       ScriptProperty System.Object Company {get=$thi...
 CPU                           ScriptProperty System.Object CPU {get=$this.To...
 Description                   ScriptProperty System.Object Description {get=...
 FileVersion                   ScriptProperty System.Object FileVersion {get=...
 Path                          ScriptProperty System.Object Path {get=$this.M...
 Product                       ScriptProperty System.Object Product {get=$thi...
 ProductVersion                ScriptProperty System.Object ProductVersion {g...

You can't pipe a command to Get-Member that doesn't generate output. Because Start-Service
doesn't produce output by default, attempting to pipe it to Get-Member results in an error.

 PowerShell

 Start-Service -Name w32time | Get-Member

  ７ Note

<!-- p.129 -->

  To be piped to Get-Member , a command must produce object-based output.

 Output

 Get-Member : You must specify an object for the Get-Member cmdlet.
 At line:1 char:31
 + Start-Service -Name w32time | Get-Member
 +                               ~~~~~~~~~~
     + CategoryInfo          : CloseError: (:) [Get-Member], InvalidOperation
    Exception
     + FullyQualifiedErrorId : NoObjectInGetMember,Microsoft.PowerShell.Comma
    nds.GetMemberCommand

To avoid this error, specify the PassThru parameter with Start-Service . As previously
mentioned, adding the PassThru parameter causes a cmdlet that doesn't usually produce
output to generate output.

 PowerShell

 Start-Service -Name w32time -PassThru | Get-Member

 Output

     TypeName: System.ServiceProcess.ServiceController

 Name                      MemberType    Definition
 ----                      ----------    ----------
 Name                      AliasProperty Name = ServiceName
 RequiredServices          AliasProperty RequiredServices = ServicesDepend...
 Disposed                  Event         System.EventHandler Disposed(Syst...
 Close                     Method        void Close()
 Continue                  Method        void Continue()
 CreateObjRef              Method        System.Runtime.Remoting.ObjRef Cr...
 Dispose                   Method        void Dispose(), void IDisposable....
 Equals                    Method        bool Equals(System.Object obj)
 ExecuteCommand            Method        void ExecuteCommand(int command)
 GetHashCode               Method        int GetHashCode()
 GetLifetimeService        Method        System.Object GetLifetimeService()
 GetType                   Method        type GetType()
 InitializeLifetimeService Method        System.Object InitializeLifetimeS...
 Pause                     Method        void Pause()
 Refresh                   Method        void Refresh()
 Start                     Method        void Start(), void Start(string[]...
 Stop                      Method        void Stop()
 WaitForStatus             Method        void WaitForStatus(System.Service...
 CanPauseAndContinue       Property      bool CanPauseAndContinue {get;}
 CanShutdown               Property      bool CanShutdown {get;}
 CanStop                   Property      bool CanStop {get;}
 Container                 Property      System.ComponentModel.IContainer ...

<!-- p.130 -->

 DependentServices             Property       System.ServiceProcess.ServiceCont...
 DisplayName                   Property       string DisplayName {get;set;}
 MachineName                   Property       string MachineName {get;set;}
 ServiceHandle                 Property       System.Runtime.InteropServices.Sa...
 ServiceName                   Property       string ServiceName {get;set;}
 ServicesDependedOn            Property       System.ServiceProcess.ServiceCont...
 ServiceType                   Property       System.ServiceProcess.ServiceType...
 Site                          Property       System.ComponentModel.ISite Site ...
 StartType                     Property       System.ServiceProcess.ServiceStar...
 Status                        Property       System.ServiceProcess.ServiceCont...
 ToString                      ScriptMethod   System.Object ToString();

Out-Host is designed to show output directly in the PowerShell host and doesn't produce

object-based output. As a result, you can't pipe its output to Get-Member , which requires
object-based input.

 PowerShell

 Get-Service -Name w32time | Out-Host | Get-Member

 Output

 Status     Name                 DisplayName
 ------     ----                 -----------
 Running    w32time              Windows Time

 Get-Member : You must specify an object for the Get-Member cmdlet.
 At line:1 char:40
 + Get-Service -Name w32time | Out-Host | Get-Member
 +                                        ~~~~~~~~~~
     + CategoryInfo          : CloseError: (:) [Get-Member], InvalidOperation
    Exception
     + FullyQualifiedErrorId : NoObjectInGetMember,Microsoft.PowerShell.Comma
    nds.GetMemberCommand

Get-Command
Knowing the type of object a command produces allows you to search for commands that
accept that type of object as input.

 PowerShell

 Get-Command -ParameterType ServiceController

The following commands accept a ServiceController object via pipeline or parameter input.

<!-- p.131 -->

 Output

 CommandType       Name                                                    Version
 -----------       ----                                                    -------
 Cmdlet            Get-Service                                             3.1.0.0
 Cmdlet            Restart-Service                                         3.1.0.0
 Cmdlet            Resume-Service                                          3.1.0.0
 Cmdlet            Set-Service                                             3.1.0.0
 Cmdlet            Start-Service                                           3.1.0.0
 Cmdlet            Stop-Service                                            3.1.0.0
 Cmdlet            Suspend-Service                                         3.1.0.0

Active Directory

  ７ Note

  As mentioned in the chapter prerequisites, ensure you have RSAT installed for this section.
  Additionally, your lab environment computer must be a member of your lab environment
  Active Directory domain.

To identify the commands added to the ActiveDirectory PowerShell module after you install
RSAT, use Get-Command combined with the Module parameter. The following example lists all
the commands available in the ActiveDirectory module.

 PowerShell

 Get-Command -Module ActiveDirectory

The ActiveDirectory PowerShell module added a total of 147 commands.

Have you observed the naming convention of these commands? The nouns in the command
names are prefixed with AD to avoid potential naming conflicts with commands in other
modules. This prefixing is a common practice among PowerShell modules.

 Output

 CommandType       Name                                                    Version
 -----------       ----                                                    -------
 Cmdlet            Add-ADCentralAccessPolicyMember                         1.0.1.0
 Cmdlet            Add-ADComputerServiceAccount                            1.0.1.0
 Cmdlet            Add-ADDomainControllerPasswordReplicationPolicy         1.0.1.0
 Cmdlet            Add-ADFineGrainedPasswordPolicySubject                  1.0.1.0
 Cmdlet            Add-ADGroupMember                                       1.0.1.0
 Cmdlet            Add-ADPrincipalGroupMembership                          1.0.1.0
 Cmdlet            Add-ADResourcePropertyListMember                        1.0.1.0

<!-- p.132 -->

 Cmdlet             Clear-ADAccountExpiration                                1.0.1.0
 Cmdlet             Clear-ADClaimTransformLink                               1.0.1.0
 Cmdlet             Disable-ADAccount                                        1.0.1.0
 ...

By default, the Get-ADUser cmdlet retrieves a limited set of properties for user objects and
limits its output to the first 1,000 users. This constraint is a performance optimization designed
to avoid overwhelming Active Directory with excessive data retrieval.

 PowerShell

 Get-ADUser -Identity mike | Get-Member -MemberType Properties

Even if you only have a basic understanding of Active Directory, you might recognize that a
user account has more properties than those shown in the example.

 Output

     TypeName: Microsoft.ActiveDirectory.Management.ADUser

 Name              MemberType Definition
 ----              ---------- ----------
 DistinguishedName Property   System.String DistinguishedName {get;set;}
 Enabled           Property   System.Boolean Enabled {get;set;}
 GivenName         Property   System.String GivenName {get;set;}
 Name              Property   System.String Name {get;}
 ObjectClass       Property   System.String ObjectClass {get;set;}
 ObjectGUID        Property   System.Nullable`1[[System.Guid, mscorlib, Ve...
 SamAccountName    Property   System.String SamAccountName {get;set;}
 SID               Property   System.Security.Principal.SecurityIdentifier...
 Surname           Property   System.String Surname {get;set;}
 UserPrincipalName Property   System.String UserPrincipalName {get;set;}

The Get-ADUser cmdlet includes a Properties parameter to specify additional properties
beyond the defaults you want to retrieve. To return all properties, use the * wildcard character
as the parameter value.

 PowerShell

 Get-ADUser -Identity mike -Properties * | Get-Member -MemberType Properties

 Output

     TypeName: Microsoft.ActiveDirectory.Management.ADUser

 Name                                      MemberType Definition

<!-- p.133 -->

----                                ---------- ----------
AccountExpirationDate               Property   System.DateTime AccountEx...
accountExpires                      Property   System.Int64 accountExpir...
AccountLockoutTime                  Property   System.DateTime AccountLo...
AccountNotDelegated                 Property   System.Boolean AccountNot...
AllowReversiblePasswordEncryption   Property   System.Boolean AllowRever...
AuthenticationPolicy                Property   Microsoft.ActiveDirectory...
AuthenticationPolicySilo            Property   Microsoft.ActiveDirectory...
BadLogonCount                       Property   System.Int32 BadLogonCoun...
badPasswordTime                     Property   System.Int64 badPasswordT...
badPwdCount                         Property   System.Int32 badPwdCount ...
CannotChangePassword                Property   System.Boolean CannotChan...
CanonicalName                       Property   System.String CanonicalNa...
Certificates                        Property   Microsoft.ActiveDirectory...
City                                Property   System.String City {get;s...
CN                                  Property   System.String CN {get;}
codePage                            Property   System.Int32 codePage {ge...
Company                             Property   System.String Company {ge...
CompoundIdentitySupported           Property   Microsoft.ActiveDirectory...
Country                             Property   System.String Country {ge...
countryCode                         Property   System.Int32 countryCode ...
Created                             Property   System.DateTime Created {...
createTimeStamp                     Property   System.DateTime createTim...
Deleted                             Property   System.Boolean Deleted {g...
Department                          Property   System.String Department ...
Description                         Property   System.String Description...
DisplayName                         Property   System.String DisplayName...
DistinguishedName                   Property   System.String Distinguish...
Division                            Property   System.String Division {g...
DoesNotRequirePreAuth               Property   System.Boolean DoesNotReq...
dSCorePropagationData               Property   Microsoft.ActiveDirectory...
EmailAddress                        Property   System.String EmailAddres...
EmployeeID                          Property   System.String EmployeeID ...
EmployeeNumber                      Property   System.String EmployeeNum...
Enabled                             Property   System.Boolean Enabled {g...
Fax                                 Property   System.String Fax {get;set;}
GivenName                           Property   System.String GivenName {...
HomeDirectory                       Property   System.String HomeDirecto...
HomedirRequired                     Property   System.Boolean HomedirReq...
HomeDrive                           Property   System.String HomeDrive {...
HomePage                            Property   System.String HomePage {g...
HomePhone                           Property   System.String HomePhone {...
Initials                            Property   System.String Initials {g...
instanceType                        Property   System.Int32 instanceType...
isDeleted                           Property   System.Boolean isDeleted ...
KerberosEncryptionType              Property   Microsoft.ActiveDirectory...
LastBadPasswordAttempt              Property   System.DateTime LastBadPa...
LastKnownParent                     Property   System.String LastKnownPa...
lastLogoff                          Property   System.Int64 lastLogoff {...
lastLogon                           Property   System.Int64 lastLogon {g...
LastLogonDate                       Property   System.DateTime LastLogon...
lastLogonTimestamp                  Property   System.Int64 lastLogonTim...
LockedOut                           Property   System.Boolean LockedOut ...
logonCount                          Property   System.Int32 logonCount {...
LogonWorkstations                   Property   System.String LogonWorkst...

<!-- p.134 -->

Manager                              Property   System.String Manager {ge...
MemberOf                             Property   Microsoft.ActiveDirectory...
MNSLogonAccount                      Property   System.Boolean MNSLogonAc...
MobilePhone                          Property   System.String MobilePhone...
Modified                             Property   System.DateTime Modified ...
modifyTimeStamp                      Property   System.DateTime modifyTim...
msDS-User-Account-Control-Computed   Property   System.Int32 msDS-User-Ac...
Name                                 Property   System.String Name {get;}
nTSecurityDescriptor                 Property   System.DirectoryServices....
ObjectCategory                       Property   System.String ObjectCateg...
ObjectClass                          Property   System.String ObjectClass...
ObjectGUID                           Property   System.Nullable`1[[System...
objectSid                            Property   System.Security.Principal...
Office                               Property   System.String Office {get...
OfficePhone                          Property   System.String OfficePhone...
Organization                         Property   System.String Organizatio...
OtherName                            Property   System.String OtherName {...
PasswordExpired                      Property   System.Boolean PasswordEx...
PasswordLastSet                      Property   System.DateTime PasswordL...
PasswordNeverExpires                 Property   System.Boolean PasswordNe...
PasswordNotRequired                  Property   System.Boolean PasswordNo...
POBox                                Property   System.String POBox {get;...
PostalCode                           Property   System.String PostalCode ...
PrimaryGroup                         Property   System.String PrimaryGrou...
primaryGroupID                       Property   System.Int32 primaryGroup...
PrincipalsAllowedToDelegateToAccount Property   Microsoft.ActiveDirectory...
ProfilePath                          Property   System.String ProfilePath...
ProtectedFromAccidentalDeletion      Property   System.Boolean ProtectedF...
pwdLastSet                           Property   System.Int64 pwdLastSet {...
SamAccountName                       Property   System.String SamAccountN...
sAMAccountType                       Property   System.Int32 sAMAccountTy...
ScriptPath                           Property   System.String ScriptPath ...
sDRightsEffective                    Property   System.Int32 sDRightsEffe...
ServicePrincipalNames                Property   Microsoft.ActiveDirectory...
SID                                  Property   System.Security.Principal...
SIDHistory                           Property   Microsoft.ActiveDirectory...
SmartcardLogonRequired               Property   System.Boolean SmartcardL...
sn                                   Property   System.String sn {get;set;}
State                                Property   System.String State {get;...
StreetAddress                        Property   System.String StreetAddre...
Surname                              Property   System.String Surname {ge...
Title                                Property   System.String Title {get;...
TrustedForDelegation                 Property   System.Boolean TrustedFor...
TrustedToAuthForDelegation           Property   System.Boolean TrustedToA...
UseDESKeyOnly                        Property   System.Boolean UseDESKeyO...
userAccountControl                   Property   System.Int32 userAccountC...
userCertificate                      Property   Microsoft.ActiveDirectory...
UserPrincipalName                    Property   System.String UserPrincip...
uSNChanged                           Property   System.Int64 uSNChanged {...
uSNCreated                           Property   System.Int64 uSNCreated {...
whenChanged                          Property   System.DateTime whenChang...
whenCreated                          Property   System.DateTime whenCreat...

<!-- p.135 -->

The default configuration for retrieving Active Directory user account properties is intentionally
limited to avoid performance issues. Trying to return every property for every user account in
your production Active Directory environment could severely degrade the performance of your
domain controllers and network. Usually, you only need specific properties for certain users.
However, returning all properties for a single user is reasonable when identifying the available
properties.

It's not uncommon to run a command multiple times when prototyping it. If you anticipate
running a resource-intensive query when prototyping a command, consider executing it once
and storing the results in a variable. Then, you can work with the variable's contents more
efficiently than repeatedly executing a resource-intensive query.

For example, the following command retrieves all properties for a user account and stores the
results in a variable named $Users . Work with the contents of the $Users variable instead of
running the Get-ADUser command multiple times. Remember, the variable's contents don't
update automatically when a user's information changes in Active Directory.

 PowerShell

 $Users = Get-ADUser -Identity mike -Properties *

You can explore the available properties by piping the $Users variable to Get-Member .

 PowerShell

 $Users | Get-Member -MemberType Properties

To view specific properties such as Name, LastLogonDate, and LastBadPasswordAttempt, pipe
the $Users variable to Select-Object . This method displays the desired properties and their
values based on the contents of the $Users variable, eliminating the need for multiple queries
to Active Directory. It's a more resource-efficient approach than repeatedly executing the Get-
ADUser command.

 PowerShell

 $Users | Select-Object -Property Name, LastLogonDate, LastBadPasswordAttempt

When you query Active Directory, filter the data at the source using the Properties parameter
of Get-ADUser to return only the necessary properties.

 PowerShell

<!-- p.136 -->

 Get-ADUser -Identity mike -Properties LastLogonDate, LastBadPasswordAttempt

 Output

 DistinguishedName      : CN=Mike F. Robbins,CN=Users,DC=mikefrobbins,DC=com
 Enabled                : True
 GivenName              : Mike
 LastBadPasswordAttempt :
 LastLogonDate          : 11/14/2023 5:10:16 AM
 Name                   : Mike F. Robbins
 ObjectClass            : user
 ObjectGUID             : 11c7b61f-46c3-4399-9ed0-ff4e453bc2a2
 SamAccountName         : mike
 SID                    : S-1-5-21-611971124-518002951-3581791498-1105
 Surname                : Robbins
 UserPrincipalName      : μ@mikefrobbins.com

Summary
In this chapter, you learned how to determine what type of object a command produces, what
properties and methods are available for a command, and how to work with commands that
limit the properties returned by default.

Review
   1. What type of object does the Get-Process cmdlet produce?
   2. How do you determine what the available properties are for a command?
   3. What should you check for if a command exists to get something but not to set the same
     thing?
   4. How can some commands that don't return output by default be made to generate
     output?
   5. What should you consider doing when prototyping a command that produces a large
     amount of output?

References
     Get-Member
     Viewing Object Structure (Get-Member)
     about_Objects
     about_Properties
     about_Methods

<!-- p.137 -->

      No PowerShell Cmdlet to Start or Stop Something? Don't Forget to Check for Methods on
      the Get Cmdlets

Next steps
In Chapter 4, you'll learn about one-liners and the pipeline.

 Last updated on 02/06/2026

<!-- p.138 -->

Chapter 4 - One-Liners and the pipeline
When I started learning PowerShell, I initially relied on the Graphical User Interface (GUI) for
tasks that seemed too complex for simple PowerShell commands. However, as I continued to
learn, I improved my skills and moved from basic one-liners to creating scripts, functions, and
modules. It's important to remember that feeling overwhelmed by advanced examples online is
normal. No one starts as an expert in PowerShell; we all start as beginners.

For those who primarily use the GUI for administrative tasks, install the management tools on
your administrative workstation to remotely manage your servers. Whether your server uses a
GUI or the Server Core OS installation, this approach is beneficial. It's a practical way to
familiarize yourself with remote server management in preparation for performing
administrative tasks with PowerShell.

As with the previous chapters, try these concepts in your lab environment.

One-Liners
A PowerShell one-liner is one continuous pipeline. It's a common misconception that a
command on one physical line is a PowerShell one-liner, but this isn't always true.

For instance, consider the following example: the command extends over multiple physical
lines, yet it's a PowerShell one-liner because it forms a continuous pipeline. Line-breaking a
lengthy one-liner at the pipe symbol, a natural breaking point in PowerShell, is recommended
to enhance readability and clarity. This strategic use of line breaks improves readability without
disrupting the flow of the pipeline.

 PowerShell

 Get-Service |
     Where-Object CanPauseAndContinue -EQ $true |
     Select-Object -Property *

 Output

 Name                : LanmanWorkstation
 RequiredServices    : {NSI, MRxSmb20, Bowser}
 CanPauseAndContinue : True
 CanShutdown         : False
 CanStop             : True
 DisplayName         : Workstation

<!-- p.139 -->

DependentServices    : {SessionEnv, Netlogon}
MachineName          : .
ServiceName          : LanmanWorkstation
ServicesDependedOn   : {NSI, MRxSmb20, Bowser}
ServiceHandle        :
Status               : Running
ServiceType          : Win32OwnProcess, Win32ShareProcess
StartType            : Automatic
Site                 :
Container            :

Name                : Netlogon
RequiredServices    : {LanmanWorkstation}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Netlogon
DependentServices   : {}
MachineName         : .
ServiceName         : Netlogon
ServicesDependedOn : {LanmanWorkstation}
ServiceHandle       :
Status              : Running
ServiceType         : Win32ShareProcess
StartType           : Automatic
Site                :
Container           :

Name                : vmicheartbeat
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Hyper-V Heartbeat Service
DependentServices   : {}
MachineName         : .
ServiceName         : vmicheartbeat
ServicesDependedOn : {}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Manual
Site                :
Container           :

Name                : vmickvpexchange
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Hyper-V Data Exchange Service
DependentServices   : {}
MachineName         : .
ServiceName         : vmickvpexchange
ServicesDependedOn : {}

<!-- p.140 -->

ServiceHandle      :
Status             : Running
ServiceType        : Win32OwnProcess, Win32ShareProcess
StartType          : Manual
Site               :
Container          :

Name                : vmicrdv
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Hyper-V Remote Desktop Virtualization Service
DependentServices   : {}
MachineName         : .
ServiceName         : vmicrdv
ServicesDependedOn : {}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Manual
Site                :
Container           :

Name                : vmicshutdown
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Hyper-V Guest Shutdown Service
DependentServices   : {}
MachineName         : .
ServiceName         : vmicshutdown
ServicesDependedOn : {}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Manual
Site                :
Container           :

Name                : vmicvss
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : False
CanStop             : True
DisplayName         : Hyper-V Volume Shadow Copy Requestor
DependentServices   : {}
MachineName         : .
ServiceName         : vmicvss
ServicesDependedOn : {}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Manual

<!-- p.141 -->

Site               :
Container          :

Name                : webthreatdefsvc
RequiredServices    : {RpcSs, wtd}
CanPauseAndContinue : True
CanShutdown         : True
CanStop             : True
DisplayName         : Web Threat Defense Service
DependentServices   : {}
MachineName         : .
ServiceName         : webthreatdefsvc
ServicesDependedOn : {RpcSs, wtd}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Manual
Site                :
Container           :

Name                : webthreatdefusersvc_644de
RequiredServices    : {}
CanPauseAndContinue : True
CanShutdown         : True
CanStop             : True
DisplayName         : Web Threat Defense User Service_644de
DependentServices   : {}
MachineName         : .
ServiceName         : webthreatdefusersvc_644de
ServicesDependedOn : {}
ServiceHandle       :
Status              : Running
ServiceType         : 240
StartType           : Automatic
Site                :
Container           :

Name                : Winmgmt
RequiredServices    : {RPCSS}
CanPauseAndContinue : True
CanShutdown         : True
CanStop             : True
DisplayName         : Windows Management Instrumentation
DependentServices   : {}
MachineName         : .
ServiceName         : Winmgmt
ServicesDependedOn : {RPCSS}
ServiceHandle       :
Status              : Running
ServiceType         : Win32OwnProcess, Win32ShareProcess
StartType           : Automatic
Site                :
Container           :

<!-- p.142 -->

Natural line breaks can occur at commonly used characters, including comma ( , ) and opening
brackets ( [ ), braces ( { ), and parenthesis ( ( ). Others that aren't so common include the
semicolon ( ; ), equals sign ( = ), and both opening single and double quotes ( ' , " ).

Using the backtick ( ` ) or grave accent character as a line continuation is controversial. It's best
to avoid it if possible. Using a backtick following a natural line break character is a common
mistake. This redundancy is unnecessary and can clutter the code.

The commands in the following example execute correctly from the PowerShell console.
However, attempting to run them in the console pane of the PowerShell Integrated Scripting
Environment (ISE) results in an error. This difference occurs because, unlike the PowerShell
console, the console pane of the ISE doesn't automatically anticipate the continuation of a
command onto the next line. To prevent this issue, press Shift + Enter in the console pane of
the ISE instead of Enter when you need to extend a command across multiple lines. This key
combination signals to the ISE that the command is continuing on the following line,
preventing the execution that leads to errors.

 PowerShell

 Get-Service -Name w32time |
     Select-Object -Property *

 Output

 Name                : w32time
 RequiredServices    : {}
 CanPauseAndContinue : False
 CanShutdown         : True
 CanStop             : True
 DisplayName         : Windows Time
 DependentServices   : {}
 MachineName         : .
 ServiceName         : w32time
 ServicesDependedOn : {}
 ServiceHandle       :
 Status              : Running
 ServiceType         : Win32OwnProcess, Win32ShareProcess
 StartType           : Manual
 Site                :
 Container           :

This next example doesn't qualify as a PowerShell one-liner because it's not one continuous
pipeline. Instead, it's two separate commands placed on a single line, separated by a
semicolon. This semicolon indicates the end of one command and the beginning of another.

<!-- p.143 -->

  PowerShell

  $Service = 'w32time'; Get-Service -Name $Service

  Output

  Status    Name                   DisplayName
  ------    ----                   -----------
  Running   w32time                Windows Time

Many programming and scripting languages require a semicolon at the end of each line.
However, in PowerShell, semicolons at the end of lines are unnecessary and not recommended.
You should avoid them for cleaner and more readable code.

Filter Left
This chapter demonstrates how to filter the results of various commands.

It's a best practice in PowerShell to filter the results as early as possible in the pipeline.
Achieving this involves applying filters using parameters on the initial command, usually at the
beginning of the pipeline. This is commonly referred to as filtering left.

To illustrate this concept, consider the following example: Use the Name parameter of Get-
Service to filter the results at the beginning of the pipeline, returning only the details for the

Windows Time service. This method demonstrates efficient data retrieval, ensuring you only
return the necessary and relevant information.

  PowerShell

  Get-Service -Name w32time

  Output

  Status    Name                   DisplayName
  ------    ----                   -----------
  Running   w32time                Windows Time

It's common to see online examples of a PowerShell command being piped to the Where-
Object cmdlet to filter its results. This technique is inefficient if an earlier command in the

pipeline has a parameter to perform the filtering.

  PowerShell

<!-- p.144 -->

  Get-Service | Where-Object Name -EQ w32time

  Output

  Status     Name                   DisplayName
  ------     ----                   -----------
  Running    W32Time                Windows Time

The first example demonstrates filtering directly at the source, returning results specifically for
the Windows Time service. In contrast, the second example retrieves all services and then uses
another command to filter the results. This might seem insignificant in small-scale scenarios,
but consider a situation involving a large dataset, like Active Directory. It's inefficient to retrieve
details for thousands of user accounts only to narrow them down to a small subset. Practice
filtering left — applying filters as early as possible in the command sequence — even in
seemingly trivial cases. This habit ensures efficiency in more complex scenarios where it
becomes more important.

Command sequencing for effective filtering
There's a misconception that the order of commands in PowerShell is inconsequential, but this
is a misunderstanding. The sequence in which you arrange commands, particularly when
filtering, is important. For example, suppose you're using Select-Object to choose specific
properties and Where-Object to filter. In that case, it's essential to apply the filtering first.
Failing to do so means the necessary properties might not be available in the pipeline for
filtering, leading to ineffective or erroneous results.

The following example fails to produce results because the CanPauseAndContinue property is
absent when Select-Object is piped to Where-Object . This is because the
CanPauseAndContinue property wasn't included in the selection made by Select-Object .
Effectively, it's excluded or filtered out.

  PowerShell

  Get-Service |
      Select-Object -Property DisplayName, Running, Status |
      Where-Object CanPauseAndContinue

Reversing the order of Select-Object and Where-Object produces the desired results.

  PowerShell

<!-- p.145 -->

 Get-Service |
     Where-Object CanPauseAndContinue |
     Select-Object -Property DisplayName, Status

 Output

 DisplayName                                    Status
 -----------                                    ------
 Workstation                                   Running
 Netlogon                                      Running
 Hyper-V Heartbeat Service                     Running
 Hyper-V Data Exchange Service                 Running
 Hyper-V Remote Desktop Virtualization Service Running
 Hyper-V Guest Shutdown Service                Running
 Hyper-V Volume Shadow Copy Requestor          Running
 Web Threat Defense Service                    Running
 Web Threat Defense User Service_644de         Running
 Windows Management Instrumentation            Running

The Pipeline
As seen in many examples throughout this book, you can often use the output of one
command as input for another command. In Chapter 3, Get-Member was used to determine
what type of object a command produces.

Chapter 3 also showed using the ParameterType parameter of Get-Command to determine what
commands accepted that type of input. Depending on how thorough help for a command is, it
might include an INPUTS and OUTPUTS section.

The INPUTS section indicates that you can pipe a ServiceController or a String object to the
Stop-Service cmdlet.

 PowerShell

 help Stop-Service -Full

The following output is abbreviated to show the relevant portion of the help.

 Output

 ...
 INPUTS
     System.ServiceProcess.ServiceController
         You can pipe a service object to this cmdlet.

<!-- p.146 -->

       System.String
           You can pipe a string that contains the name of a service to this
           cmdlet.

 OUTPUTS
     None
         By default, this cmdlet returns no output.

       System.ServiceProcess.ServiceController
           When you use the PassThru parameter, this cmdlet returns a
           ServiceController object representing the service.
 ...

However, it doesn't specify which parameters accept this type of input. You can determine that
information by checking the different parameters in the full version of the help for the Stop-
Service cmdlet.

 PowerShell

 help Stop-Service -Full

Once again, only the relevant help is shown in the following results. Notice that the
DisplayName parameter doesn't accept pipeline input. The InputObject parameter accepts
pipeline input by value for ServiceController objects. The Name parameter accepts pipeline
input by value for String objects and pipeline input by property name.

 Output

 ...
 -DisplayName <System.String[]>
     Specifies the display names of the services to stop. Wildcard
     characters are permitted.

       Required?                      true
       Position?                      named
       Default value                  None
       Accept pipeline input?         False
       Accept wildcard characters?    true

 -InputObject <System.ServiceProcess.ServiceController[]>
     Specifies ServiceController objects that represent the services to
     stop. Enter a variable that contains the objects, or type a command
     or expression that gets the objects.

       Required?                      true
       Position?                      0
       Default value                  None
       Accept pipeline input?         True (ByValue)

<!-- p.147 -->

        Accept wildcard characters?     false

 -Name <System.String[]>
     Specifies the service names of the services to stop. Wildcard
     characters are permitted.

        Required?                       true
        Position?                       0
        Default value                   None
        Accept pipeline input?          True (ByPropertyName, ByValue)
        Accept wildcard characters?     true
 ...

When handling pipeline input, a parameter that accepts pipeline input both by property name
and by value prioritizes by value binding first. If this method fails, it attempts to process
pipeline input by property name. However, the term by value can be misleading. A more
accurate description is by type.

For instance, if you pipe the output of a command that generates a ServiceController object to
Stop-Service , this output is bound to the InputObject parameter. If the piped command

produces a String object, it associates the output with the Name parameter. If you pipe output
from a command that doesn't produce a ServiceController or String object, but does include a
property named Name, Stop-Service binds the value of the Name property to its Name
parameter.

Determine what type of output the Get-Service command produces.

 PowerShell

 Get-Service -Name w32time | Get-Member

Get-Service produces a ServiceController object type.

 Output

       TypeName: System.ServiceProcess.ServiceController

As shown in the help for Stop-Service cmdlet, the InputObject parameter accepts
ServiceController objects through the pipeline by value. This implies that when you pipe the
output of the Get-Service cmdlet to Stop-Service , the ServiceController objects produced by
Get-Service bind to the InputObject parameter of Stop-Service .

 PowerShell

<!-- p.148 -->

 Get-Service -Name w32time | Stop-Service

Now try string input. Pipe w32time to Get-Member to confirm that it's a string.

 PowerShell

 'w32time' | Get-Member

 Output

     TypeName: System.String

The PowerShell help documentation illustrates that when you pipe a string to Stop-Service , it
binds to the Name parameter by value. Conduct a practical test to see this in action: pipe the
string w32time to Stop-Service . This example demonstrates how Stop-Service processes the
string w32time as the name of the service to stop. Execute the following command to observe
this binding and command execution in action.

Notice that w32time is enclosed in single quotes. In PowerShell, it's a best practice to use single
quotes for static strings, reserving double quotes for situations where the string contains
variables that require expansion. Single quotes tell PowerShell to treat the content literally
without parsing for variables. This approach not only ensures accuracy in how your script
interprets the string but also enhances performance, as PowerShell expends less processing
effort on strings within single quotes.

 PowerShell

 'w32time' | Stop-Service

Create a custom object to test pipeline input by property name for the Name parameter of
Stop-Service .

 PowerShell

 $customObject = [pscustomobject]@{
     Name = 'w32time'
 }

The contents of the CustomObject variable is a PSCustomObject object type and it contains a
property named Name.

<!-- p.149 -->

 PowerShell

 $customObject | Get-Member

 Output

     TypeName: System.Management.Automation.PSCustomObject

 Name        MemberType   Definition
 ----        ----------   ----------
 Equals      Method       bool Equals(System.Object obj)
 GetHashCode Method       int GetHashCode()
 GetType     Method       type GetType()
 ToString    Method       string ToString()
 Name        NoteProperty string Name=w32time

When working with variables in PowerShell, such as $customObject in this example, it's
important to use double quotes if you need to enclose the variable in quotes. Double quotes
allow for variable expansion — PowerShell evaluates the variable and uses its value. For
example, if you enclose $customObject in double quotes and pipe it to Get-Member , PowerShell
processes the value of $customObject . In contrast, using single quotes would result in piping
the literal string $customObject to Get-Member , not the value of the variable. This distinction is
important for scenarios where you need to evaluate the value of variables.

When piping the contents of the $customObject variable to the Stop-Service cmdlet, the
binding to the Name parameter occurs by property name rather than by value. This is because
$customObject is an object that contains a property named Name. In this scenario, PowerShell

identifies the Name property within $customObject and uses its value for the Name parameter
of Stop-Service .

Create another custom object using a different property name, such as Service.

 PowerShell

 $customObject = [pscustomobject]@{
     Service = 'w32time'
 }

An error occurs while trying to stop the w32time service by piping $customObject to Stop-
Service . The pipeline binding fails because $customObject doesn't produce a ServiceController

or String object and doesn't contain a Name property.

 PowerShell

<!-- p.150 -->

 $customObject | Stop-Service

 Output

 Stop-Service : Cannot find any service with service name
 '@{Service=w32time}'.
 At line:1 char:17
 + $customObject | Stop-Service
 +                 ~~~~~~~~~~~~
     + CategoryInfo          : ObjectNotFound: (@{Service=w32time}:String) [
    Stop-Service], ServiceCommandException
     + FullyQualifiedErrorId : NoServiceFoundForGivenName,Microsoft.PowerShe
    ll.Commands.StopServiceCommand

When the output property names of one command don't match the pipeline input
requirements of another command, you can use Select-Object to rename the property names
so they line up correctly.

In the following example, use Select-Object to rename the Service property to a property
named Name.

At first glance, the syntax of this example might appear complex. However, it's essential to
understand that more than copying and pasting code is required to learn the syntax. Instead,
take the time to type out the code manually. This hands-on practice helps you remember the
syntax, and it becomes more intuitive with repeated effort. Utilizing multiple monitors or split
screen can also aid in the learning process. Display the example code on one screen while
actively typing and experimenting with it on another. This setup makes it easier to follow along
and enhances your understanding and retention of the syntax.

 PowerShell

 $customObject |
     Select-Object -Property @{Name='Name';Expression={$_.Service}} |
     Stop-Service

There are instances where you might need to use a parameter that doesn't accept pipeline
input. In such cases, you can still use the output of one command as the input for another.
First, capture and save the display names of a few specific Windows services into a text file. This
step allows you to use the saved data as input for another command.

 PowerShell

<!-- p.151 -->

 'Background Intelligent Transfer Service', 'Windows Time' |
     Out-File -FilePath $env:TEMP\services.txt

You can use parentheses to pass the output of one command as input for a parameter to
another command.

 PowerShell

 Stop-Service -DisplayName (Get-Content -Path $env:TEMP\services.txt)

This concept is like the order of operations in Algebra. Just as mathematical operations within
parentheses are computed first, the command enclosed in parentheses is executed before the
outer command.

PowerShellGet
PowerShellGet, a module included with PowerShell version 5.0 and higher, provides commands
to discover, install, update, and publish PowerShell modules and other items in a NuGet
repository. For those using PowerShell version 3.0 and above, PowerShellGet is also available as
a separate download.

The PowerShell Gallery    is an online repository hosted by Microsoft, designed as a central hub
for sharing PowerShell modules, scripts, and other resources. While Microsoft hosts the
PowerShell Gallery, the PowerShell community contributes most of the available modules and
scripts. Given the source of these modules and scripts, exercise caution before integrating any
code from the PowerShell Gallery into your environment. Review and test downloads from the
PowerShell Gallery in an isolated test environment. This process ensures the code is secure and
reliable, works as expected, and safeguards your environment from potential issues or
vulnerabilities arising from unvetted code.

Many organizations opt to establish their own internal, private NuGet repository. This
repository serves a dual purpose. First, it acts as a secure location for storing modules
developed in-house, intended solely for internal use. Secondly, it provides a vetted collection
of modules sourced externally, including those from public repositories. Companies typically
undertake a thorough validation process before adding these external modules to the internal
repository. This process is important to ensure the modules are free from malicious content
and align with the security and operational standards of the company.

Use the Find-Module cmdlet that's part of the PowerShellGet module to find a module in the
PowerShell Gallery that I wrote named MrToolkit.

<!-- p.152 -->

 PowerShell

 Find-Module -Name MrToolkit

 Output

 NuGet provider is required to continue
 PowerShellGet requires NuGet provider version '2.8.5.201' or newer to
 interact with NuGet-based repositories. The NuGet provider must be available
  in 'C:\Program Files\PackageManagement\ProviderAssemblies' or
 'C:\Users\mikefrobbins\AppData\Local\PackageManagement\ProviderAssemblies'.
 You can also install the NuGet provider by running 'Install-PackageProvider
 -Name NuGet -MinimumVersion 2.8.5.201 -Force'. Do you want PowerShellGet to
 install and import the NuGet provider now?
 [Y] Yes [N] No [S] Suspend [?] Help (default is "Y"):

 Version      Name                        Repository          Description
 -------      ----                        ----------          -----------
 1.3          MrToolkit                   PSGallery           Misc PowerShell Tools

The first time you use one of the commands from the PowerShellGet module, you're prompted
to install the NuGet provider.

To install the MrToolkit module, pipe the previous command to Install-Module .

 PowerShell

 Find-Module -Name MrToolkit | Install-Module -Scope CurrentUser

 Output

 Untrusted repository
 You are installing the modules from an untrusted repository. If you trust
 this repository, change its InstallationPolicy value by running the
 Set-PSRepository cmdlet. Are you sure you want to install the modules from
 'https://www.powershellgallery.com/api/v2'?
 [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend [?] Help
 (default is "N"):y

Since the PowerShell Gallery is an untrusted repository, it prompts you to approve the
installation of the module.

Finding pipeline input the easy way
The MrToolkit module includes a function named Get-MrPipelineInput . This cmdlet is
designed to provide users with a convenient method for identifying the parameters of a

<!-- p.153 -->

command capable of accepting pipeline input. Specifically, it reveals three key aspects:

     Which parameters of a command can receive pipeline input
     The type of object each parameter accepts
     Whether they accept pipeline input by value or by property name

This capability dramatically simplifies the process of understanding and utilizing the pipeline
capabilities of PowerShell commands.

The information previously obtained by analyzing the help documentation can be determined
using this function.

 PowerShell

 Get-MrPipelineInput -Name Stop-Service | Format-List

 Output

 ParameterName                   : InputObject
 ParameterType                   : System.ServiceProcess.ServiceController[]
 ValueFromPipeline               : True
 ValueFromPipelineByPropertyName : False

 ParameterName                   : Name
 ParameterType                   : System.String[]
 ValueFromPipeline               : True
 ValueFromPipelineByPropertyName : True

Summary
In this chapter, you learned about the intricacies of PowerShell one-liners. You also learned that
the physical line count of a command is irrelevant to its classification as a PowerShell one-liner.
Additionally, you learned about key concepts such as filtering left, the pipeline, and
PowerShellGet.

Review
   1. What's a PowerShell one-liner?
   2. What are some characters where natural line breaks can occur in PowerShell?
   3. Why should you filter left?
   4. What are the two ways that a PowerShell command can accept pipeline input?
   5. Why shouldn't you trust commands found in the PowerShell Gallery?

<!-- p.154 -->

References
      about_Pipelines
      about_Command_Syntax
      about_Parameters
      PowerShellGet: The BIG EASY way to discover, install, and update PowerShell modules

Next steps
In Chapter 5, you'll learn about formatting, aliases, providers, and comparison operators.

 Last updated on 02/06/2026

<!-- p.155 -->

Chapter 5 - Formatting, aliases, providers,
comparison

Prerequisites
The SqlServer PowerShell module is required by some examples shown in this chapter. For
more information about the SqlServer PowerShell module and installation instructions, see SQL
Server PowerShell overview. It's also used in subsequent chapters. Download and install it on
your Windows lab environment computer.

Format Right
In Chapter 4, you learned to filter as far to the left as possible. The rule for manually formatting
a command's output is similar to that rule, except it needs to occur as far to the right as
possible.

The most common format commands are Format-Table and Format-List . Format-Wide and
Format-Custom can also be used, but are less common.

As mentioned in Chapter 3, a command that returns more than four properties defaults to a list
unless custom formatting is used.

  PowerShell

  Get-Service -Name w32time |
      Select-Object -Property Status, DisplayName, Can*

  Output

  Status              : Running
  DisplayName         : Windows Time
  CanPauseAndContinue : False
  CanShutdown         : True
  CanStop             : True

Use the Format-Table cmdlet to manually override the formatting and show the output in a
table instead of a list.

  PowerShell

<!-- p.156 -->

 Get-Service -Name w32time |
     Select-Object -Property Status, DisplayName, Can* |
     Format-Table

 Output

 Status DisplayName CanPauseAndContinue CanShutdown CanStop
 ------ ----------- ------------------- ----------- -------
 Running Windows Time             False        True    True

The default output for Get-Service is three properties in a table.

 PowerShell

 Get-Service -Name w32time

 Output

 Status    Name                  DisplayName
 ------    ----                  -----------
 Running   w32time               Windows Time

Use the Format-List cmdlet to override the default formatting and return the results in a list.

 PowerShell

 Get-Service -Name w32time | Format-List

Notice that simply piping Get-Service to Format-List made it return additional properties.
This doesn't occur with every command because of how the format for that particular
command is set up behind the scenes.

 Output

 Name                : w32time
 DisplayName         : Windows Time
 Status              : Running
 DependentServices   : {}
 ServicesDependedOn : {}
 CanPauseAndContinue : False
 CanShutdown         : True
 CanStop             : True
 ServiceType         : Win32OwnProcess, Win32ShareProcess

<!-- p.157 -->

The number one thing to be aware of with the format cmdlets is they produce format objects
that are different than normal objects in PowerShell.

 PowerShell

 Get-Service -Name w32time | Format-List | Get-Member

 Output

     TypeName: Microsoft.PowerShell.Commands.Internal.Format.FormatStartData

 Name                                    MemberType Definition
 ----                                    ---------- ----------
 Equals                                  Method     bool Equals(System.Obj...
 GetHashCode                             Method     int GetHashCode()
 GetType                                 Method     type GetType()
 ToString                                Method     string ToString()
 autosizeInfo                            Property   Microsoft.PowerShell.C...
 ClassId2e4f51ef21dd47e99d3c952918aff9cd Property   string ClassId2e4f51ef...
 groupingEntry                           Property   Microsoft.PowerShell.C...
 pageFooterEntry                         Property   Microsoft.PowerShell.C...
 pageHeaderEntry                         Property   Microsoft.PowerShell.C...
 shapeInfo                               Property   Microsoft.PowerShell.C...

     TypeName: Microsoft.PowerShell.Commands.Internal.Format.GroupStartData

 Name                                    MemberType Definition
 ----                                    ---------- ----------
 Equals                                  Method     bool Equals(System.Obj...
 GetHashCode                             Method     int GetHashCode()
 GetType                                 Method     type GetType()
 ToString                                Method     string ToString()
 ClassId2e4f51ef21dd47e99d3c952918aff9cd Property   string ClassId2e4f51ef...
 groupingEntry                           Property   Microsoft.PowerShell.C...
 shapeInfo                               Property   Microsoft.PowerShell.C...

     TypeName: Microsoft.PowerShell.Commands.Internal.Format.FormatEntryData

 Name                                    MemberType Definition
 ----                                    ---------- ----------
 Equals                                  Method     bool Equals(System.Obj...
 GetHashCode                             Method     int GetHashCode()
 GetType                                 Method     type GetType()
 ToString                                Method     string ToString()
 ClassId2e4f51ef21dd47e99d3c952918aff9cd Property   string ClassId2e4f51ef...
 formatEntryInfo                         Property   Microsoft.PowerShell.C...
 outOfBand                               Property   bool outOfBand {get;set;}
 writeStream                             Property   Microsoft.PowerShell.C...

<!-- p.158 -->

     TypeName: Microsoft.PowerShell.Commands.Internal.Format.GroupEndData

 Name                                    MemberType Definition
 ----                                    ---------- ----------
 Equals                                  Method     bool Equals(System.Obj...
 GetHashCode                             Method     int GetHashCode()
 GetType                                 Method     type GetType()
 ToString                                Method     string ToString()
 ClassId2e4f51ef21dd47e99d3c952918aff9cd Property   string ClassId2e4f51ef...
 groupingEntry                           Property   Microsoft.PowerShell.C...

     TypeName: Microsoft.PowerShell.Commands.Internal.Format.FormatEndData

 Name                                    MemberType Definition
 ----                                    ---------- ----------
 Equals                                  Method     bool Equals(System.Obj...
 GetHashCode                             Method     int GetHashCode()
 GetType                                 Method     type GetType()
 ToString                                Method     string ToString()
 ClassId2e4f51ef21dd47e99d3c952918aff9cd Property   string ClassId2e4f51ef...
 groupingEntry                           Property   Microsoft.PowerShell.C...

What this means is format commands can't be piped to most other commands. They can be
piped to some of the Out-* commands, but that's about it. This is why you want to perform
any formatting at the very end of the line (format right).

Aliases
An alias in PowerShell is a shorter name for a command. PowerShell includes a set of built-in
aliases and you can also define your own aliases.

The Get-Alias cmdlet is used to find aliases. If you already know the alias for a command, the
Name parameter is used to determine what command the alias is associated with.

 PowerShell

 Get-Alias -Name gcm

 Output

 CommandType        Name                                                   Version
 -----------        ----                                                   -------
 Alias              gcm -> Get-Command

Multiple aliases can be specified for the value of the Name parameter.

<!-- p.159 -->

 PowerShell

 Get-Alias -Name gcm, gm

 Output

 CommandType       Name                                                     Version
 -----------       ----                                                     -------
 Alias             gcm -> Get-Command
 Alias             gm -> Get-Member

You often see the Name parameter omitted since it's a positional parameter.

 PowerShell

 Get-Alias gm

 Output

 CommandType       Name                                                     Version
 -----------       ----                                                     -------
 Alias             gm -> Get-Member

If you want to find aliases for a command, you need to use the Definition parameter.

 PowerShell

 Get-Alias -Definition Get-Command, Get-Member

 Output

 CommandType       Name                                                     Version
 -----------       ----                                                     -------
 Alias             gcm -> Get-Command
 Alias             gm -> Get-Member

The Definition parameter can't be used positionally, so it must be specified.

Aliases can save you a few keystrokes, and they're fine when you type commands into the
console. They shouldn't be used in scripts or any code that you're saving or sharing with
others. As mentioned earlier in this book, using full cmdlet and parameter names is self-
documenting and easier to understand.

<!-- p.160 -->

Use caution when creating your own aliases because they only exist in your current PowerShell
session on your computer.

Providers
A provider in PowerShell is an interface that allows file system-like access to a data store. There
are several built-in providers in PowerShell.

 PowerShell

 Get-PSProvider

As you can see in the following results, there are built-in providers for the registry, aliases,
environment variables, the file system, functions, variables, certificates, and WSMan.

 Output

 Name                     Capabilities                 Drives
 ----                     ------------                 ------
 Registry                 ShouldProcess, Transactions {HKLM, HKCU}
 Alias                    ShouldProcess                {Alias}
 Environment              ShouldProcess                {Env}
 FileSystem               Filter, ShouldProcess, Cr... {C, D}
 Function                 ShouldProcess                {Function}
 Variable                 ShouldProcess                {Variable}

The actual drives that these providers use to expose their data store can be determined with
the Get-PSDrive cmdlet. The Get-PSDrive cmdlet not only displays drives exposed by providers
but also displays Windows logical drives, including drives mapped to network shares.

 PowerShell

 Get-PSDrive

 Output

 Name              Used (GB)       Free (GB) Provider          Root
 ----              ---------       --------- --------          ----
 Alias                                       Alias
 C                      18.56         107.62 FileSystem        C:\
 Cert                                        Certificate       \
 D                                           FileSystem        D:\
 Env                                         Environment
 Function                                    Function
 HKCU                                        Registry          HKEY_CURRENT_USER
