---
title: "How to use this documentation — pages 41-80"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p0041-0080
family: powershell
documentKind: "doc"
abstract: "PSReadLine history is recorded in ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt The profiles respect PowerShell's per-host configuration, so the default host-specific profiles exists at Microsoft.PowerShell_profile.ps1 in the same locations. PowerShell respects th"
---

# How to use this documentation — pages 41-80

<!-- p.41 -->

      PSReadLine history is recorded in
      ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

The profiles respect PowerShell's per-host configuration, so the default host-specific profiles
exists at Microsoft.PowerShell_profile.ps1 in the same locations.

PowerShell respects the XDG Base Directory Specification     on Linux.

Uninstall PowerShell 7
 sh

 sudo rm -rf /usr/bin/pwsh /opt/microsoft/powershell

Supported OS versions
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of Alpine
reaches end-of-life   .

Support for these versions of Alpine ends on the following dates:

      Alpine 3.24 - 2028-06-01
      Alpine 3.23 - 2027-11-01
      Alpine 3.22 - 2027-05-01
      Alpine 3.21 - 2026-11-01

The Docker images for the .NET SDK contain the latest versions of PowerShell. These images are
available from the Microsoft Artifact Registry   .

These images are built from official operating system (OS) images provided by the OS distributor.
These images may not have the latest security updates. Microsoft recommends that you update
the OS packages to the latest version to ensure the latest security updates are applied.

These images are provided for testing purposes. If you need a Docker image for a production
workload, you should build and maintain your own.

Supported installation methods
Microsoft supports the installation methods in this document. There may be other third-party
methods of installation available from other sources. While those tools and methods may work,
Microsoft can't support those methods.

<!-- p.42 -->

Last updated on 07/20/2026

<!-- p.43 -->

Install PowerShell 7 on Debian
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview
versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer
preview versions replace existing previous preview versions. If you need to run PowerShell 7.5
side-by-side with a previous version, reinstall the previous version using the binary archive
method.

Choose an installation method
On Debian Linux, you can install PowerShell using the universal .deb package from the Microsoft
package repository or by downloading a file from the GitHub releases      page.

Install PowerShell 7 from the Package Repository
Microsoft builds and supports a variety of software products for Linux systems and makes them
available via Linux packaging clients (apt, dnf, yum, etc). These Linux software packages are
hosted on the Linux package repository for Microsoft products, https://packages.microsoft.com    ,
also known as PMC.

Installing PowerShell from PMC is the preferred method of installation.

  ７ Note

  This script only works for supported versions of Debian that have a package published to the
  Microsoft package repository. For other supported versions of Debian, use the manual
  installation method.

 sh

 #!/bin/bash
 ###################################
 # Prerequisites

 # Update the list of packages

<!-- p.44 -->

 sudo apt-get update

 # Install pre-requisite packages.
 sudo apt-get install -y wget

 # Get the version of Debian
 source /etc/os-release

 # Download the Microsoft repository GPG keys
 wget -q https://packages.microsoft.com/config/debian/$VERSION_ID/packages-microsoft-
 prod.deb

 # Register the Microsoft repository GPG keys
 sudo dpkg -i packages-microsoft-prod.deb

 # Delete the Microsoft repository GPG keys file
 rm packages-microsoft-prod.deb

 # Update the list of packages after we added packages.microsoft.com
 sudo apt-get update

 ###################################
 # Install PowerShell
 sudo apt-get install -y powershell

 # Start PowerShell
 pwsh

Manually download and install PowerShell 7
Download the universal package from the GitHub releases page. Choose the link for the version
you want to install.

      PowerShell 7.6 (LTS) universal package for supported versions of Debian
         https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell_7.6.4-

        1.deb_amd64.deb

      PowerShell 7.5 universal package for supported versions of Debian
         https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell_7.5.9-

        1.deb_amd64.deb

      PowerShell 7.4 (LTS) universal package for supported versions of Debian
         https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell_7.4.1

        8-1.deb_amd64.deb

The following shell script downloads and installs the current release of PowerShell. You can
change the URL to download the version of PowerShell that you want to install.

 sh

<!-- p.45 -->

 #!/bin/bash
 ###################################
 # Prerequisites

 # Update the list of packages
 sudo apt-get update

 # Install pre-requisite packages.
 sudo apt-get install -y wget

 # Download the PowerShell package file
 wget
 https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell_7.6.4-
 1.deb_amd64.deb

 ###################################
 # Install the PowerShell package
 sudo dpkg -i powershell_7.6.4-1.deb_amd64.deb

 # Resolve missing dependencies and finish the install (if necessary)
 sudo apt-get install -f

 # Delete the downloaded package file
 rm powershell_7.6.4-1.deb_amd64.deb

 # Start PowerShell
 pwsh

Start PowerShell 7
After the package is installed, run pwsh from a terminal. If you have installed a Preview package,
run pwsh-preview .

     The location of $PSHOME varies based on the package you installed.
        For Stable and LTS packages: /opt/microsoft/powershell/7/
        For Preview packages: /opt/microsoft/powershell/7-preview/
     The profiles scripts are stored in the following locations:
        AllUsersAllHosts - $PSHOME/profile.ps1
        AllUsersCurrentHost - $PSHOME/Microsoft.PowerShell_profile.ps1
        CurrentUserAllHosts - ~/.config/powershell/profile.ps1
        CurrentUserCurrentHost - ~/.config/powershell/Microsoft.PowerShell_profile.ps1
     Modules are stored in the following locations:
        User modules - ~/.local/share/powershell/Modules
        Shared modules - /usr/local/share/powershell/Modules
        Default modules - $PSHOME/Modules

<!-- p.46 -->

      PSReadLine history is recorded in
      ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

The profiles respect PowerShell's per-host configuration, so the default host-specific profiles
exists at Microsoft.PowerShell_profile.ps1 in the same locations.

PowerShell respects the XDG Base Directory Specification     on Linux.

Uninstall PowerShell 7
 sh

 sudo apt-get remove powershell

Supported OS versions
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

Supported installation methods
Microsoft supports the installation methods in this document. There may be other methods of
installation available from other third-party sources. While those tools and methods may work,
Microsoft can't support those methods.

<!-- p.47 -->

Last updated on 07/20/2026

<!-- p.48 -->

Install PowerShell 7 on Red Hat Enterprise
Linux (RHEL)
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview
versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer
preview versions replace existing previous preview versions.

Choose an installation method
On RHEL, you can install PowerShell using the universal .rpm package from the Microsoft
package repository or by downloading file from the GitHub release page.

Install PowerShell 7 from the Package Repository
Microsoft builds and supports a variety of software products for Linux systems and makes them
available via Linux packaging clients (apt, dnf, yum, etc). These Linux software packages are
hosted on the Linux package repository for Microsoft products, https://packages.microsoft.com    ,
also known as PMC.

Installing PowerShell from PMC is the preferred method of installation.

  ７ Note

  This script only works for supported versions of RHEL that have a package published to the
  Microsoft package repository. For other supported versions of RHEL, use the manual
  installation method.

 sh

 #!/bin/bash
 ###################################
 # Prerequisites

 # Get version of RHEL
 source /etc/os-release

<!-- p.49 -->

 if [ ${VERSION_ID%.*} -ge 8 ]
 then majorver=8
 elif [ ${VERSION_ID%.*} -ge 9 ]
 then majorver=9
 fi

 # Download the Microsoft RedHat repository package
 curl -sSL -O https://packages.microsoft.com/config/rhel/$majorver/packages-microsoft-
 prod.rpm

 # Register the Microsoft RedHat repository
 sudo rpm -i packages-microsoft-prod.rpm

 # Delete the downloaded package after installing
 rm packages-microsoft-prod.rpm

 # Update package index files
 sudo dnf update
 # Install PowerShell
 sudo dnf install powershell -y

Manually download and install PowerShell 7
Download the universal package from the GitHub releases page. Select the URL of the package
version you want to install.

      PowerShell 7.6 (LTS) universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-

        1.rh.x86_64.rpm

      PowerShell 7.5 universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell-7.5.9-

        1.rh.x86_64.rpm

      PowerShell 7.4 (LTS) universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell-

        7.4.18-1.rh.x86_64.rpm

The following shell script downloads and installs the current release of PowerShell. You can
change the URL to download the version of PowerShell that you want to install.

 sh

 sudo dnf install
 https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-
 1.rh.x86_64.rpm

<!-- p.50 -->

Start PowerShell 7
After the package is installed, run pwsh from a terminal. If you have installed a Preview package,
run pwsh-preview .

      The location of $PSHOME varies based on the package you installed.
         For Stable and LTS packages: /opt/microsoft/powershell/7/
         For Preview packages: /opt/microsoft/powershell/7-preview/
      The profiles scripts are stored in the following locations:
         AllUsersAllHosts - $PSHOME/profile.ps1
         AllUsersCurrentHost - $PSHOME/Microsoft.PowerShell_profile.ps1
         CurrentUserAllHosts - ~/.config/powershell/profile.ps1
         CurrentUserCurrentHost - ~/.config/powershell/Microsoft.PowerShell_profile.ps1
      Modules are stored in the following locations:
         User modules - ~/.local/share/powershell/Modules
         Shared modules - /usr/local/share/powershell/Modules
         Default modules - $PSHOME/Modules
      PSReadLine history is recorded in
      ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

The profiles respect PowerShell's per-host configuration, so the default host-specific profiles
exists at Microsoft.PowerShell_profile.ps1 in the same locations.

PowerShell respects the XDG Base Directory Specification       on Linux.

Uninstall PowerShell 7
 sh

 sudo dnf remove powershell

Supported versions of RHEL
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of RHEL
reaches end-of-support     .

Support for these versions of RHEL ends on the following dates:

      RHEL 10 - 2035-05-31
      RHEL 9 - 2032-05-31

<!-- p.51 -->

      RHEL 8 - 2029-05-31

Install package files ( .rpm ) are also available from https://packages.microsoft.com/ .

PowerShell is tested on Red Hat Universal Base Images (UBI). For more information, see the UBI
information page       .

Supported installation methods
Microsoft supports the installation methods in this document. There may be other third-party
methods of installation available from other sources. While those tools and methods may work,
Microsoft can't support those methods.

 Last updated on 07/20/2026

<!-- p.52 -->

Install PowerShell 7 on Ubuntu
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview
versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer
preview versions replace existing previous preview versions. If you need to run PowerShell 7.5
side-by-side with a previous version, reinstall the previous version using the binary archive
method.

Choose an installation method
On Ubuntu Linux, you can install PowerShell using the universal .deb package from the Microsoft
package repository or by downloading a file from the stable release       page.

Install PowerShell 7 from the Package Repository
Microsoft builds and supports a variety of software products for Linux systems and makes them
available via Linux packaging clients (apt, dnf, yum, etc). These Linux software packages are
hosted on the Linux package repository for Microsoft products, https://packages.microsoft.com    ,
also known as PMC.

Installing PowerShell from PMC is the preferred method of installation.

  ７ Note

  This script only works for supported versions of Ubuntu that have a package published to
  the Microsoft package repository. For other versions of Ubuntu, use the manual installation
  method.

 sh

 #!/bin/bash
 ###################################
 # Prerequisites

 # Update the list of packages

<!-- p.53 -->

 sudo apt-get update

 # Install pre-requisite packages.
 sudo apt-get install -y wget apt-transport-https software-properties-common

 # Get the version of Ubuntu
 source /etc/os-release

 # Download the Microsoft repository keys
 wget -q https://packages.microsoft.com/config/ubuntu/$VERSION_ID/packages-microsoft-
 prod.deb

 # Register the Microsoft repository keys
 sudo dpkg -i packages-microsoft-prod.deb

 # Delete the Microsoft repository keys file
 rm packages-microsoft-prod.deb

 # Update the list of packages after we added packages.microsoft.com
 sudo apt-get update

 ###################################
 # Install PowerShell
 sudo apt-get install -y powershell

 # Start PowerShell
 pwsh

  ） Important

  Ubuntu comes preconfigured with a package repository that includes .NET packages, but
  not PowerShell. Using these instructions to install PowerShell registers the Microsoft
  repository as a package source. You can install PowerShell and some versions of .NET from
  this repository. However, the Ubuntu package repository has different versions of the .NET
  packages. This can cause problems when installing .NET for other purposes. For more
  information about these problems, see Troubleshoot .NET package mix ups on Linux.

  You must choose the feed you want to use to install .NET. You can set the priority of the
  package repositories to favor one over the other. For instructions on how to set the
  priorities, see My Linux distribution provides .NET packages, and I want to use them.

Manually download and install PowerShell 7
Download the universal package from the GitHub releases page. Select the URL of the package
version you want to install.

<!-- p.54 -->

      PowerShell 7.6 (LTS) universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell_7.6.4-

        1.deb_amd64.deb

      PowerShell 7.5 universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell_7.5.9-

        1.deb_amd64.deb

      PowerShell 7.4 (LTS) universal package
         https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell_7.4.1

        8-1.deb_amd64.deb

The following shell script downloads and installs the current preview release of PowerShell. You
can change the URL to download the version of PowerShell that you want to install.

 sh

 #!/bin/bash
 ###################################
 # Prerequisites

 # Update the list of packages
 sudo apt-get update

 # Install pre-requisite packages.
 sudo apt-get install -y wget

 # Download the PowerShell package file
 wget
 https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell_7.5.9-
 1.deb_amd64.deb

 ###################################
 # Install the PowerShell package
 sudo dpkg -i powershell_7.5.9-1.deb_amd64.deb

 # Resolve missing dependencies and finish the install (if necessary)
 sudo apt-get install -f

 # Delete the downloaded package file
 rm powershell_7.5.9-1.deb_amd64.deb

Start PowerShell 7
After the package is installed, run pwsh from a terminal. If you have installed a Preview package,
run pwsh-preview .

      The location of $PSHOME varies based on the package you installed.

<!-- p.55 -->

         For Stable and LTS packages: /opt/microsoft/powershell/7/
         For Preview packages: /opt/microsoft/powershell/7-preview/
      The profiles scripts are stored in the following locations:
         AllUsersAllHosts - $PSHOME/profile.ps1
         AllUsersCurrentHost - $PSHOME/Microsoft.PowerShell_profile.ps1
         CurrentUserAllHosts - ~/.config/powershell/profile.ps1
         CurrentUserCurrentHost - ~/.config/powershell/Microsoft.PowerShell_profile.ps1
      Modules are stored in the following locations:
         User modules - ~/.local/share/powershell/Modules
         Shared modules - /usr/local/share/powershell/Modules
         Default modules - $PSHOME/Modules
      PSReadLine history is recorded in
      ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

The profiles respect PowerShell's per-host configuration, so the default host-specific profiles
exists at Microsoft.PowerShell_profile.ps1 in the same locations.

PowerShell respects the XDG Base Directory Specification       on Linux.

Uninstall PowerShell
 sh

 sudo apt-get remove powershell

Support for Arm processors
PowerShell 7.2 and newer supports running on Ubuntu using 32-bit Arm processors. Use the
binary archive installation method of installing PowerShell that's described in Alternate ways to
install PowerShell on Linux.

Supported versions
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of Ubuntu
reaches end-of-support     .

Support for these versions of Ubuntu ends on the following dates:

      Ubuntu 26.04 (Resolute Raccoon) - 2031-04-30
      Ubuntu 24.04 (Noble Numbat) - 2029-05-31

<!-- p.56 -->

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

Supported installation methods
Microsoft supports the installation methods in this document. There may be other methods of
installation available from other third-party sources. While those tools and methods may work,
Microsoft can't support those methods.

 Last updated on 07/20/2026

<!-- p.57 -->

Community support for PowerShell on Linux
You can install PowerShell on some distributions of Linux that aren't supported by Microsoft. In
those cases, you might find support from the community for PowerShell on those platforms.

Supported Linux distributions must meet the following criteria:

       The version and architecture of the distribution is supported by .NET Core.
       The version of the distribution is supported for at least one year.
       The version of the distribution isn't an interim release or equivalent.
       The PowerShell team has tested the version of the distribution.

For more information, see the PowerShell Support Lifecycle documentation.

The following distributions are examples of distributions supported by the community. Each
distribution has its own community support mechanisms. Consult the distribution's website to
find their community resources. You can also get help from these PowerShell Community
resources.

Ubuntu interim releases
The documented steps to install PowerShell on Ubuntu might work on Ubuntu interim releases.
However, Microsoft only supports PowerShell on the Long Term Servicing (LTS) releases of
Ubuntu. Microsoft doesn't support interim releases       of Ubuntu.

Arch Linux
PowerShell is available from the Arch Linux      User Repository (AUR). Packages in the AUR are
maintained by the Arch community. To install the latest release binary       , see the Arch Linux
wiki    or Using PowerShell in Docker.

Kali
Installation - Kali

 sh

 # Install PowerShell package
 apt update && apt -y install powershell

<!-- p.58 -->

 # Start PowerShell
 pwsh

Uninstallation - Kali

 sh

 # Uninstall PowerShell package
 apt -y remove powershell

Gentoo
You can install PowerShell on Gentoo Linux using packages from the Gentoo package repository.
For information about installing these packages, see the PowerShell   page in the Gentoo wiki.

SLES and openSUSE
You may be able to install PowerShell on SLES and openSUSE using the Snap package manager.
Also, the following article provides information on how to install PowerShell on openSUSE:

      PowerShell - openSUSE Wiki

Raspberry Pi OS
Raspberry Pi OS    is a free operating system based on Debian.

  ） Important

  .NET isn't supported on ARMv6 architecture devices, including Raspberry Pi Zero and
  Raspberry Pi devices released before Raspberry Pi 2.

Install on Raspberry Pi OS
Being Debian-based, you can install PowerShell on Raspberry Pi OS using the Snap package. For
more information, see the Snap installation instructions.

Or you can install PowerShell on Raspberry Pi OS using the binary archives. Download the tar.gz
package from the releases page onto your Raspberry Pi computer. The links to the current
versions are:

<!-- p.59 -->

      PowerShell 7.6 - latest LTS release
         https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-

        linux-arm32.tar.gz

         https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-

        linux-arm64.tar.gz

      PowerShell 7.5 - latest stable release
         https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell-7.5.9-

        linux-arm32.tar.gz

         https://github.com/PowerShell/PowerShell/releases/download/v7.5.9/powershell-7.5.9-

        linux-arm64.tar.gz

      PowerShell 7.4 - previous LTS release
         https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell-

        7.4.18-linux-arm32.tar.gz

         https://github.com/PowerShell/PowerShell/releases/download/v7.4.18/powershell-

        7.4.18-linux-arm64.tar.gz

Use the following shell commands to download and install the package. This script detects
whether you're running a 32-bit or 64-bit OS and installs the latest stable version of PowerShell
for that processor type.

 sh

 ###################################
 # Prerequisites

 # Update package lists
 sudo apt-get update

 # Install dependencies
 sudo apt-get install jq libssl1.1 libunwind8 -y

 ###################################
 # Download and extract PowerShell

 # Grab the latest tar.gz
 bits=$(getconf LONG_BIT)
 release=$(curl -sL https://api.github.com/repos/PowerShell/PowerShell/releases/latest)
 package=$(echo -E $release | jq -r ".assets[].browser_download_url" | grep "linux-
 arm${bits}.tar.gz")
 wget $package

 # Make folder to put powershell
 mkdir ~/powershell

 # Unpack the tar.gz file
 tar -xvf "./${package##*/}" -C ~/powershell

<!-- p.60 -->

  # Start PowerShell
  ~/powershell/pwsh

Optionally, you can create a symbolic link to start PowerShell without specifying the path to the
pwsh binary.

  sh

  # Start PowerShell from bash with sudo to create a symbolic link
  sudo ~/powershell/pwsh -Command 'New-Item -ItemType SymbolicLink -Path "/usr/bin/pwsh"
  -Target "$PSHOME/pwsh" -Force'

  # alternatively you can run following to create a symbolic link
  # sudo ln -s ~/powershell/pwsh /usr/bin/pwsh

  # Now to start PowerShell you can just run "pwsh"

Uninstallation - Raspberry Pi OS

  sh

  rm -rf ~/powershell

 Last updated on 07/20/2026

<!-- p.61 -->

Install PowerShell 7 on macOS
There are multiple package versions of PowerShell 7 that can be installed. This article focuses on
installing the latest stable release package. For more information about the package versions, see
the PowerShell Support Lifecycle article.

Newer versions of PowerShell 7 replace existing previous versions of PowerShell 7. Preview
versions of PowerShell can be installed side-by-side with other versions of PowerShell. Newer
preview versions replace existing previous preview versions. If you need to run PowerShell 7.5
side-by-side with a previous version, reinstall the previous version using the binary archive
method.

Choose an installation method
There are several ways to install PowerShell on macOS. If you previously installed PowerShell
using Homebrew, see Install on macOS using Homebrew in Alternate ways to install PowerShell.

Manually download and install the package
Download the install package from the releases     page. Select the package version you want to
install.

      PowerShell 7.6 (LTS)
           Arm64 processors - powershell-7.6.4-osx-arm64.pkg
           x64 processors - powershell-7.6.4-osx-x64.pkg
      PowerShell 7.5
           Arm64 processors - powershell-7.5.9-osx-arm64.pkg
           x64 processors - powershell-7.5.9-osx-x64.pkg
      PowerShell 7.4 (LTS)
           Arm64 processors - powershell-7.4.18-osx-arm64.pkg
           x64 processors - powershell-7.4.18-osx-x64.pkg

There are two ways to install PowerShell using the downloaded package.

Beginning with the May 2026 releases of PowerShell, the macOS PKG package is notarized and
signed by Microsoft. To install the package, download the PKG file and open it.

<!-- p.62 -->

For previous versions of PowerShell, use the following instructions to bypass the Gatekeeper
checks and install the package.

Install the package using Finder

Install PowerShell using Finder:

   1. Open Finder

   2. Locate the downloaded package

   3. Double-click the file

     You will receive the following error message when installing the package:

       "powershell-7.5.6-osx-arm64.pkg" Not Opened

       Apple could not verify "powershell-7.5.6-osx-arm64.pkg" is free from malware that may
       harm your Mac or compromise your privacy.

   4. Select the Done button to close the prompt.

This error message comes from the Gatekeeper feature of macOS. For more information, see
Safely open apps on your Mac - Apple Support      .

After you've tried to open the package, follow these steps:

   1. Open System Settings.
   2. Select Privacy & Security and scroll down to the Security section.
   3. Select the Open Anyway button to confirm your intent to install PowerShell.
   4. When the warning prompt reappears, select Open Anyway.
   5. Enter username and password to allow the installation to proceed.

Install the package from a command shell

To install the PowerShell package from the command line, you must bypass the Gatekeeper
checks. Use one of the following methods to install the package:

     Run the installer command with the allowUntrusted flag:

       sh

<!-- p.63 -->

       sudo installer -allowUntrusted -pkg ./Downloads/powershell-7.5.6-osx-arm64.pkg -
       target /

      Or install the package as you normally would after running one of the following commands:
        Run sudo xattr -rd com.apple.quarantine ./Downloads/powershell-7.5.6-osx-arm64.pkg .
        Use the Unblock-File cmdlet if you're using PowerShell. Include the full path to the .pkg
        file.

Install as a .NET Global tool
If you already have the .NET Core SDK installed, you can use the .NET Global tool to install
PowerShell 7.

 sh

 dotnet tool install --global PowerShell

The dotnet tool installer adds ~/.dotnet/tools to your PATH environment variable. However, the
currently running shell doesn't have the updated PATH . Start PowerShell from a new shell by
typing pwsh .

Install PowerShell 7 from a binary archive
PowerShell binary tar.gz archives are provided for the macOS platform to enable advanced
deployment scenarios. When you install using this method, you must also manually install any
dependencies.

Download the install package from the releases     page onto your Mac. Select the archive version
you want to install.

      PowerShell 7.6 (LTS)
        Arm64 processors - powershell-7.6.4-osx-arm64.tar.gz
        x64 processors - powershell-7.6.4-osx-x64.tar.gz
      PowerShell 7.5
        Arm64 processors - powershell-7.5.9-osx-arm64.tar.gz
        x64 processors - powershell-7.5.9-osx-x64.tar.gz
      PowerShell 7.4 (LTS)
        Arm64 processors - powershell-7.4.18-osx-arm64.tar.gz
        x64 processors - powershell-7.4.18-osx-x64.tar.gz

<!-- p.64 -->

Use the following commands to install PowerShell from the binary archive. Change the download
URL to match the version you want to install.

 sh

 # Download the powershell '.tar.gz' archive
 curl -L -o /tmp/powershell.tar.gz
 https://github.com/PowerShell/PowerShell/releases/download/v7.6.4/powershell-7.6.4-
 osx-arm64.tar.gz

 # Create the target folder where powershell is placed
 sudo mkdir -p /usr/local/microsoft/powershell/7

 # Expand powershell to the target folder
 sudo tar zxf /tmp/powershell.tar.gz -C /usr/local/microsoft/powershell/7

 # Set execute permissions
 sudo chmod +x /usr/local/microsoft/powershell/7/pwsh

 # Create the symbolic link that points to pwsh
 sudo ln -s /usr/local/microsoft/powershell/7/pwsh /usr/local/bin/pwsh

Start PowerShell 7
After the package is installed, run pwsh from a terminal. If you have installed a Preview package,
run pwsh-preview .

      The location of $PSHOME varies based on the package you installed.
        For Stable and LTS packages: /usr/local/microsoft/powershell/7/
        For Preview packages: /usr/local/microsoft/powershell/7-preview/
        The macOS install package creates a symbolic link, /usr/local/bin/pwsh that points to
         pwsh in the $PSHOME location.

      User profiles are read from ~/.config/powershell/profile.ps1
      Default profiles are read from $PSHOME/profile.ps1
      User modules are read from ~/.local/share/powershell/Modules
      Shared modules are read from /usr/local/share/powershell/Modules
      Default modules are read from $PSHOME/Modules
      PSReadLine history is recorded to
      ~/.local/share/powershell/PSReadLine/ConsoleHost_history.txt

PowerShell respects the XDG Base Directory Specification     on macOS.

Update PowerShell 7

<!-- p.65 -->

To update PowerShell, download the new version of the package or binary archive and install it.

Uninstall PowerShell 7
To uninstall PowerShell you need to delete the application folder and other support files. The
following command removes the symbolic link and PowerShell files.

  sh

  sudo rm -rf /usr/local/bin/pwsh /usr/local/microsoft/powershell

Use sudo rm to remove any other remaining PowerShell files and folders.

Supported versions of macOS
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of macOS
reaches end-of-support.

The following versions of macOS are supported:

       macOS 26 (Tahoe) x64 and Arm64
       macOS 15 (Sequoia) x64 and Arm64
       macOS 14 (Sonoma) x64 and Arm64

Apple determines the support lifecycle of macOS. For more information, see the following:

       macOS release notes
       Apple Security Updates

Supported installation methods
Microsoft supports the installation methods in this document. There may be other third-party
methods of installation available from other sources. While those tools and methods may work,
Microsoft can't support those methods. For more information, see Alternate ways to install
PowerShell.

 Last updated on 07/20/2026

<!-- p.66 -->

Alternate ways to install PowerShell
There are other ways to install PowerShell on non-Windows platforms.

These methods may work but aren't officially supported by Microsoft. You may be able to get
support from the PowerShell Community or the operating system vendor. For support options,
see Community Support.

Install on macOS using Homebrew
Homebrew is a popular package manager for macOS. To install Homebrew, follow the
instructions on the Homebrew website       .

  ） Important

  The brew formula is maintained and supported by the Homebrew community. The brew
  formula builds PowerShell from source code rather than installing a package built by
  Microsoft.

  If you previously installed PowerShell using the Homebrew cask, you must first uninstall the
  cask before you can successfully install using the Homebrew formula. Use the following
  commands to uninstall the cask:

      sh

      # Uninstall the PowerShell cask instance
      brew uninstall --cask powershell
      # Uninstall the PowerShell Preview cask instance
      brew uninstall --cask powershell-preview

Run the following command to install PowerShell using the Homebrew formula:

 sh

 brew install powershell

If you receive the message: "Warning: PowerShell is already installed, it's just not linked.", run the
following command:

<!-- p.67 -->

 sh

 brew link powershell

Update PowerShell 7
Run the following commands to update the installed version of PowerShell to the latest release.

 sh

 brew update
 brew upgrade powershell

Uninstall PowerShell 7
If you installed PowerShell with Homebrew, use the following command to uninstall:

 sh

 brew uninstall powershell

If you manually installed PowerShell 7, you must manually remove it. The following command
removes the symbolic link and PowerShell files.

 sh

 sudo rm -rf /usr/local/bin/pwsh /usr/local/microsoft/powershell

Use sudo rm to remove any other remaining PowerShell files and folders.

Install on Linux using a Snap package
Snaps are application packages that are easy to install if your platform supports Snap. You can
find and install Snap packages from the Snap Store.

  ７ Note

  The Snap Store contains PowerShell snap packages for many Linux distributions that aren't
  officially supported by Microsoft.

Getting snapd

<!-- p.68 -->

The snap daemon, known as snapd , is the background service that manages and maintains your
snaps. It needs to be running before a snap can be installed. For instructions on how to install
snapd , see the Snapcraft documentation     .

Installation via Snap
There are two PowerShell for Linux is published to the Snap store     : powershell and powershell-
preview .

Use the following command to install the latest stable version of PowerShell:

 sh

 # Install PowerShell
 sudo snap install powershell --classic

 # Start PowerShell
 pwsh

If you don't specify the --channel parameter, Snap installs the latest stable version. To install the
latest LTS version, use the following method:

 sh

 # Install PowerShell
 sudo snap install powershell --channel=lts/stable --classic

 # Start PowerShell
 pwsh

To install a preview version, use the following method:

 sh

 # Install PowerShell
 sudo snap install powershell-preview --classic

 # Start PowerShell
 pwsh-preview

  ７ Note

  Microsoft only supports the latest/stable and lts/stable channels for the powershell
  package. Microsoft only supports the latest/stable channel for the powershell-preview

<!-- p.69 -->

     package. Do not install packages from the other channels.

After installation, Snap will automatically upgrade. You can trigger an upgrade using sudo snap
refresh powershell or sudo snap refresh powershell-preview .

     ） Important

     The Snap packages are maintained and supported by Canonical. Snap packages build
     PowerShell from source code rather than installing a package built by Microsoft.

Uninstall using Snap

 sh

 sudo snap remove powershell

or

 sh

 sudo snap remove powershell-preview

Install from binary archives
PowerShell binary tar.gz archives are provided for Linux platforms to enable advanced
deployment scenarios.

     ７ Note

     You can use this method to install any version of PowerShell including the latest:

          Stable release: https://aka.ms/powershell-release?tag=stable
          LTS release: https://aka.ms/powershell-release?tag=lts
          Preview release: https://aka.ms/powershell-release?tag=preview

Dependencies
PowerShell builds portable binaries for all supported Linux distributions. But, PowerShell and the
.NET runtime require different dependencies on different distributions.

<!-- p.70 -->

It's possible that when you install PowerShell, specific dependencies may not be installed, such as
when manually installing from the binary archives. The following list details Linux distributions
that are supported by Microsoft and have dependencies you may need to install. Check the Linux
distribution page for more information:

      Alpine
      Debian
      RHEL
      SLES
      Ubuntu

To deploy PowerShell binaries on Linux distributions that aren't officially supported, you need to
install the necessary dependencies for the target OS in separate steps.

  ） Important

  This method can be used to install PowerShell on any version of Linux, including
  distributions that are not officially supported by Microsoft. Be sure to install any necessary
  dependencies. For support, see the list of available Community Support options.

The following example shows the steps for installing the x64 binary archive. You must choose the
correct binary archive that matches the processor type for your platform.

      powershell-7.6.3-linux-arm32.tar.gz

      powershell-7.6.3-linux-arm64.tar.gz

      powershell-7.6.3-linux-x64.tar.gz

Use the following shell commands to download and install PowerShell from the tar.gz binary
archive. Change the URL to match the version of PowerShell you want to install.

 sh

 # Download the powershell '.tar.gz' archive
 curl -L -o /tmp/powershell.tar.gz
 https://github.com/PowerShell/PowerShell/releases/download/v7.6.3/powershell-7.6.3-
 linux-x64.tar.gz

 # Create the target folder where powershell will be placed
 sudo mkdir -p /opt/microsoft/powershell/7

 # Expand powershell to the target folder
 sudo tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7

<!-- p.71 -->

  # Set execute permissions
  sudo chmod +x /opt/microsoft/powershell/7/pwsh

  # Create the symbolic link that points to pwsh
  sudo ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh

Uninstalling binary archives

  sh

  sudo rm -rf /usr/bin/pwsh /opt/microsoft/powershell

Install as a .NET Global tool
If you already have the .NET Core SDK installed, it's easy to install PowerShell as a .NET Global
tool.

  sh

  dotnet tool install --global PowerShell

The dotnet tool installer adds ~/.dotnet/tools to your PATH environment variable. However, the
currently running shell doesn't have the updated PATH . You should be able to start PowerShell
from a new shell by typing pwsh .

The .NET team publishes Docker images containing the .NET SDK with PowerShell already
installed. You can find those images on the Microsoft Container Registry     .

 Last updated on 06/13/2026

<!-- p.72 -->

Install PowerShell 7 on Windows IoT and
Nano Server
This article describes how to install PowerShell 7 on Windows IoT and Nano Server.

Deploy on Windows 11 IoT
Windows 11 IoT Enterprise comes with Windows PowerShell, which is used to deploy PowerShell
7.

     PowerShell

     # Replace the placeholder information for the following variables:
     $deviceip = '<device ip address>'
     $zipfile = 'PowerShell-7.6.3-win-arm64.zip'
     $downloadfolder = 'U:\Users\Administrator\Downloads'
     # The download location is local to the device.
     # There should be enough space for the zip file and the unzipped contents.

     # Create PowerShell session to target device
     Set-Item -Path WSMan:\localhost\Client\TrustedHosts $deviceip
     $S = New-PSSession -ComputerName $deviceIp -Credential Administrator
     # Copy the ZIP package to the device
     Copy-Item $zipfile -Destination $downloadfolder -ToSession $S

     #Connect to the device and expand the archive
     Enter-PSSession $S
     Set-Location U:\Users\Administrator\Downloads
     Expand-Archive .\PowerShell-7.6.3-win-arm64.zip

     # Set up remoting to PowerShell 7
     Set-Location .\PowerShell-7.6.3-win-arm64
     # Be sure to use the -PowerShellHome parameter otherwise it tries to create a new
     # endpoint with Windows PowerShell 5.1
     .\Install-PowerShellRemoting.ps1 -PowerShellHome .

When you set up PowerShell Remoting you get an error message and are disconnected from the
device. PowerShell has to restart WinRM. Now you can connect to PowerShell 7 endpoint on
device.

     PowerShell

     # Be sure to use the -Configuration parameter. If you omit it, you connect to Windows
     PowerShell 5.1

<!-- p.73 -->

 Enter-PSSession -ComputerName $deviceIp -Credential Administrator -Configuration
 PowerShell.7.6.3

Windows 11 IoT Core adds Windows PowerShell when you include IOT_POWERSHELL feature. Use
Windows PowerShell to deploy PowerShell 7 using the same steps as Windows 11 IoT Enterprise.

To add the latest PowerShell in the shipping image, use the Import-PSCoreRelease        command
to include the package in the workarea and add the OPENSRC_POWERSHELL feature to your
image.

  ７ Note

  For ARM64 architecture, Windows PowerShell isn't added when you include
  IOT_POWERSHELL. So the zip based install doesn't work. You need to use Import-
  PSCoreRelease command to add it in the image.

Deploying on Nano Server
These instructions assume that the Nano Server is a "headless" OS that has a version of
PowerShell already running on it. For more information, see the Nano Server Image Builder
documentation.

PowerShell binaries can be deployed using two different methods.

   1. Offline - Mount the Nano Server VHD and unzip the contents of the zip file to your chosen
     location within the mounted image.
   2. Online - Transfer the zip file over a PowerShell Session and unzip it in your chosen location.

In both cases, you need the Windows x64 ZIP release package . Run the commands within an
"Administrator" instance of PowerShell.

Offline Deployment of PowerShell
   1. Use your favorite zip utility to unzip the package to a directory within the mounted Nano
     Server image.
   2. Unmount the image and boot it.
   3. Connect to the built-in instance of Windows PowerShell.

Online Deployment of PowerShell

<!-- p.74 -->

Deploy PowerShell to Nano Server using the following steps.

 PowerShell

 # Replace the placeholder information for the following variables:
 $ipaddr = '<Nano Server IP address>'
 $credential = Get-Credential # <An Administrator account on the system>
 $zipfile = 'PowerShell-7.6.3-win-x64.zip'
 # Connect to the built-in instance of Windows PowerShell
 $session = New-PSSession -ComputerName $ipaddr -Credential $credential
 # Copy the file to the Nano Server instance
 Copy-Item $zipfile C:\ -ToSession $session
 # Enter the interactive remote session
 Enter-PSSession $session
 # Extract the ZIP file
 Expand-Archive -Path C:\PowerShell-7.6.3-win-x64.zip -DestinationPath 'C:\Program
 Files\PowerShell 7'

Supported versions of Windows
Microsoft supports PowerShell until PowerShell reaches end-of-support or the version of
Windows reaches end-of-support.

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

You can check the version that you are using by running winver.exe .

Supported installation methods
Microsoft supports the installation methods in this document. There may be other third-party
methods of installation available from other sources. While those tools and methods may work,

<!-- p.75 -->

Microsoft can't support those methods.

  ７ Note

  The installation commands in this article are for the latest stable release of PowerShell. To
  install a different version of PowerShell, adjust the command to match the version you need.
  Open the Release tags page      on GitHub. Select the tag for the release version you want to
  install. The download links for every package are found in the Assets section of the release.
  The Assets section may be collapsed, so you may need to click to expand it.

Last updated on 06/13/2026

<!-- p.76 -->

PowerShell on Arm processors
ﾃ     Summarize this article for me

Support for the Arm processor is based on the support policy of the version of .NET that
PowerShell uses. While .NET supports many more operating systems and versions, PowerShell
support is limited to the versions that have been tested.

It may be possible to use Arm-based versions of PowerShell on other Linux distributions and
versions, but we don't officially support it.

PowerShell 7
Arm versions of PowerShell 7 can be installed on the following platforms:

                                                                                  ﾉ   Expand table

 OS                                         Architectures    Lifecycle

 Windows 11 Client Version 22000+           Arm64            Windows

 macOS                                      Arm64            macOS

 Raspberry Pi OS (Debian 12)                Arm32/Arm64      Raspberry Pi OS   and Debian

 Ubuntu 22.04                               Arm32/Arm64      Ubuntu

Support is based on the .NET 8.0 Supported OS Lifecycle Policy .

Installing PowerShell on Arm-based systems
For installation instructions, see the following articles:

Windows

      Windows 11 on Arm
      Windows 11 IoT

Linux - install from the binary archives

      Alternate ways to install PowerShell on Linux

macOS

      Installing PowerShell on macOS

<!-- p.77 -->

Raspberry Pi

     Raspberry Pi OS

Last updated on 03/12/2026

<!-- p.78 -->

Use PowerShell in Docker
ﾃ   Summarize this article for me

The .NET team publishes Docker images with PowerShell preinstalled. This article shows you
how to get started using PowerShell in the Docker container.

Find available images
These images require Docker 17.05 or newer. Also, you must be able to run Docker without
sudo or local administrative rights. For install instructions, see Docker's official

documentation .

The .NET team publishes several Docker images designed for different development scenarios.
Only the image for the .NET SDK contains PowerShell. For more information, see Official .NET
Docker images.

Use PowerShell in a container
The following command downloads the image containing the latest available stable versions of
the .NET SDK and PowerShell.

 Console

 docker pull mcr.microsoft.com/dotnet/sdk:9.0

Use the following command to start an interactive PowerShell session in the container.

 Console

 docker run -it mcr.microsoft.com/dotnet/sdk:9.0 pwsh

To download and run the latest Long Term Support (LTS) version of PowerShell, change the
image name to mcr.microsoft.com/dotnet/sdk:8.0 . When you use these image tags, Docker
downloads the appropriate image for your host operating system. If you want an image for a
specific operating system, you can specify the operating system in the image tag. See the
Microsoft Artifact Registry         for a list of available tags.

     For more information about tags, the Supported tag policy
     For more information about supported operating systems, see the Supported platforms
     policy

<!-- p.79 -->

Support lifecycle
The .NET support policy       defines how these images are supported. These images are provided
for development and testing purposes only. If you need a production-ready image, you should
build your own images. For more information about these Docker images, visit the dotnet-
docker     repository on GitHub.

The images previously published by the PowerShell team will be marked as deprecated in the
Microsoft Container Registry (MCR).

Telemetry
By default, PowerShell collects limited telemetry without personal data to help aid
development of future versions of PowerShell. To opt-out of sending telemetry, create an
environment variable called POWERSHELL_TELEMETRY_OPTOUT set to a value of 1 before starting
PowerShell from the installed location. The telemetry we collect falls under the Microsoft
Privacy Statement      .

 Last updated on 03/12/2026

<!-- p.80 -->

Microsoft Update for PowerShell FAQ
Beginning with PowerShell 7.2, when you install using the MSI package you have the option of
enabling Microsoft Update support for PowerShell.

General Information
What is the Microsoft Update feature in PowerShell?
The Microsoft Update feature of PowerShell allows you to get the latest PowerShell 7 updates in
your traditional Microsoft Update (MU) management flow, whether that's with Windows Update
for Business, WSUS, Microsoft Endpoint Configuration Manager, or the interactive MU dialog in
Settings. Microsoft Update and the related services enable you to deploy updates:

     On your schedule
     After testing for your environment
     At scale across your enterprise

How soon after release are updates advertised by
Microsoft Update?
When a new version of PowerShell is released, it can take up to two weeks for that version to
become available through Microsoft Update. Updates are delivered as optional software updates,
even if the update contains a security fix.

If you need to deploy the update before it becomes available in Microsoft Update, download the
update from the Releases     page on GitHub.

Why is the latest LTS version not marked as LTS?
We mark the earliest minor version LTS until it goes out of support. For example, both PowerShell
7.2 and 7.4 are LTS releases and have a year of overlapping support. PowerShell 7.2 was marked
as the latest LTS in MU until it reached end of support in November 2024.

Configuration
