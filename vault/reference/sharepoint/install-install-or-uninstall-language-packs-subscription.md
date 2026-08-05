---
title: "Install or uninstall language packs for SharePoint Servers Subscription Edition - SharePoint Server"
type: reference
domain: sharepoint
slug: install-install-or-uninstall-language-packs-subscription
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/install-or-uninstall-language-packs-subscription
family: install
documentKind: "install-set-up-deploy"
abstract: "Learn how to download, install, and uninstall language packs for SharePoint Server Subscription Edition."
---

# Install or uninstall language packs for SharePoint Servers Subscription Edition - SharePoint Server

Note

Install or uninstall language packs for SharePoint Servers Subscription Edition

# Install or uninstall language packs for SharePoint Servers Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Language packs enable site owners and site collection administrators to create SharePoint sites and site collections in multiple languages, without requiring separate installations of SharePoint Server. You install language packs, which contain language-specific site templates, on each SharePoint server in your farm. When an administrator creates a site or a site collection that is based on a language-specific site template, the text that appears on the site or the site collection is displayed in the site template's language. Language packs are typically used in multinational deployments where a single server farm supports users in different locations, or when sites and web pages must be duplicated in one or more languages.

Word breakers and stemmers enable you to search efficiently and effectively across content on SharePoint sites and site collections in multiple languages without requiring separate installations of SharePoint Server. Word breakers and stemmers are automatically installed on SharePoint servers by Setup.

Important

If you're uninstalling SharePoint Server, you must uninstall all language packs before you uninstall SharePoint Server.

About language IDs and language packs

## About language IDs and language packs

Site owners or site collection administrators who create sites or site collections can select a language for each site or site collection.

The language that they select has a language identifier (ID). The language ID determines the language that is used to display and interpret text that is on the site or site collection. For example, when a site owner creates a site in French, the site's toolbars, navigation bars, lists, and column headings appear in French. Similarly, if a site owner creates a site in Arabic, the site's toolbars, navigation bars, lists, and column headings appear in Arabic. In addition, the default left-to-right orientation of the site changes to a right-to-left orientation to correctly display Arabic text.

The language packs that are installed on the SharePoint servers determine the list of available languages that you can use to create a site or site collection. By default, sites and site collections are created in the language in which SharePoint Server was installed. For example, if you install the Spanish version of SharePoint Server, the default language for sites, site collections, and web pages is Spanish. If someone has to create sites, site collections, or web pages in a language other than the default SharePoint Server language, you must install the language pack for that language on the SharePoint servers. For example, if you're running the French version of SharePoint Server, and a site owner wants to create sites in French, English, and Spanish, you must install the English and Spanish language packs on the SharePoint servers.

By default, when a site owner creates a new web page in a site, the site displays text in the language that is specified by the language ID.

Language packs are not bundled into multilingual installation packages. You must install a specific language pack for each language that you want to support. Also, language packs must be installed on each SharePoint server to make sure that each SharePoint server can display content in the specified language.

Important

You cannot change an existing site, site collection, or web page from one language to another by applying different language-specific site templates. After you use a language-specific site template for a site or a site collection, the site or site collection always displays content in the language of the original site template. For example, SharePoint can render the same site in multiple languages based on the preferred language of the user's web browser.  But for this to work, the SharePoint language pack that matches the user's preferred language must be installed on each server in the SharePoint farm.

Although a site owner specifies a language ID for a site, some user interface elements such as error messages, notifications, and dialogs do not display in the language that was specified. This behavior occurs because SharePoint Server relies on several supporting technologies—for example, the Microsoft .NET Framework, Microsoft Windows Workflow Foundation, Microsoft ASP.NET, and SQL Server — some of which are localized into only a limited number of languages. If a user interface element is generated by any of the supporting technologies that are not localized into the language that the site owner specified for the site, the user interface element appears in English. For example, if a site owner creates a site in Hebrew, and the .NET Framework component displays a notification message, the notification message is not displayed in Hebrew because the .NET Framework is not localized into Hebrew. This situation can occur when sites are created in any language except the following language: Chinese, French, German, Italian, Japanese, Korean, and Spanish.

Each language pack that you install creates a folder at `%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\LAYOUTS\Locale_ID` that contains language-specific data. In each locale_ID folder, you must have only one HTML error file that contains the error information that is used when a file cannot be found. Whenever a file cannot be found for any site in that language, this file is used. You can specify the file to use by setting the **FileNotFoundPage()** for each web application.

In some cases, some text might originate from the original installation language, which can create a mixed-language experience. This kind of mixed-language experience is typically seen only by content creators or site owners and is not seen by site users.

Downloading language packs

## Downloading language packs

Follow these steps for each language that you want to support. If you decide to download more than one language, be aware that a unique file that has a common name is downloaded for each language. Therefore, make sure that you download each language pack to a separate folder on the hard disk so that you do not overwrite a language pack of a different language.

Important

By default, the Microsoft PowerShell Help files are installed in English (en-us). To view these files in the same language as the operating system, install the language pack for the same language in which the operating system was installed.

Installing language packs on the SharePoint Servers

## Installing language packs on the SharePoint Servers

Language packs are available as individual downloads (one download for each supported language). If you have a server farm environment and you're installing language packs to support multiple languages, you must install the language packs on each SharePoint server.

When you install language packs, the language-specific site templates are installed in the `%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\ _LanguageID_` directory,
where,
`_LanguageID_` is the Language ID number for the language that you're installing.

For example, the United States English language pack installs to the `%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\1033` directory. After you install a language pack, site owners and site collection administrators can create sites and site collections based on the language-specific site templates by specifying a language when they are creating a new SharePoint site or site collection.

Important

The language pack is installed in its native language. The procedure that follows is for the English language pack.

Install a language pack on Windows Server with Desktop Experience

### Install a language pack on Windows Server with Desktop Experience

Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see Initial deployment administrative and service accounts in SharePoint Server.

Mount the **ISO disc image** as a drive on your computer by double-clicking on it, or by specifying it as a virtual drive in your virtual machine manager.

Navigate to the mounted drive and run (`setup.exe`) to launch the language pack setup program.

On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.

The Setup runs and installs the language pack.

Run SharePoint Products Configuration by using the default settings.

Note

If you don't run SharePoint Products Configuration after you install a language pack, the language pack will not be installed correctly.

Run the SharePoint Products Configuration Wizard

### Run the SharePoint Products Configuration Wizard

Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see Initial deployment administrative and service accounts in SharePoint Server.

Click **Start**, point to **Microsoft SharePoint Products** folder, click **SharePoint Products Configuration Wizard**.

On the **Welcome to SharePoint Products** page, click **Next**.

Click **Yes** in the dialog that alerts you that some services might have to be restarted during configuration.

On the **Modify Server Farm Settings** page, click **Do not disconnect from this server farm**, and then click **Next**.

If the **Modify SharePoint Central Administration Web Administration Settings** page appears, do not change any of the default settings, and then click **Next**.

After you complete the **Completing the SharePoint Products Configuration Wizard**, click **Next**.

On the **Configuration Successful** page, click **Finish**.

After you install a new language pack and run the **SharePoint Products Configuration Wizard**, you must deactivate and then reactivate any language-specific features before you use the new language pack.

Install a language pack on Windows Server Core

### Install a language pack on Windows Server Core

Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see Initial deployment administrative and service accounts in SharePoint Server.

Mount the ISO disc image as a drive on your computer by using the Mount-DiskImage cmdlet or by specifying it as a virtual drive in your virtual machine manager.

Run Language Pack for SharePoint and Project Server Subscription Edition Setup (`setup.exe`) on your computer in command line mode. This step is done by adding the following command line parameters when launching (`setup.exe`):

`/config <config file>` (Where `<config file>` is the path to the **\Files\SetupSilent\config.xml** file on your mounted drive).

`/IAcceptTheLicenseTerms` (This parameter signifies that you have read, understand, and agree to the license terms of language pack for SharePoint and Project Server Subscription edition).

Once the language pack for SharePoint and Project Server Subscription Edition setup has completed, reboot your computer.

Run **Install-SPHelpCollection -All**.

Run **Initialize-SPResourceSecurity**.

Run **Install-SPService**.

Run **Install-SPFeature -AllExistingFeatures**.

Run **Install-SPApplicationContent**.

Uninstall a language pack on Windows Server with Desktop Experience

### Uninstall a language pack on Windows Server with Desktop Experience

From the **Start** menu, click **Control Panel**.

Click **Uninstall** a program.

In the list of currently installed programs, select **Language Pack for SharePoint and Project Server Subscription Edition - Language** and then click **Uninstall**.

Click **Yes** to confirm that you want to remove the program.

Click **OK** in the dialog-box alerting you that this might result in partial loss of functionality for sites that depends on this language pack.

After the language pack has been successfully uninstalled, click **Close**.

Uninstall a language pack on Windows Server Core

### Uninstall a language pack on Windows Server Core

Run SharePoint setup (`setup.exe`) from your `%CommonProgramFiles%\Microsoft Shared\SERVER16\Server Setup Controller` directory with the following parameters:

`/config <config file>` (Where `<config file>` is the path to your `config.xml` file).

`/uninstall OSMUI.<language tag>` (This parameter signifies the language pack to uninstall).

For example, the following PowerShell command is used to uninstall Japanese language pack:

```
$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\config.xml" /uninstall OSMUI.JA-JP
```

List of Languages

## List of Languages

Each folder name has a language tag appended to it, in the form ll-cc. That tag identifies the language and culture. For example, U.S. English language folders are identified by the folder name extension en-us.

Folders for the language-specific components are identified by the language tag that is shown in the table. The Windows operating system uses locale identifiers (LCIDs) to identify languages in the Windows registry.

SharePoint Servers Subscription Edition, 2019, and 2016 support the following languages:

| Language | Language tag | LCID |
| --- | --- | --- |
| Arabic | ar-sa | 1025 |
| Azerbaijani | az-latn-az | 1068 |
| Basque | eu-es | 1069 |
| Bosnian (Latin) | bs-latn-ba | 5146 |
| Bulgarian | bg-bg | 1026 |
| Catalan | ca-es | 1027 |
| Chinese (Simplified) | zh-cn | 2052 |
| Chinese (Traditional) | zh-tw | 1028 |
| Croatian | hr-hr | 1050 |
| Czech | cs-cz | 1029 |
| Danish | da-dk | 1030 |
| Dutch | nl-nl | 1043 |
| English | en-us | 1033 |
| Estonian | et-ee | 1061 |
| Finnish | fi-fi | 1035 |
| French | fr-fr | 1036 |
| Galician | gl-es | 1110 |
| German | de-de | 1031 |
| Greek | el-el | 1032 |
| Hebrew | he-il | 1037 |
| Hindi | hi-in | 1081 |
| Hungarian | hu-hu | 1038 |
| Indonesian | id-id | 1057 |
| Irish | ga-ie | 2108 |
| Italian | it-it | 1040 |
| Japanese | ja-jp | 1041 |
| Kazakh | kk-kz | 1087 |
| Korean | ko-kr | 1042 |
| Latvian | lv-lv | 1062 |
| Lithuanian | lt-lt | 1063 |
| Macedonian (North Macedonia) | mk-mk | 1071 |
| Malay (Malaysia) | ms-my | 1086 |
| Norwegian (Bokmål) | nb-no | 1044 |
| Polish | pl-pl | 1045 |
| Portuguese (Brazil) | pt-br | 1046 |
| Portuguese (Portugal) | pt-pt | 2070 |
| Romanian | ro-ro | 1048 |
| Russian | ru-ru | 1049 |
| Serbian (Cyrillic) | sr-cyrl-rs | 10266 |
| Serbian (Latin) | sr-latn-rs | 9242 |
| Slovak | sk-sk | 1051 |
| Slovenian | sl-si | 1060 |
| Spanish | es-es | 3082 |
| Swedish | sv-se | 1053 |
| Thai | th-th | 1054 |
| Turkish | tr-tr | 1055 |
| Ukrainian | uk-ua | 1058 |
| Vietnamese | vi-vn | 1066 |
| Welsh | cy-gb | 1106 |

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
