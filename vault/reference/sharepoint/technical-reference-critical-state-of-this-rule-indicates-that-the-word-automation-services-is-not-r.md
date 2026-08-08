---
title: "Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-critical-state-of-this-rule-indicates-that-the-word-automation-services-is-not-r
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/critical-state-of-this-rule-indicates-that-the-word-automation-services-is-not-r
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Critical state of this rule indicates that the Word Automation Services is not running when it should be running, for SharePoint Server."
---

# Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server) - SharePoint Server

Note

Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server)

# Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Critical state of this rule indicates that the Word Automation Services is not running when it should be running.

**Summary:** Word Automation Services uses a timer job to pull conversion items from the Word Automation Services database and then assign those conversion items to individual application servers. If the timer job does not run, conversion items cannot start to convert.

**Cause:** The Word Automation Services timer job is not enabled.

**Resolution: Enable the Word Automation Services timer job.**

Verify that the user account that is performing this procedure is a member of the Farm Administrators group.

On the SharePoint Central Administration website, click **Monitoring**.

On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.

On the Job Definitions page, in the list of timer jobs, click **Word Automation Services Timer Job**.

On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
