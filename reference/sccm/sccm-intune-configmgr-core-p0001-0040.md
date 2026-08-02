---
title: "Core infrastructure documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Core infrastructure documentation Fundamental information about the Configuration Manager product, including site servers and clients. About core infrastructure ｅ OVERVIEW What is Configuration Manager? Microsoft Configuration Manager FAQ What's new Technical preview ｂ GET START"
---

# Core infrastructure documentation — pages 1-40

<!-- p.1 -->

Core infrastructure documentation
Fundamental information about the Configuration Manager product, including site servers and
clients.

  About core infrastructure

  ｅ OVERVIEW
  What is Configuration Manager?

  Microsoft Configuration Manager FAQ

  What's new

  Technical preview

  ｂ GET STARTED
  Use the console

  Use Software Center

  Use the docs

  Find help

  Get started

  Ｙ ARCHITECTURE
  Supported configurations

  Support for Windows 11

  Site prerequisites

  ｀ DEPLOY
  Updates and servicing

  Install in-console updates

  Deploy clients

<!-- p.2 -->

Migrate between hierarchies

Top tasks

ｃ HOW-TO GUIDE
Enable TLS 1.2

CMPivot

Example management point deployment in an untrusted domain

Overview of cloud management gateway (CMG)

Enhanced HTTP

ｉ REFERENCE
Log files

Ports

Client settings

Tools

<!-- p.3 -->

What is Configuration Manager?
Article • 06/19/2024

Applies to: Configuration Manager (current branch)

Configuration Manager is part of the Microsoft Intune family of products.

The Microsoft Intune family of products is an integrated solution for managing all of
your devices. Microsoft brings together Configuration Manager and Intune, without a
complex migration, and with simplified licensing. Continue to leverage your existing
Configuration Manager investments, while taking advantage of the power of the
Microsoft cloud at your own pace.

The following Microsoft management solutions are all now part of the Microsoft Intune
brand:

      Configuration Manager
      Intune
      Endpoint analytics
      Autopilot

For more information, see Microsoft Configuration Manager FAQ.

Introduction
Use Configuration Manager to help you with the following systems management
activities:

      Increase IT productivity and efficiency by reducing manual tasks and letting you
      focus on high-value projects.
      Maximize hardware and software investments.
      Empower user productivity by providing the right software at the right time.

Configuration Manager helps you deliver more effective IT services by enabling:

      Secure and scalable deployment of applications, software updates, and operating
      systems.
      Real-time actions on managed devices.
      Cloud-powered analytics and management for on-premises and internet-based
      devices.
      Compliance settings management.
      Comprehensive management of servers, desktops, and laptops.

<!-- p.4 -->

Configuration Manager extends and works alongside many Microsoft technologies and
solutions. For example, Configuration Manager integrates with:

     Microsoft Intune to co-manage a wide variety of mobile device platforms
     Microsoft Azure to host cloud services to extend your management services
     Windows Server Update Services (WSUS) to manage software updates
     Certificate Services
     Exchange Server and Exchange Online
     Group Policy
     DNS
     Windows Automated Deployment Kit (Windows ADK) and the User State Migration
     Tool (USMT)
     Windows Deployment Services (WDS)
     Remote Desktop and Remote Assistance

Configuration Manager also uses:

     Active Directory Domain Services and Microsoft Entra ID for security, service
     location, configuration, and to discover the users and devices that you want to
     manage.
     Microsoft SQL Server as a distributed change management database—and
     integrates with SQL Server Reporting Services (SSRS) to produce reports to
     monitor and track management activities.
     Site system roles that extend management functionality and use the web services
     of Internet Information Services (IIS).
     Delivery Optimization, Windows Low Extra Delay Background Transport (LEDBAT),
     Background Intelligent Transfer Service (BITS), BranchCache, and other peer
     caching technologies to help manage content on your networks and between
     devices.

To be successful with Configuration Manager in a production environment, thoroughly
plan and test the management features. Configuration Manager is a powerful
management application, with the potential to affect every computer in your
organization. When you deploy and manage Configuration Manager with careful
planning and consideration of your business requirements, Configuration Manager can
reduce your administrative overhead and total cost of ownership.

User interfaces

The Configuration Manager console

<!-- p.5 -->

After you install Configuration Manager, use the Configuration Manager console to
configure sites and clients, and to run and monitor management tasks. This console is
the main point of administration, and lets you manage multiple sites.

You can install the Configuration Manager console on additional computers, and restrict
access and limit what administrative users can see in the console by using Configuration
Manager role-based administration.

For more information, see Use the Configuration Manager console.

Software Center
Software Center is an application that's installed when you install the Configuration
Manager client on a Windows device. Users use Software Center to request and install
software that you deploy. Software Center lets users do the following actions:

     Browse for and install applications, software updates, and new OS versions
     View their software request history
     View device compliance against your organization's policies

You can also show custom tabs in Software Center to meet additional business
requirements.

For more information, see the Software Center user guide.

Next steps
Before you install Configuration Manager, familiarize yourself with the basic concepts
and terms:

     For a high-level technical overview of Configuration Manager, see Fundamentals of
     Configuration Manager.

When you're familiar with the basic concepts, use this documentation library to help you
successfully deploy and use Configuration Manager. Start with the following articles:

     Features and capabilities of Configuration Manager
     Choose a device management solution
     Evaluate Configuration Manager by building your own lab environment
     Find help for using Configuration Manager

Feedback

<!-- p.6 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.7 -->

Microsoft Configuration Manager FAQ
Applies to: Configuration Manager (current branch, technical preview branch)

Configuration Manager is part of the Microsoft Intune family of products. This article provides
answers to frequently asked questions.

What is the Microsoft Intune family
of products?
The Microsoft Intune family of products is an integrated solution for managing all of your
devices. Microsoft brings together Configuration Manager and Intune with simplified licensing.
Continue to use your existing Configuration Manager investments, while taking advantage of the
power of the Microsoft cloud at your own pace.

The following Microsoft management solutions are all now part of the Microsoft Intune brand:

     Configuration Manager
     Intune
     Endpoint analytics
     Windows Autopilot

What things change in Configuration Manager
and the Microsoft Intune family of products?
Aside from the name change, Configuration Manager still functions the same.

Most notably, the Start menu folder names changed for common components, such as the
Configuration Manager console and Software Center.

How do we refer to the product now?
     When referring to the entire solution that includes all components: Microsoft Intune family
     of products

     When referring to the on-premises component:
        On first reference, use the full brand name: Microsoft Configuration Manager

<!-- p.8 -->

         For general use: Configuration Manager
         For space-constrained use: ConfigMgr, only in instances where the general use name
         doesn't fit

Are there any licensing changes?
If you're licensed for Configuration Manager, then you're also licensed for Intune to co-manage
your Windows PCs. For more information, see the Product and licensing FAQ.

Why do I still see "System Center Configuration
Manager" some places?
It takes time to make changes across all products, services, and supporting materials like
documentation.

There are also some fundamental components that may never change. The main Windows service
on site servers is still SMS_Executive.

Next steps
Learn about the what's new in Configuration Manager incremental versions.

 Last updated on 01/29/2026

<!-- p.9 -->

Find help for using Configuration
Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

There are several resources that you can use to find help with Configuration Manager.
Whether you're just getting started or an experienced administrator, use the following
resources when you need assistance:

      Send a smile or file a frown with product feedback

      Search the product documentation

      Follow the Configuration Manager team blog

      Understand support options and community resources

For help with product accessibility, see Accessibility features.

To get support for co-management, tenant attach, and analytics features, see How to
get support in Microsoft Intune admin center.

Product feedback
From the Configuration Manager console, you can share feedback directly to the
Microsoft product group. In the upper right corner of the console, select the smiley face
icon. There are three types of feedback:

      Send a smile: Send feedback on what you liked.

<!-- p.10 -->

     Send a frown: Send feedback on what you didn't like, and how Microsoft can
     improve it.

     Send a suggestion: Open the Configuration Manager product feedback site to
     share your idea.

For more information, see Product feedback.

Product documentation
To access the most current product documentation, start at the library index.

For tips on searching, providing feedback, and more information about using the
product documentation, see How to use the docs.

Configuration Manager team blog
The engineering and partner teams use the Configuration Manager blog       to provide
you with technical information and other news about Configuration Manager and
related technologies. Our blog posts supplement the product documentation and
support information.

Support options and community resources
The following links provide information about support options and community
resources:

     Microsoft support

     Configuration Manager forums on Microsoft Q&A

     Configuration Manager Community: Configuration Manager (Current Branch)
     Survival Guide

Next steps
Product feedback

Accessibility features

How to use the docs

How to use the console

<!-- p.11 -->

Software Center user guide

How to get support in Microsoft Intune admin center

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.12 -->

Product feedback for Configuration
Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

From the Configuration Manager console, you can share feedback directly to the
Microsoft product group. In the upper right corner of the console, select the feedback
icon. There are three types of feedback:

      Send a smile (ALT + SHIFT + 7): Send feedback on what you liked.

      Send a frown (ALT + SHIFT + 8): Send feedback on what you didn't like, and how
      Microsoft can improve it.

      Send a suggestion (ALT + SHIFT + 9): Open the Configuration Manager product
      feedback website to share your idea. For more information, see Send a suggestion.

      Contact support (ALT + SHIFT + 0): Opens the Microsoft support for business
      portal   .

When using the feedback wizard from the console, the following items are displayed
where needed:

      A description of the feedback is required
      Select from a list of issue categories for the console workspace
      It includes tips for how to write useful feedback
      You can attach additional files
      A summary page displays your feedback ID, and includes any error messages with
      suggestions to resolve them.

<!-- p.13 -->

  ７ Note

  This wizard is in the Configuration Manager console. Support Center has a similar
  feedback experience.

Recent changes to feedback
Starting in version 2203, you have the ability to connect feedback you send to Microsoft
through the Configuration Manager console to an authenticated Microsoft Entra user
account or Microsoft Account (MSA). User authentication will help Microsoft ensure the
privacy of your feedback and diagnostic data. Currently, Microsoft Entra authentication
for government clouds isn't available. After selecting either Send a smile or Send a
frown:

   1. Select Sign in and sign in with either your Microsoft Entra user account or your
     Microsoft account.

           Selecting Continue without signing in will allow you to send feedback, but
           we won't be able to contact you with questions or updates unless you
           provide an e-mail address.

   2. Once you're signed in, select Next then provide your feedback. If you need to use
     a different account, you can select Sign out to start again.

Starting in version 2203, the feedback button is displayed in additional console
locations. You can also use the keyboard shortcuts for Send a smile and Send a frown
from more locations in the console.

Starting in Configuration Manager 2111, when you Report error to Microsoft the error
information included with the feedback can't be altered or removed. Wizards and some
property pages also include an icon to provide feedback allowing you to quickly send
feedback right from your current activity.

Starting in version 2107, error messages include a link to Report error to Microsoft. This
action opens the standard send a frown window to provide feedback. It automatically
includes details about the user interface and the error to better help Microsoft engineers
diagnose the error. Aside from making it easier to send a frown, it also includes the full
context of the error message when you share a screenshot.

Prerequisites

<!-- p.14 -->

Update the Configuration Manager console to the latest version.

On the computer where you run the console, allow it to access the following internet
endpoints to send diagnostic data to Microsoft:

     petrol.office.microsoft.com

     ceuswatcab01.blob.core.windows.net

     ceuswatcab02.blob.core.windows.net

     eaus2watcab01.blob.core.windows.net

     eaus2watcab02.blob.core.windows.net

     weus2watcab01.blob.core.windows.net

     weus2watcab02.blob.core.windows.net

     umwatsonc.events.data.microsoft.com

     *-umwatsonc.events.data.microsoft.com

Send a smile
To send feedback on something that you like about Configuration Manager:

   1. In the upper-right corner of the Configuration Manager console, select the
     feedback icon. Choose Send a smile.

   2. On the first page of the Provide feedback wizard:

          Tell us what you liked: Enter a detailed description of why you're filing this
          feedback.

          You can contact me about this feedback: To allow Microsoft to contact you
          about this feedback if necessary, select this option and specify a valid email
          address.

          Include screenshot: Select this option to add a screenshot. By default it uses
          the full screen, select Refresh to capture the latest image. Select Browse to
          select a different image file.

<!-- p.15 -->

                                                                                

3. Select Next to send the feedback. You may see a progress bar as it packages the
  content to send.

4. When the progress is complete, select Details to see the transaction ID or any
  errors that occurred.

                                                                                

<!-- p.16 -->

Send a frown
Before you file a frown, prepare your information:

     If you have multiple issues, send a separate report for each issue. Don't include
     multiple issues in a single report.

     Provide clear details on the issue. Share any research that you've gathered so far.
     More detailed information is better to help Microsoft investigate and diagnose the
     issue.

     Do you need immediate assistance? If so, contact Microsoft support for urgent
     issues. For more information, see Support options and community resources.

     Is this feedback a suggestion to improve the product? If so, share a new idea
     instead. For more information, see Send a suggestion.

     Is the issue with the product documentation? You can file feedback directly on the
     documentation. For more information, see Doc feedback.

To send feedback on something that you didn't like about the Configuration Manager
product:

   1. In the upper-right corner of the Configuration Manager console, select the
     feedback icon. Choose Send a frown.

   2. On the first page of the Provide feedback wizard:

           Issue category: Select a category that's most appropriate for your issue.

           Describe your issue with as much detail as possible.

           You can contact me about this feedback: To allow Microsoft to contact you
           about this feedback if necessary, select this option and specify a valid email
           address.

<!-- p.17 -->

                                                                                   

3. On the Add more details page of the wizard:

       Include screenshot: Select this option to add a screenshot. By default it uses
       the full screen, select Refresh to capture the latest image. Select Browse to
       select a different image file.

       Include additional files: Select Attach and add log files, which can help
       Microsoft better understand the issue. To remove all attached files from your
       feedback, select Clear all. To remove individual files, select the delete icon to
       the right of the file name.

<!-- p.18 -->

                                                                                   

   4. Select Next to send the feedback. You may see a progress bar as it packages the
     content to send.

   5. When the progress is complete, select Details to see the transaction ID or any
     errors that occurred.

If you don't have internet connectivity:

     The Provide feedback wizard still packages your feedback and files.

     The final summary page shows an error that it couldn't send the feedback.

     Select the option to Save a copy of feedback and attachments. For more
     information on how to send it to Microsoft, see Send feedback that you saved for
     later submission.

If the Provide feedback wizard successfully submits your feedback, but fails to send the
attached files, use the same instructions for no internet connectivity.

Send a suggestion
When you Send a suggestion, it opens the Feedback for Configuration Manager            site.

For more information, including the different status values, see How Microsoft uses
feedback.

<!-- p.19 -->

Status messages
When you Send a smile or Send a frown, it creates a status message when you submit
the feedback. This message provides a record of:

     When you submitted the feedback
     Who submitted it
     The feedback ID
     The message ID identifies if the feedback submission was successful:
        53900: Success
        53901: Failed

You can use the built-in status message query, Feedback sent to Microsoft to easily
display these status messages. You can also display status messages in the Monitoring
workspace, under System Status in the Status Message Queries node. Start with the All
Status Messages query and select your time frame. When the messages load, select
Filter messages, and filter for message ID 53900 or 53901. If you create feedback that
you save for later submission, the site doesn't create a status message.

Information sent with feedback
When you Send a smile or Send a frown, the feedback includes the following
information:

     OS build information

<!-- p.20 -->

     Configuration Manager support ID, also known as the hierarchy ID

     Product build information

     Language information

     Device identifier: HKLM\SOFTWARE\Microsoft\SQMClient:MachineId

Send feedback that you saved for later
submission
You can save your feedback locally and submit it later. Use this process if the current
computer doesn't have internet-access.

   1. At the bottom of the Provide feedback window, select Save a copy of feedback
     and attachments.

   2. Save the .zip file. If the local machine doesn't have internet access, copy the file to
     an internet-connected machine.

   3. If needed, copy the UploadOfflineFeedback folder from the site server located at
     cd.latest\SMSSETUP\Tools\UploadOfflineFeedback\ .

        ７ Note

        For more information about the cd.latest folder, see the CD.Latest folder.

   4. On an internet-connected machine, open a command prompt.

   5. Run the following command: UploadOfflineFeedback.exe -f
     c:\folder\location_of.zip

UploadOfflineFeedback tool usage
The UploadOfflineFeedback tool supports the following command-line parameters:

     -f , --file (Required): The path to the saved feedback file to send.

     -t , --timeout : Timeout in seconds for sending the data. 0 is unlimited. Default is
     30 .

     -s , --silent : Don't log any output to the command prompt. You can't combine

     this parameter with --verbose .

<!-- p.21 -->

     -v , --verbose : Log verbose output to the command prompt. You can't combine

     this parameter with --silent .
     --help : Display this usage information.
     --version : Display the tool version.

The UploadOfflineFeedback utility supports the use of a proxy server. You can specify
the following parameters:

     -x , --proxy : Specify the proxy server address.

     -o , --port : Specify the port for the proxy server.
     -u , --user : Specify the user name to authenticate to the proxy server.

     -w , --password : Specify the password for the specified user name. If you use an

     asterisk ( * ), the tool prompts for the password. The password isn't displayed in the
     prompt. This value is recommended. Including the password in plain text on the
     command line is less secure.
     -i , --SkipConnectionCheck : Skips the network connection check, and just starts to

     upload the feedback with the specified settings.

Confirmation of console feedback
When you send feedback, it shows a confirmation message. This message includes a
Feedback ID, which you can give to Microsoft as a tracking identifier.

     In the Provide feedback window from the console, it displays the feedback ID on
     the final page. To copy it, select the copy icon next to the ID, or use the CTRL + C
     key shortcut. This ID isn't stored on your computer, so make sure to copy it before
     you close the window.

     The status message includes the feedback ID.

     The UploadOfflineFeedback command tool writes the FeedbackID to the console
     unless you use --silent .

Feedback for Support Center
If you have feedback on Support Center, use the following instructions:

<!-- p.22 -->

   1. In the upper right corner of the application, select the smiley face.

   2. In the drop-down menu, select Send a smile or Send a frown.

           If you select Send a suggestion, you will be taken to the feedback portal. For
           more information, see Send a suggestion.

   3. Use the text box to explain what you liked or what you didn't like.

   4. Choose if you would like to share your e-mail address and a screenshot.

   5. Select Submit Feedback.

                                                                                    

Feedback for PowerShell
If you have feedback on the Configuration Manager PowerShell cmdlets, use the same
options in the Configuration Manager console to send feedback.

When you send a frown, include the following additional information specific to
PowerShell:

     The exact script or command syntax that you used so that Microsoft can try to
     reproduce the issue.

     What behavior you expected compared to the actual behavior.

<!-- p.23 -->

     The full output when you run it with the Verbose common parameter.

     The version and path of the ConfigurationManager module. For example, include
     the output of the following commands:

        PowerShell

        (Get-Module -Name ConfigurationManager).Version
        (Get-Module -Name ConfigurationManager).Path

     If a cmdlet returns an error, use the following command to get exception details:

        PowerShell

        $Error[0].Exception | Format-List * -Force

Next steps
How to use the docs

How to use the console

How to get support in Microsoft Intune admin center

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.24 -->

How to use Microsoft Intune
documentation
ﾃ     Summarize this article for me

This article provides resources and tips for using the Microsoft Intune product family
documentation library. It applies to Configuration Manager, Microsoft Intune, Endpoint
analytics, and Windows Autopilot, and covers the following areas:

      How to search
      Submitting doc bugs, enhancements, questions, and new ideas
      How to get notified of changes
      How to contribute to documentation on Microsoft Learn

For general help and support, see:

      Find help for Configuration Manager
      Get support in Microsoft Intune

     Tip

    Also visit the Documentation node in the Community workspace of the Configuration
    Manager console. This node includes up-to-date information about Configuration
    Manager documentation and support articles. For more information, see Using the
    Configuration Manager console.

Information in this article also applies to the Configuration Manager PowerShell
documentation in the sccm-docs-powershell-ref repository         .

Search
Use the following search tips to help you find the information that you need:

      When using your preferred search engine to locate content, include a keyword along with
      your search keywords. For example, ConfigMgr for Configuration Manager and Intune for
      Intune.

          Look for results from learn.microsoft.com/mem . Results from
            learn.microsoft.com/previous-versions , technet.microsoft.com , or

            msdn.microsoft.com are for older product versions.

<!-- p.25 -->

  To further focus the search results to the current content library, include
   site:learn.microsoft.com in your query to scope the search engine.

Use search terms that match terminology in the user interface and online documentation.
Avoid unofficial terms or abbreviations that you might see in community content. For
example, search for:
  "management point" rather than "MP"
  "deployment type" rather than "DT"
  "Intune management extension" rather than "IME"

To search within the current article, use your browser's Find feature. With most modern
web browsers, press Ctrl+F and then enter your search terms.

Each article on learn.microsoft.com includes the following fields to assist with searching
the content:

  Search in the upper right corner. To search all articles, enter terms in this field. Articles
  in this content library automatically include one of the following search scopes:
   ConfigMgr , Intune , or Autopilot .

  Filter by title above the left table of contents. To search the current table of contents,
  enter terms in this field. This field only matches terms that appear in the article titles
  for the current node. For example, Configuration Manager Core Infrastructure
  ( learn.microsoft.com/mem/configmgr/core ) or Intune Apps
  ( https://learn.microsoft.com/mem/intune/apps/ ). The last item in the search results
  gives you the option to search for the terms in the entire content library.

<!-- p.26 -->

Having problems finding something? File feedback! When you file an issue about search
results, provide the search engine you're using, the keywords you tried, and the target article.
This feedback helps Microsoft optimize the content for better search.

Add a custom search engine
With many modern web browsers, you can create a custom search engine. Use this feature to
quickly and easily search learn.microsoft.com . For example, with Microsoft Edge, version 77
and later, use the following process:

   1. In Microsoft Edge, version 77 and later, open Settings.

   2. In the left menu, select Privacy, search, and services.

   3. Scroll to the bottom of the Services group and select Address bar and search.

   4. Select Manage search engines.

   5. Select Add and specify the following information:

           Search engine: Enter a friendly name to identify it in the list of search engines. For
           example, Microsoft Learn .

           Keyword: Specify a short term to use in the address bar to activate this search
           engine. For example, memdocs .

           URL with %s in place of query: For example,

<!-- p.27 -->

            https

            https://learn.microsoft.com/search/index?search=%s&scope=ConfigMgr

             ７ Note

             This example is specific to the ConfigMgr scope. You can remove the scope
             variable to search all learn.microsoft.com or use a different scope.

             The Microsoft technical documentation search engine requires a locale in the
             address. For example, en-us . You can change your entry to use a different
             locale.

After you add this search engine, type your keyword in the browser address bar, press Tab ,
then type your search terms, and press Enter . It will automatically search Microsoft technical
documentation for your specified terms using the defined scope.

About feedback
Select the Feedback link in the upper right of any article or go to the Feedback section at the
bottom.

<!-- p.28 -->

Types of feedback
   Product feedback for Configuration Manager or Intune
   Product questions
   Support requests for Configuration Manager   or Microsoft Intune

Notifications

<!-- p.29 -->

To receive notifications when content changes in the documentation library, use the following
steps:

   1. Use the docs search to find an article or set of articles.

            Search for a single article by title, such as What's new in Microsoft Intune.

               Tip

              To refine the search to a single article, use the full title that displays in the
              Microsoft technical documentation search results. You can also use a string
              from the first paragraph, as shown in this example.

            This example results in the following RSS link:

             https

             https://learn.microsoft.com/api/search/rss?
             search=%22What%27s+new+in+microsoft+intune%22%2B%22learn+what%27s+new%22&l
             ocale=en-us&facet=&%24filter=scopes%2Fany%28t%3A+t+eq+%27Intune%27%29

              ７ Note

              The above RSS feed URL example includes the &locale=en-us variable. The
              locale variable is required, but you can change it to another supported locale.

              For example, &locale=ja-jp .

            Search for any Configuration Manager article about BitLocker

         ７ Note

         Use other keywords or the Microsoft Learn search filters to further refine your search
         query.

   2. At the bottom of the list of results, select the RSS link.

<!-- p.30 -->

   3. Use this feed in an RSS application to receive notifications when there's a change to any
     of the search results. Refer to the RSS application's documentation on how to configure
     and tune it.

   Tip

  You can also Watch the MEMDocs repository              on GitHub. This method can generate
  many notifications. It also doesn't include changes from the private repository that
  Microsoft uses.

Contribute
The Microsoft Intune product family documentation library, like most Microsoft technical
documentation, is open-sourced on GitHub. This library accepts and encourages community
contributions. For more information on how to get started, see our contributor guide. The only
prerequisite is to create a GitHub account     .

Basic steps to contribute
   1. From the target article, select Edit in the upper right corner. This action opens the source
     file in GitHub.

   2. To edit the source file, select the pencil icon.

   3. Make changes in the markdown source. For more information, see How to use Markdown
     in Microsoft Learn articles.

<!-- p.31 -->

   4. In the Propose file change section, enter the public commit comment describing what
      you changed. Then select Propose file change.

   5. Scroll down and verify the changes you made. Select Create pull request to open the
      form. Describe why you made this change. Select Create pull request.

The writing team receives your pull request, and assigns it to the appropriate writer. The author
reviews the text, and does a quick edit pass on it. They'll either approve and merge the
changes, or contact you for more information about the update.

What to contribute
If you want to contribute, but don't know where to start, see the following suggestions:

      Review an article for accuracy. Then update the ms.date metadata using mm/dd/yyyy
      format. This contribution helps keep the content fresh.

      Add clarifications, examples, or guidance based on your experience. This contribution
      uses the power of the community to share knowledge.

  ７ Note

  Large contributions require signing a Contribution License Agreement (CLA) if you aren't a
  Microsoft employee. GitHub automatically requires you to sign this agreement when a
  contribution meets the threshold. You only need to sign this agreement once.

Contribution tips
Follow these general guidelines when you contribute:

      Don't surprise us with large pull requests. Instead, file an issue and start a discussion.
      Then we can agree on a direction before you invest a large amount of time.

      Read the Microsoft style guide. Know the Top 10 tips for Microsoft style and voice.

      Follow the GitHub Flow workflow      .

      Blog and tweet (or whatever) about your contributions, frequently!

(This list was borrowed from the .NET contributing guide.)

 Last updated on 03/09/2026

<!-- p.32 -->

Accessibility features in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager includes features to help make it accessible for everyone.

  ７ Note

  To improve the accessibility features of the Configuration Manager console, update
  .NET to version 4.7 or later on the computer running the console.

  For more information on the accessibility changes made in .NET 4.7.1 and 4.7.2, see
  What's new in accessibility in the .NET Framework.

Keyboard shortcuts

Console workspaces
To access a workspace, use the following keyboard shortcuts:

                                                                       ﾉ   Expand table

 Keyboard shortcut                        Workspace

 Ctrl + 1                                 Assets and Compliance

 Ctrl + 2                                 Software Library

 Ctrl + 3                                 Monitoring

 Ctrl + 4                                 Administration

Other console shortcuts

                                                                       ﾉ   Expand table

<!-- p.33 -->

 Keyboard        Purpose
 shortcut

 Ctrl + M        Set the focus on the main (central) pane.

 Ctrl + T        Set the focus to the top node in the navigation pane. If the focus was already in
                 that pane, the focus is set to the last node you visited.

 Ctrl + I        Set the focus to the breadcrumb bar, below the ribbon.

 Ctrl + L        Set the focus to the Search field, when available.

 Ctrl + D        Set the focus to the details pane, when available.

 Alt             Change the focus in and out of the ribbon.

CMPivot shortcuts
Most web browser keyboard shortcuts          will work in CMPivot.

                                                                                ﾉ   Expand table

 Keyboard shortcut                       Purpose

 Ctrl + 1                                Set the focus on the first tab.

 Alt + <                                 To back to the address

Collection relationship diagram shortcuts
When you view collection relationships in the Configuration Manager console, use the
TAB key to change the focus. By default, the focus is on the page number controls.
When the focus is on the graph itself (navigator), use the following keyboard shortcuts
to navigate:

                                                                                ﾉ   Expand table

 Navigator shortcut                                           Purpose

 Ctrl + W                                                     Scroll up

 Ctrl + S                                                     Scroll down

 Ctrl + A                                                     Scroll left

 Ctrl + D                                                     Scroll right

<!-- p.34 -->

 Navigator shortcut                                       Purpose

 Ctrl + +                                                 Zoom in

 Ctrl + -                                                 Zoom out

Use the following keyboard shortcuts to quickly move focus to different areas of the
window:

                                                                         ﾉ   Expand table

 Keyboard shortcut                               Purpose

 Alt + P                                         Dependent page

 Alt + B                                         Back

 Alt + H                                         Home

 Alt + N                                         Collection name

 Alt + T                                         Filter

Other accessibility features
     To navigate the navigation pane, type the letters of a node name.

     Keyboard navigation through the main view and the ribbon is circular.

     Keyboard navigation in the details pane is circular. To return to the previous object
     or pane, use Ctrl + D, then Shift + TAB.

     After refreshing a Workspace view, the focus is set to the main pane of that
     workspace.

     To access a workspace menu, select the Tab key until the Expand/Collapse icon is in
     focus. Then, select the Down arrow key to access the workspace menu.

     To navigate through a workspace menu, use the arrow keys.

     To access different areas in the workspace, use the Tab key and Shift+Tab keys. To
     navigate within an area of the workspace, such as the ribbon, use the arrow keys.

     To access the address bar when your focus is in the tree node, use Shift+Tab three
     times.

<!-- p.35 -->

     On a wizard or property page, you can move between the boxes with keyboard
     shortcuts. Select the Alt key plus the underlined character (Alt+_) to select a
     specific box.

     To navigate to the different nodes of a workspace, enter the first letter of the name
     of a node. Each key press moves the cursor to the next node that begins with that
     letter. When you're using a screen reader, the reader reads out the name of that
     node.

Next steps
For more information on the fundamentals of navigating Configuration Manager user
interfaces, see the following articles:

     Using the Configuration Manager console
     Software Center user guide

  ７ Note

  The information in this article might apply only to users who license Microsoft
  products in the United States. If you obtained this product outside of the United
  States, you can use the subsidiary information card that came with your software
  package or visit the Microsoft Accessibility website    for contact information for
  Microsoft support services. You can contact your subsidiary to find out whether the
  type of products and services that are described in this section are available in your
  area. Information about accessibility is available in other languages, including
  Japanese and French.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.36 -->

Software Center user guide
Article • 10/18/2024

Applies to: Configuration Manager (current branch)

Your organization's IT admin uses Software Center to install applications, software
updates, and upgrade Windows. This user guide explains the functionality of Software
Center for users of the computer.

Software Center is installed automatically on Windows devices that your IT organization
manages. To get started, see How to open Software Center.

General notes about Software Center functionality:

      This article describes the latest features of Software Center. If your organization is
      using an older but still supported version of Software Center, not all features are
      available. For more information, contact your IT admin.

      Your IT admin may disable some aspects of Software Center. Your specific
      experience may vary.

      If multiple users are using a device at the same time, the user with the lowest
      session ID will be the only one to see all available deployments in Software Center.
      For example, multiple users on a remote desktop environment. Users with higher
      session IDs may not see some of the deployments in Software Center. For example,
      the users with higher session IDs may see deployed Applications, but not deployed
      Packages or Task Sequences. Meanwhile the user with the lowest session ID will see
      all deployed Applications, Packages, and Task Sequences. The Users tab of
      Windows Task Manager shows all users and their session IDs.

      Your IT admin may change the color of Software Center, and add your
      organization's logo.

How to open Software Center
Software Center is installed automatically on Windows devices that your IT organization
manages. For the simplest method to start Software Center, go to Start and type
Software Center . You may not need to type the entire string for Windows to find the

best match.

<!-- p.37 -->

To navigate the Start menu, look under the Microsoft Endpoint Manager group for the
Software Center icon.

  ７ Note

  The above Start menu path is for versions from November 2019 (version 1910) or
  later. In earlier versions, the folder name is Microsoft System Center.

If you can't find Software Center in the Start menu, contact your IT administrator.

Applications

                                                                                      

Select the Applications tab (1) to find and install applications that your IT admin deploys
to you or this computer.

     All (2): Shows all available applications that you can install.

<!-- p.38 -->

        Required (3): Your IT admin enforces these applications. If you uninstall one of
        these applications, Software Center reinstalls it.

        Filters (4): Your IT admin may create categories of applications. If available, select
        the drop-down list to filter the view to only those applications in a specific
        category. Select All to show all applications.

        Sort by (5): Rearrange the list of applications. By default this list sorts by Most
        recent. Recently available applications display with a New banner that's visible for
        seven days.

        Search (6): Still can't find what you're looking for? Enter keywords in the Search
        box to find it!

        Switch the view (7): Select the icons to switch the view between list view and tile
        view. By default the applications list shows as graphic tiles.

                                                                                   ﾉ   Expand table

 Icon     View            Description

          Multi-select    Install more than one application at a time. For more information, see
          mode            Install multiple applications.

          List view       This view displays the application icon, name, publisher, version, and
                          status.

          Tile view       Your IT admin can customize the icons. Below each tile displays the
                          application name, publisher, and version.

Install an application
Select an application from the list to see more information about it. Select Install to
install it. If an app is already installed, you may have the option to Uninstall.

Some apps may require approval before they install.

        When you try to install it, you can enter a comment and then Request the app.

<!-- p.39 -->

Software Center shows the request history, and you can cancel the request.

When an administrator approves your request, you can install the app. If you wait,
Software Center automatically installs the app during your non-business hours.

<!-- p.40 -->

Install multiple applications
Install more than one application at a time instead of waiting for one to finish before
starting the next. The selected apps need to qualify:

     The app is visible to you
     The app isn't already downloading or installed
     Your IT admin doesn't require approval to install the app

To install more than one application at a time:

   1. Select the multi-select icon in the upper right corner:

   2. Select two or more apps to install. Select the checkbox to the left of each app in
     the list.

   3. Select the Install Selected button to start.

The apps install as normal, only now in succession.

Share an application
To share a link to a specific app, after you select the app, select the Share icon in the
upper right corner:

Copy the string, and paste elsewhere, such as an email message. For example,
softwarecenter:SoftwareID=ScopeId_73F3BB5E-5EDC-4928-87BD-

4E75EB4BBC34/Application_b9e438aa-f5b5-432c-9b4f-6ebeeb132a5a . Anyone else in your

organization with Software Center can use the link to open the same application.

Featured Apps
Featured tab in Software Center displays featured apps. With this tab, IT admin can
mark apps as "featured" and encourage end users to use these apps. Currently, this
