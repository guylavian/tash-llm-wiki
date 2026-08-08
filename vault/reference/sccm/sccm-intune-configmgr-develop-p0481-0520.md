---
title: "Configuration Manager SDK documentation — pages 481-520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0481-0520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0481-0520
family: sccm
documentKind: "doc"
abstract: "Report name Description Objects that failed to migrate Displays a list of objects that failed to migrate during the last attempt. Network The following six reports are listed under the Network category. ﾉ Expand table Report name Description Count IP addresses by subnet Displays"
---

# Configuration Manager SDK documentation — pages 481-520

<!-- p.481 -->

 Report name                                  Description

 Objects that failed to migrate               Displays a list of objects that failed to migrate during
                                              the last attempt.

Network
The following six reports are listed under the Network category.

                                                                                    ﾉ   Expand table

 Report name                          Description

 Count IP addresses by subnet         Displays the number of IP addresses inventoried for each IP
                                      subnet.

 IP - All subnets by subnet mask      Displays a list of IP subnets and subnet masks.

 IP - Computers in a specific         Displays a list of computers and IP information for a specified
 subnet                               IP subnet.

 IP - Information for a specific      Displays summary information about IP on a specified
 computer                             computer.

 IP - Information for a specific IP   Displays summary information about a specified IP address.
 address

 MAC - Computers for a specific       Displays the computer name and IP address of computers that
 MAC address                          have the specified MAC address.

Operating system
The following 10 reports are listed under the Operating System category.

                                                                                    ﾉ   Expand table

 Report name                               Description

 Computer operating system version         Displays the inventory history for the operating system
 history                                   on a specified computer.

 Computers with a specific operating       Displays computers with a specified operating system.
 system

 Computers with a specific operating       Displays computers with a specified operating system
 system and service pack                   and service pack.

<!-- p.482 -->

 Report name                             Description

 Count operating system versions         Displays the number of computers inventoried by
                                         operating system.

 Count operating systems and service     Displays the number of computers inventoried by
 packs                                   operating system and service pack combinations.

 Services - Computers running a          Displays a list of computers running a specified service.
 specific service

 Services - Computers running            Displays a list of computers running Remote Access
 Remote Access Server                    Server.

 Services - Services information for a   Displays summary information about the services on a
 specific computer                       specified computer.

 Windows Servicing details for a         Displays general information about Windows servicing
 specific collection                     for a specific collection.

 Windows Server computers                Displays a list of computers that run Windows Server
                                         operating systems.

Power management
The following 18 reports are listed under the Power Management category.

                                                                                  ﾉ   Expand table

 Report name                    Description

 Power Management -             Displays a graph showing monitor, computer, and user activity for
 Computer activity              a specified collection over a specified time period.

 Power Management -             Displays a graph showing monitor, computer, and user activity for
 Computer activity by           a specified computer on a specified date.
 computer

 Power Management -             Displays a list of the sleep and wake capabilities of computers in
 Computer activity details      the specified collection for a specified date and time.

 Power Management -             Displays detailed information about the power capabilities, power
 Computer details               settings, and power plans applied to a specified computer.

 Power Management -             Displays a list of computers not reporting any power activity for a
 Computer not reporting         specified date and time.
 details

<!-- p.483 -->

 Report name                  Description

 Power Management -           Displays a list of computers excluded from the power plan.
 Computers excluded

 Power Management -           Displays a list of computers that have multiple, conflicting power
 Computers with multiple      settings applied.
 power plans

 Power Management -           Displays the total monthly energy consumption (in kWh) for a
 Energy consumption           specified collection over a specified time period.

 Power Management -           Displays the total energy consumption (in kWh) for a specified
 Energy consumption by day    collection in the last 31 days.

 Power Management -           Displays the total monthly energy consumption cost for a
 Energy cost                  specified collection over a specified time period.

 Power Management -           Displays the total energy consumption cost for a specified
 Energy cost by day           collection over the past 31 days.

 Power Management -           Displays a graph showing carbon dioxide (CO2) emissions
 Environmental impact         generated by a specified collection over a specified time period.

 Power Management -           Displays a graph showing CO2 emissions generated by a specified
 Environmental impact by      collection over the past 31 days.
 day

 Power Management -           Displays detailed information about computers that didn't sleep
 Insomnia computer details    or hibernate within a specified time period.

 Power Management -           Displays a list of common causes that prevented computers from
 Insomnia report              sleeping or hibernating. It also shows the number of computers
                              affected by each cause over a specified time period.

 Power Management - Power     Displays the power management capabilities of computers in the
 capabilities                 specified collection.

 Power Management - Power     Displays an aggregated list of power settings used by computers
 settings                     in a specified collection.

 Power Management - Power     Used to display further information about computers that were
 settings details             specified in the Power Management - Power settings report.

Replication traffic
The following 10 reports are listed under the Replication Traffic category.

                                                                               ﾉ   Expand table

<!-- p.484 -->

 Report name                            Description

 Global Data Replication Traffic Per    Displays total global data replication traffic on a specified
 Link (line chart)                      link for a specified number of days.

 Global Data Replication Traffic Per    Displays total global data replication traffic on a specified
 Link (pie chart)                       link for a specified number of days.

 Hierarchy Replication Traffic By       Displays total replication traffic for each link in the hierarchy
 Link                                   for a specified number of days.

 Hierarchy Top Ten Replication          Displays the replication traffic for the top 10 replication
 Groups Traffic Per Link (pie chart)    groups across the entire hierarchy identified by link.

 Link Replication Traffic               Displays total replication traffic for all data for a specified
                                        number of days.

 Replication group traffic per link     Displays the replication group network traffic over a
                                        specified database replication link for a specified number of
                                        days.

 Site Data Replication Traffic Per      Displays total site data replication traffic on a specified link
 Link (line chart)                      for a specified number of days.

 Site Data Replication Traffic Per      Displays total site data replication traffic on a specified link
 Link (pie chart)                       for a specified number of days.

 Total Hierarchy Replication Traffic    Displays hierarchy aggregate global and site data replication
 (line chart)                           for each direction of every link for a specified number of
                                        days.

 Total Hierarchy Replication Traffic    Displays hierarchy aggregate global and site data replication
 (pie chart)                            for each direction of every link for a specified number of
                                        days.

Site - Client information
The following 19 reports are listed under the Site - Client Information category.

                                                                                       ﾉ   Expand table

 Report name                           Description

 Client assignment detailed status     Displays detailed information about client assignment status.
 report

 Client assignment failure details     Displays detailed information about client assignment
                                       failures.

<!-- p.485 -->

Report name                         Description

Client assignment status details    Displays overview information about client assignment
                                    status.

Client assignment success details   Displays detailed information about successfully assigned
                                    clients.

Client deployment failure report    Displays detailed information for clients that have failed to
                                    deploy.

Client deployment status details    Displays summary information for the status of client
                                    installations.

Client deployment success           Displays detailed information for clients that have
report                              successfully deployed.

Clients incapable of HTTPS          Displays detailed information about each client that runs the
communication                       HTTPS Communication Readiness Tool, and reports to be
                                    incapable of communicating over HTTPS.

Computers assigned but not          Displays a list of computers assigned to a specified site, but
installed for a particular site     aren't reporting to that site.

Computers with a specific           Displays a list of computers running a specified version of the
Configuration Manager client        Configuration Manager client software.
version

Count of clients and protocol       Displays a summary of the communication methods used by
used for communication              clients (HTTP or HTTPS).

Count of clients assigned and       Displays the number of computers assigned and installed for
installed for each site             each site. Clients with a network location associated to
                                    multiple sites are only counted as installed if they're
                                    reporting to that site.

Count of clients capable of         Displays detailed information about each client that runs the
HTTPS communication                 HTTPS Communication Readiness Tool, and reports to be
                                    either capable or incapable of communicating over HTTPS.

Count of clients for each site      Displays the number of Configuration Manager clients
                                    installed by site code.

Count of Configuration Manager      Displays the number of computers discovered by
clients by client versions          Configuration Manager client version.

Problem details reported to the     Displays detailed information for issues reported by clients in
fallback status point for a         a specified collection. These clients must have an assigned
specified collection                fallback status point.

Problem details reported to the     Displays detailed information about issues reported by
fallback status point for a         clients in a specified site. These clients must have an assigned

<!-- p.486 -->

 Report name                             Description

 specified site                          fallback status point.

 Summary of problems reported            Displays information about all the issues reported by clients.
 to the fallback status point            These clients must have an assigned fallback status point.

 Summary of problems reported            Displays summary information for issues reported by clients
 to the fallback status point for a      in a specified collection. These clients must have an assigned
 specific collection                     fallback status point.

Site - Discovery and inventory information
The following 10 reports are listed under the Site - Discovery and Inventory
Information category.

                                                                                       ﾉ   Expand table

 Report name                          Description

 Clients that have not reported       Displays a list of clients that haven't reported discovery data,
 recently (in a specified             hardware inventory, or software inventory in a specified number
 number of days)                      of days.

 Computers discovered by a            Displays a list of all computers that the specified site discovered.
 specific site                        It also shows the date of the most recent discovery.

 Computers discovered                 Displays a list of computers that the site discovered within the
 recently by discovery method         specified number of days. It also lists the agents that discovered
                                      them. If multiple agents discovered a computer, it may appear
                                      more than once in the list.

 Computers not discovered             Displays a list of computers that the site hasn't recently
 recently (in a specified             discovered. It also shows the number of days since the site
 number of days)                      discovered the computer.

 Computers not inventoried            Displays a list of computers that the site hasn't recently
 recently (in a specified             inventoried. It also shows the last times the client inventoried
 number of days)                      the computer.

 Computers that might share           Displays a list of computers that have changed their names. A
 the same Configuration               change in name is a possible symptom that a computer shares a
 Manager unique identifier            Configuration Manager Unique Identifier with another
                                      computer.

 Computers with duplicate             Displays computers that share MAC address.
 MAC addresses

<!-- p.487 -->

 Report name                         Description

 Count computers in resource         Displays the number of computers in each resource domain or
 domains or workgroups               workgroup.

 Discovery information for a         Displays a list of the agents and sites that discovered a specified
 specific computer                   computer.

 Inventory dates for a specific      Displays the date and time inventory was last run on a specified
 computer                            computer.

Site - General
The following three reports are listed under the Site - General category.

                                                                                       ﾉ   Expand table

 Report name                                  Description

 Computers in a specific site                 Displays a list of client computers in a specified site.

 Site status for the hierarchy                Displays the list of sites in the hierarchy with site
                                              version and site status information.

 Status of Configuration Manager              Displays information about Configuration Manager site
 update within hierarchy                      updates for the hierarchy.

Site - Server information
The following one report is listed under the Site - Server Information category.

                                                                                       ﾉ   Expand table

 Report name                                  Description

 Site system roles and site system            Displays a list of site system server and their site
 servers for a specific site                  system roles for a specified site.

Software - Companies and products
The following 15 reports are listed under the Software - Companies and Products
category.

<!-- p.488 -->

                                                                                 ﾉ    Expand table

Report name                 Description

All inventoried products    Displays a list of the inventoried software products and versions from
for a specific software     a specified software company.
company

All software companies      Displays a list of all companies manufacturing inventoried software.

All Windows apps            Displays a summary of installed Windows apps. It searches using the
                            following criteria: application name, architecture, or publisher.

Computers with a            Displays a list of the computers that a specified product is
specific product            inventoried on, and the versions of that product.

Computers with a            Displays a list of the computers that a specified version of a product
specific product name       is inventoried on.
and version

Computers with specific     Displays a summary of all computers with specified software
software registered in      registered in Add Remove Programs or Programs and Features.
Add Remove Programs

Count all inventoried       Displays a list of the inventoried software products and versions, and
products and versions       the number of computers each is installed on.

Count inventoried           Displays a list of the inventoried versions of a specified product, and
products and versions       the number of computers each is installed on.
for a specific product

Count of all instances of   Displays a summary of all instances of software installed and
software registered with    registered with Add or Remove Programs or Programs and Features
Add or Remove               on computers within the specified collection.
Programs

Count of instances of       Displays a count of instances for specified software packages
specific software           installed and registered in Add or Remove Programs or Programs
registered with Add or      and Features.
Remove Programs

Default Browser counts      Shows the count of clients with a specific web browser as the
                            Windows default.
                            Use the following reference for common BrowserProgIDs:
                            - AppXq0fevzme2pys62n3e0fbqa7peapykr8v: Microsoft Edge
                            - IE.HTTP: Microsoft Internet Explorer
                            - ChromeHTML: Google Chrome
                            - OperaStable: Opera Software
                            - FirefoxURL-308046B0AF4A39CB: Mozilla Firefox
                            - Unknown: the client OS doesn't support the query, the query hasn't
                            run, or a user hasn't logged on

<!-- p.489 -->

 Report name                   Description

 Installations of specified    This report lists all computers with a specified Windows app.
 Windows apps

 Products on a specific        Displays a summary of the inventoried software products and their
 computer                      manufacturers on a specified computer.

 Software registered in        Displays a summary of the software installed on a specified computer
 Add Remove Programs           that is registered in Add Remove Programs or Programs and
 on a specific computer        Features.

 Windows apps installed        Displays all Windows apps installed to the specified user
 to the specified user

Software - Files
The following five reports are listed under the Software - Files category.

                                                                                      ﾉ   Expand table

 Report name                  Description

 All inventoried files for    Display a summary of the files inventoried that are associated with a
 a specific product           specified software product.

 All inventoried files on     Display a summary of all the files inventoried on a specified computer.
 a specific computer

 Compare software             Displays the differences between the software inventories reported for
 inventory on two             two specified computers.
 computers

 Computers with a             Displays a list of computers that have collected software inventory for
 specific file                a specified file name. If a computer contains multiple copies of the file,
                              it might appear more than once in the list.

 Count computers with         Displays the number of computers that have collected software
 a specific file name         inventory for a specified file.

Software distribution - Application monitoring
The following 10 reports are listed under the Software Distribution - Application
Monitoring category.

                                                                                      ﾉ   Expand table

<!-- p.490 -->

 Report name                      Description

 All application deployments      Displays detailed summary information for all application
 (advanced)                       deployments.

 All application deployments      Displays summary information for all application deployments.
 (basic)

 Application compliance           Displays compliance information for the specified application
                                  within the specified collection.

 Application deployments          Displays applications deployed to a specified device or user.
 per asset

 Application infrastructure       Displays application infrastructure errors. These errors include
 errors                           internal infrastructure issues, or errors resulting from invalid
                                  requirement rules.

 Application Usage Detailed       Displays usage details for installed applications.
 Status

 Application Usage Summary        Displays a usage summary for installed applications.
 Status

 Task sequence deployments        Displays task sequence deployments that install a specified
 containing application           application.

Software distribution - Collections
The following three reports are listed under the Software Distribution - Collections
category.

                                                                                       ﾉ   Expand table

 Report name                                 Description

 All collections                             Displays all the collections in the hierarchy.

 All resources in a specific collection      Displays all the resources in a specified collection.

 Maintenance windows available to a          Displays all maintenance windows that are applicable
 specified client                            to the specified client.

Software distribution - Content
The following 16 reports are listed under the Software Distribution - Content category.

<!-- p.491 -->

                                                                                 ﾉ   Expand table

Report name                              Description

All active content distributions         Displays all distributions points on which content is
                                         currently being installed or removed.

All content                              Displays all applications and packages at a site.

All content on a specific distribution   Displays all content currently installed on a specified
point                                    distribution point.

All distribution points                  Displays information about the distribution points for
                                         each site.

All status messages for a specific       Displays all status messages for a specified package on
package on a specific distribution       a specified distribution point.
point

Application content distribution         Displays information about the distribution status for
status                                   application content.

Applications targeted to distribution    Displays information about application content that was
point group                              deployed to a specified distribution point group.

Applications that are out of             Displays the applications for which associated content
synchronization on a specified           files haven't been updated with the latest version on a
distribution point group                 specified distribution point group.

Distribution point group                 Displays information about a specified distribution
                                         point group.

Distribution point usage summary         Displays the distribution point usage summary for each
                                         distribution point.

Distribution status of specified         Displays the distribution status for specified package
package                                  content on each distribution point.

Packages targeted to distribution        Displays information about packages that target a
point group                              specified distribution point group.

Packages that are out of                 Displays packages for which associated content files
synchronization on a specified           haven't been updated with the latest version on a
distribution point group                 specified distribution point group.

Peer cache source content rejection      Displays the number of peer cache source rejections per
                                         boundary group.

Peer cache source content rejection      Displays the peer cache sources that rejected to serve
by condition                             content based on a condition.

<!-- p.492 -->

 Report name                               Description

 Peer cache source content rejection       Displays the name of the content that was rejected by a
 details                                   peer source.

Software distribution - Package and program
deployment
The following five reports are listed under the Software Distribution - Package and
Program Deployment category.

                                                                                 ﾉ   Expand table

 Report name                                Description

 All deployments for a specified package    Displays information about all deployments of a
 and program                                specified package and program.

 All package and program deployments        Displays all of the package and program deployments
                                            at this site.

 All package and program deployments        Displays all of the package and program deployments
 to a specified collection                  to a specified collection.

 All package and program deployments        Displays all of the package and program deployments
 to a specified computer                    that apply to a specified computer.

 All package and program deployments        Displays all of the package and program deployments
 to a specified user                        to a specified user.

Software distribution - Package and program
deployment status
The following five reports are listed under the Software Distribution - Package and
Program Deployment Status category.

                                                                                 ﾉ   Expand table

 Report name                    Description

 All system resource package    Displays all package and program deployments for the site with a
 and program deployments        summary status of each deployment.
 with status

<!-- p.493 -->

 Report name                     Description

 All system resources for a      Displays a list of resources that are in a specified state for a
 specified package and           specified package and program deployment.
 program deployment in a
 specified state

 Chart - Hourly package and      Displays the percentage of computers that successfully installed
 program deployment              the package. The list organizes for every hour since an
 completion status               administrator creates the package and program deployment. It
                                 can be used to track the average time for a package and program
                                 deployment.

 Package and program             Displays the status messages reported for a specified computer
 deployment status for a         and package and program deployment.
 specified client and
 deployment

 Status of a specified package   Displays the status summary for a specified package and
 and program deployment          program deployment.

Software metering
The following 13 reports are listed under the Software Metering category.

                                                                                    ﾉ    Expand table

 Report name                           Description

 All software metering rules applied   Displays a list of all software metering rules at the site.
 to this site

 Computers that have a metered         Displays all computers with the specified metered
 program installed but haven't run     application, but no user has run the program since the
 the program since a specified date    specified date.

 Computers that have run a specific    Displays a list of computers that have run programs
 metered software program              matching the specified software metering rule within the
                                       specified month and year.

 Concurrent usage for all metered      Displays the maximum number of users who concurrently
 software programs                     ran each metered software program during the specified
                                       month and year.

 Concurrent usage trend analysis of    Displays the maximum number of users who concurrently
 a specific metered software           ran the specified metered software program during each
 program                               month for the past year.

<!-- p.494 -->

 Report name                         Description

 Install base for all metered        Displays the number of computers that have metered
 software programs                   software programs installed as reported by software
                                     inventory. This report requires that the computer collects
                                     software inventory.

 Software metering summarization     Displays the time at which the most recently summarized
 progress                            metering data was processed on the site server. The
                                     software metering reports only reflect metering data
                                     processed before these dates.

 Time of day usage summary for a     Displays the average number of usages of a particular
 specific metered software program   program for the past 90 days, broken down by hour and
                                     day.

 Total usage for all metered         Displays the number of users who ran programs within the
 software programs                   specified month and year, and that match each software
                                     metering rule. These rules are for locally installed software,
                                     or using Terminal Services.

 Total usage for all metered         Displays the number of users who ran programs matching
 software programs on Windows        each software metering rule using Terminal Services within
 Terminal Servers                    the specified month and year.

 Total usage trend analysis for a    Displays the number of users who ran programs during
 specific metered software program   each month for the past year, and that match the specified
                                     software metering rule. These rules are for locally installed
                                     software, or using Terminal Services.

 Total usage trend analysis for a    Displays the number of users who ran programs during
 specific metered software program   each month for the past year, and that match the specified
 on Windows Terminal Servers         software metering rule. These rules are for using Terminal
                                     Services.

 Users that have run a specific      Displays a list of users who have run programs within the
 metered software program            specified month and year, and that match the specified
                                     software metering rule.

Software updates - A Compliance
The following eight reports are listed under the Software Updates - A Compliance
category.

                                                                                 ﾉ   Expand table

<!-- p.495 -->

 Report name                         Description

 Compliance 1 - Overall              Displays the overall compliance data for a software update
 compliance                          group.

 Compliance 2 - Specific software    Displays the compliance data for a specified software update.
 update

 Compliance 3 - Update group         Displays the compliance data for software updates defined in
 (per update)                        a software update group.

 Compliance 4 - Updates by           Displays the compliance data for software updates released
 vendor month year                   by a vendor during a specified month and year.

 Compliance 5 - Specific             This report returns the software update compliance data for
 computer                            a specified computer. To limit the amount of information
                                     returned, you can specify the vendor and software update
                                     classification.

 Compliance 6 - Specific software    Displays the count and percentage of computers in each
 update states (secondary)           compliance state for the specified software update.

 Compliance 7 - Computers in a       Displays all computers in a collection that have a specified
 specific compliance state for an    overall compliance state against a software update group.
 update group (secondary)

 Compliance 8 - Computers in a       Displays all computers in a collection that have a specified
 specific compliance state for an    compliance state for a software update.
 update (secondary)

 Compliance 9 - Overall health       Displays the overall health and compliance data for a
 and compliance                      software update group. (starting in version 1806)

Software updates - B Deployment management
The following eight reports are listed under the Software Updates - B Deployment
Management category.

                                                                                  ﾉ   Expand table

 Report name                 Description

 Management 1 -              Displays all deployments that include all of the software updates
 Deployments of an           defined in a specified software update group.
 update group

 Management 2 - Updates      Displays all vendor-specific software updates that clients detect as
 required but not            required, but an administrator hasn't deployed to a specified

<!-- p.496 -->

 Report name                  Description

 deployed                     collection.

 Management 3 - Updates       Displays the software updates that are contained in a specified
 in a deployment              deployment.

 Management 4 -               Displays all software update deployments that target a specified
 Deployments that target      collection.
 a collection

 Management 5 -               Displays all software update deployments that are deployed to a
 Deployments that target      specified computer.
 a computer

 Management 6 -               Displays all deployments that include a specified software update
 Deployments that             and the associated target collection for the deployment.
 contain a specific update

 Management 7 - Updates       Displays the software updates in a specified deployment that don't
 in a deployment missing      have all of the associated content retrieved. This state prevents
 content                      clients from installing the update, which prevents the deployment
                              from achieving 100% compliance.

 Management 8 -               Displays all computers requiring the specified software update, but
 Computers missing            the associated content isn't yet distributed to a distribution point.
 content (secondary)

Software updates - C Deployment states
The following six reports are listed under the Software Updates - C Deployment States
category.

                                                                                      ﾉ   Expand table

 Report name                                Description

 States 1 - Enforcement states for a        Displays the enforcement states for a specified software
 deployment                                 update deployment, which is typically the second phase of
                                            a deployment assessment.

 States 2 - Evaluation states for a         Displays the evaluation state for a specified software
 deployment                                 update deployment, which is typically the first phase of a
                                            deployment assessment.

 States 3 - States for a deployment         Displays the states for all software updates in the specified
 and computer                               deployment for a specified computer.

<!-- p.497 -->

 Report name                               Description

 States 4 - Computers in a specific        Displays all computers in a specified state for a software
 state for a deployment (secondary)        update deployment.

 States 5 - States for an update in a      Displays a summary of states for a specified software
 deployment (secondary)                    update targeted by a specified deployment.

 States 6 - Computers in a specific        Displays all computers in a specified enforcement state for
 enforcement state for an update           a specified software update.
 (secondary)

Software updates - D Scan
The following four reports are listed under the Software Updates - D Scan category.

                                                                                     ﾉ   Expand table

 Report name                            Description

 Scan 1 - Last scan states by           Specify a collection to display the count of computers in each
 collection                             compliance scan state. The clients return the state during the
                                        last compliance scan.

 Scan 2 - Last scan states by site      Specify a site to display the count of computers in each
                                        compliance scan state. The clients return the state during the
                                        last compliance scan.

 Scan 3 - Clients of a collection       Displays all computers for a specified collection and a
 reporting a specific state             specified compliance scan state during their last compliance
 (secondary)                            scan.

 Scan 4 - Clients of a site             Specify a site to display all computers with a specified
 reporting a specific state             compliance scan state. The clients return the state during
 (secondary)                            their last compliance scan.

Software updates - E Troubleshooting
The following four reports are listed under the Software Updates - E Troubleshooting
category.

                                                                                     ﾉ   Expand table

<!-- p.498 -->

 Report name                                      Description

 Troubleshooting 1 - Scan errors                  Displays scan errors at the site and a count of
                                                  computers that are experiencing each error.

 Troubleshooting 2 - Deployment errors            Displays the deployment errors at the site and a
                                                  count of computers that are experiencing each
                                                  error.

 Troubleshooting 3 - Computers failing with       Displays a list of the computers that failed a scan
 a specific scan error (secondary)                because of a specified error.

 Troubleshooting 4 - Computers failing with       Displays a list of the computers on which the
 a specific deployment error (secondary)          deployment of update is failing because of a
                                                  specified error.

State migration
The following three reports are listed under the State Migration category.

                                                                                    ﾉ   Expand table

 Report name                                      Description

 State migration information for a specific       Displays state migration information for a
 source computer                                  specified computer.

 State migration information for a specific       Displays state migration information for a
 state migration point                            specified state migration point.

 State migration points for a specific site       Displays the state migration points for a specified
                                                  site.

Status messages
The following 12 reports are listed under the Status Messages category.

                                                                                    ﾉ   Expand table

 Report name                               Description

 All messages for a specific message       Displays a list of status messages that have a specified
 ID                                        message ID.

 Clients reporting errors in the last 12   Displays a list of computers and components reporting
 hours for a specific site                 errors in the last 12 hours, and the number of errors

<!-- p.499 -->

 Report name                            Description

                                        reported.

 Component messages for the last 12     Displays a list of component messages for the last 12
 hours                                  hours for a specified site code, computer, and
                                        component.

 Component messages for the last        Displays a list of the status messages created in the last
 hour                                   hour by a specified component on a specified computer
                                        at a specified site.

 Count component messages for the       Displays the number of status messages by component
 last hour for a specific site          and severity reported in the last hour at a specified site.

 Count errors in the last 12 hours      Displays the number of server component error status
                                        messages in the last 12 hours.

 Fatal errors (by component)            Displays a list of computers reporting fatal errors by
                                        component.

 Fatal errors (by computer name)        Displays a list of computers reporting fatal errors by
                                        computer name.

 Last 1000 messages for a specific      Displays a summary of the last 1000 error and warning
 computer (Errors and Warnings)         component status messages for a specified computer.

 Last 1000 messages for a specific      Displays a summary of the last 1000 error, warning, and
 computer (Errors Warnings and          informational component status messages for a specified
 Information)                           computer.

 Last 1000 messages for a specific      Displays a summary of the last 1000 error server
 computer (Errors)                      component status messages for a specified computer.

 Last 1000 messages for a specific      Displays a summary of the most recent 1000 status
 server component                       messages for a specified server component.

Status messages - Audit
The following three reports are listed under the Status Messages - Audit category.

                                                                                  ﾉ   Expand table

 Report name                   Description

 All audit messages for a      Displays a summary of all audit status messages for a specified
 specific user                 user. Audit messages describe actions taken in the Configuration
                               Manager console that add, modify, or delete objects in
                               Configuration Manager.

<!-- p.500 -->

 Report name                     Description

 Remote Control - All            Displays a summary of status messages indicating remote control
 computers remote                of client computers by a specified user.
 controlled by a specific
 user

 Remote Control - All            Displays a summary of status messages related to the remote
 remote control information      control of client computers.

Task sequence - Deployment status
The following 11 reports are listed under the Task Sequence - Deployment Status
category.

                                                                                      ﾉ   Expand table

 Report name                                   Description

 All system resources for a task               Displays a list of the destination computers for the
 sequence deployment in a specific             specified task sequence deployment in a specified
 state                                         deployment state.

 All system resources for a task               Displays a list of the destination computers for the
 sequence deployment that is in a              specified task sequence deployment that is in the
 specific state and that is available to       specified deployment state.
 unknown computers

 Count of system resources that have           Displays the number of computers that have accepted
 task sequence deployments assigned            task sequences, but haven't run the task sequence.
 but not yet run

 History of a task sequence deployment         Displays the status of each step of the specified task
 on a computer                                 sequence deployment on the specified destination
                                               computer. If no record is returned, the task sequence
                                               hasn't started on the computer.

 List of computers that exceeded a             Displays the list of destination computers that
 specific length of time to run a task         exceeded the specified length of time to run a task
 sequence deployment                           sequence.

 Run time for a specific task sequence         Displays the total time that it took to successfully
 deployment on a specific destination          complete a specified task sequence on a specified
 computer                                      computer.

 Run time for each step of a task              Displays the time that it took to complete each step of
 sequence deployment on a specific             the specified task sequence deployment on the
 destination computer                          specified destination computer.

<!-- p.501 -->

 Report name                                  Description

 Status of a specific task sequence           Displays the status summary of a specified task
 deployment for a specific computer           sequence deployment on a specified computer.

 Status of a task sequence deployment         Displays the status of the specified task sequence
 on an unknown destination computer           deployment on the specified unknown destination
                                              computer.

 Status summary of a specific task            Displays a status summary of all resources that have
 sequence deployment                          been targeted by a deployment.

 Status summary of a specific task            Displays the status summary of all resources targeted
 sequence deployment available to             by the specified deployment that is available to a
 unknown computers                            collection containing unknown computers.

Task sequence - Deployments
The following 11 reports are listed under the Task Sequence - Deployments category.

                                                                                    ﾉ   Expand table

 Report name                                   Description

 All system resources currently in a           Displays a list of computers that are currently running
 specific group or phase of a specific task    in a specified group or phase of a specified task
 sequence deployment                           sequence deployment.

 All system resources where a task             Displays a list of computers that failed within a
 sequence deployment failed within a           specified group/phase of the specified task sequence
 specific group or phase                       deployment.

 All task sequence deployments                 Displays details of all task sequence deployments
                                               initiated from the current site.

 All task sequence deployments available       Displays details of all the task sequence deployments
 to unknown computers                          initiated from the site, and deployed to collections
                                               that contain unknown computers.

 Count of failures in each phase or group      Displays the number of failures in each phase or
 of a specific task sequence                   group of the specified task sequence.

 Count of failures in each phase or group      Displays the number of failures in each phase or
 of a specific task sequence deployment        group of the specified task sequence deployment.

 Deployment status of all task sequence        Displays the overall progress of all task sequence
 deployments                                   deployments.

 Progress of a running task sequence           Displays the progress of the specified task sequence.

<!-- p.502 -->

 Report name                                 Description

 Progress of a running task sequence         Displays the summary information for the specified
 deployment                                  task sequence deployment.

 Progress of all deployments for a           Displays the progress of all deployments for the
 specific task sequence                      specified task sequence.

 Summary report for a task sequence          Displays the summary information for the specified
 deployment                                  task sequence deployment.

Task sequence - Progress
The following five reports are listed under the Task Sequence - Progress category.

                                                                                  ﾉ   Expand table

 Report name                         Description

 Chart - Weekly progress of a        Displays the weekly progress of a task sequence, starting from
 task sequence                       the deployment date.

 Progress of a task sequence         Displays the progress of the specified task sequence.

 Progress of all task sequences      Displays a summary of the progress of all task sequences.

 Progress of task sequences for      Displays the progress of all task sequences that deploy
 operating system deployments        operating systems.

 Status of all unknown               Displays a list of computers that were unknown at the time
 computers                           they ran a task sequence deployment, and whether they're
                                     now known computers.

Task sequences - References
The following one report is listed under the Task Sequences - References category.

                                                                                  ﾉ   Expand table

 Report name                                 Description

 Content referenced by a specific task       Displays content that is referenced by a specified task
 sequence                                    sequence.

User - Device affinity

<!-- p.503 -->

The following two reports are listed under the User - Device Affinity category.

                                                                                     ﾉ   Expand table

 Report name                       Description

 Pending user device affinity      This report shows all pending user device affinity assignments
 associations by collection        based on usage data, for members of a collection.

 User device affinity              Displays all user device associations for the specified collection,
 associations per collection       and groups the results by collection type (for example, user or
                                   device).

User data and profiles health
The following four reports are listed under the User Data and Profiles Health category.

                                                                                     ﾉ   Expand table

 Report name                     Description

 Folder Redirection Health       Displays the health state details of folder redirection for each of
 Report - Details                the redirected folders for a given user.

 Roaming User Profiles           Displays the health state details of the roaming user profile for a
 Health Report - Details         specified user.

 User Data and Profiles          Displays the error or warning details of folder redirection or
 Health Report - Details         roaming user profiles. This report is the details target from the
                                 summary report.

 User Data and Profiles          Displays the summary of health states for folder redirection and
 Health Report - Summary         roaming user profiles.

Users
The following three reports are listed under the Users category.

                                                                                     ﾉ   Expand table

 Report name                           Description

 Computers for a specific user         Displays a list of the computers that were used by a specified
 name                                  user.

 Count users by domain                 Displays the number of users in each domain.

<!-- p.504 -->

 Report name                        Description

 Users in a specific domain         Displays a list of users and their computers in a specified
                                    domain.

Virtual applications
The following seven reports are listed under the Virtual Applications category.

                                                                                 ﾉ   Expand table

 Report name                   Description

 App-V Virtual Environment     Displays information about a specified virtual environment that is
 Results                       in a specified state for a specified collection.

 App-V Virtual Environment     Displays information about a specified virtual environment for a
 Results For Asset             specified asset. It also shows any deployment types for the
                               specified virtual environment.

 App-V Virtual Environment     Displays compliance information for a specified virtual
 Status                        environment for a specified collection.

 Computers with a specific     Displays a summary of computers that have the specified App-V
 virtual application           application shortcut as created using the Application Virtualization
                               Management Sequencer.

 Computers with a specific     Displays a summary of computers that have the specified App-V
 virtual application package   application package.

 Count of all instances of     Display a count of detected App-V application packages.
 virtual application
 packages

 Count of all instances of     Display a count of detected App-V applications.
 virtual applications

Vulnerability assessment
The following one report is listed under the Vulnerability Assessment category.

                                                                                 ﾉ   Expand table

<!-- p.505 -->

 Report name                       Description

 Vulnerability Assessment          Identifies security, administrative, and compliance
 Overall Report                    vulnerabilities for a specific computer

Wake On LAN
The following seven reports are listed under the Wake On LAN category.

                                                                                     ﾉ    Expand table

 Report name                              Description

 All computers targeted for Wake On       Specify the type of deployment to display a list of
 LAN activity                             computers targeted for Wake on LAN activity.

 All objects pending wake-up activity     Displays objects that are scheduled for wakeup.

 All sites that are enabled for Wake      Displays a list of all sites in the hierarchy that are
 On LAN                                   enabled for Wake On LAN.

 Errors received while sending wake-      Displays errors received while sending wake-up packets
 up packets for a defined period          to computers for a defined period.

 History of Wake On LAN activity          Displays a history of the wakeup activity that has
                                          occurred since a certain period.

 Wake-Up Proxy Deployment State           Displays information about the deployment status of
 Details                                  Wake-Up Proxy for each device in a specified collection.

 Wake-Up Proxy Deployment State           Displays a summary of the deployment status of wake-
 Summary                                  up proxy for a specified collection.

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.506 -->

SMS Provider Fundamentals in
Configuration Manager
Article • 10/04/2022

You use the SMS Provider to access and modify Configuration Manager data. The SMS
Provider is a Windows Management Instrumentation (WMI) provider that can be
accessed through either WMI or managed classes.

WMI Architecture
WMI is designed to function as a middle layer, by serving as a standard interface
between management applications and the systems that they manage.

WMI Object Model
Management applications and scripts work with WMI through the WMI Object Model.
The object model defines the programming interface to WMI.

For more information about WMI, see Windows Management Instrumentation.

The main elements of the WMI Object Model are shown in the following table:

                                                                                      ﾉ   Expand table

 Element      Description

 Locator      Used to locate a WMI Service that is running on a local or remote computer.

 Service      Represents an actual connection to a WMI provider. This is the main point of contact
 object       to WMI programs.

 Objects      A managed object is a logical or physical enterprise component, such as a hard
              drive, network adapter, database system, operating system, process, or service. A
              managed object communicates with WMI through a WMI provider.

 Events       Used to track changes to WMI objects at run time. Events can be captured as objects
              and then manipulated in the same ways that any other objects, except that they
              cannot be changed or saved in WMI.

 Properties   Supplies descriptive or operational information about an object. For example, a
              Win32_DiskDrive object includes a property called InterfaceType , which might have
              the value of IDE for your C: drive. Properties can also be set to particular values, if
              the property is changeable. Setting InterfaceType to SCSI is not appropriate,

<!-- p.507 -->

 Element      Description

              because the only way to change the actual interface type is to replace the controller
              card. However, you can set a share name to a different value.

 Methods      Actions that you can execute on objects. For example, a Win32_Directory object
              includes a method called Compress() that allows the contents of a folder to be
              compressed in the same way as compressing the contents by using the Windows
              graphical user interface.

 Qualifiers   Characteristics of objects, properties, and methods. For example, a qualifier for a
              property might indicate that it is read-only, or it might list the allowable values for
              the property. A qualifier for an object might be that it is read-only.

Schema
WMI objects are described by classes, providing definitions of their properties,
attributes, and other information. These classes are organized into an inheritance
hierarchy supporting object associations and grouped by areas of interest, such as
networking, applications, and systems. Each area of interest represents a schema, which
is a subset of the information that is available about the managed environment.

For more information, see the Schema overview.

For information about accessing the SMS Provider using WMI, see WMI Configuration
Manager Provider Fundamentals

WMI and .NET Framework applications
Configuration Manager has a .NET Framework library,
Microsoft.ConfigurationManager.ManagementProvider, that wraps WMI and allows you
to write managed applications.

For information about accessing the SMS Provider by using .NET Framework, see .NET
Managed Configuration Manager Provider Fundamentals

You can also use the .NET Framework WMI management namespace
System.Management, but this does not provide any Configuration Manager-specific
interfaces. It is, however, the recommended way to use managed code on a
Configuration Manager client.

See also

<!-- p.508 -->

SMS Provider fundamentals

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.509 -->

WMI Configuration Manager Provider
Fundamentals
Article • 10/04/2022

Windows Script Host-based applications and scripts work in Windows Management
Instrumentation (WMI) through the WMI Object Model, which defines the programming
interface to WMI. A number of WMI object types are used when manipulating
Configuration Manager objects. For more information about the WMI Object Model, see
Windows Management Instrumentation.

In simple Configuration Manager scripts, you use the following WMI object types:

      SWbemLocator

      SWbemServices

      SWbemObjectSet

      SWbemObject

  ７ Note

  Understanding WMI Query Language (WQL) queries is very important for
  identifying which Configuration Manager objects you want to read. WQL
  statements allow you to retrieve Configuration Manager objects that are based on
  SQL-like queries. For example, the following WQL statement is used to identify all
  Windows Server 2003 systems:

   SELECT * FROM SMS_FullCollectionMembership WHERE CollectionID='SMS000FS'

For more information about using VBScript and WMI, see Objects overview.

SWbemLocator
The SWbemServicesobject is used to create an authenticated connection to the SMS
Provider. You use the ConnectServer method to make the connection to the SMS
Provider. This method is particularly useful if you need to pass user credentials to a
remote Configuration Manager server during connection. You can also use the Windows
Script Host GetObject method to create an authenticated connection. The type of object
that is returned by GetObject depends on the parameters that are passed to it. See How

<!-- p.510 -->

to Connect to a Configuration Manager Provider Using Managed Code and How to
Connect to a Configuration Manager Provider Using WMI for examples that show how
to use either SWbemLocator or GetObject in your connection script.

SWbemServices
The SWbemServices object represents an authenticated connection to a SMS Provider,
and it is the object that you use to retrieve Configuration Manager objects. You receive
an SWbemServices object as the return value of the SWbemLocator function ConnectServer
or, alternatively, as the return value when the GetObject method is used to connect to
the SMS Provider. SWbemServices has several methods, but you use only the Get,
ExecQuery, and InstancesOf methods for retrieving objects.

Get returns a single instance of a Configuration Manager object ( SWbemObject ).
ExecQuery and InstancesOf return Configuration Manager objects in a collection

( SWbemObjectSet ) of Configuration Manager objects.

SWbemObjectSet
The SWbemObjectSet object represents a collection of Configuration Manager objects.
You can use it to enumerate through the collection and read individual instances of the
Configuration Manager object ( SWbemObject ) that you are interested in. You typically get
a SWbemObjectSet object returned to you from the SWbemServices retrieval functions.

SWbemObject
The SWbemObject object allows you to access the properties and other information for
a Configuration Manager object.

See also
SMS Provider fundamentals Objects overview

Feedback
Was this page helpful?    Yes     No

<!-- p.511 -->

Provide product feedback

<!-- p.512 -->

Managed SMS Provider Fundamentals
in Configuration Manager
Article • 10/04/2022

The managed SMS Provider library is a .NET Framework library that wraps the
System.Management classes and provides a Configuration Manager-centric object
model. It also provides a wrapper for accessing the Configuration Manager site control
file.

The library can be used outside of any code relating to the Configuration Manager
console .NET Framework library, but is built on the same underlying architecture.

For information about using managed code with the Configuration Manager client, see
About Configuration Manager WMI Programming.

Configuration Manager Classes and Interfaces
The primary classes and interfaces for use with the managed SMS Provider are the
following:

WqlConnectionManager
The class WqlConnectionManager provides access to the Configuration Manager Windows
Management Instrumentation (WMI) provider.

It is an implementation of the abstract base class ConnectionManagerBase that defines
connections throughout the managed Configuration Manager libraries.

It is used to connect to the SMS Provider and query, or create, Configuration Manager
object instances. The following tasks demonstrate the basic usage of
WqlConnectionManager.

How to Connect to a Configuration Manager Provider using Managed Code.

How to Read a Configuration Manager Object Using Managed Code.

How to Perform an Asynchronous Configuration Manager Query Using Managed Code

IResultObject

<!-- p.513 -->

IResultObject is an interface that all result sets and objects expose. Through it, you can
read, modify, delete, call methods on, and otherwise manipulate Configuration Manager
objects. You typically get an IResultObject whenever you create an object or as a result
of a query.

The following tasks demonstrate the basic use of IResultObject :

How to Modify a Configuration Manager Object Using Managed Code

How to Delete a Configuration Manager Object Using Managed Code

How to Call a Configuration Manager Object Method Using Managed Code

QueryProcessor
QueryProcesor provides support for both synchronous and asynchronous queries
against the SMS Provider. In asynchronous queries, SmsBackgroundWorker is used to
provide thread support query results. The following tasks demonstrate queries:

How to Perform an Asynchronous Configuration Manager Query Using Managed Code.

How to Perform a Synchronous Configuration Manager Query Using Managed Code.

IQueryPropertyItem
IQueryPropertyItem is a single property of the result object, supports data binding and
get/set properties.

The following tasks demonstrate the use of IQueryPropertyItem :

How to Modify a Configuration Manager Object Using Managed Code.

Assemblies
The assemblies that are required for using managed SMS Provider are:

microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

The WMI implementation of the managed Configuration Manager libraries is provided
by adminui.wqlqueryengine.

<!-- p.514 -->

See also
SMS Provider fundamentals Configuration Manager objects

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.515 -->

Configuration Manager Context
Qualifiers
Article • 10/10/2022

Context objects are used, in Configuration Manager, to provide additional information
to the SMS Provider. Typically, you use context qualifiers to give the SMS Provider
contextual information, such as your application's name. You can use context qualifiers
when you connect to the SMS Provider and with individual SMS Provider objects.

Managed Code
When using the managed SMS Provider libraries, you use the
ConnectionManagerBase.Context property to specify context qualifiers. For more
information, see How to Add a Configuration Manager Context Qualifier by Using
Managed Code.

VBScript
When using VBScript, you use the SWBemNamedValue interface set to specify context
qualifiers as a collection of named value objects. For more information, see How to Add
a Configuration Manager Context Qualifier by Using WMI.

Context Qualifiers
The following table contains the context qualifiers (named values) that are used by the
SMS Provider. Most qualifiers, like SessionHandle , are only used with specific functional
areas of the SMS Provider; but LocaleID , MachineName , and ApplicationName are for your
application's use.

                                                                             ﾉ   Expand table

 Context qualifier     Description

 ApplicationName       Identifies the application that made the call.

 ContextHandle         Identifies where the SMS Provider has stored your cached context
                       qualifiers.

 InstanceCount         Limits the number of instances returned from ExecQuery and
                       CreateInstanceEnum.

<!-- p.516 -->

 Context qualifier      Description

 LimitToCollectionIDs   Limits the results of a resource query to the members of the named
                        collections.

 LocaleID               Identifies the code page to use.

 MachineName            Identifies which computer is running the application.

 QueryQualifiers        Returns the SecurityVerbs bit flags when you execute queries against
                        secured objects.

 SessionHandle          Identifies your application's copy of the site control file to Configuration
                        Manager.

ApplicationName
The ApplicationName context qualifier is a string value that identifies the name of the
application that made the call. You should specify ApplicationName for your application
because it is used for auditing. If you do not supply the name of your application, a
value of Unknown is used. You must supply the ApplicationName value when you call
any of the raise status message methods, such as
SMS_StatusMessage::RaiseErrorStatusMsg, or the call will fail.

ContextHandle
The ContextHandle context qualifier is a string value that identifies where the SMS
Provider has stored your cached context qualifiers. The managed SMS Provider manages
data transfer. When using VBScript, You can use the following steps to reduce the
amount of data that is passed over the network.

   1. Create SWBemNamedValue value set.

   2. Add your qualifiers to the context object. For more information, see How to Add a
     Configuration Manager Context Qualifier by Using WMI.

   3. Call the GetContextHandle method to cache your qualifiers on the server. The SMS
     Provider caches the context object that you pass as a parameter of ExecMethod
     when you call GetContextHandle.

   4. Remove all the qualifiers from your context object.

   5. Add the ContextHandle qualifier and value to your context object.

<!-- p.517 -->

   6. Pass the context object on all calls to IWbemServices.

     You must call the ClearContextHandle method to remove your cached qualifiers
     before you exit your application. You can create as many ContextHandle values as
     you want, with each providing varying information for your application.

  ７ Note

  After you cache your context qualifiers, you can override your cached values by
  adding the same context qualifiers, with different values, to your context object.

InstanceCount
The InstanceCount context qualifier is an integer value that is used to limit the number
of instances returned from the ExecQuery and CreateInstanceEnum methods. You set
InstanceCount equal to the maximum number of instances that you want returned from
the query or enumerator. For example, setting InstanceCount to 10 returns, at most, 10
instances.

LimitToCollectionIDs
The LimitToCollectionIDs context qualifier is a string array that contains a list of
CollectionID values. Currently, you can specify only one CollectionID value. You use

this qualifier to limit the results of a resource query to the members of the named
collection. A resource query is a query that includes classes derived from SMS_Resource
or SMS_Group.

The user must have instance read resource permissions for the collection to which the
resource belongs. You must use collection limiting when the user does not have class
read resource rights for collections; otherwise, no data is returned. For SMS 2.0 with
Service Pack 1 and later versions, this restriction applies only to classes derived from
SMS_Group.

You cannot use this qualifier when querying collections.

LocaleID
The LocaleID context qualifier is a string value that accepts either a hexadecimal value
or a decimal value in the form MS\x, where x is the locale ID. For example, you can enter

<!-- p.518 -->

the English LocaleID value as ms\0x0409 or ms\1033. The SMS Provider only accepts
LocaleID values that use the Microsoft format. You can find a list of locale IDs at

Locale IDs Assigned by Microsoft.

If you need the locale for non-U.S. installations, you can get it from the
SMS_Identification Server WMI Class LocaleID property.

MachineName
The MachineName context qualifier is a string value that identifies which computer is
running the application. You should specify MachineName for your application because it
is used for auditing. If you do not supply the computer name, a value of Unknown is
used. You must supply the MachineName value when you call any of the raise status
message methods, such as SMS_StatusMessage::RaiseRawStatusMsg, or the call will fail.

QueryQualifiers
The QueryQualifiers context qualifier is a Boolean value that is used to return the
SecurityVerbs bit flags when you execute queries against secured objects, such as
SMS_Site or SMS_Package. Note that using QueryQualifiers when querying unsecured
objects generates an error. By default, SecurityVerbs flags are not returned with the
query. You must create this qualifier and set its value to true if you want the flags
returned. Not creating QueryQualifiers is the same as setting its value to false .

SessionHandle
The SessionHandle context qualifier is a string value that is returned as an out parameter
of the GetSessionHandle method. The string is a unique GUID that identifies your
application's copy of the site control file to Configuration Manager. You should use this
mechanism to modify the site control file and reduce data collisions with other
applications that are modifying the site control file at the same time. If you do not
supply a SessionHandle value, your application modifies the global copy of the site
control file, which has no protection from applications overwriting each other's data.

  ７ Note

  If you are using the managed SMS Provider, site control file session management is
  managed for you.

<!-- p.519 -->

See Also
How to Add a Configuration Manager Context Qualifier Using Managed Code
How to Add a Configuration Manager Context Qualifier Using WMI
SMS Provider fundamentals

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.520 -->

SMS Provider Field Length Restrictions
in Configuration Manager
Article • 10/04/2022

The SMS Provider, in Configuration Manager, places restrictions on the width of
character fields for schema classes. If you write a program that writes to these classes,
you should take these field widths into account. Where they are used in the user
interface, the Configuration Manager online Help provides the maximum character
widths. You can also determine the width by dividing the corresponding schema class
table column width by two to give the field width in characters.

You can determine the schema class table column width from the corresponding SQL
Server views. For information about mapping schema classes to SQL Server views, see
Configuration Manager Schema View Mapping. The steps for obtaining the table
column width from the SQL Server view in Microsoft SQL Server are:

   1. Open the properties of the SQL Server view to see which table and table columns it
      uses.

   2. Open the corresponding table in the database tables view to discover the column
      width.

      Classes that are commonly affected by this restriction are:

      SMS_Package

      SMS_Advertisement

      SMS_Program

      SMS_DistributionPoint

      SMS_PDF_Package

      SMS_PDF_Program

      SMS_Query

      SMS_Report

      SMS_ReportDashboard

      SMS_ReportViewSchema
