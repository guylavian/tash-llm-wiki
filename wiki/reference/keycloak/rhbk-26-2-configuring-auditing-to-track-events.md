---
title: "Chapter 15. Configuring auditing to track events - Red Hat build of Keycloak 26.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-configuring-auditing-to-track-events
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_administration_guide/configuring_auditing_to_track_events
guide: server_administration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 15. Configuring auditing to track events - Red Hat build of Keycloak 26.2 Server Administration Guide

Chapter 15. Configuring auditing to track events
Red Hat build of Keycloak includes a suite of auditing capabilities. You can record every login and administrator action and review those actions in the Admin Console. Red Hat build of Keycloak also includes a Listener SPI that listens for events and can trigger actions. Examples of built-in listeners include log files and sending emails if an event occurs.
15.1. Auditing user events
You can record and view every event that affects users. Red Hat build of Keycloak triggers login events for actions such as successful user login, a user entering an incorrect password, or a user account updating. By default, Red Hat build of Keycloak does not store or display events in the Admin Console. Only the error events are logged to the Admin Console and the server’s log file.
Procedure
Use this procedure to start auditing user events.
- Click Realm settings in the menu.
- Click the Events tab.
- Click the User events settings tab.
Toggle Save events to ON.
User events settings
- Specify the length of time to store events in the Expiration field.
Click Add saved types to see other events you can save.
Add types
- Click Add.
Click Clear user events when you want to delete all saved events.
Procedure
You can now view events.
Click the Events tab in the menu.
User events
To filter events, click Search user event.
Search user event
15.1.1. Event types
Login events:
| Event | Description |
|---|---|
| Login | A user logs in. |
| Register | A user registers. |
| Logout | A user logs out. |
| Code to Token | An application, or client, exchanges a code for a token. |
| Refresh Token | An application, or client, refreshes a token. |
Brute force protection:
| Event | Description |
|---|---|
| User disabled by permanent lockout | Brute force protection disabled the user account permanently due to too many login failures. |
| User disabled by temporary lockout | Brute force protection disabled the user account temporarily due to too many login failures. |
Identity Brokering:
| Event | Description |
|---|---|
| Federated identity link override | An existing Federated identity link was overridden |
| Federated identity link override error | Error occurred when trying to override an existing Federated identity link |
OAuth:
| Event | Description |
|---|---|
| OAuth2 extension grant | OAuth2 grant was executed |
| OAuth2 extension grant error | Error occurred during OAuth2 grant execution |
Account events:
| Event | Description |
|---|---|
| Social Link | A user account links to a social media provider. |
| Remove Social Link | The link from a social media account to a user account severs. |
| Update Email | An email address for an account changes. |
| Update Profile | A profile for an account changes. |
| Send Password Reset | Red Hat build of Keycloak sends a password reset email. |
| Update Password (deprecated) | The password for an account changes. |
| Update Credential | The password or (time-based) one-time Password (OTP/TOTP) settings for an account changes. |
| Update TOTP (deprecated) | The Time-based One-time Password (TOTP) settings for an account changes. |
| Remove TOTP (deprecated) | Red Hat build of Keycloak removes TOTP from an account. |
| Remove Credential | Red Hat build of Keycloak removes a credential from an account. |
| Send Verify Email | Red Hat build of Keycloak sends an email verification email. |
| Verify Email | Red Hat build of Keycloak verifies the email address for an account. |
Each event has a corresponding error event.
15.1.2. Event listener
Event listeners listen for events and perform actions based on that event. Red Hat build of Keycloak includes two built-in listeners, the Logging Event Listener and Email Event Listener.
15.1.2.1. The logging event listener
When the Logging Event Listener is enabled, this listener writes to a log file when an error event occurs.
An example log message from a Logging Event Listener:
11:36:09,965 WARN [org.keycloak.events] (default task-51) type=LOGIN_ERROR, realmId=master,
clientId=myapp,
userId=19aeb848-96fc-44f6-b0a3-59a17570d374, ipAddress=127.0.0.1,
error=invalid_user_credentials, auth_method=openid-connect, auth_type=code,
redirect_uri=http://localhost:8180/myapp,
code_id=b669da14-cdbb-41d0-b055-0810a0334607, username=admin
You can use the Logging Event Listener to protect against hacker bot attacks:
-
Parse the log file for the
LOGIN_ERROR
event. - Extract the IP Address of the failed login event.
- Send the IP address to an intrusion prevention software framework tool.
The Logging Event Listener logs events to the org.keycloak.events
log category. Red Hat build of Keycloak does not include debug log events in server logs, by default.
To include debug log events in server logs:
-
Change the log level for the
org.keycloak.events
category - Change the log level used by the Logging Event listener.
To change the log level used by the Logging Event listener, add the following:
bin/kc.[sh|bat] start --spi-events-listener-jboss-logging-success-level=info --spi-events-listener-jboss-logging-error-level=error
The valid values for log levels are debug
, info
, warn
, error
, and fatal
.
15.1.2.2. The Email Event Listener
The Email Event Listener sends a message to the user’s email address when an event occurs and supports the following events:
- Login Error.
- Update Password.
- Update Time-based One-time Password (TOTP).
- Remove One-time Password (OTP).
- Update Credential.
- Remove Credential.
Below are the optional events you can configure:
- User disabled by permanent lockout.
- User disabled by temporary lockout.
The following conditions need to be met for an email to be sent:
- User has an email address.
- User’s email address is marked as verified.
Prerequisites
- Realm’s email settings configured.
Procedure
To enable the Email Listener:
- Click Realm settings in the menu.
- Click the Events tab.
- Click the Event listeners field.
Select
email
.Event listeners
You can exclude events by using the --spi-events-listener-email-exclude-events
argument. For example:
kc.[sh|bat] --spi-events-listener-email-exclude-events=UPDATE_CREDENTIAL,REMOVE_CREDENTIAL
To enable optional events, use the following command:
kc.[sh|bat] --spi-events-listener-email-include-events=USER_DISABLED_BY_TEMPORARY_LOCKOUT_ERROR,USER_DISABLED_BY_PERMANENT_LOCKOUT
15.2. Auditing admin events
You can record all actions that are performed by an administrator in the Admin Console. The Admin Console performs administrative actions by invoking the Red Hat build of Keycloak REST interface and Red Hat build of Keycloak audits these REST invocations. You can view the resulting events in the Admin Console.
Procedure
Use this procedure to start auditing admin actions.
- Click Realm settings in the menu.
- Click the Events tab.
- Click the Admin events settings tab.
Toggle Save events to ON.
Red Hat build of Keycloak displays the Include representation switch.
Toggle Include representation to ON.
The
Include Representation
switch includes JSON documents sent through the admin REST API so you can view the administrators actions.Admin events settings
- Click Save.
- To clear the database of stored actions, click Clear admin events.
Procedure
You can now view admin events.
- Click Events in the menu.
Click the Admin events tab.
Admin events
When the Include Representation
switch is ON, it can lead to storing a lot of information in the database. You can set a maximum length of the representation by using the --spi-events-store-jpa-max-field-length
argument. This setting is useful if you want to adhere to the underlying storage limitation. For example:
kc.[sh|bat] --spi-events-store-jpa-max-field-length=2500
