---
title: "Exchange Server — pages 2681-2720"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2681-2720
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2681-2720
family: exchange
documentKind: "doc"
abstract: "activation based on the database copy's activation preference value and not its copy queue length. The default value is GoodAvailability . If you specify either BestAvailability or GoodAvailability , and all the logs from the active copy can't be copied to the passive copy being"
---

# Exchange Server — pages 2681-2720

<!-- p.2681 -->

     activation based on the database copy's activation preference value and not its copy
     queue length.

The default value is GoodAvailability . If you specify either BestAvailability or
GoodAvailability , and all the logs from the active copy can't be copied to the passive copy

being activated, you may lose some mailbox data. However, the Safety Net feature (which is
enabled by default) helps protect against most data loss by resubmitting messages that are in
the Safety Net queue.

Example: configuring automatic database mount dial

The following example configures a Mailbox server with an AutoDatabaseMountDial setting of
GoodAvailability .

  PowerShell

  Set-MailboxServer -Identity EX1 -AutoDatabaseMountDial GoodAvailability

Database copy automatic activation policy
The DatabaseCopyAutoActivationPolicy parameter specifies the type of automatic activation
available for mailbox database copies on the selected Mailbox servers. You can use the Set-
MailboxServer cmdlet to configure the DatabaseCopyAutoActivationPolicy parameter with any
of the following values:

      Blocked : If you specify this value, databases can't be automatically activated on the

     selected Mailbox servers.

      IntrasiteOnly : If you specify this value, the database copy is allowed to be activated on

     servers in the same Active Directory site. This activation prevents cross-site failover or
     activation. This property is for incoming mailbox database copies (for example, a passive
     copy being made an active copy). Databases can't be activated on this Mailbox server for
     database copies that are active in another Active Directory site.

      Unrestricted : If you specify this value, there are no special restrictions on activating

     mailbox database copies on the selected Mailbox servers.

Example: configuring database copy automatic activation policy

The following example configures a Mailbox server with a DatabaseCopyAutoActivationPolicy
setting of Blocked .

<!-- p.2682 -->

  PowerShell

  Set-MailboxServer -Identity EX1 -DatabaseCopyAutoActivationPolicy Blocked

Maximum active databases
The MaximumActiveDatabases parameter (also used with the Set-MailboxServer cmdlet)
specifies the number of databases that can be mounted on a Mailbox server. You can configure
Mailbox servers to meet your deployment requirements by ensuring that an individual Mailbox
server doesn't become overloaded.

The MaximumActiveDatabases parameter is configured with a whole number numeric value.
When the maximum number is reached, the database copies on the server won't be activated if
a failover or switchover occurs. If the copies are already active on a server, the server won't
allow databases to be mounted.

Example: configuring maximum active databases

The following example configures a Mailbox server to support a maximum of 20 active
databases:

  PowerShell

  Set-MailboxServer -Identity EX1 -MaximumActiveDatabases 20

Performing maintenance on DAG members
Before performing any type of software or hardware maintenance on a DAG member, you
should first put the DAG member in maintenance mode. The following scripts are provided
with Exchange Server to assist with DAG maintenance procedures:

     StartDagServerMaintenance.ps1: Assists with moving all active databases off the server. It
     also moves all critical DAG support functionality, such as the Primary Active Manager
     (PAM) role, and blocks them from moving back to the server before maintenance is
     complete.

     StopDagServerMaintenance.ps1: Assists with taking the DAG member out of
     maintenance mode, and making it an active target for all databases and all critical DAG
     support functionality.

<!-- p.2683 -->

Both the above scripts accept the ServerName parameter (which can be either the host name
or the fully qualified domain name (FQDN) of the DAG member) and the WhatIf parameters.
Both scripts can be run locally or remotely. The server on which the scripts are executed must
have the Windows Failover Cluster Management tools installed (RSAT-Clustering).

  ７ Note

  The RedistributeActiveDatabases.ps1 script is also available, which assists with mounting
  mailbox databases on specific DAG members as indicated by the Activation Preference
  number on each database. However, in Exchange 2016 CU2 or later, the new DAG
  property named PreferenceMoveFrequency automatically balances database copies across
  a DAG. Therefore, you'll only need to use RedistributeActiveDatabases.ps1 script if you've
  disabled this functionality or if you want to balance database copies manually.

The StartDagServerMaintenance.ps1 script performs the following tasks:

     Sets the value of the DatabaseCopyAutoActivationPolicy parameter on the DAG member
     to Blocked , which prevents any database copies from being activated on the server.

     Pauses the node in the cluster, which prevents the node from being and becoming the
     PAM.

     Moves all active databases currently hosted on the DAG member to other DAG members.

     If the DAG member currently owns the default cluster group, the script moves the default
     cluster group (and therefore the PAM role) to another DAG member.

If any of the preceding tasks fails, all operations, except for successful database moves, are
undone by the script.

To begin maintenance procedures on a DAG member, including flushing the transport queues
and suspending client connectivity, perform the following tasks:

   1. To empty the transport queues, run the following command:

        PowerShell

        Set-ServerComponentState <ServerName> -Component HubTransport -State Draining
        -Requester Maintenance

   2. To initiate the draining of the transport queues, run the following command:

        PowerShell

<!-- p.2684 -->

    Restart-Service MSExchangeTransport

3. To begin the process of draining all Unified Messaging calls (in Exchange 2016 only), run
  the following command:

    PowerShell

    Set-ServerComponentState <ServerName> -Component UMCallRouter -State Draining
    -Requester Maintenance

4. To access the DAG maintenance scripts, run the following command:

    PowerShell

    CD $ExScripts

5. To run the StartDagServerMaintenance.ps1 script, run the following command:

    PowerShell

    .\StartDagServerMaintenance.ps1 -ServerName <ServerName> -MoveComment
    Maintenance -PauseClusterNode

  For the value of the MoveComment parameter, you can make any notation you want. The
  above example uses "Maintenance".

    ７ Note

    This script can take some time to execute, and during this time, you may not see any
    activity on your screen.

6. To redirect messages pending delivery in the local queues to the Exchange server
  specified by the Target parameter, run the following command:

    PowerShell

    Redirect-Message -Server <ServerName> -Target <Server FQDN>

7. To place the server into maintenance mode, run the following command:

    PowerShell

<!-- p.2685 -->

        Set-ServerComponentState <ServerName> -Component ServerWideOffline -State
        Inactive -Requester Maintenance

To verify that a server is ready for maintenance, perform the following tasks:

   1. To verify the server has been placed into maintenance mode, confirm that only
      Monitoring and RecoveryActionsEnabled are in an active state when you run the following

     command:

        PowerShell

        Get-ServerComponentState <ServerName> | Format-Table Component,State -
        Autosize

   2. To verify the server isn't hosting any active database copies, run the following command:

        PowerShell

        Get-MailboxServer <ServerName> | Format-List DatabaseCopyAutoActivationPolicy

   3. To verify that the cluster node is paused, run the following command:

        PowerShell

        Get-ClusterNode <ServerName> | Format-List

   4. To verify that all transport queues have been emptied, run the following command:

        PowerShell

        Get-Queue

After the maintenance is complete and the DAG member is ready to return to service, the
StopDagServerMaintenance.ps1 script helps takes the DAG member out of maintenance mode
and put it back into production. The StopDagServerMaintenance.ps1 script performs the
following tasks:

     Resumes the node in the cluster, which enables full cluster functionality for the DAG
     member.

     Sets the value of the DatabaseCopyAutoActivationPolicy parameter on the DAG member
     to Unrestricted .

<!-- p.2686 -->

     Runs the Resume-MailboxDatabaseCopy cmdlet for each database copy hosted on the
     DAG member.

When you're ready to restore the DAG member to full production status, including resuming
the transport queues and client connectivity, perform the following tasks:

   1. To configure the server to be in out-of-maintenance mode and ready to accept client
     connections, run the following command:

       PowerShell

        Set-ServerComponentState <ServerName> -Component ServerWideOffline -State
        Active -Requester Maintenance

       ７ Note

             If your environment uses Microsoft Exchange IMAP4 & Microsoft Exchange
             POP3 services, by design, the services will stop and remain in stopped mode if
             the related ImapProxy and PopProxy components are in the Inactive state.
             To start the services, change the state of the related ImapProxy and PopProxy
             components to Active and manually start the services.

   2. To allow the server to accept Unified Messaging calls (in Exchange 2016 only), run the
     following command:

       PowerShell

        Set-ServerComponentState <ServerName> -Component UMCallRouter -State Active -
        Requester Maintenance

   3. To access the DAG maintenance scripts, run the following command:

       PowerShell

        CD $ExScripts

   4. To execute the StopDagServerMaintenance.ps1 script, run the following command:

       PowerShell

        .\StopDagServerMaintenance.ps1 -serverName <ServerName>

<!-- p.2687 -->

   5. To enable the transport queues to resume accepting and processing messages, run the
     following command:

        PowerShell

        Set-ServerComponentState <ServerName> -Component HubTransport -State Active -
        Requester Maintenance

   6. To resume transport activity, run the following command:

        PowerShell

        Restart-Service MSExchangeTransport

To verify that a server is ready for production use, perform the following tasks:

   1. To verify the server isn't in maintenance mode, run the following command:

        PowerShell

        Get-ServerComponentState <ServerName> | Format-Table Component,State -
        Autosize

     If you're installing an Exchange update, and the update process fails, it can leave some
     server components in an inactive state, which will be displayed in the output of the above
      Get-ServerComponentState cmdlet. To resolve this issue, run the following commands:

            Set-ServerComponentState <ServerName> -Component ServerWideOffline -State

            Active -Requester Functional

            Set-ServerComponentState <ServerName> -Component Monitoring -State Active -
            Requester Functional

            Set-ServerComponentState <ServerName> -Component RecoveryActionsEnabled -State
            Active -Requester Functional

Shutting down DAG members
Exchange high availability solution is integrated with the Windows shutdown process. If an
administrator or application initiates a shutdown of a Windows server in a DAG that has a
mounted database that's replicated to one or more DAG members, the system attempts to
activate another copy of the mounted database prior to allowing the shutdown process to
complete.

<!-- p.2688 -->

However, this new behavior doesn't guarantee that all of the databases on the server being
shut down will experience a lossless activation. As a result, it's a best practice to perform a
server switchover prior to shutting down a server that's a member of a DAG.

Installing updates on DAG members
Installing Exchange updates on a server that's a member of a DAG is a relatively
straightforward process. When you install an update on a server that's a member of a DAG,
several services are stopped during the installation, including all Exchange services and the
Cluster service. The general process for applying updates to a DAG member is as follows:

   1. Use the steps described above to put the DAG member in maintenance mode.

   2. Install the update.

   3. Use the steps described above to take the DAG member out of maintenance mode and
     put it back into production.

   4. Optionally, use the RedistributeActiveDatabases.ps1 script to rebalance the active
     database copies across the DAG.

For more information about the latest Exchange updates, see Exchange Server build numbers
and release dates.

  ７ Note

  You should always run all DAG members on the same version of Exchange server
  (including cumulative and security updates). Perform a "rolling update" of all DAG
  members, and don't run a DAG with members on a different Exchange version for an
  extended amount of time.

<!-- p.2689 -->

Create a database availability group in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

A database availability group (DAG) is a set of up to 16 Microsoft Exchange Server Mailbox
servers that provide automatic database-level recovery from a database, server, or network
failure. When a Mailbox server is added to a DAG, it works with the other servers in the DAG to
provide automatic, database-level recovery from database, server, and network failures.

  ） Important

  All servers within a DAG must be running the same version of Exchange. You can't mix
  Exchange 2013 servers and Exchange servers in the same DAG.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
      Estimated time to complete: 1 minute

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Database availability groups"
      entry in the High availability and site resilience permissions topic.

      When creating a DAG with Mailbox servers running Windows Server 2012, you must pre-
      stage the cluster name object (CNO) before adding members to the DAG. If you're
      creating a DAG without an administrative access point with Mailbox servers running
      Windows Server 2012 R2, then you do not need to pre-stage a CNO for the DAG. For
      detailed steps, see Pre-stage the cluster name object for a database availability group.

      When creating a DAG, you provide a unique name for the DAG of up to 15 characters. In
      addition to providing a name for the DAG, you must also assign one or more IP addresses
      (either IPv4 or both IPv4 and IPv6) to the DAG, unless you're creating a Windows Server
      2012 R2 DAG without an administrative access point and you aren't assigning any IP
      addresses to the DAG. Otherwise, the IP addresses you assign must be on each subnet

<!-- p.2690 -->

   intended for the MAPI network and must be available for use. If you specify one or more
   IPv4 addresses and your system is configured to use IPv6, the task will also attempt to
   automatically assign the DAG one or more IPv6 addresses.

   When creating a DAG, you must specify a witness server and witness directory. We
   recommend that you use an Exchange server with Client Access services. This allows an
   Exchange administrator to be aware of the availability of the witness, and it ensures that
   all of the necessary security permissions needed for using the witness server are in place.

   The following combinations of options and behaviors are available:

      You can specify a name for the DAG, the witness server that you want to use, and the
      directory you want created and shared on the witness server.

      You can specify a name for the DAG and the witness server that you want to use, and
      leave the Witness directory field empty. In this scenario, the task will create the default
      witness directory on the specified witness server.

      Note: If the witness server you specify isn't an Exchange server in your organization,
      you must add the Exchange Trusted Subsystem universal security group to the local
      Administrators group on the witness server. These security permissions are necessary
      to ensure that Exchange can create a directory and share on the witness server as
      needed. If the proper permissions aren't configured, the following error is returned:

         Error: An error occurred during discovery of the database availability group

      topology. Error: An error occurred while attempting a cluster operation. Error:

      Cluster API "AddClusterNode() (MaxPercentage=12) failed with 0x80070005. Error:
      Access is denied."

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online       , or Exchange Online Protection .

Use the EAC to create a database availability group
 1. In the EAC, go to Servers > Database Availability Groups.

 2. Click    to create a DAG.

<!-- p.2691 -->

   3. On the new database availability group page, provide the following information for the
     DAG:

            Database availability group name: Use this field to type a valid and unique name
            for the DAG of up to 15 characters. The name is equivalent to a computer name, and
            a corresponding CNO will be created in Active Directory with that name. This name
            will be both the name of the DAG and the name of the underlying cluster.

            Witness server: Use this field to specify a witness server for the DAG.

            Note: You must use either a host name or a fully qualified domain name (FQDN) for
            the witness server. Using an IP address or a wildcard name isn't supported. In
            addition, the witness server can't be a member of the DAG.

            Witness directory: Use this field to type the path to a directory on the witness server
            that will be used to store witness data. If the directory doesn't exist, the system will
            create it for you on the witness server. If you leave this field blank, the default
            directory (%SystemDrive%\DAGFileShareWitnesses\<DAG FQDN>) will be created
            on the witness server.

            Database availability group IP addresses: Use this field to assign one or more static
            IPv4 addresses to the DAG. Enter an IPv4 address and click        to add it. Leave this
            field blank if you want the DAG to use Dynamic Host Configuration Protocol (DHCP)
            to obtain the necessary IPv4 addresses. Optionally, enter 255.255.255.255 to create a
            DAG without an IP address or cluster administrative access point, which applies only
            to DAGs that will contain Mailbox servers running Windows Server 2012 R2.

   4. Click Save to create the DAG.

Use the Exchange Management Shell to create a
database availability group
The following example creates a DAG named DAG1, which is configured to use the witness
server FILESRV1 and the local directory C:\DAG1. DAG1 is also configured to use DHCP for the
DAG's IP addresses.

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG1 -WitnessServer FILESRV1 -WitnessDirectory
  C:\DAG1

This example creates the DAG DAG3. DAG3 is configured to use the witness server MBX2 and
the local directory C:\DAG3. DAG3 is assigned multiple static IP addresses because its DAG

<!-- p.2692 -->

members are on different subnets on the MAPI network.

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG3 -WitnessServer MBX2 -WitnessDirectory
  C:\DAG3 -DatabaseAvailabilityGroupIPAddresses 10.0.0.8,192.168.0.8

This example creates the DAG DAG5 that will not have an administrative access point (valid for
Windows Server 2012 R2 DAGs only). In addition, MBX4 will be used as the witness server for
the DAG, and the default witness directory will be created.

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG5 -DatabaseAvailabilityGroupIPAddresses
  ([System.Net.IPAddress]::None) -WitnessServer MBX4

How do you know this worked?
To verify that you've successfully created a DAG, do one of the following:

     In the EAC, navigate to Servers > Database Availability Groups. The newly created DAG is
     displayed.

     In the Exchange Management Shell, run the following command to verify the DAG was
     created and to display DAG property information.

        PowerShell

        Get-DatabaseAvailabilityGroup <DAGName> | Format-List

For more information
Database availability groups

Configure database availability group properties

Set-DatabaseAvailabilityGroup

New-DatabaseAvailabilityGroup

New-DatabaseAvailabilityGroupNetwork

Add-DatabaseAvailabilityGroupServer

<!-- p.2693 -->

Pre-stage the cluster name object for a
database availability group in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016       2019   Subscription Edition

In environments where computer account creation is restricted, or where computer accounts
are created in a container other than the default computers container, you can pre-stage the
cluster name object (CNO) and then provision the CNO by assigning permissions to it.

Pre-staging the CNO is also required for Windows Server 2012 and Windows Server 2012 R2
DAG members due to permissions changes in Windows for computer objects. When deploying
a database availability group (DAG) using Mailbox servers that are running Windows Server
2012 or Windows Server 2012 R2, you must pre-stage and provision the CNO, unless you're
deploying a DAG without a cluster administrative access point. DAGs without cluster
administrative access points don't use CNOs; therefore pre-staging isn't required for those
DAGs.

You create and disable a computer account for the CNO, and then either:

      Assign full control of the computer account to the computer account of the first Mailbox
      server you're adding to the DAG.

      -Or-

      Assign full control of the computer account to the Exchange Trusted Subsystem universal
      security group (USG).

What do you need to know before you begin?
      Estimated time to complete: 1 minute

      You must use an account that has permissions to create computer objects in Active
      Directory.

      After completing the following steps, allow time for Active Directory replication to occur.
      After the object is replicated, you can add the first member to the DAG.

   Tip

<!-- p.2694 -->

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

Pre-stage the CNO
 1. Open Active Directory Users and Computers.

 2. Expand the forest node.

 3. Right-click the organizational unit (OU) in which you want to create the new account,
   select New, and then select Computer.

 4. In New Object - Computer, type the computer account name for the CNO in the
   Computer name box. This is the name that you'll use for the DAG. Click OK to create the
   account.

 5. Right-click the new computer account, and then click Disable Account. Click Yes to
   confirm the disable action, and then click OK.

Assign permissions to the CNO
 1. Open Active Directory Users and Computers.

 2. If Advanced Features aren't enabled, turn them on by clicking View, and then clicking
   Advanced Features.

 3. Right-click the new computer account, and then click Properties.

 4. In <Computer Name> Properties, on the Security tab, click Add to add either the
   computer account for the first node to be added to the DAG or to add the Exchange
   Trusted Subsystem USG:

         To add the Exchange Trusted Subsystem, type Exchange Trusted Subsystem in the
         Enter the object names to select field. Click OK to add the USG. Select the Exchange
         Trusted Subsystem USG and in the Permissions for Exchange Trusted Subsystem
         field, select Full Control in the Allow column. Click OK to save the permission
         settings.

         To add the computer account for the first node to be added to the DAG, click Object
         Types. In the Object Types dialog box, clear the Built-in security principals, Groups,
         and Users check boxes. Select the Computers check box and click OK. In the Enter
         the object names to select field, type the name of the first Mailbox server to be
         added to the DAG, and then click OK. Select the first node's computer account, and

<!-- p.2695 -->

          in the Permissions for <NodeName> field, select Full Control in the Allow column.
          Click OK to save the permission settings.

How do you know this worked?
To verify that you successfully created the CNO, do the following:

   1. Open Active Directory Users and Computers.

   2. Expand the forest node.

   3. Open the OU in which you created the account, and then verify that the account is listed.

<!-- p.2696 -->

Exchange Server: Using a Microsoft Azure
VM as a DAG witness server
Article • 04/30/2025

APPLIES TO:        2016      2019       Subscription Edition

Using a Microsoft Azure virtual machine (VM) as a database availability group (DAG) witness
server requires three separate physical locations:

      Two datacenters for mailbox servers.
      A third location for the DAG witness server.

Organizations with only two physical locations now can also take advantage of automatic
datacenter failover by using a Microsoft Azure VM to act as the DAG's witness server. This
article focuses on the placement of the DAG witness on Microsoft Azure and assumes that both
of the following statements are true:

      You're familiar with site resilience concepts.
      You have a fully functional DAG infrastructure spanning two datacenters.

If you don't already have your DAG infrastructure configured, we recommend that you first
review the following articles:

      High availability and site resilience
      Database availability groups
      Plan for high availability and site resilience

Changes to Microsoft Azure
This configuration requires a multi-site VPN. It has always been possible to connect your
organization's network to Microsoft Azure using a site-to-site VPN connection. However, in the
past, Azure supported only a single site-to-site VPN. Since configuring a DAG and its witness
across three datacenters required multiple site-to-site VPNs, placement of the DAG witness on
an Azure VM wasn't initially possible.

In June 2014, Microsoft Azure introduced multi-site VPN support, which enabled organizations
to connect multiple datacenters to the same Azure virtual network. This change also made it
possible for organizations with two datacenters to use Microsoft Azure as a third location to
place their DAG witness servers. To learn more about the multi-site VPN feature in Azure, see
Configure a Multi-Site VPN.

  ７ Note

<!-- p.2697 -->

  This configuration uses Azure virtual machines and a multi-site VPN for deploying the
  witness server and does not use the Azure Cloud Witness.

Microsoft Azure file server witness
The following diagram is an overview of using a Microsoft Azure file server VM as a DAG
witness. You need an Azure virtual network, a multi-site VPN that connects your datacenters to
your Azure virtual network, and a domain controller and a file server deployed on Azure virtual
machines.

  ７ Note

  It is technically possible to use a single Azure VM for this purpose and place the file
  witness share on the domain controller. However, this will result in an unnecessary
  elevation of privileges. Therefore, it is not a recommended configuration.

DAG witness server on Microsoft Azure

<!-- p.2698 -->

The first thing you need to do in order to use a Microsoft Azure VM for your DAG witness is to
get a subscription. See How to buy Azure     for the best way to acquire an Azure subscription.

After you have your Azure subscription, you need to do the following steps in order:

   1. Prepare the Microsoft Azure virtual network
   2. Configure a multi-site VPN
   3. Configure virtual machines
   4. Configure the DAG witness

  ７ Note

  A significant portion of the guidance in this article involves Microsoft Azure configuration.
  Therefore, we link to Azure documentation whenever possible.

Prerequisites

<!-- p.2699 -->

     Two datacenters that are capable of supporting an Exchange high availability and site
     resilience deployment. See Plan for high availability and site resilience for more
     information.

     A public IP address that isn't behind NAT for the VPN gateways in each site.

     A VPN device in each site that is compatible with Microsoft Azure. For more information,
     see About VPN Devices for Virtual Network.

     Familiarity with DAG concepts and management.

     Familiarity with Windows PowerShell.

Phase 1: Prepare the Microsoft Azure virtual network
Configuring the Microsoft Azure network is the most crucial part of the deployment process. At
the end of this phase, you get a fully functional Azure virtual network that's connected to your
two datacenters via a multi-site VPN.

Register DNS servers

Because this configuration requires name resolution between the on-premises servers and
Azure VMs, you need to configure Azure to use your own DNS servers. Name resolution for
resources in Azure virtual networks article provides an overview of name resolution in Azure.

Do the following to register your DNS servers:

   1. In the Azure portal, go to networks, and then select NEW.

   2. Select NETWORK SERVICES > VIRTUAL NETWORK > REGISTER DNS SERVER.

   3. Type the name and IP address for your DNS server. The name specified here's a logical
     name used in the management portal and doesn't have to match the actual name of your
     DNS server.

   4. Repeat steps 1 through 3 for any other DNS servers you want to add.

       ７ Note

       The DNS servers you register are not used in a round robin fashion. Azure VMs will
       use the first DNS server listed and will only use any additional servers if the first one
       is not available.

<!-- p.2700 -->

   5. Repeat steps 1 through 3 to add the IP address to use for the domain controller you
     deploy on Microsoft Azure.

Create local (on-premises) network objects in Azure

Next, do the following to create logical network objects that represent your datacenters in
Microsoft Azure:

   1. In the Azure portal, and then go to networks, and then select NEW.

   2. Select NETWORK SERVICES > VIRTUAL NETWORK > ADD LOCAL NETWORK.

   3. Type the name for your first datacenter site and the IP address of the VPN device on that
     site. This IP address must be a static public IP address that isn't behind NAT.

   4. On the next screen, specify the IP subnets for your first site.

   5. Repeat steps 1 through 4 for your second site.

Create the Azure virtual network

Now, do the following steps to create an Azure virtual network that's used by the VMs:

   1. In the Azure portal, go to networks, and then select NEW.

   2. Select NETWORK SERVICES > VIRTUAL NETWORK > CUSTOM CREATE.

   3. On the Virtual Network Details page, specify a name for the virtual network, and select a
     geographic location for the network.

   4. In the DNS Servers and VPN Connectivity page, verify that the DNS servers you
     previously registered are listed as the DNS servers.

   5. Select the Configure a site-to-site VPN check box under SITE-TO-SITE CONNECTIVITY.

        ） Important

        Do not select Use ExpressRoute because this will prevent the necessary
        configuration changes required to set up a multi-site VPN.

   6. Under LOCAL NETWORK, select one of the two on-premises networks you configured.

   7. In the Virtual Network Address Spaces page, specify the IP address range to use for your
     Azure virtual network.

<!-- p.2701 -->

Checkpoint: Review the network configuration
At this point, when you go to networks, you should see the virtual network you configured
under VIRTUAL NETWORKS, your local sites under LOCAL NETWORKS, and your registered
DNS servers under DNS SERVERS.

Phase 2: Configure a multi-site VPN
Use the following steps to establish the VPN gateways to your on-premises sites:

   1. Establish a VPN gateway to one of your sites by using the Azure portal.
   2. Export the virtual network configuration settings.
   3. Modify the configuration file for multi-site VPN.
   4. Import the updated Azure network configuration.
   5. Record the Azure gateway IP address and preshared keys.
   6. Configure on-premises VPN devices.

For more information about configuring a multi-site VPN, see Configure a Multi-Site VPN.

Establish a VPN gateway to your first site
When you create your virtual gateway, you already specified that it's connected to your first
on-premises site. When you go into the virtual network dashboard, you see that the gateway
hasn't been created.

To establish the VPN gateway on the Azure side, see VPN Gateway       .

  ） Important

  Only perform the steps in the "Start the virtual network gateway" section of the article,
  and do not continue to the subsequent sections.

Export virtual network configuration settings
The Azure management portal doesn't currently allow you to configure a multi-site VPN. For
this configuration, you need to export the virtual network configuration settings to an XML file
and then modify that file. Follow the instructions at Export Virtual Network Settings to a
Network Configuration File to export your settings.

Modify the network configuration settings for the multi-site VPN

<!-- p.2702 -->

Open the file you exported in any XML editor. The gateway connections to your on-premises
sites are listed in the "ConnectionsToLocalNetwork" section. Search for that term in the XML file
to locate the section. This section in the configuration file looks like the following example (the
example site name you created for your local site is "Site A").

  XML

  <ConnectionsToLocalNetwork>
      <LocalNetworkSiteRef name="Site A">
          <Connection type="IPsec" />
  </LocalNetworkSiteRef>

To configure your second site, add another "LocalNetworkSiteRef" section under the
"ConnectionsToLocalNetwork" section. The section in the updated configuration file looks like
the following example (the example site name for your second local site is "Site B").

  XML

  <ConnectionsToLocalNetwork>
      <LocalNetworkSiteRef name="Site A">
          <Connection type="IPsec" />
      <LocalNetworkSiteRef name="Site B">
          <Connection type="IPsec" />
  </LocalNetworkSiteRef>

Save the updated configuration settings file.

Import virtual network configuration settings
The second site reference you added to the configuration file triggers Microsoft Azure to
create a new tunnel. Import the updated file using the instructions in Create a virtual network
(classic) by using the Azure portal. After you complete the import, the virtual network
dashboard will show the gateway connections to both of your local sites.

Record the Azure gateway IP address and preshared keys

After the new network configuration settings are imported, the virtual network dashboard will
display the IP address for the Azure gateway. VPN devices on both both of your sites connect
to this IP address. Record this IP address for reference.

You also need to get the preshared IPsec/IKE keys for each tunnel that was created. You use
these keys and the Azure gateway IP address to configure your on-premises VPN devices.

<!-- p.2703 -->

You need to use PowerShell to get the preshared keys. If you aren't familiar with using
PowerShell to manage Azure, see Azure PowerShell.

Use the Get-AzureVNetGatewayKey cmdlet to extract the preshared keys. Run this cmdlet once
for each tunnel. The following example shows the commands you need to run to extract the
keys for tunnels between the virtual network "Azure Site" and sites "Site A" and "Site B." In this
example, the outputs are saved into separate files. Alternatively, you can pipeline these keys to
other PowerShell cmdlets or use them in a script.

  PowerShell

  Get-AzureVNETGatewayKey -VNetName "Azure Site" -LocalNetworkSiteName "Site A" |
  Set-Content -Path C:\Keys\KeysForTunnelToSiteA.txt
  Get-AzureVNETGatewayKey -VNetName "Azure Site" -LocalNetworkSiteName "Site B" |
  Set-Content -Path C:\Keys\KeysForTunnelToSiteB.txt

Configure on-premises VPN devices

Microsoft Azure provides VPN device configuration scripts for supported VPN devices. Select
the Download VPN Device Script link on the virtual network dashboard for the appropriate
script for your VPN devices.

The script you download has the configuration setting for the first site that you configured
when you set up your virtual network, and can be used as is to configure the VPN device for
that site. For example, if you specified Site A as the LOCAL NETWORK when you created your
virtual network, the VPN device script can be used for Site A. However, you need to modify it to
configure the VPN device for Site B. Specifically, you need to update the preshared key to
match the key for the second site.

For example, if you're using a Routing and Remote Access Service (RRAS) VPN device for your
sites, you need to:

   1. Open the configuration script in any text editor.

   2. Find the #Add S2S VPN interface section.

   3. Find the Add-VpnS2SInterface command in this section. Verify that the value for the
     SharedSecret parameter matches the preshared key for the site for which you're
     configuring the VPN device.

Other devices might require more verifications. For example, the configuration scripts for Cisco
devices set ACL rules by using the local IP address ranges. You need to review and verify all
references to the local site in the configuration script before you use it.

<!-- p.2704 -->

Checkpoint: Review the VPN status
At this point, both of your sites are connected to your Azure virtual network through the VPN
gateways. You can validate the status of the multi-site VPN by running the following command
in PowerShell.

  PowerShell

  Get-AzureVnetConnection -VNetName "Azure Site" | Format-Table
  LocalNetworkSiteName, ConnectivityState

If both tunnels are up and running, the output of this command looks like the following
example.

  Console

  LocalNetworkSiteName       ConnectivityState
  --------------------       -----------------
  Site A                     Connected
  Site B                     Connected

You can also verify connectivity by viewing the virtual network dashboard in the Azure
management portal. The STATUS value for both sites shows as Connected.

  ７ Note

  It can take several minutes after the connection is successfully established for the status
  change to appear in the Azure management portal.

Phase 3: Configure virtual machines
You need to create a minimum of two virtual machines in Microsoft Azure for this deployment:
a domain controller and a file server to serve as the DAG witness.

   1. Create virtual machines for your domain controller and your file server using the
     instructions in Create a Virtual Machine Running Windows. Make sure that you select the
     virtual network you created for REGION/AFFINITY GROUP/VIRTUAL NETWORK when
     specifying the settings of your virtual machines.

   2. Specify preferred IP addresses for both the domain controller and the file server using
     Azure PowerShell. When you specify a preferred IP address for a VM, it needs to be
     updated, which requires restarting the VM. The following example sets the IP addresses
     for Azure-DC and Azure-FSW to 10.0.0.10 and 10.0.0.11 respectively.

<!-- p.2705 -->

       PowerShell

       Get-AzureVM Azure-DC | Set-AzureStaticVNetIP -IPAddress 10.0.0.10 | Update-
       AzureVM

       PowerShell

       Get-AzureVM Azure-FSW | Set-AzureStaticVNetIP -IPAddress 10.0.0.11 | Update-
       AzureVM

       ７ Note

       A VM with a preferred IP address will attempt to use that address. However, if that
       address has been assigned to a different VM, the VM with the preferred IP address
       configuration will not start. To avoid this situation, make sure that the IP address you
       use isn't assigned to another VM.

   3. Provision the domain controller VM on Azure using the standards used by your
     organization.

   4. Prepare the file server with the prerequisites for an Exchange DAG witness:

     a. Add the File Server role using the Add Roles and Features Wizard or the Install-
        WindowsFeature cmdlet.

     b. Add the Exchange Trusted Subsystems universal security group to the Local
        Administrators group.

Checkpoint: Review virtual machine status

At this point, your virtual machines should be up and running and should be able to
communicate with servers in both of your on-premises datacenters:

     Verify that your domain controller in Azure is replicating with your on-premises domain
     controllers.

     Verify that you can reach the file server on Azure by name and establish an SMB
     connection from your Exchange servers.

     Verify that you can reach your Exchange servers by name from the file server on Azure.

Phase 4: Configure the DAG witness

<!-- p.2706 -->

Finally, you need to configure your DAG to use the new witness server. By default, Exchange
uses the C:\DAGFileShareWitnesses as the file share witness path on your witness server. If
you're using a custom file path, you should also update the witness directory for the specific
share.

   1. Connect to Exchange Management Shell.

   2. Run the following command to configure the witness server for your DAGs.

         PowerShell

         Set-DatabaseAvailabilityGroup -Identity DAG1 -WitnessServer Azure-FSW

See the following articles for more information:

Configure database availability group properties.

Set-DatabaseAvailabilityGroup.

Checkpoint: Validate the DAG file share witness

At this point, your DAG is configured to use the file server on Azure as your DAG witness. Do
the following steps to validate your configuration:

   1. Validate the DAG configuration by running the following command.

         PowerShell

         Get-DatabaseAvailabilityGroup -Identity DAG1 -Status | Format-List Name,
         WitnessServer, WitnessDirectory, WitnessShareInUse

     Verify that the WitnessServer parameter is set to the file server on Azure, the
     WitnessDirectory parameter is set to the correct path, and the WitnessShareInUse
     parameter shows Primary.

   2. If the DAG has an even number of nodes, the file share witness is configured. Validate the
     file share witness setting in cluster properties by running the following command. The
     value for the SharePath parameter should point to the file server and display the correct
     path.

         PowerShell

         Get-ClusterResource -Cluster MBX1 | Get-ClusterParameter | Format-List

<!-- p.2707 -->

3. Next, verify the status of the "File Share Witness" cluster resource by running the
  following command. The State of the cluster resource should display Online.

     PowerShell

     Get-ClusterResource -Cluster MBX1

4. Lastly, verify that the share is successfully created on the file server by reviewing the
  folder in File Explorer and the shares in Server Manager.

<!-- p.2708 -->

Remove a database availability group in
Microsoft Exchange
07/23/2025

APPLIES TO:      2016      2019       Subscription Edition

Removing a DAG is a quick and easy task. You can use the EAC or the Exchange Management
Shell to remove a DAG.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
     Estimated time to complete: 1 minute

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions topic.

     Before you can remove a DAG, the DAG must be empty. If the DAG you want to remove
     contains any Mailbox servers, you must first remove the servers from the DAG. For
     detailed steps about how to remove a Mailbox server from a DAG, see Manage database
     availability group membership.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to remove a database availability
group
   1. Navigate to Servers > Database availability groups.

   2. Select the DAG you want to remove and click Delete       .

<!-- p.2709 -->

   3. Click Yes to confirm the warning and remove the DAG.

Use the Exchange Management Shell to remove a
database availability group
This example removes the DAG DAG1.

  PowerShell

  Remove-DatabaseAvailabilityGroup -Identity DAG1

How do you know this worked?
To verify that you've successfully removed the DAG, do one of the following:

     In the EAC, go to Servers > Database Availability Groups, and see if the DAG is still
     displayed.

     In the Exchange Management Shell, run the following command to see if the DAG still
     exists:

        PowerShell

        Get-DatabaseAvailabilityGroup <DAGName>

     If the DAG was successfully deleted, the preceding command will produce an error
     message indicating the object could not be found.

<!-- p.2710 -->

Configure AutoReseed for a database
availability group in Exchange Server
07/23/2025

APPLIES TO:        2016       2019    Subscription Edition

Use the steps in this article to configure AutoReseed for a database availability group (DAG) in
Exchange Server.

  Ｕ Caution

  The AutoReseed feature doesn't perform any prerequisite configuration tasks for you. An
  administrator must manually install disks correctly, add spare disks to the system, replace
  bad disks, and format new disks.

For more management tasks related to DAGs, see Manage database availability groups.

What do you need to know before you begin?
     Estimated time to complete this task: 10 minutes.

     To open the Exchange Management Shell, see Open the Exchange Management Shell.

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions article.

     A single logical disk/partition per physical disk must be created.

     You must use the specific database and log folder structure described in the following
     steps in this article.

     For information about keyboard shortcuts that apply to the procedures in this article, see
     Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

<!-- p.2711 -->

Step 1: Configure the root paths for databases and
volumes
The first step involves configuring the root folders for the databases
(AutoDagDatabasesRootFolderPath) and volumes (AutoDagVolumesRootFolderPath) used by the
DAG. The defaults are C:\ExchangeDatabases, and C:\ExchangeVolumes, respectively. You can
omit this step if you're using the default paths.

This example illustrates how to configure the root path for the databases.

  PowerShell

  Set-DatabaseAvailabilityGroup DAG1 -AutoDagDatabasesRootFolderPath "C:\ExchDbs"

This example illustrates how to configure the root path for the storage volumes.

  PowerShell

  Set-DatabaseAvailabilityGroup DAG1 -AutoDagVolumesRootFolderPath "C:\ExchVols"

How do you know you successfully configured the root paths
for databases and volumes?
To verify you successfully configured the root paths for databases and volumes, run the
following command:

  PowerShell

  Get-DatabaseAvailabilityGroup DAG1 | Format-List *auto*

The output for AutoDagDatabasesRootFolderPath and AutoDagVolumesRootFolderPath should
reflect the configured paths.

Step 2: Configure the number of databases per
volume
Next, configure the number of databases per volume (AutoDagDatabaseCopiesPerVolume) for
the DAG.

<!-- p.2712 -->

This example illustrates how to configure this AutoReseed setting for a DAG configured with
four databases per volume.

  PowerShell

  Set-DatabaseAvailabilityGroup DAG1 -AutoDagDatabaseCopiesPerVolume 4

How do you know you successfully configured the number of
databases per volume?
To verify successful configuration of the number of databases per volume, run the following
command:

  PowerShell

  Get-DatabaseAvailabilityGroup DAG1 | Format-List *auto*

The output for AutoDagDatabaseCopiesPerVolume should reflect the configured value.

Step 3: Create the root folders for databases and
volumes
Next, create the folders that correspond to the root folders you configured in Step 1. This
example shows how to create the default folders in a Windows Command Prompt.

  dos

  md C:\ExchangeDatabases

  md C:\ExchangeVolumes

How do you know you successfully created the root folders
for databases and volumes?
To verify successful configuration of the root folders for databases and volumes, run the
following command.

  dos

  Dir C:\

<!-- p.2713 -->

The created folders should appear in the output list.

Step 4: Mount the volume folders
For every volume that is used for databases (including spare volumes), use the Windows Disk
Management application (diskmgmt.msc) to mount each volume in a mounted folder under
C:\ExchangeVolumes. For example, if there are two volumes with databases and one spare
volume, mount the volumes to the following mounted folders:

        C:\ExchangeVolumes\Volume1
        C:\ExchangeVolumes\Volume2
        C:\ExchangeVolumes\Volume3

The names of the mounted folders can be any folder name, as long as the folders are mounted
under the root volume's path.

How do you know you successfully mounted the volume
folders?
To verify you mounted the volume folders successfully, run the following command.

  dos

  Dir C:\

The mounted volumes should appear in the output list.

Step 5: Create the database folders
Next, create the database folders under the root path C:\ExchangeDatabases. This example
illustrates how to create folders for a storage configuration with four databases on each
volume.

  dos

  md c:\ExchangeDatabases\db001

  dos

  md c:\ExchangeDatabases\db002

<!-- p.2714 -->

  dos

  md c:\ExchangeDatabases\db003

  dos

  md c:\ExchangeDatabases\db004

How do you know you successfully created the database
folders?
To verify you created the database folders successfully, run the following command.

  dos

  Dir C:\ExchangeDatabases

The created folders should appear in the output list.

Step 6: Create the mount points for the databases
Create the mount points for each database and link the mount point to the correct volume. For
example, the mounted folder for db001 should be at C:\ExchangeDatabases\db001. You can
use diskmgmt.msc or mountvol.exe to do create and configure the mount points. This example
illustrates how to mount db001 to C:\ExchangeDatabases\db001 using mountvol.exe.

  dos

  Mountvol.exe c:\ExchangeDatabases\db001 \\?\Volume (GUID)

How do you know you successfully create the mount points
for the databases?
To verify you successfully created the mount points for the database, run the following
command.

  dos

  Mountvol.exe C:\ExchangeDatabases\db001 /L

<!-- p.2715 -->

The mounted volume should appear in the mount point list.

Step 7: Create the database folder structure
Next, create two folders in the folders you created in Step 5:

        A folder for each database.
        A folder for each of the database's log stream stored on the same volume.

You must use the following format for your folder structure:

C:\<DatabaseFolderName >\ DatabaseName \<DatabaseName >.db

C:\<DatabaseFolderName >\ DatabaseName \<DatabaseName >.log

This example illustrates how to create folders for four databases stored on Volume 1:

  dos

  md c:\ExchangeDatabases\db001\db001.db

  dos

  md c:\ExchangeDatabases\db001\db001.log

  dos

  md c:\ExchangeDatabases\db002\db002.db

  dos

  md c:\ExchangeDatabases\db002\db002.log

  dos

  md c:\ExchangeDatabases\db003\db003.db

  dos

  md c:\ExchangeDatabases\db003\db003.log

  dos

<!-- p.2716 -->

  md c:\ExchangeDatabases\db004\db004.db

  dos

  md c:\ExchangeDatabases\db004\db004.log

Repeat the preceding commands for databases on every volume.

How do you know you successfully create the database folder
structure?
To verify you successfully created the database folder structure, run the following command.

  dos

  Dir C:\ExchangeDatabases /s

The created folders should appear in the output list.

Step 8: Create databases
Create databases with log and database paths configured with the appropriate folders. This
example illustrates how to create a database stored in the newly created folder and mount
point structure in the Exchange Management Shell.

  PowerShell

  New-MailboxDatabase -Name db001 -Server MBX1 -LogFolderPath
  C:\ExchangeDatabases\db001\db001.log -EdbFilePath
  C:\ExchangeDatabases\db001\db001.db\db001.edb

How do you know you successfully created databases?
To verify you successfully created databases in the appropriate folder, run the following
command in the Exchange Management Shell.

  PowerShell

  Get-MailboxDatabase db001 | Format List *path*

<!-- p.2717 -->

Database properties that are returned should indicate that the database file and log files are
being stored in the above folders.

How do you know you successfully configured
AutoReseed for a DAG?
To verify you successfully configured AutoReseed for a DAG, do the following steps:

   1. Run the following command in the Exchange Management Shell to verify the DAG is
     configured correctly.

       PowerShell

        Get-DatabaseAvailabilityGroup DAG1 | Format-List *auto*

   2. Run the following command to verify the folder structure is configured correctly (the
     following examples are the default paths; if necessary, substitute the paths for the paths
     you're using).

       dos

        Dir c:\ExchangeDatabases /s

       dos

        Dir c:\ExchangeVolumes /s

<!-- p.2718 -->

Configure database availability group
network properties in Exchange Server
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

Configurable properties include the name of the DAG network, a description field for the DAG
network, a list of subnets that are used by the DAG network, and whether the DAG network is
enabled for replication.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
     Estimated time to complete: 1 minute

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions topic.

     You can configure a DAG network only when automatic network configuration has been
     disabled for a DAG. For detailed steps about how to disable automatic network
     configuration for a DAG, see Configure database availability group properties.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to configure database availability
group network properties
   1. In the EAC, go to Servers > Database Availability Groups.

   2. Select the DAG you want to configure, and in the Details pane, under the DAG network
     you want to configure, choose from the following configuration options.

<!-- p.2719 -->

        ７ Note

        These options will only be visible if you have selected Configure database
        availability group networks manually on the DAG properties page.

     Disable Replication or Enable Replication: Configures the replication settings for the DAG
     network.

     Remove: Removes a DAG network. Before you can remove a DAG network, you must first
     remove all associated subnets from the DAG network.

     View details: Configures DAG network properties, such as the name, description, and
     associated subnets for the DAG network. You can also view the network interfaces
     associated with those subnets, and enable or disable replication for the DAG network.

Use the Exchange Management Shell to configure
database availability group network properties
This example adds a subnet of 10.0.0.0 and subnet mask of 255.0.0.0 to the DAG network
MapiDagNetwork in the DAG DAG1.

  PowerShell

  Set-DatabaseAvailabilityGroupNetwork -Subnets 10.0.0.0/8 -Identity
  DAG1\MapiDagNetwork

How do you know this worked?
To verify that you've successfully configured the DAG network, do the following:

     In the Exchange Management Shell, run the following command to display DAG network
     configuration settings and verify the DAG network was configured successfully.

        PowerShell

        Get-DatabaseAvailabilityGroupNetwork <DAGNetworkName> | Format-List

For more information
Set-DatabaseAvailabilityGroupNetwork

<!-- p.2720 -->

Get-DatabaseAvailabilityGroupNetwork

New-DatabaseAvailabilityGroupNetwork

Remove-DatabaseAvailabilityGroupNetwork
