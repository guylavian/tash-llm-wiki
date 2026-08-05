---
title: "Exchange Server — pages 521-560"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0521-0560
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0521-0560
family: exchange
documentKind: "doc"
abstract: "Console Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /role:Mailbox /AnswerFile:c:\\ExchangeConfig.txt This example uses the domain controller named DC01 to read from and write to Active Directory while installing the Mailbox server role and the mana"
---

# Exchange Server — pages 521-560

<!-- p.521 -->

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /role:Mailbox /AnswerFile:c:\ExchangeConfig.txt

     This example uses the domain controller named DC01 to read from and write to Active Directory while installing the Mailbox server role and
     the management tools on the local server.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /role:Mailbox /DomainController:DC01

     This example updates Exchange Setup with patches from the specified folder, and then installs the Mailbox server role and the management
     tools on the local server. In Exchange 2016 only, if any UM language packs are located in this folder, the language packs are automatically
     installed.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /role:Mailbox /UpdatesDir:"C:\ExchangeServer\New Patches"

Install Edge Transport servers in unattended mode
     This example installs the Edge Transport server role and the management tools in the default location on the local server.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /r:EdgeTransport

     This example installs the Edge Transport server role and the management tools in the specified folder on the local server.

       Console

        Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /mode:Install /r:ET /TargetDir:"D:\Exchange Server"

Uninstall Exchange from servers in unattended mode
This example completely removes Exchange from the local server and removes the server's Exchange configuration from Active Directory.

  Console

  Setup.exe /mode:Uninstall

Remove provisioned Exchange server objects from Active Directory in
unattended mode
This example removes the provisioned Exchange server object named Exchange03 from Active Directory before Exchange is installed on the server
(if Exchange is already installed on the server, the command won't work).

  Console

  Setup.exe /rprs:Exchange03

For more information, see Delegate the installation of Exchange servers.

Add and remove UM language packs from existing Exchange 2016 Mailbox
servers in unattended mode

  ７ Note

  These procedures aren't available in Exchange 2019.

<!-- p.522 -->

  This example installs the Russian and Spain Spanish language packs on the local Exchange 2016 Mailbox server from the specified folder.

    Console

    Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /AddUmLanguagePack:ru-RU,es-ES /SourceDir:"D:\UM Language
    Packs"

  This example uninstalls the Korean UM language pack from the local Exchange 2016 Mailbox server.

    Console

    Setup.exe   /RemoveUmLanguagePack:ko-KR

Next steps
  To verify that you've successfully installed Exchange in unattended mode, see Verify Exchange Server installations.

  Complete your deployment by performing the tasks provided in Exchange post-installation tasks.

  Having problems? Ask for help in the Exchange forums. Visit the forums at Exchange Server     .

<!-- p.523 -->

Delegate the installation of Exchange
servers
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

In large companies, people who install and configure new Windows servers often aren't
Exchange administrators. In Exchange 2016 and Exchange 2019, these users can still install
Exchange on Windows servers, but only after an Exchange administrator provisions the
Exchange server object in Active Directory. Provisioning an Exchange server object makes all of
the required Active Directory changes independently of the actual installation of Exchange on a
server. An Exchange administrator can provision a new Exchange server object hours or even
days before Exchange is installed.

After an Exchange administrator provisions the Exchange server object, the only requirement
for installing Exchange on the server is membership in the Delegated Setup role group, which
allows members to install Exchange on provisioned servers. If this sounds like something you
want to do, then this topic is for you.

What do you need to know before you begin?
      Estimated time to complete this procedure: Less than 10 minutes.

      You can only provision an Exchange server from the command line (Unattended Setup).
      You can't use the Exchange Setup wizard.

      You can't provision the first Exchange server object in your organization for the
      installation of Exchange by a delegate. An Exchange administrator needs to install the first
      Exchange server in the organization. After that, you can provision additional Exchange
      server objects so users who aren't Exchange administrators can install Exchange using
      delegated setup.

      A delegated user can't uninstall an Exchange server. To uninstall an Exchange server, you
      need to be an Exchange administrator.

      Download and use the latest available release of Updates for Exchange Server.

      To provision an Exchange server object, you need to be a member of the Organization
      Management role group.

      You can provision the Exchange server object in Active Directory from the target server
      itself, or from another computer.

<!-- p.524 -->

   Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
   Server   , Exchange Online    , or Exchange Online Protection   .

Use the Command Prompt to provision Exchange
2019 servers
 1. In File Explorer, right-click on the Exchange ISO image file that you downloaded, and then
   select Mount. Note the virtual DVD drive letter that's assigned.

 2. Open a Windows Command Prompt window. For example:

        Press the Windows key + 'R' to open the Run dialog, type cmd.exe, and then press
        OK.

        Press Start. In the Search box, type Command Prompt, then in the list of results,
        select Command Prompt.

 3. In the Command Prompt window, use the following syntax:

     ７ Note

            The previous /IAcceptExchangeServerLicenseTerms switch will not work starting
            with the September 2021 Cumulative Updates (CUs). You now must use either
            /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
            /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and
            scripted installs.

            The examples below use the
            /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you to
            change the switch to /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

     Console

     <Virtual DVD drive letter>:\Setup.exe
     /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /NewProvisionedServer[:
     <ServerName>]

   If you run the command on the target server, you can use the /NewProvisionedServer
   switch by itself. Otherwise, you need to specify the Name of the server to provision.

<!-- p.525 -->

     This example uses the Exchange installation files on drive E: to provision the server
     Mailbox01:

        Console

        E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
        /NewProvisionedServer:Mailbox01

     This example uses the Exchange installation files on drive E: to provision the local server
     where you're running the command:

        Console

        E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
        /NewProvisionedServer

     Note: To remove a provisioned Exchange server object from Active Directory before
     Exchange is installed on it, replace the /NewProvisionedServer switch with
     /RemoveProvisionedServer.

   4. Add the appropriate users to the Delegated Setup role group so they can install Exchange
     on the provisioned server. To add users to a role group, see Add members to a role
     group. The delegates can use the procedures in Install Exchange Mailbox servers using
     the Setup wizard to install Exchange on the provisioned server.

How do you know this worked?
To verify that you've successfully provisioned an Exchange server for a delegate installation of
Exchange, do the following steps:

   1. In Active Directory Users & Computers, select Microsoft Exchange Security Groups,
     double-click Exchange Servers, and then select the Members tab.

   2. On the Members tab, verify that the provisioned server is a member of the security
     group. A member of the Delegated Setup role group can now install Exchange on the
     server.

If your server is listed as a member of the Exchange Servers security group, it was properly
provisioned. Someone who's a member of the Delegated Setup role group can now install
Exchange on that server.

Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server         .

<!-- p.526 -->

More information
An Exchange administrator might need to complete the deployment by performing the tasks
provided in Exchange post-installation tasks.

The high-level Active Directory changes that are made when you provision an Exchange server
object are described in the following list:

     A server object is created in the CN=Servers,CN=Exchange Administrative Group
     (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=<Organization
     Name>,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=<Root Domain>
     configuration partition.

     The following access control entries (ACEs) are added to the server object within the
     configuration partition for the Delegated Setup role group:

        Full Control on the server object and its child objects

        Deny access control entry for the Send As extended right

        Deny access control entry for the Receive As extended right

        Deny CreateChild and DeleteChild permissions for Exchange Public Folder Store
        objects

        Note: Public folders are administered at an organizational level; therefore, the creation
        and deletion of public folder stores is restricted to Exchange administrators.

     The Active Directory computer account for the server is added to the Exchange Servers
     group.

     The server is added as a provisioned server in the Exchange admin center (EAC).

Only members of the Organization Management role group in Exchange have the permissions
required to make these changes to Active Directory.

<!-- p.527 -->

Exchange dev/test environments in Azure
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

This topic steps you through creating an Exchange 2016 or Exchange 2019 dev/test
deployment in Microsoft Azure. Here is the resulting configuration.

This configuration consists of a single Exchange server and a Windows Server Active Directory
(AD) domain controller in a subnet of an Azure virtual network. This provides a basis and
common starting point from which you can demonstrate Exchange and develop Exchange
Server applications. This configuration is only for internal email and application testing on the
Exchange server. No external email flow is configured.

There are three major phases to setting up this dev/test environment:

   1. Set up the virtual network and domain controller (adVM).
   2. Add the Exchange server (exVM).
   3. Configure Exchange.

If you don't already have an Azure subscription, you can sign up for an Azure Free Trial    . If
you have an MSDN or Visual Studio subscription, see Monthly Azure credit for Visual Studio
subscribers    .

  ７ Note

  Because Exchange makes changes to the schema in Windows Server AD, this configuration
  cannot use Microsoft Entra Domain Services.

<!-- p.528 -->

Phase 1: Deploy the virtual network and a domain
controller
You can create a new Azure virtual network with a domain controller with Azure PowerShell.
You can run the following PowerShell commands from a Windows PowerShell command
prompt or in the PowerShell Integrated Script Environment (ISE). If you have not installed Azure
PowerShell, see Get started with Azure PowerShell cmdlets.

  ７ Note

  These commands are for Azure PowerShell 1.0.0 and later.

   1. Sign into your Azure account.

       PowerShell

        Connect-AzAccount

   2. Get your subscription name using the following command.

       PowerShell

        Get-AZSubscription | Sort-Object Name | Select-Object Name

   3. Set your Azure subscription with the following commands. Set the $subscrName variable
     by replacing everything within the quotes, including the < and > characters, with the
     correct name.

       PowerShell

        $subscrName="<subscription name>"

        Select-AzSubscription -SubscriptionName $subscrName

   4. Create a new resource group. To determine a unique resource group name, use this
     command to list your existing resource groups.

       PowerShell

        Get-AZResourceGroup | Sort-Object ResourceGroupName | Select-Object
        ResourceGroupName

<!-- p.529 -->

  Create your new resource group with these commands. Set the variables by replacing
  everything within the quotes, including the < and > characters, with the correct names.

    PowerShell

    $rgName="<resource group name>"

    $locName="<location name, such as West US>"

    New-AZResourceGroup -Name $rgName -Location $locName

5. Resource Manager-based virtual machines require a Resource Manager-based storage
  account. You must pick a globally unique name for your storage account that contains
  only lowercase letters and numbers. You can use this command to list the existing storage
  accounts.

    PowerShell

    Get-AZStorageAccount | Sort-Object StorageAccountName | Select-Object
    StorageAccountName

  Use this command to test whether a proposed storage account name is unique.

    PowerShell

    Get-AZStorageAccountNameAvailability "<proposed name>"

  Create a new storage account for your new test environment with these commands.

    PowerShell

    $saName = "<storage account name>"

    New-AZStorageAccount -Name $saName -ResourceGroupName $rgName -Type
    Standard_LRS -Location $locName

6. Create the EXSrvrVnet Azure Virtual Network that will host the EXSrvrSubnet subnet and
  protect it with a network security group.

    PowerShell

    $exSubnet=New-AZVirtualNetworkSubnetConfig -Name EXSrvrSubnet -AddressPrefix
    10.0.0.0/24

    New-AZVirtualNetwork -Name EXSrvrVnet -ResourceGroupName $rgName -Location
    $locName -AddressPrefix 10.0.0.0/16 -Subnet $exSubnet -DNSServer 10.0.0.4

<!-- p.530 -->

    $rule1 = New-AZNetworkSecurityRuleConfig -Name "RDPTraffic" -Description
    "Allow RDP to all VMs on the subnet" -Access Allow -Protocol Tcp -Direction
    Inbound -Priority 100 -SourceAddressPrefix Internet -SourcePortRange * -
    DestinationAddressPrefix * -DestinationPortRange 3389

    $rule2 = New-AZNetworkSecurityRuleConfig -Name "ExchangeSecureWebTraffic" -
    Description "Allow HTTPS to the Exchange server" -Access Allow -Protocol Tcp
    -Direction Inbound -Priority 101 -SourceAddressPrefix Internet -
    SourcePortRange * -DestinationAddressPrefix "10.0.0.5/32" -
    DestinationPortRange 443

    New-AZNetworkSecurityGroup -Name EXSrvrSubnet -ResourceGroupName $rgName -
    Location $locName -SecurityRules $rule1, $rule2

    $vnet=Get-AZVirtualNetwork -ResourceGroupName $rgName -Name EXSrvrVnet

    $nsg=Get-AZNetworkSecurityGroup -Name EXSrvrSubnet -ResourceGroupName $rgName

    Set-AZVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name EXSrvrSubnet -
    AddressPrefix "10.0.0.0/24" -NetworkSecurityGroup $nsg

    $vnet | Set-AzVirtualNetwork

7. Create the adVM virtual machine in Azure. adVM is a domain controller for the
  corp.contoso.com Windows Server AD domain and a DNS server for the virtual machines
  of the EXSrvrVnet virtual network.

  First, fill in the name of your resource group, Azure location, and storage account name
  and run these commands at the Azure PowerShell command prompt on your local
  computer to create an Azure virtual machine for adVM.

    PowerShell

    # Create an availability set for domain controller virtual machines
    New-AZAvailabilitySet -ResourceGroupName $rgName -Name dcAvailabilitySet -
    Location $locName -Sku Aligned -PlatformUpdateDomainCount 5 -
    PlatformFaultDomainCount 2

    # Create the domain controller virtual machine
    $vnet = Get-AZVirtualNetwork -Name EXSrvrVnet -ResourceGroupName $rgName

    $pip = New-AZPublicIpAddress -Name adVM-NIC -ResourceGroupName $rgName -
    Location $locName -AllocationMethod Dynamic

    $nic = New-AZNetworkInterface -Name adVM-NIC -ResourceGroupName $rgName -
    Location $locName -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id -
    PrivateIpAddress 10.0.0.4

    $avSet=Get-AZAvailabilitySet -Name dcAvailabilitySet -ResourceGroupName
    $rgName

<!-- p.531 -->

        $vm=New-AZVMConfig -VMName adVM -VMSize Standard_D1_v2 -AvailabilitySetId
        $avSet.Id

        $vm=Set-AZVMOSDisk -VM $vm -Name adVM-OS -DiskSizeInGB 128 -CreateOption
        FromImage -StorageAccountType "Standard_LRS"

        $diskConfig=New-AZDiskConfig -AccountType "Standard_LRS" -Location $locName -
        CreateOption Empty -DiskSizeGB 20

        $dataDisk1=New-AZDisk -DiskName adVM-DataDisk1 -Disk $diskConfig -
        ResourceGroupName $rgName

        $vm=Add-AZVMDataDisk -VM $vm -Name adVM-DataDisk1 -CreateOption Attach -
        ManagedDiskId $dataDisk1.Id -Lun 1

        $cred=Get-Credential -Message "Type the name and password of the local
        administrator account for adVM."

        $vm=Set-AZVMOperatingSystem -VM $vm -Windows -ComputerName adVM -Credential
        $cred -ProvisionVMAgent -EnableAutoUpdate

        $vm=Set-AZVMSourceImage -VM $vm -PublisherName MicrosoftWindowsServer -Offer
        WindowsServer -Skus 2012-R2-Datacenter -Version "latest"

        $vm=Add-AZVMNetworkInterface -VM $vm -Id $nic.Id

        New-AZVM -ResourceGroupName $rgName -Location $locName -VM $vm

     You will be prompted for a username and password. This article will refer to this username
     as ADMIN_NAME. Use a strong password and record both in a secure location.

     Note: The password that you specify cannot be "pass@word1". It must be between 8-123
     characters long and must satisfy at least 3 of the following password complexity
     requirements:

           Contains an uppercase letter
           Contains an lowercase letter
           Contains a numeric digit
           Contains a special character

It can take a few minutes for Azure to build the virtual machine.

Connect to the domain controller virtual machine using local
administrator account credentials
   1. In the Azure portal   , click Resource Groups > <your resource group name>> adVM >
     Connect.

<!-- p.532 -->

  2. Run the adVM.rdp file that is downloaded, and then click Connect.

  3. In Windows Security, click Use another account. In User name, type **adVM**
     <ADMIN_NAME>.

  4. In Password, type the password of the ADMIN_NAME account, and then click OK.

  5. When prompted, click Yes.

  6. Add an extra data disk as a new volume with the drive letter F: with these commands at
     an administrator-level Windows PowerShell command prompt on adVM.

       PowerShell

       $disk=Get-Disk | where {$_.PartitionStyle -eq "RAW"}

       $diskNumber=$disk.Number

       Initialize-Disk -Number $diskNumber

       New-Partition -DiskNumber $diskNumber -UseMaximumSize -AssignDriveLetter

       Format-Volume -DriveLetter F

  7. Configure adVM as a domain controller and DNS server for the corp.contoso.com
     domain. Run these commands at an administrator-level Windows PowerShell command
     prompt on adVM.

       PowerShell

       Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

       Install-ADDSForest -DomainName corp.contoso.com -DatabasePath "F:\NTDS" -
       SysvolPath "F:\SYSVOL" -LogPath "F:\Logs"

Note that these commands can take a few minutes to complete.

After adVM restarts, reconnect to the adVM virtual machine.

Connect to the domain controller virtual machine using
domain credentials
  1. In the Azure portal   , click Resource Groups > <the name of your new resource group>
     > adVM > Connect.

  2. Run the adVM.rdp file that is downloaded, and then click Connect.

<!-- p.533 -->

   3. In Windows Security, click Use another account. In User name, type **CORP**
     <ADMIN_NAME>.

   4. In Password, type the password of the ADMIN_NAME account, and then click OK.

   5. When prompted, click Yes.

   6. From the desktop, open an administrator-level Windows PowerShell command prompt
     and run the following command:

        PowerShell

        Add-WindowsFeature RSAT-ADDS-Tools

Here is the result of Phase 1.

Phase 2: Create the Exchange virtual machine
In this phase, you create an Exchange virtual machine in the EXSrvrVNet virtual network and
make it a member of the CORP domain.

To create the Exchange virtual machine with Azure PowerShell, first log in to Azure with your
Azure account from the Windows PowerShell command prompt (if needed).

  PowerShell

  Connect-AzAccount

You must determine a globally unique DNS name for the exVM virtual machine. You must pick
a globally unique DNS name that contains only lowercase letters and numbers. You can do this
with the following PowerShell commands:

<!-- p.534 -->

  PowerShell

  $vmDNSName="<DNS name to test>"

  $rgName="<resource group name>"

  $locName=(Get-AZResourceGroup -Name $rgName).Location

  Test-AZDnsAvailability -DomainQualifiedName $vmDNSName -Location $locName

If you see "True", your proposed name is globally unique.

Next, fill in the variable values and run the resulting block at the PowerShell prompt.

  PowerShell

  # Set up key variables
  $subscrName="<name of your Azure subscription>"

  $vmDNSName="<unique, public DNS name for the Exchange server>"

  # Set the Azure subscription
  Select-AzSubscription -SubscriptionName $subscrName

  # Get the Azure location and storage account names
  $locName=(Get-AZResourceGroup -Name $rgName).Location

  $saName=(Get-AZStorageaccount | Where {$_.ResourceGroupName -eq
  $rgName}).StorageAccountName

  # Create an availability set for Exchange virtual machines
  New-AZAvailabilitySet -ResourceGroupName $rgName -Name exAvailabilitySet -Location
  $locName -Sku Aligned -PlatformUpdateDomainCount 5 -PlatformFaultDomainCount 2

  # Specify the virtual machine name and size
  $vmName="exVM"

  $vmSize="standard_d8s_v3"

  $vnet=Get-AZVirtualNetwork -Name "EXSrvrVnet" -ResourceGroupName $rgName

  $avSet=Get-AZAvailabilitySet -Name exAvailabilitySet -ResourceGroupName $rgName

  $vm=New-AZVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avSet.Id

  # Create the NIC for the virtual machine
  $nicName=$vmName + "-NIC"

  $pipName=$vmName + "-PublicIP"

  $pip=New-AZPublicIpAddress -Name $pipName -ResourceGroupName $rgName -
  DomainNameLabel $vmDNSName -Location $locName -AllocationMethod Dynamic

<!-- p.535 -->

  $nic=New-AZNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location
  $locName -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id -
  PrivateIpAddress "10.0.0.5"

  # Create and configure the virtual machine
  $cred=Get-Credential -Message "Type the name and password of the local
  administrator account for exVM."

  $vm=Set-AZVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption
  FromImage -StorageAccountType "Standard_LRS"

  $vm=Set-AZVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential
  $cred -ProvisionVMAgent -EnableAutoUpdate

  $vm=Set-AZVMSourceImage -VM $vm -PublisherName MicrosoftWindowsServer -Offer
  WindowsServer -Skus 2019-Datacenter -Version "latest"

  $vm=Add-AZVMNetworkInterface -VM $vm -Id $nic.Id

  New-AZVM -ResourceGroupName $rgName -Location $locName -VM $vm

  ７ Note

  This command block uses a standard storage account created in phase 1 to reduce costs
  for this dev/test environment. For a production Exchange server, you must use a premium
  storage account.

From the Azure portal, connect to the exVM virtual machine using the credentials of the local
administrator account.

Next, join exVM to the Windows AD domain with these commands at a Windows PowerShell
prompt.

  PowerShell

  Add-Computer -DomainName "corp.contoso.com"
  Restart-Computer

Note that you must supply domain account credentials after entering the Add-Computer
command. Use the CORP\<ADMIN_NAME> account and password.

Here is the result of Phase 2.

<!-- p.536 -->

Phase 3: Configure Exchange
In this phase, you configure Exchange on exVM and test mail delivery between two mailboxes.

Prepare Windows Server AD
  1. At the Windows PowerShell command prompt on your local computer, run the following
     command:

       PowerShell

       Write-Host (Get-AZPublicIpaddress -Name "exVM-PublicIP" -ResourceGroup
       $rgName).DnsSettings.Fqdn

  2. Note or copy the full DNS name from the display of the command. This is the Internet
     DNS name of the exVM virtual machine. You will need this value later.

  3. If needed, connect to the adVM virtual machine with the Azure portal using the CORP\
     <ADMIN_NAME> account and password.

  4. At the Windows PowerShell command prompt, run the following command:

       PowerShell

       Get-ADForest | Set-ADForest -UPNSuffixes @{Add="<DNS Name of Exchange>"}

  5. Close the remote desktop session with adVM.

Install Exchange

<!-- p.537 -->

 1. Connect to the exVM virtual machine with the Azure portal using the CORP\
   <ADMIN_NAME> account and password.

 2. From exVM, open an administrator-level Windows PowerShell command prompt and run
   the following commands.

      PowerShell

      Install-WindowsFeature NET-Framework-45-Core, NET-Framework-45-ASPNET, NET-
      WCF-HTTP-Activation45, NET-WCF-Pipe-Activation45, NET-WCF-TCP-Activation45,
      NET-WCF-TCP-PortSharing45, RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-
      Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-Clustering-PowerShell,
      Web-Mgmt-Console, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth, Web-
      Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression, Web-
      Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing, Web-
      ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-Mgmt-
      Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-Server,
      Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-WMI, Windows-
      Identity-Foundation, RSAT-ADDS-Tools

      Restart-Computer

 3. Connect to the exVM virtual machine with the Azure portal using the CORP\
   <ADMIN_NAME> account and password.

 4. From Server Manager, click Local Server. In the Properties for exVM, click On for IE
   Enhanced Security Configuration. In Internet Explorer Enhanced Security Configuration,
   click Off for both Administrators and Users, and then click OK.

 5. From the Start screen, click Internet Explorer, and then download the Unified
   Communications Managed API 4.0 Runtime from
   https://www.microsoft.com/download/details.aspx?id=34992          . When prompted, click
   Run.

 6. When prompted with the Microsoft Unified Communications Managed API 4.0, Runtime
   Setup, click Next.

 7. Click I have read and accept the license terms, and then click Install. On the Installation
   is Complete page, click Finish.

 8. From Internet Explorer, download the latest version of Exchange. For more information,
   see Updates for Exchange Server.

 9. Click Save to store the ISO file in the Downloads folder.

10. Click Open Folder, right-click the Exchange ISO file, and then click Mount.

<!-- p.538 -->

 11. From an administrator-level Windows PowerShell command prompt on exVM, run the
       following:

  ７ Note

         The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
         the September 2021 Cumulative Updates (CUs). You now must use either
         /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
         /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
         installs.

         The examples below use the /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
         switch. It's up to you to change the switch to
         /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

  PowerShell

  e:

  .\setup.exe /mode:Install /role:Mailbox /OrganizationName:Contoso
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON
  Restart-Computer

Wait until Exchange setup completes, which can take some time, and exVM restarts.

Add two mailboxes to the Exchange server
  1. Connect to the exVM virtual machine with the Azure portal using the CORP\
       <ADMIN_NAME> account and password.

  2. From the Start screen, type Exchange, and then click Exchange Management Shell.

  3. Copy the following commands to Notepad, insert the Internet DNS name of the exVM
       virtual machine for the $dnsName variable, and then copy and paste the resulting
       commands into the Exchange Management Shell.

         PowerShell

         $dnsName="<Internet DNS name of the exVM virtual machine>"

         $user1Name="chris@" + $dnsName

         $user2Name="janet@" + $dnsName

<!-- p.539 -->

      $db=Get-MailboxDatabase

      $dbName=$db.Name

      $password = Read-Host "Enter password" -AsSecureString

 4. Record the password specified in a safe place. Next, run these commands to create two
   mailboxes.

     PowerShell

      New-Mailbox -UserPrincipalName $user1Name -Alias chris -Database $dbName -
      Name ChrisAshton -OrganizationalUnit Users -Password $password -FirstName
      Chris -LastName Ashton -DisplayName "Chris Ashton"

      New-Mailbox -UserPrincipalName $user2Name -Alias janet -Database $dbName -
      Name JanetSchorr -OrganizationalUnit Users -Password $password -FirstName
      Janet -LastName Schorr -DisplayName "Janet Schorr"

Test email delivery between mailboxes
 1. From the browser on your local computer, access the web site https://<Internet DNS
   name of the exVM virtual machine> /owa. When prompted with an error page for the
   website's security certificate, click Continue to this website. On the Outlook sign-in page,
   use the corp\chris account name with its password.

 2. When prompted to specify the language and time zone, select the appropriate value for
   each, and then click Save.

 3. From Chris Ashton's inbox, click New. In To, type janet and then click Search Directory.
   For Subject, type Test message, and then click Send.

 4. Click the user icon in the upper right part of the Mail web page, and then click Sign out.

 5. On the Outlook sign-in page, use the corp\janet account name with its password. When
   prompted to specify the language and time zone, select the appropriate value for each,
   and then click Save.

 6. Verify that the inbox contains the test message from Chris Ashton. Click it, then click
   Reply all. In the body of the message, type Replied, and then click Send.

 7. Click the user icon in the upper right part of the Mail web page, and then click Sign out.

 8. On the Outlook sign-in page, use the corp\chris account name with its password. Verify
   that the reply email message sent from Janet is in the inbox.

<!-- p.540 -->

You are now ready to test Exchange features or applications.

Stop and start the virtual machines
Azure virtual machines incur an ongoing cost when they are running. To help minimize the cost
of your Exchange dev/test environment, use these commands to stop the virtual machines:

  PowerShell

  $rgName="<your resource group name>"

  Stop-AZVM -Name exVM -ResourceGroupName $rgName -Force

  Stop-AZVM -Name adVM -ResourceGroupName $rgName -Force

To start them again, use these commands:

  PowerShell

  $rgName="<your resource group name>"

  Start-AZVM -Name adVM -ResourceGroupName $rgName

  Start-AZVM -Name exVM -ResourceGroupName $rgName

See also
Troubleshoot outbound SMTP connectivity issues in Azure

Deploy new installations of Exchange

Exchange Server system requirements

Exchange Server

What's new in Exchange Server

Cloud adoption Test Lab Guides (TLGs)

<!-- p.541 -->

Upgrade Exchange to the latest Cumulative
Update
07/01/2025

APPLIES TO:        2016      2019     Subscription Edition

If you have Exchange Server installed, you can upgrade the Exchange servers to the latest
Cumulative Update (CU). Because each CU is a full installation of Exchange that includes
updates and changes from all previous CUs, you don't need to install any previous CUs or
Exchange Server RTM first. For more information about the latest available Exchange CUs, see
Updates for Exchange Server.

  Ｕ Caution

  After you upgrade Exchange to a newer CU, you can't uninstall the new version to revert
  to the previous version. Uninstalling the new version completely removes Exchange from
  the server.

What do you need to know before you begin?
     Estimated time to complete: 180 minutes

     The account that you'll use to install the CU requires membership in the Exchange
     Organization Management role group. If the CU requires Active Directory schema
     updates or domain preparation, the account will likely require more permissions. For
     more information, see Prepare Active Directory and domains for Exchange Server.

     Check the Release notes before you install the CU.

     Verify the target server meets the potentially new system requirements and prerequisites
     for the CU. For more information, see Exchange Server system requirements and
     Exchange Server prerequisites.

       Ｕ Caution

       The following types of customized settings will be overwritten when you install an
       Exchange CU:
             Any customized Exchange or Internet Information Server (IIS) settings that you
             made in Exchange XML application configuration files on the Exchange server. For

<!-- p.542 -->

         example, web.config files or the EdgeTransport.exe.config file. Starting with
         Exchange Server 2019 CU13, the most common configuration file changes will be
         backed up and automatically restored. More information can be found here.
         Customizations to the operating system's TLS/Cipher settings.

      Be sure save this information so you can easily re-apply the settings after the install.
      After you install the Exchange CU, you need to re-configure these settings.

   After you install an Exchange CU, you need to restart the computer so that changes can
   be made to the registry and operating system.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server .

Best Practices
   Always keep your servers as up to date as possible. This especially applies to the
   installation of a new server.
   Always install the latest Cumulative Update when creating a new server.
   There's no need to install the RTM build or previous builds and then upgrade to the latest
   Cumulative Update. This is because each Cumulative Update is a full build of the product.
   Reboot the server beforehand.
   Test the new update in a non-production environment first to avoid any problems in the
   new update affecting the running production environment.
   Have a tested and working backup of both the Active Directory and your Exchange
   Server.
   Back up any and all customizations. They won't survive the update.

      ７ Note

      Exchange Server 2019 CU13 or later will back up and restore the most common
      configuration files. You can find the list of preserved configurations here.

   Use an elevated command prompt to run the Cumulative Update.
   Temporarily disable any anti-virus software during the update process.
   Reboot your server upon completion of the update.
   For exchange servers installed on database availability group, follow steps mentioned in
   Manage database availability groups in Exchange Server to put the DAG members in

<!-- p.543 -->

   maintenance mode before installing the cumulative updates.

Install an Exchange CU using the Setup wizard
 1. Download the latest version of Exchange on the target computer. For more information,
   see Updates for Exchange Server.

 2. In File Explorer, right-click on the Exchange CU ISO image file that you downloaded, and
   then select Mount. In the resulting virtual DVD drive that appears, start Exchange Setup
   by double-clicking Setup.exe .

 3. The Exchange Server Setup wizard opens. On the Check for Updates? page, choose one
   of the following options, and then click Next to continue:

        Connect to the Internet and check for updates: We recommend this option, which
        searches for updates to the version of Exchange that you're currently installing (it
        doesn't detect newer CUs). This option takes you to the Downloading Updates page
        that searches for updates. Click Next to continue.

        Don't check for updates right now

<!-- p.544 -->

4. The Copying Files page shows the progress of copying files to the local hard drive.
  Typically, the files are copied to %WinDir%\Temp\ExchangeSetup , but you can confirm the
  location in the Exchange Setup log at C:\ExchangeSetupLogs\ExchangeSetup.log .

<!-- p.545 -->

5. The Upgrade page shows that Setup detected the existing installation of Exchange, so
  you're upgrading Exchange on the server (not installing a new Exchange server). Click
  Next to continue.

6. On the License Agreement page, review the software license terms, select I accept the
  terms in the license agreement, and then click Next to continue.

<!-- p.546 -->

7. On the Readiness Checks page, verify that the prerequisite checks completed
  successfully. If they haven't, the only option on the page is Retry, so you need to resolve
  the errors before you can continue.

<!-- p.547 -->

  After you resolve the errors, click Retry to run the prerequisite checks again. You can fix
  some errors without exiting Setup, while the fix for other errors requires you to restart the
  computer. If you restart the computer, you need to start over at Step 1.

  When no more errors are detected on the Readiness Checks page, the Retry button
  changes to Install so you can continue. Be sure to review any warnings, and then click
  Install to install Exchange.

8. On the Setup Progress page, a progress bar indicates how the installation is proceeding.

<!-- p.548 -->

9. On the Setup Completed page, click Finish, and then restart the computer.

<!-- p.549 -->

Install an Exchange CU using unattended Setup
from the command line
To install an Exchange CU from the command line, use the following syntax:

  ７ Note

       The previous /IAcceptExchangeServerLicenseTerms switch will not work starting with
       the September 2021 Cumulative Updates (CUs). You now must use either
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON or
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF for unattended and scripted
       installs.

       The following examples use the
       /IAcceptExchangeServerLicenseTerms_DiagnosticDataON switch. It's up to you to
       change the switch to /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF.

  Console

  <Virtual DVD drive letter>:\Setup.exe
  /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade
  [/DomainController:<ServerFQDN>] [/EnableErrorReporting]

  ７ Note

       The optional /DomainController switch specifies the domain controller that Setup
       uses to read from a write to Active Directory.

       The optional /EnableErrorReporting switch enables Setup to automatically submit
       critical error reports to Microsoft. Microsoft uses this information to diagnose
       problems and provide solutions.

This example uses the Exchange CU files on drive E: to install the CU on the local server, and
uses the domain controller dc01.contoso.com to read from and write to Active Directory.

  Console

  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade
  /DomainController:dc01.contoso.com

<!-- p.550 -->

For more information about unattended Setup from the command line, see Install Exchange
using unattended mode.

How do you know this worked?
To verify that you've successfully installed an Exchange CU, see Verify Exchange Server
installations.

<!-- p.551 -->

Upgrading to Exchange Server Subscription
Edition (SE)
07/01/2025

APPLIES TO:       2016       2019     Subscription Edition

Exchange Server Subscription Edition (SE) is capable of operating alongside earlier versions of
Exchange Server within the same organization. Previously, organizations could run older,
including unsupported, versions of Exchange Server together with newer versions. There are
now two significant changes to this practice:

       The installation process for Exchange Server SE Release to Manufacturing (RTM) prevents
       coexistence with Exchange Server 2013.
       The setup procedure for Exchange Server SE CU2 will prohibit coexistence with any
       version of Exchange Server that is not supported at the time of release.

To upgrade Exchange Server 2016 or Exchange Server 2019 to Exchange Server SE, two
upgrade methods are available:

       Legacy upgrade: This method involves transitioning to a new major version of Exchange
       Server by adding the newer server to the organization, migrating all mailboxes and
       resources from existing servers to the new servers, and then uninstalling the previous
       servers. Legacy upgrades are necessary when moving from Exchange Server 2016 to
       Exchange Server 2019 or to Exchange Server SE, as well as when switching to new
       hardware or a newer version of Windows Server.
       In-place upgrade: Exchange Server SE supports an in-place upgrade from Exchange
       Server 2019 Cumulative Update (CU) 14 or 15. This process allows you to install Exchange
       Server SE over your existing Exchange Server 2019 installation, similar to the procedure
       for applying cumulative updates. Please adhere to the recommended steps and best
       practices outlined in the Upgrade Exchange to the latest Cumulative Update
       documentation.

The Exchange Server Deployment Assistant        guides you through the correct steps for your
specific upgrade scenario. It generates a tailored, step-by-step checklist to help you
successfully deploy Exchange Server SE in your on-premises environment.

For more context, see the blog posts Upgrading your organization from current versions to
Exchange Server SE       and Why in-place upgrade from Exchange 2019 to Exchange SE is low
risk   .

Exchange Server SE Product Key requirements

<!-- p.552 -->

Exchange Server SE RTM does not require a new product key. It will continue to function after a
legacy or in-place upgrade to Exchange Server SE. However, starting with a future cumulative
update, Exchange Server SE will introduce a new product key requirement. This documentation
will be updated with the latest requirements when they become available.

<!-- p.553 -->

Exchange Server custom configuration preservation
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Overview
After installing Exchange Server, a common admin task is to customize settings, such as client-specific message size limits. These settings are
typically configured in web.config , sharedweb.config , and other configuration files on the Exchange server.

Historically, one of the challenges for Exchange server admins is that each time a Cumulative Update (CU) is installed, these files and the custom
settings therein are overwritten by Setup, forcing an admin to back up/restore their settings, or reapply them after every CU install.

With Exchange Server 2019 CU13 and later, Setup now backs up and restores the most common configuration files so that admins no longer need
to manually restore them or reapply them.

Setup preserves custom configurations in the following way:

   1. Setup creates a backup of the existing files.
   2. Setup installs Exchange Server (or upgrades existing Exchange Server), and overwrites existing files with default configurations and settings
      present in Exchange Setup.
   3. Setup finally restores appropriate files and custom values of critical keys stored in the preupgrade configuration files in the new config files
      copied from Exchange Setup.

Setup preserves the most critical configuration settings (if present), which can include entire sections or certain key value pairs.

   1. appSettings contains many key value pairs that configure a range of application settings, (for example, logging path, message queue size,
      etc.). Any key value pair created using <add key> tag is preserved if this section is present.

      For example, in the following file, ClientTunnelExpirationTime is preserved.

        <configuration>
        <appSettings>
            <add key="ClientTunnelExpirationTime" value="30" />
        </appSettings>
        </ configuration>

   2. The entire proxySettings section is critical and is preserved.

   3. maxAllowedContentLength is used to specify the maximum length of content (in bytes) in a request.

        <system.webServer>
            <security>
            <requestFiltering>
                <requestLimits maxAllowedContentLength="4194304" />
            </requestFiltering>
            </security>
        <system.webServer>

   4. maxRequestLength is used to specify the maximum request size.

        <system.web>
            <httpRuntime maxRequestLength="4194304" />
        </system.web>

   5. maxReceivedMessageSize is used in systembinding and custombinding elements to set the maximum size (in bytes) for a message that can be
      received on a channel configured with this binding.

   6. maxStringContentLength is present in both systembinding and customBinding elements and is used to limit the maximum string size that the
      XML reader returns.

<!-- p.554 -->

     7. extendedProtectionPolicy is used to set the extended protection policy, which is used by the server to validate incoming client connections.

     8. defaultProxy is used to configure the HTTP proxy server.

List of preserved config files along with sections and keys
preserved
Here's the list of all the config files along with sections and keys that are automatically preserved during CU upgrade.

     ７ Note

     IIS URL rewrite rule mitigations that were applied on a per-site/per-vDir level will not be preserved by this feature and eventually be
     reapplied by the Exchange Emergency Mitigation service if they are still applicable for the CU that was installed. More information can be
     found here.

                                                                                                                                      ﾉ     Expand table

 No.     Config File Name                                                                                              Sections Preserved         Additional K
                                                                                                                                                  Preserved

 1       <ExchangeInstallPath>\V15\Bin\ComplianceAuditService.exe.config                                               appSettings                -

 2       <ExchangeInstallPath>\V15\Bin\EdgeTransport.exe.config                                                        appSettings                -

 3       <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Diagnostics.Service.exe.config                               appSettings                -

 4       <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Directory.TopologyService.exe.config                         appSettings                maxReceived
                                                                                                                                                  maxStringCo

 5       <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.EdgeSyncSvc.exe.config                                       appSettings                -

 6       <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Mitigation.Service.exe.config                                appSettings                -

 9       <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.RpcClientAccess.Service.exe.config                           appSettings,               maxReceived
                                                                                                                       defaultProxy               maxStringCo

 10      <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Search.Service.exe.config                                    appSettings                -

 12      <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Servicehost.exe.config                                       appSettings,               maxReceived
                                                                                                                       defaultProxy               maxStringCo

 14      <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Store.Service.exe.config                                     appSettings                -

 17      <ExchangeInstallPath>\V15\Bin\MSExchangeCompliance.exe.config                                                 appSettings                -

 18      <ExchangeInstallPath>\V15\Bin\MSExchangeDelivery.exe.config                                                   appSettings                -

 19      <ExchangeInstallPath>\V15\Bin\MSExchangeFrontEndTransport.exe.config                                          appSettings                -

 20      <ExchangeInstallPath>\V15\Bin\MSExchangeHMHost.exe.config                                                     appSettings                -

 21      <ExchangeInstallPath>\V15\Bin\MSExchangeHMRecovery.exe.config                                                 appSettings                -

 22      <ExchangeInstallPath>\V15\Bin\MSExchangeHMWorker.exe.config                                                   appSettings                -

 23      <ExchangeInstallPath>\V15\Bin\MSExchangeMailboxAssistants.exe.config                                          appSettings                -

 24      <ExchangeInstallPath>\V15\Bin\MsExchangeMailboxReplication.exe.config                                         appSettings,               maxReceived
                                                                                                                       defaultProxy               maxStringCo

 26      <ExchangeInstallPath>\V15\Bin\MSExchangeSubmission.exe.config                                                 appSettings                -

 27      <ExchangeInstallPath>\V15\Bin\MSExchangeThrottling.exe.config                                                 appSettings                -

 28      <ExchangeInstallPath>\V15\Bin\MSExchangeTransport.exe.config                                                  appSettings                -

 29      <ExchangeInstallPath>\V15\ClientAccess\PopImap\Microsoft.Exchange.Imap4.exe.config                            appSettings,               -
                                                                                                                       defaultProxy

 30      <ExchangeInstallPath>\V15\ClientAccess\PopImap\Microsoft.Exchange.Imap4Service.exe.config                     appSettings                -

 31      <ExchangeInstallPath>\V15\ClientAccess\PopImap\Microsoft.Exchange.Pop3.exe.config                             appSettings,               -

<!-- p.555 -->

No.   Config File Name                                                                                                    Sections Preserved         Additional K
                                                                                                                                                     Preserved

                                                                                                                          defaultProxy

32    <ExchangeInstallPath>\V15\ClientAccess\PopImap\Microsoft.Exchange.Pop3Service.exe.config                            appSettings                -

33    <ExchangeInstallPath>\V15\FrontEnd\PopImap\Microsoft.Exchange.Imap4.exe.config                                      appSettings,               -
                                                                                                                          defaultProxy

34    <ExchangeInstallPath>\V15\FrontEnd\PopImap\Microsoft.Exchange.Imap4Service.exe.config                               appSettings                -

35    <ExchangeInstallPath>\V15\FrontEnd\PopImap\Microsoft.Exchange.Pop3.exe.config                                       appSettings,               -
                                                                                                                          defaultProxy

36    <ExchangeInstallPath>\V15\FrontEnd\PopImap\Microsoft.Exchange.Pop3Service.exe.config                                appSettings                -

37    <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.AddressBook.Service.dll.config                                     appSettings                -

38    <ExchangeInstallPath>\V15\Bin\Microsoft.Exchange.Management.Transport.dll.config                                    appSettings                -

39    <ExchangeInstallPath>\V15\TransportRoles\agents\Antimalware\Microsoft.Exchange.Transport.Agent.Malware.dll.config   appSettings                -

40    <ExchangeInstallPath>\V15\Bin\MSExchangeUM.config                                                                   appSettings                -

41    <ExchangeInstallPath>\V15\ClientAccess\Autodiscover\web.config                                                      appSettings                maxReceived

42    <ExchangeInstallPath>\V15\ClientAccess\ecp\web.config                                                               appSettings                maxReceived
                                                                                                                                                     maxStringCo

43    <ExchangeInstallPath>\V15\ClientAccess\ecp\DLPPolicy\Web.config                                                     -                          maxRequest

44    <ExchangeInstallPath>\V15\ClientAccess\ecp\Handlers\Web.config                                                      -                          maxRequest

45    <ExchangeInstallPath>\V15\ClientAccess\ecp\PersonalSettings\Web.config                                              -                          maxRequest

46    <ExchangeInstallPath>\V15\ClientAccess\ecp\UsersGroups\Web.config                                                   -                          maxRequest

47    <ExchangeInstallPath>\V15\ClientAccess\exchweb\ews\web.config                                                       appSettings,               maxAllowed
                                                                                                                          defaultProxy,              maxReceived
                                                                                                                          extendedProtectionPolicy   maxRequest
                                                                                                                                                     maxStringCo

48    <ExchangeInstallPath>\V15\ClientAccess\mapi\emsmdb\web.config                                                       appSettings,               maxAllowed
                                                                                                                          defaultProxy               maxReceived
                                                                                                                                                     maxRequest
                                                                                                                                                     maxStringCo

49    <ExchangeInstallPath>\V15\ClientAccess\mapi\nspi\web.config                                                         appSettings,               maxAllowed
                                                                                                                          defaultProxy               maxRequest

50    <ExchangeInstallPath>\V15\ClientAccess\OAB\web.config                                                               appSettings                -

52    <ExchangeInstallPath>\V15\ClientAccess\PowerShell\web.config                                                        appSettings                -

53    <ExchangeInstallPath>\V15\ClientAccess\PowerShell-Proxy\web.config                                                  appSettings                -

54    <ExchangeInstallPath>\V15\ClientAccess\PushNotifications\web.config                                                 appSettings                maxReceived

55    <ExchangeInstallPath>\V15\ClientAccess\rest\web.config                                                              appSettings                maxAllowed
                                                                                                                                                     maxRequest

56    <ExchangeInstallPath>\V15\ClientAccess\RpcProxy\web.config                                                          appSettings                -

57    <ExchangeInstallPath>\V15\ClientAccess\Sync\web.config                                                              appSettings,               MaxDocume
                                                                                                                          defaultProxy               maxRequest
                                                                                                                                                     maxAllowed

58    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\autodiscover\web.config                                                appSettings                -

59    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\ecp\web.config                                                         appSettings                maxAllowed
                                                                                                                                                     maxRequest

60    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\ews\web.config                                                         appSettings                maxAllowed
                                                                                                                                                     maxRequest

61    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\mapi\web.config                                                        appSettings                maxAllowed
                                                                                                                                                     maxRequest

<!-- p.556 -->

 No.   Config File Name                                                                                              Sections Preserved           Additional K
                                                                                                                                                  Preserved

 62    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\oab\web.config                                                   appSettings                  -

 63    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\owa\web.config                                                   appSettings                  maxAllowed
                                                                                                                                                  maxRequest

 64    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\powershell\web.config                                            appSettings                  -

 65    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\pushnotifications\web.config                                     appSettings                  maxAllowed
                                                                                                                                                  maxRequest

 66    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\ReportingWebService\web.config                                   appSettings                  -

 67    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\rest\web.config                                                  appSettings                  maxAllowed
                                                                                                                                                  maxRequest

 68    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\rpc\web.config                                                   appSettings                  maxAllowed
                                                                                                                                                  maxRequest

 69    <ExchangeInstallPath>\V15\FrontEnd\HttpProxy\sync\web.config                                                  appSettings                  maxRequest
                                                                                                                                                  maxAllowed

 70    <ExchangeInstallPath>\V15\FIP-FS\Data\Configuration.xml                                                       ProxySettings                -

 71    <ExchangeInstallPath>\V15\Bin\Search\Ceres\Runtime\1.0\Noderunner.exe.config                                  -                            memoryLimi

After Setup completes, it will display the following messages to indicate that all preserved configuration settings were successfully restored.

GUI mode

<!-- p.557 -->

                      

Unattended mode

                  

<!-- p.558 -->

The backup of the preserved configuration files is stored in %ProgramFiles%\Microsoft\Exchange Server\V15\Config in subfolders that using a
naming format of v_<ExchangeVersion>_<Timestamp> .

                                                                                                                                                                    

  ７ Note

  If these files are not needed after Setup has completed, they can be safely deleted.

Setup preserves custom settings by default. If you don't want to use this feature, you can disable it by creating a REG_SZ entry
DisablePreservation under HKLM\SOFTWARE\Microsoft\ExchangeServer\v15\Setup and setting the value to 1 .

The key/value pair can be created by running the following PowerShell command:

  PowerShell

  New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\Setup -Name "DisablePreservation" -Value 1 -Type String

If the Exchange Setup is run after setting the regkey to 1 , setup won't back up nor restore any key/value pair in any of the configs.

                                                                                                                                                    ﾉ    Expand table

 Registry Key                    Registry        Exchange setup behavior
                                 Value

 DisablePreservation (Type:      1               All the key value pairs in config files are reset and no backup of preupgrade config is stored (this behavior is
 REG_SZ )                                        equivalent to previous CU upgrades).

 DisablePreservation (Type:      NULL            Setup creates a backup of preupgrade configs and preserves certain key/value pair in preupgrade configs to the
 REG_SZ )                                        new configs.

 DisablePreservation (Type:      Any other       Setup creates a backup of preupgrade configs and preserves certain key/value pair in preupgrade configs to the
 REG_SZ )                        value           new configs.

If Setup can't restore all settings to their previous state, it displays a warning.

Unattended Mode

<!-- p.559 -->

                

Attended Mode

                    

<!-- p.560 -->

As a next step, admins can analyze the Setup log file to see which settings couldn't be preserved. One or more entries may be present in the log
file to indicate which settings couldn't be preserved:

   1. Exception encountered during reading config file: <configFileName> . Skipping preservation.
   2. Exception encountered during saving <Preservation cmdlet name> changes to: <configFileName> .
   3. Exception encountered during schema validation of config file: <configFileName> . Skipping preservation.
   4. <Preservation cmdlet name> failed for: <configFileName>

Admins can manually copy any configurations files from the backup location to the required location by overwriting the files created by Setup.
This also restores these files to their pre-Setup state.
