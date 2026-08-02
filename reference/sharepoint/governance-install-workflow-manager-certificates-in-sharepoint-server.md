---
title: "Install Workflow Manager certificates in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: governance-install-workflow-manager-certificates-in-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/governance/install-workflow-manager-certificates-in-sharepoint-server
family: governance
documentKind: "install-set-up-deploy"
abstract: "Learn how to configure SSL certificates for encrypted communication between Workflow Manager and SharePoint Server."
---

# Install Workflow Manager certificates in SharePoint Server - SharePoint Server

Note

Install Workflow Manager certificates in SharePoint Server

# Install Workflow Manager certificates in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Secure Socket Layer (SSL) is an encrypted communication protocol which uses encryption certificates. Workflow Manager and SharePoint Server can communicate in a secure manor using SSL. This article describes the steps required to setup and configure SSL certificates.

Configuration steps

## Configuration steps

The following sections provide instructions for configuring SSL communication with Workflow Manager and SharePoint Server.

Enable SSL

### Enable SSL

Enable Secure Sockets Layer (SSL) in IIS Manager. For guidance on completing the configuration, see the following:

Configuring SSL in IIS Manager

How to Set Up SSL on IIS 7

Install Workflow Manager certificates in SharePoint

### Install Workflow Manager certificates in SharePoint

Under some circumstances, you must obtain and install Workflow Manager "issuer" certificates on SharePoint Server. Here are the circumstances where you must install Workflow Manager certificates:

If SSL is enabled either on SharePoint Server (which is not the default) or on Workflow Manager (which is the default), AND

If SharePoint Server and Workflow Manager do not share a Certificate Authority, AND

If Workflow Manager is configured to generate self-signed certificates (which is the default).

Note

Product trial, workflow development, and troubleshooting are easier if SSL is not enabled. However, communication between SharePoint Server and Workflow Manager is not encrypted if SSL is not enabled. For this reason, SSL should be enabled for production configurations.

**To obtain and export certificates from the Workflow Manager server**

On a computer that has Workflow Manager installed, choose **IIS Manager**, **Sites**. Right-click **Workflow Management Site**, and then choose **Edit Bindings**.

Choose the **https** port, and then choose **Edit**. Choose the **View** button in the **SSL Certificate** section.

To export the issuer certificate, do the following:

In the **Certificate** window, choose the **Certification path** tab.

Select **root certification path** and choose **View**.

On the **Details** tab, choose **Export Certificate**, and take the default options in the export wizard.

Give the exported certificate file a friendly name.

**To install certificates on SharePoint Server**

Copy the issuer certificate to your SharePoint Server computer.

Add the certificates to the Windows Certificate store.

For each certificate, do the following:

Double-click the file to open and view the certificate.

On the certificate, choose the **Install Certificate** button to start the installation wizard.

In the wizard, choose **Place all certificates in the following store**, and then choose **Trusted Root Certification Authorities**.

Add the certificates to SharePoint Server by going to the SharePoint Management shell and running the **New-SPTrustedRootAuthority** cmdlet. Do this for each certificate file.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
