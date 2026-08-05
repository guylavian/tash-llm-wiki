---
title: "Chapter 8. Configuring authentication - Red Hat build of Keycloak 26.4 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-configuring-authentication-server-administration-guide
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_administration_guide/configuring-authentication_server_administration_guide
guide: server_administration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This chapter covers several authentication topics. These topics include: Enforcing strict password and One Time Password (OTP) policies. Managing different credential types. Logging in with Kerberos. Disabling and enabling built-in credential types. 8.1. Password policies When Red Hat build of Keycloak creates a realm, it does not associate password policies with the realm. You can set a simple pa…"
---

# Chapter 8. Configuring authentication - Red Hat build of Keycloak 26.4 Server Administration Guide

Chapter 8. Configuring authentication
This chapter covers several authentication topics. These topics include:
- Enforcing strict password and One Time Password (OTP) policies.
- Managing different credential types.
- Logging in with Kerberos.
- Disabling and enabling built-in credential types.
8.1. Password policies
When Red Hat build of Keycloak creates a realm, it does not associate password policies with the realm. You can set a simple password with no restrictions on its length, security, or complexity. Simple passwords are unacceptable in production environments. Red Hat build of Keycloak has a set of password policies available through the Admin Console.
Procedure
- Click Authentication in the menu.
- Click the Policies tab.
- Select the policy to add in the Add policy drop-down box.
- Enter a value that applies to the policy chosen.
Click Save.
Password policy
After saving the policy, Red Hat build of Keycloak enforces the policy for new users.
The new policy will not be effective for existing users. Therefore, make sure that you set the password policy from the beginning of the realm creation or add "Update password" to existing users or use "Expire password" to make sure that users update their passwords in next "N" days, which will actually adjust to new password policies.
8.1.1. Password policy types
8.1.1.1. HashAlgorithm
Passwords are not stored in cleartext. Before storage or validation, Red Hat build of Keycloak hashes passwords using standard hashing algorithms.
Supported password hashing algorithms are shown in the following table.
| Hashing algorithm | Description |
|---|---|
|
| Argon2 (default for non-FIPS deployments) |
|
| PBKDF2 with SHA512 (default for FIPS deployments) |
|
| PBKDF2 with SHA256 |
|
| PBKDF2 with SHA1 (deprecated) |
It is highly recommended to use Argon2 when possible as it has significantly less CPU requirements compared to PBKDF2, while at the same time being more secure.
The default password hashing algorithm for the server can be configured with --spi-password-hashing--provider-default=<algorithm>
.
To prevent excessive memory and CPU usage, the parallel computation of hashes by Argon2 is by default limited to the number of cores available to the JVM. To configure the Argon2 hashing provider, use its provider options.
See the Server Developer Guide on how to add your own hashing algorithm.
If you change the hashing algorithm, password hashes in storage will not change until the user logs in.
8.1.1.2. Hashing iterations
Specifies the number of times Red Hat build of Keycloak hashes passwords before storage or verification. The default value is -1, which uses the default hashing iterations for the selected hashing algorithm as listed in the following table.
| Hashing algorithm | Default hash iterations |
|---|---|
|
| 5 |
|
| 210,000 |
|
| 600,000 |
|
| 1,300,000 |
In most cases the hashing iterations should not be changed from the recommended default values. Lower values for iterations provide insufficient security, while higher values result in higher CPU power requirements.
8.1.1.3. Digits
The number of numerical digits required in the password string.
8.1.1.4. Lowercase characters
The number of lower case letters required in the password string.
8.1.1.5. Uppercase characters
The number of upper case letters required in the password string.
8.1.1.6. Special characters
The number of special characters required in the password string.
8.1.1.7. Not username
The password cannot be the same as the username.
8.1.1.8. Not email
The password cannot be the same as the email address of the user.
8.1.1.9. Regular expression
Password must match one or more defined Java regular expression patterns. See Java’s regular expression documentation for the syntax of those expressions.
8.1.1.10. Expire password
The number of days the password is valid. When the number of days has expired, the user must change their password.
8.1.1.11. Not recently used
Password cannot be already used by the user. Red Hat build of Keycloak stores a history of used passwords. The number of old passwords stored is configurable in Red Hat build of Keycloak.
8.1.1.12. Not recently used (In Days)
Password cannot be reused within the configured time period (in days). If the new password was last set within this period, the user will be forced to provide a different one.
8.1.1.13. Password blacklist
Password must not be in a blacklist file.
- Blacklist files are UTF-8 plain-text files with Unix line endings. Every line represents a blacklisted password.
- Red Hat build of Keycloak compares passwords in a case-insensitive manner.
-
The value of the blacklist file must be the name of the blacklist file, for example,
100k_passwords.txt
. Blacklist files resolve against
${kc.home.dir}/data/password-blacklists/
by default. Customize this path using:-
The
keycloak.password.blacklists.path
system property. -
The
blacklistsPath
property of thepasswordBlacklist
policy SPI configuration. To configure the blacklist folder using the CLI, use--spi-password-policy--password-blacklist--blacklists-path=/path/to/blacklistsFolder
.
-
The
A note about False Positives
The current implementation uses a BloomFilter for fast and memory efficient containment checks, such as whether a given password is contained in a blacklist, with the possibility for false positives.
-
By default a false positive probability of
0.01%
is used. -
To change the false positive probability by CLI configuration, use
--spi-password-policy--password-blacklist--false-positive-probability=0.00001
.
8.1.1.14. Maximum Authentication Age
Specifies the maximum age of a user authentication in seconds with which the user can update a password without re-authentication. A value of 0
indicates that the user has to always re-authenticate with their current password before they can update the password. See AIA section for some additional details about this policy.
The Maximum Authentication Age is configurable also when configuring the required action Update Password in the Required Actions tab in the Admin Console. The better choice is to use the required action for the configuration because the Maximum Authentication Age password policy might be deprecated/removed in the future.
8.2. One Time Password (OTP) policies
Red Hat build of Keycloak has several policies for setting up a FreeOTP or Google Authenticator One-Time Password generator.
Procedure
- Click Authentication in the menu.
- Click the Policy tab.
- Click the OTP Policy tab.
Otp Policy
Red Hat build of Keycloak generates a QR code on the OTP set-up page, based on information configured in the OTP Policy tab. FreeOTP and Google Authenticator scan the QR code when configuring OTP.
8.2.1. Time-based or counter-based one time passwords
The algorithms available in Red Hat build of Keycloak for your OTP generators are time-based and counter-based.
With Time-Based One Time Passwords (TOTP), the token generator will hash the current time and a shared secret. The server validates the OTP by comparing the hashes within a window of time to the submitted value. TOTPs are valid for a short window of time.
With Counter-Based One Time Passwords (HOTP), Red Hat build of Keycloak uses a shared counter rather than the current time. The Red Hat build of Keycloak server increments the counter with each successful OTP login. Valid OTPs change after a successful login.
TOTP is more secure than HOTP because the matchable OTP is valid for a short window of time, while the OTP for HOTP is valid for an indeterminate amount of time. HOTP is more user-friendly than TOTP because no time limit exists to enter the OTP.
HOTP requires a database update every time the server increments the counter. This update is a performance drain on the authentication server during heavy load. To increase efficiency, TOTP does not remember passwords used, so there is no need to perform database updates. The drawback is that it is possible to reuse TOTPs in the valid time interval.
8.2.2. TOTP configuration options
8.2.2.1. OTP hash algorithm
The default algorithm is SHA1. The other, more secure options are SHA256 and SHA512.
8.2.2.2. Number of digits
The length of the OTP. Short OTPs are user-friendly, easier to type, and easier to remember. Longer OTPs are more secure than shorter OTPs.
8.2.2.3. Look around window
The number of intervals the server attempts to match the hash. This option is present in Red Hat build of Keycloak if the clock of the TOTP generator or authentication server becomes out-of-sync. The default value of 1 is adequate. For example, if the time interval for a token is 30 seconds, the default value of 1 means it will accept valid tokens in the 90-second window (time interval 30 seconds + look ahead 30 seconds + look behind 30 seconds). Every increment of this value increases the valid window by 60 seconds (look ahead 30 seconds + look behind 30 seconds).
8.2.2.4. OTP token period
The time interval in seconds the server matches a hash. Each time the interval passes, the token generator generates a TOTP.
8.2.2.5. Reusable code
Determine whether OTP tokens can be reused in the authentication process or user needs to wait for the next token. Users cannot reuse those tokens by default, and the administrator needs to explicitly specify that those tokens can be reused.
8.2.3. HOTP configuration options
8.2.3.1. OTP hash algorithm
The default algorithm is SHA1. The other, more secure options are SHA256 and SHA512.
8.2.3.2. Number of digits
The length of the OTP. Short OTPs are user-friendly, easier to type, and easier to remember. Longer OTPs are more secure than shorter OTPs.
8.2.3.3. Look around window
The number of previous and following intervals the server attempts to match the hash. This option is present in Red Hat build of Keycloak if the clock of the TOTP generator or authentication server become out-of-sync. The default value of 1 is adequate. This option is present in Red Hat build of Keycloak to cover when the user’s counter gets ahead of the server.
8.2.3.4. Initial counter
The value of the initial counter.
8.3. Authentication flows
An authentication flow is a container of authentications, screens, and actions, during log in, registration, and other Red Hat build of Keycloak workflows.
8.3.1. Built-in flows
Red Hat build of Keycloak has several built-in flows. You cannot modify these flows, but you can alter the flow’s requirements to suit your needs.
Procedure
- Click Authentication in the menu.
- Click on the Browser item in the list to see the details.
Browser flow
8.3.1.1. Auth type
The name of the authentication or the action to execute. If an authentication is indented, it is in a sub-flow. It may or may not be executed, depending on the behavior of its parent.
Cookie
The first time a user logs in successfully, Red Hat build of Keycloak sets a session cookie. If the cookie is already set, this authentication type is successful. Since the cookie provider returned success and each execution at this level of the flow is alternative, Red Hat build of Keycloak does not perform any other execution. This results in a successful login.
Kerberos
This authenticator is disabled by default and is skipped during the Browser Flow.
Identity Provider Redirector
This action is configured through the Actions > Config link. It redirects to another IdP for identity brokering.
Forms
Since this sub-flow is marked as alternative, it will not be executed if the Cookie authentication type passed. This sub-flow contains an additional authentication type that needs to be executed. Red Hat build of Keycloak loads the executions for this sub-flow and processes them.
The first execution is the Username Password Form, an authentication type that renders the username and password page. It is marked as required, so the user must enter a valid username and password.
The second execution is the Browser - Conditional 2FA sub-flow. This sub-flow is conditional and executes depending on the result of the Condition - User Configured and Condition - credential execution. If the result is true, Red Hat build of Keycloak loads the executions for this sub-flow and processes them.
The next execution is the Condition - User Configured authentication. This authentication checks if Red Hat build of Keycloak has configured other executions in the flow for the user. The Browser - Conditional 2FA sub-flow executes only when the user has a configured OTP credential.
The next execution is the Condition - credential authentication. The step checks if the authentication process has already authenticated the user with a passwordless WebAuthn credential (passkey), avoiding 2FA in that case.
The final execution is the OTP Form. Red Hat build of Keycloak marks this execution as alternative, but it runs only when the user has an OTP credential set up because of the setup in the conditional sub-flow. If the OTP credential is not set up, the user does not see an OTP form.
The default browser flow contains two more executions inside the Browser - Conditional 2FA, WebAuthn Authenticator and Recovery Authentication Code Form. These executions are Disabled by default and they are the other 2FA methods that can be added to the flow. Change the requirement from Disabled to Alternative to make them available if the respective credential has been configured for the user. If the user has configured all alternative credential types, the credential with the highest priority is displayed by default. However, the Try Another Way option will appear so that the user has the alternative methods to log in.
8.3.1.2. Requirement
A drop-down menu that controls the execution of an action.
- Required
- All Required elements in the flow must be successfully sequentially executed. The flow terminates if a required element fails.
- Alternative
- Only a single element must successfully execute for the flow to evaluate as successful. Because the Required flow elements are sufficient to mark a flow as successful, any Alternative flow element within a flow containing Required flow elements will not execute.
- Disabled
- The element does not count to mark a flow as successful.
- Conditional
This requirement type is only set on sub-flows.
- A Conditional sub-flow contains executions. These executions must evaluate to logical statements.
- If all executions evaluate as true, the Conditional sub-flow acts as Required.
- If any executions evaluate as false, the Conditional sub-flow acts as Disabled.
- If you do not set an execution, the Conditional sub-flow acts as Disabled.
- If a flow contains executions and the flow is not set to Conditional, Red Hat build of Keycloak does not evaluate the executions, and the executions are considered functionally Disabled.
8.3.2. Creating flows
Important functionality and security considerations apply when you design a flow.
To create a flow, perform the following:
Procedure
- Click Authentication in the menu.
- Click Create flow.
You can copy and then modify an existing flow. Click the "Action list" (the three dots at the end of the row), click Duplicate, and enter a name for the new flow.
When creating a new flow, you must create a top-level flow first with the following options:
- Name
- The name of the flow.
- Description
- The description you can set to the flow.
- Top-Level Flow Type
- The type of flow. The type client is used only for the authentication of clients (applications). For all other cases, choose basic.
Create a top-level flow
When Red Hat build of Keycloak has created the flow, Red Hat build of Keycloak displays the Add step, and Add sub-flow buttons.
An empty new flow
Three factors determine the behavior of flows and sub-flows.
- The structure of the flow and sub-flows.
- The executions within the flows
- The requirements set within the sub-flows and the executions.
Executions have a wide variety of actions, from sending a reset email to validating an OTP. Add executions with the Add step button.
Adding an authentication execution
Authentication executions can optionally have a reference value configured. This can be utilized by the Authentication Method Reference (AMR) protocol mapper to populate the amr claim in OIDC access and ID tokens (for more information on the AMR claim, see RFC-8176). When the Authentication Method Reference (AMR) protocol mapper is configured for a client, it will populate the amr claim with the reference value for any authenticator execution the user successfully completes during the authentication flow.
Adding an authenticator reference value
Two types of executions exist, automatic executions and interactive executions. Automatic executions are similar to the Cookie execution and will automatically perform their action in the flow. Interactive executions halt the flow to get input. Executions executing successfully set their status to success. For a flow to complete, it needs at least one execution with a status of success.
You can add sub-flows to top-level flows with the Add sub-flow button. The Add sub-flow button displays the Create Execution Flow page. This page is similar to the Create Top Level Form page. The difference is that the Flow Type can be basic (default) or form. The form type constructs a sub-flow that generates a form for the user, similar to the built-in Registration flow. Sub-flows success depends on how their executions evaluate, including their contained sub-flows. See the execution requirements section for an in-depth explanation of how sub-flows work.
After adding an execution, check the requirement has the correct value.
All elements in a flow have a Delete option next to the element. Some executions have a ⚙️ menu item (the gear icon) to configure the execution. It is also possible to add executions and sub-flows to sub-flows with the Add step and Add sub-flow links.
Since the order of execution is important, you can move executions and sub-flows up and down by dragging their names.
Make sure to properly test your configuration when you configure the authentication flow to confirm that no security holes exist in your setup. We recommend that you test various corner cases. For example, consider testing the authentication behavior for a user when you remove various credentials from the user’s account before authentication.
As an example, when 2nd-factor authenticators, such as OTP Form or WebAuthn Authenticator, are configured in the flow as REQUIRED and the user does not have credential of particular type, the user will be able to set up the particular credential during authentication itself. This situation means that the user does not authenticate with this credential as he set up it right during the authentication. So for browser authentication, make sure to configure your authentication flow with some 1st-factor credentials such as Password or WebAuthn Passwordless Authenticator.
8.3.3. Creating a password-less browser login flow
To illustrate the creation of flows, this section describes creating an advanced browser login flow. The purpose of this flow is to allow a user a choice between logging in using a password-less manner with WebAuthn, or two-factor authentication with a password and OTP.
Procedure
- Click Authentication in the menu.
- Click the Flows tab.
- Click Create flow.
-
Enter
Browser Password-less
as a name. - Click Create.
- Click Add execution.
- Select Cookie from the list.
- Click Add.
- Select Alternative for the Cookie authentication type to set its requirement to alternative.
- Click Add step.
- Select Kerberos from the list.
- Click Add.
- Click Add step.
- Select Identity Provider Redirector from the list.
- Click Add.
- Select Alternative for the Identity Provider Redirector authentication type to set its requirement to alternative.
- Click Add sub-flow.
- Enter Forms as a name.
- Click Add.
Select Alternative for the Forms authentication type to set its requirement to alternative.
The common part with the browser flow
- Click + menu of the Forms execution.
- Select Add step.
- Select Username Form from the list.
- Click Add.
At this stage, the form requires a username but no password. We must enable password authentication to avoid security risks.
- Click + menu of the Forms sub-flow.
- Click Add sub-flow.
-
Enter
Authentication
as name. - Click Add.
- Select Required for the Authentication authentication type to set its requirement to required.
- Click + menu of the Authentication sub-flow.
- Click Add step.
- Select WebAuthn Passwordless Authenticator from the list.
- Click Add.
- Select Alternative for the Webauthn Passwordless Authenticator authentication type to set its requirement to alternative.
- Click + menu of the Authentication sub-flow.
- Click Add sub-flow.
-
Enter
Password with OTP
as name. - Click Add.
- Select Alternative for the Password with OTP authentication type to set its requirement to alternative.
- Click + menu of the Password with OTP sub-flow.
- Click Add step.
- Select Password Form from the list.
- Click Add.
- Select Required for the Password Form authentication type to set its requirement to required.
- Click + menu of the Password with OTP sub-flow.
- Click Add step.
- Select OTP Form from the list.
- Click Add.
- Click Required for the OTP Form authentication type to set its requirement to required.
Finally, change the bindings.
- Click the Action menu at the top of the screen.
- Select Bind flow from the menu.
- Click the Browser Flow drop-down list.
- Click Save.
A password-less browser login
After entering the username, the flow works as follows:
If users have WebAuthn passwordless credentials recorded, they can use these credentials to log in directly. This is the password-less login. The user can also select Password with OTP because the WebAuthn Passwordless
execution and the Password with OTP
flow are set to Alternative. If they are set to Required, the user has to enter WebAuthn, password, and OTP.
If the user selects the Try another way link with WebAuthn passwordless
authentication, the user can choose between Password
and Passkey
(WebAuthn passwordless). When selecting the password, the user will need to continue and log in with the assigned OTP. If the user has no WebAuthn credentials, the user must enter the password and then the OTP. If the user has no OTP credential, they will be asked to record one.
Since the WebAuthn Passwordless execution is set to Alternative rather than Required, this flow will never ask the user to register a WebAuthn credential. For a user to have a Webauthn credential, an administrator must add a required action to the user. Do this by:
- Enabling the Webauthn Register Passwordless required action in the realm (see the WebAuthn documentation).
- Setting the required action using the Credential Reset part of a user’s Credentials management menu.
Creating an advanced flow such as this can have side effects. For example, if you enable the ability to reset the password for users, this would be accessible from the password form. In the default Reset Credentials
flow, users must enter their username. Since the user has already entered a username earlier in the Browser Password-less
flow, this action is unnecessary for Red Hat build of Keycloak and suboptimal for user experience. To correct this problem, you can:
-
Duplicate the
Reset Credentials
flow. Set its name toReset Credentials for password-less
, for example. - Click Delete (trash icon) of the Choose user step.
- In the Action menu, select Bind flow and select Reset credentials flow from the dropdown and click Save
8.3.4. Using Client Policies to Select an Authentication Flow
Client Policies can be used to dynamically select an Authentication Flow based on specific conditions, such as requesting a particular scope or an ACR (Authentication Context Class Reference) using the AuthenticationFlowSelectorExecutor
in combination with the condition you prefer.
The AuthenticationFlowSelectorExecutor
allows you to select an appropriate authentication flow and set the level of authentication to be applied once the selected flow is completed.
A possible configuration involves using the ACRCondition
in combination with the AuthenticationFlowSelectorExecutor
. This setup enables you to select an authentication flow based on the requested ACR and have the ACR value included in the token using ACR to LoA Mapping.
For more details, see Client Policies.
8.3.5. Creating a browser login flow with step-up mechanism
This section describes how to create advanced browser login flow using the step-up mechanism. The purpose of step-up authentication is to allow access to clients or resources based on a specific authentication level of a user.
Procedure
- Click Authentication in the menu.
- Click the Flows tab.
- Click Create flow.
-
Enter
Browser Incl Step up Mechanism
as a name. - Click Save.
- Click Add execution.
- Select Cookie from the list.
- Click Add.
- Select Alternative for the Cookie authentication type to set its requirement to alternative.
- Click Add sub-flow.
- Enter Auth Flow as a name.
- Click Add.
- Click Alternative for the Auth Flow authentication type to set its requirement to alternative.
Now you configure the flow for the first authentication level.
- Click + menu of the Auth Flow.
- Click Add sub-flow.
-
Enter
1st Condition Flow
as a name. - Click Add.
- Click Conditional for the 1st Condition Flow authentication type to set its requirement to conditional.
- Click + menu of the 1st Condition Flow.
- Click Add condition.
- Select Conditional - Level Of Authentication from the list.
- Click Add.
- Click Required for the Conditional - Level Of Authentication authentication type to set its requirement to required.
- Click ⚙️ (gear icon).
-
Enter
Level 1
as an alias. -
Enter
1
for the Level of Authentication (LoA). -
Set Max Age to 36000. This value is in seconds and it is equivalent to 10 hours, which is the default
SSO Session Max
timeout set in the realm. As a result, when a user authenticates with this level, subsequent SSO logins can reuse this level and the user does not need to authenticate with this level until the end of the user session, which is 10 hours by default. Click Save
Configure the condition for the first authentication level
- Click + menu of the 1st Condition Flow.
- Click Add step.
- Select Username Password Form from the list.
- Click Add.
Now you configure the flow for the second authentication level.
- Click + menu of the Auth Flow.
- Click Add sub-flow.
-
Enter
2nd Condition Flow
as an alias. - Click Add.
- Click Conditional for the 2nd Condition Flow authentication type to set its requirement to conditional.
- Click + menu of the 2nd Condition Flow.
- Click Add condition.
- Select Conditional - Level Of Authentication from the item list.
- Click Add.
- Click Required for the Conditional - Level Of Authentication authentication type to set its requirement to required.
- Click ⚙️ (gear icon).
-
Enter
Level 2
as an alias. -
Enter
2
for the Level of Authentication (LoA). - Set Max Age to 0. As a result, when a user authenticates, this level is valid just for the current authentication, but not any subsequent SSO authentications. So the user will always need to authenticate again with this level when this level is requested.
Click Save
Configure the condition for the second authentication level
- Click + menu of the 2nd Condition Flow.
- Click Add step.
- Select OTP Form from the list.
- Click Add.
- Click Required for the OTP Form authentication type to set its requirement to required.
Finally, change the bindings.
- Click the Action menu at the top of the screen.
- Select Bind flow from the list.
- Select Browser Flow in the dropdown.
- Click Save.
Browser login with step-up mechanism
Request a certain authentication level
To use the step-up mechanism, you specify a requested level of authentication (LoA) in your authentication request. The claims
parameter is used for this purpose:
https://{DOMAIN}/realms/{REALMNAME}/protocol/openid-connect/auth?client_id={CLIENT-ID}&redirect_uri={REDIRECT-URI}&scope=openid&response_type=code&response_mode=query&nonce=exg16fxdjcu&claims=%7B%22id_token%22%3A%7B%22acr%22%3A%7B%22essential%22%3Atrue%2C%22values%22%3A%5B%22gold%22%5D%7D%7D%7D
The claims
parameter is specified in a JSON representation:
claims= {
"id_token": {
"acr": {
"essential": true,
"values": ["gold"]
}
}
}
The Red Hat build of Keycloak javascript adapter has support for easy construct of this JSON and sending it in the login request. See Keycloak JavaScript adapter in the securing apps section for more details.
You can also use simpler parameter acr_values
instead of claims
parameter to request particular levels as non-essential. This is mentioned in the OIDC specification.
You can also configure the default level for the particular client, which is used when the parameter acr_values
or the parameter claims
with the acr
claim is not present. For further details, see Client ACR configuration).
To request the acr_values as text (such as gold
) instead of a numeric value, you configure the mapping between the ACR and the LoA. It is possible to configure it at the realm level (recommended) or at the client level. For configuration see ACR to LoA Mapping.
For more details see the official OIDC specification.
Flow logic
The logic for the previous configured authentication flow is as follows:
If a client request a high authentication level, meaning Level of Authentication 2 (LoA 2), a user has to perform full 2-factor authentication: Username/Password + OTP. However, if a user already has a session in Red Hat build of Keycloak, that was logged in with username and password (LoA 1), the user is only asked for the second authentication factor (OTP).
The option Max Age in the condition determines how long (how much seconds) the subsequent authentication level is valid. This setting helps to decide whether the user will be asked to present the authentication factor again during a subsequent authentication. If the particular level X is requested by the claims
or acr_values
parameter and user already authenticated with level X, but it is expired (for example max age is configured to 300 and user authenticated before 310 seconds) then the user will be asked to re-authenticate again with the particular level. However if the level is not yet expired, the user will be automatically considered as authenticated with that level.
Using Max Age with the value 0 means, that particular level is valid just for this single authentication. Hence every re-authentication requesting that level will need to authenticate again with that level. This is useful for operations that require higher security in the application (e.g. send payment) and always require authentication with the specific level.
Note that parameters such as claims
or acr_values
might be changed by the user in the URL when the login request is sent from the client to the Red Hat build of Keycloak via the user’s browser. This situation can be mitigated if client uses PAR (Pushed authorization request), a request object, or other mechanisms that prevents the user from rewrite the parameters in the URL. Hence after the authentication, clients are encouraged to check the ID Token to double-check that acr
in the token corresponds to the expected level.
If no explicit level is requested by parameters, the Red Hat build of Keycloak will require the authentication with the first LoA condition found in the authentication flow, such as the Username/Password in the preceding example. When a user was already authenticated with that level and that level expired, the user is not required to re-authenticate, but acr
in the token will have the value 0. This result is considered as authentication based solely on long-lived browser cookie
as mentioned in the section 2 of OIDC Core 1.0 specification.
During the first authentication of the user, the first configured subflow with the Conditional - Level Of Authentication is always executed (regardless of the requested level) as the user does not yet have any level. Therefore, we recommend that the first level subflow contains the minimal required authenticators for user authentication. In addition, ensure that the subflows with different values of Conditional - Level Of Authentication are ordered starting with the lowest as shown in the example above. For example, if you configure a subflow with level 2 and then add another subflow with level 1, the level 2 subflow will be always asked during the first authentication, which may not be the desired behavior.
A conflict situation may arise when an admin specifies several flows, sets different LoA levels to each, and assigns the flows to different clients. However, the rule is always the same: if a user has a certain level, it needs only have that level to connect to a client. It’s up to the admin to make sure that the LoA is coherent.
Step-up authentication with Level of Authentication conditions is intended for use cases where each level requires all authentication methods from the preceding levels. For instance, level X must always include all authentication methods required by level X-1. For use cases where a specific level, such as level 3, requires a different authentication method from the previous levels, it may be more appropriate to use mapping of ACR to a specific flow. For more details, see Using Client Policies to Select an Authentication Flow.
Example scenario
- Max Age is configured as 300 seconds for level 1 condition.
-
Login request is sent without requesting any acr. Level 1 will be used and the user needs to authenticate with username and password. The token will have
acr=1
. -
Another login request is sent after 100 seconds. The user is automatically authenticated due to the SSO and the token will return
acr=1
. -
Another login request is sent after another 201 seconds (301 seconds since authentication in point 2). The user is automatically authenticated due to the SSO, but the token will return
acr=0
due the level 1 is considered expired. -
Another login request is sent, but now it will explicitly request ACR of level 1 in the
claims
parameter. User will be asked to re-authenticate with username/password and thenacr=1
will be returned in the token.
ACR claim in the token
ACR claim is added to the token by the acr loa level
protocol mapper defined in the acr
client scope. This client scope is the realm default client scope and hence will be added to all newly created clients in the realm.
In case you do not want acr
claim inside tokens or you need some custom logic for adding it, you can remove the client scope from your client.
Note when the login request initiates a request with the claims
parameter requesting acr
as essential
claim, then Red Hat build of Keycloak will always return one of the specified levels. If it is not able to return one of the specified levels (For example if the requested level is unknown or bigger than configured conditions in the authentication flow), then Red Hat build of Keycloak will throw an error.
8.3.6. Registration or Reset credentials requested by client
Usually when the user is redirected to the Red Hat build of Keycloak from client application, the browser
flow is triggered. This flow may allow the user to register in case that realm registration is enabled and the user clicks Register
on the login screen. Also, if Forget password is enabled for the realm, the user can click Forget password
on the login screen, which triggers the Reset credentials
flow where users can reset credentials after email address confirmation.
Sometimes it can be useful for the client application to directly redirect the user to the Registration screen or to the Reset credentials flow. The resulting action will match the action of when the user clicks Register or Forget password on the normal login screen. Automatic redirect to the registration or reset-credentials screen can be done as follows:
-
When the client wants the user to be redirected directly to the registration, the OIDC client should add parameter
prompt=create
to the login request. As a deprecated alternative, clients can replace the very last snippet from the OIDC login URL path (/auth
) with/registrations
. So the full URL might be similar to the following:https://keycloak.example.com/realms/your_realm/protocol/openid-connect/registrations
. Theprompt=create
is recommended as it is a specification standard. -
When the client wants a user to be redirected directly to the
Reset credentials
flow, the OIDC client should replace the very last snippet from the OIDC login URL path (/auth
) with/forgot-credentials
.
The preceding steps are the only supported method for a client to directly request a registration or reset-credentials flow. For security purposes, it is not supported and recommended for client applications to bypass OIDC/SAML flows and directly redirect to other Red Hat build of Keycloak endpoints (such as for instance endpoints under /realms/realm_name/login-actions
or /realms/realm_name/broker
).
8.4. User session limits
Limits on the number of session that a user can have can be configured. Sessions can be limited per realm or per client.
To add session limits to a flow, perform the following steps.
- Click Add step for the flow.
- Select User session count limiter from the item list.
- Click Add.
- Click Required for the User Session Count Limiter authentication type to set its requirement to required.
- Click ⚙️ (gear icon) for the User Session Count Limiter.
- Enter an alias for this config.
- Enter the required maximum number of sessions that a user can have in this realm. For example, if 2 is the value, 2 SSO sessions is the maximum that each user can have in this realm. If 0 is the value, this check is disabled.
-
Enter the required maximum number of sessions a user can have for the client. For example, if 2 is the value, then 2 SSO sessions is the maximum in this realm for each client. So when a user is trying to authenticate to client
foo
, but that user has already authenticated in 2 SSO sessions to clientfoo
, either the authentication will be denied or an existing sessions will be killed based on the behavior configured. If a value of 0 is used, this check is disabled. If both session limits and client session limits are enabled, it makes sense to have client session limits to be always lower than session limits. The limit per client can never exceed the limit of all SSO sessions of this user. Select the behavior that is required when the user tries to create a session after the limit is reached. Available behaviors are:
- Deny new session - when a new session is requested and the session limit is reached, no new sessions can be created.
- Terminate oldest session - when a new session is requested and the session limit has been reached, the oldest session will be removed and the new session created.
- Optionally, add a custom error message to be displayed when the limit is reached.
Note that the user session limits should be added to your bound Browser flow, Direct grant flow, Reset credentials and also to any Post broker login flow. The authenticator should be added at the point when the user is already known during authentication (usually at the end of the authentication flow) and should be typically REQUIRED. Note that it is not possible to have ALTERNATIVE and REQUIRED executions at the same level.
For most of authenticators like Direct grant flow
, Reset credentials
or Post broker login flow
, it is recommended to add the authenticator as REQUIRED at the end of the authentication flow. Here is an example for the Reset credentials
flow:
For Browser
flow, consider not adding the Session Limits authenticator at the top level flow. This recommendation is due to the Cookie
authenticator, which automatically re-authenticates users based on SSO cookie. It is at the top level and it is better to not check session limits during SSO re-authentication because a user session already exists. So instead, consider adding a separate ALTERNATIVE subflow, such as the following authenticate-user-with-session-limit
example at the same level like Cookie
. Then you can add a REQUIRED subflow, in the following real-authentication-subflow`example, as a nested subflow of `authenticate-user-with-session-limit
and add a User Session Limit
at the same level as well. Inside the real-authentication-subflow
, you can add real authenticators in a similar fashion to the default browser flow. The following example flow allows to users to authenticate with an identity provider or with password and OTP:
Regarding Post Broker login flow
, you can add the User Session Limits
as the only authenticator in the authentication flow as long as you have no other authenticators that you trigger after authentication with your identity provider. However, make sure that this flow is configured as Post Broker Flow
at your identity providers. This requirement exists needed so that the authentication with Identity providers also participates in the session limits.
Currently, the administrator is responsible for maintaining consistency between the different configurations. So make sure that all your flows use same the configuration of User Session Limits
.
User session limit feature is not available for CIBA.
8.5. Kerberos
Red Hat build of Keycloak supports login with a Kerberos ticket through the Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO) protocol. SPNEGO authenticates transparently through the web browser after the user authenticates the session. For non-web cases, or when a ticket is not available during login, Red Hat build of Keycloak supports login with Kerberos username and password.
A typical use case for web authentication is the following:
- The user logs into the desktop.
- The user accesses a web application secured by Red Hat build of Keycloak using a browser.
- The application redirects to Red Hat build of Keycloak login.
-
Red Hat build of Keycloak renders the HTML login screen with status 401 and HTTP header
WWW-Authenticate: Negotiate
-
If the browser has a Kerberos ticket from desktop login, the browser transfers the desktop sign-on information to Red Hat build of Keycloak in header
Authorization: Negotiate 'spnego-token'
. Otherwise, it displays the standard login screen, and the user enters the login credentials. - Red Hat build of Keycloak validates the token from the browser and authenticates the user.
- If using LDAPFederationProvider with Kerberos authentication support, Red Hat build of Keycloak provisions user data from LDAP. If using KerberosFederationProvider, Red Hat build of Keycloak lets the user update the profile and pre-fill login data.
- Red Hat build of Keycloak returns to the application. Red Hat build of Keycloak and the application communicate through OpenID Connect or SAML messages. Red Hat build of Keycloak acts as a broker to Kerberos/SPNEGO login. Therefore Red Hat build of Keycloak authenticating through Kerberos is hidden from the application.
The Negotiate www-authenticate scheme allows NTLM as a fallback to Kerberos and on some web browsers in Windows NTLM is supported by default. If a www-authenticate challenge comes from a server outside a browsers permitted list, users may encounter an NTLM dialog prompt. A user would need to click the cancel button on the dialog to continue as Red Hat build of Keycloak does not support this mechanism. This situation can happen if Intranet web browsers are not strictly configured or if Red Hat build of Keycloak serves users in both the Intranet and Internet. A custom authenticator can be used to restrict Negotiate challenges to a whitelist of hosts.
Perform the following steps to set up Kerberos authentication:
- The setup and configuration of the Kerberos server (KDC).
- The setup and configuration of the Red Hat build of Keycloak server.
- The setup and configuration of the client machines.
8.5.1. Setup of Kerberos server
The steps to set up a Kerberos server depends on the operating system (OS) and the Kerberos vendor. Consult Windows Active Directory, MIT Kerberos, and your OS documentation for instructions on setting up and configuring a Kerberos server.
During setup, perform these steps:
- Add some user principals to your Kerberos database. You can also integrate your Kerberos with LDAP, so user accounts provision from the LDAP server.
Add service principal for "HTTP" service. For example, if the Red Hat build of Keycloak server runs on
www.mydomain.org
, add the service principalHTTP/www.mydomain.org@<kerberos realm>
.On MIT Kerberos, you run a "kadmin" session. On a machine with MIT Kerberos, you can use the command:
sudo kadmin.local
Then, add HTTP principal and export its key to a keytab file with commands such as:
addprinc -randkey HTTP/www.mydomain.org@MYDOMAIN.ORG
ktadd -k /tmp/http.keytab HTTP/www.mydomain.org@MYDOMAIN.ORG
Ensure the keytab file /tmp/http.keytab
is accessible on the host where Red Hat build of Keycloak is running.
8.5.2. Setup and configuration of Red Hat build of Keycloak server
Install a Kerberos client on your machine.
Procedure
- Install a Kerberos client. If your machine runs Fedora, Ubuntu, or RHEL, install the freeipa-client package, containing a Kerberos client and other utilities.
Configure the Kerberos client (on Linux, the configuration settings are in the /etc/krb5.conf file ).
Add your Kerberos realm to the configuration and configure the HTTP domains your server runs on.
For example, for the MYDOMAIN.ORG realm, you can configure the
domain_realm
section like this:[domain_realm] .mydomain.org = MYDOMAIN.ORG mydomain.org = MYDOMAIN.ORG
Export the keytab file with the HTTP principal and ensure the file is accessible to the process running the Red Hat build of Keycloak server. For production, ensure that the file is readable by this process only.
For the MIT Kerberos example above, we exported keytab to the
/tmp/http.keytab
file. If your Key Distribution Centre (KDC) and Red Hat build of Keycloak run on the same host, the file is already available.
8.5.2.1. Enabling SPNEGO processing
By default, Red Hat build of Keycloak disables SPNEGO protocol support. To enable it, go to the browser flow and enable Kerberos.
Browser flow
Set the Kerberos requirement from disabled to alternative (Kerberos is optional) or required (browser must have Kerberos enabled). If you have not configured the browser to work with SPNEGO or Kerberos, Red Hat build of Keycloak falls back to the regular login screen.
8.5.2.2. Configure Kerberos user storage federation providers
You must now use User Storage Federation to configure how Red Hat build of Keycloak interprets Kerberos tickets. Two different federation providers exist with Kerberos authentication support.
To authenticate with Kerberos backed by an LDAP server, configure the LDAP Federation Provider.
Procedure
Go to the configuration page for your LDAP provider.
Ldap kerberos integration
- Toggle Allow Kerberos authentication to ON
Allow Kerberos authentication makes Red Hat build of Keycloak use the Kerberos principal access user information so information can import into the Red Hat build of Keycloak environment.
If an LDAP server is not backing up your Kerberos solution, use the Kerberos User Storage Federation Provider.
Procedure
- Click User Federation in the menu.
Select Kerberos from the Add provider select box.
Kerberos user storage provider
The Kerberos provider parses the Kerberos ticket for simple principal information and imports the information into the local Red Hat build of Keycloak database. User profile information, such as first name, last name, and email, are not provisioned.
8.5.3. Setup and configuration of client machines
Client machines must have a Kerberos client and set up the krb5.conf
as described above. The client machines must also enable SPNEGO login support in their browser. See configuring Firefox for Kerberos if you are using the Firefox browser.
The .mydomain.org
URI must be in the network.negotiate-auth.trusted-uris
configuration option.
In Windows domains, clients do not need to adjust their configuration. Internet Explorer and Edge can already participate in SPNEGO authentication.
8.5.4. Credential delegation
Kerberos supports the credential delegation. Applications may need access to the Kerberos ticket so they can reuse it to interact with other services secured by Kerberos. Because the Red Hat build of Keycloak server processed the SPNEGO protocol, you must propagate the GSS credential to your application within the OpenID Connect token claim or a SAML assertion attribute. Red Hat build of Keycloak transmits this to your application from the Red Hat build of Keycloak server. To insert this claim into the token or assertion, each application must enable the built-in protocol mapper gss delegation credential
. This mapper is available in the Mappers tab of the application’s client page. See Protocol Mappers chapter for more details.
Applications must deserialize the claim it receives from Red Hat build of Keycloak before using it to make GSS calls against other services. When you deserialize the credential from the access token to the GSSCredential object, create the GSSContext with this credential passed to the GSSManager.createContext
method. For example:
// Obtain accessToken in your application.
KeycloakPrincipal keycloakPrincipal = (KeycloakPrincipal) servletReq.getUserPrincipal();
AccessToken accessToken = keycloakPrincipal.getKeycloakSecurityContext().getToken();
// Retrieve Kerberos credential from accessToken and deserialize it
String serializedGssCredential = (String) accessToken.getOtherClaims().
get(org.keycloak.common.constants.KerberosConstants.GSS_DELEGATION_CREDENTIAL);
GSSCredential deserializedGssCredential = org.keycloak.common.util.KerberosSerializationUtils.
deserializeCredential(serializedGssCredential);
// Create GSSContext to call other Kerberos-secured services
GSSContext context = gssManager.createContext(serviceName, krb5Oid,
deserializedGssCredential, GSSContext.DEFAULT_LIFETIME);
Configure forwardable
Kerberos tickets in krb5.conf
file and add support for delegated credentials to your browser.
Credential delegation has security implications, so use it only if necessary and only with HTTPS. See this article for more details and an example.
8.5.5. Cross-realm trust
In the Kerberos protocol, the realm
is a set of Kerberos principals. The definition of these principals exists in the Kerberos database, which is typically an LDAP server.
The Kerberos protocol allows cross-realm trust. For example, if 2 Kerberos realms, A and B, exist, then cross-realm trust will allow the users from realm A to access realm B’s resources. Realm B trusts realm A.
Kerberos cross-realm trust
The Red Hat build of Keycloak server supports cross-realm trust. To implement this, perform the following:
-
Configure the Kerberos servers for the cross-realm trust. Implementing this step depends on the Kerberos server implementations. This step is necessary to add the Kerberos principal
krbtgt/B@A
to the Kerberos databases of realm A and B. This principal must have the same keys on both Kerberos realms. The principals must have the same password, key version numbers, and ciphers in both realms. Consult the Kerberos server documentation for more details.
The cross-realm trust is unidirectional by default. You must add the principal krbtgt/A@B
to both Kerberos databases for bidirectional trust between realm A and realm B. However, trust is transitive by default. If realm B trusts realm A and realm C trusts realm B, then realm C trusts realm A without the principal, krbtgt/C@A
, available. Additional configuration (for example, capaths
) may be necessary on the Kerberos client-side so clients can find the trust path. Consult the Kerberos documentation for more details.
Configure Red Hat build of Keycloak server
-
When using an LDAP storage provider with Kerberos support, configure the server principal for realm B, as in this example:
HTTP/mydomain.com@B
. The LDAP server must find the users from realm A if users from realm A are to successfully authenticate to Red Hat build of Keycloak, because Red Hat build of Keycloak must perform the SPNEGO flow and then find the users.
-
When using an LDAP storage provider with Kerberos support, configure the server principal for realm B, as in this example:
Finding users is based on the LDAP storage provider option Kerberos principal attribute
. When this is configured for instance with value like userPrincipalName
, then after SPNEGO authentication of user john@A
, Red Hat build of Keycloak will try to lookup LDAP user with attribute userPrincipalName
equivalent to john@A
. If Kerberos principal attribute
is left empty, then Red Hat build of Keycloak will lookup the LDAP user based on the prefix of his kerberos principal with the realm omitted. For example, Kerberos principal user john@A
must be available in the LDAP under username john
, so typically under an LDAP DN such as uid=john,ou=People,dc=example,dc=com
. If you want users from realm A and B to authenticate, ensure that LDAP can find users from both realms A and B.
-
When using a Kerberos user storage provider (typically, Kerberos without LDAP integration), configure the server principal as
HTTP/mydomain.com@B
, and users from Kerberos realms A and B must be able to authenticate.
Users from multiple Kerberos realms are allowed to authenticate as every user would have attribute KERBEROS_PRINCIPAL
referring to the kerberos principal used for authentication and this is used for further lookups of this user. To avoid conflicts when there is user john
in both kerberos realms A
and B
, the username of the Red Hat build of Keycloak user might contain the kerberos realm lowercased. For instance username would be john@a
. Just in case when realm matches with the configured Kerberos realm
, the realm suffix might be omitted from the generated username. For instance username would be john
for the Kerberos principal john@A
as long as the Kerberos realm
is configured on the Kerberos provider is A
.
8.5.6. Troubleshooting
If you have issues, enable additional logging to debug the problem:
-
Enable
Debug
flag in the Admin Console for Kerberos or LDAP federation providers -
Enable TRACE logging for category
org.keycloak
to receive more information in server logs -
Add system properties
-Dsun.security.krb5.debug=true
and-Dsun.security.spnego.debug=true
8.6. X.509 client certificate user authentication
Red Hat build of Keycloak supports logging in with an X.509 client certificate if you have configured the server to use mutual SSL authentication.
A typical workflow:
- A client sends an authentication request over SSL/TLS channel.
- During the SSL/TLS handshake, the server and the client exchange their x.509/v3 certificates.
- The container (JBoss EAP) validates the certificate PKIX path and the certificate expiration date.
The x.509 client certificate authenticator validates the client certificate by using the following methods:
- Checks the certificate revocation status by using CRL or CRL Distribution Points.
- Checks the Certificate revocation status by using OCSP (Online Certificate Status Protocol).
- Validates whether the key in the certificate matches the expected key.
- Validates whether the extended key in the certificate matches the expected extended key.
- If any of the these checks fail, the x.509 authentication fails. Otherwise, the authenticator extracts the certificate identity and maps it to an existing user.
When the certificate maps to an existing user, the behavior diverges depending on the authentication flow:
- In the Browser Flow, the server prompts users to confirm their identity or sign in with a username and password.
- In the Direct Grant Flow, the server signs in the user.
Note that it is the responsibility of the web container to validate certificate PKIX path. X.509 authenticator on the Red Hat build of Keycloak side provides just the additional support for check the certificate expiration, certificate revocation status and key usage. If you are using Red Hat build of Keycloak deployed behind reverse proxy, make sure that your reverse proxy is configured to validate PKIX path. If you do not use reverse proxy and users directly access the JBoss EAP, you should be fine as JBoss EAP makes sure that PKIX path is validated as long as it is configured as described below.
8.6.1. Features
Supported Certificate Identity Sources:
- Match SubjectDN by using regular expressions
- X500 Subject’s email attribute
- X500 Subject’s email from Subject Alternative Name Extension (RFC822Name General Name)
- X500 Subject’s other name from Subject Alternative Name Extension. This other name is the User Principal Name (UPN), typically.
- X500 Subject’s Common Name attribute
- Match IssuerDN by using regular expressions
- Certificate Serial Number
- Certificate Serial Number and IssuerDN
- SHA-256 Certificate thumbprint
- Full certificate in PEM format
8.6.1.1. Regular expressions
Red Hat build of Keycloak extracts the certificate identity from Subject DN or Issuer DN by using a regular expression as a filter. For example, this regular expression matches the email attribute:
emailAddress=(.*?)(?:,|$)
The regular expression filtering applies if the Identity Source
is set to either Match SubjectDN using regular expression
or Match IssuerDN using regular expression
.
8.6.1.1.1. Mapping certificate identity to an existing user
The certificate identity mapping can map the extracted user identity to an existing user’s username, email, or a custom attribute whose value matches the certificate identity. For example, setting Identity source
to Subject’s email or User mapping method
to Username or email makes the X.509 client certificate authenticator use the email attribute in the certificate’s Subject DN as the search criteria when searching for an existing user by username or by email.
- If you disable Login with email at realm settings, the same rules apply to certificate authentication. Users are unable to log in by using the email attribute.
-
Using
Certificate Serial Number and IssuerDN
as an identity source requires two custom attributes for the serial number and the IssuerDN. -
SHA-256 Certificate thumbprint
is the lowercase hexadecimal representation of SHA-256 certificate thumbprint. -
Using
Full certificate in PEM format
as an identity source is limited to the custom attributes mapped to external federation sources, such as LDAP. Red Hat build of Keycloak cannot store certificates in its database due to length limitations, so in the case of LDAP, you must enableAlways Read Value From LDAP
.
8.6.1.1.2. Extended certificate validation
- Revocation status checking using CRL.
- Revocation status checking using CRL/Distribution Point.
- Revocation status checking using OCSP/Responder URI.
- Certificate KeyUsage validation.
- Certificate ExtendedKeyUsage validation.
8.6.2. Adding X.509 client certificate authentication to browser flows
- Click Authentication in the menu.
- Click the Browser flow.
- From the Action list, select Duplicate.
- Enter a name for the copy.
- Click Duplicate.
- Click Add step.
- Click "X509/Validate Username Form".
Click Add.
X509 execution
- Click and drag the "X509/Validate Username Form" over the "Browser Forms" execution.
Set the requirement to "ALTERNATIVE".
X509 browser flow
- Click the Action menu.
- Click the Bind flow.
- Click the Browser flow from the drop-down list.
Click Save.
X509 browser flow bindings
8.6.3. Configuring X.509 client certificate authentication
X509 configuration
- User Identity Source
- Defines the method for extracting the user identity from a client certificate.
- Canonical DN representation enabled
Defines whether to use the canonical format to determine a distinguished name. The format adds additional normalization rules to the RFC 2253 conformant string representation. The official Java API documentation describes the additions in detail. This option affects the following User Identity Sources only:
- Match SubjectDN using regular expression
- Match IssuerDN using regular expression
- Certificate Serial Number and IssuerDN (the IssuerDN portion)
Do not enable this option to retain backward compatibility with existing Red Hat build of Keycloak instances.
The canonical
format performs modifications over the presented DN in the certificate (e.g., leading and trailing spaces are removed or the entire name is converted to uppercase and lowercase using the English locale). This behavior can lead to collisions in user matching if the Certificate Authorities (CA) that issue the certificates do not validate the assigned DN (e.g., if DNs are issued using any locale and present problems when performing the upper and lower case in English). Do not enable this option if you cannot guarantee that the canonical representation avoids duplications for later matching.
- Enable Serial Number hexadecimal representation
- Represent the serial number as hexadecimal. The serial number with the sign bit set to 1 must be left padded with 00 octet. For example, a serial number with decimal value 161, or a1 in hexadecimal representation is encoded as 00a1, according to RFC5280. See RFC5280, appendix-B for more details.
- A regular expression
- A regular expression to use as a filter for extracting the certificate identity. The expression must contain a single group.
- User Mapping Method
- Defines the method to match the certificate identity with an existing user. Username or email searches for existing users by username or email. Custom Attribute Mapper searches for existing users with a custom attribute that matches the certificate identity. The name of the custom attribute is configurable.
- A name of user attribute
- A custom attribute whose value matches against the certificate identity. Use multiple custom attributes when attribute mapping is related to multiple values, For example, 'Certificate Serial Number and IssuerDN'.
- CRL Checking Enabled
- Check the revocation status of the certificate by using the Certificate Revocation List. The location of the list is defined in the CRL file path attribute.
- Enable CRL Distribution Point to check certificate revocation status
- Use CDP to check the certificate revocation status. Most PKI authorities include CDP in their certificates.
- CRL file path
- The path to a file containing a CRL list. The value must be a path to a valid file if the CRL Checking Enabled option is enabled.
- CRL abort if non updated
-
A CRL conforming to RFC5280 contains a next update field that indicates the date by which the next CRL will be issued. When that time is passed, the CRL is considered outdated and it should be refreshed. If this option is
true
, the authentication will fail if the CRL is outdated (recommended). If the option is set tofalse
, the outdated CRL is still used to validate the user certificates. - OCSP Checking Enabled
- Checks the certificate revocation status by using Online Certificate Status Protocol.
- OCSP Fail-Open Behavior
- By default the OCSP check must return a positive response in order to continue with a successful authentication. Sometimes however this check can be inconclusive: for example, the OCSP server could be unreachable, overloaded, or the client certificate may not contain an OCSP responder URI. When this setting is turned ON, authentication will be denied only if an explicit negative response is received by the OCSP responder and the certificate is definitely revoked. If a valid OCSP response is not available the authentication attempt will be accepted.
- OCSP Responder URI
- Override the value of the OCSP responder URI in the certificate.
- Validate Key Usage
- Verifies the certificate’s KeyUsage extension bits are set. For example, "digitalSignature,KeyEncipherment" verifies if bits 0 and 2 in the KeyUsage extension are set. Leave this parameter empty to disable the Key Usage validation. See RFC5280, Section-4.2.1.3 for more information. Red Hat build of Keycloak raises an error when a key usage mismatch occurs.
- Validate Extended Key Usage
- Verifies one or more purposes defined in the Extended Key Usage extension. See RFC5280, Section-4.2.1.12 for more information. Leave this parameter empty to disable the Extended Key Usage validation. Red Hat build of Keycloak raises an error when flagged as critical by the issuing CA and a key usage extension mismatch occurs.
- Validate Certificate Policy
- Verifies one or more policy OIDs as defined in the Certificate Policy extension. See RFC5280, Section-4.2.1.4. Leave the parameter empty to disable the Certificate Policy validation. Multiple policies should be separated using a comma.
- Certificate Policy Validation Mode
-
When more than one policy is specified in the
Validate Certificate Policy
setting, it decides whether the matching should check for all requested policies to be present, or one match is enough for a successful authentication. Default value isAll
, meaning that all requested policies should be present in the client certificate. - Bypass identity confirmation
- If enabled, X.509 client certificate authentication does not prompt the user to confirm the certificate identity. Red Hat build of Keycloak signs in the user upon successful authentication.
- Revalidate client certificate
- If set, the client certificate trust chain will be always verified at the application level using the certificates present in the configured trust store. This can be useful if the underlying web server does not enforce client certificate chain validation, for example because it is behind a non-validating load balancer or reverse proxy, or when the number of allowed CAs is too large for the mutual SSL negotiation (most browsers cap the maximum SSL negotiation packet size at 32767 bytes, which corresponds to about 200 advertised CAs). By default this option is off.
8.6.4. Adding X.509 Client Certificate Authentication to a Direct Grant Flow
- Click Authentication in the menu.
- Select Duplicate from the "Action list" to make a copy of the built-in "Direct grant" flow.
- Enter a name for the copy.
- Click Duplicate.
- Click the created flow.
- Click the trash can icon 🗑️ of the "Username Validation" and click Delete.
- Click the trash can icon 🗑️ of the "Password" and click Delete.
- Click Add step.
- Click "X509/Validate Username".
Click Add.
X509 direct grant execution
- Set up the x509 authentication configuration by following the steps described in the x509 Browser Flow section.
- Click the Bindings tab.
- Click the Direct Grant Flow drop-down list.
- Click the newly created "x509 Direct Grant" flow.
Click Save.
X509 direct grant flow bindings
8.6.4.1. Example using CURL
The following example shows how to obtain an access token for a user in the realm test
with the direct grant flow. The example is using OAuth2 Resource Owner Password Credentials Grant in the securing apps section and the confidential client resource-owner
:
curl \
-d "client_id=resource-owner" \
-d "client_secret=40cc097b-2a57-4c17-b36a-8fdf3fc2d578" \
-d "grant_type=password" \
--cacert /tmp/truststore.pem \
--cert /tmp/keystore.pem:kssecret \
"https://localhost:8543/realms/test/protocol/openid-connect/token"
The file /tmp/truststore.pem
points to the file with the truststore containing the certificate of the Red Hat build of Keycloak server. The file /tmp/keystore.pem
contains the private key and certificates corresponding to the Red Hat build of Keycloak user, which would be successfully authenticated by this request. It is dependent on the configuration of the authenticator on how exactly is the content from the certificate mapped to the Red Hat build of Keycloak user as described in the configuration section. The kssecret
might be the password of this keystore file.
According to your environment, it might be needed to use more options to CURL commands like for instance:
-
Option
--insecure
if you are using self-signed certificates -
Option
--capath
to include the whole directory containing the certificate authority path -
Options
--cert-type
or--key-type
in case you want to use different files thanPEM
Please consult the documentation of the curl
tool for the details if needed. If you are using other tools than curl
, consult the documentation of your tool. However, the setup would be similar. A need exists to include keystore and truststore as well as client credentials in case you are using a confidential client.
If it is possible, it is preferred to use Service accounts together with the MTLS client authentication (client authenticator X509 Certificate
) rather than using the Direct grant with X.509 authentication as direct grant may require sharing of the user certificate with client applications. When using service account, the tokens are obtained on behalf of the client itself, which in general is better and more secure practice.
8.7. W3C Web Authentication (WebAuthn)
Red Hat build of Keycloak provides support for W3C Web Authentication (WebAuthn). Red Hat build of Keycloak works as a WebAuthn’s Relying Party (RP).
WebAuthn’s operations success depends on the user’s WebAuthn supporting authenticator, browser, and platform. Make sure your authenticator, browser, and platform support the WebAuthn specification.
WebAuthn’s specification uses a user.id
to map a public key credential to a specific user account in the Relying Party. This user ID handle is an opaque byte sequence with a maximum size of 64 bytes. Red Hat build of Keycloak passes the internal database ID to the registration, which in common users is an UUID of 36 characters. But, if the user is from a external user federation provider, the internal Red Hat build of Keycloak ID is an storage ID in the form f:<provider-id>:<user-id>
that can exceed the 64 byte limitation. Please take this into account and use short IDs for the federation provider component and for the users coming from that provider when combining the Storage SPI and WebAuthn.
8.7.1. Setup
The setup procedure of WebAuthn support for 2FA is the following:
8.7.1.1. Check WebAuthn authenticator registration is enabled
- Click Authentication in the menu.
- Click the Required Actions tab.
- Check action Webauthn Register switch is set to ON.
Toggle the Default Action switch to ON if you want all new users to be required to register their WebAuthn credentials.
8.7.2. Enable WebAuthn authentication in the default browser flow
- Click Authentication in the menu.
- Click the Browser flow.
- Locate the execution WebAuthn Authenticator inside the Browser - Conditional 2FA sub-flow.
Change the requirement from Disabled to Alternative for that execution.
WebAuthn browser flow conditional with OTP
With this configuration, the users can choose between using WebAuthn and OTP for the second factor. As the sub-flow is conditional, they are only asked to present a 2FA credential (OTP or WebAuthn) if they have already registered one of the respective credential types. If a user has configured both credential types, the credential with the highest priority will be displayed by default. However, the Try Another Way option will appear so that the user has the alternative methods to log in.
If you want to substitute OTP for WebAuthn and maintain it as conditional:
- Change requirement in OTP Form to Disabled.
Change requirement in WebAuthn Authenticator to Alternative.
Webauthn browser flow conditional
If you require WebAuthn for all users and enforce them to configure the credential if not configured:
- Change requirement in Browser - Conditional 2FA to Required.
- Change requirement in OTP Form to Disabled.
Change requirement in WebAuthn Authenticator to Required.
Webauthn browser flow required
You can see more examples of 2FA configurations in Section 8.10.3, “2FA conditional workflow examples”.
8.7.3. Authenticate with WebAuthn authenticator
After registering a WebAuthn authenticator, the user carries out the following operations:
- Open the login form. The user must authenticate with a username and password.
- The user’s browser asks the user to authenticate by using their WebAuthn authenticator.
8.7.4. Managing WebAuthn as an administrator
8.7.4.1. Managing credentials
Red Hat build of Keycloak manages WebAuthn credentials similarly to other credentials from User credential management:
- Red Hat build of Keycloak assigns users a required action to create a WebAuthn credential from the Reset Actions list and select Webauthn Register.
- Administrators can delete a WebAuthn credential by clicking Delete.
- Administrators can view the credential’s data, such as the AAGUID, by selecting Show data….
- Administrators can set a label for the credential by setting a value in the User Label field and saving the data.
8.7.4.2. Managing policy
Administrators can configure WebAuthn related operations as WebAuthn Policy per realm.
Procedure
- Click Authentication in the menu.
- Click the Policy tab.
- Click the WebAuthn Policy tab.
- Configure the items within the policy (see description below).
- Click Save.
The configurable items and their description are as follows:
| Configuration | Description |
|---|---|
| Relying Party Entity Name | The readable server name as a WebAuthn Relying Party. This item is mandatory and applies to the registration of the WebAuthn authenticator. The default setting is "keycloak". For more details, see WebAuthn Specification. |
| Signature Algorithms | The algorithms telling the WebAuthn authenticator which signature algorithms to use for the Public Key Credential. Red Hat build of Keycloak uses the Public Key Credential to sign and verify Authentication Assertions. If no algorithms exist, the default ES256 and RS256 is adapted. ES256 and RS256 are an optional configuration item applying to the registration of WebAuthn authenticators. For more details, see WebAuthn Specification. |
| Relying Party ID | The ID of a WebAuthn Relying Party that determines the scope of Public Key Credentials. The ID must be the origin’s effective domain. This ID is an optional configuration item applied to the registration of WebAuthn authenticators. If this entry is blank, Red Hat build of Keycloak adapts the host part of Red Hat build of Keycloak’s base URL. For more details, see WebAuthn Specification. |
| Attestation Conveyance Preference | The WebAuthn API implementation on the browser (WebAuthn Client) is the preferential method to generate Attestation statements. This preference is an optional configuration item applying to the registration of the WebAuthn authenticator. If no option exists, its behavior is the same as selecting "none". For more details, see WebAuthn Specification. |
| Authenticator Attachment | The acceptable attachment pattern of a WebAuthn authenticator for the WebAuthn Client. This pattern is an optional configuration item applying to the registration of the WebAuthn authenticator. For more details, see WebAuthn Specification. |
| Require Discoverable Credential | The option requiring that the WebAuthn authenticator generates the Public Key Credential as Client-side discoverable Credential. This option applies to the registration of the WebAuthn authenticator. If left blank, its behavior is the same as selecting "No". For more details, see WebAuthn Specification. |
| User Verification Requirement | The option requiring that the WebAuthn authenticator confirms the verification of a user. This is an optional configuration item applying to the registration of a WebAuthn authenticator and the authentication of a user by a WebAuthn authenticator. If no option exists, its behavior is the same as selecting "preferred". For more details, see WebAuthn Specification for registering a WebAuthn authenticator and WebAuthn Specification for authenticating the user by a WebAuthn authenticator. |
| Timeout | The timeout value, in seconds, for registering a WebAuthn authenticator and authenticating the user by using a WebAuthn authenticator. If set to zero, its behavior depends on the WebAuthn authenticator’s implementation. The default value is 0. For more details, see WebAuthn Specification for registering a WebAuthn authenticator and WebAuthn Specification for authenticating the user by a WebAuthn authenticator. |
| Avoid Same Authenticator Registration | If enabled, Red Hat build of Keycloak cannot re-register an already registered WebAuthn authenticator. |
| Acceptable AAGUIDs |
The list of allowed AAGUIDs which a WebAuthn authenticator must register against. An AAGUID (Authenticator Attestation Global Unique Identifier) is a 128-bit identifier indicating the authenticator’s type (e.g., make and model). This option needs the Attestation conveyance preference to be configured (normally |
8.7.5. Attestation statement verification
When registering a WebAuthn authenticator, Red Hat build of Keycloak verifies the trustworthiness of the attestation statement generated by the WebAuthn authenticator. Red Hat build of Keycloak requires the trust anchor’s certificates imported into the truststore.
To omit this validation, disable this truststore or set the WebAuthn policy’s configuration item "Attestation Conveyance Preference" to "none".
8.7.6. Managing WebAuthn credentials as a user
8.7.6.1. Register WebAuthn authenticator
The appropriate method to register a WebAuthn authenticator depends on whether the user has already registered an account on Red Hat build of Keycloak.
8.7.6.2. New user
If the WebAuthn Register required action is Default Action in a realm, new users must set up the Passkey after their first login.
Procedure
- Open the login form.
- Click Register.
- Fill in the items on the form.
- Click Register.
After successfully registering, the browser asks the user to enter the text of their WebAuthn authenticator’s label.
8.7.6.3. Existing user
If WebAuthn Authenticator
is set up as required as shown in the first example, then when existing users try to log in, they are required to register their WebAuthn authenticator automatically:
Procedure
- Open the login form.
- Enter the items on the form.
- Click Save.
- Click Login.
After successful registration, the user’s browser asks the user to enter the text of their WebAuthn authenticator’s label.
8.7.7. Registering WebAuthn credentials using AIA
WebAuthn credentials can also be registered for a user using Application Initiated Actions (AIA). The actions Webauthn Register (kc_action=webauthn-register
) and Webauthn Register Passwordless (kc_action=webauthn-register-passwordless
) are available for the applications if enabled in the Required actions tab.
Both required actions allow a parameter skip_if_exists that allows to skip the AIA execution if the user already has a credential of that type. The kc_action_status
will be success if skipped. For example, adding the option to the common WebAuthn register action is just using the following query parameter kc_action=webauthn-register:skip_if_exists
.
8.7.8. Passwordless WebAuthn together with Two-Factor
Red Hat build of Keycloak uses WebAuthn for two-factor authentication, but you can use WebAuthn as the first-factor authentication. In this case, users with passwordless
WebAuthn credentials can authenticate to Red Hat build of Keycloak without a password. Red Hat build of Keycloak can use WebAuthn as both the passwordless and two-factor authentication mechanism in the context of a realm and a single authentication flow.
An administrator typically requires that Passkeys registered by users for the WebAuthn passwordless authentication meet different requirements. For example, the Passkeys may require users to authenticate to the Passkey using a PIN, or the Passkey attests with a stronger certificate authority.
Because of this, Red Hat build of Keycloak permits administrators to configure a separate WebAuthn Passwordless Policy
. There is a required Webauthn Register Passwordless
action of type and separate authenticator of type WebAuthn Passwordless Authenticator
.
8.7.8.1. Setup
Set up WebAuthn passwordless support as follows:
-
(if not already present) Register a new required action for WebAuthn passwordless support. Use the steps described in Enable WebAuthn Authenticator Registration. Register the
Webauthn Register Passwordless
action. - Configure the policy. You can use the steps and configuration options described in Managing Policy. Perform the configuration in the Admin Console in the tab WebAuthn Passwordless Policy. Typically the requirements for the Passkey will be stronger than for the two-factor policy. For example, you can set the User Verification Requirement to Required when you configure the passwordless policy.
Configure the authentication flow. Use the WebAuthn Browser flow described in Adding WebAuthn Authentication to a Browser Flow. Configure the flow as follows:
- The WebAuthn Browser Forms subflow contains Username Form as the first authenticator. Delete the default Username Password Form authenticator and add the Username Form authenticator. This action requires the user to provide a username as the first step.
- There will be a required subflow, which can be named Passwordless Or Two-factor, for example. This subflow indicates the user can authenticate with Passwordless WebAuthn credential or with Two-factor authentication.
- The flow contains WebAuthn Passwordless Authenticator as the first alternative.
- The second alternative will be a subflow named Password And Two-factor Webauthn, for example. This subflow contains a Password Form and a WebAuthn Authenticator.
The final configuration of the flow looks similar to this:
PasswordLess flow
You can now add WebAuthn Register Passwordless as the required action to a user, already known to Red Hat build of Keycloak, to test this. During the first authentication, the user must use the password and second-factor WebAuthn credential. The user does not need to provide the password and second-factor WebAuthn credential if they use the WebAuthn Passwordless credential.
8.7.9. LoginLess WebAuthn
Red Hat build of Keycloak uses WebAuthn for two-factor authentication, but you can use WebAuthn as the first-factor authentication. In this case, users with passwordless
WebAuthn credentials can authenticate to Red Hat build of Keycloak without submitting a login or a password. Red Hat build of Keycloak can use WebAuthn as both the loginless/passwordless and two-factor authentication mechanism in the context of a realm.
An administrator typically requires that Passkeys registered by users for the WebAuthn loginless authentication meet different requirements. Loginless authentication requires users to authenticate to the Passkey (for example by using a PIN code or a fingerprint) and that the cryptographic keys associated with the loginless credential are stored physically on the Passkey. Not all Passkeys meet that kind of requirement. Check with your Passkey vendor if your device supports 'user verification' and 'discoverable credential'. See Supported Passkeys.
Red Hat build of Keycloak permits administrators to configure the WebAuthn Passwordless Policy
in a way that allows loginless authentication. Note that loginless authentication can only be configured with WebAuthn Passwordless Policy
and with WebAuthn Passwordless
credentials. WebAuthn loginless authentication and WebAuthn passwordless authentication can be configured on the same realm but will share the same policy WebAuthn Passwordless Policy
.
8.7.9.1. Setup
Procedure
Set up WebAuthn Loginless support as follows:
- (If not already done) Check the required action for WebAuthn Register Passwordless is enabled. Use the steps described in Enable WebAuthn Authenticator Registration, but using WebAuthn Register Passwordless instead of WebAuthn Register.
-
Configure the
WebAuthn Passwordless Policy
if needed. Perform the configuration in the Admin Console,Authentication
section, in thePolicies
WebAuthn Passwordless Policy
tab. By default, Red Hat build of Keycloak sets User Verification Requirement to required and Require Discoverable Credential to Yes for the passwordless scenario to work properly. Storage capacity is usually very limited on Passkeys meaning that you won’t be able to store many discoverable credentials on your Passkey. - Configure the authentication flow. Create a new authentication flow, add the "WebAuthn Passwordless" execution and set the Requirement setting of the execution to Required
The final configuration of the flow looks similar to this:
LoginLess flow
You can now add the required action WebAuthn Register Passwordless
to a user, already known to Red Hat build of Keycloak, to test this. The user with the required action configured will have to authenticate (with a username/password for example) and will then be prompted to register a Passkey to be used for loginless authentication.
8.7.9.2. Vendor specific remarks
8.7.9.2.1. Compatibility check list
Loginless authentication with Red Hat build of Keycloak requires the Passkey to meet the following features
- FIDO2 compliance: not to be confused with FIDO/U2F
- User verification: the ability for the Passkey to authenticate the user (prevents someone finding your Passkey to be able to authenticate loginless and passwordless)
- Discoverable Credential: the ability for the Passkey to store the login and the cryptographic keys associated with the client application
8.7.9.2.2. Windows Hello
To use Windows Hello based credentials to authenticate against Red Hat build of Keycloak, configure the Signature Algorithms setting of the WebAuthn Passwordless Policy
to include the RS256 value. Note that some browsers don’t allow access to platform Passkey (like Windows Hello) inside private windows.
8.7.9.2.3. Supported Passkeys
The following Passkeys have been successfully tested for loginless authentication with Red Hat build of Keycloak:
- Windows Hello (Windows 10 21H1/21H2)
- Yubico Yubikey 5 NFC
- Feitian ePass FIDO-NFC
8.8. Passkeys
Red Hat build of Keycloak provides support for Passkeys. Red Hat build of Keycloak works as a Passkeys Relying Party (RP).
Passkey registration and authentication are performed using the same features of WebAuthn. More specifically Passkeys are related to LoginLess WebAuthn as they try to avoid any password during login. Therefore, users of Red Hat build of Keycloak can do Passkey registration and authentication by existing WebAuthn registration and authentication, using the passwordless variants.
The Passkeys feature has been integrated seamlessly in the default authentication forms in two different ways. When activated, both conditional UI and modal UI are available in the forms in which the username input is displayed (for example Username Password Form or Username Form). Besides, the password forms, when the username was already selected, always show the modal UI button to login by passkey if the current user has passwordless WebAuthn credentials associated. This way modal and conditional UI can be used to perform a complete login from scratch that needs username and password, and only modal UI is presented when the username is already selected in the authentication process (because of re-authentication or because the user was selected before in the process not using a passkey).
Passkeys have been added to the following authenticator implementations:
- Username Password Form: The username and password form used by default in Red Hat build of Keycloak.
- Username Form: The form in which the username is displayed alone and is typically followed by the password form. This authenticator is used when the username and password fields want to be presented to the user in two different steps.
- Password Form: Authenticating using Passkeys in the Username Form skips the next Password Form execution. The Password Form implementation checks if the user was already authenticated using a passwordless WebAuthn credential and, if that is the case, no password is requested. If the Password Form cannot be skipped, it allows using modal UI to authenticate the user if the account has passkey credentials associated.
- Organization Identity - First Login: The organization form that is used when the organizations feature is enabled for the realm. Using Passkeys in this step avoids the subsequent execution of the username and password form in the same way than in the username form.
- Username Password Form for identity provider re-authentication: Similar to the default Username Password Form but used in the first login flow to re-authenticate and prove ownership of the account. Now the modal UI button is available to use passkeys to re-authenticate.
Finally, the default browser flow is modified to skip the flow Browser - Conditional 2FA if a passkey was used previously to authenticate the account. So now, when passkeys are enabled in the realm, 2FA is only presented if the user introduced a common password to login, not if a passkey was used. The new Condition - credential is added to the sub-flow to check the credential presented before. If you want to always use 2FA, you can just change the requirement from Required to Disabled for this condition. See Conditions in conditional flows for more information.
Both synced Passkeys and device-bound Passkeys can be used for both Same-Device and Cross-Device Authentication (CDA). However, Passkeys operations success depends on the user’s environment. Make sure which operations can succeed in the environment.
8.8.1. Passkey Authentication with Conditional UI or autofill
The Conditional User Interface (UI) or autofill is a feature related to passkeys in which the username input (the field in which the username to login is typed) is tagged with a webauthn
autofill detail token (for example using the attribute autocomplete="username webauthn"
). When the user clicks in such an input field, the user agent (browser) can render a list of discovered credentials for the user to select from, and perhaps also give the user the option to try another way. If the user selects one of the presented passkeys, Red Hat build of Keycloak initiates the WebAuthn authentication with that key and avoids any password typing.
Compared with LoginLess WebAuthn, the authentication improves the user’s experience of authentication.
Passkey Authentication with Conditional UI Autofill using Chrome browser
This authentication uses the WebAuthn Conditional UI. Therefore, this authentication success depends on the user’s environment. If the environment does not support WebAuthn Conditional UI, the user should use the direct modal UI or username and password login.
8.8.2. Passkeys Authentication with Modal UI
Nevertheless, because conditional UI can sometimes not show all the credentials to the user, the modal UI can always be initiated using the button Sign in with Passkey. The Modal User Interface (UI) ensures all passkeys are usable, including the ones stored in hardware tokens or on other devices that cannot be enumerated without user interaction.
The modal UI button is also presented in the password forms when the user is already selected, for example when re-authenticating in the common Username Password Form. In this case, the modal UI is limited to the passwordless WebAuthn credentials that Red Hat build of Keycloak has defined for the account.
Passkey Authentication with Modal UI using Chrome browser
8.8.3. Setup
Set up Passkey Authentication for the default forms as follows:
- (If not already done) Check the required action for WebAuthn Register Passwordless is enabled. Use the steps described in Enable WebAuthn Authenticator Registration, but using WebAuthn Register Passwordless instead of WebAuthn Register.
Configure the WebAuthn Passwordless Policy in the same way that is explained in LoginLess WebAuthn. Perform the configuration in the Admin Console,
Authentication
section, in the tabPolicies
WebAuthn Passwordless Policy
. The default configuration for the passwordless policy is usually enough for correct passkeys integration.NoteStorage capacity is usually very limited on hardware passkeys meaning that you cannot store many discoverable credentials on your passkey. However, this limitation may be mitigated for instance if you use an Android phone backed by a Google account as a passkey device or an iPhone backed by Bitwarden.
- In the WebAuthn Passwordless Policy tab, activate the Enable Passkeys option at the bottom. This switch is the one that really enables passkeys in the realm.
8.9. Recovery Codes
The Recovery Codes are a number of sequential one-time passwords (currently 12) auto-generated by Red Hat build of Keycloak. The codes can be used as a 2nd Factor Authentication (2FA) by adding the Recovery Authentication Code Form
authenticator to your authentication flow. When configured in the flow, Red Hat build of Keycloak asks the user for the next generated code in order. When the current code is introduced by the user, it is removed and the next code will be required for the next login.
Due to its nature, the Recovery Codes work normally as a backup for another 2FA methods. They can complement the OTP Form
or the WebAuthn Authenticator
to give a backing way to log inside Red Hat build of Keycloak, for example, if the software or hardware device used for the previous 2FA methods is broken or unavailable.
You can configure the Configure OTP
required action to ask for recovery codes automatically by enabling Add recovery codes.
8.9.1. Check Recovery Codes required action is enabled
Check the Recovery Codes action is enabled in Red Hat build of Keycloak:
- Click Authentication in the menu.
- Click the Required Actions tab.
- Ensure the Recovery Authentication Codes switch Enabled is set to On.
Toggle the Default Action switch to On if you want all the new users to register their Recovery Codes credentials in the first login.
8.9.2. Configure the Recovery Codes required action
From the Required Actions tab of the admin console, you have the option to configure the Recovery Authentication Codes required action. So far, there is a configuration option Warning Threshold available. When a user has a smaller amount of remaining recovery codes on his account than the value configured here, account console will show warning to the user, which will recommend them to set up a new set of recovery codes. The warning displayed to the user may look similar to this:
Recovery Codes Account console warning
8.9.3. Adding Recovery Codes to the browser flow
The following procedure adds the Recovery Authentication Code Form
as an alternative way of login in the default Browser flow.
- Click Authentication in the realm menu.
- Click the Browser flow.
- Locate the execution Recovery Authentication Code Form inside the Browser - Conditional 2FA sub-flow.
Change the requirement from Disabled to Alternative for that execution.
Recovery Codes Browser flow
With this configuration, both 2FA authenticators (
OTP Form
andRecovery Authentication Code Form
) are alternate ways to log into Red Hat build of Keycloak. If the user has configured both credential types, the credential with the highest priority will be displayed by default, but the Try Another Way option will appear so that the user has the alternative methods to log in.
You can see more examples of 2FA configurations in Section 8.10.3, “2FA conditional workflow examples”.
8.9.4. Creating the Recovery Codes credential
Once the Recovery Codes required action is enabled and the credential type is managed in the flow, users can request to create their own codes. The action is just another required action that can be used in Red Hat build of Keycloak (directly called by the user by using the Account Console or assigned by an administrator by using the Admin Console).
The required action, when executed, generates the list of codes and presents it to the user. The action offers to print, download, or copy the list of codes to help the user to store them is a safe place. In order to complete the setup, the checkbox I have saved these codes somewhere safe should be previously checked.
Recovery Authentication Codes setup page
The Recovery Codes can be re-created at any moment.
8.10. Conditions in conditional flows
As was mentioned in Execution requirements, Condition executions can be only contained in Conditional subflow. If all Condition executions evaluate as true, then the Conditional sub-flow acts as Required. You can process the next execution in the Conditional sub-flow. If some executions included in the Conditional sub-flow evaluate as false, then the whole sub-flow is considered as Disabled.
8.10.1. Available conditions
Condition - User Role
This execution has the ability to determine if the user has a role defined by User role field. If the user has the required role, the execution is considered as true and other executions are evaluated. The administrator has to define the following fields:
- Alias
- Describes a name of the execution, which will be shown in the authentication flow.
- User role
-
Role the user should have to execute this flow. To specify an application role the syntax is
appname.approle
(for examplemyapp.myrole
).
Condition - User Configured
- This checks if the other executions in the flow are configured for the user. The Execution requirements section includes an example of the OTP form.
Condition - User Attribute
This checks if the user has set up the required attribute: optionally, the check can also evaluate the group attributes. There is a possibility to negate output, which means the user should not have the attribute. The User Attributes section shows how to add a custom attribute. You can provide these fields:
- Alias
- Describes a name of the execution, which will be shown in the authentication flow.
- Attribute name
- Name of the attribute to check.
- Expected attribute value
- Expected value in the attribute.
- Include group attributes
- If On, the condition checks if any of the joined group has one attribute matching the configured name and value: this option can affect performance
- Negate output
- You can negate the output. In other words, the attribute should not be present.
Condition - sub-flow executed
The condition checks if a previous sub-flow was successfully executed (or not executed) in the authentication process. Therefore, the flow can trigger other steps based on a previous sub-flow termination. These configuration fields exist:
- Flow name
- The sub-flow name to check if it was executed or not executed. Required.
- Check result
-
When the condition evaluates to true. If
executed
returns true when the configured sub-flow was executed with output success, false otherwise. Ifnot-executed
returns false when the sub-flow was executed with output success, true otherwise (the negation of the previous option).
Condition - client scope
The condition to evaluate if a configured client scope is present as a client scope of the client requesting authentication. These configuration fields exist:
- Client scope name
-
The name of the client scope, which should be present as a client scope of the client, which is requesting authentication. If requested client scope is default client scope of the client requesting login, the condition will be evaluated to true. If requested client scope is optional client scope of the client requesting login, condition will be evaluated to true if client scope is sent by the client in the login request (for example, by the
scope
parameter in case of OIDC/OAuth2 client login). Required. - Negate output
- Apply a NOT to the check result. When this is true, then the condition will evaluate to true just if configured client scope is not present.
Condition - credential
This condition evaluates if a specific credential type has been used (or not used) by the user during the authentication process. Configuration options:
- Credentials
- The list of credentials to be considered by the condition.
- Included
-
If included is true, the condition will be evaluated to
true
when any of the credentials specified in the credentials option has been used in the authentication process, false otherwise. If included is false, the condition is evaluated in the opposite way, it will betrue
if none of the credentials configured have been used, andfalse
if one or more of them have been used.
8.10.2. Explicitly deny/allow access in conditional flows
You can allow or deny access to resources in a conditional flow. The two authenticators Deny Access
and Allow Access
control access to the resources by conditions.
Allow Access
- Authenticator will always successfully authenticate. This authenticator is not configurable.
Deny Access
Access will always be denied. You can define an error message, which will be shown to the user. You can provide these fields:
- Alias
- Describes a name of the execution, which will be shown in the authentication flow.
- Error message
-
Error message which will be shown to the user. The error message could be provided as a particular message or as a property in order to use it with localization. (i.e. "You do not have the role 'admin'.", my-property-deny in messages properties) Leave blank for the default message defined as property
access-denied
.
Here is an example how to deny access to all users who do not have the role role1
and show an error message defined by a property deny-role1
. This example includes Condition - User Role
and Deny Access
executions.
Browser flow
Condition - user role configuration
Configuration of the Deny Access
is really easy. You can specify an arbitrary Alias and required message like this:
The last thing is defining the property with an error message in the login theme messages_en.properties
(for English):
deny-role1 = You do not have required role!
8.10.3. 2FA conditional workflow examples
The section presents some examples of conditional workflows that integrates 2nd Factor Authentication (2FA) in different ways. The examples copy the default browser
flow and modify the configuration inside the forms
sub-flow.
8.10.3.1. Conditional 2FA sub-flow
The default browser
flow uses a Conditional 2FA
sub-flow that already gives 2nd factor Authentication (2FA) with OTP Form (One Time Password). It also provides WebAuthn and Recovery Codes but they are disabled by default. Consistent with this approach, different 2FA methods can be integrated with the Condition - User Configured
.
2FA all alternative
The forms
sub-flow contains another 2FA
conditional sub-flow with Condition - user configured
. Three 2FA steps (OTP, Webauthn and Recovery Codes) are allowed as alternative steps. The user will be able to choose one of the three options, if they are configured for the user. As the sub-flow is conditional, the authentication process will complete successfully if no 2FA credential is configured.
This configuration provides the same behavior as when you configure with the default browser flow with both Disabled steps are configured to Alternative.
8.10.3.2. Conditional 2FA sub-flow and deny access
The second example continues the previous one. After the 2FA
sub-flow, another flow Deny access if no 2FA
is used to check if the previous 2FA
was not executed. In that case (the user has no 2FA credential configured) the access is denied.
2FA all alternative and deny access
The Condition - sub-flow executed
is configured to detect if the 2FA
sub-flow was not executed previously.
Configuration for the sub-flow executed
The step Deny access
denies the authentication if not executed.
8.10.3.3. Conditional 2FA sub-flow with OTP default
The last example is very similar to the previous one. Instead of denying the access, step OTP Form
is configured as required.
2FA all alternative with OTP default
With this flow, if the user has none of the 2FA methods configured, the OTP setup will be enforced to continue the login.
8.11. Authentication sessions
When a login page is opened for the first time in a web browser, Red Hat build of Keycloak creates an object called authentication session that stores some useful information about the request. Whenever a new login page is opened from a different tab in the same browser, Red Hat build of Keycloak creates a new record called authentication sub-session that is stored within the authentication session. Authentication requests can come from any type of clients such as the Admin CLI. In that case, a new authentication session is also created with one authentication sub-session. Please note that authentication sessions can be created also in other ways than using a browser flow.
The authentication session usually expires after 30 minutes by default. The exact time is specified by the Login timeout switch in the Sessions tab of the admin console when configuring realms.
8.11.1. Authentication in more browser tabs
As described in the previous section, a situation can involve a user who is trying to authenticate to the Red Hat build of Keycloak server from multiple tabs of a single browser. However, when that user authenticates in one browser tab, the other browser tabs will automatically restart the authentication. This authentication occurs due to the small javascript available on the Red Hat build of Keycloak login pages. The restart will typically authenticate the user in other browser tabs and redirect to clients because there is an SSO session now due to the fact that the user just successfully authenticated in first browser tab. Some rare exceptions exist when a user is not automatically authenticated in other browser tabs, such as for instance when using an OIDC parameter prompt=login or step-up authentication requesting a stronger authentication factor than the currently authenticated factor.
In some rare cases, it can happen that after authentication in the first browser tab, other browser tabs are not able to restart authentication because the authentication session is already expired. In this case, the particular browser tab will redirect the error about the expired authentication session back to the client in a protocol specific way. For more details, see the corresponding sections of OIDC documentation in the securing apps section. When the client application receives such an error, it can immediately resubmit the OIDC/SAML authentication request to Red Hat build of Keycloak as this should usually automatically authenticate the user due to the existing SSO session as described earlier. As a result, the end user is authenticated automatically in all browser tabs. The Keycloak JavaScript adapter in the securing apps section, and Red Hat build of Keycloak Identity provider support to handle this error automatically and retry the authentication to the Red Hat build of Keycloak server in such a case.
