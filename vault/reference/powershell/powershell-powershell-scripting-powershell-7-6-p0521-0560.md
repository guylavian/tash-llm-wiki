---
title: "How to use this documentation — pages 521-560"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0521-0560
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0521-0560
family: powershell
documentKind: "doc"
abstract: "Complex process manipulation is possible by using some of the object filtering cmdlets. Because a Process object has a Responding property that's true when it's no longer responding, you can stop all nonresponsive applications with the following command: PowerShell Get-Process |"
---

# How to use this documentation — pages 521-560

<!-- p.521 -->

Complex process manipulation is possible by using some of the object filtering cmdlets.
Because a Process object has a Responding property that's true when it's no longer
responding, you can stop all nonresponsive applications with the following command:

 PowerShell

 Get-Process | Where-Object -FilterScript {$_.Responding -eq $false} | Stop-Process

You can use the same approach in other situations. For example, suppose a secondary
notification area application automatically runs when users start another application. You may
find that this doesn't work correctly in Terminal Services sessions, but you still want to keep it in
sessions that run on the physical computer console. Sessions connected to the physical
computer desktop always have a session ID of 0, so you can stop all instances of the process
that are in other sessions by using Where-Object and the process, SessionId:

 PowerShell

 Get-Process -Name BadApp | Where-Object -FilterScript {$_.SessionId -neq 0} | Stop-
 Process

The Stop-Process cmdlet doesn't have a ComputerName parameter. Therefore, to run a stop
process command on a remote computer, you need to use the Invoke-Command cmdlet. For
example, to stop the PowerShell process on the Server01 remote computer, type:

 PowerShell

 Invoke-Command -ComputerName Server01 {Stop-Process PowerShell}

Stopping All Other PowerShell Sessions
It may occasionally be useful to be able to stop all running PowerShell sessions other than the
current session. If a session is using too many resources or is inaccessible (it may be running
remotely or in another desktop session), you may not be able to directly stop it. If you try to
stop all running sessions, however, the current session may be terminated instead.

Each PowerShell session has an environment variable PID that contains the Id of the Windows
PowerShell process. You can check the $PID against the Id of each session and terminate only
Windows PowerShell sessions that have a different Id. The following pipeline command does
this and returns the list of terminated sessions (because of the use of the PassThru parameter):

<!-- p.522 -->

  PowerShell

  Get-Process -Name powershell | Where-Object -FilterScript {$_.Id -ne $PID} |
      Stop-Process -PassThru

  Output

  Handles    NPM(K)       PM(K)      WS(K) VM(M)   CPU(s)     Id ProcessName
  -------    ------       -----      ----- -----   ------     -- -----------
      334         9       23348      29136   143     1.03    388 powershell
      304         9       23152      29040   143     1.03    632 powershell
      302         9       20916      26804   143     1.03   1116 powershell
      335         9       25656      31412   143     1.09   3452 powershell
      303         9       23156      29044   143     1.05   3608 powershell
      287         9       21044      26928   143     1.02   3672 powershell

Starting, debugging, and waiting for processes
PowerShell also comes with cmdlets to start (or restart), debug a process, and wait for a
process to complete before running a command. For information about these cmdlets, see the
cmdlet help topic for each cmdlet.

See also
      Get-Process
      Stop-Process
      Start-Process
      Wait-Process
      Debug-Process
      Invoke-Command

 Last updated on 03/24/2025

<!-- p.523 -->

Managing services
  This sample only applies to Windows PowerShell 5.1.

There are eight core Service cmdlets, designed for a wide range of service tasks . This article
only looks at listing and changing running state for services. You can get a list of service
cmdlets using Get-Command *-Service . You can find information about each cmdlet by using
Get-Help <Cmdlet-Name> , such as Get-Help New-Service .

Getting services
You can get the services on a local or remote computer by using the Get-Service cmdlet. As
with Get-Process , using the Get-Service command without parameters returns all services.
You can filter by name, even using an asterisk as a wildcard:

 PowerShell

 PS> Get-Service -Name se*

 Status     Name                  DisplayName
 ------     ----                  -----------
 Running    seclogon              Secondary Logon
 Running    SENS                  System Event Notification
 Stopped    ServiceLayer          ServiceLayer

Because it isn't always apparent what the real name for the service is, you may find you need to
find services by display name. You can search by specific name, use wildcards, or provide a list
of display names:

 PowerShell

 PS> Get-Service -DisplayName se*

 Status     Name                  DisplayName
 ------     ----                  -----------
 Running    lanmanserver          Server
 Running    SamSs                 Security Accounts Manager
 Running    seclogon              Secondary Logon
 Stopped    ServiceLayer          ServiceLayer
 Running    wscsvc                Security Center

 PS> Get-Service -DisplayName ServiceLayer, Server

<!-- p.524 -->

 Status    Name                 DisplayName
 ------    ----                 -----------
 Running   lanmanserver         Server
 Stopped   ServiceLayer         ServiceLayer

Getting remote services
With Windows PowerShell, you can use the ComputerName parameter of the Get-Service
cmdlet to get the services on remote computers. The ComputerName parameter accepts
multiple values and wildcard characters, so you can get the services on multiple computers
with a single command. For example, the following command gets the services on the Server01
remote computer.

 PowerShell

 Get-Service -ComputerName Server01

Starting in PowerShell 6.0, the *-Service cmdlets don't have the ComputerName parameter.
You can still get services on remote computers with PowerShell remoting. For example, the
following command gets the services on the Server02 remote computer.

 PowerShell

 Invoke-Command -ComputerName Server02 -ScriptBlock { Get-Service }

You can also manage services with the other *-Service cmdlets. For more information on
PowerShell remoting, see about_Remote.

Getting required and dependent services
The Get-Service cmdlet has two parameters that are very useful in service administration. The
DependentServices parameter gets services that depend on the service.

The RequiredServices parameter gets services upon which the LanmanWorkstation service
depends.

 PowerShell

 PS> Get-Service -Name LanmanWorkstation -RequiredServices

 Status    Name                 DisplayName
 ------    ----                 -----------
 Running   MRxSmb20             SMB 2.0 MiniRedirector

<!-- p.525 -->

  Running   bowser                Bowser
  Running   MRxSmb10              SMB 1.x MiniRedirector
  Running   NSI                   Network Store Interface Service

The DependentServices parameter gets that require the LanmanWorkstation service.

  PowerShell

  PS> Get-Service -Name LanmanWorkstation -DependentServices

  Status    Name                  DisplayName
  ------    ----                  -----------
  Running   SessionEnv            Terminal Services Configuration
  Running   Netlogon              Netlogon
  Stopped   Browser               Computer Browser
  Running   BITS                  Background Intelligent Transfer Ser...

The following command gets all services that have dependencies. The Format-Table cmdlet to
display the Status, Name, RequiredServices, and DependentServices properties of the
services.

  PowerShell

  Get-Service -Name * | Where-Object {$_.RequiredServices -or $_.DependentServices} |
    Format-Table -Property Status, Name, RequiredServices, DependentServices -Auto

Stopping, starting, suspending, and restarting
services
The Service cmdlets all have the same general form. Services can be specified by common
name or display name, and take lists and wildcards as values. To stop the print spooler, use:

  PowerShell

  Stop-Service -Name spooler

To start the print spooler after it's stopped, use:

  PowerShell

  Start-Service -Name spooler

To suspend the print spooler, use:

<!-- p.526 -->

 PowerShell

 Suspend-Service -Name spooler

The Restart-Service cmdlet works in the same manner as the other Service cmdlets:

 PowerShell

 PS> Restart-Service -Name spooler

 WARNING: Waiting for service 'Print Spooler (Spooler)' to finish starting...
 WARNING: Waiting for service 'Print Spooler (Spooler)' to finish starting...
 PS>

Notice that you get a repeated warning message about the Print Spooler starting up. When
you perform a service operation that takes some time, PowerShell notifies you that it's still
attempting to perform the task.

If you want to restart multiple services, you can get a list of services, filter them, and then
perform the restart:

 PowerShell

 PS> Get-Service | Where-Object -FilterScript {$_.CanStop} | Restart-Service

 WARNING: Waiting for service 'Computer Browser (Browser)' to finish stopping...
 WARNING: Waiting for service 'Computer Browser (Browser)' to finish stopping...
 Restart-Service : can't stop service 'Logical Disk Manager (dmserver)' because
  it has dependent services. It can only be stopped if the Force flag is set.
 At line:1 char:57
 + Get-Service | Where-Object -FilterScript {$_.CanStop} | Restart-Service <<<<
 WARNING: Waiting for service 'Print Spooler (Spooler)' to finish starting...
 WARNING: Waiting for service 'Print Spooler (Spooler)' to finish starting...

These Service cmdlets don't have a ComputerName parameter, but you can run them on a
remote computer by using the Invoke-Command cmdlet. For example, the following command
restarts the Spooler service on the Server01 remote computer.

 PowerShell

 Invoke-Command -ComputerName Server01 {Restart-Service Spooler}

Setting service properties

<!-- p.527 -->

The Set-Service cmdlet changes the properties of a service on a local or remote computer.
Because the service status is a property, you can use this cmdlet to start, stop, and suspend a
service. The Set-Service cmdlet also has a StartupType parameter that lets you change the
service startup type.

To use Set-Service on Windows Vista and later versions of Windows, open PowerShell with the
Run as administrator option.

For more information, see Set-Service

See also
      about_Remote
      Get-Service
      Set-Service
      Restart-Service
      Suspend-Service

 Last updated on 03/24/2025

<!-- p.528 -->

Working with printers in Windows
Article • 12/09/2022

  This sample only applies to Windows platforms.

You can use PowerShell to manage printers using WMI and the WScript.Network COM
object from WSH.

Listing printer connections
The simplest way to list the printers installed on a computer is to use the WMI
Win32_Printer class:

  PowerShell

  Get-CimInstance -Class Win32_Printer

You can also list the printers using the WScript.Network COM object that's typically
used in WSH scripts:

  PowerShell

  (New-Object -ComObject WScript.Network).EnumPrinterConnections()

Because this command returns a simple string collection of port names and printer
device names without any distinguishing labels, it isn't easy to interpret.

Adding a network printer
To add a new network printer, use WScript.Network:

  PowerShell

  (New-Object -ComObject
  WScript.Network).AddWindowsPrinterConnection("\\Printserver01\Xerox5")

Setting a default printer

<!-- p.529 -->

To use WMI to set the default printer, find the printer in the Win32_Printer collection
and then invoke the SetDefaultPrinter method:

  PowerShell

  $printer = Get-CimInstance -Class Win32_Printer -Filter "Name='HP LaserJet
  5Si'"
  Invoke-CimMethod -InputObject $printer -MethodName SetDefaultPrinter

WScript.Network is a little simpler to use, because it has a SetDefaultPrinter method
that takes only the printer name as an argument:

  PowerShell

  (New-Object -ComObject WScript.Network).SetDefaultPrinter('HP LaserJet 5Si')

Removing a printer connection
To remove a printer connection, use the WScript.Network RemovePrinterConnection
method:

  PowerShell

  (New-Object -ComObject
  WScript.Network).RemovePrinterConnection("\\Printserver01\Xerox5")

<!-- p.530 -->

Performing networking tasks
  This sample only applies to Windows platforms.

Because TCP/IP is the most commonly used network protocol, most low-level network protocol
administration tasks involve TCP/IP. In this section, we use PowerShell and WMI to do these
tasks.

Listing IP addresses for a computer
To get all IP addresses in use on the local computer, use the following command:

  PowerShell

  Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true |
      Select-Object -ExpandProperty IPAddress

Since the IPAddress property of a Win32_NetworkAdapterConfiguration object is an array,
you must use the ExpandProperty parameter of Select-Object to see the entire list of
addresses.

  Output

  10.0.0.1
  fe80::60ea:29a7:a233:7cb7
  2601:600:a27f:a470:f532:6451:5630:ec8b
  2601:600:a27f:a470:e167:477d:6c5c:342d
  2601:600:a27f:a470:b021:7f0d:eab9:6299
  2601:600:a27f:a470:a40e:ebce:1a8c:a2f3
  2601:600:a27f:a470:613c:12a2:e0e0:bd89
  2601:600:a27f:a470:444f:17ec:b463:7edd
  2601:600:a27f:a470:10fd:7063:28e9:c9f3
  2601:600:a27f:a470:60ea:29a7:a233:7cb7
  2601:600:a27f:a470::2ec1

Using the Get-Member cmdlet, you can see that the IPAddress property is an array:

  PowerShell

  Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true |
      Get-Member -Name IPAddress

<!-- p.531 -->

 Output

    TypeName:
 Microsoft.Management.Infrastructure.CimInstance#root/cimv2/Win32_NetworkAdapterConf
 iguration

 Name      MemberType Definition
 ----      ---------- ----------
 IPAddress Property   string[] IPAddress {get;}

The IPAddress property for each network adapter is actually an array. The braces in the
definition indicate that IPAddress isn't a System.String value, but an array of System.String
values.

Listing IP configuration data
To display detailed IP configuration data for each network adapter, use the following
command:

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true

The default display for the network adapter configuration object is a very reduced set of the
available information. For in-depth inspection and troubleshooting, use Select-Object or a
formatting cmdlet, such as Format-List , to specify the properties to be displayed.

In modern TCP/IP networks you are probably not interested in IPX or WINS properties. You can
use the ExcludeProperty parameter of Select-Object to hide properties with names that begin
with "WINS" or "IPX".

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true |
     Select-Object -ExcludeProperty IPX*,WINS*

This command returns detailed information about DHCP, DNS, routing, and other minor IP
configuration properties.

Pinging computers
You can perform a simple ping against a computer by using Win32_PingStatus. The following
command performs the ping, but returns lengthy output:

<!-- p.532 -->

 PowerShell

 Get-CimInstance -Class Win32_PingStatus -Filter "Address='127.0.0.1'"

The response from Win32_PingStatus contains 29 properties. You can use Format-Table to
select the properties that are most interesting to you. The AutoSize parameter of Format-Table
resizes the table columns so that they display properly in PowerShell.

 PowerShell

 Get-CimInstance -Class Win32_PingStatus -Filter "Address='127.0.0.1'" |
     Format-Table -Property Address,ResponseTime,StatusCode -AutoSize

 Output

 Address   ResponseTime StatusCode
 -------   ------------ ----------
 127.0.0.1            0          0

A StatusCode of 0 indicates a successful ping.

You can use an array to ping multiple computers with a single command. Because there is
more than one address, use the ForEach-Object to ping each address separately:

 PowerShell

 '127.0.0.1','localhost','bing.com' |
   ForEach-Object -Process {
     Get-CimInstance -Class Win32_PingStatus -Filter ("Address='$_'") |
       Select-Object -Property Address,ResponseTime,StatusCode
   }

You can use the same command format to ping all the addresses on a subnet, such as a private
network that uses network number 192.168.1.0 and a standard Class C subnet mask
(255.255.255.0)., Only addresses in the range of 192.168.1.1 through 192.168.1.254 are
legitimate local addresses (0 is always reserved for the network number and 255 is a subnet
broadcast address).

To represent an array of the numbers from 1 through 254 in PowerShell, use the expression
1..254 . A complete subnet ping can be performed by adding each value in the range to a

partial address in the ping statement:

 PowerShell

<!-- p.533 -->

 1..254| ForEach-Object -Process {
   Get-CimInstance -Class Win32_PingStatus -Filter ("Address='192.168.1.$_'") } |
     Select-Object -Property Address,ResponseTime,StatusCode

Note that this technique for generating a range of addresses can be used elsewhere as well.
You can generate a complete set of addresses in this way:

 PowerShell

 $ips = 1..254 | ForEach-Object -Process {'192.168.1.' + $_}

Retrieving network adapter properties
Earlier, we mentioned that you could retrieve general configuration properties using the
Win32_NetworkAdapterConfiguration class. Although not strictly TCP/IP information, network
adapter information such as MAC addresses and adapter types can be useful for understanding
what's going on with a computer. To get a summary of this information, use the following
command:

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapter -ComputerName .

Assigning the DNS domain for a network adapter
To assign the DNS domain for automatic name resolution, use the SetDNSDomain method of
the Win32_NetworkAdapterConfiguration. The Query parameter of Invoke-CimMethod takes a
WQL query string. The cmdlet calls the method specified on each instance returned by the
query.

 PowerShell

 $wql = 'SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled=True'
 $args = @{ DnsDomain = 'fabrikam.com'}
 Invoke-CimMethod -MethodName SetDNSDomain -Arguments $args -Query $wql

Filtering on IPEnabled=True is necessary, because even on a network that uses only TCP/IP,
several of the network adapter configurations on a computer aren't true TCP/IP adapters.
they're general software elements supporting RAS, VPN, QoS, and other services for all
adapters and thus don't have an address of their own.

<!-- p.534 -->

Performing DHCP configuration tasks
Modifying DHCP details involves working with a set of network adapters, just as the DNS
configuration does. There are several distinct actions you can perform using WMI.

Finding DHCP-enabled adapters
To find the DHCP-enabled adapters on a computer, use the following command:

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter
 "DHCPEnabled=$true"

To exclude adapters with IP configuration problems, you can retrieve only IP-enabled adapters:

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter "IPEnabled=$true
 and DHCPEnabled=$true"

Retrieving DHCP properties
Because DHCP-related properties for an adapter generally begin with DHCP , you can use the
Property parameter of Format-Table to display only those properties:

 PowerShell

 Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter        "IPEnabled=$true
 and DHCPEnabled=$true" |
   Format-Table -Property DHCP*

Enabling DHCP on each adapter
To enable DHCP on all adapters, use the following command:

 PowerShell

 $wql = 'SELECT * from Win32_NetworkAdapterConfiguration WHERE IPEnabled=True and
 DHCPEnabled=False'
 Invoke-CimMethod -MethodName ReleaseDHCPLease -Query $wql

<!-- p.535 -->

Using the filter statement IPEnabled=True and DHCPEnabled=False avoids enabling DHCP where
it's already enabled.

Releasing and renewing DHCP leases on specific adapters
Instances of the Win32_NetworkAdapterConfiguration class has ReleaseDHCPLease and
RenewDHCPLease methods. Both are used in the same way. In general, use these methods if you

only need to release or renew addresses for an adapter on a specific subnet. The easiest way to
filter adapters on a subnet is to choose only the adapter configurations that use the gateway
for that subnet. For example, the following command releases all DHCP leases on adapters on
the local computer that are obtaining DHCP leases from 192.168.1.254:

 PowerShell

 $wql = 'SELECT * from Win32_NetworkAdapterConfiguration WHERE
 DHCPServer="192.168.1.1"'
 Invoke-CimMethod -MethodName ReleaseDHCPLease -Query $wql

The only change for renewing a DHCP lease is to use the RenewDHCPLease method instead of
the ReleaseDHCPLease method:

 PowerShell

 $wql = 'SELECT * from Win32_NetworkAdapterConfiguration WHERE
 DHCPServer="192.168.1.1"'
 Invoke-CimMethod -MethodName RenewDHCPLease -Query $wql

  ７ Note

  When using these methods on a remote computer, be aware that you can lose access to
  the remote system if you are connected to it through the adapter with the released or
  renewed lease.

Releasing and renewing DHCP leases on all adapters
You can perform global DHCP address releases or renewals on all adapters by using the
Win32_NetworkAdapterConfiguration methods, ReleaseDHCPLeaseAll and RenewDHCPLeaseAll .
However, the command must apply to the WMI class, rather than a particular adapter, because
releasing and renewing leases globally is performed on the class, not on a specific adapter. The
Invoke-CimMethod cmdlet can call the methods of a class.

<!-- p.536 -->

 PowerShell

 Invoke-CimMethod -ClassName Win32_NetworkAdapterConfiguration -MethodName
 ReleaseDHCPLeaseAll

You can use the same command format to invoke the RenewDHCPLeaseAll method:

 PowerShell

 Invoke-CimMethod -ClassName Win32_NetworkAdapterConfiguration -MethodName
 RenewDHCPLeaseAll

Creating a network share
To create a network share, use the Create method of Win32_Share:

 PowerShell

 Invoke-CimMethod -ClassName Win32_Share -MethodName Create -Arguments @{
     Path = 'C:\temp'
     Name = 'TempShare'
     Type = [uint32]0 #Disk Drive
     MaximumAllowed = [uint32]25
     Description = 'test share of the temp folder'
 }

This is equivalent to the following net share command on Windows:

 PowerShell

 net share tempshare=C:\temp /users:25 /remark:"test share of the temp folder"

To call a method of a WMI class that takes parameters you must know what parameters are
available and the types of those parameters. For example, you can list the methods of the
Win32_Class with the following commands:

 PowerShell

 (Get-CimClass -ClassName Win32_Share).CimClassMethods

 Output

 Name            ReturnType Parameters                                   Qualifiers
 ----            ---------- ----------                                   ----------
 Create              UInt32 {Access, Description, MaximumAllowed, Name…} {Constructor,

<!-- p.537 -->

 Implemented, MappingStrings, Stati…
 SetShareInfo      UInt32 {Access, Description, MaximumAllowed}               {Implemented,
 MappingStrings}
 GetAccessMask     UInt32 {}                                                  {Implemented,
 MappingStrings}
 Delete            UInt32 {}                                                  {Destructor,
 Implemented, MappingStrings}

Use the following command to list the parameters of the Create method.

 PowerShell

 (Get-CimClass -ClassName Win32_Share).CimClassMethods['Create'].Parameters

 Output

 Name            CimType Qualifiers
 ReferenceClassName
 ----            ------- ----------                                  ---------------
 ---
 Access         Instance {EmbeddedInstance, ID, In, MappingStrings…}
 Description      String {ID, In, MappingStrings, Optional}
 MaximumAllowed   UInt32 {ID, In, MappingStrings, Optional}
 Name             String {ID, In, MappingStrings}
 Password         String {ID, In, MappingStrings, Optional}
 Path             String {ID, In, MappingStrings}
 Type             UInt32 {ID, In, MappingStrings}

You can also read the documentation for Create method of the Win32_Share class.

Removing a network share
You can remove a network share with Win32_Share, but the process is slightly different from
creating a share, because you need to retrieve the specific instance to be removed, rather than
the Win32_Share class. The following example deletes the share TempShare:

 PowerShell

 $wql = 'SELECT * from Win32_Share WHERE Name="TempShare"'
 Invoke-CimMethod -MethodName Delete -Query $wql

Connecting a Windows-accessible network drive
The New-PSDrive cmdlet can create a PowerShell drive that's mapped to a network share.

<!-- p.538 -->

  PowerShell

  New-PSDrive -Name "X" -PSProvider "FileSystem" -Root "\\Server01\Public"

However, drives created this way are only available to PowerShell session where they're
created. To map a drive that's available outside of PowerShell (or to other PowerShell sessions),
you must use the Persist parameter.

  PowerShell

  New-PSDrive -Persist -Name "X" -PSProvider "FileSystem" -Root "\\Server01\Public"

  ７ Note

  Persistently mapped drives may not be available when running in an elevated context. This
  is the default behavior of Windows UAC. For more information, see the following article:

         Mapped drives aren't available from an elevated prompt when UAC is configured
         to Prompt for credentials

 Last updated on 03/24/2025

<!-- p.539 -->

Working with software installations
Article • 03/17/2023

Applications installed with the Windows Installer can be found through WMI's queries,
but not all applications use the Windows Installer. The specific techniques for find
applications installed with other tools depends on the installer software.

For example, applications installed by copying the files to a folder on the computer
usually can't be managed using techniques discussed here. You can manage these
applications as files and folders using the techniques discussed in Working With Files
and Folders.

For software installed using an installer package, the Windows Installer can be found
using the Win32Reg_AddRemovePrograms or the Win32_Product classes. However,
both of these have problems. The Win32Reg_AddRemovePrograms is only available if
you are using System Center Configuration Manager (SCCM). And the Win32_Product
class can be slow and has side effects.

  Ｕ Caution

  The Win32_Product class isn't query optimized. Queries that use wildcard filters
  cause WMI to use the MSI provider to enumerate all installed products then parse
  the full list sequentially to handle the filter. This also initiates a consistency check of
  packages installed, verifying and repairing the install. The validation is a slow
  process and may result in errors in the event logs. For more information seek KB
  article 974524       .

This article provides an alternative method for finding installed software.

Querying the Uninstall registry key to find
installed software
Because most standard applications register an uninstaller with Windows, we can work
with those locally by finding them in the Windows registry. There is no guaranteed way
to find every application on a system. However, it's possible to find all programs with
listings displayed in Add or Remove Programs in the following registry key:

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall .

<!-- p.540 -->

We can find the number of installed applications by counting the number of registry
keys:

  PowerShell

  $UninstallPath = 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall'
  (Get-ChildItem -Path $UninstallPath).Count

  Output

  459

We can search this list of applications further using a variety of techniques. To display
the values of the registry values in the registry keys under Uninstall , use the
GetValue() method of the registry keys. The value of the method is the name of the

registry entry. For example, to find the display names of applications in the Uninstall
key, use the following command:

  PowerShell

  Get-ChildItem -Path $UninstallPath |
      ForEach-Object -Process { $_.GetValue('DisplayName') } |
      Sort-Object

  ７ Note

  There is no guarantee that the DisplayName values are unique.

The following example produces output similar to the Win32Reg_AddRemovePrograms
class:

  PowerShell

  Get-ChildItem $UninstallPath |
      ForEach-Object {
          $ProdID = ($_.Name -split '\\')[-1]
          Get-ItemProperty -Path "$UninstallPath\$ProdID" -ea SilentlyContinue
  |
          Select-Object -Property DisplayName, InstallDate, @{n='ProdID'; e=
  {$ProdID}}, Publisher, DisplayVersion
  } | Select-Object -First 3

<!-- p.541 -->

For the sake of brevity, this example uses Select-Object to limit the number of items
returned to three.

  Output

  DisplayName    : 7-Zip 22.01 (x64)
  InstallDate    :
  ProdID         : 7-Zip
  Publisher      : Igor Pavlov
  DisplayVersion : 22.01

  DisplayName    : AutoHotkey 1.1.33.10
  InstallDate    :
  ProdID         : AutoHotkey
  Publisher      : Lexikos
  DisplayVersion : 1.1.33.10

  DisplayName    : Beyond Compare 4.4.6
  InstallDate    : 20230310
  ProdID         : BeyondCompare4_is1
  Publisher      : Scooter Software
  DisplayVersion : 4.4.6.27483

<!-- p.542 -->

Decode a PowerShell command from a
running process
  This sample only runs on Windows platforms.

At times, you may have a PowerShell process running that's taking up a large amount of
resources. This process could be running in the context of a Task Scheduler job or a SQL Server
Agent job. Where there are multiple PowerShell processes running, it can be difficult to know
which process represents the problem. This article shows how to decode a script block that a
PowerShell process is currently running.

Create a long running process
To demonstrate this scenario, open a new PowerShell window and run the following code. It
executes a PowerShell command that outputs a number every minute for 10 minutes.

 PowerShell

 powershell.exe -Command {
     $i = 1
     while ( $i -le 10 )
     {
         Write-Output -InputObject $i
         Start-Sleep -Seconds 60
         $i++
     }
 }

View the process
The body of the command that PowerShell is executing is stored in the CommandLine
property of the Win32_Process class. If the command is an encoded command, the
CommandLine property contains the string "EncodedCommand". Using this information, the
encoded command can be de-obfuscated via the following process.

Start PowerShell as Administrator. It's vital that PowerShell is running as administrator,
otherwise no results are returned when querying the running processes.

<!-- p.543 -->

Execute the following command to get all the PowerShell processes that have an encoded
command:

 PowerShell

 $powerShellProcesses = Get-CimInstance -ClassName Win32_Process -Filter
 'CommandLine LIKE "%EncodedCommand%"'

The following command creates a custom PowerShell object that contains the process ID and
the encoded command.

 PowerShell

 $commandDetails = $powerShellProcesses | Select-Object -Property ProcessId,
 @{
     Name       = 'EncodedCommand'
     Expression = {
         if ( $_.CommandLine -match 'encodedCommand (.*) -inputFormat' )
         {
             return $Matches[1]
         }
     }
 }

Now the encoded command can be decoded. The following snippet iterates over the
command details object, decodes the encoded command, and adds the decoded command
back to the object for further investigation.

 PowerShell

 $commandDetails | ForEach-Object -Process {
     # Get the current process
     $currentProcess = $_

     # Convert the Base 64 string to a Byte Array
     $commandBytes =
 [System.Convert]::FromBase64String($currentProcess.EncodedCommand)

      # Convert the Byte Array to a string
      $decodedCommand = [System.Text.Encoding]::Unicode.GetString($commandBytes)

     # Add the decoded command back to the object
     $commandDetails |
         Where-Object -FilterScript { $_.ProcessId -eq $currentProcess.ProcessId } |
         Add-Member -MemberType NoteProperty -Name DecodedCommand -Value
 $decodedCommand
 }
 $commandDetails[0] | Format-List -Property *

<!-- p.544 -->

The decoded command can now be reviewed by selecting the decoded command property.

 Output

 ProcessId      : 8752
 EncodedCommand :
 IAAKAAoACgAgAAoAIAAgACAAIAAkAGkAIAA9ACAAMQAgAAoACgAKACAACgAgACAAIAAgAHcAaABpAGwAZQA
 gACgAIAAkAGkAIAAtAG

 wAZQAgADEAMAAgACkAIAAKAAoACgAgAAoAIAAgACAAIAB7ACAACgAKAAoAIAAKACAAIAAgACAAIAAgACAAI
 ABXAHIAaQB0AGUALQBP

 AHUAdABwAHUAdAAgAC0ASQBuAHAAdQB0AE8AYgBqAGUAYwB0ACAAJABpACAACgAKAAoAIAAKACAAIAAgACA
 AIAAgACAAIABTAHQAYQ

 ByAHQALQBTAGwAZQBlAHAAIAAtAFMAZQBjAG8AbgBkAHMAIAA2ADAAIAAKAAoACgAgAAoAIAAgACAAIAAgA
 CAAIAAgACQAaQArACsA
                  IAAKAAoACgAgAAoAIAAgACAAIAB9ACAACgAKAAoAIAAKAA==
 DecodedCommand :
                      $i = 1
                      while ( $i -le 10 )
                      {
                          Write-Output -InputObject $i
                          Start-Sleep -Seconds 60
                          $i++
                      }

Last updated on 03/24/2025

<!-- p.545 -->

Redirecting output
PowerShell provides several cmdlets that let you control data output directly. These cmdlets
share two important characteristics.

First, they generally transform data to some form of text. They do this because they output the
data to system components that require text input. This means they need to represent the
objects as text. Therefore, the text is formatted as you see it in the PowerShell console window.

Second, these cmdlets use the PowerShell verb Out because they send information out from
PowerShell to somewhere else.

Console output
By default, PowerShell sends data to the host window, which is exactly what the Out-Host
cmdlet does. The primary use for the Out-Host cmdlet is paging. For example, the following
command uses Out-Host to page the output of the Get-Command cmdlet:

  PowerShell

  Get-Command | Out-Host -Paging

The host window display is outside of PowerShell. This is important because when data is sent
out of PowerShell, it's actually removed. You can see this if you try to create a pipeline that
pages data to the host window, and then attempt to format it as a list, as shown here:

  PowerShell

  Get-Process | Out-Host -Paging | Format-List

You might expect the command to display pages of process information in list format. Instead,
it displays the default tabular list:

  Output

  Handles    NPM(K)      PM(K)          WS(K) VM(M)   CPU(s)     Id ProcessName
  -------    ------      -----          ----- -----   ------     -- -----------
      101         5       1076           3316    32     0.05   2888 alg
  ...
      618         18     39348          51108   143   211.20    740 explorer
      257          8      9752          16828    79     3.02   2560 explorer

<!-- p.546 -->

 ...
 <SPACE> next page; <CR> next line; Q quit
 ...

The Out-Host cmdlet sends the data directly to the console, so the Format-List command
never receives anything to format.

The correct way to structure this command is to put the Out-Host cmdlet at the end of the
pipeline as shown below. This causes the process data to be formatted in a list before being
paged and displayed.

 PowerShell

 Get-Process | Format-List | Out-Host -Paging

 Output

 Id      : 2888
 Handles : 101
 CPU     : 0.046875
 Name    : alg
 ...

 Id      : 740
 Handles : 612
 CPU     : 211.703125
 Name    : explorer

 Id      : 2560
 Handles : 257
 CPU     : 3.015625
 Name    : explorer
 ...
 <SPACE> next page; <CR> next line; Q quit
 ...

This applies to all of the Out cmdlets. An Out cmdlet should always appear at the end of the
pipeline.

  ７ Note

  All the Out cmdlets render output as text, using the formatting in effect for the console
  window, including line length limits.

Discarding output

<!-- p.547 -->

The Out-Null cmdlet is designed to immediately discard any input it receives. This is useful for
discarding unnecessary data that you get as a side-effect of running a command. When type
the following command, you don't get anything back from the command:

 PowerShell

 Get-Command | Out-Null

The Out-Null cmdlet doesn't discard error output. For example, if you enter the following
command, a message is displayed informing you that PowerShell doesn't recognize Is-
NotACommand :

 PS> Get-Command Is-NotACommand | Out-Null
 Get-Command : 'Is-NotACommand' isn't recognized as a cmdlet, function, operable
 program, or script file.
 At line:1 char:12
 + Get-Command <<<< Is-NotACommand | Out-Null

Printing data
  Out-Printer is only available on Windows platforms.

You can print data using the Out-Printer cmdlet. The Out-Printer cmdlet uses your default
printer if you don't provide a printer name. You can use any Windows-based printer by
specifying its display name. There is no need for any kind of printer port mapping or even a
real physical printer. For example, if you have the Microsoft Office document imaging tools
installed, you can send the data to an image file by typing:

 PowerShell

 Get-Command -Name Get-* | Out-Printer -Name 'Microsoft Office Document Image
 Writer'

Saving data
You can send output to a file instead of the console window using the Out-File cmdlet. The
following command line sends a list of processes to the file C:\temp\processlist.txt :

 PowerShell

<!-- p.548 -->

 Get-Process | Out-File -FilePath C:\temp\processlist.txt

The results of using the Out-File cmdlet may not be what you expect if you are used to
traditional output redirection. To understand its behavior, you must be aware of the context in
which the Out-File cmdlet operates.

On Window PowerShell 5.1, the Out-File cmdlet creates a Unicode file. Some tools, that
expect ASCII files, don't work correctly with the default output format. You can change the
default output format to ASCII using the Encoding parameter:

 PowerShell

 Get-Process | Out-File -FilePath C:\temp\processlist.txt -Encoding ascii

Out-File formats file contents to look like console output. This causes the output to be

truncated just as it's in a console window in most circumstances. For example, if you run the
following command:

 PowerShell

 Get-Command | Out-File -FilePath C:\temp\output.txt

The output will look like this:

 Output

 CommandType        Name                               Definition
 -----------        ----                               ----------
 Cmdlet             Add-Content                        Add-Content [-Path] <String[...
 Cmdlet             Add-History                        Add-History [[-InputObject] ...
 ...

To get output that doesn't force line wraps to match the screen width, you can use the Width
parameter to specify line width. Because Width is a 32-bit integer parameter, the maximum
value it can have is 2147483647. Type the following to set the line width to this maximum
value:

 PowerShell

 Get-Command | Out-File -FilePath C:\temp\output.txt -Width 2147483647

<!-- p.549 -->

The Out-File cmdlet is most useful when you want to save output as it would have displayed
on the console.

Last updated on 03/24/2025

<!-- p.550 -->

Using Format commands to change output
view
PowerShell has a set of cmdlets that allow you to control how properties are displayed for
particular objects. The names of all the cmdlets begin with the verb Format . They let you select
which properties you want to show.

 PowerShell

 Get-Command -Verb Format -Module Microsoft.PowerShell.Utility

 Output

 CommandType       Name                   Version    Source
 -----------       ----                   -------    ------
 Cmdlet            Format-Custom          6.1.0.0    Microsoft.PowerShell.Utility
 Cmdlet            Format-Hex             6.1.0.0    Microsoft.PowerShell.Utility
 Cmdlet            Format-List            6.1.0.0    Microsoft.PowerShell.Utility
 Cmdlet            Format-Table           6.1.0.0    Microsoft.PowerShell.Utility
 Cmdlet            Format-Wide            6.1.0.0    Microsoft.PowerShell.Utility

This article describes the Format-Wide , Format-List , and Format-Table cmdlets.

Each object type in PowerShell has default properties that are used when you don't select the
properties to display. Each cmdlet uses the same Property parameter to specify which
properties you want displayed. Because Format-Wide only shows a single property, its Property
parameter only takes a single value, but the Property parameter of Format-List and Format-
Table accepts a list of property names.

In this example, the default output of Get-Process cmdlet shows that we've two instances of
Internet Explorer running.

 PowerShell

 Get-Process -Name iexplore

The default format for Process objects displays the properties shown here:

 Output

<!-- p.551 -->

   NPM(K)     PM(M)        WS(M)      CPU(s)        Id   SI ProcessName
   ------     -----        -----      ------        --   -- -----------
       32     25.52        10.25       13.11     12808    1 iexplore
       52     11.46        26.46        3.55     21748    1 iexplore

Using Format-Wide for single-item output
The Format-Wide cmdlet, by default, displays only the default property of an object. The
information associated with each object is displayed in a single column:

 PowerShell

 Get-Command -Verb Format | Format-Wide

 Output

 Format-Custom              Format-Hex
 Format-List                Format-Table
 Format-Wide

You can also specify a non-default property:

 PowerShell

 Get-Command -Verb Format | Format-Wide -Property Noun

 Output

 Custom                     Hex
 List                       Table
 Wide

Controlling Format-Wide display with column
With the Format-Wide cmdlet, you can only display a single property at a time. This makes it
useful for displaying large lists in multiple columns.

 PowerShell

 Get-Command -Verb Format | Format-Wide -Property Noun -Column 3

 Output

<!-- p.552 -->

 Custom                    Hex                    List
 Table                     Wide

Using Format-List for a list view
The Format-List cmdlet displays an object in the form of a listing, with each property labeled
and displayed on a separate line:

 PowerShell

 Get-Process -Name iexplore | Format-List

 Output

 Id      : 12808
 Handles : 578
 CPU     : 13.140625
 SI      : 1
 Name    : iexplore

 Id      : 21748
 Handles : 641
 CPU     : 3.59375
 SI      : 1
 Name    : iexplore

You can specify as many properties as you want:

 PowerShell

 Get-Process -Name iexplore | Format-List -Property
 ProcessName,FileVersion,StartTime,Id

 Output

 ProcessName : iexplore
 FileVersion : 11.00.18362.1 (WinBuild.160101.0800)
 StartTime   : 10/22/2019 11:23:58 AM
 Id          : 12808

 ProcessName : iexplore
 FileVersion : 11.00.18362.1 (WinBuild.160101.0800)
 StartTime   : 10/22/2019 11:23:57 AM
 Id          : 21748

<!-- p.553 -->

Getting detailed information using Format-List with wildcards
The Format-List cmdlet lets you use a wildcard as the value of its Property parameter. This lets
you display detailed information. Often, objects include more information than you need,
which is why PowerShell doesn't show all property values by default. To show all properties of
an object, use the Format-List -Property * command. The following command generates
more than 60 lines of output for a single process:

 PowerShell

 Get-Process -Name iexplore | Format-List -Property *

Although the Format-List command is useful for showing detail, if you want an overview of
output that includes many items, a simpler tabular view is often more useful.

Using Format-Table for tabular output
If you use the Format-Table cmdlet with no property names specified to format the output of
the Get-Process command, you get exactly the same output as you do without a Format
cmdlet. By default, PowerShell displays Process objects in a tabular format.

 PowerShell

 Get-Service -Name win* | Format-Table

 Output

 Status    Name               DisplayName
 ------    ----               -----------
 Running   WinDefend          Windows Defender Antivirus Service
 Running   WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
 Running   Winmgmt            Windows Management Instrumentation
 Running   WinRM              Windows Remote Management (WS-Manag...

  ７ Note

  Get-Service is only available on Windows platforms.

Improving Format-Table output

<!-- p.554 -->

Although a tabular view is useful for displaying lots of information, it may be difficult to
interpret if the display is too narrow for the data. In the previous example, the output is
truncated. If you specify the AutoSize parameter when you run the Format-Table command,
PowerShell calculates column widths based on the actual data displayed. This makes the
columns readable.

 PowerShell

 Get-Service -Name win* | Format-Table -AutoSize

 Output

 Status Name                 DisplayName
 ------ ----                 -----------
 Running WinDefend           Windows Defender Antivirus Service
 Running WinHttpAutoProxySvc WinHTTP Web Proxy Auto-Discovery Service
 Running Winmgmt             Windows Management Instrumentation
 Running WinRM               Windows Remote Management (WS-Management)

The Format-Table cmdlet might still truncate data, but it only truncates at the end of the
screen. Properties, other than the last one displayed, are given as much size as they need for
their longest data element to display correctly.

 PowerShell

 Get-Service -Name win* |
     Format-Table -Property Name, Status, StartType, DisplayName, DependentServices
 -AutoSize

 Output

 Name                     Status StartType DisplayName
 DependentServi
                                                                                               ces
 ----                 ------ --------- -----------                                             ---
 -----------
 WinDefend           Running Automatic Windows Defender Antivirus Service        {}
 WinHttpAutoProxySvc Running    Manual WinHTTP Web Proxy Auto-Discovery Service
 {NcaSvc, iphl…
 Winmgmt             Running Automatic Windows Management Instrumentation
 {vmms, TPHKLO…
 WinRM               Running Automatic Windows Remote Management (WS-Management) {}

The Format-Table command assumes that properties are listed in order of importance. The
cmdlet attempts to fully display the properties nearest the beginning. If the Format-Table

<!-- p.555 -->

command can't display all the properties, it removes some columns from the display. You can
see this behavior in the DependentServices property previous example.

Wrapping Format-Table output in columns
You can force lengthy Format-Table data to wrap within its display column using the Wrap
parameter. Using the Wrap parameter may not do what you expect, since it uses default
settings if you don't also specify AutoSize:

 PowerShell

 Get-Service -Name win* |
     Format-Table -Property Name, Status, StartType, DisplayName, DependentServices
 -Wrap

 Output

 Name                    Status StartType DisplayName
 DependentServi
                                                                                            ces
 ----                 ------ --------- -----------                                          ---
 -----------
 WinDefend           Running Automatic Windows Defender Antivirus Service                   {}
 WinHttpAutoProxySvc Running    Manual WinHTTP Web Proxy Auto-Discovery Service
 {NcaSvc,

 iphlpsvc}
 Winmgmt                Running Automatic Windows Management Instrumentation
 {vmms,

 TPHKLOAD,

 SUService,

 smstsmgr…}
 WinRM                  Running Automatic Windows Remote Management (WS-Management) {}

Using the Wrap parameter by itself doesn't slow down processing very much. However, using
AutoSize to format a recursive file listing of a large directory structure can take a long time and
use lots of memory before displaying the first output items.

If you aren't concerned about system load, then AutoSize works well with the Wrap parameter.
The initial columns still use as much width as needed to display items on one line, but the final
column is wrapped, if necessary.

<!-- p.556 -->

  ７ Note

  Some columns may not be displayed when you specify the widest columns first. For best
  results, specify the smallest data elements first.

In the following example, we specify the widest properties first.

 PowerShell

 Get-Process -Name iexplore |
     Format-Table -Wrap -AutoSize -Property FileVersion, Path, Name, Id

Even with wrapping, the final Id column is omitted:

 Output

 FileVersion                                Path
 Nam

 e
 -----------                          ----
 ---
 11.00.18362.1 (WinBuild.160101.0800) C:\Program Files (x86)\Internet
 Explorer\IEXPLORE.EXE iex

 plo

 re
 11.00.18362.1 (WinBuild.160101.0800) C:\Program Files\Internet
 Explorer\iexplore.exe       iex

 plo

 re

Organizing table output
Another useful parameter for tabular output control is GroupBy. Longer tabular listings in
particular may be hard to compare. The GroupBy parameter groups output based on a
property value. For example, we can group services by StartType for easier inspection, omitting
the StartType value from the property listing:

 PowerShell

 Get-Service -Name win* | Sort-Object StartType | Format-Table -GroupBy StartType

<!-- p.557 -->

 Output

    StartType: Automatic
 Status   Name               DisplayName
 ------   ----               -----------
 Running WinDefend           Windows Defender Antivirus Service
 Running Winmgmt             Windows Management Instrumentation
 Running WinRM               Windows Remote Management (WS-Managem…

    StartType: Manual
 Status   Name              DisplayName
 ------   ----              -----------
 Running WinHttpAutoProxyS… WinHTTP Web Proxy Auto-Discovery Serv…

Last updated on 03/24/2025

<!-- p.558 -->

Managing current location
When navigating folder systems in File Explorer, you usually have a specific working location -
namely, the current open folder. Items in the current folder can be manipulated easily by
clicking them. For command-line interfaces such as Cmd.exe, when you are in the same folder
as a particular file, you can access it by specifying a relatively short name, rather than needing
to specify the entire path to the file. The current directory is called the working directory.

PowerShell uses the noun Location to refer to the working directory, and implements a family
of cmdlets to examine and manipulate your location.

Getting your current location (Get-Location)
To determine the path of your current directory location, enter the Get-Location command:

 PowerShell

 Get-Location

 Output

 Path
 ----
 C:\Documents and Settings\PowerUser

  ７ Note

  The Get-Location cmdlet is similar to the pwd command in the BASH shell. The Set-
  Location cmdlet is similar to the cd command in Cmd.exe.

Setting your current location (Set-Location)
The Get-Location command is used with the Set-Location command. The Set-Location
command allows you to specify your current directory location.

 PowerShell

 Set-Location -Path C:\Windows

<!-- p.559 -->

After you enter the command, notice that you don't receive any direct feedback about the
effect of the command. Most PowerShell commands that perform an action produce little or no
output because the output isn't always useful. To verify that a successful directory change has
occurred when you enter the Set-Location command, include the PassThru parameter when
you enter the Set-Location command:

 PowerShell

 Set-Location -Path C:\Windows -PassThru

 Output

 Path
 ----
 C:\WINDOWS

The PassThru parameter can be used with many Set commands in PowerShell to return
information about the result for cases in which there is no default output.

You can specify paths relative to your current location in the same way as you would in most
Unix and Windows command shells. In standard notation for relative paths, a period ( . )
represents your current folder, and a doubled period ( .. ) represents the parent directory of
your current location.

For example, if you are in the C:\Windows folder, a period ( . ) represents C:\Windows and
double periods ( .. ) represent C: . You can change from your current location to the root of
the C: drive by typing:

 PowerShell

 Set-Location -Path .. -PassThru

 Output

 Path
 ----
 C:\

The same technique works on PowerShell drives that aren't file system drives, such as HKLM: .
You can set your location to the HKLM\Software key in the registry by typing:

 PowerShell

<!-- p.560 -->

 Set-Location -Path HKLM:\SOFTWARE -PassThru

 Output

 Path
 ----
 HKLM:\SOFTWARE

You can then change the directory location to the parent directory, using a relative path:

 PowerShell

 Set-Location -Path .. -PassThru

 Output

 Path
 ----
 HKLM:\

You can type Set-Location or use any of the built-in PowerShell aliases for Set-Location ( cd ,
chdir , sl ). For example:

 PowerShell

 cd -Path C:\Windows

 PowerShell

 chdir -Path .. -PassThru

 PowerShell

 sl -Path HKLM:\SOFTWARE -PassThru

Saving and recalling recent locations (Push-
Location and Pop-Location)
When changing locations, it's helpful to keep track of where you have been and to be able to
return to your previous location. The Push-Location cmdlet in PowerShell creates an ordered
