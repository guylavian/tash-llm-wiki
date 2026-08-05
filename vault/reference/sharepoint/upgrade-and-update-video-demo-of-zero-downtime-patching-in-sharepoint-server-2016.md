---
title: "Video demo of Zero Downtime Patching in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: upgrade-and-update-video-demo-of-zero-downtime-patching-in-sharepoint-server-2016
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/upgrade-and-update/video-demo-of-zero-downtime-patching-in-sharepoint-server-2016
family: upgrade-and-update
documentKind: "article"
abstract: "Take a SharePoint tutorial that can help you learn how to patch a server in a SharePoint Server 2016 farm by using Zero Downtime Patching."
---

# Video demo of Zero Downtime Patching in SharePoint Server 2016 - SharePoint Server

Note

Video demo of Zero Downtime Patching in SharePoint Server 2016

# Video demo of Zero Downtime Patching in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Overview

## Overview

One of the new features in SharePoint Server 2016 is Zero Downtime patching.

Zero Downtime patching doesn't demand any server downtime while patching a SharePoint Server 2016 farm. However, your farm needs to be set up in a Highly Available (HA) configuration (so that SharePoint roles are hosted on more than one server). That way, patching can be done in batches where certain of the redundant servers are taken out of load balancing, patched, replaced, and tested for soundness before the other servers follow through the same process.

There's a two-step process to patch a server in a SharePoint Server 2016 farm. First, you install the binaries of the patch to each server. This step is called the patch phase. Second, after you finish the patch phase, you must complete the update installation by starting the build-to-build upgrade phase.

During Zero downtime patching, users can add and edit files and use search as at any other time, accessing the servers still handled by the load balancer. Likewise, though the database schemas may differ between the patched and unpatched sides of the farm, SharePoint Server 2016 operates in a backward-compatible mode. Its databases are able to properly function, until patching completes.

This SharePoint tutorial explains how to patch a SharePoint Server 2016 HA farm from beginning to end, including the installation of the binary files on all servers, and the build-to-build (B2B) upgrade itself.

Important

During the demonstration, the graceful shut down of Distributed Cache Service was discussed and demonstrated. The environment depicted is a test farm and the process shown is NOT how a customer should do this in a live environment.

**Important**: If you're actively using areas such as Microblogs, Newsfeeds etc. you'll instead need to use the following steps to gracefully shut down the Distributed Cache Service on each Distributed Cache Server during the patch and upgrade sequence:

**Gracefully STOP Distributed Cache Service**

$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"

$serviceInstance = Get-SPServiceInstance | ? {($*.service.tostring()) -eq $instanceName -and ($*.server.name) -eq $env:computername}

$serviceInstance.Unprovision()

**Start Distributed Cache Service**

$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"

$serviceInstance = Get-SPServiceInstance | ? {($*.service.tostring()) -eq $instanceName -and ($*.server.name) -eq $env:computername}

$serviceInstance.Provision()

For reference, here's an overview of the steps, however for further detail on SharePoint patching watch the video.

Remove the Front-end web server (SPWEB01) from the Load balancer.

Patch the front-end web server (SPWEB01) by using the STS & WSS Packages.

Restart the front-end web server (SPWEB01).

Add the front-end web server (SPWEB01) back into the Load balancer.

Remove the front-end web server (SPWEB02) from the Load balancer.

Patch the front-end web server (SPWEB02).

Restart the front-end web server (SPWEB02) computer.

Patch the following Application servers: SPAPP01, SPDCH01, and SPSRCH01 in parallel, and then restart the computers.

Patch the following Application servers: SPAPP02, SPDCH02, and SPSRCH02 in parallel, and then restart the computers.

With the front-end web server (SPWEB02) out of the Load balancer (See step 7), Open the SharePoint 2016 Management Shell, and then run following PSConfig command:  `PSConfig.exe -cmd upgrade -inplace b2b -wait -cmd applicationcontent -install -cmd installfeatures -cmd secureresources -cmd services -install`

Note

In the video, syntax is condensed to save time, but the full syntax listed in Step 10 is the recommend one to run.

Once the upgrade is complete, add the front-end web server (SPWEB02) back into the Load balancer. Once the front-end web server (SPWEB02) has been added to the Load balancer, remove the front-end web server (SPWEB01).

On the front-end web server (SPWEB01) computer, run the PSConfig command from step 10.

Add the front-end web server (SPWEB01) back into the Load balancer.

On the Application server (SPAPP01), run the PSConfig command from Step 10.

On the Distributed Cache server (SPDCH01), run the PSConfig command from Step 10.

On the Search server (SPSRCH01), run the PSConfig command from Step10.

Once the upgrade has completed run the same steps (14-16) on 02 series servers (SPAPP02, SPDCH02, SPSRCH02).

Note

We recommend to test pages throughout to ensure patching and upgrading of servers is complete.

During the video, the following Microsoft PowerShell script was used to take Servers out of the Azure Service Management Internal Load Balancer.

```
#Remove the SPWEB01 Azure Load Balanced EndPoint
$svc=<"NameYourLBService">
$vmname=<"NameofYourVM">
$epname="TCP-80-80"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add the SPWEB01 AzureEndpoint back
$ilb="minroleilb"
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM
# Remove the SPWEB02 Azure Load Balanced EndPoint for the patch install and build to build (B2B) phase
$vmname=<"NameofYourVM">
$epname="TCP-80-80-2"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add for the B2B SPWEB02 AzureEndPoint to ILB
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80-2"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM
# B2B for SPWEB01::::: Phase Remove the SPWEB01 Azure Load Balanced EndPoint
$svc=<"NameYourLBService">
$vmname=<"NameofYourVM">
$epname="TCP-80-80"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add the SPWEB01 AzureEndpoint back
$ilb="minroleilb"
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM
```

For more information about the Microsoft PowerShell for Azure cmdlets, see Get-AzureVM.

Related articles

## Related articles

Install a software update for SharePoint Server 2016

SharePoint Server 2016 zero downtime patching steps

Video: How to enable Remote Windows PowerShell to use with SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
