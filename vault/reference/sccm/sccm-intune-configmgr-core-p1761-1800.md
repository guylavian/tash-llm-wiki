---
title: "Core infrastructure documentation — pages 1761-1800"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1761-1800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1761-1800
family: sccm
documentKind: "doc"
abstract: "Manager uses Bing Maps to display the location on the geographical view. Then you can view your hierarchy with the geographical locations. This view provides insight into regional issues that might affect specific sites or intersite replication. When you specify a location, you"
---

# Core infrastructure documentation — pages 1761-1800

<!-- p.1761 -->

Manager uses Bing Maps to display the location on the geographical view. Then you can
view your hierarchy with the geographical locations. This view provides insight into
regional issues that might affect specific sites or intersite replication.

When you specify a location, you can use the Location box to search for a specific site in
your hierarchy. With the site selected, enter the location as a city name or street address
in the Location column. Configuration Manager uses Bing Maps to resolve the location.

Next steps
Monitor database replication

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1762 -->

Use the status system in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the built-in status message system to understand the state of your Configuration
Manager environment.

All major site components generate status messages that provide feedback on site and
hierarchy operations. This information can keep you informed about the health of
different site processes. You can tune the alert system to ignore noise for known
problems, and increase early visibility for other issues that might need your attention.

You generally don't need to configure the Configuration Manager status system. By
default, it uses suitable settings for most environments. You can configure the following
components:

      Status summarizers: Control the frequency of status messages that indicate a
      change for the following four summarizers:

         Application deployment summarizer

         Application statistics summarizer

         Component status summarizer

         Site system status summarizer

      Status filter rules: Create new status filter rules, modify the priority of rules, disable
      or enable rules, and delete unused rules at each site.

        ７ Note

        Status filter rules don't support environment variables to run external
        commands.

      Status reporting: Configure both server and client component reporting, and
      specify where they're sent.

        ２ Warning

<!-- p.1763 -->

        Because the default reporting settings are appropriate for most environments,
        change them with caution. When you increase the level of status reporting by
        choosing to report all status details, you can increase the amount of status
        messages for the site to process. This change increases the processing load
        on the Configuration Manager site. If you decrease the level of status
        reporting, you might limit the usefulness of the status summarizers.

Because the status system maintains separate configurations for each site, edit each site
individually.

Configure status summarizers
   1. In the Configuration Manager console, go to the Administration workspace,
      expand Site Configuration, and select the Sites node.

   2. Select a site. Then on the Home tab of the ribbon, in the Settings group, select
      Status Summarizers.

   3. In the Status Summarizers window, select the status summarizer that you want to
      configure, and select Edit.

Application deployment or application statistics
summarizers
On the General tab of the summarizer properties page, configure the summarization
intervals.

For the application deployment summarizer, these time periods specify how frequently
the site updates the deployment status for applications, task sequences, and packages.
It's calculated based on the deployment start time. The following values show the
defaults:

      Modified in the last 30 days: 60 minutes
      Modified in the last 31 to 90 days: 24 hours
      Modified over 90 days ago: 7 days

For the application statistics summarizer, these time periods specify how often the site
updates application statistics. They're based on the date you last modified the
application. The following values show the defaults:

      Modified in the last 30 days: 240 minutes
      Modified in the last 31 to 90 days: 24 hours

<!-- p.1764 -->

     Modified over 90 days ago: 7 days

Component status summarizer
   1. On the General tab of the summarizer properties page, configure the replication
     and threshold period values:

           Enable status summarization
           Replicate to parent site and select the Replication priority (by default,
           Normal)
           Threshold period (by default, Since 00:00:00). In other words, by default
           component status is reset at midnight.

   2. On the Thresholds tab, select the Message type: Informational, Warning, or Error.

   3. Select a component and then select the properties icon. You can also double-click
     the component, or right-click and select Property.

   4. Specify the threshold for the number of status messages on the component before
     the site changes the status.

The following table shows the default values:

                                                                           ﾉ      Expand table

 Message type               Warning threshold                Critical threshold

 Informational              2000                             5000

 Warning                    10                               50

 Error                      1                                5

For example, if a component generates 2000 informational status messages in the
threshold period (by default, since midnight), the site sets that component's state to
warning.

Site system status summarizer
   1. On the General tab of the summarizer properties page, configure the replication
     and schedule values:

           Enable status summarization
           Replicate to parent site and select the Replication priority (by default,
           Medium)

<!-- p.1765 -->

           Status summarization schedule (by default, every hour on the hour)

   2. On the Thresholds tab, specify values for the Default thresholds for free space on
     any site system. The following values are the defaults:

           Warning (KB): 10485760 (10 GB)
           Critical (KB): 5242880 (5 GB)

     For example, if a site system reports less than 10 GB of free space on a drive, that
     site system's status changes to warning.

   3. The site can also monitor specific thresholds for specific Storage objects. By
     default, it includes thresholds for the SQL Server database and transaction log for
     the site database. The default values for these default objects are the same as the
     default thresholds.

     To modify these thresholds, select the object in the list, and then select the
     properties icon. (You can also double-click the object, or right-click to access these
     actions.)

   4. To create a new storage object to monitor, select the gold asterisk "new" icon.
     Select a storage object from the list, and specify the free space thresholds.

   5. To delete a storage object, select the object, and then select the delete icon.

Manage status filter rules
With status filter rules, the site can take action when specific status message criteria
occurs. There are several default status filter rules, and you can create custom rules.

   Tip

  Starting in version 2107, you can enable the site to send notifications to an external
  system or application. This capability simplifies the process by using a web service-
  based method. You configure subscriptions to send these notifications. These
  notifications are in response to specific, defined events as they occur. For example,
  status message filter rules. For more information, see External notifications.

Modify a status filter rule
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

<!-- p.1766 -->

  2. Select a site, and then on the Home tab of the ribbon, in the Settings group, select
    Status Filter Rules.

  3. In the Status Filter Rules window, select the rule that you want to modify.

          To change the processing order of the status filter rule, select Increase
          Priority or Decrease Priority.

          To change the status of the rule, select Disable or Enable.

          To delete the status filter rule from the site, select Delete

          To change the criteria for the status message rule, select Edit.

Create a status filter rule
  1. In the Configuration Manager console, go to the Administration workspace,
    expand Site Configuration, and select the Sites node.

  2. Select a site, and then on the Home tab of the ribbon, in the Settings group, select
    Status Filter Rules.

  3. Select Create.

  4. On the General page of the Create Status Filter Rule Wizard, specify a Name for
    the new status filter rule. Select message-matching criteria for the rule, and specify
    values to match. The following criteria are available:

          Source: Client, SMS Provider, Site Server
          Site code
          System
          Component
          Message type: Milestone, Detail, Audit
          Severity: Informational, Warning, Error
          Message ID
          Property
          Property value

  5. On the Actions page, specify the actions when a status message matches the
    specified criteria. The following actions are available:

          Write to the Configuration Manager database
             Allow the user to delete messages after how many days
          Report to the event log
          Replicate to the parent site

<!-- p.1767 -->

              Replication priority
           Run a program
              Specify a command line to run on the site server
           Do not forward to status summarizers
           Do not process lower-priority status filter rules

   6. Complete the wizard.

  ７ Note

  Configuration Manager only requires that a new status filter rule has a name. If you
  create a rule, but you don't specify any criteria to process status messages, the
  status filter rule has no effect. This behavior allows you to create and organize rules
  before you configure the criteria for each rule.

Configure status reporting
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select a site, and then on the Home tab of the ribbon, in the Settings group, select
     Configure Site Components, and then select Status Reporting.

   3. In the Status Reporting Component Properties window, specify the server and
     client component status messages that you want to report or log:

           Report: Send status messages to the Configuration Manager status message
           system. By default, this option is enabled for All Milestones for both server
           and client components. The option to Report details on failure is also
           enabled by default.

           Log: Write the type and severity of status messages to the Windows event
           log. By default, this option isn't enabled for either server or client
           components.

Monitor the status system
System status in Configuration Manager provides an overview of the general operations
of sites and site server operations of your hierarchy. It can reveal operational problems
for site system servers or components. You can use the system status to review specific
details for different Configuration Manager operations. You monitor system status from

<!-- p.1768 -->

the System Status node of the Monitoring workspace in the Configuration Manager
console.

Most Configuration Manager site system roles and components generate status
messages. Status message details are logged in each component's operational log, but
are also submitted to the site database. The site then summarizes and presents them in
a general health rollup for each component or site system. These status message rollups
provide information details for regular operations, and details of warnings and errors.
You can configure the thresholds at which the site triggers warnings or errors. Tune the
system in your environment to make sure rollup information ignores known issues that
aren't relevant to you. Also configure it to call attention to actual problems that you
need to investigate.

System status is replicated to other sites in a hierarchy as site data, not global data. This
behavior means you can only see the status for the site to which your Configuration
Manager console connects, and any child sites below that site. When you view system
status, use the Configuration Manager console with the top-level site of your hierarchy.
For more information on site data versus global data, see Database replication: Types of
data.

There are different system status views in the Configuration Manager console:

        Site Status: View a rollup of the status of each site system to review the health of
        each server. The site determines site system health by thresholds that you
        configure for each site in the Site System Status Summarizer. In this node:
           View status messages for each site system
           Set thresholds for status messages
           Manage the operation of the components on site systems by using the
           Configuration Manager Service Manager

        Component Status: View a rollup of the status of each Configuration Manager
        component to review its operational health. The site determines component health
        by thresholds that you configure for each site in the Component Status
        Summarizer. In this node:
           View status messages for each component
           Set thresholds for status messages
           Manage the operation of components by using the Configuration Manager
           Service Manager

        Conflicting Records: View status messages about clients that might have
        conflicting records. Configuration Manager uses the hardware ID to attempt to
        identify clients that might be duplicates and alert you to the conflicting records.

<!-- p.1769 -->

   For example, if you have to reinstall a computer, the hardware ID would be the
   same, but the GUID that Configuration Manager uses might change.

   Status Message Queries: Query status messages for specific events and related
   details. Use status message queries to find the status messages related to specific
   events. You can identify when a specific component, operation, or Configuration
   Manager object was modified, and the account that was used to make the
   modification. For example, run the built-in Collections Created, Modified, or
   Deleted query to identify when a specific collection was created, and the user
   account used to create it.

View status messages
 1. To view status messages in the Configuration Manager console, select a specific
   site system server or component.

 2. In the ribbon, select Show Messages, then choose the type of messages to show:
   All, Error, Warning, Information.

 3. Select the viewing period. Either on or after a specific date and time, or from a
   specific time period. By default, the viewing period is 1 day ago.

 4. The Status Message Viewer has many controls to customize the view. For example,
   to filter the results based on the status messages details, go to the View menu, and
   select Filter.

<!-- p.1770 -->

Starting in version 2010, there's an easier way to view status messages for the following
objects:

     Devices
     Users
     Content
     Deployments
           Monitoring workspace
             Phased deployments (select Show Deployments from the Phased
             Deployments node)
           Deployments tab in the details pane for:
             Packages
             Task sequences

Select one of these objects in the Configuration Manager console, and then select Show
Status Messages from the ribbon.

Next steps
Configure alerts

Configuration Manager Service Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1771 -->

Configure alerts in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configure alerts to understand the state of your Configuration Manager environment.
Configuration Manager generates alerts by some operations when a specific condition
occurs:

      Typically, when an error occurs that you need to resolve.

      To warn you that a condition exists, so that you can continue to monitor the
      situation.

Some alerts you configure, such as alerts for endpoint protection and client status.
Configuration Manager automatically configures other alerts.

You can configure subscriptions to alerts. Subscriptions can send details by email, which
increases your awareness of key issues.

Manage general alerts
In the Configuration Manager console, go to the Monitoring workspace, expand Alerts,
and then select Active Alerts or All Alerts.

The following actions are available on alerts in these nodes:

      Postpone: Suspend monitoring this alert until the specified date is reached. At that
      time, the site updates the state of the alert. You can only postpone an enabled
      alert. When you postpone an alert, you can also add a comment.

      Edit Comments: Enter a comment for the selected alerts. These comments display
      with the alert in the Configuration Manager console.

      Configure: Modify the name, severity, and definition for the selected alert. If you
      change the severity of the alert, this configuration affects how the alerts are
      displayed in the Configuration Manager console.

      Create subscription: Create an email subscription to the selected alert. For more
      information, see Email alerts.

<!-- p.1772 -->

Configure client status alerts
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Device Collections node.

   2. Select the collection for which you want to configure alerts. In the Home tab of the
     ribbon, in the Properties group, select Properties.

        ７ Note

        You can't configure alerts for user collections.

   3. Switch to the Alerts tab, and select Add.

        ７ Note

        The Alerts tab is only visible if your security role has permissions for alerts.

   4. Choose the alerts that you want the site to generate when client status thresholds
     fall below a specific value:

           Client check pass or no results for active clients falls below threshold (%)
           Client remediation success falls below the threshold (%)
           Client activity falls below threshold (%)

   5. In the Conditions list of the Alerts tab, select each client status alert, and then
     specify the following information:

           Alert Name: Accept the default name or enter a new name for the alert.

           Alert Severity: Choose the alert level that displays in the Configuration
           Manager console: Information, Warning, or Critical.

           Raise alert if...: Specify the threshold percentage for the alert.

   6. Select OK to save the alerts and close the collection properties.

Email alerts
You can create an email subscription for alerts. When the site triggers an alert, it can
then send you email notification.

<!-- p.1773 -->

Configure email notification for alerts
Before you can subscribe to email alerts, you need to configure the site to send email
notifications. You'll need information about an SMTP email server.

   Tip

  If you use Microsoft 365, use the following information:

       SMTP server: smtp.office365.com
       Port: 587
       This server requires an encrypted connection (SSL)

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Alerts, and select the Subscriptions node.

   2. On the Home tab of the ribbon, in the Create group, select Configure Email
     Notification.

   3. Specify the following information:

          Enable email notification for alerts: Allow Configuration Manager to use an
          SMTP server to send email alerts.

          FQDN or IP Address of the SMTP server to send email alerts: Enter the fully
          qualified domain name (FQDN) or IP address for the email server to use for
          these alerts.

          Port: Specify the SMTP port for the email server to use for these alerts. For
          example, 587 .

          This server requires an encrypted connection (SSL): Require that the site
          creates an encrypted connection with the SMTP server.

          SMTP Server Connection Account: Specify the authentication method for
          Configuration Manager to use to connect the email server.

             ） Important

             Specify an account that has the least possible permissions to send
             emails.

<!-- p.1774 -->

           Sender address for email alerts: Specify the email address from which alert
           emails are sent.

           Test SMTP Server: Sends a test email to the email address specified in Sender
           address for email alerts.

   4. Select OK to save the settings and to close the window.

Subscribe to email alerts
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Alerts, and select either Active Alerts or All Alerts.

   2. Select an alert. On the Home tab of the ribbon, in the Subscription group, select
     Create subscription.

   3. In the New Subscription window, specify the following information:

           Subscription name: Enter a name to identify the email subscription. You can
           use up to 255 characters.

           Email address: Enter the recipient email addresses to get this alert. Separate
           multiple email addresses with a semicolon ( ; ).

           Email language: Select the language for the email.

   4. Select OK to close the New Subscription window and to create the email
     subscription.

To edit or delete a subscription, select the Subscriptions node under Alerts.

Monitor alerts
You can view alerts in one of the Alerts node of the Monitoring workspace. Alerts have
one of the following alert states:

     Never triggered: The component hasn't met the condition of the alert.

     Active: The site triggered the alert when the component met the condition.

     Canceled: The condition that caused the alert is now resolved.

     Postponed: An administrator suspended monitoring of the alert. Configuration
     Manager will evaluate the state of the alert at a later time.

<!-- p.1775 -->

     Disabled: An administrator disabled the alert. Configuration Manager doesn't
     update the alert even if the state of the alert changes.

When Configuration Manager generates an alert, you can take one of the following
actions:

     Resolve the condition that caused the alert. For example, you resolve a network
     issue. After Configuration Manager detects that the issue no longer exists, the alert
     state changes to Cancel.

     If the alert is a known issue, postpone the alert until a specific time. At that later
     time, Configuration Manager updates the alert to its current state.

     You can only postpone an alert when it's active.

     Edit the Comment of an alert. This action informs other administrators that you're
     aware of the alert. For example, in the comment you can identify how to resolve
     the condition, provide information about the current status of the condition, or
     explain why you postponed the alert.

External notifications
Starting in version 2107, you can enable the site to send notifications to an external
system or application. This capability simplifies the process by using a web service-
based method. You configure subscriptions to send these notifications. These
notifications are in response to specific, defined events as they occur. For example,
status message filter rules. For more information, see External notifications.

Next steps
Configure endpoint protection alerts for a collection

Configure client status alerts for a collection

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1776 -->

External notifications
Article • 10/09/2023

Applies to: Configuration Manager (current branch)

In a complex IT environment, you may have an automation system like Azure Logic
Apps. Customers use these systems to define and control automated workflows to
integrate multiple systems. You could integrate Configuration Manager into a separate
automation system through the product's SDK APIs. But this process can be complex
and challenging for IT professionals without a software development background.

Starting in version 2107, you can enable the site to send notifications to an external
system or application. This feature simplifies the process by using a web service-based
method. You configure subscriptions to send these notifications. These notifications are
in response to specific, defined events as they occur. For example, status message filter
rules.

  ７ Note

  The external system or application defines and provides the methods that this
  feature calls.

When you set up this feature, the site opens a communication channel with the external
system. That system can then start a complex workflow or action that doesn't exist in
Configuration Manager.

Starting in version 2111, use the Configuration Manager console to create or edit
subscriptions for external notifications. This article now focuses on that experience. If
you're using version 2107, see Configuration Manager version 2107.

Prerequisites
         Create the subscription on the top-level site of the hierarchy. This site is either a
         standalone primary site, or a central administration site (CAS). You can view and
         modify an existing subscription on any site in a hierarchy.

         The site's service connection point needs to be in online mode. For more
         information, see About the service connection point.

         Currently, this feature only supports Azure Logic Apps as the external system. An
         active Azure subscription with rights to create a logic app is required.

<!-- p.1777 -->

     The service connection point needs to communicate with the notification service,
     for example Azure Logic Apps. For more information, see Internet access
     requirements.

     To create an event type for an application approval request, the site needs an app
     that requires approval and is deployed to a user collection. For more information,
     see Deploy applications and Approve applications.

Permissions
You can configure the following permissions to the NotificationSubscription object:
Read, Delete, Modify, Create.

     The Full administrator default security role has these permissions.
     The Read only analyst default security role has the Read permission.

In version 2107, users also need the All security scope. In version 2111 and later, you
can't scope the subscription objects. If needed, you can use scopes on the Site object, to
which users need at least read permission.

Other permissions may be required for custom roles. Use the following table to
understand what's needed:

                                                                                 ﾉ    Expand table

 Action                     Alerts:   Site:   Notify:   Notify:   Notify:   Notify:   Site:
                            Read      Read    Read      Modify    Create    Delete    Manage
                                                                                      SFR

 View subscription          X                 X

 Modify subscription        X         X       X         X

 Create subscription Note   X         X       X                   X
 1

 Delete subscription        X                 X                             X

 Create new SFR             X         X       X         Note 2    Note 2              X

 Add existing SFR           X         X       X         Note 2    Note 2

 Add app approval           X         X       X         Note 2    Note 2

The above table uses the following shorthand:

     Notify: Notification subscription objects

<!-- p.1778 -->

     SFR: Status filter rule

Note 1: Top-level site in hierarchy
Create the subscription on the top-level site of the hierarchy. This site is either a
standalone primary site, or a CAS. You can view and modify an existing subscription on
any site in a hierarchy.

Note 2: Modify and Create permissions for event actions
When managing events on the subscription, the permissions to Modify or Create on the
Notification subscription object depend upon whether you need to modify or create
the event. For example, if you have the Create permission, then you can add a status
filter rule to the subscription. If you don't have the Modify permission, then you can't
make changes to the subscription events.

Create an Azure logic app and workflow
Use the following process to create a sample app in Azure Logic Apps to receive the
notification from Configuration Manager.

  ７ Note

  This process is provided as an example to help you get started. It's not intended for
  production use.

   1. Sign in to the Azure portal .

   2. In the Azure search box, enter logic apps , and select Logic Apps.

   3. Select Add and choose Consumption. This action creates a new logic app.

   4. On the Basics tab, specify the project details as necessary for your environment:
     subscription name, resource group, logic app name, and region.

   5. Select Review + create. On the validation page, confirm the details that you
     provided, and select Create.

   6. Under Next steps, select Go to resource.

   7. Under the section to Start with a common trigger, select When a HTTP request is
     received.

<!-- p.1779 -->

  8. At the bottom of the trigger editor, select Use sample payload to generate
    schema.

  9. Paste the following sample payload:

      JSON

       {
             "EventID":0,
             "EventName":"",
             "SiteCode":"",
             "ServerName":"",
             "MessageID":0,
             "Source":"",
             "EventPayload":""
       }

 10. Select Done and then select Save.

 11. Copy the generated URL for the logic app. You'll use this URL later when you create
    the subscription in Configuration Manager.

      ７ Note

      The URL from Azure for the logic app includes the secret key. When saved in
      Configuration Manager, it's protected the same as any other password or
      secret key. If your environment uses a proxy server or other network
      inspection device, there's a risk that it will log this URL and expose the secret
      key. Control access to such systems, and be prepared to renew the secret key
      for the logic app in the Azure portal. You can also set an expiration date for
      the secret key in the Azure portal. For more information, see Secure your
      logic apps.

 12. To add a new step in the designer, select + New Step. Choose an appropriate
    action when it receives a notification from Configuration Manager. For example:

           To send an email, use the Office 365 Outlook connector.
           To post a message to Teams, use the Microsoft Teams connector.

    Sign in if necessary and complete the required information for the action. For more
    information, see the Create logic apps quickstart in the Azure Logic Apps
    documentation.

Notification schema

<!-- p.1780 -->

These notifications use the following standardized schema:

  JSON

  {
         "properties": {
             "EventID": {
                 "type": "integer"
             },
             "EventName": {
                 "type": "string"
             },
             "EventPayload": {
                 "type": "string"
             },
             "MessageID": {
                 "type": "string"
             },
             "ServerName": {
                 "type": "string"
             },
             "SiteCode": {
                 "type": "string"
             },
             "Source": {
                 "type": "string"
             }
         },
         "type": "object"
  }

Create an event
There are two types of events that are currently supported:

      The site raises a status message that matches conditions specified in a status filter
      rule for external notification. You can create a new rule or use an existing one.

      A user requests approval for an application in Software Center.

  ７ Note

  In a hierarchy, the scope of events depends upon the event type:

         Application approval events only happen at primary sites.
         Status filter rules apply to the site where you create the rule using the Create
         external service notification event wizard.

<!-- p.1781 -->

           If you run the wizard to create the event while connected to the CAS, it
           only triggers on matching events from the CAS.
           To subscribe to events raised by a child primary site, connect to the primary
           site. Modify the notification subscription to create a new status filter rule
           for the child primary site.

Use the following process to create an event:

   1. In the Configuration Manager console, connect to the top-level site of the
     hierarchy. This site is either a standalone primary site, or a CAS.

   2. Go to the Monitoring workspace, expand Alerts, and select the External service
     notifications node.

   3. In the ribbon, select Create subscription.

   4. In the New Subscription window, specify a Name for the subscription to identify it
     in the Configuration Manager console. The maximum length is 254 characters.
     Optionally add a Description.

   5. For the External service URL value, paste the URL of the Azure Logic App that you
     previously copied.

   6. Select the gold asterisk     to add a new event to the subscription.

      a. In the Create External Service Notification Event wizard, on the Event type page,
        select one of the following event types:

              New status filter rule: Create a new status filter rule to use for this event.
              Specify a name for the status filter rule, and then configure the filter
              criteria. For more information about criteria for status message rules, see
              Use the status system.

                ） Important

                Be cautious with the type of status filter rule that you create. For
                external notifications, the site can process 300 status messages every
                five minutes. If your rule allows more messages than this limit, it will
                cause a backlog on the site. Create rules with narrow filters for
                specific scenarios. Avoid generic rules that allow a lot of messages.

<!-- p.1782 -->

              Existing status filter rule: Reuse a status filter rule for external notification
              that already exists. It doesn't display all status filter rules, only the rules
              that you created using this wizard.

              User submits application request: Send an external notification for
              application approval requests.

Manage events
After you create a subscription, use the External service notifications node to do the
following actions:

     Properties: Edit the name, description, or events for a subscription. You can't edit
     the external service URL.

     Delete: Remove a subscription.

  ７ Note

  You can view and modify an existing subscription on any site in a hierarchy.

When you select a subscription, the details pane shows information about the events
that have happened.

Trigger an event
The process to trigger an event depends upon the type of subscription:

     For a status filter rule, trigger an event for the site component. For example, use
     the Configuration Manager Service Manager to restart the component.

     For an app approval request, use Software Center to request an app that requires
     approval. For more information, see Software Center user guide.

Monitor the workflow

Configuration Manager Console
Starting in version 2309, when Azure Logic Apps generate notifications or alerts related
to specific events or conditions, Configuration Manager can now capture and display
these notifications. This integration enables the monitoring of Azure Logic App

<!-- p.1783 -->

notifications directly within the Configuration Manager console, providing a centralized
location for tracking critical events, taking appropriate actions and maintain a high level
of operational efficiency.

To use this feature a valid Microsoft Entra Web app is required. Please deploy the Azure
services for Administration Service Management under Administration\Overview\Cloud
Services\Azure Services. If the service is already deployed, admin can use the existing
web application to view Run details from Azure logic app.

For more information, see Configure Azure services for use with Configuration Manager.

Use the following process to view Run Details of subscription:

   1. In the Configuration Manager console click Monitoring.
   2. In the Monitoring workspace, click External Service Notifications and select the
     desired subscription.
   3. Click on Show Details.
   4. In the dialog box, Select the Azure Environment, Microsoft Entra tenant name from
     the drop down and SignIn using your Azure Admin Account.
   5. Select the Subscription ID and enter the Resource group name and Workflow
     name.
   6. Click on Get Run Details button to view the Run Details.

<!-- p.1784 -->

Azure Portal
Within five minutes, the event triggers the logic app workflow. Check the status of the
workflow in the Azure portal. Navigate to the Runs history page of the logic app.

For more information, see Monitor run status, review trigger history, and set up alerts
for Azure Logic Apps.

Troubleshoot
Use the following Configuration Manager log files on the site server to help
troubleshoot this process:

<!-- p.1785 -->

      ExternalNotificationsWorker.log: Check if the queue has been processed and
      notifications are sent to external system.
      statmgr.log: Check if the status filter rules have been processed without errors

Known issues
If you create a status filter rule, you'll see it in the site's list of Status filter rules in the
Configuration Manager console. If you make a change on the Actions tab of the rule
properties, the external notification won't work.

After you recover a central administration site (CAS), delete and recreate the
subscription.

   Tip

  Before you remove a CAS, recreate the subscriptions at the child primary site.

Configuration Manager version 2107

  ） Important

  This section and the PowerShell script only apply to version 2107. In version 2111
  and later, use the Configuration Manager console to create and manage events.

Other prerequisites for version 2107
To create the objects in Configuration Manager version 2107, you need to use the
PowerShell script SetupExternalServiceNotifications.ps1. Use the following script
sample to properly get the PowerShell script to use for this feature:

  PowerShell

  $FileName = ".\SetupExternalServiceNotifications.ps1"
  Invoke-WebRequest https://aka.ms/cmextnotificationscript -OutFile $FileName
  (Get-Content $FileName -Raw).Replace("`n","`r`n") | Set-Content $FileName -
  Force
  (Get-Content $FileName -Raw).TrimEnd("`r`n") | Set-Content $FileName -Force

  ７ Note

<!-- p.1786 -->

  SetupExternalServiceNotifications.ps1 is digitally signed by Microsoft. This script
  sample downloads the file and fixes the line breaks to preserve the digital
  signature.

Create an event in version 2107
There are two types of events that are supported in version 2107:

     The site raises a status message that matches conditions specified in a status filter
     rule.

     A user requests approval for an application in Software Center.

Create a status message event in version 2107

   1. On the site server, run SetupExternalServiceNotifications.ps1. Since you're running
     it on the site server, enter y to continue.

   2. Select option 2 to create a new status filter rule.

   3. Specify a name for the new status filter rule.

   4. Select message-matching criteria for the rule, and specify values to match. Specify
     0 to not use a criterion.

     The following criteria are available:

             Source: Client, SMS Provider, Site Server
             Site code
             System
             Component
             Message type: Milestone, Detail, Audit
             Severity: Informational, Warning, Error
             Message ID
             Property
             Property value

     For more information about criteria for status message rules, see Use the status
     system.

        ） Important

<!-- p.1787 -->

        Be cautious with the type of status filter rule that you create. For external
        notifications, the site can process 300 status messages every five minutes. If
        your rule allows more messages than this limit, it will cause a backlog on the
        site. Create rules with narrow filters for specific scenarios. Avoid generic rules
        that allow a lot of messages.

   5. Rerun the PowerShell script. Select option 3 to create a new subscription.

   6. Specify a name and description for the subscription. Then specify the logic app
     URL that you previously copied from the Azure portal.

   7. Select the new status filter rule.

   8. Select 0 to exit the script.

Create an app approval event in version 2107

  ７ Note

  This event type requires an application that requires approval and is deployed to a
  user collection. For more information, see Deploy applications and Approve
  applications.

   1. On the site server, run SetupExternalServiceNotifications.ps1. Since you're running
     it on the site server, enter y to continue.

   2. Select option 3 to create a new subscription.

   3. Specify a name and description for the subscription. Then specify the logic app
     URL that you previously copied from the Azure portal.

   4. Select the appropriate event for an application request.

   5. Select 0 to exit the script.

Remove a subscription in version 2107
If you need to delete a subscription, use the following process:

   1. Run the SetupExternalServiceNotifications.ps1 script with option 1 to list the
     available subscriptions. Note the subscription ID, which is an integer value.

<!-- p.1788 -->

   2. Use the NotificationSubscription API of the administration service. Make a DELETE
      call to the URI
      https://<SMSProviderFQDN>/AdminService/v1.0/NotificationSubscription/<Subscrip
      tion_ID> .

      For more information, see How to use the administration service in Configuration
      Manager.

After you remove the subscription, the site doesn't send notifications to the external
system.

Script usage in version 2107
When you run SetupExternalServiceNotifications.ps1, it detects whether it's running on
a site server:

      Y : Continue on the current server

      N : Specify the FQDN of a site server to use

If the script doesn't detect a site server, it prompts for an FQDN.

The following actions are then available:

      0 : Skip/continue
      1 : List available subscriptions

      2 : Create a status filter rule to expose status messages

      3 : Create a subscription. This option is only available for the top-level site.

  ７ Note

  This script is only supported for sites running version 2107 or later.

Next steps
Use the status system

Configure alerts

Feedback

<!-- p.1789 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1790 -->

Monitor scenario health in
Configuration Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

You can use Configuration Manager to monitor the health of end-to-end scenarios.
Monitoring scenario health enhances awareness of system latency and component
backlogs which are critical for cloud service-attached features. Configuration Manager
simulates activities to expose performance metrics and failure points.It simulates
activities to expose performance metrics and failure points. These synthetic activities are
similar to methods that Microsoft uses to monitor some components in its cloud
services. Use this additional data to better understand timeframes for activities. If
failures occur, it can help focus your investigation.

Starting in version 2010, Configuration Manager monitors the health for the following
two scenarios:

      SQL Server Service Broker: Many of the core subsystems in Configuration
      Manager use the service broker.

      Client action health: Monitor the health of the fast channel used for client actions.

In the Configuration Manager console, go to the Monitoring workspace, and select the
Scenario Health node. The list view displays the available scenarios:

                                                                                        

  ７ Note

<!-- p.1791 -->

  If you use a high availability option, scenario health only monitors the active node.
  For the SQL Server Service Broker scenario, it only applies to the primary replica of
  the SQL Server Always On availability group. The client action health scenario only
  applies to the site server in active mode.

Prerequisites
     Full administrator role in Configuration Manager, with scope to the top-level site

Actions for all scenarios
In the Scenario Health node, when you select a scenario, the following actions are
available in the ribbon:

     Show Status: This action is the main one you'll use to view the latest results of
     tests for the scenario. This action opens a window with more information. The top
     section shows the overall status per site. Select a site, to see more detailed status
     for that site in the bottom section.

<!-- p.1792 -->

                                                                                

Scenario Settings: Configure the settings for this scenario: such as whether it's
enabled, and the time interval in minutes.
   Enable activity simulation and measurement: Enable the scenario health
   checks.
   Run time interval (minute): How frequently the site runs the scenario health
   checks. By default, Configuration Manager tests scenarios every 30 minutes.
   Job timeout (minute): How long the site waits for a specific test to complete. By
   default, the timeout is one hour (60 minutes).

History: Display the previous instances of the synthetic transaction. Use this history
to track the scenario's health over time. From the history node, you can also Show
Status of a specific instance.

Run Now: Trigger the site to check the scenario health. If a previous check isn't
successful, you might use this action after you make changes to a site component.
This action creates audit status message ID 54099.

<!-- p.1793 -->

SQL Server Service Broker
The SQL Server Service Broker is a required configuration for the site database. Many of
the core subsystems in Configuration Manager use the service broker.

Configuration Manager includes the following tests for this scenario:

     Ping all sites through SQL Server services broker
     Received ping message
     Received acknowledgment: Check the last update times between the first three
     tests. If there's a long delay, it will impact Configuration Manager performance.
     Check if SQL server service broker queue is enabled: This test makes sure that the
     ConfigMgrHMSQueue is enabled. If the queue is disabled, it will impact many core
     features of Configuration Manager.

  ７ Note

  Not all sites run all tests.

With this health information, you can see how long it takes for SQL Server to exchange
messages via the service broker. A longer delay or timeout shows a backlog in the
processing queue. A failure indicates a larger problem with the service broker, such as
the queue is disabled. Since SQL Server service broker is a core component, issues with
it can impact many other scenarios. For example, client notifications, client status, and
some tenant attach features.

Client action health
Monitor the health of the fast channel used for client actions. If your environment is
tenant attached with devices uploaded, this feature helps you see potential issues with
client actions from the Microsoft Intune admin center. You can also use this feature for
on-premises client actions. For example, CMPivot, run scripts, and device wake-up.

Configuration Manager includes the following tests for this scenario:

     Created client action: Tests that the site can create a client action using the
     administration service.
     CMPivot configuration: Makes sure that CMPivot is correctly configured on the
     central administration site (CAS). For more detail, see rcmctrl.log.
     Client action result: Tests that the CAS receives client action results from primary
     sites. This test can fail if the SQL Server Service Broker is unhealthy, or the site is in

<!-- p.1794 -->

     maintenance mode.
     Processed client action: For more detail, see objreplmgr.log.
     Client action inbox backlog: Checks the backlog for the objmgr.box inbox. If
     there's a large backlog, it impacts how quickly the site sends actions to clients. For
     more detail, see objreplmgr.log.
     Message Processing Engine backlog: Checks the backlog for the message
     processing engine. If there's a large backlog, it impacts how quickly the site
     processes results for client actions. For more detail, see
     SMS_MESSAGE_PROCESSING_ENGINE.log.
     Management point client action backlog: Checks the backlog for the SQL Server
     service broker queue ConfigMgrBGBQueue. If there's a large backlog, it impacts
     how quickly the management point can push actions to clients. Check the scenario
     health for the SQL Server service broker. For more detail, see the management
     point's bgbserver.log.
     Client action result summary: Checks the task to calculate client operation
     summary. For more detail, see statesys.log.
     Management point online status: Checks that management points are online and
     able to send actions to clients. For details, check the management point's
     ccmexec.log, bgbsetup.log, and bgbserver.log.
     Client health summary: Checks the client health scheduled task. For more detail,
     see statesys.log.
     Client state system inbox backlog: Checks the backlog for the inbox
     auth\statesys.box\incoming. If there's a large backlog, it impacts how quickly the
     site processes results for client actions. For more detail, see statesys.log.

  ７ Note

  Not all sites run all tests.

Next steps
Log file reference

Monitor database replication

Feedback
Was this page helpful?    Yes     No

<!-- p.1795 -->

Provide product feedback

<!-- p.1796 -->

Health attestation for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can view the status of Windows 10 Device Health Attestation in the Configuration
Manager console. Device health attestation lets you make sure that client computers
have the following trustworthy BIOS, TPM, and boot software configurations enabled:

      Early-launch antimalware (ELAM) protects your computer when it starts up and
      before third-party drivers initialize. For more information, see theOverview of Early
      Launch AntiMalware.

      Windows BitLocker Drive Encryption encrypts all data stored on the OS and data
      volumes, including removable disks. For more information, see Plan for BitLocker
      management.

      Secure Boot is a security standard to help make sure that a device boots using only
      software that's trusted by the PC manufacturer. For more information, see Secure
      Boot.

      Code Integrity improves OS security by validating the integrity of a driver or system
      file each time it's loaded into memory. For more information, see Enable
      virtualization-based protection of code integrity.

This functionality is available for on-premises resources managed by Configuration
Manager and mobile devices managed with Microsoft Intune. You can specify whether
reporting is done via the cloud or on-premises infrastructure. On-premises device health
attestation monitoring enables you to monitor client PCs without internet access.

Enable health attestation

Requirements
      Client devices running a supported version of Windows 10 or Windows Server
      2016 or later, with Device health attestation enabled.

      TPM 1.2 or TPM 2 enabled devices.

<!-- p.1797 -->

     When using cloud management, communication between the Configuration
     Manager client agent and the management point with has.spserv.microsoft.com
     (port 443) health attestation service. When on-premises, the client needs to
     communicate with the device health attestation-enabled management point.

How to enable health attestation service communication
on Configuration Manager client computers
Use this procedure to enable device health attestation monitoring for devices that
connect to the internet.

   1. In the Configuration Manager console, choose Administration > Overview >
     Client Settings. Select the tab for Computer Agent settings.

   2. In the Default Settings dialog box, select Computer Agent and then scroll down to
     Enable communication with Health Attestation Service.

   3. Set Enable communication with Health Attestation Service to Yes, and then select
     OK.

   4. Target the collections of devices that should report device health.

How to enable on-premises health attestation service
communication on Configuration Manager client
computers
Use this procedure to enable device health attestation monitoring for on-premises
devices that don't connect to the internet.

You can configure the on-premises device health attestation service URL on the
management point to support client devices without internet access.

   1. In the Configuration Manager console, navigate Administration > Overview > Site
     Configuration > Sites.

   2. Right-click the primary or secondary site with the management point that support
     on-premises device health attestation clients, and select Configure site
     components > Management Point. The Management Point Component
     Properties page opens.

   3. On the Advanced Options tab, select Add and specify a valid on-premises device
     health attestation service URL. You can add multiple URLs. If multiple on-premises
     URLs are specified, clients receive the full set and randomly choose which to use.

<!-- p.1798 -->

   4. In the Configuration Manager console, choose Administration > Overview >
     Client Settings. Select the tab for Computer Agent settings.

   5. Scroll down to Enable communication with Health Attestation Service, and set to
     Yes.

   6. Select the Use on-premises Health Attestation Service option, and set to Yes.

   7. Target the collections of devices that should report device health with the client
     agent settings to enable device health attestation reporting.

You can also Edit or Remove device health attestation service URLs.

Monitor device health attestation
To view the device health attestation status, in the Configuration Manager console go to
the Monitoring workspace, expand the Security node, and then select Health
Attestation.

Configuration Manager device health attestation displays the following information:

     Health Attestation Status - Shows the share of devices in compliant,
     noncompliant, error, and unknown states

     Devices Reporting Health Attestation - Shows the percentage of devices
     reporting Health Attestation status

     Noncompliant Devices by Client Type - Shows share of mobile devices and
     computers that are noncompliant

     Top Missing Health Attestation Settings - Shows the number of devices missing
     the health attestation setting, listed per setting

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1799 -->

Monitor database replication
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Monitor details for database replication with the Database Replication node in the
Monitoring workspace of the Configuration Manager console. You can monitor the
status of replication links between sites. It also shows initialization and replication of
replication groups for the site to which you connect.

   Tip

  Although a Database Replication node also appears under the Hierarchy
  Configuration node in the Administration workspace, you can't view the
  replication status for database replication links from that location.

Replication link status
Database replication between sites involves the replication of several sets of
information, called replication groups. Each replication group sends and receives data
with different priorities. By default, you can't modify the data contained in a replication
group and the frequency of replication.

When a replication link is active, and its status isn't failed or degraded, all groups
replicate quickly. If one or more groups fail to complete replication in the expected
period of time, the link displays as degraded. Degraded links can still function, but you
should monitor them to make sure they return to active status. Investigate them to
make sure additional degradation or replication failures don't occur.

For each replication link, specify the number of times that an unsuccessfully replicated
group retries. After this number of retries, the site sets the status of the link to degraded
or failed. Even if all but one group replicates successfully, the site sets the status of the
link to degraded or failed. It sets this status because the one replication group fails to
complete replication in the specified number of attempts. For more information, see the
Database replication thresholds.

Use the following information to understand the status of replication links that might
require further investigation:

Link is active

<!-- p.1800 -->

No problems have been detected, and communication across the link is current.

While a parent site is updating to a new version, and you view the link status from the
child site, the link status displays as active. After the update, until the child site is at the
same version as the parent site, the link status displays as active when viewed from the
parent site. When viewed from the child site, it displays as being configured.

Link is degraded
Replication is functional, but at least one replication object or group is delayed. Monitor
links that are in this state. Review information from both sites on the link for indications
that the link might fail.

A link can also display a status of degraded when the site that receives replicated data is
unable to quickly commit the data to the database. This behavior happens when large
volumes of data replicate. For example, you deploy a software update to a large number
of computers. The parent site on the link might take some time to process this volume
of replicated data. A processing lag at the parent site results in it setting the link status
to degraded until it can successfully process the backlog of data.

Link has failed
Replication isn't functional. It's possible that a replication link might recover without
further action. To investigate and help remediate replication on this link, use the
Replication Link Analyzer (RLA).

This status can also indicate a problem with the physical network between the parent
and child site on the replication link.

Monitor replication status
Use the Database Replication node in the Monitoring workspace to view the status for
a replication link. View details about the database at each site on the replication link.
You can also view details about replication groups. To view these details, select a
replication link, and then select the appropriate tab for the replication status you want
to view.

The following sections give details about the different tabs for replication status:

Summary
