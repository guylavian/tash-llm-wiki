---
title: "Enhance Document Antivirus with AMSI Option - SharePoint Server"
description: "Learn how to configure the Document Antivirus feature with AMSI option in SharePoint Server."
ms.topic: how-to
---
Note

Enhance Document Antivirus with AMSI Option in SharePoint Server

# Enhance Document Antivirus with AMSI Option in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn how to configure and manage the Document Antivirus feature with AMSI option in SharePoint Server. This article describes the feature, prerequisites, configuration steps, and troubleshooting guidance.

Overview

## Overview

The **Enhance Document Antivirus with AMSI Option** feature enables SharePoint Server to scan documents for malware using the Antimalware Scan Interface (AMSI). This allows SharePoint to leverage Microsoft Defender or any AMSI-compatible antimalware solution to scan documents uploaded to or downloaded from SharePoint Server.

This feature enhances the legacy document virus scanning capability by providing an AMSI-based option that integrates with modern Windows security.

Tip

This feature is distinct from the AMSI Filter feature. AMSI Filter scans incoming HTTP requests for SharePoint Server, while Document Antivirus with AMSI scans documents during upload, download, or online editing.

Prerequisites

## Prerequisites

Before you configure this feature, ensure the following:

- You are running SharePoint Server Subscription Edition with the latest updates.

- Windows Server 2016 or later is installed.

- An AMSI-compatible antimalware solution (such as Microsoft Defender Antivirus) is installed and enabled on all SharePoint servers.

- You must be a member of the **Farm Administrators** group.

Available Document Malware Scanning Options

## Available Document Malware Scanning Options

You can configure SharePoint Server to use one of the following document scanning options:

- **Automatic (default):** Attempts to use the legacy VSAPI (Virus Scanning API) first. If VSAPI is unavailable, AMSI is used.

- **AMSI:** Forces SharePoint to use AMSI for document scanning, even if VSAPI-compatible software is present.

- **VSAPI:** Forces SharePoint to use VSAPI for document scanning, even if AMSI-compatible software is present.

Configure Document Antivirus with AMSI

## Configure Document Antivirus with AMSI

To configure the document antivirus scanning:

Open **SharePoint Central Administration**.

Select **Security** in the left navigation.

Click **Manage antivirus settings**.

Under **Antivirus Settings**, select the document antivirus option you need:

- Select **Scan documents on upload** to scan files as users upload them to libraries.

- Select **Scan documents on download** to scan files before users download them.

Under **Scan Interface Type**, select one of the following:

- **Automatically choose the available scan interface** – This is recommended option. SharePoint will attempt to use the legacy VSAPI (Virus Scanning API) first. If VSAPI is unavailable, AMSI is used.

- **Use the Antimalware Scan Interface (AMSI) API for scanning** – Only use the newer Antimalware Scan Interface, even if VSAPI-compatible software is present. If you have both VSAPI and AMSI compatible software, then you may want to select this to ensure the document antiviurs feature uses AMSI.

- **Use the legacy Microsoft Office SharePoint Virus Scan Engine (VSE) API for scanning.** – Only use the legacy VSAPI integration, even if AMSI-compatible software is present.

Click **OK** to save your changes.

How It Works

## How It Works

When a user uploads, downloads, or edits a document in SharePoint, the selected scanning engine (AMSI or VSAPI) is invoked to check the file for malware. If malware is detected, the action is blocked and an error is logged.

Additional resources

## Additional resources

- Last updated on 
		2025-09-05
