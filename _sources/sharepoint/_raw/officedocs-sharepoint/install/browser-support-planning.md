---
title: "Plan browser support in SharePoint 2013 - SharePoint Server"
description: "Learn about how SharePoint supports Internet Explorer, Google Chrome, Mozilla Firefox, and Apple Safari."
ms.topic: interactive-tutorial
---
Note

Plan browser support in SharePoint 2013

# Plan browser support in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365.

SharePoint 2013 supports several commonly used web browsers, such as  Internet Explorer,  Google Chrome,  Mozilla Firefox,  Apple Safari, and Microsoft Edge. However, certain web browsers could cause some SharePoint 2013 functionality to be downgraded, limited, or available only through alternative steps.

As you plan your deployment of SharePoint 2013, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint 2013.

Key planning phase of browser support

## Key planning phase of browser support

Browser support is an important part of your SharePoint 2013 implementation. Before you install SharePoint 2013, make sure that you know the browsers that SharePoint 2013 supports. The information in this article describes browser support in the following sections:

Browser support matrix

Browser details

Browser support matrix

### Browser support matrix

The following table summarizes the support levels of typically used web browsers.

| **Browser** | **Supported** | **Not supported** |
| --- | --- | --- |
| Microsoft Edge (Chromium) | X |  |
| Microsoft Edge (EdgeHTML - Legacy) | X |  |
| Internet Explorer 11 | X |  |
| Internet Explorer 10 | X |  |
| Internet Explorer 9 | X |  |
| Internet Explorer 8 | X |  |
| Internet Explorer 7 |  | X |
| Internet Explorer 6 |  | X |
| Google Chrome (latest released version) | X |  |
| Mozilla Firefox (latest released version) | X |  |
| Apple Safari (latest released version) | X |  |

Browser details

### Browser details

Review the details of the web browser that you have or plan to use in your organization to make sure that the web browser works with SharePoint 2013 and according to your business needs.

Supported Internet Explorer versions

#### Supported Internet Explorer versions

The product group makes every effort to validate that SharePoint functionality works correctly with released versions of Internet Explorer. Customers who want a more deeply validated browser interaction experience should strongly consider Internet Explorer.

**Microsoft Edge, Internet Explorer 11, Internet Explorer 10, Internet Explorer 9, Internet Explorer 8**

Note

Internet Explorer 11  *edge mode*  is not supported. Add sites to the **Compatibility View** list to make some features work.

Note

Microsoft Edge (Chromium-based and EdgeHTML-based) is supported with the SharePoint Server 2013 December 2015 CU. For additional information about the December 2015 CU, see December 8, 2015, update for SharePoint Foundation 2013 (KB3114352)

Other supported browsers

#### Other supported browsers

**Google Chrome (latest released version)**

**Mozilla Firefox (latest released version plus immediate previous version)**

For example, if the latest released version is 10, then version 9 would be supported.

**Apple Safari (latest released version)**

ActiveX controls

#### ActiveX controls

Some functionality in SharePoint 2013 requires ActiveX controls. This produces limitations on browsers which do not support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. All other browsers have the following limitations.

Note

Internet Explorer 10 does not support Active X controls when in immersive mode. The functionality for the controls listed below should only be expected to work in desktop mode.

| Plugin name | DLL Filename | What it does | Supported browser version | Known limitations |
| --- | --- | --- | --- | --- |
| Digital Signature | Dsigctrl.dll, dsigres.dll | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Make sure that the following conditions exist:  
  Forms that are signed on the client can be verified on the server.  
  Forms that are signed on the server can be verified on the client. | Internet Explorer versions 8, 9 and 10 | An inability to verify a form produces an error that states that the form cannot be signed. |
| NameCtrl | Name.dll | Enables a web page to display a contact card and presence status for people. Integrates through client-side APIs with Office 2016. | Supported in Internet Explorer versions 8, 9, and 10.  
 Firefox, Google Chrome are also supported by using a plug-in.  
 Internet Explorer version 10 immersive mode is not supported. |  |
| TaskLauncher | Nameext.dll | Used to export items in a task list to Project Server if Project 2010 is installed on the client computer. | All browsers | If software requirements are not met, an error message states that you need to install Project Server. |
| SpreadSheetLauncher | Owssupp.dll | Used to verify whether Excel is installed for Export to Excel feature. | Internet Explorer versions 8, 9, and 10 | If Excel is not installed, an error message states that a list cannot be imported because a compatible spreadsheet application is not installed or is not compatible with the browser. |
| StssyncHandler | Owssupp.dll | Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook 2016. | Internet Explorer versions 8, 9, and 10 |  |
| ExportDatabase | Owssupp.dll | Enables a user to use an application such as Access to create or open a database that contains SharePoint list data. | Internet Explorer versions 8, 9, and 10 | To export a list, the client computer must have a SharePoint compatible application. |
| OpenDocuments | Owssupp.dll | Starts Office client applications so that a user can create a document or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write. | All except Internet Explorer version 10 in immersive mode. | If a compatible Office application or browser is not installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser. |
| UploadCtl | Stsupld.dll | Enables drag-and-drop in SharePoint 2013 visual mode "upload multiple files" dialog. | Internet Explorer versions 8 and 9. |  |
| CopyCtl | Stsupld.dll | Enables a user to copy a document on a SharePoint site to one or more locations on a server. | Internet Explorer versions 8, 9, and 10 | In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog is not displayed. |
| PPActiveX | PPSLAX.dll | Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library. | Internet Explorer versions 8, 9, and 10 | Does not work on Click-to-Run installations of Office and version of Office that run on Windows for ARM. |
| BCSLauncher | BCSLaunch.dll | Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server. | Internet Explorer versions 8, 9, and 10 |  |

Mobile browser support

## Mobile browser support

To learn about the different mobile device browsers supported, see Mobile device browsers supported in SharePoint 2013

See also

## See also

Other Resources

#### Other Resources

Plan for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
