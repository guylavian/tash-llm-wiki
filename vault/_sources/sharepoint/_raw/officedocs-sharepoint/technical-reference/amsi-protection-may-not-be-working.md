---
title: "Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server) - SharePoint Server"
description: "Learn what to do, if AMSI protection isn't working."
ms.topic: troubleshooting
---
Note

Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)

# Antimalware Scan Interface (AMSI) protection may not be working (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Antimalware Scan Interface (AMSI) protection may not be working.

**Summary:** Antimalware Scan Interface (AMSI) protection is enabled for one or more web applications in the SharePoint farm. However, SharePoint didn't receive the expected response from the antimalware scan engine when verifying that this protection is working. Web applications may not be protected on the servers listed in the Failing Servers section of this health analyzer report.

**Cause:** AMSI running prerequisites aren't met, or the real-time protection service of the antimalware scan engine isn't enabled.

**Resolution: Ensure the prerequisites to activate AMSI**

For example, AMSI would only work on Windows Server 2016 or higher. For more information on other prerequisites, see Prerequisites or you can deactivate AMSI for SharePoint Server to turn off this health rule alarm.

**Resolution: Enable the real-time protection service**

If you're using Microsoft Defender as your antimalware scan engine, ensure that real-time protection is enabled on each server listed in the "Failing Servers" section of this health report.

Select the **Start** button.

Select **Settings**.

Select **Update & Security**.

Select **Windows Security**.

Select **Virus & protection settings**.

Select **Manage settings**.

Ensure Real-time protection is set to **On**.

Additional resources

## Additional resources

- Last updated on 
		2023-09-12
