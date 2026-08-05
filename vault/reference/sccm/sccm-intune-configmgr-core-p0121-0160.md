---
title: "Core infrastructure documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0121-0160
family: sccm
documentKind: "doc"
abstract: "All security assignments are replicated and available throughout the hierarchy. Role-based administration configurations replicate to each site in the hierarchy as global data, and then are applied to all administrative connections. ） Important Intersite replication delays can p"
---

# Core infrastructure documentation — pages 121-160

<!-- p.121 -->

     All security assignments are replicated and available throughout the hierarchy.
     Role-based administration configurations replicate to each site in the hierarchy as
     global data, and then are applied to all administrative connections.

        ） Important

        Intersite replication delays can prevent a site from receiving changes for role-
        based administration. For more information about how to monitor intersite
        database replication, see Data transfers between sites.

     There are built-in security roles that are used to assign the typical administration
     tasks. Create your own custom security roles to support your specific business
     requirements.

     Administrative users see only the objects that they have permissions to manage.

     You can audit administrative security actions.

Security roles
Use security roles to grant security permissions to administrative users. Security roles are
groups of security permissions that you assign to administrative users so that they can
do their administrative tasks. These security permissions define the actions that an
administrative user can do and the permissions that are granted for particular object
types. As a security best practice, assign the security roles that provide the least
permissions that are required for the task.

Configuration Manager has several built-in security roles to support typical groupings of
administrative tasks. You can create your own custom security roles to support your
specific business requirements.

The following table summarizes all of the built-in roles:

                                                                                  ﾉ    Expand table

 Name                 Description

 Application          Combines the permissions of the Application deployment manager and
 administrator        the Application author roles. Administrative users in this role can also
                      manage queries, view site settings, manage collections, edit settings for
                      user device affinity, and manage App-V virtual environments.

 Application author   Can create, modify, and retire applications. Administrative users in this role

<!-- p.122 -->

Name                 Description

                     can also manage applications, packages, and App-V virtual environments.

Application          Can deploy applications. Administrative users in this role can view a list of
deployment           applications. They can manage deployments for applications, alerts, and
manager              packages. They can view collections and their members, status messages,
                     queries, conditional delivery rules, and App-V virtual environments.

Asset manager        Grants permissions to manage the Asset Intelligence synchronization point,
                     Asset Intelligence reporting classes, software inventory, hardware inventory,
                     and metering rules.

Company resource     Grants permissions to create, manage, and deploy company resource
access manager       access profiles. For example, Wi-Fi, VPN, Exchange ActiveSync email, and
                     certificate profiles.

Compliance           Grants permissions to define and monitor compliance settings.
settings manager     Administrative users in this role can create, modify, and delete
                     configuration items and baselines. They can also deploy configuration
                     baselines to collections, start compliance evaluation, and start remediation
                     for non-compliant computers.

Endpoint             Grants permissions to create, modify, and delete endpoint protection
protection           policies. They can deploy these policies to collections, create and modify
manager              alerts, and monitor endpoint protection status.

Full administrator   Grants all permissions in Configuration Manager. The administrative user
                     who installs Configuration Manager is automatically granted this security
                     role, all scopes, and all collections.

Infrastructure       Grants permissions to create, delete, and modify the Configuration
administrator        Manager server infrastructure and to run migration tasks.

Operating system     Grants permissions to create OS images and deploy them to computers,
deployment           manage OS upgrade packages and images, task sequences, drivers, boot
manager              images, and state migration settings.

Operations           Grants permissions for all actions in Configuration Manager except for the
administrator        permissions to manage security. This role can't manage administrative
                     users, security roles, and security scopes.

Read-only analyst    Grants permissions to view all Configuration Manager objects.

Remote tools         Grants permissions to run and audit the remote administration tools that
operator             help users resolve computer issues. Administrative users in this role can run
                     remote control, remote assistance, and remote desktop from the
                     Configuration Manager console.

Security             Grants permissions to add and remove administrative users and to
administrator        associate administrative users with security roles, collections, and security

<!-- p.123 -->

 Name                Description

                     scopes. Administrative users in this role can also create, modify, and delete
                     security roles and their assigned security scopes and collections.

 Software update     Grants permissions to define and deploy software updates. Administrative
 manager             users in this role can manage software update groups, deployments, and
                     deployment templates.

   Tip

  If you have permissions, you can view the list of all security roles in the
  Configuration Manager console. To view the roles, go to the Administration
  workspace, expand Security, and then select the Security Roles node.

You can't modify the built-in security roles, other than add administrative users. You can
copy the role, make changes, and then save these changes as a new custom security
role. You can also import security roles that you've exported from another hierarchy like
a lab environment. For more information, see Configure role-based administration.

Review the security roles and their permissions to determine whether you'll use the
built-in security roles, or whether you have to create your own custom security roles.

Role permissions
Each security role has specific permissions for different object types. For example, the
application author role has the following permissions for applications:

     Approve
     Create
     Delete
     Modify
     Modify folder
     Move object
     Read
     Run report
     Set security scope

This role also has permissions for other objects.

<!-- p.124 -->

For more information on how to view the permissions for a role, or change the
permissions for a custom role, see Configure role-based administration.

Plan for security roles
Use this process to plan for Configuration Manager security roles in your environment:

   1. Identify the tasks that administrative users need to do in Configuration Manager.
     These tasks might relate to one or more groups of management tasks. For
     example, deploying operating systems and settings for compliance.

   2. Map these administrative tasks to one or more of the built-in roles.

   3. If some of the administrative users do the tasks of multiple roles, assign the users
     to the multiple roles. Don't create a custom role that combines the permissions.

   4. If the tasks that you identified don't map to the built-in security roles, create and
     test custom roles.

For more information, see Create custom security roles and Configure security roles.

<!-- p.125 -->

Collections
Collections specify the users and devices that an administrative user can view or
manage. For example, to deploy an application to a device, the administrative user
needs to be in a security role that grants access to a collection that contains the device.

For more information about collections, see Introduction to collections.

Before you configure role-based administration, decide whether you have to create new
collections for any of the following reasons:

     Functional organization. For example, separate collections of servers and
     workstations.
     Geographic alignment. For example, separate collections for North America and
     Europe.
     Security requirements and business processes. For example, separate collections
     for production and test computers.
     Organization alignment. For example, separate collections for each business unit.

For more information, see Configure collections to manage security.

Security scopes
Use security scopes to provide administrative users with access to securable objects. A
security scope is a named set of securable objects that are assigned to administrator
users as a group. All securable objects are assigned to one or more security scopes.
Configuration Manager has two built-in security scopes:

     All: Grants access to all scopes. You can't assign objects to this security scope.

     Default: This scope is used for all objects by default. When you install
     Configuration Manager, it assigns all objects to this security scope.

If you want to restrict the objects that administrative users can see and manage, create
your own custom security scopes. Security scopes don't support a hierarchical structure
and can't be nested. Security scopes can contain one or more object types, which
include the following items:

     Alert subscriptions
     Applications and application groups
     App-V virtual environments
     Boot images
     Boundary groups

<!-- p.126 -->

     Configuration items and baselines
     Custom client settings
     Distribution points and distribution point groups
     Driver packages
     Endpoint protection policies (all)
     Folders
     Global conditions
     Migration jobs
     OneDrive for Business profiles
     OS images
     OS upgrade packages
     Packages
     Queries
     Remote connection profiles
     Scripts
     Sites
     Software metering rules
     Software update groups
     Software updates packages
     Task sequences
     User data and profiles configuration items
     Windows Update for Business policies

There are also some objects that you can't include in security scopes because they're
only secured by security roles. Administrative access to these objects can't be limited to
a subset of the available objects. For example, you might have an administrative user
who creates boundary groups that are used for a specific site. Because the boundary
object doesn't support security scopes, you can't assign this user a security scope that
provides access to only the boundaries that might be associated with that site. Because
a boundary object can't be associated to a security scope, when you assign a security
role that includes access to boundary objects to a user, that user can access every
boundary in the hierarchy.

Objects that don't support security scopes include but aren't limited to the following
items:

     Active Directory forests
     Administrative users
     Alerts
     Boundaries
     Computer associations
     Default client settings

<!-- p.127 -->

     Deployment templates
     Device drivers
     Migration site-to-site mappings
     Security roles
     Security scopes
     Site addresses
     Site system roles
     Software updates
     Status messages
     User device affinities

Create security scopes when you have to limit access to separate instances of objects.
For example:

     You have a group of administrative users who need to see production applications
     and not test applications. Create one security scope for production applications
     and another for test applications.

     One group of administrative users requires Read permission to specific software
     update groups. Another group of administrative users requires Modify and Delete
     permissions for other software update groups. Create different security scopes for
     these software update groups.

For more information, see Configure security scopes for an object.

Next steps
Configure role-based administration for Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.128 -->

Configuration Manager and Windows as
a service
Article • 03/31/2025

Applies to: Configuration Manager (current branch)

Configuration Manager provides comprehensive control over feature updates for
Windows. To fully adopt the Windows as a service model, you also must adopt the
Configuration Manager current branch model. To stay current with Windows, requires
that you stay current with Configuration Manager for the best experience. New versions
of Configuration Manager are required to take full advantage of the exciting new
enterprise features for Windows. This article is intended to be a landing page for the key
articles required to adopt Configuration Manager current branch. Configuration
Manager current branch gets you on your way to Windows as a service.

Configuration Manager current branch
                                                                                ﾉ   Expand table

 Article                         Description

 Overview of Configuration       Provides a brief summary of the key points for the servicing
 Manager current branch          model for Configuration Manager current branch

 Support lifecycle               Explains the current branch support and servicing model.

 Removed and deprecated items    Provides early notice about future changes that might affect
                                 your use of Configuration Manager.

 Updates to Configuration        Explains the easy in-console method of applying feature
 Manager current branch          updates to Configuration Manager.

 Get available updates           Explains the two modes available to get new Configuration
                                 Manager feature updates.

 Update checklist                Provides update version-specific checklists, if applicable.

 Install new Configuration       Explains the simple installation steps for feature updates.
 Manager feature updates

 Support for Windows 11          Provides a support matrix for Windows 11 versions.

 Support for Windows 10          Provides a support matrix for Windows 10 versions.

<!-- p.129 -->

 Article                            Description

 Support for Windows ADK            Provides a support matrix for the Windows Assessment and
                                    Deployment Kit (Windows ADK).

 Technical Previews for             Provides information about the Configuration Manager
 Configuration Manager              technical preview program.

Windows as a service
                                                                               ﾉ    Expand table

 Article                                    Description

 Manage Windows as a service                Explains how to use servicing plans to deploy
                                            Windows feature updates.

 Upgrade Windows via task sequence          The details of creating a task sequence to upgrade
                                            Windows with additional recommendations.

 Phased deployments                         Phased deployments automate a coordinated,
                                            sequenced rollout of a task sequence across multiple
                                            collections.

 Optimize Windows update delivery           Use Configuration Manager to manage update
                                            content to stay current with Windows.

 Integrate Windows Update client policies   Explains how to define and deploy Windows Update
 (optional)                                 client policies using Configuration Manager.

 Use co-management with Microsoft           Provides an overview of co-management.
 Intune and Windows Update client
 policies (optional)

Product lifecycle
Another important aspect of staying current with Windows and Configuration Manager
is to monitor product lifecycles. Configuration Manager has built-in features to help:

     Be proactive with dashboards for planning:
           Product lifecycle dashboard: View the Microsoft Lifecycle Policy for applicable
           products.
           Windows servicing dashboard: Provides you with information about computers
           in your environment, servicing plans, and compliance information.

     Be reactive with notifications, management insights, and reports:

<!-- p.130 -->

        Configuration Manager console notifications: Look for in-console notifications
        about devices with operating systems that are past the end of support date and
        that are no longer eligible to receive security updates.
        Management insights
            Security: Identify clients with unsupported antimalware client versions or
            clients running earlier versions of Windows that don't receive security
            updates by default.
            Simplified management: Identify clients running an unsupported version of
            Windows or with an earlier version of the Configuration Manager client.
        Reports:
            Data warehouse historical reporting: View computers that are missing
            software updates.
            OS reports: View computers by OS versions and servicing details.
            Software Updates compliance reports: View software update compliance
            details.
        Power BI sample reports for software updates: Use Power BI to view software
        update compliance status.

Next steps
     In-place upgrade to Configuration Manager current branch from System Center
     2012 Configuration Manager
     Plan for migration to Configuration Manager current branch

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.131 -->

Use cloud services with Configuration
Manager
Article • 07/17/2024

Applies to: Configuration Manager (current branch)

Configuration Manager supports several cloud-based options. These can supplement
your on-premises infrastructure, and can help solve business problems like:

         How to manage clients that roam onto the internet.

         How to provide content resources to isolated clients or resources on the intranet,
         outside your firewall.

         How to scale out infrastructure when physical hardware isn't available, or isn't
         logically placed to support your needs.

Provisioning cloud resources isn't something you have to do before you deploy
Configuration Manager. It can be beneficial to understand these options before
progressing too far in a hierarchy design plan. The use of cloud resources might save
you money and time, while solving business problems that on-premises infrastructure
can't.

Cloud-based resources
Each option has different requirements. Investigate each in greater depth to understand
the unique prerequisites, limitations, and potential for additional costs based on use.

Azure virtual machines for cloud-based infrastructure
Configuration Manager supports using computers that run in virtual machines in Azure.
You can use Azure virtual machines in the following scenarios:

         Run Configuration Manager in a virtual machine and use it to manage clients
         installed in other cloud-based virtual machines.

         Run Configuration Manager in a virtual machine and use it to manage clients that
         aren't in Azure.

         Run different Configuration Manager site system roles in Azure virtual machines.
         Run other roles in your on-premises network. Configure appropriate network

<!-- p.132 -->

     connectivity for communications.

The same requirements for networks, operating systems, and hardware requirements
that apply to installing the Configuration Manager on your on-premises network also
apply to the installation of Configuration Manager in Azure.

An Azure subscription is required to use Azure virtual machines. You incur charges based
on the number of virtual machines you use, their configuration, and use of cloud-based
resources.

Additionally, Configuration Manager sites and clients that run in Azure virtual machines
are subject to the same license requirements as on-premises installations.

For more information, see Configuration Manager on Azure FAQ.

Azure services
You can connect the site to Azure for several scenarios:

     Microsoft Entra authentication and discovery. For more information, see Configure
     Azure services.
     Cloud management gateway to manage internet-based clients. For more
     information, see Cloud management gateway overview.
     Deploy apps from the Microsoft Store for Business and Education. For more
     information, see Manage apps from the Microsoft Store for Business and
     Education.
     Microsoft Intune tenant attach

These are different than using an Azure virtual machine, on which you deploy a site
system role.

     Run as a service in Azure, not on a virtual machine.

     Automatically scale to meet increased content requests from clients.

     Support clients on the internet and the intranet.

An Azure subscription is required for these scenarios. You incur charges based on the
amount of data that transfers to and from the service.

Additional Configuration Manager capabilities
Some Configuration Manager capabilities can connect to cloud-based services, like:

<!-- p.133 -->

     Windows Server Update Services (WSUS)

     Download updates for Configuration Manager

These additional capabilities don't require you to have an Azure subscription. You don't
have to set up specific connections, certificates, or services in the cloud. Instead, they are
automatically managed by Configuration Manager for you. All you need to do is ensure
applicable site systems and devices can access the internet-based URLs.

Security for cloud-based services
Configuration Manager uses certificates to provision and access your content in Azure,
and to manage the services that you use. Configuration Manager encrypts the data that
you store in Azure, but doesn't introduce additional security or data controls beyond
those that Azure provides.

For more information, see the details for the different cloud-based resource scenarios.
Also see an Introduction to Azure security.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.134 -->

Configuration Manager on Azure FAQ
Applies to: Configuration Manager (current branch)

These frequently asked questions (FAQ) about Configuration Manager on Microsoft Azure can
help you understand when to use it and how to configure it.

General questions
Can I move on-premises Configuration Manager
servers to Azure?
Yes, this scenario is supported. For more information, see Support for virtualization environments.

Should all child primary sites be in Azure with the
central administration site or on-premises? What
about secondary sites?
File-based and database replication for site-to-site communications benefit from the proximity of
being hosted in Azure. However, all client-related traffic would be remote from site servers and
site systems. If you use a fast and reliable network connection between Azure and your intranet
with an unlimited data plan, hosting all your infrastructure in Azure is an option.

If you use a metered data plan and available bandwidth or cost is a concern, then consider
placing specific sites and site systems on-premises. Then use the bandwidth controls built into
Configuration Manager. Also consider this configuration when the network connection between
Azure and your intranet isn't fast or can be unreliable.

Is Configuration Manager in Azure considered
software as a service (SaaS)?
No, it's infrastructure as a service (IaaS). You host your Configuration Manager infrastructure
servers in Azure virtual machines.

<!-- p.135 -->

What factors are most important when considering to
move Configuration Manager to Azure?
   1. Networking
   2. Availability
   3. Performance
   4. Cost
   5. User Experience

For more information on these factors, see the other questions below.

Can I use Configuration Manager with Azure
Stack Hub?
Yes. Azure Stack Hub supports IaaS virtual machines the same as the Azure cloud. So
Configuration Manager is supported on Azure Stack Hub in the same way as with Azure IaaS.

Configuration Manager cloud-attached features that rely on specific cloud services aren't
supported with Azure Stack Hub. For example, you can't create a cloud management gateway
(CMG) in Azure Stack Hub.

Networking
Should I use ExpressRoute or an Azure VPN Gateway?
Microsoft recommends using ExpressRoute. Network speeds and latency can affect functionality
between the site server and remote site systems and between any client communication to the
site systems.

There's no limitation in Configuration Manager for using Azure VPN Gateway. You should
carefully review the following requirements from this infrastructure and then make your decision:

     Performance
     Patching
     Software distribution
     OS deployment

Consider the following aspects for each solution:

<!-- p.136 -->

ExpressRoute (recommended)

     Natural extension to your datacenter and can link together multiple datacenters
     Private connections between Azure datacenters and your infrastructure
     Doesn't go over the public internet
     Offers reliability, fast speeds, lower latency, high security
     Offers up to 10 Gbps speeds and unlimited data plan options

VPN Gateway

     Site-to-site or point-to-site VPNs
     Traffic goes over the public internet
     Uses Internet Protocol Security (IPsec) and Internet Key Exchange (IKE)

For more information, see ExpressRoute or Azure VPN         .

Which ExpressRoute options should I choose?
It depends. ExpressRoute has many different options like unlimited or metered, different speed
options, and premium add-ons. The options you select depend on the Configuration Manager
functionality you're using and how much data you plan to distribute. You can control the transfer
of Configuration Manager data between site servers and distribution points, but you can't control
site server-to-site server communication. When you use a metered data plan, if you place specific
sites and site systems on-premises, and use Configuration Manager's built-in bandwidth controls,
you can help control the cost of using Azure.

Do I still need to join my site servers to an Active
Directory domain?
Yes. When you move to Azure, the supported configurations remain the same, including Active
Directory requirements for installing Configuration Manager.

Can I use Microsoft Entra ID?
No. Microsoft Entra ID isn't currently supported. Your site servers still need to be members of a
Active Directory domain.

Availability

<!-- p.137 -->

Can I use high availability options like Azure VM
availability sets with Configuration Manager?
Yes. You can use Azure VM availability sets for redundant site system roles like distribution points
or management points.

You can also use them for the Configuration Manager site servers. For example, central
administration sites and primary sites can all be in the same availability set. This configuration can
help you make sure that they're not rebooted at the same time.

For more information, see Availability options for Azure Virtual Machines and High availability
options for Configuration Manager.

Can I use an Azure SQL Server database?
No. You need to use SQL Server in a VM. Configuration Manager doesn't currently support Azure
SQL Server.

For high availability of the site database server, use SQL Server Always On availability groups. For
more information, see Prepare to use a SQL Server Always On availability group with
Configuration Manager.

Can I use Azure load balancers with site system roles
like management points or software update points?
Configuration Manager isn't tested with Azure load balancers. If the functionality is transparent to
the application, it shouldn't have any adverse effects on normal operations.

Performance
What factors affect performance in this scenario?
The following factors are the most important to Configuration Manager performance on Azure:

     Azure VM size and type
     Azure VM disks: premium storage is recommended, especially for SQL Server
     Network latency and speed

What size VMs should I use?

<!-- p.138 -->

In general, your compute power (CPU and memory) need to meet the recommended hardware
for Configuration Manager. But there are some differences between regular computer hardware
and Azure VMs, especially when it comes to the disks these VMs use. The VM size you use
depends on the size of your environment.

The following list includes some general recommendations for VM size:

     For production deployments of any significant size, use S class Azure VMs. These VMs can
     use premium storage disks. Non S class VMs use blob storage and in general won't meet
     the performance requirements necessary for an acceptable production experience.
     Use multiple premium storage disks for higher scale, and striped in the Windows Disk
     Management console for maximum IOPS.
     Use better or multiple premium disks during your initial site deployment. For example, P30
     instead of P20, and two P30 disks in a striped volume, instead of a single P30. If your site
     later needs to increase VM size due to additional load, you can take advantage of the
     additional CPU and memory that a larger VM size provides. You'll also already have disks in
     place that can take advantage of the additional IOPS throughput that the larger VM size
     allows.

The following tables list the initial suggested disk counts to use at primary and central
administration sites for various size installations:

Co-located site database

A primary or central administration site with the site database on the site server:

                                                                                        ﾉ   Expand table

   Desktop clients               Recommended VM size                  Recommended disks

   < 25,000                      DS4_V2                               2xP30 (striped)

   25,000 to 50,000              DS13_V2                              2xP30 (striped)

   50,000 to 100,000             DS14_V2                              3xP30 (striped)

Remote site database

A primary or central administration site with the site database on a remote server:

<!-- p.139 -->

                                                                                  ﾉ   Expand table

  Desktop clients          Recommended VM size              Recommended disks

  < 25,000                 Site server: F4S                 Site server: 1xP30
                           Database server: DS12_V2         Database server: 2xP30 (striped)

  25,000 to 50,000         Site server: F4S                 Site server: 1xP30
                           Database server: DS13_V2         Database server: 2xP30 (striped)

  50,000 to 100,000        Site server: F8S                 Site server: 2xP30 (striped)
                           Database server: DS14_V2         Database server: 3xP30 (striped)

Example

This image shows an example disk configuration for the following VM:

     A DS14_V2 size VM for a site that manages 50,000 to 100,000 clients
     Three P30 disks in a striped volume
     Separate logical volumes for the Configuration Manager install and database files

<!-- p.140 -->

User experience
Why is user experience a main area of importance?
The decisions you make for networking, availability, performance, and site server location can
directly affect your users. Moving a site to Azure should be transparent to your users so that they
don't experience a change in their day-to-day interactions with Configuration Manager.

To keep costs low for a single primary site, should
remote site systems be in Azure or on-premises?
Except for communication from the site server to a distribution point, these server-to-server
communications in a site can occur at any time and don't use mechanisms to control the use of
network bandwidth. Because you can't control the communication between site systems like

<!-- p.141 -->

management points and software update points, make sure to consider any costs associated with
these communications.

Network speeds and latency are other factors to consider as well. Slow or unreliable networks
could impact functionality between the site server and remote site systems, and client
communication to the site systems. Factor in the number of managed clients that use a given site
system and the features you actively use.

As a starting point, you can use the standard guidance for site systems across WAN links. Ideally,
the network throughput that you select and receive between Azure and your intranet will be
consistent with a WAN that is well-connected with a fast network.

What about content distribution and
content management?
The approach for content management is much the same as for site servers and site systems.

     If you use a fast and reliable network connection between Azure and your intranet with an
     unlimited data plan, hosting standard distribution points in Azure could be an option.

     If any of the following factors apply:
        You use a metered data plan
        Bandwidth cost is a concern
        The network connection between Azure and your intranet isn't fast or can be unreliable

     Then you might consider the following other approaches:
        Use standard or pull distribution points on-premises.
        Enable Windows BranchCache on distribution points or other peer caching technologies.
        Use a content-enabled cloud management gateway (CMG). Note that it doesn't support
        software update packages for Microsoft updates. You need to have an alternate location,
        or configure the software update deployment need to allow clients to get update
        content from the internet.

  ７ Note

  If you require PXE or multicast support, you need an on-premises distribution point to
  respond to these boot requests.

<!-- p.142 -->

To support internet-based clients, what
can I do instead of using an internet-facing
management point?
Use a cloud management gateway (CMG). The CMG provides a simple way to manage
Configuration Manager clients on the internet. You deploy the service to an Azure subscription,
and it connects to your on-premises infrastructure through the cloud management gateway
connector point. Clients can then access on-premises site system roles whether they're connected
to the internal network or on the internet.

Which peer caching technology should I use?
Peer cache is a 100% native Configuration Manager technology. BranchCache and Delivery
Optimization are Windows features. They can all be useful depending upon your requirements.
For more information, including a table to compare features, see Content management
fundamentals - Peer caching technologies.

Cost
Will moving Configuration Manager to Azure be a
cost-effective solution for my organization?
It's hard to say since every environment is different. To estimate the cost for your environment,
use the Azure pricing calculator   .

More information
Where I can learn more about these
Azure technologies?
Fundamentals

     What is Azure

Azure VM machine types

     Azure machine sizes

<!-- p.143 -->

     VM pricing
     Storage pricing

Disk performance considerations

     Premium storage
     Select a disk type of IaaS VMs
     Scalability and performance targets for standard storage accounts
     Blog post on how premium storage works

Availability

     Azure service level agreement (SLA) for virtual machines
     Availability options for Azure Virtual Machines

Connectivity

     ExpressRoute or Azure VPN
     Azure ExpressRoute pricing
     What is Azure ExpressRoute?

Last updated on 01/29/2026

<!-- p.144 -->

Frequently asked questions for
Configuration Manager branches
and licensing
Applies to: Configuration Manager (current branch) & System Center Configuration Manager (long-
term servicing branch)

This FAQ addresses common licensing questions about Configuration Manager current branch
and the long-term servicing branch (LTSB) versions, available through Microsoft Volume Licensing
programs. This article is for informational purposes. It doesn't supersede or replace any
documentation covering Configuration Manager licensing. For more information, see the Product
Terms   . The Product Terms describe the use terms for all Microsoft products in Volume
Licensing.

What's current branch?
The current branch is the production-ready build of Configuration Manager that provides an
active servicing model. This servicing model is like the experience with Windows. This approach
supports customers who are moving at a cloud cadence and wish to innovate more quickly. With
the current branch servicing model, you continue to receive new features and functionality. For
this reason, only customers with active Software Assurance on Configuration Manager licenses, or
with equivalent subscription rights, may install and use the current branch of Configuration
Manager.

What's the long-term servicing branch (LTSB)?
The LTSB is a production-ready build of Configuration Manager. It's intended for customers who
allow Software Assurance or equivalent subscription rights to expire. When compared to the
current branch, the LTSB has reduced functionality. Customers who allow Software Assurance or
equivalent subscription rights to expire must uninstall the current branch of Configuration
Manager. Customers who have perpetual license rights to Configuration Manager may then
install and use the LTSB build of the Configuration Manager version that's current at the time of
expiration.

<!-- p.145 -->

What do the acronyms 'SA' and 'L&SA' mean in
regard to Configuration Manager?
Both Software Assurance (SA) and License and Software Assurance (L&SA) are license options
that grant rights to use Configuration Manager. SA is an option for a customer that's renewing
SA coverage from a prior agreement. L&SA is an option for a customer buying a new license and
SA coverage.

     Software Assurance (SA): Customers must have active SA on Configuration Manager
     licenses, or equivalent subscription rights, in order to install and use the current branch
     option of Configuration Manager.

     While SA is optional for some Microsoft products, the only way to get rights to use
     Configuration Manager current branch is with SA or equivalent subscription rights. For more
     information, see the Software Assurance FAQ      .

     Microsoft License and Software Assurance (L&SA): Customers buying new licenses for
     Configuration Manager must acquire L&SA (the license and SA coverage).

        The SA grants rights to use the current branch.

        If your SA expires, and you still have a license for Configuration Manager, you can no
        longer use the current branch. For more information, see the FAQ If my SA expires and I
        had L&SA, what do I get?

For more information about license offerings, see Ways to buy      and Licensing Product Terms     .

What are 'equivalent subscriptions'?
Equivalent subscriptions refer to programs like Enterprise Mobility + Security    (EMS) or
Microsoft 365 Enterprise   . There can be others, but these programs are the most common. The
Microsoft Volume Licensing Product Terms refers to these programs as Management License
Equivalent Licenses.

Configuration Manager is included in the following plans:

     Intune user subscription license (USL)
     EMS E3
     EMS E5
     Microsoft 365 E3

<!-- p.146 -->

     Microsoft 365 E5
     Microsoft 365 F3 (formerly Microsoft 365 F1)

  ） Important

  Configuration Manager isn't included in the Microsoft 365 Business Premium          plan.

What changes with licensing for co-
management in the Microsoft Intune family
of products?
The co-management license lets Configuration Manager customers with Software Assurance get
Intune PC management rights without having to purchase and assign individual Intune licenses to
users. This license makes it easier for you to manage Windows devices with Microsoft Intune and
Configuration Manager.

     Devices already managed by Configuration Manager that you enroll to Intune for co-
     management have almost the same rights as an Intune standalone-managed PC. If you
     reset Windows on this device, you can't provision it with Windows Autopilot. Windows
     Autopilot requires a full Intune license.

     If you enroll a Windows device to Intune by other means, it still requires a full Intune license.
     For example, you use Windows Autopilot to provision a device, or a user manually does
     self-service enrollment.

     For existing Configuration Manager-managed devices to enroll into Intune for co-
     management at scale without user interaction, co-management uses an Azure Active
     Directory (Azure AD) feature called Windows auto-enrollment. Auto-enrollment with co-
     management requires licenses for both Microsoft Entra ID P1 or P2 (AADP1) and Intune.
     Starting on December 1, 2019, you no longer need to assign individual Intune licenses for
     this scenario. Microsoft Intune and Configuration Manager each include the licenses for co-
     management. The separate AADP1 licensing requirement remains the same for this scenario
     to work. You still need to assign Intune licenses for other enrollment scenarios.

     If you want to use Intune for managing iOS, Android, or macOS devices, then you need the
     appropriate Intune subscription through a standalone Intune license, Enterprise Mobility +
     Security (EMS), or Microsoft 365.

<!-- p.147 -->

  If you don't have any Intune-related subscription plan, to support co-management you
  need to purchase at least one Intune license. This license is for an administrator to activate
  the subscription plan and get access to the Microsoft Intune admin center.

  If you use the Microsoft 365 built-in Basic Mobility and Security , you can't use the new
  co-management license for a user that also has devices managed by Basic Mobility and
  Security. To use the co-management license for the user's Configuration Manager-managed
  device, do one of the following actions:
      Assign a full Intune license to the user, and manage their devices through Intune.
      Unenroll the devices from Basic Mobility and Security.

  The licensing that you previously had for System Center Configuration Manager still applies
  to Microsoft Configuration Manager. If installing a new site, use existing product keys.

                                                                                ﾉ     Expand table

Feature                             Co-management license                       Full Intune
                                                                                license

Windows enrollment                  Yes (only for existing ConfigMgr-           Yes
                                    managed devices)

iOS, Android, macOS enrollment      No                                          Yes

Windows Autopilot                   No                                          Yes

Mobile Application Management       No                                          Yes
(MAM)

Conditional Access                  Yes                                         Yes
(additional AADP1 required)

Device profiles                     Yes                                         Yes

Software update management          Yes                                         Yes

Inventory                           Yes                                         Yes

App management                      Yes                                         Yes

<!-- p.148 -->

   Feature                             Co-management license                      Full Intune
                                                                                  license

   Remote Full/Selective wipe          Yes                                        Yes

   Remote assistance                   Yes                                        Yes
   (TeamViewer license required)

   Tenant attach                       Yes                                        N/A

   Endpoint analytics                  Yes                                        Yes

For more information, see the following articles:

     Co-management prerequisites
     Windows Autopilot requirements
     Tenant attach prerequisites
     Endpoint analytics licensing prerequisites
     Use Conditional Access with Intune
     TeamViewer prerequisites

I have Enterprise Mobility + Security and it
expired, what must I do now?
EMS grants rights to use Configuration Manager current branch and long-term service branch.
When these rights expire, you no longer have rights to use either branch and must uninstall.

If my SA expires, and I had L&SA, what do
I get?
If your SA expired after October 1, 2016, depending on what program you acquired L&SA under,
you could retain a perpetual license to use the LTSB. If you currently use the current branch, you
must uninstall it, and then install the LTSB. There's no support to migrate or convert to the LTSB
from the current branch.

If your SA expired before October 1, 2016, and you retained a perpetual license to Configuration
Manager, then your only option for ongoing use is to install and use System Center 2012 R2

<!-- p.149 -->

Configuration Manager and its available service packs. You're required to uninstall the current
branch when your SA expires, and reinstall that earlier version of the product. There's no support
to migrate to or downgrade from Configuration Manager current branch to prior versions of
Configuration Manager.

If you use System Center Endpoint Protection, and your SA expires, you must uninstall it. System
Center Endpoint Protection offers no L (License) rights, and no perpetual rights.

Do I "own" the current branch?
No. You're licensed to use the current branch while you have active SA. For example, via L&SA,
when SA expires, you then have only L (License) rights, which don't include rights to use the
current branch. If your L provides perpetual rights, you can use the Configuration Manager LTSB
in place of the current branch. If your SA expired prior to October 1, 2016, you can also use
System Center 2012 R2 Configuration Manager.

Can I purchase Configuration Manager
standalone without SA?
No. The only way to get rights to use Configuration Manager is to acquire a license with SA or
through an equivalent subscription. There are developer programs like MSDN where
Configuration Manager is offered for development and test purposes, but not production usage.

Does a non-production environment
for testing or development require an
explicit license?
     If you use the same current branch software as your production environment, you need an
     explicit license. Check with your account team to determine if your specific license
     agreement covers multiple instances in multiple environments.

     Some developer programs like MSDN offer products like Configuration Manager for
     development and test, but not production use.

     For a temporary environment, you can use the evaluation version       for 180 days.

     For a lab environment, you can use the technical preview branch. Technical preview has the
     same functionality as current branch, but has some limitations in terms of scale and

<!-- p.150 -->

        supported platforms.

Do I have rights to install any update in the
Configuration Manager console?
If you have active SA, you do have rights.

If you don't have active SA, uninstall the current branch, and then install the LTSB of
Configuration Manager. The LTSB doesn't receive updates for incremental versions of
Configuration Manager, but does receive security updates based on the Support Lifecycle.

I have purchased EMS or Microsoft 365
through a Cloud Solution Provider (CSP), do I
have rights to use Configuration Manager?
Yes, you have rights to use Configuration Manager to manage clients covered by the EMS license.
First download and install the evaluation software    . Then contact your CSP partner to obtain the
license key from the Microsoft Partner Center support team, specifically CSP. When your CSP
partner talks with Microsoft Support, they should ask them to reference the internal article ID
5037094.

Is my subscription end-date the same as an SA
expiration date?
If SA or your subscription is active, you have use rights for Configuration Manager current branch.
An active subscription is equivalent of having active SA, but no perpetual "L" (license). Once your
subscription is over, uninstall the current branch. At this time, you don't have rights to use the
LTSB.

What are the use rights associated with the
SQL Server technology provided with
Configuration Manager?
Configuration Manager includes SQL Server technology. Microsoft's licensing terms for this
product allows your use of SQL Server technology only to support Configuration Manager

<!-- p.151 -->

components. SQL Server client access licenses are not required for that use.

Approved use rights for the SQL Server capabilities with Configuration Manager include:

      Site database role
      Windows Server Update Services (WSUS) for software update point role
      SQL Server Reporting Services (SSRS) for reporting point role
      Data warehouse service point role
      Database replicas for management point roles

The SQL Server license that's included with Configuration Manager supports each instance of SQL
Server that you install to host a database for Configuration Manager. However, only databases for
Configuration Manager in the preceding list can run on that SQL Server when you use this
license. If a database for any additional Microsoft or third-party product shares the SQL Server,
you must have a separate license for that SQL Server instance.

Does on-premises mobile device management
(MDM) require an Intune subscription?
No. An Intune connection isn't required for new on-premises MDM deployments. Your
organization still requires Intune licenses to use this feature. For more information, see the Intune
support blog post       .

 Last updated on 04/16/2026

<!-- p.152 -->

Which branch of Configuration Manager
should I use?
Article • 10/04/2022

Applies to: Configuration Manager (current branch & technical preview branch) & System
Center Configuration Manager (long-term servicing branch)

There are three branches of Configuration Manager available:

      Current branch
      Long-term servicing branch
      Technical preview branch

Use this article to help you choose the right branch.

   Tip

  All sites in a hierarchy must run the same branch. It isn't supported to have a
  hierarchy with different branches at different sites.

Current branch
This branch is licensed for use in a production environment. Use this branch to get the
latest features and functionalities. If you have one of the following licenses, you can use
this branch:

      System Center Datacenter
      System Center Standard
      System Center Configuration Manager
      Equivalent subscription rights

For more information about Software Assurance and licensing options, see Licensing
and branches for Configuration Manager and Frequently asked questions for
Configuration Manager branches and licensing.

Microsoft plans to release updates for Configuration Manager current branch a few
times per year. Each update version remains in support for 18 months from its general
availability (GA) release date. Technical support is provided for the entire period of
support. However, our support structure is dynamic, evolving into two distinct servicing
phases that depend on the availability of the latest current branch version. (For more

<!-- p.153 -->

information, see Support for Configuration Manager current branch versions. Updates to
newer versions are available as in-console updates.

To install the current branch as a new site, use baseline media. Also use baseline media
to upgrade from System Center 2012 Configuration Manager with Service Pack 2 or
System Center 2012 R2 Configuration Manager with Service Pack 1. Access to this media
depends on how your organization licenses Configuration Manager.

You can also use the baseline media to install a new site that is an evaluation edition of
the current branch. The evaluation edition doesn't require a license. You can use the
evaluation edition for 180 days. It supports upgrade to a licensed edition of the current
branch. To install only an evaluation edition, get it from the Evaluation Center   .

  Use baseline media to install sites for a new Configuration Manager hierarchy. If you
  previously installed a baseline version, use in-console updates to update your sites
  to a new version.

  Sites that are updated using in-console updates result in sites that are the same as
  the new site installed using the baseline media.

  For more information, see Updates for Configuration Manager.

Features of the current branch
     Receives in-console updates that make new features available for use.
     Receives in-console updates that deliver security and quality fixes to existing
     features.
     Supports out-of-band updates when necessary. For more information, see Use the
     update registration tool or Use the hotfix installer.
     Integrates with cloud-based services.
     Supports migration of data to and from other Configuration Manager installations.
     Supports upgrade from previous versions of Configuration Manager.
     Supports installation as an evaluation edition, from which you can later upgrade to
     a fully licensed installation.

Microsoft recommends that you update to the newest version soon after its release. You
can wait up to 18 months before updating to a newer version. You can also skip an
update to install the newest version available. Because each version is cumulative, if you
skip over an update and install the newest version, you still get access to all features and
improvements from previous versions.

For more information, see Support for current branch versions.

<!-- p.154 -->

Current branch update options
     With active Software Assurance, you can install in-console updates for current
     branch versions.
     There's no option to convert the current branch to a technical preview branch.
     Technical preview branches are separate installations that don't require a license.
     There's no option to convert your current branch to the long-term servicing branch
     (LTSB). You must uninstall the current branch and then install the LTSB as a new
     installation.

Long-term servicing branch
This branch is licensed for use in production for Configuration Manager customers who
are using the current branch and have allowed their Configuration Manager Software
Assurance (SA) or equivalent subscription rights to expire after October 1, 2016. For
more about Software Assurance and licensing options, see Licensing and branches for
Configuration Manager and Frequently asked questions for Configuration Manager
branches and licensing.

The LTSB is based on version 1606. This branch doesn't receive in-console updates that
deliver new features or update existing capabilities. However, critical security fixes are
provided. To install the LTSB, you must use the version 1606 baseline media that you get
with System Center 2016. Later baseline versions don't support install of the LTSB.

To install the LTSB as a new site or as an upgrade from a supported System Center 2012
Configuration Manager site, use the version 1606 baseline media that you get with
System Center 2016. You can use baseline media to install a new site that runs version
1606 of the current branch, or a new site that runs the long-term servicing branch.

   Tip

  To learn about System Center 2016, see System Center 2016 documentation. This
  documentation also identifies how to get System Center 2016, which requires a
  Microsoft license agreement or similar rights.

  To find Configuration Manager version 1606 in the Volume Licensing Service Center
  (VLSC), go to the Downloads and Keys tab of the VLSC , search for System Center
  2016 , and then select either System Center 2016 Datacenter or System Center 2016

  Standard.

<!-- p.155 -->

  You can also get an evaluation edition of System Center 2019 from the Evaluation
  Center   .

Features of the LTSB
     Receives in-console updates that deliver critical security fixes.
     Provides an installation option when your SA agreement or equivalent rights to
     Configuration Manager have expired.
     Supports upgrade (conversion) to the current branch when you have a current SA
     agreement or equivalent rights to Configuration Manager.

LTSB limitations
The LTSB is based on the current branch version 1606 and has the following limitations:

     The LTSB is supported for 10 years of critical security updates after its general
     availability (October 2016), after which, support for this branch expires. For more
     information about the support lifecycle, see Microsoft Lifecycle Policy   .
     Supports a limited set list of server and client operating systems and related
     technologies, like SQL Server versions. For more information, see Supported
     configurations for the long-term servicing branch.
     Doesn't receive updates for new features
     Doesn't support the following capabilities:
        Cloud-attached features like co-management or tenant attach
        On-premises MDM
        The Windows servicing dashboard, servicing plans, or Windows release channels
        Future releases of Windows 10 LTSB and Windows Server
        Asset intelligence
        Any pre-release features

LTSB update options
     You can convert your LTSB install to a current branch installation. Conversion to the
     current branch is supported before or after support for the LTSB expires.

     To convert, you must have an active Software Assurance agreement with Microsoft.
     For more information, see the following articles:
        Upgrade the long-term servicing branch to the current branch
        Licensing and branches for Configuration Manager
        Baseline and update versions

<!-- p.156 -->

     There's no option to convert the LTSB to a technical preview branch. Technical
     preview branches are separate installations that don't require a license.

     You can't upgrade an evaluation edition of the current branch to an LTSB
     installation.

Technical preview branch
The technical preview branch is for use in a lab environment. Learn about and try out
the newest features being developed for Configuration Manager. It isn't supported in a
production environment, and doesn't require you to have a Software Assurance license
agreement.

To install a new site that runs the technical preview branch, use the latest baseline media
for the technical preview branch. After you install the technical preview branch, new
versions are available as in-console updates each month.

Features of the technical preview branch
     Based on recent baseline versions of the current branch
     Receives in-console updates that update your installation to the latest technical
     preview branch version
     Includes new features that are being developed, and for which Microsoft wants
     your feedback
     Receives updates that apply only to the technical preview branch

Technical preview limitations
     Support is limited, including only a single primary site and up to 10 clients.
     You can't upgrade or migrate it to a current branch or LTSB installation.
     Doesn't support the following behaviors:
        Use migration to import or export data to another Configuration Manager
        installation
        Upgrade from a previous version of Configuration Manager
        Install as an evaluation edition

Features that are first introduced in a technical preview branch are often added to the
current branch in a later update. Each new technical preview branch version includes the
features from previous technical preview branches, even after those features have been
added to the current branch.

For more information, see the Technical preview for Configuration Manager.

<!-- p.157 -->

Technical preview update options
     You can install any in-console update for a new technical preview branch version.

     There's no option to convert a technical preview branch to the current branch or
     LTSB.

Identify your version and branch

Version
To check the version of your site, in the console go to About Configuration Manager at
the upper-left corner of the console. This dialog displays the Site version. For a list of
site versions, see Baseline and update versions.

Branch
To confirm the branch of your site, in the console go to Administration > Site
Configuration > Sites, and open Hierarchy Settings. If there's an active option to
convert to the current branch, the site runs the LTSB version. When the site runs the
current branch, the console disables this option.

For more information about the different versions of Configuration Manager, see
Baseline and update versions.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.158 -->

Licensing and branches for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch), & System Center Configuration
Manager (long-term servicing branch)

Use this article to learn about the licensing requirements for the installation options
available with Configuration Manager. These installation options include the following
branches:

      Current branch
      Long-term servicing branch (LTSB)
      Evaluation installation of the current branch
      Technical preview branch

Licensing overview
Customers with active Software Assurance (SA) on Configuration Manager licenses or
with equivalent subscription rights as of October 1, 2016 have rights to use the October
2016 version 1606 release of Configuration Manager. Customers with rights to
Configuration Manager on or after October 1, 2016 will find two licensed options upon
installation: current branch and long-term servicing branch (LTSB).

For the complete terms and conditions for the products you purchase through Microsoft
Volume Licensing programs, see Licensing Terms and Documentation          .

Licensed branches
This article references the Software Assurance agreement or equivalent subscription
rights. This Microsoft licensing agreement grants rights to install and use Configuration
Manager.

Current branch
The current branch requires an active Software Assurance agreement or equivalent
rights to Configuration Manager. For more information, see Software Assurance and the
Current Branch.

<!-- p.159 -->

This branch is supported for use in production environments that want to receive
regular quality and feature updates from Microsoft. It provides access to use all features
and improvements.

Beginning with the 1710 release, each update version remains in support for 18 months
from its general availability release date. For more information, see Support for
Configuration Manager current branch versions.

Long-term servicing branch (LTSB)
The LTSB requires a current Software Assurance agreement with Microsoft as of October
1, 2016. For more information, see Software Assurance and the LTSB.

This branch is supported for use in production environments. It's intended for use by
customers that have let their Software Assurance (SA) or equivalent subscriptions rights
to Configuration Manager expire after October 1, 2016. This branch is limited when
compared to the Current Branch.

Critical security updates for Configuration Manager are made available to this branch
but no new features are made available.

Evaluation installation of the current branch
The evaluation version doesn't require a Software Assurance agreement with Microsoft.
Evaluation installs   are always the current branch, and you can use them for 180 days.

You can upgrade the evaluation installation to a full installation of the current branch.
You can't upgrade an evaluation installation to the long-term servicing branch.

Technical preview branch
The technical preview branch     is also available. This branch is a limited build of
Configuration Manager that lets you try out new features. You install the technical
preview using different media than the licensed versions. For more information, see
Technical Preview.

Software Assurance agreements
The status of Software Assurance on your Configuration Manager licenses, or equivalent
subscription rights, on or after October 1, 2016, determines the branch you can install
and use.

<!-- p.160 -->

Software Assurance and the current branch
Rights to use Configuration Manager current branch can be provided by:

     System Center: Customers with active SA on System Center Standard or
     Datacenter licenses can install and use the current branch option of Configuration
     Manager.

     System Center Configuration Manager: Customers with active SA on
     Configuration Manager licenses, or with equivalent subscription rights, can install
     and use the current branch option of Configuration Manager.

If you have active SA on Configuration Manager licenses or equivalent subscription
rights on or after October 1, 2016:

     You can install and use the current branch.
     If you allow SA or subscription to lapse, you must uninstall the current branch.

Software Assurance and the LTSB
If you have an active SA on Configuration Manager licenses or equivalent subscription
rights on or after October 1, 2016:

     You can install and use the LTSB. Customers who have perpetual rights to
     Configuration Manager, or who allow their SA or subscription to lapse, can install
     the version of Configuration Manager LTSB that's current at the time of lapse.

LTSB is based on current branch version 1606, and has the following limitations:

     There's no support to convert a current branch to the LTSB. If you currently have a
     current branch site, you must install the LTSB as a new site.

     LTSB doesn't support all the capabilities of the current branch. For more
     information, see Introduction to the long-term servicing branch. These limitations
     include a limited feature set, limited upgrade options, and a separate product
     support lifecycle.

Software Assurance expiration date
Beginning with the October 2016 release of the version 1606 baseline media for
Configuration Manager, you can specify the expiration date of your Software Assurance
agreement. The Software Assurance expiration date is an optional value as a
