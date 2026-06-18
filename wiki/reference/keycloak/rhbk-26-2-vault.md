---
title: "Chapter 20. Using a vault - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-vault
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/vault-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 20. Using a vault - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 20. Using a vault
Configure and use a vault in Red Hat build of Keycloak.
Red Hat build of Keycloak provides two out-of-the-box implementations of the Vault SPI: a plain-text file-based vault and Java KeyStore-based vault.
The file-based vault implementation is especially useful for Kubernetes/OpenShift secrets. You can mount Kubernetes secrets into the Red Hat build of Keycloak Container, and the data fields will be available in the mounted folder with a flat-file structure.
The Java KeyStore-based vault implementation is useful for storing secrets in bare metal installations. You can use the KeyStore vault, which is encrypted using a password.
20.1. Available integrations
Secrets stored in the vaults can be used at the following places of the Administration Console:
- Obtain the SMTP Mail server Password
- Obtain the LDAP Bind Credential when using LDAP-based User Federation
- Obtain the OIDC identity providers Client Secret when integrating external identity providers
20.2. Enabling a vault
For enabling the file-based vault you need to build Red Hat build of Keycloak first using the following build option:
bin/kc.[sh|bat] build --vault=file
Analogically, for the Java KeyStore-based you need to specify the following build option:
bin/kc.[sh|bat] build --vault=keystore
20.3. Configuring the file-based vault
20.3.1. Setting the base directory to lookup secrets
Kubernetes/OpenShift secrets are basically mounted files. To configure a directory where these files should be mounted, enter this command:
bin/kc.[sh|bat] start --vault-dir=/my/path
20.3.2. Realm-specific secret files
Kubernetes/OpenShift Secrets are used on a per-realm basis in Red Hat build of Keycloak, which requires a naming convention for the file in place:
${vault.<realmname>_<secretname>}
20.4. Configuring the Java KeyStore-based vault
In order to use the Java KeyStore-based vault, you need to create a KeyStore file first. You can use the following command for doing so:
keytool -importpass -alias <realm-name>_<alias> -keystore keystore.p12 -storepass keystorepassword
and then enter a value you want to store in the vault. Note that the format of the -alias
parameter depends on the key resolver used. The default key resolver is REALM_UNDERSCORE_KEY
.
This by default results to storing the value in a form of generic PBEKey (password based encryption) within SecretKeyEntry.
You can then start Red Hat build of Keycloak using the following runtime options:
bin/kc.[sh|bat] start --vault-file=/path/to/keystore.p12 --vault-pass=<value> --vault-type=<value>
Note that the --vault-type
parameter is optional and defaults to PKCS12
.
Secrets stored in the vault can then be accessed in a realm via the following placeholder (assuming using the REALM_UNDERSCORE_KEY
key resolver): ${vault.realm-name_alias}
.
20.5. Using underscores in the secret names
To process the secret correctly, you double all underscores in the <secretname>. When REALM_UNDERSCORE_KEY
key resolver is used, underscores in <realmname> are also doubled and <secretname> and <realmname> is separated by a single underscore.
Example
-
Realm Name:
sso_realm
-
Desired Name:
ldap_credential
- Resulting file name:
sso__realm_ldap__credential
Note the doubled underscores between sso and realm and also between ldap and credential.
To learn more about key resolvers, see Key resolvers section in the Server Administration guide.
20.6. Example: Use an LDAP bind credential secret in the Admin Console
Example setup
-
A realm named
secrettest
-
A desired Name
ldapBc
for the bind Credential -
Resulting file name:
secrettest_ldapBc
Usage in Admin Console
You can then use this secret from the Admin Console by using ${vault.ldapBc}
as the value for the Bind Credential
when configuring your LDAP User federation.
20.7. Relevant options
| Value | |
|---|---|
| 🛠
|
|
|
| |
|
| |
|
| |
|
| (default) |
