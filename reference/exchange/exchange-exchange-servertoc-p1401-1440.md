---
title: "Exchange Server — pages 1401-1440"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p1401-1440
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p1401-1440
family: exchange
documentKind: "doc"
abstract: "Create an app configuration policy for Outlook for iOS and Android using Microsoft Intune If you're using Microsoft Intune as your mobile device management provider, the following steps allow you to deploy account configuration settings for your on-premises mailboxes that use ba"
---

# Exchange Server — pages 1401-1440

<!-- p.1401 -->

Create an app configuration policy for Outlook for
iOS and Android using Microsoft Intune
If you're using Microsoft Intune as your mobile device management provider, the following
steps allow you to deploy account configuration settings for your on-premises mailboxes that
use basic authentication with the ActiveSync protocol. Once the configuration is created, you
can assign the settings to groups of users, as detailed in the next section, Assign configuration
settings.

  ７ Note

  If users in your organization use both iOS and Android for Work devices, you'll need to
  create a separate app configuration policy for each platform.

   1. In the Microsoft Intune admin center at https://intune.microsoft.com       , select Apps >
     Policy section > App configuration policies. Or, to go directly to the App configuration
     policies page, use
     https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/~/appC
     onfig .

   2. On the App Configuration policies page, select Add > Managed devices to start the app
     configuration policy wizard.

   3. On the Basics tab of the Create app configuration policy page that opens, configure the
     following settings:

            Name: Enter a unique, descriptive name.

            Description: Enter an optional description for the app configuration settings.

            Platform: Select" iOS/iPadOS or Android Enterprise.

            Targeted app: Select Select app. In the Associated app flyout that opens, select
            Outlook.

               Tip

              If Outlook isn't listed as an available app, add it by following the instructions in
              Add Android store apps to Microsoft Intune and How to add iOS store apps
              to Microsoft Intune.

<!-- p.1402 -->

       When you're finished on the Associated app flyout, select OK to return to the Basics
       tab of the Create app configuration policy page.

  When you're finished on the Basics tab, select Next.

    ７ Note

    If Outlook is not listed as an available app, then you must add it by following the
    instructions in Add Android store apps to Microsoft Intune and How to add iOS
    store apps to Microsoft Intune.

4. On the Settings tab, configure the following settings:

       Email account configuration section: Configure the following settings:
          Configuration settings section
             Configuration settings format: Select Use configuration designer. This
             selection causes many more settings to appear. The key value pairs used in
             this section are defined in the section Key value pairs.
             Email account configuration section:
                Configure email account settings: Select Yes to deploy account setup
                configuration:
                Authentication type: Select Basic authentication. This value is required for
                on-premises accounts that don't use hybrid modern authentication.
                Username attribute from Microsoft Entra ID: Select one of the following
                values:
                   User Principal Name
                   sAMAccountName: This value requires the NetBIOS domain name in the
                   Account domain field.
                Email address attribute from Microsoft Entra ID: Select Primary SMTP
                Address.
                   Email server: Enter the Exchange ActiveSync externally accessible domain
                   name.
                   Email account name: Enter a descriptive value for the account.
       General app configuration section: If you want to deploy general app configuration
       settings, configure the desired settings accordingly:

          Focused Inbox: Select one of the following values:
             Not configured (default)
             On (app default)
             Off

          Require Biometrics to access the app: Select one of the following values:

<!-- p.1403 -->

           Not configured (default)

           On

           Off (app default)

           The values On or Off activate the Allow user to change setting option:
             Select Yes (app default) to allow the user to change the setting.
             Select No to prevent users from changing the setting. This setting is only
             available in Outlook for iOS.

        Save Contacts: Select one of the following values:

           Not configured (default)

           On

           Off (app default)

           The values On or Off active the Allow user to change setting option:
             Select Yes (app default) to allow the user to change the setting.
             Select No to prevent users from changing the setting.

        Default app signature: Select one of the following values:
           Not configured (default)
           On (app default)
           Off

        Block external images: Select one of the following values:

           Not configured (default)

           On

           Off (app default)

           The values On or Off active the Allow user to change setting option:
             Select Yes (app default) to allow the user to change the setting.
             Select No to prevent users from changing the setting.

        Organize mail by thread: Select one of the following values:
           Not configured (default)
           On (app default)
           Off

When you're finished on the Settings tab, select Next.

<!-- p.1404 -->

   5. On the Assignments tab, select who the policy applies to. You assign the settings to
     groups of users in Microsoft Entra ID. When a user has the Microsoft Outlook app
     installed, the app is managed by the settings you configured.

             Included groups section: Select and configure one of the following options:
               Add groups
               Add all users
               Add all devices

             Excluded groups section: Select Add groups to exclude groups from the policy.

                Tip

               You can't mix user groups and device groups to include and exclude.

     When you're finished on the Assignments tab, select Next.

   6. On the Review + create tab, review your selections.

     Select Previous or use the tabs to go back and make changes.

     When you're finished on the Review + create tab, select Create

Back on the App configuration policies page, the newly created configuration policy is
displayed.

Assign configuration settings
You assign the settings to groups of users in Microsoft Entra ID. When a user has the Microsoft
Outlook app installed, the app is managed by the settings you have specified.

   1. On the App configuration policies page at
     https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/AppsMenu/~/appC
     onfig , select the policy from the list by clicking on the Name value.

   2. In the policy details page that opens, select Properties from the Manage section.

   3. On the Properties page that opens, select Edit in the Assignments section.

   4. On the Assignments tab of the Edit app configuration policy page that opens, configure
     the following settings:

             Included groups section: Select and configure one of the following options:
               Add groups

<!-- p.1405 -->

              Add all users
              Add all devices

            Excluded groups section: Select Add groups to exclude groups from the policy.

               Tip

              You can't mix user groups and device groups to include and exclude.

       When you're finished on the Assignments tab, select Review + save.

Key value pairs
When you create an app configuration policy in the Azure portal or through your UEM
provider, you need the following key value pairs:

                                                                                     ﾉ     Expand table

 Key                                                   Values

 com.microsoft.outlook.EmailProfile.EmailAccountName   This value specifies the display name email
                                                       account as it appears to users on their devices.
                                                       Value type: String
                                                       Accepted values: Display Name
                                                       Default if not specified: <blank>
                                                       Required: Yes
                                                       Example: user
                                                       Intune Token*: {{username}}

 com.microsoft.outlook.EmailProfile.EmailAddress       This value specifies the email address to be
                                                       used for sending and receiving mail.
                                                       Value type: String
                                                       Accepted values: Email address
                                                       Default if not specified: <blank>
                                                       Required: Yes
                                                       Example: user@contoso.com
                                                       Intune Token*: {{mail}}

 com.microsoft.outlook.EmailProfile.EmailUPN           This value specifies the User Principal Name or
                                                       username for the email profile that's used to
                                                       authenticate the account.
                                                       Value type: String
                                                       Accepted values: UPN Address or username
                                                       Default if not specified: <blank>
                                                       Required: Yes

<!-- p.1406 -->

    Key                                                       Values

                                                              Example: userupn@contoso.com
                                                              Intune Token*: {{userprincipalname}}

    com.microsoft.outlook.EmailProfile.ServerAuthentication   This value specifies the authentication method
                                                              for the user.
                                                              Value type: String
                                                              Accepted values: 'Username and Password'
                                                              Default if not specified: 'Username and
                                                              Password'
                                                              Required: No
                                                              Example: 'Username and Password'

    com.microsoft.outlook.EmailProfile.ServerHostName         This value specifies the host name of your
                                                              Exchange server.
                                                              Value type: String
                                                              Accepted values: ActiveSync FQDN
                                                              Default if not specified: <blank>
                                                              Required: Yes
                                                              Example: mail.contoso.com

    com.microsoft.outlook.EmailProfile.AccountDomain          This value specifies the user's account domain.
                                                              Value type: String
                                                              Accepted values: Domain
                                                              Default if not specified: <blank>
                                                              Required: No
                                                              Example: contoso

    com.microsoft.outlook.EmailProfile.AccountType            This value specifies the account type being
                                                              configured based on the authentication model.
                                                              Value type: String
                                                              Accepted values: BasicAuth
                                                              Default if not specified: BasicAuth
                                                              Required: No
                                                              Example: BasicAuth

*
    Microsoft Intune users can use tokens that will expand to the correct value according to the
enrolled user. See Add app configuration policies for managed iOS devices for more
information.

<!-- p.1407 -->

Passwords and security in Outlook for iOS
and Android for Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

This article describes how passwords and security work in Outlook for iOS and Android with
Exchange Server when using Basic authentication with the Exchange ActiveSync protocol.

  ） Important

  Outlook for iOS and Android supports hybrid Modern Authentication for on-premises
  mailboxes which eliminates the need to leverage basic authentication. The information
  contained in this article only pertains to basic authentication. For more information, please
  see Using hybrid Modern Authentication with Outlook for iOS and Android.

Creating an account and protecting passwords
The first time the Outlook app for iOS and Android is run in an Exchange on-premises
environment, Outlook generates a random AES-128 key. This key is known as the device key
and is stored only on the user's device.

When a user logs onto Exchange with Basic authentication, the username, password, and a
unique AES-128 device key are sent from the user's device to the Outlook cloud service over a
TLS connection, where the device key is held in runtime compute memory. After verifying the
password with the Exchange server, the Microsoft 365 or Office 365-based architecture uses
the device key to encrypt the password, and the encrypted password is then stored in the
service. The device key, meanwhile, is wiped from memory and never stored in the Microsoft
365 or Office 365-based architecture (the key is only stored on the user's device).

Next, when a user attempts to connect to Exchange to retrieve mailbox data, the device key is
again passed from the device to the Microsoft 365 or Office 365-based architecture over a TLS-
secured connection, where it is used to decrypt the password in runtime compute memory.
Once decrypted, the password is never stored in the service or written to a local storage disk,
and the device key is once again wiped from memory.

After the Microsoft 365 or Office 365-based architecture has decrypted the password at
runtime, the service can then connect to the Exchange server to synchronize mail, calendar, and
other mailbox data. As long as the user continues to open and use Outlook periodically, the

<!-- p.1408 -->

Microsoft 365 or Office 365-based architecture will keep a copy of the user's decrypted
password in memory to keep the connection to the Exchange server active.

Compliance considerations when sending
passwords
Before you enable anything that allows for the transmission of passwords from your on-
premises Exchange environment, be sure to consider the possible ramifications. For example,
transmitting passwords to Microsoft 365 or Office 365-based architecture might result in your
inability to meet the requirements of PCI-DSS or ISO/IEC 27001.

Furthermore, if you connect and synchronize email, calendars, and other email-related data,
you might run into issues of compliance with GDPR, which restricts the private information that
you can transmit without owner consent. This information might be contained in and found
within emails, calendar items, and so on.

Account inactivity and flushing passwords from
memory
After three days of inactivity, the Microsoft 365 or Office 365-based architecture will flush a
decrypted password from memory. With the decrypted password flushed, the architecture is
unable to access a user's mailbox on-premises. The encrypted password remains stored in the
Microsoft 365 or Office 365-based architecture, but decrypting it again isn't possible without
the device key, which is only available from the user's device.

There are three ways a user account can become inactive:

     Outlook for iOS and Android is uninstalled by the user.

     Background app refresh is disabled in the Settings options, and then a force-quit is
     applied to Outlook.

     No internet connection is available on the device, preventing Outlook from synchronizing
     with Exchange.

  ７ Note

  Outlook will not become inactive simply because the user does not open the app for
  some time, such as over a weekend or while on vacation. As long as background app

<!-- p.1409 -->

  refresh is enabled (which is the default setting for Outlook for iOS and Android), functions
  like push notifications and background synchronization of email will count as activity.

Flushing encrypted password and synchronized mailbox data from Microsoft 365 or Office
365

The Microsoft 365 or Office 365-based architecture flushes, or deletes, inactive accounts on a
weekly schedule. After a user account becomes inactive, the architecture will flush both the
encrypted password and all of the user's synchronized mailbox content out of the service.

Device and service security combination

Each user's unique device key is never stored in the Microsoft 365 or Office 365-based
architecture, and a user's Exchange password is never stored on the device. This architecture
means that for a malicious party to gain access to a user's password, they would need both
unauthorized access to the Microsoft 365 or Office 365-based architecture and physical access
to that user's device.

By enforcing PIN policies and encryption on devices in your organization, the malicious party
would also have to defeat a device's encryption to get access to the device key. This would all
have to take place before the user noticed that the device was compromised and could request
a remote wipe for the device.

Password security FAQ
The following are frequently asked questions regarding security design and settings for
Outlook for iOS and Android when used with Basic authentication.

Are user credentials stored in the Microsoft 365 or Office 365-
based architecture if I block Outlook from accessing my
Exchange Server?
If you have chosen to block Outlook for iOS and Android from accessing your on-premises
Exchange servers, the initial connection will be rejected by Exchange. User credentials will not
be stored by the Outlook cloud service and the credentials presented in the failed connection
attempt are immediately flushed from memory.

How is the unique device key and user password encrypted in
transit to the Microsoft 365 or Office 365-based architecture?

<!-- p.1410 -->

All communication between the Outlook app and the Microsoft 365 or Office 365-based
architecture is through an encrypted TLS connection. The Outlook app is capable of connecting
with the Microsoft 365 or Office 365-based architecture and nothing else.

How do I remove a user's credentials and mailbox information
from the Microsoft 365 or Office 365-based architecture?
Have the user uninstall Outlook for iOS and Android on all devices. All data will be removed
from the Microsoft 365 or Office 365-based architecture in approximately 3-7 days.

The app is closed or uninstalled, but I still see it connecting to
my Exchange server. How is this happening?
The Microsoft 365 or Office 365-based architecture decrypts user passwords in runtime
compute memory and then uses the decrypted passwords to connect to Exchange. Since the
architecture is connecting to Exchange on behalf of the device to fetch and cache mailbox
data, it can continue for a short period until the service detects that Outlook is no longer
requesting data.

If a user uninstalls the app from their device without first using the Delete Account option, the
Microsoft 365 or Office 365-based architecture will stay connected to your Exchange server
until the account becomes inactive, as described above in "Account inactivity and flushing
passwords from memory." To stop this activity, follow Option 1 or Option 3 from the above
FAQ, or block the app, as described in Blocking Outlook for iOS and Android.

Is a user password less secure in Outlook for iOS and Android
than when using other Exchange ActiveSync clients?
No. EAS clients generally save user credentials locally on the user's device. This means a stolen
or compromised device could result in a malicious party gaining access to the user's password.
With the security design of Outlook for iOS and Android, a malicious party would need
unauthorized access to the Microsoft 365 or Office 365-based architecture and have physical
access to a user's device.

What happens if a user attempts to use Outlook for iOS and
Android after their data has been deleted from the Outlook
cloud service?
If a user account becomes inactive (such as by disabling background app refresh on the device
or having their device disconnected from the Internet for some time), the Outlook app will

<!-- p.1411 -->

reconnect to the Microsoft 365 or Office 365-based architecture the next time the app is
launched, and the password encryption and email caching process will restart. This is all
transparent to the user.

Is there a way to prevent the use of Basic authentication for
on-premises mailboxes with Outlook for iOS and Android?
Yes, you can deploy hybrid Modern Authentication. For more information, see Using hybrid
Modern Authentication with Outlook for iOS and Android.

<!-- p.1412 -->

Managing devices for Outlook for iOS and
Android for Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

  ） Important

  Outlook for iOS and Android supports hybrid Modern Authentication for on-premises
  mailboxes which eliminates the need to leverage basic authentication. The information
  contained in this article only pertains to basic authentication. For more information, please
  see Using hybrid Modern Authentication with Outlook for iOS and Android.

Microsoft recommends Exchange ActiveSync for managing the mobile devices that are used to
access Exchange mailboxes in your on-premises environment. Exchange ActiveSync is a
Microsoft Exchange synchronization protocol that lets mobile phones access an organization's
information on a server that's running Microsoft Exchange.

This article focuses on specific Exchange ActiveSync features and scenarios for mobile devices
running Outlook for iOS and Android when authenticating with Basic authentication. Complete
information about the Microsoft Exchange synchronization protocol is available in Exchange
ActiveSync. In addition, there is information on the Office Blog   detailing password
enforcement and other benefits of using Exchange ActiveSync with devices running Outlook for
iOS and Android.

Mobile device mailbox policy
Outlook for iOS and Android supports the following mobile device mailbox policy settings in
Exchange on-premises:

      Device encryption enabled

      Min password length (only on Android)

      Password enabled

      Allow Bluetooth (used to manage the Outlook for Android wearable app)

         When AllowBluetooth is enabled (default behavior) or configured for HandsfreeOnly,
         wearable synchronization between Outlook on the Android device and Outlook on the
         wearable is allowed for the work or school account.

<!-- p.1413 -->

        When AllowBluetooth is disabled, Outlook for Android will disable synchronization
        between Outlook on the Android device and Outlook on the wearable for the specified
        work or school account (and delete any data previously synced for the account).
        Disabling the synchronization is controlled entirely within Outlook itself; Bluetooth is
        not disabled on the device or wearable nor is any other wearable app affected.

  ７ Note

  Outlook for Android will roll out support for the AllowBluetooth setting beginning at the
  end of August.

For information on how to create or modify an existing mobile device mailbox policy, see
Mobile device mailbox policies.

PIN lock and device encryption
If your organization's Exchange ActiveSync policy requires a password on mobile devices in
order for users to synchronize email, Outlook will enforce this policy at the device level. This
works differently between iOS devices and Android devices, based on the available controls
provided by Apple and Google.

On iOS devices, Outlook checks to make sure a passcode or PIN is properly set. In the event a
passcode is not set, Outlook prompts users to create a passcode in iOS settings. Until the
passcode is setup, the user will be unable to access Outlook for iOS.

On Android devices, Outlook will enforce screen lock rules. In addition, Google provides
controls that allow Outlook for Android to comply with Exchange policies regarding password
length and complexity, and the number of allowable screen-unlock attempts before wiping the
phone. Outlook for Android will also encourage storage encryption if it is not enabled, guiding
users through this process with a step-by-step walkthrough.

iOS and Android devices that do not support these password security settings will not be able
to connect to an Exchange mailbox.

Device encryption
iOS devices are shipped with built-in encryption, which Outlook uses once the passcode is
enabled to encrypt all the data Outlook stores locally on the iOS device. Therefore, iOS devices
with a PIN are encrypted whether or not this is required by an ActiveSync policy.

Outlook for Android supports device encryption via Exchange mobile device mailbox policies.
However, prior to Android 7.0, the availability and implementation of this process varies by

<!-- p.1414 -->

Android OS version and device manufacturer, which allow the user to cancel out during the
encryption process. With changes that Google introduced to Android 7.0, Outlook for Android
is now able to enforce encryption on devices running Android 7.0 or later. Users with devices
running those operating systems will not be able to cancel out of the encryption process.

Even if the Android device is unencrypted and an attacker is in possession of the device, as
long as a device PIN is enabled, the Outlook database remains inaccessible. This is true even
with USB debugging enabled and the Android SDK installed. If an attacker attempts to root the
device to bypass the PIN to gain access to this information, the rooting process wipes all device
storage and removes all Outlook data. If the device is unencrypted and rooted by the user prior
to being stolen, it is possible for an attacker to gain access to the Outlook database by
enabling USB debugging on the device and plugging the device into a computer with the
Android SDK installed.

Remote wipe with Exchange ActiveSync
Exchange ActiveSync enables administrators to remotely wipe devices, such as if they become
compromised or lost/stolen. With Outlook for iOS and Android, a remote wipe only wipes data
within the Outlook app itself and does not trigger a full device wipe.

See Perform a remote wipe on a mobile phone for more information.

Device access policy
Outlook for iOS and Android should be enabled by default, but in some existing Exchange on-
premises environments the app may be blocked for a variety of reasons. Once an organization
decides to standardize how users access Exchange data and use Outlook for iOS and Android
as the only email app for end users, you can configure blocks for other email apps running on
users' iOS and Android devices. You have two options for instituting these blocks within
Exchange on-premises: the first option blocks all devices and only allows usage of Outlook for
iOS and Android; the second option allows you to block individual devices from using the
native Exchange ActiveSync apps.

  ７ Note

  Because device IDs are not governed by any physical device ID, they can change without
  notice. When this happens, it can cause unintended consequences when device IDs are
  used for managing user devices, as existing 'allowed' devices may be unexpectedly
  blocked or quarantined by Exchange. Therefore, Microsoft recommends administrators

<!-- p.1415 -->

  only set mobile device access policies that allow/block devices based on device type or
  device model.

Option 1: Block all email apps except Outlook for iOS and Android

You can define a default block rule and then configure an allow rule for Outlook for iOS and
Android, and for Windows devices, using the following Exchange on-premises PowerShell
commands. This configuration will prevent any Exchange ActiveSync native app from
connecting, and will only allow Outlook for iOS and Android.

   1. Create the default block rule:

        PowerShell

        Set-ActiveSyncOrganizationSettings -DefaultAccessLevel Block

   2. Create an allow rule for Outlook for iOS and Android

        PowerShell

        New-ActiveSyncDeviceAccessRule -Characteristic DeviceModel -QueryString
        "Outlook for iOS and Android" -AccessLevel Allow

   3. Optional: Create rules that allow Outlook on Windows devices for Exchange ActiveSync
     connectivity (WindowsMail refers to the Mail app included in Windows 10):

        PowerShell

        New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString
        "WindowsMail" -AccessLevel Allow

Option 2: Block native Exchange ActiveSync apps on Android and iOS
devices
Alternatively, you can block native Exchange ActiveSync apps on specific Android and iOS
devices or other types of devices.

   1. Confirm that there are no Exchange ActiveSync device access rules in place that block
     Outlook for iOS and Android:

        PowerShell

<!-- p.1416 -->

    Get-ActiveSyncDeviceAccessRule | where {$_.AccessLevel -eq "Block" -and
    $_.QueryString -like "Outlook*"} | ft Name,AccessLevel,QueryString -auto

  If any device access rules that block Outlook for iOS and Android are found, type the
  following to remove them:

    PowerShell

    Get-ActiveSyncDeviceAccessRule | where {$_.AccessLevel -eq "Block" -and
    $_.QueryString -like "Outlook*"} | Remove-ActiveSyncDeviceAccessRule

2. You can block most Android and iOS devices with the following commands:

    PowerShell

    New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString
    "Android" -AccessLevel Block
    New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString "iPad"
    -AccessLevel Block
    New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString
    "iPhone" -AccessLevel Block
    New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString "iPod"
    -AccessLevel Block

3. Not all Android device manufacturers specify "Android" as the DeviceType. Manufacturers
  may specify a unique value with each release. In order to find other Android devices that
  are accessing your environment, execute the following command to generate a report of
  all devices that have an active Exchange ActiveSync partnership:

    PowerShell

    Get-MobileDevice | Select-Object DeviceOS,DeviceModel,DeviceType | Export-CSV
    c:\temp\easdevices.csv

4. Create additional block rules, depending on your results from Step 3. For example, if you
  find your environment has a high usage of HTCOne Android devices, you can create an
  Exchange ActiveSync device access rule that blocks that particular device, forcing the
  users to use Outlook for iOS and Android. In this example, you would type:

    PowerShell

    New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString
    "HTCOne" -AccessLevel Block

<!-- p.1417 -->

  ７ Note

  The QueryString parameter does not accept wildcards or partial matches.

Additional resources:

     New-ActiveSyncDeviceAccessRule

     Get-MobileDevice

     Set-ActiveSyncOrganizationSettings

Blocking Outlook for iOS and Android
Every Exchange organization has different policies regarding security and device management.
If an organization decides that Outlook for iOS and Android doesn't meet their needs or is not
the best solution for them, administrators have the ability to block the app. Once the app is
blocked, mobile Exchange users in your organization can continue accessing their mailboxes by
using the built-in mail applications on iOS and Android.

The New-ActiveSyncDeviceAccessRule cmdlet has a Characteristic parameter, and there are
three Characteristic options that administrators can use to block the Outlook for iOS and
Android app. The options are UserAgent, DeviceModel, and DeviceType. In the two blocking
options described in the following sections, you will use one or more of these characteristic
values to restrict the access that Outlook for iOS and Android has to the mailboxes in your
organization.

The values for each characteristic are displayed in the following table:

                                                                                  ﾉ    Expand table

 Characteristic         String for iOS                       String for Android

 DeviceModel            Outlook for iOS and Android          Outlook for iOS and Android

 DeviceType             Outlook                              Outlook

 UserAgent              Outlook-iOS-Android/1.0              Outlook-iOS-Android/1.0

With the New-ActiveSyncDeviceAccessRule cmdlet, you can define a device access rule, using
either the DeviceModel or DeviceType characteristic. In both cases, the access rule blocks
Outlook for iOS and Android across all platforms, and will prevent any device, on both the iOS
platform and Android platform, from accessing an Exchange mailbox via the app.

<!-- p.1418 -->

The following are two examples of a device access rule. The first example uses the DeviceModel
characteristic; the second example uses the DeviceType characteristic.

  PowerShell

  New-ActiveSyncDeviceAccessRule -Characteristic DeviceType -QueryString "Outlook" -
  AccessLevel Block

  PowerShell

  New-ActiveSyncDeviceAccessRule -Characteristic DeviceModel -QueryString "Outlook
  for iOS and Android" -AccessLevel Block

<!-- p.1419 -->

Default settings for Exchange virtual
directories in Exchange Server
Article • 04/30/2025

APPLIES TO:          2016    2019      Subscription Edition

Exchange Server 2016 and Exchange Server 2019 automatically configure multiple Internet
Information Services (IIS) virtual directories during the server installation. The tables in the
following sections show the settings for the Client Access (frontend) services on Mailbox
servers and the default IIS authentication and Secure Sockets Layer (SSL) settings.

Client Access services (frontend) on Mailbox
servers
The following table lists the default settings in the Client Access services (the default web site)
on Exchange Mailbox servers.

                                                                                    ﾉ   Expand table

 Virtual directory      Authentication method           SSL settings         Management method

 Default Web Site       Anonymous                       Required             IIS management console

 API1                   Anonymous authentication        SSL required
                        Windows authentication          Requires 128-bit
                                                        encryption

 aspnet_client          Anonymous authentication        SSL required         IIS management console
                                                        Requires 128-bit
                                                        encryption

 Autodiscover           Anonymous authentication        SSL required         EAC or Exchange
                        Basic authentication            Requires 128-bit     Management Shell
                        Windows authentication          encryption

 ecp                    Anonymous authentication        SSL required         EAC or Exchange
                        Basic authentication            Requires 128-bit     Management Shell
                                                        encryption

 EWS                    Anonymous authentication        SSL required         EAC or Exchange
                        Windows authentication          Requires 128-bit     Management Shell
                                                        encryption

 MAPI                   Windows authentication          SSL required         EAC or Exchange
                                                        Requires 128-bit     Management Shell

<!-- p.1420 -->

    Virtual directory   Authentication method                 SSL settings         Management method

                                                              encryption

    Microsoft-Server-   Basic authentication                  SSL required         EAC or Exchange
    ActiveSync                                                Requires 128-bit     Management Shell
                                                              encryption

    OAB                 Windows authentication                SSL required         EAC or Exchange
                                                              Requires 128-bit     Management Shell
                                                              encryption

    owa                 Basic authentication                  SSL required         EAC or Exchange
                                                              Requires 128-bit     Management Shell
                                                              encryption

    PowerShell          By default, all authentication        Not required         EAC or Exchange
                        methods are disabled.                                      Management Shell

    Rpc                 Basic authentication                  Not required         EAC or Exchange
                        Windows authentication                                     Management Shell

1
    The API virtual directory is available in Exchange 2016 CU3 or newer.

Back End Virtual Directories on Mailbox servers
The following table lists the default settings in the back end services on Exchange Mailbox
servers.

                                                                                           ﾉ   Expand table

    Virtual directory   Authentication           SSL settings           Management method
                        method

    Exchange Back End   Anonymous                SSL required           This virtual directory shouldn't be
                        authentication           Requires 128-bit       configured by the user.
                                                 encryption

    API1                Anonymous                SSL required           This virtual directory shouldn't be
                        authentication           Requires 128-bit       configured by the user.
                        Windows                  encryption
                        authentication

    Autodiscover        Anonymous                SSL required           This virtual directory shouldn't be
                        authentication           Requires 128-bit       configured by the user.
                        Windows                  encryption
                        authentication

<!-- p.1421 -->

    Virtual directory   Authentication         SSL settings       Management method
                        method

    ecp                 Anonymous              SSL required       This virtual directory shouldn't be
                        authentication         Requires 128-bit   configured by the user.
                        Windows                encryption
                        authentication

    EWS                 Anonymous              SSL required       This virtual directory shouldn't be
                        authentication         Requires 128-bit   configured by the user.
                        Windows                encryption
                        authentication

    Microsoft-Server-   Basic authentication   SSL required       This virtual directory shouldn't be
    ActiveSync                                 Requires 128-bit   configured by the user.
                                               encryption

    OAB                 Windows                SSL required       This virtual directory shouldn't be
                        authentication         Requires 128-bit   configured by the user.
                                               encryption

    owa                 Anonymous              SSL required       This virtual directory shouldn't be
                        authentication         Requires 128-bit   configured by the user.
                        Windows                encryption
                        authentication

    PowerShell          Windows                SSL required       This virtual directory shouldn't be
                        authentication         Requires 128-bit   configured by the user.
                                               encryption

    Rpc                 Windows                Not required       This virtual directory shouldn't be
                        authentication                            configured by the user.

    RpcWithCert         Windows                Not required       This virtual directory shouldn't be
                        authentication                            configured by the user.

1
    The API virtual directory is available in Exchange 2016 CU3 or newer.

See also
Virtual directory management

<!-- p.1422 -->

Outlook on the web in Exchange Server
Article • 05/09/2025

APPLIES TO:         2016   2019      Subscription Edition

The user interface in Outlook on the web (formerly known as Outlook Web App) for Exchange
Server has been optimized and simplified for use with phones and tablets. Supported web
browsers give users access to more Outlook features. Unsupported web browsers give users
the light version of Outlook on the web that has less features. For more information about
features and supported web browsers, see Outlook on the web (formerly Outlook Web App)
and Outlook on the web (formerly Outlook Web App).

When you install Exchange Server, Outlook on the web is automatically available for internal
users at https://<ServerName>/owa (for example, https://mailbox01.contoso.com/owa ). But,
you'll likely want to configure Outlook on the web for external access (for example,
https://mail.contoso.com/owa ). For more information, see Step 4: Configure external URLs in

Configure mail flow and client access on Exchange servers.

In an Outlook 2010 or later installation that's connected to an Exchange mailbox, you can
typically see the Outlook on the web URL at File > Info > Account Information in the Account
Settings section.

Outlook on the web is provided by the Client Access (frontend) services on Mailbox servers. In
Exchange Server, Client Access services are part of the Mailbox server, so you can't configure a
standalone Client Access server like you could in previous versions of Exchange. For more
information, see Client access protocol architecture.

If you're looking for information about Outlook on the web in Microsoft 365 or Office 365, see
Using email in Outlook on the web .

<!-- p.1423 -->

Administrative tasks for managing Outlook on the
web
The configuration and management tasks that are documented for Outlook on the web in
Outlook 2016 are listed in the following table.

                                                                                         ﾉ   Expand table

 Topic                                        Description

 View or configure Outlook on the web         View and configure the properties of Outlook on the web for
 virtual directories in Exchange Server       all users that connect to the server.

 Configure http to https redirection for      Redirect Outlook on the web unencrypted http requests to
 Outlook on the web in Exchange Server        https.

 Create a theme for Outlook on the web in     Outlook on the web comes with built-in themes that define
 Exchange Server                              the colors and icons that are used in Outlook on the web, but
                                              you can also create your own themes.

 Customize the Outlook on the web sign-       Customize key pages in Outlook on the web.
 in, language selection, and error pages in
 Exchange Server

 Use AD FS claims-based authentication        Centralize Outlook on the web authentication by using Active
 with Outlook on the web                      Directory Federation Services.

<!-- p.1424 -->

Enable or disable Outlook on the web
access to mailboxes in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019      Subscription Edition

Administrators can use the Exchange admin center (EAC) or the Exchange Management Shell
to enable or disable Outlook on the web access to a mailbox. By default, users can access their
mailboxes by using Outlook on the web. When you disable Outlook on the web access to
mailboxes, users can still access their mailboxes by using Outlook or other email clients.

For additional management tasks related to user access to mailboxes, see these topics:

      Enable or disable Exchange ActiveSync access to mailboxes in Exchange Server

      Enable or disable POP3 or IMAP4 access to mailboxes in Exchange Server

      Enable or disable MAPI access to mailboxes in Exchange Server

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      For more information about accessing and using the EAC, see Exchange admin center in
      Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Client Access user settings" entry
      in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.1425 -->

Enable or disable Outlook on the web access to a
single mailbox

Use the EAC to Enable or disable Outlook on the web access
to a single mailbox
 1. In the EAC, go to Recipients > Mailboxes.

 2. In the list of mailboxes, find the mailbox that you want to modify. You can:

        Scroll through the list of mailboxes.

        Click Search     and enter part of the user's name, email address, or alias.

        Click More options      > Advanced search to find the mailbox.

   Once you've found the mailbox that you want to modify, select it, and then click Edit      .

 3. On the mailbox properties page that opens, click Mailbox features.

 4. In the Email Connectivity section, configure one of these settings:

        If you see Outlook on the web: Enabled, click Disable to disable it, and then click
        Yes in the warning message that appears.

        If you see Outlook on the web: Disabled, click Enable to enable it.

   When you're finished, click Save.

<!-- p.1426 -->

Use the Exchange Management Shell to enable or disable
Outlook on the web access to a mailbox
To enable or disable Outlook on the web access to a single mailbox, use this syntax:

  PowerShell

  Set-CasMailbox -Identity <MailboxIdentity> -OWAEnabled <$true | $false>

This example disables Outlook on the web access to the mailbox named Yan Li.

  PowerShell

  Set-CasMailbox -Identity "Yan Li" -OWAEnabled $false

This example enables Outlook on the web access to the mailbox named Elly Nkya.

  PowerShell

  Set-CasMailbox -Identity "Elly Nkya" -OWAEnabled $true

For detailed syntax and parameter information, see Set-CASMailbox.

Enable or disable Outlook on the web access to
multiple mailboxes

Use the EAC to enable or disable Outlook on the web access
to multiple mailboxes
   1. In the EAC, go to Recipients > Mailboxes.

   2. In the list of mailboxes, find the mailboxes that you want to modify. You can:

           Scroll through the list of mailboxes.

           Click Search    and enter part of the user's name, email address, or alias.

           Click More options      > Advanced search to find the mailbox.

   3. In the list of mailboxes, select multiple mailboxes of the same type (for example, User)
     from the list. For example:

<!-- p.1427 -->

          Select a mailbox, hold down the Shift key, and select another mailbox that's farther
          down in the list.

          Hold down the CTRL key as you select each mailbox.

     After you select multiple mailboxes of the same type, the title of the details pane changes
     to Bulk Edit.

  4. In the details pane, scroll down to Outlook on the web, click Enable or Disable, and then
     click OK in the warning message that appears.

Use the Exchange Management Shell to enable or disable
Outlook on the web access to multiple mailboxes
You can use the Get-Mailbox, Get-User or Get-Content cmdlets to identify the mailboxes that
you want to modify. For example:

     Use the OrganizationalUnit parameter to filter the mailboxes by organizational unit (OU).

     Use the Filter parameter to create OPATH filters that identify the mailboxes. For more
     information, see Filterable Properties for the -Filter Parameter.

     Use a text file to specify the mailboxes. The text file contains one mailbox (email address,
     name, or other unique identifier) on each line like this:

       ebrunner@tailspintoys.com
       fapodaca@tailspintoys.com

<!-- p.1428 -->

       glaureano@tailspintoys.com
       hrim@tailspintoys.com

This example disables Outlook on the web access to all user mailboxes in the North
America\Finance OU.

  PowerShell

  $NAFinance = Get-Mailbox -OrganizationalUnit "OU=Marketing,OU=North
  America,DC=contoso,DC=com" -Filter "RecipientTypeDetails -eq 'UserMailbox'" -
  ResultSize Unlimited; $NAFinance | foreach {Set-CasMailbox $_.Identity -
  OWAEnabled $false}

This example disables Outlook on the web access to all user mailboxes in the Engineering
department in Washington state.

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Set-CasMailbox -OWAEnabled $false

This example uses the text file C:\My Documents\Accounts.txt to disable Outlook on the web
access to the specified mailboxes.

  PowerShell

  Get-Content "C:\My Documents\Accounts.txt" | foreach {Set-CasMailbox $_ -
  OWAEnabled $false}

For detailed syntax and parameter information, see Get-Mailbox and Get-User.

How do you know this worked?
To verify that you've successfully enabled or disabled Outlook on the web access to a mailbox,
do any of these steps:

     In the EAC, go to Recipients > Mailboxes > select the mailbox > click Edit    > Mailbox
     features and verify the Outlook on the web value in the Email Connectivity section.

<!-- p.1429 -->

In the Exchange Management Shell, replace <MailboxIdentity> with the identity of the
mailbox (for example, name, alias, or email address), and run this command:

  PowerShell

  Get-CasMailbox -Identity "<MailboxIdentity>"

Use the same filter that you used to identify the mailboxes, but use the Get-CasMailbox
cmdlet instead of Set-CasMailbox. For example:

  PowerShell

  Get-User -Filter "RecipientType -eq 'UserMailbox' -and Department -like
  'Engineering*' -and StateOrProvince -eq 'WA'" | Get-CasMailbox

In the Exchange Management Shell, run this command to show all mailboxes where
Outlook on the web access is disabled:

  PowerShell

  Get-CasMailbox -ResultSize unlimited -Filter "OWAEnabled -eq `$false"

<!-- p.1430 -->

View or configure Outlook on the web
virtual directories in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

You can use the Exchange admin center (EAC) or the Exchange Management Shell to view or
modify the properties of an Outlook on the web (formerly known as Outlook Web App) virtual
directory. Although the name has changed to Outlook on the web, the name of the virtual
directory is still "owa".

What do you need to know before you begin?
      Estimated time to complete each procedure: 10 minutes.

      For more information about the EAC, see .Exchange admin center in Exchange Server. To
      learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      Secure Sockets Layer (SSL) is being replaced by Transport Layer Security (TLS) as the
      protocol that's used to encrypt data sent between computer systems. They're so closely
      related that the terms "SSL" and "TLS" (without versions) are often used interchangeably.
      Because of this similarity, references to "SSL" in Exchange topics, the Exchange admin
      center, and the Exchange Management Shell have often been used to encompass both
      the SSL and TLS protocols. Typically, "SSL" refers to the actual SSL protocol only when a
      version is also provided (for example, SSL 3.0). To find out why you should disable the SSL
      protocol and switch to TLS, check out Protecting you against the SSL 3.0 vulnerability .

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Outlook on the web virtual
      directories" entry in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.1431 -->

Use the EAC to view or configure Outlook on the
web virtual directory properties
 1. In the EAC, go to Servers > Virtual directories.

 2. Select the Outlook on the web virtual directory you want to view or configure.

         You can use the Select server drop down list to filter the Exchange servers by name.

         To only display Outlook on the web virtual directories, select OWA in the Select type
         drop down list.

   After you select the virtual directory, you can see the following properties and values in
   the feature pane:

         Website (read-only): The default web site is named Default Web Site.

         Authentication: The default authentication methods are Basic and FBA (forms-
         based authentication).

         Outlook on the web version: The default version is Exchange2013 .

         External URL: The default value is blank (not configured).

 3. To see more properties, or to modify the settings that aren't read only, click Edit (   ). The
   following tabs and settings are available:

         General tab:

            Internal URL: The URL that's used to access Outlook on the web from the internal
            network. This value is configured automatically during Exchange Server setup,

<!-- p.1432 -->

  and the default value is https:// _<Server FQDN>_/owa (for example,
  https://mailbox01.contoso.com/owa ).

  External URL: The URL that's used to access Outlook on the web from the
  Internet. The default value is blank.

  For Internet-facing Exchange servers, this is the value that clients use to access
  Outlook on the web. To configure this setting, see the Use the EAC to configure
  the external URL for Outlook on the web section in this topic.

  For Exchange servers that don't have an Internet presence, the leave the External
  URL value blank.

Authentication tab:

  Use one or more standard authentication methods: Select this option to use one
  or more of the following authentication methods:

  Integrated Windows authentication: This method requires that users have a valid
  Active Directory user account, and the client computer is a member of the same
  domain as the Exchange server (or a domain that's trusted by the Exchange
  server's domain). Users aren't prompted for their account names and passwords.
  Instead, the server negotiates with the Windows security packages that are
  installed on the client computer. No unencrypted information is transmitted over
  the network.

  Digest authentication for Windows domain servers: This method requires that
  users have a valid Active Directory user account. Passwords are transmitted over

<!-- p.1433 -->

  the network as a hash value for additional security.

  Basic authentication (password is sent in clear text): This is the default value.
  When you use basic authentication, you should require TLS encrypted
  connections between client computers and the Exchange server.

  Use forms-based authentication: Forms-based authentication provides enhanced
  security and allows you to configure the type of prompt that's used to sign-in.
  However, forms-based authentication won't provide a secure channel unless TLS
  is enabled.

  Select one of the following logon formats to use with forms-based
  authentication. The examples use the account for the user named Valeria Barrios
  in the contoso.com domain.

     Domain\user name For example, CONTOSO\VBarrios. This is the default value.

     User principal name (UPN) For example, vbarrios@contoso.com. Note that if
     the UPN doesn't match the email address, users can't access Outlook on the
     web by using this method.

     Username only For example, VBarrios. This setting requires you to configure
     the default domain that's used with all user names. Click Browse in the Logon
     Domain property to select the default Active Directory domain. If the user isn't
     a member of the specified domain, they're required to enter the domain and
     username when they sign in.

Features tab:

<!-- p.1434 -->

These settings affect all users who connect to the Outlook on the web virtual
directory. You can configure custom Outlook on the web settings for specific users
or groups of users by using Outlook on the web mailbox policies. For more
information, see View or configure Outlook on the web mailbox policy properties.

  Communication management

  Instant messaging

  Text messaging

  Unified Messaging: (In Exchange 2016 only; not available in Exchange 2019)

  Exchange ActiveSync

  Contacts

  All address lists*

  Information management

  Journaling

  Inbox rules*

  Recover deleted items*: Disabling this setting doesn't affect the deleted item
  retention for mailboxes; it prevents users from viewing or recovering deleted
  items in Outlook on the web.

  Security

  Change password

  Junk email-filtering: This setting doesn't enable or disable the junk email rule in
  mailboxes; it controls the availability of the junk email settings for users in
  Outlook on the web. For more information about the junk email rule and junk
  email filtering in mailboxes, see Configure Exchange antispam settings on
  mailboxes.

  User experience

  Themes

  Premium client: If you uncheck this setting, The standard version of Outlook on
  the web (formerly known as the premium version of Outlook Web App) is
  disabled, and all clients are forced to use the light version of Outlook on the web.

<!-- p.1435 -->

     Email signature*

     Time management*

     Calendar*

     Tasks*

     Reminders and notifications*

*
    These settings are available after you click More options.

File access tab:

The direct file access settings on this page affect traditional file attachments that
you click on to open or save, or MIME files (typically, image files) that are embedded
directly in the message. Disabling direct file access doesn't affect file access in other
email clients (for example, in Outlook), or by using other access methods in Outlook
on the web (for example, web document access that's provided by Office Online
Server, or links to files in the cloud).

Note that users can select public or private computer access in Outlook on the web
only when the virtual directory is configured for forms-based authentication. All
other authentication methods automatically use private computer access.

     Direct file access for public or shared computers.

     Direct file access for private computers.

<!-- p.1436 -->

 4. If you changed any of the virtual directory settings, click Save. If you're just browsing, click
   Cancel.

Use the EAC to configure the external URL for
Outlook on the web
 1. In the EAC, go to Servers > Virtual directories, select the Outlook on the web virtual
   directory you want to view or configure, and then click Configure (       ).

         You can use the Select server drop down list to filter the Exchange servers by name.

         To only display Outlook on the web virtual directories, select OWA in the Select type
         drop down list.

<!-- p.1437 -->

   2. In the Configure external access domain page that opens, configure the following
     settings:

           Select the servers to use with the external URL: Click Add (     ) and select one or
           more Exchange servers that external clients will use to connect to Outlook on the
           web (don't select internal only servers).

           Enter the domain name you will use with your external servers: Enter the FQDN
           that external clients will use to connect to Outlook on the web (for example,
           mail.contoso.com). Note that this value needs to be configured and resolvable in
           your organization's public DNS.

     When you're finished, click Save.

Reset an Outlook on the web virtual directory
If an Outlook on the web virtual directory isn't working the way you expect, you can reset it.
The virtual directory is deleted and recreated with the default settings. Although any
customized settings are lost, you're forced to select a location for a text document to backup
the current settings.

   1. In the EAC, go to Servers > Virtual directories, select the Outlook on the web virtual
     directory you want to view or configure, and then click Reset (   ).

           You can use the Select server drop down list to filter the Exchange servers by name.

           To only display Outlook on the web virtual directories, select OWA in the Select type
           drop down list.

<!-- p.1438 -->

2. In the Warning page that opens, specify the UNC path of the file to save the current
  virtual directory settings (for example, \ <Server>\ <Share>\owavdir.txt or \
  <LocalServerName>\c$\owavdir.txt).

  When you're finished, click Reset.

3. Restart IIS by using either of the following methods:

       IIS Manager:

        a. Open IIS Manager on the Exchange server. An easy way to do this in Windows
          Server 2012 or later is to press Windows key + Q, type inetmgr, and select
          Internet Information Services (IIS) Manager in the results.

        b. In IIS Manager, select the server.

        c. In the Actions pane, click Restart.

<!-- p.1439 -->

           Command prompt:

     Open an elevated command prompt on the Exchange server (a Command Prompt
     window you open by selecting Run as administrator) and run the following commands:

        Console

        net stop w3svc /y

        Console

        net start w3svc

Use the Exchange Management Shell to view
Outlook on the web virtual directory properties
To use the Exchange Management Shell to view the properties of Outlook on the web virtual
directories, use the following syntax:

  PowerShell

  Get-OWAVirtualDirectory [-Identity "<ExchangeServer>\owa <Website>"]

This example returns a summary list of all Outlook on the web virtual directories on all
Exchange servers in the organization.

<!-- p.1440 -->

  PowerShell

  Get-OWAVirtualDirectory

This example returns detailed information for the Outlook on the web virtual directory in the
default website on the Exchange server named Mailbox01.

  PowerShell

  Get-OWAVirtualDirectory -Identity "Mailbox01\owa (Default Web Site)" | Format-List

This example returns the authentication methods and settings for the same virtual directory:

  PowerShell

  Get-OWAVirtualDirectory -Identity "Mailbox01\owa (Default Web Site)" | Format-List
  *Authentication*

Note: Not every setting is applicable to Exchange 2016 or Exchange 2019 (for example,
SpellCheckerEnabled).

For detailed syntax and parameter information, see Get-OWAVirtualDirectory.

Use the Exchange Management Shell to configure
Outlook on the web virtual directory settings
There are many more configuration settings available for Outlook on the web virtual directories
in the Exchange Management Shell (the Set-OwaVirtualDirectory cmdlet) than in the EAC.
Hare are some of the Outlook on the web virtual directory settings that are only available in
the Exchange Management Shell:

                                                                                          ﾉ   Expand table

 Parameter                          Function

 AllowedFileTypes                   Defines the file types for direct file access (traditional file
 BlockedFileTypes                   attachments an embedded MIME files) in Outlook on the web (not
 ForceSaveFileTypes                 in other email clients).
 AllowedMimeTypes
 BlockedMimeTypes
 ForceSaveMimeTypes
 ActionForUnknownFileAndMIMETypes
