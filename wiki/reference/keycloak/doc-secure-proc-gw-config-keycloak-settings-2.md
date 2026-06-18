---
title: "Configure keycloak authentication - Red Hat Ansible Automation Platform 2.7"
type: reference
domain: keycloak
slug: doc-secure-proc-gw-config-keycloak-settings-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_gw_config_keycloak_settings
documentKind: "Documentation"
---

# Configure keycloak authentication - Red Hat Ansible Automation Platform 2.7

You can configure Ansible Automation Platform to integrate Keycloak to manage user authentication.
About this task
Note
When using this authenticator some specific setup in your Keycloak instance is required. Refer to the Python Keycloak reference for more details.
Procedure
- From the navigation panel, select .
- Click Create authentication.
- Enter a Name for this authentication configuration.
- Select Keycloak from the Authentication type list. The Authentication details section automatically updates to show the fields relevant to the selected authentication type.
- Enter the location where the user’s token can be retrieved in the Keycloak Access Token URL field.
- Optional: Enter the redirect location the user is taken to during the login flow in the Keycloak Provider URL field.
- Enter the Client ID from your Keycloak installation in the Keycloak OIDC Key field.
- Enter the RS256 public key provided by your Keycloak realm in the Keycloak Public Key field.
- Enter the OIDC secret (Client Secret) from your Keycloak installation in the Keycloak OIDC Secret field.
- Optional: Enter any Additional Authenticator Fields that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.
Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.
- To automatically create organizations, users, and teams upon successful login, select Create objects.
- To enable this authentication method upon creation, select Enabled.
- To remove a user for any groups they were previously added to when they authenticate from this source, select Remove users.
- Click Create Authentication Method.
If you receive an jwt.exceptions.InvalidAudienceError: Audience doesn’t match
error, you must re-enable the audience by doing the following:
- From the navigation for your Keycloak configuration, select .
- Pick a name for the mapper.
- Select the Client ID corresponding to your client in
Included Client Audience
.
What to do next
To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to Mapping.
