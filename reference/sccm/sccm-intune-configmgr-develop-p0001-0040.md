---
title: "Configuration Manager SDK documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. Configuration Manager SDK documentation The Configuration Manager SDK contains documentation and samples that are useful in developing applications that access and modify Configuration Manager data. About Configuration Manager SDK ｅ OVERVIEW SD"
---

# Configuration Manager SDK documentation — pages 1-40

<!-- p.1 -->

                                                           Tell us about your PDF experience.

Configuration Manager SDK
documentation
The Configuration Manager SDK contains documentation and samples that are useful in
developing applications that access and modify Configuration Manager data.

  About Configuration Manager SDK

  ｅ OVERVIEW
  SDK overview

  What's new

  SDK requirements

  ｉ REFERENCE
  Configuration Manager API reference

  Administration service REST API

  Get started

  Ｙ ARCHITECTURE
  Get started with Configuration Manager programming

  Architectural overview

  Get started with PowerShell

  ｉ REFERENCE
  Configuration Manager PowerShell cmdlets

  Top tasks

  ｃ HOW-TO GUIDE
  Introduction to WBEMTEST

<!-- p.2 -->

ｉ REFERENCE
Configuration Manager schema SQL views

SMS_R_System server WMI class

<!-- p.3 -->

Configuration Manager SDK
Article • 10/10/2022

Welcome to the Configuration Manager software development kit (SDK).

This SDK provides information applicable to:

      Administrators who want to automate Configuration Manager through scripts
      Developers adding features and extensions to Configuration Manager functionality

The Configuration Manager SDK contains documentation and samples that are useful in
developing applications that access and modify Configuration Manager data. It also
provides reference material for Configuration Manager features.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.4 -->

Privacy Information
Article • 10/04/2022

The Configuration Manager SDK provides documentation and code samples
demonstrating how to programmatically access Configuration Manager features. When
you build a program or script by using the Configuration Manager SDK, Configuration
Manager does not limit the types of information it transmits. For example, a program
that identifies each computer and logon account could be used to transmit information
between clients and servers.

No information is sent back to Microsoft by the Configuration Manager SDK unless you
choose to send it to Microsoft.

Before writing any scripts or programs that are based on the information in the
Configuration Manager SDK, consider your privacy requirements.

See Also
Configuration Manager Software Development Kit

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.5 -->

What's new in the Configuration
Manager SDK
Article • 10/10/2022

This article lists any recent additions or changes to the Configuration Manager software
development kit (SDK).

External dependencies require .NET 4.6.2
Starting in version 2111, all Configuration Manager libraries are built using Microsoft
.NET Framework version 4.6.2 or later. If you develop an application or tool that depends
upon these libraries, it also needs to support .NET 4.6.2 or later. Microsoft recommends
using .NET Framework version 4.8.

Applications or tools that use Configuration Manager WMI classes and methods, REST
APIs, or PowerShell cmdlets aren't affected.

If you develop a third-party add-on to Configuration Manager, you should test your
add-on with every monthly technical preview branch release. Regular testing helps
confirm compatibility, and allows for early reporting of any issues with standard
interfaces.

Configuration Manager SDK redistributable
files available on NuGet

Client messaging
Client messaging SDK package

Management point API (MPAPI)
The MPAPI contains the management point interface libraries.

      Microsoft.ConfigurationManagement.MPAPI.i386

      Microsoft.ConfigurationManagement.MPAPI.amd64

For more information, see the MPAPI documentation.

<!-- p.6 -->

Install status MIF COM library (ISMIFCOM)
ISMIFCOM is a COM library with a class wrapper for the install status MIF functions.

     Microsoft.ConfigurationManagement.ISMIFCOM.i386

     Microsoft.ConfigurationManagement.ISMIFCOM.amd64

For more information, see the ISMIFCOM documentation.

Data discovery record creation libraries
SMSRsGen and SMSRsGenCtl are legacy COM libraries used to create data discovery
records (DDRs).

  ） Important

  These are legacy libraries. The current recommendation is to use the Client
  Messaging SDK DiscoveryDataRecordFile class. Use the latest Client Messaging
  SDK package       from NuGet.

     Microsoft.ConfigurationManagement.SMSRsGen.i386

     Microsoft.ConfigurationManagement.SMSRsGen.amd64

     Microsoft.ConfigurationManagement.SMSRsGenCtl.i386

     Microsoft.ConfigurationManagement.SMSRsGenCtl.amd64

For more information, see the SMSResGen documentation

See also
     Configuration Manager SDK

     Get started with Configuration Manager cmdlets for Windows PowerShell

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.7 -->

About Configuration Manager SDK
Requirements
Article • 10/10/2022

Developing applications and scripts for Microsoft Configuration Manager can be done
using a number of development languages and tools. Which one you use depends on
the type of application you are writing. Large applications will likely be written in C#
using the managed Configuration Manager SDK libraries. VBScript is a good choice for
scripting Configuration Manager.

This documentation provides examples in C#, VBScript and, where appropriate, C++.

  ７ Note

  If you are programming with another .NET Framework language, use the C#
  examples for reference.

Development tools
Visual Studio provides a suitable environment for developing Configuration Manager
applications and scripts. For more information, see Visual Studio documentation.

Development Requirements
For information about development requirements, see Configuration Manager Client
Development Requirements and Configuration Manager Server Development
Requirements.

Runtime Requirements
For information about runtime requirements, see Configuration Manager Client Runtime
Requirements and Configuration Manager Server Runtime Requirements.

  ） Important

  For more information about general Configuration Manager requirements, see
  Supported configurations.

<!-- p.8 -->

See Also
Configuration Manager Reference About SDK requirements

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.9 -->

Configuration Manager Client Runtime
Requirements
Article • 10/10/2022

Applications that run on Microsoft Configuration Manager clients have the following
runtime requirements.

Managed Code
      Configuration Manager client

      Microsoft .NET Framework version 4

VBScript
      Configuration Manager client

      Windows Script Host

Windows 64-Bit Support
A 32-bit compiled application that uses Configuration Manager SDK interfaces to access
Configuration Manager client or Configuration Manager server functionality works when
it runs in 32-bit emulation on a 64-bit Windows operating system. However, a 64-bit
compiled application that uses Configuration Manager SDK interfaces that access 32-bit
Configuration Manager client or Configuration Manager server functionality does not
work. Similarly, Configuration Manager SDK scripts do not work when the scripting host
is a native 64-bit application. A Configuration Manager SDK script does work if it is
called from within a 32-bit scripting host.

The Configuration Manager client has a native 64-bit version that is installed
automatically on Windows 64-bit operating systems. Applications that relied on the 32-
bit interfaces to be present may need to be re-compiled in a native 64-bit environment
to interact with the Configuration Manager client APIs.

General Requirements
For more information about Configuration Manager client requirements, see Supported
configurations.

<!-- p.10 -->

See Also
Configuration Manager Client Development Requirements
Configuration Manager Server Runtime Requirements
Configuration Manager Server Development Requirements

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.11 -->

Configuration Manager Server Runtime
Requirements
Article • 10/10/2022

Microsoft Configuration Manager server applications that are developed by using the
Configuration Manager SDK, have the following runtime requirements.

Managed Code
      A supported version of Windows Server as defined in Supported operating systems
      for Configuration Manager site system servers. For more information, see General
      Requirements.

      Installed Configuration Manager site server

      Microsoft.ConfigurationManagement.ManagementProvider .NET Framework
      assembly

      Microsoft .NET Framework version 4

Configuration Manager Console User Interface
Extension
Programming Configuration Manager console extensions has the following
requirements:

      Installed Configuration Manager site server

      Installed Configuration Manager console

      .NET Framework 4.0

      For more information, see About console extensions.

VBScript
      Installed Configuration Manager site server

      Windows Script Host

<!-- p.12 -->

Windows 64-Bit Support
A 32-bit compiled application that uses Configuration Manager SDK interfaces to access
Configuration Manager client or Configuration Manager server functionality works when
it runs in 32-bit emulation on a 64-bit Windows operating system. However, a 64-bit
compiled application that uses Configuration Manager SDK interfaces that access 32-bit
Configuration Manager client or Configuration Manager server functionality does not
work. Similarly, Configuration Manager SDK scripts do not work when the scripting host
is a native 64-bit application. A Configuration Manager SDK script does work if it is
called from within a 32-bit scripting host.

General Requirements

  ） Important

  For more information about general Configuration Manager requirements, see
  Supported configurations for Configuration Manager.

See Also
About console extensions Configuration Manager Client Development Requirements
Configuration Manager Server Development Requirements

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.13 -->

Configuration Manager Client
Development Requirements
Article • 10/10/2022

The Configuration Manager client can be programmed by using the following
programming languages.

Managed Code
If you are programming the Configuration Manager client by using managed code, you
use the System.Management namespace and, where applicable, you use COM
Interoperability to access the Configuration Manager automation objects.

NET Framework
You should have version 4.0 of the Microsoft .NET Framework installed on the
development computer and on the computers you want to deploy your .NET Framework
application to. To download the .NET Framework redistributable package, see Download
.NET Framework         . It is also installed as part of Visual Studio.

VBScript
You can use VBScript to access the Configuration Manager client WMI namespaces. The
client also has a number of COM automation objects that you can use.

For more information about scripting with WMI, see Windows Management
Instrumentation.

C++
C++ examples are provided for some Configuration Manager technologies where C++
is the most appropriate development language. In most cases, C++ developers should
use the VBScript samples as a guide. For more information about using WMI with C++,
see Creating a WMI Application Using C++.

Other Languages

<!-- p.14 -->

For languages that are not based on .NET Framework, use the VBScript samples as a
starting point for accessing Configuration Manager through WMI.

  ） Important

  For more information about general Configuration Manager requirements, see
  Supported configurations.

See Also
Configuration Manager Server Development Requirements
Configuration Manager SDK Libraries and Header Files

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.15 -->

Configuration Manager Server
Development Requirements
Article • 10/10/2022

In Configuration Manager, the SMS Provider and associated technologies can be
programmed by using the following programming languages.

Managed Code
The Configuration Manager SDK provides Microsoft .NET Framework libraries for
accessing the SMS Provider and also for extending the Configuration Manager console.

  ７ Note

  You can also use the System.Management namespace for accessing the SMS
  Provider, but this approach is not documented in the Configuration Manager SDK.

Programming the SMS Provider with managed code has the following requirements:

      Installed Configuration Manager site server

      Microsoft.ConfigurationManagement.ManagementProvider .NET Framework
      assembly.

      Microsoft Visual Studio

      Microsoft .NET Framework version 4

NET Framework
You should have version 4 of the .NET Framework installed on the development
computer and on the computers you want to deploy your .NET Framework application
to. To download the .NET Framework redistributable package, see Download .NET
Framework     . It is also installed as part of Visual Studio.

Configuration Manager Console User Interface
Extension

<!-- p.16 -->

Programming Configuration Manager console extensions has the following
requirements:

     Installed Configuration Manager site server

     Installed Configuration Manager console

     Microsoft Visual Studio

     Microsoft.ConfigurationManagement.ManagementProvider .NET Framework
     assembly.

     Microsoft .NET Framework 4

     For more information, see About console extensions.

     For specific information about deploying Configuration Manager console
     extensions, see Configuration Manager Console Extension Deployment

VBScript
You can use Windows Management Instrumentation (WMI) to access the SMS Provider.

The scripting samples are provided in VBScript and use WMI to access Configuration
Manager. For more information, see Objects overview.

Programming the SMS Provider with VBScript has the following requirements:

     Installed Configuration Manager site server

     Windows Script Host

     For more information about scripting with WMI, see Windows Management
     Instrumentation.

C++
C++ examples are provided for some Configuration Manager technologies where C++
is the most appropriate development language. In most cases, C++ developers should
use the VBScript samples as a guide. For more information about using WMI with C++,
see Creating a WMI Application Using C++.

Other Languages

<!-- p.17 -->

For languages that are not based on the .NET Framework, use the VBScript samples as a
starting point for accessing Configuration Manager through WMI.

  ） Important

  For more information about general Configuration Manager requirements, see
  Supported configurations.

See Also
Configuration Manager Client Development Requirements
Configuration Manager SDK Libraries and Header Files

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.18 -->

Configuration Manager SDK libraries
Article • 10/10/2022

In Configuration Manager, when you write unmanaged applications, you might have to
include one or more of the following libraries. Use COM Interoperability to access COM
objects from .NET Framework applications.

                                                                              ﾉ   Expand table

 Library                                        Description

 ismifcom.dll                                   Contains a class wrapper for the install status
                                                MIF functions. Visual Basic and scripting
                                                programmers use this ActiveX control to create
                                                a status MIF file.

                                                Visual Basic users must select the ISMIFCOM 1.0
                                                Type Library project reference. Scripting users
                                                create this object by using
                                                "ISMIFCOM.InstallStatusMIF".

 Microsoft.ConfigurationManager.Messaging.dll   Contains A .NET assembly encapsulating the
                                                client SDK that has an object model and
                                                transport for communicating with Configuration
                                                Manager site server roles such as the
                                                management point.

 smsmsgapi.dll                                  Contains management point interface libraries.

 smsrsgen.dll                                   Contains the Discovery Data Record functions.
                                                This DLL must exist in the directory from where
                                                you start your application.

 smsrsgenctl.dll                                Contains a class wrapper for the Discovery Data
                                                Record Functions. Visual Basic and scripting
                                                programmers use this control to create
                                                discovery data records.

  ７ Note

  The library files are available as NuGet packages .

For more information about general Configuration Manager requirements, see
Supported configurations.

<!-- p.19 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.20 -->

Get started with Configuration Manager
programming
Article • 10/10/2022

To get started with programming for Configuration Manager, it's beneficial to have a
basic functional and architectural understanding of Configuration Manager. In addition,
there are a number of key tools and resources that critical to validating and
troubleshooting solutions. Below are tips and resources for someone new to
programming for Configuration Manager.

  ） Important

  You should recognize that Configuration Manager, previously Systems
  Management Server (SMS), has quite a long history as a product. In reviewing
  namespaces, classes, methods, properties and log files you'll find many references
  containing "SMS" – in fact, most WMI classes start with "SMS_" and the primary
  Configuration Manager WMI namespace is "SMS". Over the course of years,
  numerous legacy classes, methods and properties have accumulated – not
  apparent to an administrative user, but when programming the history/legacy can
  be confusing.

Functional understanding
To successfully automate or extend Configuration Manager, it is incredibly important to
gain a functional understanding of the product. Configuration Manager is multi-tiered,
distributed management system, most often spread over numerous servers and
numerous locations. For more information, see Fundamentals of Configuration Manager.

More resources

Books
      System Center 2012 Configuration Manager: Mastering the Fundamentals

      System Center 2012 Configuration Manager (SCCM) Unleashed

      Microsoft System Center 2012 Configuration Manager: Administration Cookbook

<!-- p.21 -->

Videos
     YouTube: Technical Deep Dive: Configuration Manager 2012 Technical Overview

Forums

     Configuration Manager on Microsoft Q&A

     windows-noob.com: Configuration Manager 2012

Architectural understanding
Configuration Manager is multi-tiered, distributed management system. It's important
to understand the general architecture of Configuration Manager. Below is a link to an
overview of the Configuration Manager architecture.

     Architectural Overview

In addition to the architectural information, there are several key points that commonly
confuse administrators and programmers new to Configuration Manager.

     Server: In a general sense, most programming actions (in particular, automation)
     take place on a Configuration Manager site server. Actions or configuration
     changes are propagated throughout the Configuration Manager hierarchy to the
     clients via policy. Policy is pulled down by the client on a configurable polling
     interval NOT pushed immediately to the client by the server. In general, once a
     client is installed, there is no direct communication from the site server to the
     client or the client to the site server – all communication takes place through
     intermediary server roles.

     Client: Configuration Manager clients are systems and devices managed by
     Configuration Manager. A 'server' can be a Configuration Manger client. An
     Exchange server, an Active Directory server, and a Configuration Manager server
     can all be Configuration Manager clients. In addition, Windows 10, Windows
     Phone, and macOS devices can all be Configuration Manager clients.

Configuration Manager clients receive policy by periodically polling a Configuration
Manager Management Point. The polling interval for retrieving basic policy is
configurable, as are other settings. Because of this, there are inherent delays in client
targeted actions initiated from the Configuration Manager site server.

     Console: Remote Configuration Manager console binaries and files are not
     automatically updated when changes are made on the site server. Modifications

<!-- p.22 -->

     and extensions must be copied to systems running the Configuration Manager
     console, either manually or using Configuration Manager Application
     Management/Software Distribution.

     SMS Provider vs SQL Server: Although Configuration Manager leverages SQL
     Server for data storage, SQL Server is NOT the primary programming interface to
     Configuration Manager. The primary programming interface to Configuration
     Manager is the SMS Provider (WMI) - object creation and modification must be
     done via the SMS Provider. You should consider SQL Server as providing read-only
     access to Configuration Manager data for querying and reporting purposes. This is
     not a matter of permissions, rather matter of maintaining data integrity.

Namespaces and Classes

Server
Primary WMI Namespace: ROOT\SMS\SITE_<site code>

Server WMI Classes: Configuration Manager API reference

Client
Primary WMI Namespace: ROOT\CCM

Client WMI Classes: Configuration Manager API reference

  ） Important

  The client-side programming story for Configuration Manager is evolving to be
  primarily WMI-based. In the past, a set of client-side COM classes were the primary
  method used to access client functionality, although additional client-side WMI
  classes/methods were also used. With the release of System Center 2012
  Configuration Manager, the focus is shifting to a set of WMI classes in the
  namespace: root/ccm/ClientSDK. Understandably, an abstraction, in the form of
  COM or specific SDK classes, provides a useful abstraction from underlying
  architectural changes over the course of product updates.

Console
Console-related Managed Classes:

<!-- p.23 -->

     Microsoft.configurationmanagement.exe

     Microsoft.configurationmanagement.managementprovider.dll

     Microsoft.ConfigurationManagement.DialogFoundation.dll

     AdminUI.DialogFoundation.dll

Introductory Configuration Manager Console topics:

     About Configuration Manager Console Extension

     Configuration Manager Console Extension Architecture

Programming fundamentals
The Configuration Manager Programming Fundamentals section of the SDK provides
examples of how to work with the various types of objects and structures available in
Configuration Manager. Configuration Manager contains some objects/concepts that
can be initially confusing. Of particular interest are embedded properties (used primary
with the Site Control File) and lazy properties (used throughout the Configuration
Manager classes). Below are links to the Programming Fundamentals (and other sub-
sections) of the SDK. These sections contain code examples showing how to work with
the various object types.

  ） Important

  The SDK most often provides code examples in VBScript and C#. This does not
  mean that other languages will not work with the SMS Provider. The SMS Provider
  is language agnostic, as long as the correct objects and constructs can be
  exchanged. Use the language (tool) that is most appropriate for your environment.
  C# is used internally as a baseline for testing the SDK code snippets, so examples of
  object manipulation and code constructs will most often be provided in C#. If you
  use another language, you should be comfortable translating from C# to your
  language of choice.

     SMS Provider fundamentals

     Objects overview

     About the site control file

     About errors

<!-- p.24 -->

Basic tools

WBEMTEST
If you spend much time around Configuration Manager you become aware that much of
it runs through WMI. WMI is "Windows Management Instrumentation" and is
Microsoft's implementation of an Internet standard called Web Based Enterprise
Management (WBEM). There are many WMI tools out there. However, WBEMTEST is
immediately available on most systems, rather than having to be downloaded first. You
might think of it like Notepad.exe – there are text editors with richer capabilities
available, but Notepad.exe is always there when you need to view or create a text file.

Introduction to WBEMTEST

   Tip

  Internally, the most commonly used tool when troubleshooting SMS Provider
  related issues (object creation, modification and deletion) is WBEMTEST.

CMTrace
CMTrace: CMTrace is a customized log file viewer that is useful in monitoring and
troubleshooting Configuration Manager. CMTrace provides a continuous view of the log
file changes (rather than having to reload to monitor logged activity) and is particularly
useful when monitoring/troubleshooting object creation or modification via the SMS
Provider (see the SMSProv.log below).

CMTrace can be found on the Configuration Manager site server, under the "
<Configuration Manager Installation Directory>\tools" folder.

SMSProv.log: SMS Provider log file (<Configuration Manager Installation
Directory>\Logs\SMSProv.log) logs the activity of the SMS Provider and provides low-
level information that is useful to monitor/troubleshoot issues when programmatically
creating or modifying Configuration Manager objects via the SMS Provider.

Client Spy and Policy Spy
Client Spy: A tool that helps you troubleshoot issues related to software distribution,
inventory, and software metering on System Center 2012 Configuration Manager clients.

<!-- p.25 -->

Policy Spy: A policy viewer that helps you review and troubleshoot the policy system on
System Center 2012 Configuration Manager clients.

Basic Configuration Manager program example
Below is link to a very simple Configuration Manager program showing some basic
operations common to many Configuration Manager programs:

      Connect to the SMS Provider

      List all programs

     Create a new program

     Modify an existing program

     Delete an existing program

     Simple Example of List, Create, Modify, and Delete

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.26 -->

Architectural overview
Article • 10/10/2022

Configuration Manager is a configuration management product that requires servers to
administer client computers. The following sections describe both Configuration
Manager server and client architecture. Gaining an understanding of the concepts
relating to both server and client architecture will help you understand how you can
customize Configuration Manager for specific uses in your organization.

Configuration Manager server architecture
The Configuration Manager server architecture can be divided into two separate tiers:

      The Configuration Manager components
      The WBEM interface to the Configuration Manager architecture (SMS Provider)

Configuration Manager components are analogous to the mechanisms and devices that
enable the elevator, the phone system, and the electrical system in an office building to
work properly. When you make changes through the Configuration Manager console,
Configuration Manager services and components start working to complete the
operation successfully, whether it's software distribution, hardware inventory, or any
other administrator-initiated or schedules Configuration Manager task, feature, or tool.

The WBEM interface to the Configuration Manager architecture is a description of the
Configuration Manager framework, much as building plans describe a building. As you
become more familiar with Configuration Manager, you might find that your
organization needs to provide Configuration Manager functionality in a slightly different
fashion. You might need to gather additional inventory information and store it in your
Configuration Manager database. The WBEM interface enables you to customer
Configuration Manager for optimal change and configuration management.

SMS component and data store architecture
To fully understand Configuration Manager features, you need a basic understanding of
the elements that make up Configuration Manager. Service components, thread
components, and data stores are the major elements of Configuration Manager server
architecture. Each of these elements does a specific function to complete the work that
you assign and schedule.

SMS components

<!-- p.27 -->

In Configuration Manager, components are threads, services, and applications that run
on both server and client computers and provide Configuration Manager functionality.
Service and thread components accomplish the many tasks Configuration Manager
requires to function – tasks such as communication for inter- and intra-site connectivity,
configuration, resource discovery, client installation, database maintenance, status, site
system installation, and reporting.

Data stores
A dynamic computing environment must have a central location that stores the critical
operations information. Also, server and client components need access to their
configuration data, scheduled times of operation, and the data in the Configuration
Manager site database to accomplish tasks. For example, Collection Evaluator operation
requires information such as which collections to evaluate, when to evaluate them, and
what resources belong to each specific collection. To do these tasks, Collection Evaluator
needs access to both configuration data and data stored in the Configuration Manager
site database.

In Configuration Manager, there are two basic types of data stores: configuration data
and system data.

Configuration data

Configuration Manager gathers configuration data from Configuration Manager default
settings, changes you make through the Configuration Manager console, and changes
Configuration Manager services make. Configuration is a dynamic system that enables
you to make decisions about how and with the site will operate. As you make
configuration changes, Configuration Manager updates the site control file and the
registry. The site control file contains configuration for a Configuration Manager site.
Many Configuration Manager features, such as Software Inventory, function on a
schedule. After Configuration Manager server service and thread components are
enabled, they periodically check the site control file for their configuration and schedule
as they continue to work.

System data

Configuration Manager gathers system data from the various resources in the site.
Systems within an organization change constantly as hardware and software are
upgraded and repaired, new systems are brought on line, and old systems are retired.
Configuration Manager stores the information in the Configuration Manager site

<!-- p.28 -->

database. This database stores all of the data pertinent to Configuration Manager
functions including DDRs, MIF files, network discovery data, and site configuration data.

The WBEM interface with the SMS architecture
Configuration Manager provides an open architecture that enables you to write
applications and scripts that automate and customize Configuration Manager features,
such as Software Distribution. You can also create and install customized programs that
you can start from the Configuration Manager console.

Terms and concepts that relate to Configuration Manager architecture originate from
various sources. Some originated with the Desktop Management Task Force (DMTF) and
were created to describe managed objects. Others are standard COM and Web-Based
Enterprise Management (WBEM) initiative terms and concepts. Still others are specific to
Configuration Manager.

                                                                              ﾉ   Expand table

 Term               Definition

 Windows            The Microsoft implementation of one of the DMTF standards for identifying
 Management         and manipulating managed objects.

 CIM Object         The primary component in the management infrastructure of the WBEM
 Manager            technology. Client applications access the CIM Object Manager to find the
                    correct provider.

<!-- p.29 -->

 Term              Definition

 SMS Provider      The WBEM provider that exposes the Configuration Manager site database.
                   The SMS Provider acts as an intermediary between the CIM Object Manager
                   and any Configuration Manager data. The SMS Provider also accesses the
                   Configuration Manager site database to provide data to the Configuration
                   Manager console.

 Configuration     A SQL Server database that stores Configuration Manager data. The
 Manager Site      managed objects (such as disk drives or collections) stored in the
 Database          Configuration Manager site database are represented by instances of
                   Configuration Manager classes in the database rather than records in a
                   database.

 WBEM              An executable application that makes API calls to the CIM Object Manager to
 Application       view or manage data from providers.

 Windows           A Windows service that starts and stops the CIM Object Manager.
 Management
 Service

 Configuration     A WBEM application.
 Manager Console

Configuration Manager and the WBEM architecture
Configuration Manager uses the WBEM architecture to manage objects. WBEM is an
industry initiative adopted by the DMTF that is also supported by many non-Windows
computer and network device manufacturers. The WBEM initiative complements Active
Directory that locates and manages entity policies. WBEM also provides a unifying
mechanism through which management applications can interact with the managed
entities (like Configuration Manager objects) – without you having to understand the
underlying management protocols that these entities use.

In Configuration Manager, objects are items such as client computers, advertisements,
and packages stored in the Configuration Manager database. The WBEM initiative
outlines the architecture used by Windows Management, Microsoft's implementation of
one of the DMTF object management standards.

The CIM Object Manager stores the metadata, Windows Management provides access
to the Configuration Manager configuration and operations data with an extensible,
platform-independent interface. And managed object, such as a disk drive or a
collection is represented by an instance of a Configuration Manager class. Each
Configuration Manager managed object is represented by a CIM class.

<!-- p.30 -->

Configuration Manager and Windows management
To view and manipulate objects, Configuration Manager makes a request to the CIM
Object Manager (the central WBEM component). Configuration Manager uses the site
database to store managed object data. However, Configuration Manager uses the CIM
Object Manager interface and the SMS Provider to view and manipulate that managed
data. You can't view or manipulate the Configuration Manager database directly.
Instead, you gain access to the underlying Configuration Manager site database through
the CIM Object Manager, which in turn communicates with the SMS Provider.

Client architecture
A Configuration Manager client computer is any computer in your organization that has
the Configuration Manager client software installed. Computers serving as Configuration
Manager site servers and site systems can also be installed as Configuration Manager
client computers, in addition to any other servers in your organization where you install
Configuration Manager client software.

Configuration Manager client software:

     Runs almost entirely as services, processes, or applications started from
     Configuration Manager services.

<!-- p.31 -->

     Runs from the client computer (as opposed to over the network).

     Maintains history information for most function so the client computer (such as
     software and hardware inventory).

See also
Getting started with Configuration Manager programming

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.32 -->

Introduction to WBEMTEST
Article • 01/05/2024

If you spend much time around Configuration Manager, you become aware that much
of it runs through WMI. WMI is "Windows Management Instrumentation" and is
Microsoft's implementation of an Internet standard called Web Based Enterprise
Management (WBEM).

As you dig further into Configuration Manager - perhaps doing task sequences and
wanting to provide intelligent branching, digging into hardware inventory to possibly
extend it, or working with the Configuration Manger SDK – you'll need to dig deeper in
to WMI/WBEM. One useful tool for working with WMI/WBEM is WBEMTEST. There are
many WMI tools out there. However, WBEMTEST is immediately available on most
systems, rather than having to be downloaded first. You might think of it like
Notepad.exe – there are text editors with richer capabilities available, but Notepad.exe is
always there when you need to view or create a text file.

Opening WBEMTEST
WBEMTEST is available on any Windows system. Go to Start and type "WBEMTEST" into
the search or run box.

When you launch WBEMTEST, different operating system will work slightly differently.
Some will automatically connect to a WMI namespace, others (like Windows 7) won't. If
you aren't connected automatically to a WMI namespace, you can hit the connect
button, make sure that "root\cimv2" is selected, then hit connect again. Now you're
back in the main user interface with everything available (when not connected, most
buttons are grayed out). You can think of a WMI namespace as similar to a directory
within WMI. You can navigate to other WMI namespaces, just like you might change
directories on the file system. ROOT\CIMV2 is a WMI namespace where much hardware
information is kept – a good starting point.

  ） Important

  One limitation of WBEMTEST, is that it doesn't browse the WMI namespaces – you
  need to know where you're going to connect. ROOT\CIMV2 (all Windows systems),
  ROOT\CCM (Configuration Manager clients) and ROOT\SMS\site_<site code>
  (Configuration Manager site server) are some useful starting points.

ROOT\CIMV2 Namespace

<!-- p.33 -->

Configuration Manager Primary Client Namespace

Configuration Manager Primary Site Server Namespace (Site Code: ABC)

<!-- p.34 -->

Once you're connected to a WMI namespace, there are many options. If you're already a
WMI expert and know what you are after, you could hit the query button and type in a
WMI query to look for something specific.

When just starting out, one approach is to explore WMI a bit by browsing the classes in
the ROOT\CIMV2 namespace.

   1. Open WBEMTEST.

   2. Connect to the ROOT\CIMV2 namespace.

   3. Click the Enum Classes button.

   4. Select Recursive and click OK.

     You have just done the equivalent of a DIR to list all the contents of the
     namespace. Everything with underscores (_) in the front of the name is WMI
     overhead - this is what helps WMI be WMI. In most cases you'll skip over everything
     starting with underscores (\_) and look at classes that are specific interest to you.

     A more specific example using Win32_Service :

   5. Open WBEMTEST.

   6. Connect to the ROOT\CIMV2 namespace.

   7. Click the Enum Classes button.

<!-- p.35 -->

  8. Select Recursive and click OK.

  9. Browse to Win32_Service and select it by double-clicking.

     You have now opened up the Win32_Service class in WMI - all of the services on
     your computer are related to this class. (It gets a little complicated here and the
     directory analogy breaks down at this point – we'll skip the details and move on to
     some useful next steps).

 10. Click the Instances button to see a list of the services available on your computer.

 11. Pick a service, such as RemoteRegistry and select it by double-clicking.

 12. Click the Show MOF button.

     Looking at the MOF is a convenient way to look at the information about the
     RemoteRegistry service- here you can see the service state, description, start mode,
     etc.

     This was just a starting point to introduce WBEMTEST. Once you're familiar with
     WBEMTEST, it will become an invaluable tool as you dig into WMI.

More Resources
Books: There are numerous books available for WMI. A few example books are listed
below.

     Developing WMI Solutions: A Guide to Windows Management Instrumentation

     Windows Management Instrumentation

     Microsoft® Windows® Scripting with WMI: Self-Paced Learning Guide

     Videos: There are numerous videos available for WMI. A few example videos are
     listed below.

     YouTube: WMI PowerShell Introduction

     YouTube: What is WMI and how to enable remote WMI ?

     Other: Other resources for WMI are listed below.

     Windows Management Instrumentation (SDK)

     WMI Scripting Primer: Part 1

     WMI Scripting Primer: Part 2

<!-- p.36 -->

     WMI Scripting Primer: Part 3

See Also
Getting Started with Configuration Manager Programming

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.37 -->

Simple Example of List, Create, Modify,
and Delete
Article • 10/04/2022

The following example shows set of very basic methods using the SMS_Package class to
demonstrate List, Create, Modify and Delete operations using the SMS Provider. This is a
look at the structure of a basic Configuration Manager program – there are more useful
method snippets in other areas of the SDK that accomplish specific tasks.

  ） Important

  To simplify the code example, some methods are commented out, as they need
  additional information (an existing package identifier). Use the ListPackages
  method to obtain the package identifier for use with the ModifyPackage and
   DeletePackage methods.

To list packages
   1. Set up a connection to the SMS Provider.

   2. Run a query, which populates a variable with a collection of SMS_Package class
      instances.

   3. Enumerate through the collection and list the packages returned by the query.

To create a package
   1. Set up a connection to the SMS Provider.

   2. Create the new package object by using the SMS_Package class.

   3. Populate the new package properties.

   4. Save the package.

To modify a package
   1. Set up a connection to the SMS Provider.

   2. Load the existing package object by using the SMS_Package class.

<!-- p.38 -->

   3. Modify a package property.

   4. Save the package.

To delete a package
   1. Set up a connection to the SMS Provider.

   2. Load the existing package object by using the SMS_Package class.

   3. Delete the package by using the delete method.

Example
The following example method shows set of very basic methods using SMS_Package class
to demonstrate List, Create, Modify and Delete operations using the SMS Provider.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  ７ Note

  The below example embeds the calling code in the code. Most other examples in
  SDK the simply show a method with parameters.

  c#

  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;

  // Added the below Configuration Manager DLL references to support basic SMS
  Provider operations:
  //    C:\Program Files (x86)\Microsoft Endpoint
  Manager\AdminConsole\bin\Microsoft.ConfigurationManagement.ManagementProvide
  r.dll
  //    C:\Program Files (x86)\Microsoft Endpoint
  Manager\AdminConsole\bin\AdminUI.WqlQueryEngine.dll
  // Added the below Configuration Manager namespaces to support basic SMS
  Provider operations:
        using Microsoft.ConfigurationManagement.ManagementProvider;
        using
  Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine;

<!-- p.39 -->

//
// A set of very basic methods using the SMS_Package class to demonstrate
List, Create, Modify and Delete operations using the SMS Provider.
//
// Note: To simplify the code example, some methods are commented out, as
they need additional information (an existing package identifier).
// Use the ListPackages method to obtain the package identifier for use with
the ModifyPackage and DeletePackage methods.
//
namespace BasicApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Setup Objects
            SnippetClass BasicCMAppSnippets = new SnippetClass();

            // Setup a connection to the SMS Provider.
            // Passing in <server name>, <domain\\account>, <password>.
            WqlConnectionManager WMIConnection =
BasicCMAppSnippets.Connect("CMLABSERVER", "CMLABSERVER\\cmlabuser",
"password");

            // List all packages (instances of SMS_Package).
            BasicCMAppSnippets.ListPackages(WMIConnection);

            // Create a new package.
            // Note: This is not a useful package (too few properties), just
a demonstration of creating a Configuration Manager object.
            BasicCMAppSnippets.CreatePackage(WMIConnection, "New Package",
"This is the new package.");

            // Modifies a specific package (instance of SMS_Package).
            // A valid PackageID needs to be passed to the ModifyPackage
method - replace "ABC00000".
            //BasicCMAppSnippets.ModifyPackage(WMIConnection, "ABC00000");

            // Deletes a specific package (instance of SMS_Package).
            // A valid PackageID needs to be passed to the DeletePackage
method - replace "ABC00000".
            //BasicCMAppSnippets.DeletePackage(WMIConnection, "ABC00000");

            // Delay to keep the console output visible.
            Console.ReadLine();
        }
    }

    class SnippetClass
    {
        public WqlConnectionManager Connect(string serverName, string
userName, string userPassword)
        {
            try

<!-- p.40 -->

               {
                 SmsNamedValuesDictionary namedValues = new
SmsNamedValuesDictionary();
                 WqlConnectionManager connection = new
WqlConnectionManager(namedValues);
                 if (System.Net.Dns.GetHostName().ToUpper() ==
serverName.ToUpper())
                 {
                      connection.Connect(serverName);
                 }
                 else
                 {
                      connection.Connect(serverName, userName, userPassword);
                 }
                 return connection;
             }
             catch (SmsException ex)
             {
                 Console.WriteLine("Failed to connect. Error: " +
ex.Message);
                 return null;

               }
               catch (UnauthorizedAccessException ex)
               {
                   Console.WriteLine("Failed to authenticate. Error:" +
ex.Message);
                   throw;
               }
        }

        public void ListPackages(WqlConnectionManager connection)
        {
            try
            {
                // This query selects all packages (instances of
SMS_Package).
                string query = "SELECT * FROM SMS_Package";

                // Run query, which populates 'listOfPackages' with a
collection of package objects.
                IResultObject listOfPackages =
connection.QueryProcessor.ExecuteQuery(query);

                   // Output header for list of distribution points.
                   Console.WriteLine(" ");
                   Console.WriteLine("List of packages: ");
                   Console.WriteLine("-------------------");

                   // Enumerate through the collection of objects returned by
the query.
                   foreach (IResultObject package in listOfPackages)
                   {
                       // Output the package name for each package object.
                       Console.WriteLine("Package ID: {0} Package Name: {1}",
