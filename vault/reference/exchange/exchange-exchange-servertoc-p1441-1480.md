---
title: "Exchange Server — pages 1441-1480"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1441-1480
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1441-1480
family: exchange
documentKind: "doc"
abstract: "Parameter Function DefaultTheme Specifies the default theme that's used in Outlook on the web. LogonAndErrorLanguage Configures the various language settings for Outlook on the web. OutboundCharset UseGB18030 UseISO885915 DisplayPhotosEnabled Configures the user photo settings i"
---

# Exchange Server — pages 1441-1480

<!-- p.1441 -->

 Parameter                             Function

 DefaultTheme                          Specifies the default theme that's used in Outlook on the web.

 LogonAndErrorLanguage                 Configures the various language settings for Outlook on the web.
 OutboundCharset
 UseGB18030
 UseISO885915

 DisplayPhotosEnabled                  Configures the user photo settings in Outlook on the web.
 SetPhotoEnabled
 SetPhotoURL

Note: Not all of the available parameters apply to Exchange 2016 or Exchange 2019 (for
example, SpellCheckerEnabled).

To use the Exchange Management Shell to configure the properties of Outlook on the web
virtual directories, use the following syntax:

  PowerShell

  Set-OWAVirtualDirectory -Identity "<ExchangeServer>\owa <Website>" <Settings>

This example enables configures direct file access in Outlook on the web to block file types that
aren't specifically defined in the Allow list (the default action is allow).

  PowerShell

  Set-OwaVirtualDirectory -Identity "Contoso\owa (Default Web Site)" -
  ActionForUnknownFileAndMIMETypes Block

For detailed syntax and parameter information, see Set-OwaVirtualDirectory.

<!-- p.1442 -->

Configure http to https redirection for
Outlook on the web in Exchange Server
Article • 04/30/2025

APPLIES TO:          2016      2019     Subscription Edition

By default in Exchange Server, the URL https://<ServerName> redirects users to
https://<ServerName>/owa . But, if anyone tries to access Outlook on the web (formerly known

as Outlook Web App) by using http://<ServerName> or http://<ServerName>/owa , they'll get an
error.

You can configure http redirection for Outlook on the web so that requests for
http://<ServerName> or http://<ServerName>/owa are automatically redirected to https://*

<ServerName>*/owa . This requires the following configuration steps in Internet Information

Services (IIS):

   1. Remove the Require SSL setting from the default website.

   2. Restore the Require SSL setting on other virtual directories in the default website that had
         it enabled by default (except for /owa).

   3. Configure the default website to redirect http requests to the /owa virtual directory.

   4. Remove http redirection from all virtual directories in the default website (including
         /owa).

   5. Reset IIS for the changes to take effect.

For the default SSL and http redirect settings on all virtual directories in the default website,
see the Default Require SSL and HTTP Redirect settings in the default website on an Exchange
server section at the end of this topic.

What do you need to know before you begin?
         Estimated time to complete this procedure: 15 minutes.

         You need to be assigned permissions before you can perform this procedure or
         procedures. To see what permissions you need, see the "IIS Manager" entry in the
         Outlook on the web permissions section of the Clients and mobile devices permissions
         topic.

         The procedures in this topic might cause a web.config file to be created in the folder
         %ExchangeInstallPath%ClientAccess\OAB . If you later remove http redirection for Outlook

<!-- p.1443 -->

   on the web, Outlook might freeze when users click Send and Receive. To prevent Outlook
   from freezing after you remove http redirection, delete the web.config file in
    %ExchangeInstallPath%ClientAccess\OAB .

   Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
   protocol that's used to encrypt data sent between computer systems. They're so closely
   related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
   Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
   center, and the Exchange Management Shell have often been used to encompass both
   the SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
   version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
   protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online      , or Exchange Online Protection .

Step 1: Use IIS Manager to remove the Require SSL
setting from the default website
 1. Open IIS Manager on the Exchange server. An easy way to do this in Windows Server
   2012 or later is to press Windows key + Q, type inetmgr, and select Internet Information
   Services (IIS) Manager in the results.

 2. Expand the server, and expand Sites.

 3. Select Default Web Site. and verify Features View is selected at the bottom of the page.

 4. In the IIS section, double-click SSL Settings.

<!-- p.1444 -->

   5. On the SSL Settings page, clear the Require SSL check box, and in the Actions pane, click
     Apply.

Note: To perform this procedure on the command line, open an elevated command prompt on
the Exchange server (a Command Prompt window you open by selecting Run as administrator)
and run the following command:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -section:access
  -sslFlags:None -commit:APPHOST

Step 2: Use IIS Manager to restore the Require SSL
setting on other virtual directories in the default
website
When you change the Require SSL setting on a website in IIS, the setting is automatically
inherited by all virtual directories in the website. Because we're only interested in configuring

<!-- p.1445 -->

Outlook on the web, you need to restore the Require SSL setting for other virtual directories
that had it enabled by default.

Based on the information in the Default Require SSL and HTTP Redirect settings in the default
website on an Exchange server section, use the following procedure to restore the setting on
the other virtual directories where Require SSL was enabled by default:

   1. In IIS Manager, expand the server, expand Sites, and expand Default Web Site.

   2. Select the virtual directory, and verify Features View is selected at the bottom of the
     page.

   3. In the IIS section, double-click SSL Settings.

   4. On the SSL Settings page, select the Require SSL check box, and in the Actions pane,
     click Apply.

   5. Repeat the previous steps on each virtual directory in the default website that had
     Require SSL enabled by default (except for /owa). The only virtual directories that don't
     have Require SSL enabled by default are /PowerShell and /Rpc.

<!-- p.1446 -->

Note: To perform these procedures on the command line, replace <VirtualDirectory> with the
name of the virtual directory, and run the following command in an elevated command
prompt:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web
  Site/<VirtualDirectory>" -section:Access -sslFlags:Ssl,Ssl128 -commit:APPHOST

Step 3: Use IIS Manager to configure the default
website to redirect to the /owa virtual directory.
  1. In IIS Manager, expand the server, and expand Sites.

  2. Select Default Web Site. and verify Features View is selected at the bottom of the page.

  3. In the IIS section, double-click HTTP Redirect.

  4. On the HTTP Redirect page, configure the following settings:

  5. Select the Redirect requests to this destination check box, and enter the value https://*
     <OWAUrl>*/owa (For example, https://webmail.contoso.com/owa       ).

  6. In the Redirect Behavior section, select the Only redirect requests to content in this
     directory (not subdirectories) check box.

  7. In the Status code list, verify Found (302) is selected.

     When you're finished, click Apply in the Actions pane.

<!-- p.1447 -->

Note: To perform this procedure on the command line, replace <OWAUrl> with the URL of the
OWA virtual directory, open an elevated command prompt and run the following command:

  Console

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web Site" -
  section:httpredirect -enabled:true -destination:"https://<OWAUrl>/owa" -
  childOnly:true

Step 4: Use IIS Manager to remove http redirection
from all virtual directories in the default website
When you enable redirection on a website in IIS, the setting is automatically inherited by all
virtual directories in the website. Because we're only interested in configuring redirection for
the default website, you need to remove the redirect setting from all virtual directories. By
default, no directories or virtual directories in the default website are enabled for redirection.
For more information, see the Default Require SSL and HTTP Redirect settings in the default
website on an Exchange server section.

Use the following procedure to remove the redirect setting from all virtual directories in the
default website (including /owa):

   1. In IIS Manager, expand the server, expand Sites, and expand Default Web Site.

   2. Select the virtual directory, and verify Features View is selected at the bottom of the
     page.

   3. In the IIS section, double-click HTTP Redirect.

<!-- p.1448 -->

  4. On the HTTP Redirect page, change the following settings:

  5. Clear the Only redirect requests to content in this directory (not subdirectories) check
     box.

  6. Clear the Redirect requests to this destination check box.

  7. In the Actions pane, click Apply.

  8. Repeat the previous steps on each virtual directory in the default website.

Note: To perform these procedures on the command line, replace <VirtualDirectory> with the
name of the virtual directory, and run the following command in an elevated command
prompt:

  Console

<!-- p.1449 -->

  %windir%\system32\inetsrv\appcmd.exe set config "Default Web
  Site/<VirtualDirectory>" -section:httpredirect -enabled:false -destination:"" -
  childOnly:false

Step 5: Use IIS Manager to restart IIS
   1. In IIS Manager, select the server.

   2. In the Actions pane, click Restart.

Note: To perform this procedure on the command line, open an elevated command prompt on
the Exchange server and run the following commands:

  Console

  net stop w3svc /y

  Console

  net start w3svc

How do you know this worked?
To verify that you have successfully configured http to https redirection for Outlook on the
web, perform the following steps:

<!-- p.1450 -->

   1. On a client computer, open a web browser and enter the URL http://<ServerName> . On
     the local server, you can use the value http://127.0.0.1 or http://localhost .

   2. Verify that you're redirected to Outlook on the web in https, and verify that you can log in
     successfully.

   3. Open the URL http://<ServerName>/owa (or http://127.0.0.1/owa or
     http://localhost/owa ).

   4. Verify that you're redirected to Outlook on the web in https, and verify that you can log in
     successfully.

Default Require SSL and HTTP Redirect settings in
the default website on an Exchange server
The default Require SSL and HTTP Redirect settings for the default website and all virtual
directories in the default website on an Exchange server are described in the following table.

                                                                                ﾉ   Expand table

 Website             Virtual directory                Require SSL               HTTP Redirect

 Default Web Site    n/a                              yes                       none

 Default Web Site    API                              yes                       none

 Default Web Site    aspnet_client (directory)        yes                       none

 Default Web Site    Autodiscover                     yes                       none

 Default Web Site    ecp                              yes                       none

 Default Web Site    EWS                              yes                       none

 Default Web Site    mapi                             yes                       none

 Default Web Site    Microsoft-Server-ActiveSync      yes                       none

 Default Web Site    OAB                              yes                       none

 Default Web Site    owa                              yes                       none
                                                      Subdirectories:

                                                            auth: yes
                                                            Calendar: no
                                                            Integrated: yes

<!-- p.1451 -->

Website            Virtual directory   Require SSL     HTTP Redirect

                                            oma: yes

Default Web Site   PowerShell          no              none

Default Web Site   Rpc                 no              none

<!-- p.1452 -->

View or configure Outlook on the web
mailbox policy properties
Article • 04/30/2025

APPLIES TO:         2016    2019       Subscription Edition

You can configure mailbox policies in Exchange Server for Outlook on the web through the
Exchange admin center (EAC) or Exchange Management Shell. After you create an Outlook on
the web mailbox policy, you can then configure a variety of options to control the features
available to users in Outlook on the web. For example, you can enable or disable Inbox rules or
create a list of allowed file types for attachments.

What do you need to know before you begin?
      Estimated time to complete each procedure: 3 minutes.

      To open the EAC, see Exchange admin center in Exchange Server. To open the Exchange
      Management Shell, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Outlook on the web mailbox
      policies" entry in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the EAC to view or configure Outlook on the
web mailbox policies
   1. In the EAC, click Permissions > Outlook Web App policies.

   2. In the result pane, click to select the mailbox policy you want to view or configure.

   3. Click Edit.

   4. On the General tab, you can view and edit the name of the policy.

<!-- p.1453 -->

   5. On the Features tab, use the check boxes to enable or disable features. By default, the
     most common features are displayed. To see all features that can be enabled or disabled,
     click More options.

     Notes:

           Features settings for Outlook on the web mailbox policies override Outlook on the
           web virtual directory settings. You can change segmentation settings for individual
           users by using the Set-CASMailbox cmdlet in the Exchange Management Shell.

           The option to enable or disable the standard version of Outlook on the web by
           using the Premium client check box has been deprecated and will be removed from
           the settings. The standard version of Outlook on the web is always enabled.

   6. On the File Access tab, use the check boxes to configure the file access and viewing
     options for users. File access lets a user open or view the contents of files attached to an
     email message.

     File access can be controlled based on whether a user has signed in on a public or private
     computer. The option for users to select private computer access or public computer
     access is available only when you're using forms-based authentication. All other forms of
     authentication default to private computer access.

           Direct file access: Select this check box if you want to enable direct file access.
           Direct file access lets users open files attached to email messages.

           WebReady Document Viewing: Select this check box if you want to enable
           supported documents to be converted to HTML and displayed in a web browser.

           Force WebReady Document Viewing when a converter is available: Select this
           check box if you want to force documents to be converted to HTML and displayed
           in a web browser before users can open them in the viewing application. Documents
           can be opened in the viewing application only if direct file access has been enabled.

   7. On the Offline access tab, use the option buttons to configure offline access availability.

   8. Click Save to update the policy.

Use the Exchange Management Shell to view
Outlook on the web mailbox policies
This example retrieves the properties of the Outlook on the web mailbox policy Executives in
the organization Fabrikam .

<!-- p.1454 -->

  PowerShell

  Get-OwaMailboxPolicy -Identity Fabrikam\Executives

For more information about syntax and parameters, see Get-OwaMailboxPolicy.

Use the Exchange Management Shell to configure
Outlook on the web mailbox policies
This example enables calendar access in the default mailbox policy.

  PowerShell

  Set-OwaMailboxPolicy -Identity Default -CalendarEnabled $true

For more information about syntax and parameters, see Set-OwaMailboxPolicy.

How do you know this worked?
To verify that you've successfully edited an Outlook on the web mailbox policy:

   1. In the EAC, click Permissions > Outlook Web App Policies, and then choose a specific
     Outlook on the web mailbox policy.

   2. Click Edit to view the properties of the mailbox policy.

   3. Click Save or Cancel to close the properties page.

See also
Outlook Web App mailbox policy procedures in Exchange 2013

<!-- p.1455 -->

Create a theme for Outlook on the web in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

A theme defines the colors, fonts, and images that are displayed to users in Outlook on the
web (formerly known as Outlook Web App) in Exchange Server. Each theme is a collection of
files that are stored on the Exchange server. The built-in themes are described in the Default
Outlook on the web themes in Exchange Server section at the end of this topic.

The basic steps to create a new theme for Outlook on the web are:

   1. Copy the folders and files of an existing theme, and rename the copied folders and files.

   2. Configure the display name and sort order of the new theme.

   3. Customize the new theme.

   4. (Optional) Set the new theme as the default, and prevent users from selecting themes.

   5. (Optional) Allow users to see and select the new theme

   6. Restart IIS for the changes to take affect.

If you use multiple Exchange servers for Outlook on the web client connections, you need to
copy the new theme to each server. You should also create a backup copy of the new theme so
you can copy the files back after you reinstall or upgrade the Exchange server.

After you create a theme, you may also want to customize elements that are common to all
themes. For more information, see Customize the Outlook on the web sign-in, language
selection, and error pages in Exchange Server.

What do you need to know before you begin?
      Estimated time to complete this task: 45 minutes.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Outlook on the web virtual
      directories" entry in the Clients and mobile devices permissions topic. The account you
      use also needs to be a member of the local Administrators group on the Exchange server.

      The light version of Outlook on the web doesn't support themes.

<!-- p.1456 -->

     To replace an existing color with a new color, you need the HTML RGB value of the new
     color. You can find HTML RGB values at Color Table     . If you can't find the color there,
     you can use an image editing tool or an HTML color codes web site to determine its
     HTML RGB value.

     Don't delete the folder %ExchangeInstallPath%ClientAccess\OWA\prem\
     <ExchangeVersion>\resources\themes\base , or any files in it.

     If you decide to directly edit an existing theme (not a copy of the theme), make a backup
     copy of the original files before you modify them.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server .

Step 1: Use File Explorer to copy the folders and
files of an existing theme, and rename the copied
folders and files
You can inspect the built-in themes by opening a mailbox in Outlook on the web, selecting
Settings, and then selecting Change theme.

You can use the information in the Default Outlook on the web themes in Exchange Server
section at the end of this topic to match the display name of the theme in Outlook on the web
to the name of the theme folder on the Exchange server.

The theme files and folders are stored in the following locations:

<!-- p.1457 -->

     %ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\themes\

     contains the theme folder that holds the header image, theme preview image, and theme
     description text.

     %ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\styles\

     contains the _fabric.color.variables.theme.<ThemeFolderName>.less and
     fabric.color.theme.<ThemeFolderName>.css files that define the colors that are used in the

     theme.

     Note: The <ExchangeVersion> subfolder uses the syntax 15.1. nnn. nn, and indicates the
     Exchange Cumulative Update (CU) that's installed.

After you've identified the theme that's closest to what you want (for example, with or without
a header image), you need to copy the theme folder and the corresponding files, and then
rename the copied folders and files

   1. In File Explorer, browse to %ExchangeInstallPath%ClientAccess\OWA\prem\
     <ExchangeVersion>\resources\themes .

   2. Select an existing theme folder in the \themes folder, copy it, and then paste it back into
     the \themes folder. This results in a new folder named <ThemeFolderName> - Copy .

     Note: An easy way to copy and paste the theme folder is to select the folder, press the
     Control key + C, and then press the Control key + V.

   3. Rename the new theme folder that you created in the previous step. For example,
     fourthcoffee .

     Note: An easy way to rename the folder is to select it, and then press the F2 key.

   4. In File Explorer, browse to %ExchangeInstallPath%ClientAccess\OWA\prem\
     <ExchangeVersion>\resources\styles\ .

   5. Locate the files named _fabric.color.variables.theme.<ThemeFolderName>.less and
     fabric.color.theme.<ThemeFolderName>.css that correspond to the theme folder you

     copied in step 2. Select each file, copy it, and paste it back into the \styles folder. This
     results in new files named _fabric.color.variables.theme.<ThemeFolderName> - Copy.less
     and fabric.color.theme.<ThemeFolderName> - Copy.css .

   6. Rename the new files that you created in the previous step. The <ThemeFolderName>
     value must match the folder name from step 3. For example,
     _fabric.color.variables.theme.fourthcoffee.less and

     fabric.color.theme.fourthcoffee.css .

<!-- p.1458 -->

Step 2: Use Notepad to configure the display name
and sort order of the new theme
You need to configure a unique display name and sort order for the new theme, because the
new theme has the same display name and sort order as the theme you copied. The theme's
display name appears in the Change theme panel in Outlook on the web. The sort order
determines where the theme appears in the list of themes.

  1. Use Notepad to open the file named themeinfo.xml in the new theme folder
     %ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\themes\
     <NewThemeFolder> that you created in Step 1. The contents of the file look like this:

     <theme displayname="__<CopiedThemeName>__" sortorder="<CopiedThemeSortOrder>"/>

  2. Change the displayname="__<CopiedThemeName>__" value to the value you want. For
     example displayname = "Fourth Coffee Corporate Theme" .

     Note: The theme display name value "__<ThemeName>__" is a code string that's localized
     into different languages. The text value that you specify for the new theme isn't localized
     into different languages.

  3. Change the sortorder="<CopiedThemeSortOrder>" integer value to the unique value you
     want. A lower value appears earlier in the list of themes. You can use the information in
     the Default Outlook on the web themes in Exchange Server section at the end of this
     topic to find the sort order values for the built-in themes. The Default theme has
     sortorder="0" , and appears first in the list.

          If you want to insert your new theme among the list of built-in themes, change the
          number to a unique value that isn't already in use. For example, if you want your
          new theme to appear second in the list, you can use the value sortorder="5" .

          If you want to replace the position of a built-in theme in the list, set the number to
          the same value as built-in theme, and then change the sort order for the built-in
          theme. For example, if you want your new theme to appear first in the list, you need
          to set your new theme to sortorder="0" . But, you also need to open the
           themeinfo.xml file in the \base folder (the Default theme) to change the value
           sortorder="0" to something else (for example, sortorder="5") .

  4. When you're finished, save and close the themeinfo.xml file.

Step 3: Customize the new theme

<!-- p.1459 -->

Image files
Theme image files are stored in the following folders in
%ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\themes\

<ThemeFolderName> :

      \images\0 : These files are used in left-to-right languages.

      \images\rtl : These files are used in right-to-left languages. Depending on the image, the

     file might be exactly the same as the left-to-right version, or it might be reversed (right-
     to-left instead of left-to-right).

The image files that exist in these folders are described in the following table:

                                                                                      ﾉ    Expand table

 File name              Dimensions (width x   Bit       Description
                        height in pixels)     depth

 headerbgmaing2.png     2000 x 50             32        The header image for themes that use a static
                                                        header image. The size of the file varies.

                                                        If the theme doesn't use a static header
                                                        image, the file is 1 x 1, and the size is 2815
                                                        bytes.

 headerbgmaing2.gif     2000 x 50             24        The header image for themes that use an
                                                        animated header image. The size of the file
                                                        varies.

                                                        If the theme doesn't use an animated header
                                                        image, the file is 1 x 1, and the size is 43
                                                        bytes.

 themepreview.png       64 x 64               24 or 8   The small square image that represents the
                                                        theme in the Change theme panel in Outlook
                                                        on the web.

                                                        For the Default theme and the Black theme,
                                                        this file 1 x 1, and the preview image is a black
                                                        square.

You can edit the existing image file, or replace the file with a new file that has the same name
and dimensions.

Colors

<!-- p.1460 -->

Theme colors are defined in the following files in the
%ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\styles folder:

     fabric.color.theme.<ThemeFolderName>.css

     _fabric.color.variables.<ThemeFolderName>.less

If you change a color value, you need to change all references to the color in both files.

Step 4: (Optional) Set the default theme and
prevent users from selecting a theme
Setting a new default theme only affects users who haven't manually selected their theme. To
force all users to use the default theme, you also need to disable theme selection in Outlook
on the web. These settings affect all users who connect to Outlook on the web through the
Exchange server.

To set the default theme and prevent users from changing their theme in Outlook on the web,
use the following syntax:

  PowerShell

  Set-OwaVirtualDirectory -Identity <VirtualDirectoryIdentity> -DefaultTheme
  <ThemeFolderName> -ThemeSelectionEnabled $false

This example configures the theme folder named fourthcoffee as the default theme in
Outlook on the web for the default website on the server named Mailbox01.

  PowerShell

  Set-OwaVirtualDirectory -Identity "Mailbox01\owa (Default Web Site)" -DefaultTheme
  fourthcoffee -ThemeSelectionEnabled $false

Notes:

     By default, the value of the DefaultTheme parameter is blank ( $null ). This value indicates
     that no default theme is specified, and the theme named Default is used if the user hasn't
     manually selected a theme.

     Exchange doesn't validate the value that you specify for the DefaultTheme parameter.
     Make sure that the theme exists.

<!-- p.1461 -->

     To specify a default theme for specific users that overrides the default theme setting on
     the Outlook on the web virtual directory, use the DefaultTheme parameter on the Set-
     OwaMailboxPolicy cmdlet.

Step 5: (Optional) Allow users to select the new
theme
If you don't want to force all users to use the new theme, you need to add the new theme to
the stylemanifest.xml file so users can find and select it in the list of themes. The
stylemanifest.xml file is located in %ExchangeInstallPath%ClientAccess\OWA\prem\
<ExchangeVersion>\manifests .

This example adds a new line in the stylemanifest.xml file for the new fourthcoffee theme.

<themeVariables themeName="fourthcoffee"

fileName="_fabric.color.variables.theme.fourthcoffee.less" />

Step 6: Restart IIS
You need to restart Internet Information Services (IIS) for the changes to take effect.

   1. Open IIS Manager on the Exchange server. An easy way to do this in Windows Server
     2012 or later is to press Windows key + Q, type inetmgr, and select Internet Information
     Services (IIS) Manager in the results.

   2. In IIS Manager, select the server.

   3. In the Actions pane, click Restart.

<!-- p.1462 -->

Note: To perform this procedure on the command line, open an elevated command prompt on
the Exchange server (a Command Prompt window you open by selecting Run as administrator)
and run the following command:

  Console

  net stop w3svc /y

  Console

  net start w3svc

How do you know this worked?
To verify that you've successfully created an Outlook on the web theme, perform the following
steps:

   1. Open a mailbox in Outlook on the web. On the Exchange server, you can test your theme
     by opening the URL https://localhost/owa or https://127.0.0.1/owa .

   2. Depending on the settings you configured, verify the new theme is used by default, or
     verify that you can see and select the new theme at Settings > Change theme.

   3. If you don't see your changes after you restart IIS, clear your browsing history (delete
     temporary Internet files), and refresh the browser window.

<!-- p.1463 -->

Default Outlook on the web themes in Exchange
Server
The built-in Outlook on the web themes are located in the folder
%ExchangeInstallPath%ClientAccess\OWA\prem\<ExchangeVersion>\resources\themes , and are

described in the following table.

                                                                                ﾉ   Expand table

 Folder name      Display name in Outlook    Sort order in Outlook on the web   Header image
                  on the web                 (lower listed first)               type

 angular          Angular 80's               110                                Static

 balloons         Balloons                   240                                Static

 base             Default                    0                                  None

 beach            Beach Sunset               40                                 Animated

 black            Black                      670                                None

 blueberry        Blueberry                  600                                None

 blueprint        Blueprint                  120                                Static

 bricks           Bricks                     20                                 Static

 cats             Cats                       300                                Static

 chevron          Chevron                    80                                 Static

 circuit          Circuit                    130                                Static

 comic            Comic Book                 170                                Static

 contrast         Contrast                   500                                None

 cordovan         Cordovan                   650                                None

 crayon           Crayon                     140                                Static

 cubes            3D Cubes                   190                                Static

 cubism           Cubism                     310                                Static

 darkcordovan     Dark Cordovan              660                                None

 darkorange       Dark Orange                620                                None

<!-- p.1464 -->

Folder name      Display name in Outlook   Sort order in Outlook on the web   Header image
                 on the web                (lower listed first)               type

diamonds         Floating Diamonds         160                                Static

far              Far, Far Away             150                                Animated

grape            Grape                     610                                None

jelly            Jelly Fish                70                                 Animated

lightblue        Light Blue                530                                None

lightgreen       Light Green               540                                None

lite             Lite                      510                                None

mediumdarkblue   Dark Blue                 640                                None

minimal          Minimal                   520                                None

modern           20th Century Modern       280                                Static

mountain         Mountain Peak             50                                 Static

orange           Orange                    580                                None

paint            Finger paints             290                                Static

pink             Pink                      550                                None

pixel            Pixel Pop                 60                                 Static

polka            Polka Dot                 200                                Static

pomegranate      Pomegranate               590                                None

primary          Primary                   180                                Static

raspberry        Raspberry                 570                                None

robot            Robot                     100                                Animated

simple           Simple Facets             230                                Static

spectrum         Spectrum Facets           90                                 Static

strawberry       Strawberry                250                                Static

super            Super sparkle happy       10                                 Static

teagarden        Tea Garden                210                                Static

teal             Teal                      550                                None

<!-- p.1465 -->

Folder name   Display name in Outlook   Sort order in Outlook on the web   Header image
              on the web                (lower listed first)               type

watermelon    Watermelon                630                                None

whale         Whale of a Time           30                                 Animated

whimsical     Whimsical                 220                                Static

wntrlnd       Winterland                260                                Static

wrld          One World                 270                                Static

<!-- p.1466 -->

Customize the Outlook on the web sign-in,
language selection, and error pages in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

The Outlook on the web (formerly known as Outlook Web App) sign-in, language selection, and error
pages are based on image and content style sheet (CSS) files in the themes resources folder in the
Client Access (front end) services on an Exchange Server 2016 or Exchange 2019 server. Outlook on
the web uses only one set of sign-in, language selection, and error pages for all themes. Any
modifications to those pages will be seen by all users who connect to the Exchange server for
Outlook on the web.

Notes:

      Backup the default Outlook on the web files before you make any changes.

      Create a back-up copy of your customized files so you can reapply them after a reinstallation or
      upgrade of the Exchange server.

      If you use multiple Exchange servers for Outlook on the web connections, you need to copy the
      modified files to each server.

For more information about Outlook on the web, see Outlook on the web in Exchange Server. For
information about creating a custom theme, see Create a theme for Outlook on the web in Exchange
Server.

What do you need to know before you begin?
      Estimated time to complete this task: 30 minutes.

      You need to be assigned permissions before you can perform this procedure or procedures. To
      see what permissions you need, see the "Graphics editor" entry under "Outlook on the web
      Permissions" in the Clients and mobile devices permissions topic.

      To replace the existing color with a new color, you need the HTML RGB value of the new color.
      You can find HTML RGB values in the topic Color Table   . If you can't find the color there, you
      can use an image editing tool to sample a color and determine its HTML RGB value.

      For information about keyboard shortcuts that may apply to the procedures in this topic, see
      Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.1467 -->

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server   ,
 Exchange Online    , or Exchange Online Protection .

Customize the color of the Outlook on the web sign-
in page
 1. Use Notepad to open the file %ExchangeInstallPath%FrontEnd\HttpProxy\owa\auth\
   <ExchangeVersion>\themes\resources\logon.css .

   Note: The <ExchangeVersion> subfolder uses the syntax 15.1. nnn. nn, and changes every time
   you install an Exchange Cumulative Update (CU).

 2. In the logon.css file, replace the default blue color value #0072c6 with the HTML RGB value
   that you want to use.

 3. When you're finished, save and close the file.

Customize the color of the Outlook on the web error
page
 1. Use Notepad to open the file %ExchangeInstallPath%FrontEnd\HttpProxy\owa\auth\
   <ExchangeVersion>\themes\resources\errorFE.css .

<!-- p.1468 -->

 2. In the errorFE.css file, replace the default blue color value #0072c6 with the HTML RGB value
   that you want to use.

 3. When you're finished, save and close the file.

Customize the color of the Outlook on the web
language selection page
 1. Use Notepad to open the file %ExchangeInstallPath%ClientAccess\Owa\prem\
   <ExchangeVersion>\resources\styles\languageselection.css .

 2. In the languageselection.css file, replace the default blue color value #0072c6 with the HTML
   RGB value that you want to use.

 3. When you're finished, save and close the file.

<!-- p.1469 -->

Customize the images on the Outlook on the web
sign-in, language selection, and error pages
You can edit the existing image files, or replace the files with new files that have the same names and
dimensions. The images are described in the following table:

                                                                                            ﾉ   Expand table

 Image   File name                      Location                                            Dimensions    Bit
                                                                                            (width x      depth
                                                                                            height in
                                                                                            pixels)

 1       favicon.ico                    %ExchangeInstallPath%FrontEnd\HttpProxy\owa\auth\   16 x 16       32
                                        <ExchangeVersion>\themes\resources

 2       olk_logo_white.png             %ExchangeInstallPath%ClientAccess\Owa\prem\         128 x 108     32
                                        <ExchangeVersion>\resources\images\0

 3       owa_text_blue.png              %ExchangeInstallPath%ClientAccess\Owa\prem\         300 x 76      32
                                        <ExchangeVersion>\resources\images\0

 4       Sign_in_arrow.png (for left-   %ExchangeInstallPath%FrontEnd\HttpProxy\owa\auth\   22 x 22       32
         to-right languages)            <ExchangeVersion>\themes\resources
         Sign_in_arrow_rtl.png (for
         right-to-left languages)

<!-- p.1470 -->

 Image     File name                     Location                                             Dimensions   Bit
                                                                                              (width x     depth
                                                                                              height in
                                                                                              pixels)

 5         olk_logo_white_cropped.png    %ExchangeInstallPath%FrontEnd\HttpProxy\owa\auth\    265 x 310    32
                                         <ExchangeVersion>\themes\resources

 6         office_logo_white_small.png   %ExchangeInstallPath%ClientAccess\Owa\prem\          81 x 26      8
                                         <ExchangeVersion>\resources\images\0 (for left-to-
                                         right languages)

                                         %ExchangeInstallPath%ClientAccess\Owa\prem\
                                         <ExchangeVersion>\resources\images\rtl (for right-
                                         to-left languages)

How do you know this worked?
To verify that you've successfully customized the Outlook on the web sign-in, language selection, and
error pages, perform the following steps:

     1. Open the Outlook on the web sign-in page in a web browser. On the Exchange server that
       hosts the Outlook on the web virtual directory, you can test your changes by opening the URL
       https://localhost/owa or https://127.0.0.1/owa .

     2. If you don't see your changes, clear your browsing history (delete temporary Internet files), and
       refresh the browser window.

       Note: To see the effects of your changes, you can keep the .css file open and refresh the
       browser window after you save each change.

<!-- p.1471 -->

Use AD FS claims-based authentication
with Outlook on the web
10/15/2025

APPLIES TO:          2016   2019     Subscription Edition

Installing and configuring Active Directory Federation Services (AD FS) in Exchange Server
organizations allows clients to use AD FS claims-based authentication to connect to Outlook
on the web (formerly known as Outlook Web App) and the Exchange admin center (EAC).
Claims-based identity is another approach to authentication that removes authentication
management from the application, and makes it easier for you to manage accounts by
centralizing authentication. When claims-based authentication is enabled, Outlook on the web
and the EAC aren't responsible for authenticating users, storing user accounts and passwords,
looking up user identity details, or integrating with other identity systems. Centralizing
authentication helps make it easier to upgrade authentication methods in the future.

AD FS claims-based authentication replaces the traditional authentication methods that are
available for Outlook on the web and the EAC. For example:

     Active Directory client certificate authentication
     Basic authentication
     Digest authentication
     Forms authentication
     Windows authentication

Setting up AD FS claims-based authentication for Outlook on the web and the EAC in Exchange
Server involves the following additional servers:

     A Windows Server 2012 or later domain controller (Active Directory Domain Services
     server role).

     A Windows Server 2012 or later AD FS server (Active Directory Federation Services server
     role). Windows Server 2012 uses AD FS 2.1, and Windows Server 2012 R2 uses AD FS 3.0.
     You need to be a member of the Domain Admins, Enterprise Admins, or local
     Administrators security group to install AD FS, and to create the required relying party
     trusts and claim rules on the AD FS server.

     Optionally, a Windows Server 2012 R2 or later Web Application Proxy server (Remote
     Access server role, Web Application Proxy role service).

        Web Application Proxy is a reverse proxy server for web applications that are inside the
        corporate network. Web Application Proxy allows users on many devices to access

<!-- p.1472 -->

        published web applications from outside the corporate network. For more information,
        see Installing and Configuring Web Application Proxy for Publishing Internal
        Applications.

        Although Web Application Proxy is typically recommended when AD FS is accessible to
        external clients, offline access in Outlook on the web isn't supported when using AD FS
        authentication through Web Application Proxy.

        Installing Web Application Proxy on a Windows Server 2012 R2 server requires local
        administrator permissions.

        You need to deploy and configure the AD FS server before you configure the Web
        Application Proxy server, and you can't install Web Application Proxy on the same
        server where AD FS is installed.

What do you need to know before you begin?
     Estimated time to complete this procedure: 45 minutes.

     The procedures in this topic are based on Windows Server 2012 R2.

     Outlook on the web for devices doesn't support AD FS claims-based authentication.

     For the procedures in the Exchange organization, you need to have Organization
     Management permissions.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Step 1: Review the certificate requirements for AD
FS
AD FS requires two basic types of certificates:

     A service communication Secure Sockets Layer (SSL) certificate for encrypted web services
     traffic between the AD FS server, clients, Exchange servers, and the optional Web
     Application Proxy server. We recommend that you use a certificate that's issued by an

<!-- p.1473 -->

      internal or commercial certification authority (CA), because all clients need to trust this
      certificate.

      A token-signing certificate for encrypted communication and authentication between the
      AD FS server, Active Directory domain controllers, and Exchange servers. We recommend
      that you use the default self-signed AD FS token signing certificate.

For more information about creating and importing SSL certificates in Windows, see Server
Certificates.

Here's a summary of the certificates that we'll be using in this scenario:

                                                                                        ﾉ   Expand table

 Common name (CN) in the        Type     Required on    Comments
 certificate (in the Subject,            servers
 Subject Alternative Name,
 or a wildcard certificate
 match)

 adfs.contoso.com               Issued   AD FS server   This is the host name that's visible to clients, so
                                by a     Web            clients need to trust the issuer of this
                                CA       Application    certificate.
                                         Proxy server

 ADFS Signing -                 Self-    AD FS server   The default self-signed certificate is
 adfs.contoso.com               signed   Exchange       automatically copied over during the
                                         servers        configuration of the optional Web Application
                                                        Proxy server, but you'll need to manually
                                         Web            import it into the Trusted Root Certificate store
                                         Application    on all Exchange servers in your organization.
                                         Proxy server   By default, the self-signed token-signing
                                                        certificates are valid for one year. The AD FS
                                                        server is configured to automatically renew
                                                        (replace) its self-signed certificates before they
                                                        expire, but you'll need to re-import the
                                                        certificate on the Exchange servers.

                                                        You can increase the default certificate
                                                        expiration period by running this command in
                                                        Windows PowerShell on the AD FS server: Set-
                                                        AdfsProperties -CertificateDuration <Days>
                                                        (the default value is 365). For more information,
                                                        see Set-AdfsProperties.

                                                        To export the certificate from the AD FS
                                                        Management console, select Service >
                                                        Certificates > right-click on the token-signing

<!-- p.1474 -->

 Common name (CN) in the        Type     Required on    Comments
 certificate (in the Subject,            servers
 Subject Alternative Name,
 or a wildcard certificate
 match)

                                                        certificate > select View Certificate > click the
                                                        Details tab > click Copy to File.

 mail.contoso.com               Issued   Exchange       This is the typical certificate that's used to
                                by a     servers        encrypt external client connections to Outlook
                                CA       Web            on the web (and likely other Exchange IIS
                                         Application    services). For more information, see Certificate
                                         Proxy server   requirements for Exchange services.

For more information, see the "Certificate requirements" section in AD FS Requirements.

  ７ Note

  Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
  protocol that's used to encrypt data sent between computer systems. They're so closely
  related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
  Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
  center, and the Exchange Management Shell have often been used to encompass both the
  SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
  version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
  protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

Step 2: Deploy an AD FS server
You can use Server Manager or Windows PowerShell to install the Active Directory Federation
Services role service on the target server.

To use Server Manager to install AD FS, follow these steps:

   1. On the target server, open Server Manager, click Manage, and then select Add Roles and
     Features.

<!-- p.1475 -->

2. The Add Roles and Features Wizard opens. You'll start on the Before you begin page
  unless you previously selected Skip this page by default. Click Next.

3. On the Select installation type page, verify that Role-based or feature-based installation
  is selected, and then click Next.

4. On the Select destination server page, verify the server selection, and then click Next.

<!-- p.1476 -->

5. On the Select server roles page, select Active Directory Federation Services from the list,
  and then click Next.

6. On the Select features page, click Next (accept the default feature selections).

<!-- p.1477 -->

7. On the Active Directory Federation Services (AD FS) page, click Next.

8. Windows Server 2012 only: On the Select role services page, click Next (accept the
  default role service selections).

9. On the Confirm installation selections page, click Install.

<!-- p.1478 -->

 10. On the Installation progress page, you can watch the progress bar to verify that the
     installation was successful. When the installation is finished, leave the wizard open so you
     can click Configure the federation service on this server in Step 3b: Configure the AD FS
     server.

To use Windows PowerShell to install AD FS, run the following command:

  PowerShell

  Install-WindowsFeature ADFS-Federation -IncludeManagementTools

Step 3: Configure and test the AD FS server

<!-- p.1479 -->

You can also refer to this checklist to help you configure AD FS: Checklist: Setting Up a
Federation Server.

Step 3a: Create a gMSA on a domain controller
Before you configure the AD FS server, you need to create a group Managed Service Account
(gMSA) on a Windows Server 2012 or later domain controller. You do this in an elevated
Windows PowerShell window on the domain controller (a Windows PowerShell window you
open by selecting Run as administrator).

   1. Run the following command:

        PowerShell

        Add-KdsRootKey -EffectiveTime (Get-Date).AddHours(-10)

     If the command is successful, a GUID value is returned. For example:

       Guid
       ----
       2570034b-ab50-461d-eb80-04e73ecf142b

   2. To create a new gMSA account for the AD FS server, use the following syntax:

        PowerShell

        New-ADServiceAccount -Name <AccountName> -DnsHostName <FederationServiceName>
        -ServicePrincipalNames http/<FederationServiceName>

     This example creates a new gMSA account named FSgMSA for the Federation Service
     named adfs.contoso.com. The Federation Service name is the value that's visible to
     clients.

        PowerShell

        New-ADServiceAccount -Name FSgMSA -DnsHostName adfs.contoso.com -
        ServicePrincipalNames http/adfs.contoso.com

Step 3b: Configure the AD FS server
To configure the AD FS server, you can use Server Manager or Windows PowerShell.

<!-- p.1480 -->

To use Server Manager, following these steps:

   1. If you left the Add Roles and Features Wizard open on the AD FS server from Step 2:
     Deploy an AD FS server, you can click the Configure the federation service on this server
     link on the Installation progress page.

     If you closed the Add Roles and Features Wizard or you used Windows PowerShell to
     install AD FS, you can get to the same place in Server Manager by clicking Notifications,
     and then clicking Configure the federation service on this server in the Post-
     deployment Configuration warning.

   2. The Active Directory Federation Services Wizard opens. On the Welcome page, verify
     Create the first federation server in a federation server farm is selected, and then click
     Next.
