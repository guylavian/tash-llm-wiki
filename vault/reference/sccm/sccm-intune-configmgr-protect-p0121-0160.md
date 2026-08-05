---
title: "Protect data and infrastructure documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0121-0160
family: sccm
documentKind: "doc"
abstract: "Endpoint Protection Client Help Article • 10/04/2022 Applies to: Configuration Manager (current branch) This version of Windows Defender or Endpoint Protection includes the following features to help protect your computer from threats: Windows Firewall integration. Endpoint Prot"
---

# Protect data and infrastructure documentation — pages 121-160

<!-- p.121 -->

Endpoint Protection Client Help
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This version of Windows Defender or Endpoint Protection includes the following
features to help protect your computer from threats:

      Windows Firewall integration. Endpoint Protection setup enables you to turn on
      or off Windows Firewall.
      Network Inspection System. This feature enhances real-time protection by
      inspecting network traffic to help proactively block exploitation of known network-
      based vulnerabilities.
      Protection engine. Real-time protection finds and stops malware from installing or
      running on your PC. The updated engine offers enhanced detection and cleanup
      capabilities with better performance.

Windows Defender comes as part of the operating system starting in Windows 10. On
earlier versions of Windows, your administrator can provide either Windows Defender or
Endpoint Protection using management software.

You can also find a list of frequently asked questions for Windows Defender and
Endpoint Protection. For help troubleshooting, see Troubleshooting Windows Defender
or Endpoint Protection client. For a list of new features, see What's new Windows
Defender client    .

Windows Firewall integration
Windows Firewall can help prevent attackers or malicious software from gaining access
to your computer through the Internet or a network. Now when you install Endpoint
Protection, the installation wizard verifies that Windows Firewall is turned on. If you have
intentionally turned off Windows Firewall, you can avoid turning it on by clearing a
check box. You can change your Windows Firewall settings at any time via the System
and Security settings in Control Panel.

Network Inspection System
Attackers are increasingly carrying out network-based attacks against exposed
vulnerabilities before software vendors can develop and distribute security updates.
Studies of vulnerabilities show that it can take a month or longer from the time of an

<!-- p.122 -->

initial attack report before a suitable security update is developed, tested, and released.
This gap in protection leaves many computers vulnerable to attacks and exploitation for
a substantial period of time. Network Inspection System works with real-time protection
to better protect you against network-based attacks by greatly reducing the timespan
between vulnerability disclosures and update deployment from weeks to a few hours.

Award-winning protection engine
Under the hood of Windows Defender or Endpoint Protection is its award-winning
protection engine that is updated regularly. The engine is backed by a team of
antimalware researchers from the Microsoft Malware Protection Center, providing
responses to the latest malware threats 24 hours a day.

Windows Defender settings
Windows Defender settings enable settings that help protect your PC from malicious
software. Your administrator might manage some Windows Defender settings for you.
You can manage others using the Windows Defender settings. We recommend you
enable Windows Defender settings to help protect your PC and data.

To view Windows Defender settings, search for Windows Defender on your PC. Open
Windows Defender and select Settings. Windows Defender settings include:

     Real-time protection - Find and stop malware from installing or running on your
     PC.
     Cloud-based Protection - Windows Defender sends info to Microsoft about
     potential security threats.
     Automatic sample submission - Allow Windows Defender to send samples of
     suspicious files to Microsoft to help improve malware detection.
     Exclusions - You can exlude specific files, folders, file extensions, or processes from
     Windows Defender scanning.
     Enhanced notification - Enables notifications that inform about the health of your
     PC. Even Off you will receive critical notifications.
     Windows Defender Offline - You can run Windows Defender Offline to help find
     and remove malicious software. This scan will restart your PC and will take about
     15 minutes.

See also

<!-- p.123 -->

Endpoint Protection client frequently asked questions
Troubleshooting Windows Defender or Endpoint Protection client

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.124 -->

Troubleshoot Windows Defender or
Endpoint Protection client
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you come across problems with Windows Defender or Endpoint Protection, use this
article to troubleshoot the following problems:

      Update Windows Defender or Endpoint Protection
      Starting Windows Defender or Endpoint Protection service
      Internet connection issues
      Detected threat can't be remediated

Update Windows Defender or Endpoint
Protection

Symptoms
Windows Defender or Endpoint Protection works automatically with Microsoft Update
to make sure that your virus and spyware definitions are kept up-to-date.

This section addresses common issues with automatic updates, including the following
situations:

      You see error messages indicating that updates have failed.

      When you check for updates, you receive an error message that the virus and
      spyware definition updates can't be checked, downloaded, or installed.

      Even though your device is connected to the internet, the updates fail.

      Updates aren't automatically installing as scheduled.

Causes
The most common causes for update issues are problems with internet connectivity. If
you know your device is connected to the internet because you can browse to other
Web sites, the issue might be caused by conflicts with your internet settings in Windows.

<!-- p.125 -->

Options to resolve

Step 1: Reset your internet settings
   1. Exit all open programs, including the web browser.

        ７ Note

        When you reset these internet settings, it may delete your browser temporary
        files, cookies, browsing history, and online passwords. It doesn't delete your
        favorites.

   2. Go to the Start menu, and open inetcpl.cpl .

   3. Switch to the Advanced tab.

   4. In the section to Reset Internet Explorer settings, select Reset, and then select
     Reset again to confirm.

   5. Select OK when the settings are reset.

   6. Try to update Windows Defender again.

If the issue persists, continue to the next step.

Step 2: Make sure that the date and time are set correctly on your
computer
If the error message contains the code 0x80072f8f, the problem is most likely caused by
an incorrect date or time setting on your computer. Go to the Start menu, select
Settings, select Time & language, and select Date & time.

Step 3: Rename the Software Distribution folder on your computer

   1. Stop the Windows Update service.

      a. Go to Start, and open services.msc.

      b. Select the Windows Update service. Go to the Action menu, and select Stop.

   2. Rename the SoftwareDistribution directory.

      a. Open a command prompt as an administrator.

<!-- p.126 -->

      b. Enter the following commands:

           Windows Command Prompt

           cd %windir%
           ren SoftwareDistribution SDTemp
           exit

   3. Restart the Windows Update service.

      a. Switch back to the Services window.

      b. Select the Windows Update service. Go to the Action menu, and select Start.

      c. Close the Services window.

Step 4: Reset the Microsoft antivirus update engine on your
computer

   1. Open a command prompt as an administrator.

   2. Enter the following commands:

        Windows Command Prompt

        cd \

        cd program files\windows defender

        MpCmdRun -RemoveDefinitions -all

        exit

   3. Restart the computer.

   4. Try to update Windows Defender again.

If the issue persists, continue to the next step.

Step 5: Manually install the definition updates
Manually download the latest updates .

Step 6: Contact Microsoft support

<!-- p.127 -->

If these steps didn't resolve the issue, contact Microsoft support. For more information,
see Support options and community resources.

Starting Windows Defender or Endpoint
Protection service

Symptom
You receive a message notifying you that Windows Defender or Endpoint Protection
isn't monitoring your computer because the program's service stopped. You should
restart it now.

Solution

Step 1: Restart your computer
Close all applications and restart your computer.

Step 2: Check the Windows service
   1. Go to Start, and open services.msc.

   2. Select the Windows Defender Antivirus Service.

   3. Make sure that the Startup Type is set to Automatic.

   4. Go to the Action menu and select Start.
      a. If this action isn't available, select Stop. Wait for the service to stop, and then
        select the Start action to restart the service.

Note any errors that may appear during this process. Contact Microsoft Support and
provide the error information.

Step 3: Remove any third-party security programs

  ７ Note

<!-- p.128 -->

  Some security applications don't uninstall completely. You may need to download
  and run a cleanup utility for your previous security application to completely
  remove it.

   1. Go to Start and open appwiz.cpl.

   2. In the list of installed programs, uninstall any third-party security programs.

   3. Restart your computer.

  Ｕ Caution

  When you remove security programs, your computer may be unprotected. If you
  have problems installing Windows Defender after you remove existing security
  programs, contact Microsoft Support       . Select the Security product family, and
  then the Windows Defender product.

Internet connection issues
For your computer to receive the latest updates from Windows Update, connect it to the
internet.

   1. Go to Start and open ncpa.cpl.

   2. Open the connection name to view the connection Status.

   3. If your computer is connected, the IPv4 connectivity and/or IPv6 connectivity
     status is Internet.

   4. If your computer doesn't appear to be connected, select the connection name, and
     select Diagnose this connection.

Close any open programs and restart your computer.

Detected threat can't be remediated
When Windows Defender or Endpoint Protection detects a potential threat, it tries to
mitigate the threat by quarantining or removing the threat. These threats can hide
inside a compressed archive ( .zip ) or in a network share.

Remove or scan the file

<!-- p.129 -->

     If the detected threat was in a compressed archive file, browse to the file. Delete
     the file, or manually scan it. Right-click the file and select Scan with Windows
     Defender. If Windows Defender detects additional threats in the file, it notifies you.
     Then you can choose an appropriate action.

     If the detected threat was in a network share, open the share, and manually scan it.
     Right-click the file and select Scan with Windows Defender. If Windows Defender
     detects additional threats in the network share, it notifies you. Then you can
     choose an appropriate action.

     If you're not sure of the file's origin, run a full scan on your computer. A full scan
     may take some time to complete.

See also
Endpoint Protection client frequently asked questions

Endpoint Protection client help

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.130 -->

Endpoint Protection client frequently asked
questions
Applies to: Configuration Manager (current branch)

This FAQ is for computer users whose IT administrator has deployed Windows Defender or
Endpoint Protection to their managed computer. The content here might not apply to other
antimalware software. Microsoft System Center Endpoint Protection manages Windows
Defender on Windows 10 or later. It can also deploy and manage the Endpoint Protection
client to computers before Windows 10. While Windows Defender is described in this article, its
information also applies to Endpoint Protection.

Why do I need antivirus and antispyware
software?
It's critical to make sure that your computer is running software that protects against malicious
software. Malicious software, which includes viruses, spyware, or other potentially unwanted
software can try to install itself on your computer anytime you connect to the Internet. It can
also infect your computer when you install a program using a CD, DVD, or other removable
media. Malicious software can also be programmed to run at unexpected times, not just when
it's installed.

Windows Defender or Endpoint Protection offers three ways to help keep malicious software
from infecting your computer:

      Using real-time protection - Real-time protection enables Windows Defender to monitor
      your computer all the time and alert you when malicious software, including viruses,
      spyware, or other potentially unwanted software attempts to install itself or run on your
      computer. Windows Defender then suspends the software and enables you to follow its
      recommendation on the software or take an alternative action.

      Scanning options - You can use Windows Defender to scan for potential threats, such as
      viruses, spyware, and other malicious software that might put your computer at risk. You
      can also use it to schedule scans on a regular basis and to remove malicious software that
      is detected during a scan.

      Microsoft Active Protection Service community - The online Microsoft Active Protection
      Service community helps you see how other people respond to software that hasn't yet
      been classified for risks. You can use this information to help you choose whether to allow
      this software on your computer. In turn, if you participate, your choices are added to the
      community ratings to help other people decide what to do.

<!-- p.131 -->

How can I tell if my computer is infected
with malicious software?
You might have some form of malicious software, including viruses, spyware, or other
potentially unwanted software, on your computer if:

     You notice new toolbars, links, or favorites that you didn't intentionally add to your Web
     browser.

     Your home page, mouse pointer, or search program changes unexpectedly.

     You type the address for a specific site, such as a search engine, but you're taken to a
     different Web site without notice.

     Files are automatically deleted from your computer.

     Your computer is used to attack other computers.

     You see pop-up ads, even if you're not on the Internet.

     Your computer suddenly starts running more slowly than it usually does. Not all computer
     performance problems are caused by malicious software, but malicious software,
     especially spyware, can cause a noticeable change.

There might be malicious software on your computer even if you don't see any symptoms. This
type of software can collect information about you and your computer without your
knowledge or consent. To help protect your privacy and your computer, you should run
Windows Defender or Endpoint Protection at all times.

How can I find the version of Windows
Defender?
To view the version of Windows Defender running on your computer, open Windows Defender
(click Start and then search for Windows Defender), click Settings, and scroll to the bottom of
the Windows Defender settings to find Version info.

What should I do if Windows Defender or
Endpoint Protection detects malicious
software on my computer?

<!-- p.132 -->

If Windows Defender detects malicious software or potentially unwanted software on your
computer (either when monitoring your computer using real-time protection or after running a
scan), it notifies you about the detected item by displaying a notification message in the
bottom right-hand corner of your screen.

The notification message includes a Clean computer button and a Show details link that lets
you view additional information about the detected item. Click the Show details link to open
the Potential threat details window to get additional information about the detected item. You
can now choose which action to apply to the item, or click Clean computer. If you need help
with determining which action to apply to the detected item, use the alert level that Windows
Defender assigned to the item as your guide (for more information see, Understanding alert
levels).

Alert levels help you choose how to respond to viruses, spyware, and other potentially
unwanted software. While Windows Defender will recommend that you remove all viruses and
spyware, not all software that is flagged is malicious or unwanted. The following information
can help you decide what to do if Windows Defender detects potentially unwanted software on
your computer.

Depending on the alert level, you can choose one of the following actions to apply to the
detected item:

      Remove - This action permanently deletes the software from your computer.

      Quarantine - This action quarantines the software so that it can't run. When Windows
      Defender quarantines software, it moves it to another location on your computer, and
      then prevents the software from running until you choose to restore it or remove it from
      your computer.

      Allow - This action adds the software to the Windows Defender allowed list and allows it
      to run on your computer. Windows Defender will stop alerting you to risks that the
      software might pose to your privacy or to your computer.

      If you choose Allow for an item, such as software, Windows Defender will stop alerting
      you to risks that the software might pose to your privacy or to your computer. Therefore,
      add software to the allowed list only if you trust the software and the software publisher.

How to remove potentially harmful
software
To remove all unwanted or potentially harmful items that Windows Defender detects quickly
and easily, use the Clean computer option.

<!-- p.133 -->

   1. When you see the notification message that displays in the Notification area after it
     detects potential threats, click Clean computer.

   2. Windows Defender removes the potential threat (or threats), and then notifies you when
     it's finished cleaning your computer.

   3. To learn more about the detected threats, click the History tab, and then select All
     detected items.

   4. If you don't see all the detected items, click View details. If you're prompted for an
     administrator password or confirmation, type the password or confirm the action.

  ７ Note

  During computer cleanup, whenever possible, Windows Defender removes only the
  infected part of a file, not the entire file.

What is a virus?
Computer viruses are software programs deliberately designed to interfere with computer
operation, to record, corrupt, or delete data, or to infect other computers throughout the
Internet. Viruses often slow things down and cause other problems in the process.

What is spyware?
Spyware is software that can install itself or run on your computer without getting your consent
or providing you with adequate notice or control. Spyware might not display symptoms after it
infects your computer, but many malicious or unwanted programs can affect how your
computer runs. For example, spyware can monitor your online behavior or collect information
about you (including information that can identify you or other sensitive information), change
settings on your computer, or cause your computer to run slowly.

What's the difference between viruses,
spyware, and other potentially harmful
software?
Both viruses and spyware are installed on your computer without your knowledge and both
have the potential to be intrusive and destructive. They also have the ability to capture

<!-- p.134 -->

information on your computer and damage or delete that information. They both can
negatively affect your computer's performance.

The main difference between viruses and spyware is how they behave on your computer.
Viruses, like living organisms, want to infect a computer, replicate, and then spread to as many
other computers as possible. Spyware, however, is more like a mole - it wants to "move into"
your computer and stay there as long as possible, sending valuable information about your
computer to an outside source while it's there.

Where do viruses, spyware, and other
potentially unwanted software come from?
Unwanted software, such as viruses, can be installed by Web sites or by programs that you
download or that you install using a CD, DVD, external hard disk, or a device. Spyware is most
commonly installed through free software, such as file sharing, screen savers, or search
toolbars.

Can I get malicious software without
knowing it?
Yes, some malicious software can be installed from a website through an embedded script or
program in a webpage. Some malicious software requires your help to install it. This software
uses Web pop-ups or free software that requires you to accept a downloadable file. However, if
you keep Microsoft Windows® up to date and don't reduce your security settings, you can
minimize the chances of an infection.

Why is it important to review license
agreements before installing software?
When you visit websites, don't automatically agree to download anything the site offers. If you
download free software, such as file sharing programs or screen savers, read the license
agreement carefully. Look for clauses that say that you must accept advertising and pop-ups
from the company, or that the software will send certain information back to the software
publisher.

<!-- p.135 -->

Why doesn't Windows Defender detect
cookies?
Cookies are small text files that websites put on your computer to store information about you
and your preferences. Websites use cookies to offer you a personalized experience and to
gather information about website use. Windows Defender doesn't detect cookies because it
doesn't consider them a threat to your privacy or to the security of your computer. Most
internet browser programs allow you to block cookies.

How can I prevent malware?
Two of the biggest concerns for computer users today are viruses and spyware. In both cases,
while these can be a problem, you can defend yourself against them easily enough with just a
little bit of planning:

      Keep your computer's software current and remember to install all patches. Remember to
      update your operating system on a regular basis.

      Make sure your antivirus and antispyware software, Windows Defender, is using the latest
      updates again potential threats (see How do I keep virus and spyware definitions up to
      date?). Also make sure you're always using the latest version of Windows Defender.

      Only download updates from reputable sources. For Windows operating systems, always
      go to the Microsoft Update catalog    . For other software, always use the legitimate
      websites of the company or person who produces it.

      If you receive an e-mail with an attachment and you're unsure of the source, then you
      should delete it immediately. Don't download any applications or files from unknown
      sources, and be careful when trading files with other users.

      Install and use a firewall. It's recommended that you enable Windows Firewall.

What are virus and spyware definitions?
When you use Windows Defender or Endpoint Protection, it's important to have up-to-date
virus and spyware definitions. Definitions are files that act like an ever-growing encyclopedia of
potential software threats. Windows Defender or Endpoint Protection uses definitions to
determine if software that it detects is a virus, spyware, or other potentially unwanted software,
and then to alert you to potential risks. To help keep your definitions up to date, Windows
Defender or Endpoint Protection works with Microsoft Update to install new definitions

<!-- p.136 -->

automatically as they're released. You can also set Windows Defender or Endpoint Protection
to check online for updated definitions before scanning.

How do I keep virus and spyware
definitions up to date?
Virus and spyware definitions are files that act like an encyclopedia of known malicious
software, including viruses, spyware, and other potentially unwanted software. Because
malicious software is continually being developed, Windows Defender or Endpoint Protection
relies on up-to-date definitions to determine if software that is trying to install, run, or change
settings on your computer is a virus, spyware, or other potentially unwanted software.

To automatically check for new definitions before scheduled
scans (recommended)
   1. Open Windows Defender or Endpoint Protection client by clicking the icon in the
     notification area or launching it from the Start menu.

   2. Click Settings, and then click Scheduled scan.

   3. Make sure the Check for the latest virus and spyware definitions before running a
     scheduled scan check box is selected, and then click Save changes. If you're prompted
     for an administrator password or confirmation, type the password or confirm the action.

To check for new definitions manually
Windows Defender or Endpoint Protection updates the virus and spyware definitions on your
computer automatically. If the definitions haven't been updated for over seven days (for
example, if you didn't turn on your computer for a week), Windows Defender or Endpoint
Protection will notify you that the definitions are out of date.

   1. Open Windows Defender or Endpoint Protection client by clicking the icon in the
     notification area or launching it from the Start menu.

   2. To check for new definitions manually, click the Update tab and then click Update
     definitions.

How do I remove or restore items
quarantined by Windows Defender or

<!-- p.137 -->

Endpoint Protection?
When Windows Defender or Endpoint Protection quarantines software, it moves the software
to another location on your computer, and then it prevents the software from running until you
choose to restore it or to remove it from your computer.

For all the steps mentioned in this procedure, if you're prompted for an administrator
password or confirmation, type the password or provide confirmation.

To remove or restore items quarantined by Windows
Defender or Endpoint Protection
   1. Click the History tab, select Quarantined items, and then select the Quarantined items
     option.

   2. Click View details to see all of the items.

   3. Review each item, and then for each, click Remove or Restore. If you want to remove of
     the all quarantined items from your computer, click Remove All.

What is real-time protection?
Real-time protection enables Windows Defender to monitor your computer all the time and
alert you when potential threats, such as viruses and spyware, are trying to install themselves or
run on your computer. Because this feature is an important element of the way that Windows
Defender helps protect your computer, you should make sure real-time protection is always
turned on. If real-time protection gets turned off, Windows Defender notifies you, and changes
your computer's status to at risk.

Whenever real-time protection detects a threat or potential threat, Windows Defender displays
a notification. You can now choose from the following options:

     Click Clean computer to remove the detected item. Windows Defender will automatically
     remove the item from your computer.

     Click the Show details link to display the Potential threat details window, and then choose
     which action to apply to the detected item.

     You can choose the software and settings that you want Windows Defender to monitor,
     but we recommend that you turn on real-time protection and enable all real-time
     protection options. The following table explains the available options.

<!-- p.138 -->

                                                                                      ﾉ   Expand table

 Real-time            Purpose
 protection
 option

 Scan all             This option monitors files and programs that are downloaded, including files
 downloads            that are automatically downloaded via Windows Internet Explorer and
                      Microsoft Outlook® Express, such as ActiveX® controls and software
                      installation programs. These files can be downloaded, installed, or run by the
                      browser itself. Malicious software, including viruses, spyware, and other
                      potentially unwanted software, can be included with these files and installed
                      without your knowledge.

                      Using the real-time protection option, Windows Defender monitors your
                      computer all the time and checks for any malicious files or programs that you
                      may have downloaded. This monitoring feature means that Windows Defender
                      doesn't need to slow down your browsing or e-mail experience by requiring a
                      check of any files or programs you may want to download.

 Monitor file and     This option monitors when files and programs start running on your computer,
 program activity     and then it alerts you about any actions they perform and actions taken on
 on your              them. This is important, because malicious software can use vulnerabilities in
 computer             programs that you have installed to run malicious or unwanted software
                      without your knowledge. For example, spyware can run itself in the
                      background when you start a program that you frequently use. Windows
                      Defender monitors your programs and alerts you if it detects suspicious
                      activity.

 Enable behavior      This option monitors collections of behavior for suspicious patterns that might
 monitoring           not be detected by traditional antivirus detection methods.

 Enable Network       This option helps protect your computer against zero day exploits of known
 Inspection           vulnerabilities, decreasing the window of time between the moment a
 System               vulnerability is discovered and an update is applied.

To turn off real-time protection
  1. Click Settings, and then click Real-time protection.

  2. Clear the real-time protection options you want to turn off, and then click Save changes.
    If you're prompted for an administrator password or confirmation, type the password or
    confirm the action.

<!-- p.139 -->

How do I know that Windows Defender or
Endpoint Protection is running on my
computer?
After you install Windows Defender on your computer, you can close the main window and let
Windows Defender run quietly in the background. Windows Defender will continue running on
your computer, monitor it, and help protect it against threats.

Of course, you'll know that Windows Defender is running whenever it displays notification
messages in the notification area. These notifications alert you to potential threats that
Windows Defender has detected.

You'll also receive other alert notifications, for example, if for some reason real-time protection
has been turned off, if you haven't updated your virus and spyware definitions for a number of
days, or when upgrades to the program become available. Windows Defender also briefly
displays a notification to let you know that it's scanning your computer.

   Tip

  If you don't see the Windows Defender icon in the notification area, click the arrow in the
  notification area to show hidden icons, including the Windows Defender icon.

The icon color depends on your computer's current status:

     Green indicates that your computer's status is "protected."

     Yellow indicates that your computer's status is "potentially unprotected."

     Red indicates that your computer's status is "at risk."

Can you describe a little bit what
protected, potentially protected or at risk
means?
Depending whether Defender or another antivirus product is being used as primary provider,
the general states above represented by a color show the overall assessment of the security
state of the device. In case of security level being satisfactory, a green label will be provided.

<!-- p.140 -->

The "potentially unprotected" state is mostly due to settings - not directly impacting detection
- not being set to the recommended security level. For example, in Defender case, a quick scan
didn't run in a while, or cloud protection is turned off. In the case of another antivirus, those
states are reported via Security Center and could be in basically the following categories - a
scan is recommended, settings change is recommended or an update is recommended.

The "at risk" status represents serious security issues, such as a malware detection, software out
of date or antivirus not running at all. In the case of another Antivirus that could mean license
has expired.

How to set up Windows Defender or
Endpoint Protection alerts?
When Windows Defender is running on your computer, it automatically alerts you if it detects
viruses, spyware, or other potentially unwanted software. You can also set Windows Defender
to alert you if you run software that hasn't yet been analyzed, and you can choose to be alerted
when software makes changes to your computer.

To set up alerts
   1. Click Settings, and then click Real-time protection.

   2. Make sure the Turn on real-time protection (recommended) check box is selected.

   3. Select the check boxes next to the real-time protections options you want to run, and
     then click Save changes. If you're prompted for an administrator password or
     confirmation, type the password or confirm the action.

See also
Troubleshooting Windows Defender or Endpoint Protection client

Endpoint Protection Client Help

<!-- p.141 -->

Encrypt recovery data over the network
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you create a BitLocker management policy, Configuration Manager deploys the
recovery service to a management point. On the Client Management page of the
BitLocker management policy, when you Configure BitLocker Management Services,
the client backs up key recovery information to the site database. This information
includes BitLocker recovery keys, recovery packages, and TPM password hashes. When
users are locked out of their protected device, you can use this information to help them
recover access to the device.

Given the sensitive nature of this information, you need to protect it.

  ） Important

  Starting in version 2103, the implementation of the recovery service changed. It's
  no longer using legacy MBAM components, but is still conceptually referred to as
  the recovery service. All version 2103 clients use the message processing engine
  component of the management point as their recovery service. They escrow their
  recovery keys over the secure client notification channel. With this change, you can
  enable the Configuration Manager site for enhanced HTTP. This configuration
  doesn't affect the functionality of BitLocker management in Configuration
  Manager.

  When both the site and clients are running Configuration Manager version 2103 or
  later, clients send their recovery keys to the management point over the secure
  client notification channel. If any clients are on version 2010 or earlier, they need an
  HTTPS-enabled recovery service on the management point to escrow their keys.

HTTPS certificate requirements

  ７ Note

  These requirements only apply if the site is version 2010 or earlier, or if you deploy
  BitLocker management policies to devices with Configuration Manager client
  version 2010 or earlier.

<!-- p.142 -->

Configuration Manager requires a secure connection between the client and the
recovery service to encrypt the data in transit across the network. Use one of the
following options:

     HTTPS-enable the IIS website on the management point that hosts the recovery
     service, not the entire management point role.

     Configure the management point for HTTPS. On the properties of the
     management point, the Client connections setting must be HTTPS.

  ７ Note

  If your site has more than one management point, enable HTTPS on all
  management points at the site with which a BitLocker-managed client could
  potentially communicate. If the HTTPS management point is unavailable, the client
  could fail over to an HTTP management point, and then fail to escrow its recovery
  key.

  This recommendation applies to both options: enable the management point for
  HTTPS, or enable the IIS website that hosts the recovery service on the
  management point.

Configure the management point for HTTPS
In earlier versions of Configuration Manager current branch, to integrate the BitLocker
recovery service you had to HTTPS-enable a management point. The HTTPS connection
is necessary to encrypt the recovery keys across the network from the Configuration
Manager client to the management point. Configuring the management point and all
clients for HTTPS can be challenging for many customers.

HTTPS-enable the IIS website
The HTTPS requirement is now for the IIS website that hosts the recovery service, not
the entire management point role. This configuration relaxes the certificate
requirements, and still encrypts the recovery keys in transit.

The Client connections property of the management point can be HTTP or HTTPS. If
the management point is configured for HTTP, to support the BitLocker recovery
service:

   1. Acquire a server authentication certificate. Bind the certificate to the IIS website on
     the management point that hosts the BitLocker recovery service.

<!-- p.143 -->

   2. Configure clients to trust the server authentication certificate. There are two
      methods to accomplish this trust:

            Use a certificate from a public and globally trusted certificate provider.
            Windows clients include trusted root certificate authorities (CAs) from these
            providers. By using a server authentication certificate that's issued by one of
            these providers, your clients should automatically trust it.

            Use a certificate issued by a CA from your organization's public key
            infrastructure (PKI). Most PKI implementations add the trusted root CAs to
            Windows clients. For example, using Active Directory Certificate Services with
            group policy. If you issue the server authentication certificate from a CA that
            your clients don't automatically trust, add the CA trusted root certificate to
            clients.

   Tip

  The only clients that need to communicate with the recovery service are those
  clients that you plan to target with a BitLocker management policy and includes a
  Client Management rule.

Troubleshoot the connection
On the client, use the BitLockerManagementHandler.log to troubleshoot this
connection. For connectivity to the recovery service, the log shows the URL that the
client is using. Locate an entry in the log based on the version of Configuration
Manager:

      In version 2103 and later, the entry starts with Recovery keys escrowed to MP
      In version 2010 and earlier, the entry starts with Checking for Recovery Service at

Next steps
Encrypt recovery data in the database is an optional prerequisite before deploying
policy for the first time.

Deploy BitLocker management client

Feedback

<!-- p.144 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.145 -->

Encrypt recovery data in the database
06/12/2025

Applies to: Configuration Manager (current branch)

When you create a BitLocker management policy, Configuration Manager deploys the recovery
service to a management point. On the Client Management page of the BitLocker
management policy, when you Configure BitLocker Management Services, the client backs up
key recovery information to the site database. This information includes BitLocker recovery
keys, recovery packages, and TPM password hashes. When users are locked out of their
protected device, you can use this information to help them recover access to the device.

Given the sensitive nature of this information, you need to protect it. Configuration Manager
requires an HTTPS connection between the client and the recovery service to encrypt the data
in transit across the network. For more information, see Encrypt recovery data over the
network.

Consider also encrypting this data when stored in the site database. If you install a SQL Server
certificate, Configuration Manager encrypts your data in SQL.

If you don't want to create a BitLocker management encryption certificate, opt-in to plain-text
storage of the recovery data. When you create a BitLocker management policy, enable the
option to Allow recovery information to be stored in plain text.

  ７ Note

  Another layer of security is to encrypt the entire site database. If you enable encryption on
  the database, there aren't any functional issues in Configuration Manager.

  Encrypt with caution, especially in large-scale environments. Depending upon the tables
  you encrypt and the version of SQL, you might notice up to a 25% performance
  degradation. Update your backup and recovery plans, so that you can successfully recover
  the encrypted data.

  ７ Note

  Configuration Manager never removes or deletes recovery information for devices from
  the database, even if the client is inactive or deleted. This behavior is for security reasons.
  It helps with scenarios where a device is stolen but later recovered. For large
  environments, the impact to the database size is about 9 KB of data per encrypted
  volume.

<!-- p.146 -->

SQL Server encryption certificate
Use this SQL Server certificate for Configuration Manager to encrypt BitLocker recovery data in
the site database. You can create a self-signed certificate using a script in SQL Server.

Alternatively, you can use your own process to create and deploy this certificate, as long as it
meets the following requirements:

     The name of the BitLocker management encryption certificate must be
      BitLockerManagement_CERT .

     Encrypt this certificate with a database master key.

     The following SQL Server users need Control permissions on the certificate:
        RecoveryAndHardwareCore
        RecoveryAndHardwareRead
        RecoveryAndHardwareWrite

     Deploy the same certificate at every site database in your hierarchy.

     Create the certificate with the latest version of SQL Server.

        ） Important
           Certificates created with SQL Server 2016 or later are compatible with SQL Server
           2014 or earlier.
           Certificates created with SQL Server 2014 or earlier aren't compatible with SQL
           Server 2016 or later.

Manage the encryption certificate on SQL Server upgrade
If your site database is on SQL Server 2014 or earlier, before you upgrade SQL Server to version
2016 or later, use the following procedure to rotate the certificate to a supported version.

   1. On an instance of SQL Server running the latest available version, at least version 2016:

      a. Create a new certificate

      b. Back up the new certificate

   2. On the SQL Server instance with the encrypted site database that you plan to upgrade:

      a. Move the existing certificate on the site database server SQL Server instance to
        another name.

<!-- p.147 -->

        b. Restore the new certificate.

        c. Rotate the new certificate in for the existing certificate. Use the provided SQL function
          [RecoveryAndHardwareCore].[RecryptKey]

  ） Important

  If you upgrade SQL Server before you rotate the certificate, contact Microsoft Support for
  assistance with a work around.

You can also use this process if your business requirements specify that you need to regularly
renew this certificate.

Example scripts
These SQL scripts are examples to create and deploy a BitLocker management encryption
certificate in the Configuration Manager site database.

Create certificate
This sample script does the following actions:

     Creates a certificate
     Sets the permissions
     Creates a database master key

Before you use this script in a production environment, change the following values:

     Site database name ( CM_ABC )
     Password to create the master key ( MyMasterKeyPassword )
     Certificate expiry date ( 20391022 )

  SQL

  USE CM_ABC
  IF NOT EXISTS (SELECT name FROM sys.symmetric_keys WHERE name =
  '##MS_DatabaseMasterKey##')
  BEGIN
      CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MyMasterKeyPassword'
  END

  IF NOT EXISTS (SELECT name from sys.certificates WHERE name =
  'BitLockerManagement_CERT')
  BEGIN

<!-- p.148 -->

      CREATE CERTIFICATE BitLockerManagement_CERT AUTHORIZATION
  RecoveryAndHardwareCore
      WITH SUBJECT = 'BitLocker Management',
      EXPIRY_DATE = '20391022'

      GRANT CONTROL ON CERTIFICATE ::BitLockerManagement_CERT TO
  RecoveryAndHardwareRead
      GRANT CONTROL ON CERTIFICATE ::BitLockerManagement_CERT TO
  RecoveryAndHardwareWrite
  END

  ７ Note

  SQL doesn't check or enforce the certificate expiration date when the certificate is used for
  database encryption as is the case here.

  If your business requirements specify that you regularly renew this certificate, use the
  same process to Manage the encryption certificate on SQL Server upgrade.

Back up certificate
This sample script backs up a certificate. When you save the certificate to a file, you can then
restore it to other site databases in the hierarchy.

Before you use this script in a production environment, change the following values:

     Site database name ( CM_ABC )
     File path and name ( C:\BitLockerManagement_CERT_KEY )
     Export key password ( MyExportKeyPassword )

  SQL

  USE CM_ABC
  BACKUP CERTIFICATE BitLockerManagement_CERT TO FILE =
  'C:\BitLockerManagement_CERT'
      WITH PRIVATE KEY ( FILE = 'C:\BitLockerManagement_CERT_KEY',
          ENCRYPTION BY PASSWORD = 'MyExportKeyPassword')

  ） Important

  Always back up the certificate. In case you need to recover the site database, you might
  need to restore the certificate to regain access to the recovery keys.

<!-- p.149 -->

  Store the exported certificate file and associated password in a secure location.

Restore certificate
This sample script restores a certificate from a file. Use this process to deploy a certificate that
you created on another site database.

Before you use this script in a production environment, change the following values:

     Site database name ( CM_ABC )
     Master key password ( MyMasterKeyPassword )
     File path and name ( C:\BitLockerManagement_CERT_KEY )
     Export key password ( MyExportKeyPassword )

  SQL

  USE CM_ABC
  IF NOT EXISTS (SELECT name FROM sys.symmetric_keys WHERE name =
  '##MS_DatabaseMasterKey##')
  BEGIN
      CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MyMasterKeyPassword'
  END

  IF NOT EXISTS (SELECT name from sys.certificates WHERE name =
  'BitLockerManagement_CERT')
  BEGIN

  CREATE CERTIFICATE BitLockerManagement_CERT AUTHORIZATION RecoveryAndHardwareCore
  FROM FILE = 'C:\BitLockerManagement_CERT'
      WITH PRIVATE KEY ( FILE = 'C:\BitLockerManagement_CERT_KEY',
          DECRYPTION BY PASSWORD = 'MyExportKeyPassword')

  GRANT CONTROL ON CERTIFICATE ::BitLockerManagement_CERT TO RecoveryAndHardwareRead
  GRANT CONTROL ON CERTIFICATE ::BitLockerManagement_CERT TO
  RecoveryAndHardwareWrite
  END

Verify certificate
Use this SQL script to verify that SQL Server successfully created the certificate with the
required permissions.

  SQL

  USE CM_ABC
  declare @count int

<!-- p.150 -->

  select @count = count(distinct u.name) from sys.database_principals u
  join sys.database_permissions p on p.grantee_principal_id = u.principal_id or
  p.grantor_principal_id = u.principal_id
  join sys.certificates c on c.certificate_id = p.major_id
  where u.name in('RecoveryAndHardwareCore', 'RecoveryAndHardwareRead',
  'RecoveryAndHardwareWrite') and
  c.name = 'BitLockerManagement_CERT' and p.permission_name like 'CONTROL'
  if(@count >= 3) select 1
  else select 0

If the certificate is valid, the script returns a value of 1 .

SQL AlwaysOn when BitLocker recovery data is
encrypted in the database
If using SQL AlwaysOn, see SQL AlwaysOn when BitLocker recovery data is encrypted in the
database for additional important and required steps and instructions.

Related articles
For more information on these SQL commands, see the following articles:

      SQL Server and database encryption keys.
      Create certificate.
      Backup certificate.
      Create master key.
      Backup master key.
      Grant certificate permissions.
      SQL AlwaysOn when BitLocker recovery data is encrypted in the database.

Next steps
      Deploy BitLocker management client.
      SQL AlwaysOn when BitLocker recovery data is encrypted in the database.

<!-- p.151 -->

Deploy BitLocker management
Article • 02/09/2023

Applies to: Configuration Manager (current branch)

BitLocker management in Configuration Manager includes the following components:

      BitLocker management agent: Configuration Manager enables this agent on a
      device when you create a policy and deploy it to a collection.

      Recovery service: The server component that receives BitLocker recovery data
      from clients. For more information, see Recovery service.

Before you create and deploy BitLocker management policies:

      Review the prerequisites

      If necessary, encrypt recovery keys in the site database

Create a policy
When you create and deploy this policy, the Configuration Manager client enables the
BitLocker management agent on the device.

  ７ Note

  To create a BitLocker management policy, you need the Full Administrator role in
  Configuration Manager.

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, expand Endpoint Protection, and select the BitLocker Management
      node.

   2. In the ribbon, select Create BitLocker Management Control Policy.

   3. On the General page, specify a name and optional description. Select the
      components to enable on clients with this policy:

            Operating System Drive: Manage whether the OS drive is encrypted

            Fixed Drive: Manage encryption for other data drives in a device

<!-- p.152 -->

       Removable Drive: Manage encryption for drives that you can remove from a
       device, like a USB key

       Client Management: Manage the key recovery service backup of BitLocker
       Drive Encryption recovery information

4. On the Setup page, configure the following global settings for BitLocker Drive
  Encryption:

    ７ Note

    Configuration Manager applies these settings when you enable BitLocker. If
    the drive is already encrypted or is in progress, any change to these policy
    settings doesn't change the drive encryption on the device.

    If you disable or don't configure these settings, BitLocker uses the default
    encryption method (AES 128-bit).

       For Windows 8.1 devices, enable the option for Drive encryption method
       and cipher strength. Then select the encryption method.

       For Windows 10 or later devices, enable the option for Drive encryption
       method and cipher strength (Windows 10 or later). Then individually select
       the encryption method for OS drives, fixed data drives, and removable data
       drives.

  For more information on these and other settings on this page, see Settings
  reference - Setup.

5. On the Operating System Drive page, specify the following settings:

       Operating System Drive Encryption Settings: If you enable this setting, the
       user has to protect the OS drive, and BitLocker encrypts the drive. If you
       disable it, the user can't protect the drive.

  On devices with a compatible TPM, two types of authentication methods can be
  used at startup to provide added protection for encrypted data. When the
  computer starts, it can use only the TPM for authentication, or it can also require
  the entry of a personal identification number (PIN). Configure the following
  settings:

       Select protector for operating system drive: Configure it to use a TPM and
       PIN, or just the TPM.

<!-- p.153 -->

       Configure minimum PIN length for startup: If you require a PIN, this value is
       the shortest length the user can specify. The user enters this PIN when the
       computer boots to unlock the drive. By default, the minimum PIN length is 4 .

  For more information on these and other settings on this page, see Settings
  reference - OS drive.

6. On the Fixed Drive page, specify the following settings:

       Fixed data drive encryption: If you enable this setting, BitLocker requires
       users to put all fixed data drives under protection. It then encrypts the data
       drives. When you enable this policy, either enable auto-unlock or the settings
       for Fixed data drive password policy.

       Configure auto-unlock for fixed data drive: Allow or require BitLocker to
       automatically unlock any encrypted data drive. To use auto-unlock, also
       require BitLocker to encrypt the OS drive.

  For more information on these and other settings on this page, see Settings
  reference - Fixed drive.

7. On the Removable Drive page, specify the following settings:

       Removable data drive encryption: When you enable this setting, and allow
       users to apply BitLocker protection, the Configuration Manager client saves
       recovery information about removable drives to the recovery service on the
       management point. This behavior allows users to recover the drive if they
       forget or lose the protector (password).

       Allow users to apply BitLocker protection on removable data drives: Users
       can turn on BitLocker protection for a removable drive.

       Removable data drive password policy: Use these settings to set the
       constraints for passwords to unlock BitLocker-protected removable drives.

  For more information on these and other settings on this page, see Settings
  reference - Removable drive.

8. On the Client Management page, specify the following settings:

    ） Important

<!-- p.154 -->

        For versions of Configuration Manager prior to 2103, if you don't have a
        management point with an HTTPS-enabled website, don't configure this
        setting. For more information, see Recovery service.

           Configure BitLocker Management Services: When you enable this setting,
           Configuration Manager automatically and silently backs up key recovery
           information in the site database. If you disable or don't configure this setting,
           Configuration Manager doesn't save key recovery information.

               Select BitLocker recovery information to store: Configure it to use a
               recovery password and key package, or just a recovery password.

               Allow recovery information to be stored in plain text: Without a BitLocker
               management encryption certificate, Configuration Manager stores the key
               recovery information in plain text. For more information, see Encrypt
               recovery data in the database.

     For more information on these and other settings on this page, see Settings
     reference - Client management.

   9. Complete the wizard.

To change the settings of an existing policy, choose it in the list, and select Properties.

When you create more than one policy, you can configure their relative priority. If you
deploy multiple policies to a client, it uses the priority value to determine its settings.

Starting in version 2006, you can use Windows PowerShell cmdlets for this task. For
more information, see New-CMBlmSetting.

Deploy a policy
   1. Choose an existing policy in the BitLocker Management node. In the ribbon, select
     Deploy.

   2. Select a device collection as the target of the deployment.

   3. If you want the device to potentially encrypt or decrypt its drives at any time, select
     the option to Allow remediation outside the maintenance window. If the
     collection has any maintenance windows, it still remediates this BitLocker policy.

   4. Configure a Simple or Custom schedule. The client evaluates its compliance based
     on the settings specified in the schedule.

<!-- p.155 -->

   5. Select OK to deploy the policy.

You can create multiple deployments of the same policy. To view additional information
about each deployment, select the policy in the BitLocker Management node, and then
in the details pane, switch to the Deployments tab. You can also use Windows
PowerShell cmdlets for this task. For more information, see New-CMSettingDeployment.

  ） Important

  If a remote desktop protocol (RDP) connection is active, the MBAM client doesn't
  start BitLocker Drive Encryption actions. Close all remote console connections and
  sign in to a console session with a domain user account. Then BitLocker Drive
  Encryption begins and the client uploads recovery keys and packages. If you sign in
  with a local user account, BitLocker Drive Encryption doesn't start.

  You can use RDP to remotely connect to the console session of the device with the
  /admin switch. For example: mstsc.exe /admin /v:<IP address of device>

  A console session is either when you're at the computer's physical console, or a
  remote connection that's the same as if you're at the computer's physical console.

Monitor
View basic compliance statistics about the policy deployment in the details pane of the
BitLocker Management node:

     Compliance count
     Failure count
     Non-compliance count

Switch to the Deployments tab to see compliance percentage and recommended
action. Select the deployment, then in the ribbon, select View Status. This action
switches the view to the Monitoring workspace, Deployments node. Similar to the
deployment of other configuration policy deployments, you can see more detailed
compliance status in this view.

To understand why clients are reporting not compliant with the BitLocker management
policy, see Non-compliance codes.

For more troubleshooting information, see Troubleshoot BitLocker.

Use the following logs to monitor and troubleshoot:

<!-- p.156 -->

Client logs
     MBAM event log: in the Windows Event Viewer, browse to Applications and
     Services > Microsoft > Windows > MBAM. For more information, see About
     BitLocker event logs and Client event logs.

     BitlockerManagementHandler.log and
     BitlockerManagement_GroupPolicyHandler.log in client logs path,
     %WINDIR%\CCM\Logs by default

Management point logs (recovery service)
     Recovery service event log: in the Windows Event Viewer, browse to Applications
     and Services > Microsoft > Windows > MBAM-Web. For more information, see
     About BitLocker event logs and Server event logs.

     Recovery service trace logs: <Default IIS Web Root>\Microsoft BitLocker
     Management Solution\Logs\Recovery And Hardware Service\trace*.etl

Migration considerations
If you currently use Microsoft BitLocker Administration and Monitoring (MBAM), you can
seamlessly migrate management to Configuration Manager. When you deploy BitLocker
management policies in Configuration Manager, clients automatically upload recovery
keys and packages to the Configuration Manager recovery service.

  ） Important

  When you migrate from stand-alone MBAM to Configuration Manager BitLocker
  management, if you require existing functionality of stand-alone MBAM, don't
  reuse stand-alone MBAM servers or components with Configuration Manager
  BitLocker management. If you reuse these servers, stand-alone MBAM will stop
  working when Configuration Manager BitLocker management installs its
  components on those servers. Don't run the MBAMWebSiteInstaller.ps1 script to
  set up the BitLocker portals on stand-alone MBAM servers. When you set up
  Configuration Manager BitLocker management, use separate servers.

Group policy

<!-- p.157 -->

   The BitLocker management settings are fully compatible with MBAM group policy
   settings. If devices receive both group policy settings and Configuration Manager
   policies, configure them to match.

     ７ Note

     If a group policy setting exists for standalone MBAM, it will override the
     equivalent setting attempted by Configuration Manager. Standalone MBAM
     uses domain group policy, while Configuration Manager sets local policies for
     BitLocker management. Domain policies will override the local Configuration
     Manager BitLocker management policies. If the standalone MBAM domain
     group policy doesn't match the Configuration Manager policy, Configuration
     Manager BitLocker management will fail. For example, if a domain group
     policy sets the standalone MBAM server for key recovery services,
     Configuration Manager BitLocker management can't set the same setting for
     the management point. This behavior causes clients to not report their
     recovery keys to the Configuration Manager BitLocker management key
     recovery service on the management point.

   Configuration Manager doesn't implement all MBAM group policy settings. If you
   configure more settings in group policy, the BitLocker management agent on
   Configuration Manager clients honors these settings.

     ） Important

     Don't set a group policy for a setting that Configuration Manager BitLocker
     management already specifies. Only set group policies for settings that don't
     currently exist in Configuration Manager BitLocker management.
     Configuration Manager version 2002 has feature parity with standalone
     MBAM. With Configuration Manager version 2002 and later, in most instances
     there should be no reason to set domain group policies to configure BitLocker
     policies. To prevent conflicts and problems, avoid use of group policies for
     BitLocker. Configure all settings through Configuration Manager BitLocker
     management policies.

TPM password hash
   Previous MBAM clients don't upload the TPM password hash to Configuration
   Manager. The client only uploads the TPM password hash once.

<!-- p.158 -->

     If you need to migrate this information to the Configuration Manager recovery
     service, clear the TPM on the device. After it restarts, it uploads the new TPM
     password hash to the recovery service.

  ７ Note

  Uploading of the TPM password hash mainly pertains to versions of Windows
  before Windows 10. Windows 10 or later by default doesn't save the TPM password
  hash, so these devices don't normally upload it. For more information, see About
  the TPM owner password.

Re-encryption
Configuration Manager doesn't re-encrypt drives that are already protected with
BitLocker Drive Encryption. If you deploy a BitLocker management policy that doesn't
match the drive's current protection, it reports as non-compliant. The drive is still
protected.

For example, you used MBAM to encrypt the drive with the AES-XTS 128 encryption
algorithm, but the Configuration Manager policy requires AES-XTS 256. The drive is
non-compliant with the policy, even though the drive is encrypted.

To work around this behavior, first disable BitLocker on the device. Then deploy a new
policy with the new settings.

Co-management and Intune
The Configuration Manager client handler for BitLocker is co-management aware. If the
device is co-managed, and you switch the Endpoint Protection workload to Intune, then
the Configuration Manager client ignores its BitLocker policy. The device gets Windows
encryption policy from Intune.

  ７ Note

  Switching encryption management authorities while maintaining the desired
  encryption algorithm doesn't require any additional actions on the client. However,
  if you switch encryption management authorities and the desired encryption
  algorithm also changes, you will need to plan for re-encryption.

For more information about managing BitLocker with Intune, see the following articles:

<!-- p.159 -->

     Use device encryption with Intune
     Troubleshoot BitLocker policies in Microsoft Intune

Next steps
About the BitLocker recovery service

Set up BitLocker reports and portals

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.160 -->

About the BitLocker recovery service
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in version 2103, the implementation of the recovery service changed. It's
  no longer using legacy MBAM components, but is still conceptually referred to as
  the recovery service. All version 2103 clients use the message processing engine
  component of the management point as their recovery service. They escrow their
  recovery keys over the secure client notification channel. With this change, you can
  enable the Configuration Manager site for enhanced HTTP. This configuration
  doesn't affect the functionality of BitLocker management in Configuration
  Manager.

  When both the site and clients are running Configuration Manager version 2103 or
  later, clients send their recovery keys to the management point over the secure
  client notification channel. If any clients are on version 2010 or earlier, they need an
  HTTPS-enabled recovery service on the management point to escrow their keys.

The BitLocker recovery service is a server component that receives BitLocker recovery
data from Configuration Manager clients. The site deploys the recovery service when
you create a BitLocker management policy. Configuration Manager automatically installs
the recovery service on each management point with an HTTPS-enabled website.

Configuration Manager stores the recovery information in the site database. Without a
BitLocker management encryption certificate, Configuration Manager stores the key
recovery information in plain text. For more information, see Encrypt recovery data in
the database.

Starting in version 2010, you can manage BitLocker policies and escrow recovery keys
over a cloud management gateway (CMG). When domain-joined clients communicate
via the CMG, they don't use the legacy recovery service, but the message processing
engine component of the management point. Microsoft Entra hybrid joined devices also
use the message processing engine.

Starting in version 2103, all supported clients use the message processing engine
component of the management point as the recovery service. This change reduces
dependencies on legacy MBAM components, and enables support for enhanced HTTP.
