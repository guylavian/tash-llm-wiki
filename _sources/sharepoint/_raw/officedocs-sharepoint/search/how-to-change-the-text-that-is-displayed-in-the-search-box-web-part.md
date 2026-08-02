---
title: "How to change the text that is displayed in the Search Box Web Part in SharePoint Server - SharePoint Server"
description: "Learn how to change the text that is displayed in the Search Box Web Part in SharePoint Server."
ms.topic: how-to
---
Note

How to change the text that is displayed in the Search Box Web Part in SharePoint Server

# How to change the text that is displayed in the Search Box Web Part in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article will be short and sweet, so let's get right to it.

How to change the text that is displayed in the Search Box Web Part

## How to change the text that is displayed in the Search Box Web Part

The following screenshot shows the default text that is displayed in the Search Box Web Part.

Here are the steps to change this text:

In your mapped network drive, go to **Display Templates** --> **Search**, and open the file  *Control_SearchBox*  . For details about mapping your network drive, see Stage 6: Upload and apply a new master page to a publishing site in SharePoint Server.

Replace the value for the  *prompt* variable with the text you want to display. Enclose the text in quotation marks.

The following screenshot shows how we changed this in our Search Center scenario.

Save the file.

In the Search Center, you can now see the new text.

So that's it for this series. If you plan to change how search results are displayed in your Search Center, we hope you'll find the information in this series helpful.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
