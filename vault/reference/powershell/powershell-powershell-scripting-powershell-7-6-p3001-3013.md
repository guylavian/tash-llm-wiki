---
title: "How to use this documentation — pages 3001-3013"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p3001-3013
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p3001-3013
family: powershell
documentKind: "doc"
abstract: "Labeling in GitHub Article • 03/30/2025 This article documents how we label issues and pull requests in the PowerShell-Docs repository. This article is designed to be a job aid for members of the PowerShell-Docs team. We publish this information here to provide process transpare"
---

# How to use this documentation — pages 3001-3013

<!-- p.3001 -->

Labeling in GitHub
Article • 03/30/2025

This article documents how we label issues and pull requests in the PowerShell-Docs
repository. This article is designed to be a job aid for members of the PowerShell-Docs
team. We publish this information here to provide process transparency for our public
contributors.

Labels always have a name and a description that is prefixed with their type.

Area labels
Area labels identify the parts of PowerShell or the documentation that the issue relates
to.

                                                                             ﾉ   Expand table

 Label                 Related Content

 area-about            The about_* articles.

 area-archive          The Microsoft.PowerShell.Archive module.

 area-cim              The CimCmdlets module.

 area-community        Community-facing projects, including the contributor's guide and
                       monthly updates.

 area-conceptual       Conceptual articles (not cmdlet reference).

 area-console          The console host

 area-core             The Microsoft.PowerShell.Core module.

 area-crescendo        The Crescendo module.

 area-debugging        Debugging PowerShell.

 area-diagnostics      The Microsoft.PowerShell.Diagnostics module.

 area-dsc              PowerShell Desired State Configuration.

 area-editorsvcs       The PowerShell editor services.

 area-engine           The PowerShell engine.

 area-error-handling   Error handling in PowerShell

<!-- p.3002 -->

Label                Related Content

area-experimental    PowerShell's experimental features

area-gallery         The PowerShell Gallery.

area-helpsystem      The Help services, including the pipeline and *-Help cmdlets.

area-host            The Microsoft.PowerShell.Host module.

area-ise             The PowerShell ISE.

area-jea             The Just Enough Administration feature.

area-language        The PowerShell syntax and keywords.

area-learn           The structured training content for PowerShell.

area-localaccounts   The Microsoft.PowerShell.LocalAccounts module.

area-localization    Localization problems or opportunities for the content.

area-management      The Microsoft.PowerShell.Management module.

area-native-cmds     Using native commands in PowerShell.

area-omi             Open Management Infrastructure & CDXML.

area-ops-issue       Building and rendering the content on the site.

area-other           Miscellaneous modules.

area-overview        The overview section in the conceptual content.

area-                The PackageManagement module.
packagemanagement

area-parallelism     Content covering parallel processing, such as using ForEach-Object or
                     PowerShell Jobs.

area-platyps         The PlatyPS module.

area-portability     Cross-platform compatibility.

area-powershellget   The PowerShellGet module.

area-providers       PowerShell providers.

area-psreadline      The PSReadLine module.

area-release-notes   The PowerShell release notes.

<!-- p.3003 -->

 Label                    Related Content

 area-remoting            The PowerShell remoting feature and cmdlets.

 area-scriptanalyzer      The PSScriptAnalyzer module.

 area-sdk-docs            The conceptual documentation for the PowerShell SDK.

 area-sdk-ref             The .NET API reference documentation for the PowerShell SDK.

 area-security            The Microsoft.PowerShell.Security module and security concepts in
                          general.

 area-setup               Installing and configuring PowerShell.

 area-threadjob           The ThreadJob module.

 area-utility             The Microsoft.PowerShell.Utility module.

 area-versions            Issues with the versioning of the documentation.

 area-vscode              The VS Code PowerShell extension.

 area-wincompat           The Windows Compatibility feature.

 area-wmf                 The Windows Management Framework.

 area-workflow            The Windows PowerShell Workflow feature.

Issue labels
Issue labels distinguish issues by purpose.

                                                                                 ﾉ   Expand table

 Label                         Issue Category

 issue-doc-bug                 Errors or ambiguities in the content

 issue-doc-idea                Requests for new content

 issue-kudos                   Praise, positive feedback, or thanks rather than work items

 issue-product-feedback        Feedback or problems with the product itself

 issue-question                Support questions

Priority labels

<!-- p.3004 -->

Priority labels rank which work items need to be worked on before others. These labels
are only used when needed to manage large sets of work items.

                                                                                   ﾉ   Expand table

                           Label     Priority Level

                           Pri0      Highest

                           Pri1      High

                           Pri2      Medium

                           Pri3      Low

Project Labels
Project labels indicate what ongoing GitHub Project a work item is related to. These
labels are used for automatically adding work items to a project on creation.

                                                                                   ﾉ   Expand table

                             Label     Project

                   project-quality     The quality improvement project

Quality labels
Quality labels categorize work items for the quality improvement effort.

                                                                                   ﾉ   Expand table

 Label                             Improvement

 quality-aliases                   Ensure cmdlet aliases are documented

 quality-format-code-samples       Ensure proper casing, line length, and other formatting in code
                                   samples

 quality-format-command-           Ensure proper casing and formatting for command syntax
 syntax

 quality-link-references           Ensure links in conceptual docs are defined as numbered
                                   references

<!-- p.3005 -->

 Label                         Improvement

 quality-markdownlint          Ensure content follows markdownlint rules

 quality-spelling              Ensure proper casing and spelling for words

Status labels
Status labels indicate why a work item was closed or shouldn't be merged. Issues are
only given status labels when they're closed without a related PR.

                                                                                   ﾉ   Expand table

 Label                             Status

 resolution-answered               Closed by existing documentation

 resolution-duplicate              Closed as duplicate issue

 resolution-external               Closed by customer or outside resource

 resolution-no-repro               Unable to reproduce the reported issue

 resolution-refer-to-support       Closed and referred to community or product support

 resolution-wont-fix               Closed as won't fix

Tag labels
Tag labels add independent context for work items.

                                                                                   ﾉ   Expand table

 Label                     Purpose

 in-progress               Someone is actively working on the item

 go-live                   The work item is related to a specific release

 doc-a-thon                The work item is related to a doc-a-thon

 up-for-grabs              Any contributor can volunteer to resolve the work item

 hacktoberfest-accepted    The PR is accepted for inclusion in #hacktoberfest

 hacktoberfest-candidate   The PR is a candidate for inclusion in #hacktoberfest

<!-- p.3006 -->

 Label                    Purpose

 needs-triage             The issue must be triaged by the team before it's ready to be worked

 code-of-conduct          Closed for spam, trolling, or code of conduct violations

 do-not-merge             The PR isn't meant to be merged

Waiting labels
Waiting labels indicate that a work item can't be resolved until an external condition is
met.

                                                                               ﾉ     Expand table

 Label                     Waiting For

 hold-for-pr               Upstream PR to be merged

 hold-for-release          Upstream product to release

 needs-investigation       Waiting for team member to verify or research

 needs-more-info           Additional details or clarification from work item author

 needs-response            Response from work item author

 review-shiproom           Shiproom discussion with the PowerShell team

<!-- p.3007 -->

PowerShell Support Lifecycle
There are multiple versions of PowerShell 7 that can be installed.

     Stable release - A stable release is a release that occurs between LTS releases. Stable
     releases can contain critical fixes, innovations, and new features. Microsoft supports a Stable
     release for about six months after the next LTS release.

     The current Stable release is PowerShell 7.5.9.

     Long Term Servicing (LTS) release - An LTS release of PowerShell is an LTS release of .NET.
     Updates to an LTS release only contain critical security updates and servicing fixes that are
     designed to minimize impact on existing workloads.

     The current LTS release is PowerShell 7.6.4. The previous LTS release, PowerShell 7.4.18, is
     still supported until 10-Nov-2026.

     Preview release - A preview release is a version of PowerShell that's currently in
     development. Preview releases can contain breaking changes, bug fixes, new features, and
     experiments. Preview releases might contain bugs and might not be stable. For that reason,
     you shouldn't use them in production environments. Preview versions aren't officially
     supported. They allow you to test out new features and provide feedback. Your feedback is
     important and can influence the features that get released.

     PowerShell 7.7-preview.2 is the current preview release.

PowerShell follows the Microsoft Modern Lifecycle Policy. The end-of-support dates follow the
.NET Support Policy    for the version of .NET that the release of PowerShell was built upon. Both
LTS and Stable releases of PowerShell receive security updates and bug fixes. Microsoft only
supports the latest update version of a release.

  ７ Note

  This document is about support for PowerShell, not Windows PowerShell. Windows
  PowerShell is a component of the Windows operating system and is subject to the Windows
  support lifecycle. For more information, see Product and Services Lifecycle Information.

Support options

<!-- p.3008 -->

Microsoft provides support for PowerShell on a best-effort basis. Support for Windows
PowerShell 5.1 is provided through Windows support channels. You can use the standard paid
support channels to get support for PowerShell.

     Support for business
     Contact support

There are many free support options available from the PowerShell community. The most active
community support channels are available through Discord or Slack. The discussion channels are
mirrored on both platforms, so you can choose the platform that you prefer. These channels can
help you troubleshoot issues, answer questions, and provide guidance on how to use PowerShell.

If you think that you found a bug, you can file an issue on GitHub . The PowerShell team can't
provide support through GitHub, but they welcome bug reports. The community support page
provides links to the most popular community support channels.

Supported platforms
PowerShell runs on multiple operating systems (OS) and processor architecture platforms. The
platform must meet the following criteria:

     The target platform (OS version and processor architecture) is supported by .NET
     Microsoft has tested and approved PowerShell on the target platform
     The OS version is supported by the distributor for at least one year
     The OS version isn't an interim release or equivalent
     The OS version is currently supported by the distributor

Support for PowerShell ends when either of the following conditions are met:

     The target platform reaches end-of-life as defined by the platform owner
     The specific version of PowerShell reaches end-of-life

After a version of PowerShell reaches end-of-life, no further updates, including security updates,
are provided. Microsoft encourages customers to upgrade to a supported version of PowerShell
to continue receiving updates and support.

Windows
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Windows reaches end-of-support.

<!-- p.3009 -->

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images are
available from the Microsoft Artifact Registry   . These images may not have the latest security
updates. Microsoft recommends that you update the OS packages to the latest version to ensure
the latest security updates are applied. These images are provided for testing purposes. If you
need a Docker image for a production workload, you should build and maintain your own image.

  ７ Note

  Support for a specific version of Windows is determined by the Microsoft Support Lifecycle
  policies. For more information, see:

        Windows client lifecycle FAQ
        Modern Lifecycle Policy FAQ

macOS
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of macOS
reaches end-of-support.

The following versions of macOS are supported:

     macOS 26 (Tahoe) x64 and Arm64
     macOS 15 (Sequoia) x64 and Arm64
     macOS 14 (Sonoma) x64 and Arm64

Apple determines the support lifecycle of macOS. For more information, see the following:

     macOS release notes
     Apple Security Updates

Alpine Linux
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of Alpine
reaches end-of-life   .

Support for these versions of Alpine ends on the following dates:

     Alpine 3.24 - 2028-06-01
     Alpine 3.23 - 2027-11-01
     Alpine 3.22 - 2027-05-01
     Alpine 3.21 - 2026-11-01

<!-- p.3010 -->

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images are
available from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provided by the OS distributor.
These images may not have the latest security updates. Microsoft recommends that you update
the OS packages to the latest version to ensure the latest security updates are applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

Debian Linux
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of Debian
reaches end-of-life   .

Support for these versions of Debian ends on the following dates:

     Debian 13 - 2028-08-09

Install package files ( .deb ) are also available from https://packages.microsoft.com/ .

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images are
available from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provide by the OS distributor.
These images may not have the latest security updates. Microsoft recommends that you update
the OS packages to the latest version to ensure the latest security updates are applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

Red Hat Enterprise Linux (RHEL)
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of RHEL
reaches end-of-support    .

Support for these versions of RHEL ends on the following dates:

     RHEL 10 - 2035-05-31
     RHEL 9 - 2032-05-31
     RHEL 8 - 2029-05-31

Install package files ( .rpm ) are also available from https://packages.microsoft.com/ .

<!-- p.3011 -->

PowerShell is tested on Red Hat Universal Base Images (UBI). For more information, see the UBI
information page     .

Ubuntu Linux
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of Ubuntu
reaches end-of-support       .

Support for these versions of Ubuntu ends on the following dates:

     Ubuntu 26.04 (Resolute Raccoon) - 2031-04-30
     Ubuntu 24.04 (Noble Numbat) - 2029-05-31
     Ubuntu 22.04 (Jammy Jellyfish) - 2024-09-30

Install package files ( .deb ) are also available from https://packages.microsoft.com/ .

The Docker images for the .NET SDK contain the latest versions of PowerShell. You can download
these images from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provide by the OS distributor.
These images may not have the latest security updates. Microsoft recommends that you update
the OS packages to the latest version to ensure the latest security updates are applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

  ７ Note

  Ubuntu 25.10 (Questing Quokka) is an interim release. Microsoft doesn't test or support
  interim releases       of Ubuntu. For more information, see Community supported
  distributions.

Support for PowerShell modules
The support lifecycle for PowerShell doesn't cover modules that ship outside of the PowerShell
release package. For example, using the ActiveDirectory module that ships as part of Windows
Server is supported under the Windows Support Lifecycle.

Support for experimental features

<!-- p.3012 -->

Experimental features aren't intended to be used in production environments. We appreciate
feedback on experimental features and we provide best-effort support for them.

Notes on licensing
PowerShell is released under the MIT license     . Under this license, and without a paid support
agreement, users are limited to community support. With community support, Microsoft makes
no guarantees of responsiveness or fixes.

PowerShell end-of-support dates
The PowerShell support lifecycle follows the support lifecycle of .NET    . The following table lists
the end-of-support dates for the current versions of PowerShell:

                                                                                    ﾉ    Expand table

 Version                              Release Date           End-of-support       .NET Version

 PowerShell 7.7 (preview)                                                         .NET 11.0

 PowerShell 7.6 (LTS)                 18-Mar-2026             14-Nov-2028         .NET 10.0

 PowerShell 7.5                        23-Jan-2025            10-Nov-2026         .NET 9.0

 PowerShell 7.4 (LTS)                 16-Nov-2023             10-Nov-2026         .NET 8.0

The following table lists the end-of-support dates for retired versions of PowerShell:

                                                                                    ﾉ    Expand table

 Version                          Release Date           End-of-support       .NET Version

 PowerShell 7.3                   09-Nov-2022             08-May-2024         .NET 7.0

 PowerShell 7.2 (LTS)             08-Nov-2021             08-Nov-2024         .NET 6.0

 PowerShell 7.1                   11-Nov-2020             08-May-2022         .NET 5.0

 PowerShell 7.0 (LTS)             04-Mar-2020             03-Dec-2022         .NET Core 3.1

 PowerShell 6.2                   29-Mar-2019             04-Sep-2020         .NET Core 2.1

 PowerShell 6.1                   13-Sep-2018             28-Sep-2019         .NET Core 2.1

 PowerShell 6.0                   20-Jan-2018             13-Feb-2019         .NET Core 2.0

<!-- p.3013 -->

Windows PowerShell release history
The following table contains a historical timeline of the major releases of Windows PowerShell.
Microsoft no longer supports Windows PowerShell versions lower than 5.1.

                                                                                        ﾉ   Expand table

 Version                      Release    Note
                               Date

 Windows PowerShell           Aug-2016   Released in Windows 10 Anniversary Update and Windows Server
 5.1                                     2016, WMF 5.1

 Windows PowerShell           Feb-2016   Released in Windows Management Framework (WMF) 5.0
 5.0

 Windows PowerShell           Oct-2013   Released in Windows 8.1 and with Windows Server 2012 R2, WMF
 4.0                                     4.0

 Windows PowerShell           Oct-2012   Released in Windows 8 and with Windows Server 2012 WMF 3.0
 3.0

 Windows PowerShell           Jul-2009   Released in Windows 7 and Windows Server 2008 R2, WMF 2.0
 2.0

 Windows PowerShell           Nov-2006   Released as optional component of Windows Server 2008
 1.0

Run the following command to see the full version number of .NET used by the version of
PowerShell you're running:

  PowerShell

  [System.Runtime.InteropServices.RuntimeInformation]::FrameworkDescription

 Last updated on 07/20/2026
