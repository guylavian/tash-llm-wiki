---
title: "Outbound e-mail hasn't been configured (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Outbound email hasn't been configured, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Outbound e-mail hasn't been configured (SharePoint Server)

# Outbound e-mail hasn't been configured (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Outbound email hasn't been configured.

**Summary:** An outgoing email server hasn't been configured on this SharePoint Server deployment. With no SMPT server configured for outgoing email, SharePoint Server can't send email messages, including alert email, confirmation email, invitation email, and email about exceeding quotas.

**Cause:** An SMPT email server hasn't yet been configured in the farm.

**Resolution: Configure outgoing email settings in Central Administration**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, select **System Settings**.

On the System Settings page, in the **E-Mail and Text Messages (SMS)** section, select **Configure outgoing e-mail settings**.

On the Outgoing E-Mail Settings page, type the SMTP server information in the **Outbound SMTP server** box, and then specify the addresses and the character set that you want to use.

Select **OK**.

See also

## See also

Concepts

### Concepts

Plan email integration for a SharePoint Server farm

Configure email integration for a SharePoint Server farm

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
