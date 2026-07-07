---
title: "Chapter 3. Red Hat build of Keycloak Realm Import - Red Hat build of Keycloak 26.0 Operator Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-realm-import
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/operator_guide/realm-import-
guide: operator_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "3.1. Importing a Red Hat build of Keycloak Realm Using the Red Hat build of Keycloak Operator, you can perform a realm import for the Keycloak Deployment. Note If a Realm with the same name already exists in Red Hat build of Keycloak, it will not be overwritten. The Realm Import CR only supports creation of new realms and does not update or delete those. Changes to the realm performed directly on …"
---

# Chapter 3. Red Hat build of Keycloak Realm Import - Red Hat build of Keycloak 26.0 Operator Guide

Chapter 3. Red Hat build of Keycloak Realm Import
3.1. Importing a Red Hat build of Keycloak Realm
Using the Red Hat build of Keycloak Operator, you can perform a realm import for the Keycloak Deployment.
- If a Realm with the same name already exists in Red Hat build of Keycloak, it will not be overwritten.
- The Realm Import CR only supports creation of new realms and does not update or delete those. Changes to the realm performed directly on Red Hat build of Keycloak are not synced back in the CR.
3.1.1. Creating a Realm Import Custom Resource
The following is an example of a Realm Import Custom Resource (CR):
apiVersion: k8s.keycloak.org/v2alpha1
kind: KeycloakRealmImport
metadata:
name: my-realm-kc
spec:
keycloakCRName: <name of the keycloak CR>
realm:
...
This CR should be created in the same namespace as the Keycloak Deployment CR, defined in the field keycloakCRName
. The realm
field accepts a full RealmRepresentation.
The recommended way to obtain a RealmRepresentation
is by leveraging the export functionality Importing and Exporting Realms.
- Export the Realm to a single file.
- Convert the JSON file to YAML.
-
Copy and paste the obtained YAML file as body for the
realm
key, making sure the indentation is correct.
3.1.2. Applying the Realm Import CR
Use oc
to create the CR in the correct cluster namespace:
Create YAML file example-realm-import.yaml
:
apiVersion: k8s.keycloak.org/v2alpha1
kind: KeycloakRealmImport
metadata:
name: my-realm-kc
spec:
keycloakCRName: <name of the keycloak CR>
realm:
id: example-realm
realm: example-realm
displayName: ExampleRealm
enabled: true
Apply the changes:
oc apply -f example-realm-import.yaml
To check the status of the running import, enter the following command:
oc get keycloakrealmimports/my-realm-kc -o go-template='{{range .status.conditions}}CONDITION: {{.type}}{{"\n"}} STATUS: {{.status}}{{"\n"}} MESSAGE: {{.message}}{{"\n"}}{{end}}'
When the import has successfully completed, the output will look like the following example:
CONDITION: Done
STATUS: true
MESSAGE:
CONDITION: Started
STATUS: false
MESSAGE:
CONDITION: HasErrors
STATUS: false
MESSAGE:
3.1.3. Placeholders
Imports support placeholders referencing environment variables, see Importing and Exporting Realms for more. The KeycloakRealmImport
CR allows you to leverage this functionality via the spec.placeholders
stanza, for example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: KeycloakRealmImport
metadata:
name: my-realm-kc
spec:
keycloakCRName: <name of the keycloak CR>
placeholders:
ENV_KEY:
secret:
name: SECRET_NAME
key: SECRET_KEY
...
In the above example placeholder replacement will be enabled and an environment variable with key ENV_KEY
will be created from the Secret SECRET_NAME’s value for key `SECRET_KEY
. Currently only Secrets are supported and they must be in the same namespace as the Keycloak CR.
3.1.4. Security Considerations
Anyone with the ability to create or edit KeycloakRealmImport CRs should be a namespace level admin.
Placeholder replacement gives access to all environment variables even sensitive ones.
