---
title: "Chapter 14. Using a vault to obtain secrets - Red Hat build of Keycloak 26.0 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-vault-administration
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/vault-administration
guide: server_administration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 14. Using a vault to obtain secrets - Red Hat build of Keycloak 26.0 Server Administration Guide

Chapter 14. Using a vault to obtain secrets
Red Hat build of Keycloak currently provides two out-of-the-box implementations of the Vault SPI: a plain-text file-based vault and Java KeyStore-based vault.
To obtain a secret from a vault rather than entering it directly, enter the following specially crafted string into the appropriate field:
${vault.key}
where the key
is the name of the secret recognized by the vault.
To prevent secrets from leaking across realms, Red Hat build of Keycloak combines the realm name with the key
obtained from the vault expression. This method means that the key
does not directly map to an entry in the vault but creates the final entry name according to the algorithm used to combine the key
with the realm name. In case of the file-based vault, such combination reflects to a specific filename, for the Java KeyStore-based vault it’s a specific alias name.
You can obtain the secret from the vault in the following fields:
- SMTP password
- In the realm SMTP settings
- LDAP bind credential
- In the LDAP settings of LDAP-based user federation.
- OIDC identity provider secret
- In the Client Secret inside identity provider OpenID Connect Config
14.1. Key resolvers
All built-in providers support the configuration of key resolvers. A key resolver implements the algorithm or strategy for combining the realm name with the key, obtained from the ${vault.key}
expression, into the final entry name used to retrieve the secret from the vault. Red Hat build of Keycloak uses the keyResolvers
property to configure the resolvers that the provider uses. The value is a comma-separated list of resolver names. An example of the configuration for the files-plaintext
provider follows:
kc.[sh|bat] start --spi-vault-file-key-resolvers=REALM_UNDERSCORE_KEY,KEY_ONLY
The resolvers run in the same order you declare them in the configuration. For each resolver, Red Hat build of Keycloak uses the last entry name the resolver produces, which combines the realm with the vault key to search for the vault’s secret. If Red Hat build of Keycloak finds a secret, it returns the secret. If not, Red Hat build of Keycloak uses the next resolver. This search continues until Red Hat build of Keycloak finds a non-empty secret or runs out of resolvers. If Red Hat build of Keycloak finds no secret, Red Hat build of Keycloak returns an empty secret.
In the previous example, Red Hat build of Keycloak uses the REALM_UNDERSCORE_KEY
resolver first. If Red Hat build of Keycloak finds an entry in the vault that using that resolver, Red Hat build of Keycloak returns that entry. If not, Red Hat build of Keycloak searches again using the KEY_ONLY
resolver. If Red Hat build of Keycloak finds an entry by using the KEY_ONLY
resolver, Red Hat build of Keycloak returns that entry. If Red Hat build of Keycloak uses all resolvers, Red Hat build of Keycloak returns an empty secret.
A list of the currently available resolvers follows:
| Name | Description |
|---|---|
| KEY_ONLY |
Red Hat build of Keycloak ignores the realm name and uses the key from the vault expression. Red Hat build of Keycloak escapes occurrences of underscores in the key with another underscore character. For example, if the key is called |
| REALM_UNDERSCORE_KEY |
Red Hat build of Keycloak combines the realm and key by using an underscore character. Red Hat build of Keycloak escapes occurrences of underscores in the realm or key with another underscore character. For example, if the realm is called |
| REALM_FILESEPARATOR_KEY | Red Hat build of Keycloak combines the realm and key by using the platform file separator character. The vault expression prohibits the use of characters that could cause path traversal, thus preventing access to secrets outside the corresponding realm. |
If you have not configured a resolver for the built-in providers, Red Hat build of Keycloak selects the REALM_UNDERSCORE_KEY
.
