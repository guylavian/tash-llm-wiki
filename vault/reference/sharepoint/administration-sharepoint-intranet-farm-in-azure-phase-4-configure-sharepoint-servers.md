---
title: "SharePoint Intranet Farm in Azure Phase 4 Configure SharePoint servers - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-sharepoint-intranet-farm-in-azure-phase-4-configure-sharepoint-servers
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/sharepoint-intranet-farm-in-azure-phase-4-configure-sharepoint-servers
family: administration
documentKind: "article"
abstract: "Configure the SharePoint servers to host a high-availability SharePoint Server 2016 farm in Microsoft Azure."
---

# SharePoint Intranet Farm in Azure Phase 4 Configure SharePoint servers - SharePoint Server

Note

SharePoint Intranet Farm in Azure Phase 4: Configure SharePoint servers

# SharePoint Intranet Farm in Azure Phase 4: Configure SharePoint servers

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

In this phase of deploying an intranet-only SharePoint Server 2016 farm in Azure infrastructure services, you create the SharePoint Server 2016 servers and configure their roles with the SharePoint Configuration Wizard.

You must complete this phase before moving on to SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases. See Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure for all of the phases.

Create the SharePoint server virtual machines in Azure

## Create the SharePoint server virtual machines in Azure

There are four SharePoint server virtual machines:

Two SharePoint server virtual machines are the front-end and distributed cache servers

Two are for search and the administration and hosting of SharePoint applications

Two SharePoint servers for each set of server roles provide high availability.

Use the following blocks of PowerShell commands to create the components in Azure. Specify the values for the variables, removing the < and > characters. Note that these PowerShell command blocks use values from the following tables:

Table R, for your resource groups

Table V, for your virtual network settings

Table S, for your subnet

Table I, for your static IP addresses

Table M, for your virtual machines

Table A, for your availability sets

Recall that you defined Table M in SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers and Tables R, V, S, I, and A in SharePoint Intranet Farm in Azure Phase 1: Configure Azure.

First, you configure internal load balancing so that Azure distributes the client traffic evenly among the two front end and distributed caching servers.

Note

The following command sets use the latest version of Azure PowerShell. See Get started with Azure PowerShell cmdlets.

When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell Integrated Script Environment (ISE) on your local computer.

```
# Set up key variables
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 4 - Subnet name column>"
$privIP="<Table I - Item 3 - Value column>"
$rgName="<Table R - Item 5 - Resource group name column>"
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$frontendIP=New-AzLoadBalancerFrontendIpConfig -Name "SharePointWebServers-LBFE" -PrivateIPAddress $privIP -Subnet $subnet
$beAddressPool=New-AzLoadBalancerBackendAddressPoolConfig -Name "SharePointWebServers-LBBE"
# This example assumes unsecured (HTTP-based) web traffic to the front end servers.
$healthProbe=New-AzLoadBalancerProbeConfig -Name "WebServersProbe" -Protocol "TCP" -Port 80 -IntervalInSeconds 15 -ProbeCount 2
$lbrule=New-AzLoadBalancerRuleConfig -Name "WebTraffic" -FrontendIpConfiguration $frontendIP -BackendAddressPool $beAddressPool -Probe $healthProbe -Protocol "TCP" -FrontendPort 80 -BackendPort 80
# To use TCP 443, comment the previous line and un-comment the next line
# $lbrule=New-AzLoadBalancerRuleConfig -Name "WebTraffic" -FrontendIpConfiguration $frontendIP -BackendAddressPool $beAddressPool -Probe $healthProbe -Protocol "TCP" -FrontendPort 443 -BackendPort 443
New-AzLoadBalancer -ResourceGroupName $rgName -Name "SharePointWebServers" -Location $locName -LoadBalancingRule $lbrule -BackendAddressPool $beAddressPool -Probe $healthProbe -FrontendIpConfiguration $frontendIP
```

Next, add a DNS address record to your organization's internal DNS infrastructure that resolves the fully qualified domain name of the SharePoint farm (such as spfarm.corp.contoso.com) to the IP address assigned to the internal load balancer (the value of Table I - Item 3).

Use the following block of Azure PowerShell commands to create the virtual machines for the two SharePoint application and search servers. When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell ISE on your local computer.

```
# Set up variables common to both virtual machines
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 3 - Subnet name column>"
$avName="<Table A - Item 3 - Availability set name column>"
$rgNameTier="<Table R - Item 3 - Resource group name column>"
$rgNameInfra="<Table R - Item 5 - Resource group name column>"
$rgName=$rgNameInfra
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$rgName=$rgNameTier
$avSet=Get-AzAvailabilitySet -Name $avName -ResourceGroupName $rgName
# Create the first application/search server
$vmName="<Table M - Item 6 - Virtual machine name column>"
$vmSize="<Table M - Item 6 - Minimum size column>"
$staticIP="<Table I - Item 8 - Value column>"
$diskStorageType="<Table M - Item 6 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName +"-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $subnet -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$diskSize=200
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPSearchData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPSearchData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 2
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the first application server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
# Create the second application server
$vmName="<Table M - Item 7 - Virtual machine name column>"
$vmSize="<Table M - Item 7 - Minimum size column>"
$staticIP="<Table I - Item 9 - Value column>"
$diskStorageType="<Table M - Item 7 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName +"-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $subnet -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$diskSize=200
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPSearchData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPSearchData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 2
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the second application server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
```

Use the following block of Azure PowerShell commands to create the virtual machines for the two SharePoint front end and distributed cache servers. When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell ISE on your local computer.

```
# Set up variables common to both virtual machines
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 4 - Subnet name column>"
$avName="<Table A - Item 4 - Availability set name column>"
$rgNameTier="<Table R - Item 4 - Resource group name column>"
$rgNameInfra="<Table R - Item 5 - Resource group name column>"
$rgName=$rgNameInfra
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$backendSubnet=Get-AzVirtualNetworkSubnetConfig -Name $subnetName -VirtualNetwork $vnet
$webLB=Get-AzLoadBalancer -ResourceGroupName $rgName -Name "SharePointWebServers" 
$rgName=$rgNameTier
$avSet=Get-AzAvailabilitySet -Name $avName -ResourceGroupName $rgName
# Create the first front end  and distributed cache server virtual machine
$vmName="<Table M - Item 8 - Virtual machine name column>"
$vmSize="<Table M - Item 8 - Minimum size column>"
$staticIP="<Table I - Item 10 - Value column>"
$diskStorageType="<Table M - Item 8 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName + "-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $backendSubnet -LoadBalancerBackendAddressPool $webLB.BackendAddressPools[0] -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the first front end and distributed cache server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
# Create the second front end and distributed cache server virtual machine
$vmName="<Table M - Item 9 - Virtual machine name column>"
$vmSize="<Table M - Item 9 - Minimum size column>"
$staticIP="<Table I - Item 11 - Value column>"
$diskStorageType="<Table M - Item 9 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName + "-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $backendSubnet -LoadBalancerBackendAddressPool $webLB.BackendAddressPools[0] -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the second front end and distributed cache server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
```

Note

Because these virtual machines are for an intranet application, they are not assigned a public IP address or a DNS domain name label and exposed to the Internet. However, this also means that you cannot connect to them from the Azure portal. The Connect option is unavailable when you view the properties of the virtual machine. Use the Remote Desktop Connection accessory or another Remote Desktop tool to connect to the virtual machine using its private IP address or intranet DNS name.

Do the following for each of the SharePoint servers:

Use the remote desktop client of your choice and create a remote desktop connection. Use its intranet DNS or computer name and the credentials of the local administrator account.

Join it to the appropriate Active Directory domain with these commands at the Windows PowerShell prompt on the connected virtual machine.

```
  $domName="<Active Directory domain name to join, such as corp.contoso.com>"
  Add-Computer -DomainName $domName
  Restart-Computer
```

Note that you must supply domain account credentials after running the **Add-Computer** command.

After the virtual machine restarts, create a Remote Desktop connection using the <your domain>\sp_farm_db account credentials four times, once for each SharePoint server. You created these credentials in SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers.

Note

The SharePoint servers are created from the SharePoint Server 2016 Trial image. You need to convert the installation to use a Retail or Volume License key for either the Standard or Enterprise edition of SharePoint Server 2016. For more info, see SharePoint 2016 Licensing.

Next, you need to add the extra data disks to each SharePoint server.

For the first and second front end and distributed cache servers, run these commands at an administrator-level Windows PowerShell prompt to initialize the F: drive.

```
Get-Disk | Where PartitionStyle -eq "RAW" | Initialize-Disk -PartitionStyle MBR -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -NewFileSystemLabel "SPLogData"
md F:\Logs
```

For the first and second application and search servers, run these commands at an administrator-level Windows PowerShell prompt to initialize the F: and G: drives.

```
$newDisks=Get-Disk | Where Partitionstyle -eq "RAW"
ForEach ($d in $newDisks) {
$diskNum=$d.Number - 1
Get-Disk $d.Number | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -NewFileSystemLabel "DataDisk$diskNum"
}
md F:\Logs
md G:\Index
```

Configure the SharePoint farm

## Configure the SharePoint farm

Before the farm can be created, the build version of SharePoint must be updated to at least the November 2016 PU. This PU contains feature pack one that enables support for shared roles. Without this update, the servers can only be configured for single role use.

Download and install the latest SharePoint Server 2016 update (at least the November 2016 PU).

Note

Each monthy update contains two downloadable files. You should download and install both to ensure the server farm is correctly updated. Install the Server Patch first, then the MUI/Language patch.

Once downloaded follow the instructions in Install a software update for SharePoint Server 2016 to install the updates and upgrade the SharePoint server virtual machines. You need to complete this on all four servers.

Use these steps to configure the first SharePoint application and search server (Table M - Item 6) as the first server in the farm:

Create a remote desktop connection to the first SharePoint application and search server.

From the Start screen, enter **SharePoint**, and then select **SharePoint 2016 Products Configuration Wizard**.

On the **Welcome to SharePoint Products** page, select **Next**.

A **SharePoint Products Configuration Wizard** dialog appears, warning that services (such as IIS) will be restarted or reset. Select **Yes**.

On the **Connect to a server farm** page, select **Create a new server farm**, and then select **Next**.

On the **Specify Configuration Database Settings** page:

In **Database server**, enter the name of your first SQL server virtual machine.

In **Username**, enter <your domain>**\sp_farm_db**.

In **Password**, enter the sp_farm_db account password.

Note the value in the **Database name** field (default is SharePoint_Config). You will need this database name for the additional servers in the farm.

Select **Next**.

On the **Specify Farm Security Settings** page, enter a passphrase twice. Record the passphrase and store it in a secure location for future reference. Select **Next**.

On the **Specify Server Role** page, in **Shared Roles,** select **Application with Search,** and then select **Next**.

On the **Configure SharePoint Central Administration Web Application** page, select **Next**.

The **Completing the SharePoint Products Configuration Wizard** page appears. Select **Next**.

The **Configuring SharePoint Products** page appears. Wait until the configuration process completes.

On the **Configuration Successful** page, select **Finish**. The new administration website starts.

On the **Help Make SharePoint Better** page, to participate in the Customer Experience Improvement Program, make your selection, and then select **OK**.

On the Welcome page, select **Start the Wizard**.

On the **Service Applications and Services** page, in **Service Account**, select **Use existing managed account**, and then select **Next**. It can take a few minutes to display the next page.

On the **Create Site Collection** page, enter a site name in **Title**, and then select **OK**.

On the **This completes the Farm Configuration Wizard** page, select **Finish**. The SharePoint Central Administration web page appears.

Open a new tab in Internet Explorer, in the Address bar, enter **http://**<name of the first SharePoint application server>/, and then press Enter. You should see the default team site.

Perform the following procedure on the second SharePoint application and search server (Table M - Item 7):

Create a remote desktop connection to the second SharePoint application and search server.

From the Start screen, enter **SharePoint**, and then select **SharePoint 2016 Products Configuration Wizard**.

On the **Welcome to SharePoint Products** page, select **Next**.

A **SharePoint Products Configuration Wizard** dialog appears, warning that services (such as IIS) will be restarted or reset. Select **Yes**.

On the **Connect to a server farm** page, select **Connect to an existing server farm**, and then select **Next**.

On the **Specify Configuration Database Settings** page:

In **Database server**, enter the name of your first SQL server virtual machine, and then select **Retrieve Database Names**.

In **Database name**, select the name of the SharePoint database from Step 6 of the previous procedure.

Select **Next**.

On the **Specify Farm Security Settings** page, in **Passphrase**, enter the passphrase from step 8 of the previous procedure. Select **Next**.

On the **Specify Server Role** page, in **Shared Roles**, select **Application with Search**, and then select **Next**.

The **Completing the SharePoint Products Configuration Wizard** page appears. Select **Next**.

The **Configuring SharePoint Products** page appears. Wait until the configuration process completes.

On the **Configuration Successful** page, select **Finish**.

On the **Initial Farm Configuration** page, select **Cancel**. The **Central Administration** page appears.

Perform the following procedure on the two front-end and distributed cache servers (Table M - Items 8 and 9):

Create a remote desktop connection to the SharePoint front-end and distributed cache server.

From the Start screen, enter **SharePoint**, and then select **SharePoint 2016 Products Configuration Wizard**.

On the **Welcome to SharePoint Products** page, select **Next**.

A **SharePoint Products Configuration Wizard** dialog box appears, warning that services (such as IIS) will be restarted or reset. Select **Yes**.

On the **Connect to a server farm** page, select **Connect to an existing server farm**, and then select **Next**.

On the **Specify Configuration Database Settings** page:

In **Database server**, enter the name of your first SQL server virtual machine, and then select **Retrieve Database Names**.

In **Database name**, select the name of the SharePoint database.

Select **Next**.

On the **Specify Farm Security Settings** page, in **Passphrase**, enter the farm passphrase.

On the **Specify Server Role** page, in **Shared Roles**, select **Front-end with Distributed Cache**, and then select **Next**.

The **Completing the SharePoint Products Configuration Wizard** page appears. Select **Next**.

The **Configuring SharePoint Products** page appears. Wait until the configuration process completes.

On the **Configuration Successful** page, select **Finish**.

On the **Initial Farm Configuration** page, select **Cancel**. The **Central Administration** page appears.

When SharePoint creates the farm, it configures a set of server logins on the primary SQL Server virtual machine. The database itself stores all the database metadata and user information, and a user who is defined in this database does not need to have a corresponding login. The information in this database is replicated by the availability group and is available after a failover. For more information, see Contained database.

However, by default, SharePoint databases are not contained databases. Therefore, you will need to manually configure the secondary database server so that it has the same set of logins for SharePoint farm accounts as the primary database server. You can perform this synchronization from SQL Server Management Studio by connecting to both servers at the same time.

Here is the configuration that results from the successful completion of this phase.

**Phase 4: The SharePoint servers for your high-availability SharePoint Server 2016 farm**

Next step

## Next step

Use SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases to continue configuring this workload.

See also

## See also

Other Resources

#### Other Resources

Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure

SharePoint Server in Microsoft Azure

Designing a SharePoint Server 2016 farm in Azure

Install SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
