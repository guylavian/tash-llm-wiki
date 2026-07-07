---
title: "Syncing LDAP groups"
type: reference
domain: openshift
slug: authentication-4-22-ldap-syncing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/ldap-syncing
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Syncing LDAP groups

[id="ldap-syncing"]
= Syncing LDAP groups

As an administrator,
As an administrator with the `dedicated-admin` role,
you can use groups to manage users, change
their permissions, and enhance collaboration. Your organization may have already
created user groups and stored them in an LDAP server. OpenShift Container Platform can sync
those LDAP records with internal OpenShift Container Platform records, enabling you to manage
your groups in one place. OpenShift Container Platform currently supports group sync with
LDAP servers using three common schemas for defining group membership: RFC 2307,
Active Directory, and augmented Active Directory.

For more information on configuring LDAP, see
Configuring an LDAP identity provider.

For more information on configuring LDAP, see
Configuring an LDAP identity provider.

[NOTE]
====
You must have `cluster-admin` privileges to sync groups.
====
[NOTE]
====
You must have `dedicated-admin` privileges to sync groups.
====

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-about_{context}"]
= About configuring LDAP sync

Before you can run LDAP sync, you need a sync
configuration file. This file contains the following LDAP client configuration details:

* Configuration for connecting to your LDAP server.
* Sync configuration options that are dependent on the schema used in your LDAP
server.
* An administrator-defined list of name mappings that maps OpenShift Container Platform group names to groups in your LDAP server.

The format of the configuration file depends upon the schema you are using: RFC 2307, Active Directory, or augmented Active Directory.

[[ldap-client-configuration]]
LDAP client configuration::

The LDAP client configuration section of the configuration defines the connections to your LDAP server.

The LDAP client configuration section of the configuration defines the connections to your LDAP server.

.LDAP client configuration
[source,yaml]
----
url: ldap://10.0.0.0:389 <1>
bindDN: cn=admin,dc=example,dc=com <2>
bindPassword: <password> <3>
insecure: false <4>
ca: my-ldap-ca-bundle.crt <5>
----
<1> The connection protocol, IP address of the LDAP server hosting your
database, and the port to connect to, formatted as `scheme://host:port`.
<2> Optional distinguished name (DN) to use as the Bind DN.
OpenShift Container Platform uses this if elevated privilege is required to retrieve entries for
the sync operation.
<3> Optional password to use to bind. OpenShift Container Platform uses this if elevated privilege is
necessary to retrieve entries for the sync operation. This value may also be
provided in an environment variable, external file, or encrypted file.
<4> When `false`, secure
LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are
upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.
<5> The certificate bundle to use for validating server certificates for the
configured URL. If empty, OpenShift Container Platform uses system-trusted roots. This only applies
if `insecure` is set to `false`.

[[ldap-query-definition]]
LDAP query definition::
Sync configurations consist of LDAP query definitions for the entries that are
required for synchronization. The specific definition of an LDAP query depends
on the schema used to store membership information in the LDAP server.

.LDAP query definition
[source,yaml]
----
baseDN: ou=users,dc=example,dc=com <1>
scope: sub <2>
derefAliases: never <3>
timeout: 0 <4>
filter: (objectClass=person) <5>
pageSize: 0 <6>
----
<1> The distinguished name (DN) of the branch of the directory where all
searches will start from. It is required that you specify the top of your
directory tree, but you can also specify a subtree in the directory.
<2> The scope of the search. Valid values are `base`, `one`, or `sub`. If this
is left undefined, then a scope of `sub` is assumed. Descriptions of the scope
options can be found in the table below.
<3> The behavior of the search with respect to aliases in the LDAP tree. Valid
values are `never`, `search`, `base`, or `always`. If this is left undefined,
then the default is to `always` dereference aliases. Descriptions of the
dereferencing behaviors can be found in the table below.
<4> The time limit allowed for the search by the client, in seconds. A value of
`0` imposes no client-side limit.
<5> A valid LDAP search filter. If this is left undefined, then the default is
`(objectClass=*)`.
<6> The optional maximum size of response pages from the server, measured in LDAP
entries. If set to `0`, no size restrictions will be made on pages of responses.
Setting paging sizes is necessary when queries return more entries than the
client or server allow by default.

[[ldap-search]]
.LDAP search scope options
[cols="2a,8a",options="header"]
|===
|LDAP search scope | Description
.^|`base`          | Only consider the object specified by the base DN given for the query.
.^|`one`           | Consider all of the objects on the same level in the tree as the base DN for
the query.
.^|`sub`           | Consider the entire subtree rooted at the base DN given for the query.
|===

[[deref-aliases]]
.LDAP dereferencing behaviors
[cols="2a,8a",options="header"]
|===
|Dereferencing behavior | Description
.^|`never`              | Never dereference any aliases found in the LDAP tree.
.^|`search`             | Only dereference aliases found while searching.
.^|`base`               | Only dereference aliases while finding the base object.
.^|`always`             | Always dereference all aliases found in the LDAP tree.
|===

[[user-defined-name-mapping]]
User-defined name mapping::
A user-defined name mapping explicitly maps the names of OpenShift Container Platform groups to
unique identifiers that find groups on your LDAP server. The mapping uses normal
YAML syntax. A user-defined mapping can contain an entry for every group in your
LDAP server or only a subset of those groups. If there are groups on the LDAP
server that do not have a user-defined name mapping, the default behavior during
sync is to use the attribute specified as the OpenShift Container Platform group's name.

.User-defined name mapping
[source,yaml]
----
groupUIDNameMapping:
  "cn=group1,ou=groups,dc=example,dc=com": firstgroup
  "cn=group2,ou=groups,dc=example,dc=com": secondgroup
  "cn=group3,ou=groups,dc=example,dc=com": thirdgroup
----

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-config-rfc2307_{context}"]
= About the RFC 2307 configuration file

The RFC 2307 schema requires you to provide an LDAP query definition for both user
and group entries, as well as the attributes with which to represent them in the
internal OpenShift Container Platform records.

For clarity, the group you create in OpenShift Container Platform should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the
name of the group as the common name. The following configuration file creates
these relationships:

[NOTE]
====
If using user-defined name mappings, your configuration file will differ.
====

.LDAP sync configuration that uses RFC 2307 schema: `rfc2307_config.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389 <1>
insecure: false <2>
bindDN: cn=admin,dc=example,dc=com
bindPassword:
  file: "/etc/secrets/bindPassword"
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <3>
    groupNameAttributes: [ cn ] <4>
    groupMembershipAttributes: [ member ] <5>
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn <6>
    userNameAttributes: [ mail ] <7>
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
----
<1> The IP address and host of the LDAP server where this group's record is
stored.
<2> When `false`, secure
LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are
upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.
<3> The attribute that uniquely identifies a group on the LDAP server.
You cannot specify `groupsQuery` filters when using DN for `groupUIDAttribute`.
For fine-grained filtering, use the whitelist / blacklist method.
<4> The attribute to use as the name of the group.
<5> The attribute on the group that stores the membership information.
<6> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.
<7> The attribute to use as the name of the user in the OpenShift Container Platform group record.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-config-activedir_{context}"]
= About the Active Directory configuration file

The Active Directory schema requires you to provide an LDAP query definition for
user entries, as well as the attributes to represent them with in the internal
OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, but define
the name of the group by the name of the group on the LDAP server.
The following configuration file creates these relationships:

.LDAP sync configuration that uses Active Directory schema: `active_directory_config.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
activeDirectory:
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ] <1>
    groupMembershipAttributes: [ memberOf ] <2>
----
<1> The attribute to use as the name of the user in the OpenShift Container Platform group record.
<2> The attribute on the user that stores the membership information.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-config-augmented-activedir_{context}"]
=  About the augmented Active Directory configuration file

The augmented Active Directory schema requires you to provide an LDAP query
definition for both user entries and group entries, as well as the attributes
with which to represent them in the internal OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an OpenShift Container Platform group by their e-mail,
and use the name of the group as the common name. The following configuration
file creates these relationships.

.LDAP sync configuration that uses augmented Active Directory schema: `augmented_active_directory_config.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <1>
    groupNameAttributes: [ cn ] <2>
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ] <3>
    groupMembershipAttributes: [ memberOf ] <4>
----
<1> The attribute that uniquely identifies a group on the LDAP server. You
cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For
fine-grained filtering, use the whitelist / blacklist method.
<2> The attribute to use as the name of the group.
<3> The attribute to use as the name of the user in the OpenShift Container Platform group record.
<4> The attribute on the user that stores the membership information.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

[id="ldap-syncing-running_{context}"]
= Running LDAP sync

Once you have created a sync configuration file, you can begin to sync. OpenShift Container Platform allows administrators to perform a number of different sync types with the same server.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

[id="ldap-syncing-running-all-ldap_{context}"]
= Syncing the LDAP server with OpenShift Container Platform

You can sync all groups from the LDAP server with OpenShift Container Platform.

.Prerequisites

* Create a sync configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* To sync all groups from the LDAP server with OpenShift Container Platform:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=config.yaml --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to OpenShift Container Platform group records.
====

// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

[id="ldap-syncing-running-openshift_{context}"]
= Syncing OpenShift Container Platform groups with the LDAP server

You can sync all groups already in OpenShift Container Platform that correspond to groups in the
LDAP server specified in the configuration file.

.Prerequisites

* Create a sync configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* To sync OpenShift Container Platform groups with the LDAP server:
+
[source,terminal]
----
$ oc adm groups sync --type=openshift --sync-config=config.yaml --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to OpenShift Container Platform group records.
====

// Module included in the following assemblies:
//
// * authentication/ldap-syncing-groups.adoc

[id="ldap-syncing-running-subset_{context}"]
= Syncing subgroups from the LDAP server with OpenShift Container Platform

You can sync a subset of LDAP groups with OpenShift Container Platform using whitelist files,
blacklist files, or both.

[NOTE]
====
You can use any combination of blacklist files, whitelist files, or whitelist
literals. Whitelist and blacklist files must contain one unique group identifier
per line, and you can include whitelist literals directly in the command itself.
These guidelines apply to groups found on LDAP servers as well as groups already
present in OpenShift Container Platform.
====

.Prerequisites

* Create a sync configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* To sync a subset of LDAP groups with OpenShift Container Platform, use any the following commands:
+
[source,terminal]
----
$ oc adm groups sync --whitelist=<whitelist_file> \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync --blacklist=<blacklist_file> \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync <group_unique_identifier>    \
                   --sync-config=config.yaml      \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync <group_unique_identifier>  \
                   --whitelist=<whitelist_file> \
                   --blacklist=<blacklist_file> \
                   --sync-config=config.yaml    \
                   --confirm
----
+
[source,terminal]
----
$ oc adm groups sync --type=openshift           \
                   --whitelist=<whitelist_file> \
                   --sync-config=config.yaml    \
                   --confirm
----
+
[NOTE]
====
By default, all group synchronization operations are dry-run, so you
must set the `--confirm` flag on the `oc adm groups sync` command to make
changes to OpenShift Container Platform group records.
====

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-pruning_{context}"]
= Running a group pruning job

An administrator can also choose to remove groups from OpenShift Container Platform records if the records on the LDAP server that created them are no longer present. The prune job will accept the same sync configuration file and whitelists or blacklists as used for the sync job.

For example:

[source,terminal]
----
$ oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
----

[source,terminal]
----
$ oc adm prune groups --whitelist=/path/to/whitelist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
----

[source,terminal]
----
$ oc adm prune groups --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
----

// OSD and ROSA dedicated-admins cannot create the cluster roles and cluster role bindings required for this procedure.
// Automatically syncing LDAP groups
// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-auto-syncing_{context}"]
= Automatically syncing LDAP groups

You can automatically sync LDAP groups on a periodic basis by configuring a cron job.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have configured an LDAP identity provider (IDP).
+
This procedure assumes that you created an LDAP secret named `ldap-secret` and a config map named `ca-config-map`.

.Procedure

. Create a project where the cron job will run:
+
[source,terminal]
----
$ oc new-project ldap-sync <1>
----
<1> This procedure uses a project called `ldap-sync`.

. Locate the secret and config map that you created when configuring the LDAP identity provider and copy them to this new project.
+
The secret and config map exist in the `openshift-config` project and must be copied to the new `ldap-sync` project.

. Define a service account:
+
.Example `ldap-sync-service-account.yaml`
[source,yaml]
----
kind: ServiceAccount
apiVersion: v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
----

. Create the service account:
+
[source,terminal]
----
$ oc create -f ldap-sync-service-account.yaml
----

. Define a cluster role:
+
.Example `ldap-sync-cluster-role.yaml`
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ldap-group-syncer
rules:
  - apiGroups:
      - user.openshift.io
    resources:
      - groups
    verbs:
      - get
      - list
      - create
      - update
----

. Create the cluster role:
+
[source,terminal]
----
$ oc create -f ldap-sync-cluster-role.yaml
----

. Define a cluster role binding to bind the cluster role to the service account:
+
.Example `ldap-sync-cluster-role-binding.yaml`
[source,yaml]
----
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ldap-group-syncer
subjects:
  - kind: ServiceAccount
    name: ldap-group-syncer              <1>
    namespace: ldap-sync
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ldap-group-syncer                <2>
----
<1> Reference to the service account created earlier in this procedure.
<2> Reference to the cluster role created earlier in this procedure.

. Create the cluster role binding:
+
[source,terminal]
----
$ oc create -f ldap-sync-cluster-role-binding.yaml
----

. Define a config map that specifies the sync configuration file:
+
.Example `ldap-sync-config-map.yaml`
[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
data:
  sync.yaml: |                                 <1>
    kind: LDAPSyncConfig
    apiVersion: v1
    url: ldaps://10.0.0.0:636                  <2>
    insecure: false
    bindDN: cn=admin,dc=example,dc=com         <3>
    bindPassword:
      file: "/etc/secrets/bindPassword"
    ca: /etc/ldap-ca/ca.crt
    rfc2307:                                   <4>
      groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"  <5>
        scope: sub
        filter: "(objectClass=groupOfMembers)"
        derefAliases: never
        pageSize: 0
      groupUIDAttribute: dn
      groupNameAttributes: [ cn ]
      groupMembershipAttributes: [ member ]
      usersQuery:
        baseDN: "ou=users,dc=example,dc=com"   <6>
        scope: sub
        derefAliases: never
        pageSize: 0
      userUIDAttribute: dn
      userNameAttributes: [ uid ]
      tolerateMemberNotFoundErrors: false
      tolerateMemberOutOfScopeErrors: false
----
<1> Define the sync configuration file.
<2> Specify the URL.
<3> Specify the `bindDN`.
<4> This example uses the RFC2307 schema; adjust values as necessary. You can also use a different schema.
<5> Specify the `baseDN` for `groupsQuery`.
<6> Specify the `baseDN` for `usersQuery`.

. Create the config map:
+
[source,terminal]
----
$ oc create -f ldap-sync-config-map.yaml
----

. Define a cron job:
+
.Example `ldap-sync-cron-job.yaml`
[source,yaml]
----
kind: CronJob
apiVersion: batch/v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
spec:                                                                                <1>
  schedule: "*/30 * * * *"                                                           <2>
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 0
      ttlSecondsAfterFinished: 1800                                                  <3>
      template:
        spec:
          containers:
            - name: ldap-group-sync
              image: "registry.redhat.io/openshift4/ose-cli:latest"
              command:
                - "/bin/bash"
                - "-c"
                - "oc adm groups sync --sync-config=/etc/config/sync.yaml --confirm" <4>
              volumeMounts:
                - mountPath: "/etc/config"
                  name: "ldap-sync-volume"
                - mountPath: "/etc/secrets"
                  name: "ldap-bind-password"
                - mountPath: "/etc/ldap-ca"
                  name: "ldap-ca"
          volumes:
            - name: "ldap-sync-volume"
              configMap:
                name: "ldap-group-syncer"
            - name: "ldap-bind-password"
              secret:
                secretName: "ldap-secret"                                            <5>
            - name: "ldap-ca"
              configMap:
                name: "ca-config-map"                                                <6>
          restartPolicy: "Never"
          terminationGracePeriodSeconds: 30
          activeDeadlineSeconds: 500
          dnsPolicy: "ClusterFirst"
          serviceAccountName: "ldap-group-syncer"
----
<1> Configure the settings for the cron job. See "Creating cron jobs" for more information on cron job settings.
<2> The schedule for the job specified in cron format. This example cron job runs every 30 minutes. Adjust the frequency as necessary, making sure to take into account how long the sync takes to run.
<3> How long, in seconds, to keep finished jobs. This should match the period of the job schedule in order to clean old failed jobs and prevent unnecessary alerts. For more information, see TTL-after-finished Controller in the Kubernetes documentation.
<4> The LDAP sync command for the cron job to run. Passes in the sync configuration file that was defined in the config map.
<5> This secret was created when the LDAP IDP was configured.
<6> This config map was created when the LDAP IDP was configured.

. Create the cron job:
+
[source,terminal]
----
$ oc create -f ldap-sync-cron-job.yaml
----

[role="_additional-resources"]
.Additional resources

* Configuring an LDAP identity provider
* Creating cron jobs

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-examples_{context}"]
= LDAP group sync examples

This section contains examples for the RFC 2307, Active Directory, and augmented Active Directory schemas.

[NOTE]
====
These examples assume that all users are direct members of their respective groups. Specifically, no groups have other groups as members. See the Nested Membership Sync Example for information on how to sync nested groups.
====

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-rfc2307_{context}"]
= Syncing groups using the RFC 2307 schema

For the RFC 2307 schema, the following examples synchronize a group named `admins` that has two
members: `Jane` and `Jim`. The examples explain:

* How the group and users are added to the LDAP server.
* What the resulting group record in OpenShift Container Platform will be after synchronization.

[NOTE]
====
These examples assume that all users are direct members of their respective
groups. Specifically, no groups have other groups as members. See
the Nested Membership Sync Example for information on
how to sync nested groups.
====

In the RFC 2307 schema, both users (Jane and Jim) and groups exist on the LDAP
server as first-class entries, and group membership is stored in attributes on
the group. The following snippet of `ldif` defines the users and group for this
schema:

.LDAP entries that use RFC 2307 schema: `rfc2307.ldif`
[source,ldif]
----
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com <1>
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com <2>
  member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The group is a first-class entry in the LDAP server.
<2> Members of a group are listed with an identifying reference as attributes on
the group.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `rfc2307_config.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config.yaml --confirm
----
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `rfc2307_config.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801
format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is
stored.
<4> The name of the group as specified by the sync file.
<5> The users that are members of the group, named as specified by the sync file.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-rfc2307-user-defined_{context}"]
= Syncing groups using the RFC2307 schema with user-defined name mappings

When syncing groups with user-defined name mappings, the configuration file
changes to contain these mappings as shown below.

.LDAP sync configuration that uses RFC 2307 schema with user-defined name mappings: `rfc2307_config_user_defined.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
groupUIDNameMapping:
  "cn=admins,ou=groups,dc=example,dc=com": Administrators <1>
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <2>
    groupNameAttributes: [ cn ] <3>
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn <4>
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
----
<1> The user-defined name mapping.
<2> The unique identifier attribute that is used for the keys in the
user-defined name mapping. You cannot specify `groupsQuery` filters when using
DN for groupUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.
<3> The attribute to name OpenShift Container Platform groups with if their unique identifier is
not in the user-defined name mapping.
<4> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `rfc2307_config_user_defined.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config_user_defined.yaml --confirm
----
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `rfc2307_config_user_defined.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: Administrators <1>
users:
- jane.smith@example.com
- jim.adams@example.com
----
<1> The name of the group as specified by the user-defined name mapping.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-rfc2307-user-defined-error_{context}"]
= Syncing groups using RFC 2307 with user-defined error tolerances

By default, if the groups being synced contain members whose entries are outside
of the scope defined in the member query, the group sync fails with an error:

----
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with dn="<user-dn>" would search outside of the base dn specified (dn="<base-dn>")".
----

This often indicates a misconfigured `baseDN` in the `usersQuery` field.
However, in cases where the `baseDN` intentionally does not contain some of the
members of the group, setting `tolerateMemberOutOfScopeErrors: true` allows
the group sync to continue. Out of scope members will be ignored.

Similarly, when the group sync process fails to locate a member for a group, it
fails outright with errors:

----
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" refers to a non-existent entry".
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" and filter "<filter>" did not return any results".
----

This often indicates a misconfigured `usersQuery` field. However, in cases
where the group contains member entries that are known to be missing, setting
`tolerateMemberNotFoundErrors: true` allows the group sync to continue.
Problematic members will be ignored.

[WARNING]
====
Enabling error tolerances for the LDAP group sync causes the sync process to
ignore problematic member entries. If the LDAP group sync is not configured
correctly, this could result in synced OpenShift Container Platform groups missing members.
====

.LDAP entries that use RFC 2307 schema with problematic group membership: `rfc2307_problematic_users.ldif`
[source,ldif]
----
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
  member: cn=INVALID,ou=users,dc=example,dc=com <1>
  member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com <2>
----
<1> A member that does not exist on the LDAP server.
<2> A member that may exist, but is not under the `baseDN` in the
user query for the sync job.

To tolerate the errors in the above example, the following additions to
your sync configuration file must be made:

.LDAP sync configuration that uses RFC 2307 schema tolerating errors: `rfc2307_config_tolerating.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
    userUIDAttribute: dn <1>
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: true <2>
    tolerateMemberOutOfScopeErrors: true <3>
----
<1> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.
<2> When `true`, the sync job tolerates groups for which some members were not
found, and members whose LDAP entries are not found are ignored. The
default behavior for the sync job is to fail if a member of a group is not
found.
<3> When `true`, the sync job tolerates groups for which some members are outside
the user scope given in the `usersQuery` base DN, and members outside the member
query scope are ignored. The default behavior for the sync job is to fail if a
member of a group is out of scope.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `rfc2307_config_tolerating.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config_tolerating.yaml --confirm
----
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `rfc2307_config.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users: <1>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The users that are members of the group, as specified by the sync file.
Members for which lookup encountered tolerated errors are absent.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-activedir_{context}"]
= Syncing groups using the Active Directory schema

In the Active Directory schema, both users (Jane and Jim) exist in the LDAP
server as first-class entries, and group membership is stored in attributes on
the user. The following snippet of `ldif` defines the users and group for this
schema:

.LDAP entries that use Active Directory schema: `active_directory.ldif`
[source,ldif]
----
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: admins <1>

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: admins
----
<1> The user's group memberships are listed as attributes on the user, and the
group does not exist as an entry on the server. The `memberOf` attribute does
not have to be a literal attribute on the user; in some LDAP servers, it is created
during search and returned to the client, but not committed to the database.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `active_directory_config.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=active_directory_config.yaml --confirm
----
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `active_directory_config.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: admins <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801
format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is
stored.
<4> The name of the group as listed in the LDAP server.
<5> The users that are members of the group, named as specified by the sync
file.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-augmented-activedir_{context}"]
= Syncing groups using the augmented Active Directory schema

In the augmented Active Directory schema, both users (Jane and Jim) and groups
exist in the LDAP server as first-class entries, and group membership is stored
in attributes on the user. The following snippet of `ldif` defines the users and
group for this schema:

.LDAP entries that use augmented Active Directory schema: `augmented_active_directory.ldif`
[source,ldif]
----
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com <1>

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com <2>
objectClass: groupOfNames
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The user's group memberships are listed as attributes on the user.
<2> The group is a first-class entry on the LDAP server.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `augmented_active_directory_config.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=augmented_active_directory_config.yaml --confirm
----
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `augmented_active_directory_config.yaml` file

[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is stored.
<4> The name of the group as specified by the sync file.
<5> The users that are members of the group, named as specified by the sync file.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-nesting_{context}"]
== LDAP nested membership sync example

Groups in OpenShift Container Platform do not nest. The LDAP server must flatten group
membership before the data can be consumed. Microsoft's Active Directory Server supports this feature via the `LDAP_MATCHING_RULE_IN_CHAIN` rule, which has the OID `1.2.840.113556.1.4.1941`. Furthermore, only explicitly
whitelisted groups can be synced when using this matching rule.

This section has an example for the augmented Active Directory schema, which
synchronizes a group named `admins` that has one user `Jane` and one group
`otheradmins` as members. The `otheradmins` group has one user member: `Jim`.
This example explains:

* How the group and users are added to the LDAP server.
* What the LDAP sync configuration file looks like.
* What the resulting group record in OpenShift Container Platform will be after synchronization.

In the augmented Active Directory schema, both users (`Jane` and `Jim`) and
groups exist in the LDAP server as first-class entries, and group membership is
stored in attributes on the user or the group. The following snippet of `ldif`
defines the users and groups for this schema:

.LDAP entries that use augmented Active Directory schema with nested members: `augmented_active_directory_nested.ldif`
[source,ldif]
----
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com <1>

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=otheradmins,ou=groups,dc=example,dc=com <1>

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com <2>
objectClass: group
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=otheradmins,ou=groups,dc=example,dc=com

dn: cn=otheradmins,ou=groups,dc=example,dc=com <2>
objectClass: group
cn: otheradmins
owner: cn=admin,dc=example,dc=com
description: Other System Administrators
memberOf: cn=admins,ou=groups,dc=example,dc=com <1> <3>
member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The user's and group's memberships are listed as attributes on the object.
<2> The groups are first-class entries on the LDAP server.
<3> The `otheradmins` group is a member of the `admins` group.

When syncing nested groups with Active Directory, you must provide an LDAP query
definition for both user entries and group entries, as well as the attributes
with which to represent them in the internal OpenShift Container Platform group records.
Furthermore, certain changes are required in this configuration:

- The `oc adm groups sync` command must explicitly whitelist groups.
- The user's `groupMembershipAttributes` must include `"memberOf:1.2.840.113556.1.4.1941:"` to comply with the `LDAP_MATCHING_RULE_IN_CHAIN` rule.
- The `groupUIDAttribute` must be set to `dn`.
- The `groupsQuery`:
  * Must not set `filter`.
  * Must set a valid `derefAliases`.
  * Should not set `baseDN` as that value is ignored.
  * Should not set `scope` as that value is ignored.

For clarity, the group you create in OpenShift Container Platform should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the
name of the group as the common name. The following configuration file creates
these relationships:

.LDAP sync configuration that uses augmented Active Directory schema with nested members: `augmented_active_directory_config_nested.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery: <1>
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <2>
    groupNameAttributes: [ cn ] <3>
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ] <4>
    groupMembershipAttributes: [ "memberOf:1.2.840.113556.1.4.1941:" ] <5>
----
<1> `groupsQuery` filters cannot be specified. The `groupsQuery` base DN and scope
values are ignored. `groupsQuery` must set a valid `derefAliases`.
<2> The attribute that uniquely identifies a group on the LDAP server. It must be set to `dn`.
<3> The attribute to use as the name of the group.
<4> The attribute to use as the name of the user in the OpenShift Container Platform group
record.
+
[NOTE]
====
`mail` or `sAMAccountName` are preferred choices in most installations.
====
<5> The attribute on the user that stores the membership information. Note the use of `LDAP_MATCHING_RULE_IN_CHAIN`.

.Prerequisites

* Create the configuration file.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

* Run the sync with the `augmented_active_directory_config_nested.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync \
    'cn=admins,ou=groups,dc=example,dc=com' \
    --sync-config=augmented_active_directory_config_nested.yaml \
    --confirm
----
+
[NOTE]
====
You must explicitly whitelist the `cn=admins,ou=groups,dc=example,dc=com` group.
====
+
OpenShift Container Platform creates the following group record as a result of the above sync
operation:
+
.OpenShift Container Platform group created by using the `augmented_active_directory_config_nested.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is stored.
<4> The name of the group as specified by the sync file.
<5> The users that are members of the group, named as specified by the sync file.
Note that members of nested groups are included since the group membership was
flattened by the Microsoft Active Directory Server.

// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

[id="ldap-syncing-spec_{context}"]
= LDAP sync configuration specification

The object specification for the configuration file is below.  Note that the different schema
objects have different fields.  For example, v1.ActiveDirectoryConfig has no `groupsQuery`
field whereas v1.RFC2307Config and v1.AugmentedActiveDirectoryConfig both do.

[IMPORTANT]
====
There is no support for binary attributes. All attribute data coming from the
LDAP server must be in the format of a UTF-8 encoded string. For example, never
use a binary attribute, such as `objectGUID`, as an ID attribute. You must use
string attributes, such as `sAMAccountName` or `userPrincipalName`, instead.
====

[[sync-ldap-v1-ldapsyncconfig]]
== v1.LDAPSyncConfig

`LDAPSyncConfig` holds the necessary configuration options to define an LDAP
group sync.

[options="header"]
|===
|Name |Description |Schema

|`kind`
|String value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: 
|string

|`apiVersion`
|Defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: 
|string

|`url`
|Host is the scheme, host and port of the LDAP server to connect to: `scheme://host:port`
|string

|`bindDN`
|Optional DN to bind to the LDAP server with.
|string

|`bindPassword`
|Optional password to bind with during the search phase. |v1.StringSource

|`insecure`
|If `true`, indicates the connection should not use TLS. If `false`, `ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to a TLS connection using StartTLS as specified in . If you set `insecure` to `true`, you cannot use `ldaps://` URL schemes.
|boolean

|`ca`
|Optional trusted certificate authority bundle to use when making requests to the server. If empty, the default system roots are used.
|string

|`groupUIDNameMapping`
|Optional direct mapping of LDAP group UIDs to OpenShift Container Platform group names.
|object

|`rfc2307`
|Holds the configuration for extracting data from an LDAP server set up in a fashion similar to RFC2307: first-class group and user entries, with group membership determined by a multi-valued attribute on the group entry listing its members.
|v1.RFC2307Config

|`activeDirectory`
|Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory: first-class user entries, with group membership determined by a multi-valued attribute on members listing groups they are a member of.
|v1.ActiveDirectoryConfig

|`augmentedActiveDirectory`
|Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory as described above, with one addition: first-class group entries exist and are used to hold metadata but not group membership.
|v1.AugmentedActiveDirectoryConfig
|===

[[sync-ldap-v1-stringsource]]
== v1.StringSource

`StringSource` allows specifying a string inline, or externally via environment
variable or file. When it contains only a string value, it marshals to a simple
JSON string.

[options="header"]
|===
|Name |Description |Schema

|`value`
|Specifies the cleartext value, or an encrypted value if `keyFile` is specified.
|string

|`env`
|Specifies an environment variable containing the cleartext value, or an
encrypted value if the `keyFile` is specified.
|string

|`file`
|References a file containing the cleartext value, or an encrypted value if a `keyFile` is specified.
|string

|`keyFile`
|References a file containing the key to use to decrypt the value.
|string
|===

[[sync-ldap-v1-ldapquery]]
== v1.LDAPQuery

`LDAPQuery` holds the options necessary to build an LDAP query.

[options="header"]
|===
|Name |Description |Schema

|`baseDN`
|DN of the branch of the directory where all searches should start from.
|string

|`scope`
|The optional scope of the search. Can be `base`: only the base object, `one`:
all objects on the base level, `sub`: the entire subtree. Defaults to `sub`
if not set.
|string

|`derefAliases`
|The optional behavior of the search with regards to aliases. Can be `never`:
never dereference aliases, `search`: only dereference in searching, `base`:
only dereference in finding the base object, `always`: always dereference.
Defaults to `always` if not set.
|string

|`timeout`
|Holds the limit of time in seconds that any request to the server can remain outstanding before the wait for a response is given up. If this is `0`, no client-side limit is imposed.
|integer

|`filter`
|A valid LDAP search filter that retrieves all relevant entries from the LDAP server with the base DN.
|string

|`pageSize`
|Maximum preferred page size, measured in LDAP entries. A page size of `0` means no paging will be done.
|integer
|===

[[sync-ldap-v1-rfc2307config]]
== v1.RFC2307Config

`RFC2307Config` holds the necessary configuration options to define how an LDAP
group sync interacts with an LDAP server using the RFC2307 schema.

[options="header"]
|===
|Name |Description |Schema

|`groupsQuery`
|Holds the template for an LDAP query that returns group entries.
|v1.LDAPQuery

|`groupUIDAttribute`
|Defines which attribute on an LDAP group entry will be interpreted as its unique identifier. (`ldapGroupUID`)
|string

|`groupNameAttributes`
|Defines which attributes on an LDAP group entry will be interpreted as its name to use for an OpenShift Container Platform group.
|string array

|`groupMembershipAttributes`
|Defines which attributes on an LDAP group entry will be interpreted as its members. The values contained in those attributes must be queryable by your `UserUIDAttribute`.
|string array

|`usersQuery`
|Holds the template for an LDAP query that returns user entries.
|v1.LDAPQuery

|`userUIDAttribute`
|Defines which attribute on an LDAP user entry will be interpreted as its unique identifier. It must correspond to values that will be found from the `GroupMembershipAttributes`.
|string

|`userNameAttributes`
|Defines which attributes on an LDAP user entry will be used, in order, as its OpenShift Container Platform user name. The first attribute with a non-empty value is used. This should match your `PreferredUsername` setting for your `LDAPPasswordIdentityProvider`. The attribute to use as the name of the user in the OpenShift Container Platform group
record. `mail` or `sAMAccountName` are preferred choices in most installations.
|string array

|`tolerateMemberNotFoundErrors`
|Determines the behavior of the LDAP sync job when missing user entries are encountered. If `true`, an LDAP query for users that does not find any will be tolerated and an only and error will be logged. If `false`, the LDAP sync job will fail if a query for users does not find any. The default value is `false`. Misconfigured LDAP sync jobs with this flag set to `true` can cause group membership to be removed, so it is recommended to use this flag with caution.
|boolean

|`tolerateMemberOutOfScopeErrors`
|Determines the behavior of the LDAP sync job when out-of-scope user entries are encountered. If `true`, an LDAP query for a user that falls outside of the base DN given for the all user query will be tolerated and only an error will be logged. If `false`, the LDAP sync job will fail if a user query would search outside of the base DN specified by the all user query. Misconfigured LDAP sync jobs with this flag set to `true` can result in groups missing users, so it is recommended to use this flag with caution.
|boolean
|===

[[sync-ldap-v1-activedirectoryconfig]]
== v1.ActiveDirectoryConfig

`ActiveDirectoryConfig` holds the necessary configuration options to define how
an LDAP group sync interacts with an LDAP server using the Active Directory
schema.

[options="header"]
|===
|Name |Description |Schema

|`usersQuery`
|Holds the template for an LDAP query that returns user entries.
|v1.LDAPQuery

|`userNameAttributes`
|Defines which attributes on an LDAP user entry will be interpreted as its OpenShift Container Platform user name. The attribute to use as the name of the user in the OpenShift Container Platform group
record. `mail` or `sAMAccountName` are preferred choices in most installations.
|string array

|`groupMembershipAttributes`
|Defines which attributes on an LDAP user entry will be interpreted as the groups it is a member of.
|string array
|===

[[sync-ldap-v1-augmentedactivedirectoryconfig]]
== v1.AugmentedActiveDirectoryConfig

`AugmentedActiveDirectoryConfig` holds the necessary configuration options to
define how an LDAP group sync interacts with an LDAP server using the augmented
Active Directory schema.

[options="header"]
|===
|Name |Description |Schema

|`usersQuery`
|Holds the template for an LDAP query that returns user entries.
|v1.LDAPQuery

|`userNameAttributes`
|Defines which attributes on an LDAP user entry will be interpreted as its OpenShift Container Platform user name. The attribute to use as the name of the user in the OpenShift Container Platform group
record. `mail` or `sAMAccountName` are preferred choices in most installations.
|string array

|`groupMembershipAttributes`
|Defines which attributes on an LDAP user entry will be interpreted as the groups it is a member of.
|string array

|`groupsQuery`
|Holds the template for an LDAP query that returns group entries.
|v1.LDAPQuery

|`groupUIDAttribute`
|Defines which attribute on an LDAP group entry will be interpreted as its unique identifier. (`ldapGroupUID`)
|string

|`groupNameAttributes`
|Defines which attributes on an LDAP group entry will be interpreted as its name to use for an OpenShift Container Platform group.
|string array
|===
