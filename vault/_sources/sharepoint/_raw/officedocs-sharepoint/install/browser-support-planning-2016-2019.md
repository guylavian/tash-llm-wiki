---
title: "Plan browser support in SharePoint Servers 2016 and 2019 - SharePoint Server"
description: "Learn about how SharePoint Server supports Internet Explorer, Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge."
ms.topic: interactive-tutorial
---
Note

Plan browser support in SharePoint Servers 2016 and 2019

# Plan browser support in SharePoint Servers 2016 and 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Servers 2016 and 2019 supports several commonly used web browsers, such as  Internet Explorer,  Google Chrome,  Mozilla Firefox,  Apple Safari, and Microsoft Edge. However, certain web browsers can cause some SharePoint Servers 2016 or 2019 functionality to be downgraded, limited, or available only through alternative steps.

As you plan your deployment of SharePoint Servers 2016 or 2019, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint Servers 2016 and 2019.

Key planning phase of browser support

## Key planning phase of browser support

Browser support is an important part of your SharePoint Servers 2016 or 2019 implementation. Before you install SharePoint Server, make sure that you know the browsers that SharePoint Server supports. The information in this article describes browser support in the following sections:

Browser support levels

Browser details

Browser support levels in SharePoint Server 2016

### Browser support levels in SharePoint Server 2016

The following table summarizes the support levels of typically used web browsers.

| **Browser** | **Supported** | **Not supported** |
| --- | --- | --- |
| Microsoft Edge (Chromium) | X |  |
| Microsoft Edge (EdgeHTML - Legacy) | X |  |
| Internet Explorer 11 | X |  |
| Internet Explorer 10 | X |  |
| Internet Explorer 9 |  | X |
| Internet Explorer 8 |  | X |
| Internet Explorer 7 |  | X |
| Internet Explorer 6 |  | X |
| Google Chrome (latest released version) | X |  |
| Mozilla Firefox (latest released version plus immediate previous version) | X |  |
| Apple Safari (latest released version) | X |  |

Browser support levels in SharePoint Server 2019

### Browser support levels in SharePoint Server 2019

The following table summarizes the support levels of typically used web browsers.

| **Browser** | **Supported** | **Not supported** |
| --- | --- | --- |
| Microsoft Edge (Chromium) | X |  |
| Microsoft Edge (EdgeHTML - Legacy) | X |  |
| Internet Explorer 11 | X |  |
| Internet Explorer 10 |  | X |
| Internet Explorer 9 |  | X |
| Internet Explorer 8 |  | X |
| Internet Explorer 7 |  | X |
| Internet Explorer 6 |  | X |
| Google Chrome (latest released version) | X |  |
| Mozilla Firefox (latest released version plus immediate previous version) | X |  |
| Apple Safari (latest released version) | X |  |

Browser details

### Browser details

Review the details of the web browser that you have or plan to use in your organization to make sure that the web browser works with SharePoint Server 2016 and 2019, and according to your business needs.

**Internet Explorer and older functionality**

Note

Some older SharePoint functionality that relies on NPAPI or ActiveX will not work on browsers other than Internet Explorer. You can work around each of these issues by using Internet Explorer to perform these tasks.

Using ActiveX controls in SharePoint Server

#### Using ActiveX controls in SharePoint Server

Some functionality in SharePoint Server requires ActiveX controls. This produces limitations on browsers which do not support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. In SharePoint Server 2016, all other supported browsers, including Microsoft Edge and the Immersive mode of Internet Explorer 10 have the following limitations.

For SharePoint Server 2016 and 2019, browsers other than Internet Explorer 11 have the following limitations.

| Plugin name | DLL file name | What it does |  | Known limitations |
| --- | --- | --- | --- | --- |
| Digital Signature | Dsigctrl.dll, dsigres.dll | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Make sure that the following conditions exist:  
  Forms that are signed on the client can be verified on the server.  
  Forms that are signed on the server can be verified on the client. |  | An inability to verify a form produces an error that states that the form cannot be signed. |
| NameCtrl | Name.dll | Enables a webpage to display a contact card and presence status for people. Integrates through client-side APIs with Office client and Skype for Business client. |  |  |
| TaskLauncher | Nameext.dll | Used to export items in a task list to Project Server if Project client is installed on the client computer. |  | If software requirements are not met, an error message states that you need to install Project client. |
| SpreadSheetLauncher | Owssupp.dll | Used to verify whether Excel is installed for Export to Excel feature. |  | If Excel is not installed, the user may be prompted to download the file "query.iqy" which can then be opened in Excel. |
| StssyncHandler | Owssupp.dll | Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook. Non-IE clients may have an additional prompt to open the calendar in Outlook. |  |  |
| ExportDatabase | Owssupp.dll | Enables a user to use an application such as Access to create or open a database that contains SharePoint list data. |  | To export a list, the client computer must have a SharePoint compatible application. |
| OpenDocuments | Owssupp.dll | Starts Office client applications so that a user can create a or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write. |  | If a compatible Office application or browser is not installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser. |
| CopyCtl | Stsupld.dll | Enables a user to copy a document on a SharePoint site to one or more locations on a server. |  | In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog is not displayed. |
| PPActiveX | PPSLAX.dll | Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library. |  | Does not work on Click-to-Run installations of Office and version of Office that run on Windows for ARM. |
| BCSLauncher | BCSLaunch.dll | Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server. |  |  |

Other functionality, such as **Form settings** in **List settings** only function with Internet Explorer.

Mobile browser support

## Mobile browser support

SharePoint Server 2016 supports the following versions:

Internet Explorer and Microsoft Edge on Windows Phone 8.1 or later.

Latest version of Chrome on Android 4.4 or later.

Latest versions of Safari and Chrome on iOS 8 or later.

For SharePoint Server 2019, Chrome or Safari on iOS10 or later

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
