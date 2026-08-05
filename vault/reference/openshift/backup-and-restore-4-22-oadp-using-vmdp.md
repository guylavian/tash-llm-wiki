---
title: "Using {oadp-short} virtual machine data protection"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-using-vmdp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-using-vmdp
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Using {oadp-short} virtual machine data protection

[id="oadp-using-vmdp"]
= Using {oadp-short} virtual machine data protection

[role="_abstract"]
Install the {oadp-full} virtual machine data protection (VMDP) command-line interface (CLI), configure a backup storage location, and back up and restore data from within your VM. This helps you to manage your own VM backups independently.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-installing-cli_{context}"]
= Installing the {oadp-short} virtual machine data protection CLI

[role="_abstract"]
Install the {oadp-full} virtual machine data protection (VMDP) command-line interface (CLI) inside your VM to back up and restore data. This helps you to download the correct binary for your VM guest operating system.

The {oadp-short} Operator deploys a download server in the cluster as the `openshift-adp-vmdp-server` service in the `openshift-adp` namespace. A `ConsoleCLIDownload` resource links to the download server routes, and users can access the download links from the OpenShift Container Platform web console or by using HTTP directly.

.Prerequisites

* You have installed the {oadp-short} Operator.
* You have a running VM on {VirtProductName} with a supported guest operating system.
* You have installed the `virtctl` CLI tool.

.Procedure

. Get the cluster IP of the VMDP download server by running the following command:
+
[source,terminal]
----
$ oc get svc -n openshift-adp openshift-adp-vmdp-server
----
+
Make a note of the `CLUSTER-IP` value from the output.

. Install the VMDP CLI:

** For Linux VMs, download the VMDP binary and make it executable inside the VM by running the following command:
+
[source,terminal]
----
$ virtctl ssh <vm_user>@<vm_name> -n <vm_namespace> \
  --command "curl -kLf 'http://<cluster_ip>:80/download/oadp-vmdp_linux_amd64' \
  -o oadp-vmdp_linux_amd64 && chmod +x oadp-vmdp_linux_amd64"
----
+
where:

`<vm_user>`:: Specifies the username for the VM. For example, `fedora`.
`<vm_name>`:: Specifies the name of the VM.
`<vm_namespace>`:: Specifies the namespace of the VM.
`<cluster_ip>`:: Specifies the `CLUSTER-IP` value of the `openshift-adp-vmdp-server` service.

** For Microsoft Windows VMs, access the VM by using Remote Desktop Protocol (RDP) or the VNC console, open PowerShell, and download the VMDP binary by running the following command:
+
[source,powershell]
----
PS> curl.exe -L -o oadp-vmdp.exe "http://<cluster_ip>:80/download/oadp-vmdp_windows_amd64.exe"
----
+
Replace `<cluster_ip>` with the `CLUSTER-IP` value of the `openshift-adp-vmdp-server` service.

.Verification

* Depending on your operating system, use one of the following steps to verify the installation:

** For Linux VMs, verify that the binary is installed and working by running the following command:
+
[source,terminal]
----
$ virtctl ssh <vm_user>@<vm_name> -n <vm_namespace> \
  --command "./oadp-vmdp_linux_amd64 --help"
----
+
[source,terminal]
----
usage: oadp-vmdp [<flags>] <command> [<args> ...]
OADP VM Data Protection - Virtual Machine Data Protection for OpenShift
    Virtualization

Flags:
  --[no-]help                Show context-sensitive help (also try --help-long
                             and --help-man).
  --[no-]version             Show application version.
  --log-file=LOG-FILE        Override log file.
  --[no-]disable-file-logging
                             Disable file-based logging.
  ....
----

** For Microsoft Windows VMs, open PowerShell and verify the binary by running the following command:
+
[source,powershell]
----
PS> .\oadp-vmdp.exe --help
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-creating-bsl-s3_{context}"]
= Creating a backup storage location with S3-compatible storage by using the VMDP CLI

[role="_abstract"]
Create a backup storage location (BSL) with S3-compatible storage to set up an encrypted repository for storing your virtual machine (VM) backups. This helps you to configure remote S3-compatible storage for your data.

When you create a BSL, the virtual machine data protection (VMDP) command-line interface (CLI) creates a personal encrypted repository in the specified storage backend. You provide the encryption password, which is used to encrypt all backup data. Only users with this password can access the backup data.

.Prerequisites

* You have installed the VMDP CLI inside your VM.
* You have the storage credentials for your S3-compatible storage.

.Procedure

. To create a BSL with S3-compatible storage, run the following command:
+
[source,terminal]
----
$ sshpass -p <vm_password> virtctl ssh vm/<vm_name> -n <vm_namespace> \
  --username <vm_username> \
  --local-ssh-opts=-oUserKnownHostsFile=/dev/null \
  --local-ssh-opts=-oStrictHostKeyChecking=no \
  --local-ssh-opts=-oPreferredAuthentications=password \
  --local-ssh-opts=-oPubkeyAuthentication=no \
  --command "./oadp-vmdp_linux_amd64 bsl create s3 --bucket <bucket_name> --endpoint <s3_endpoint> --access-key <access_key> --secret-access-key <secret_access_key> --disable-tls"
----
+
where:

`<vm_password>`:: Specifies the password for the VM user.
`<vm_name>`:: Specifies the name of the VM.
`<vm_namespace>`:: Specifies the namespace of the VM.
`<vm_username>`:: Specifies the username for the VM. For example, `fedora`.
`<bucket_name>`:: Specifies the name of the S3 bucket.
`<s3_endpoint>`:: Specifies the S3 endpoint URL.
`<access_key>`:: Specifies the access key ID.
`<secret_access_key>`:: Specifies the secret access key.

+
You should see an output similar to the following example:
+
[source,terminal]
----
Initializing repository with:
  block hash:          BLAKE2B-256-128
  encryption:          AES256-GCM-HMAC-SHA256
  key derivation:      scrypt-65536-8-1
  splitter:            DYNAMIC-4M-BUZHASH
----

. Create an alias for the VMDP binary and name it `oadp-vmdp`.

.Verification

* To verify the BSL connection status, run the following command:
+
[source,terminal]
----
$ oadp-vmdp bsl status
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-creating-bsl-filesystem_{context}"]
= Creating a backup storage location with file system storage by using the VMDP CLI

[role="_abstract"]
Create a backup storage location (BSL) with file system storage to set up an encrypted repository for storing your virtual machine (VM) backups. This helps you to configure local file system storage for your data.

When you create a BSL, the virtual machine data protection (VMDP) command-line interface (CLI) creates a personal encrypted repository in the specified storage backend. You provide the encryption password, which is used to encrypt all backup data. Only users with this password can access the backup data.

.Prerequisites

* You have installed the VMDP CLI inside your VM.
* You have created an alias called `oadp-vmdp` for the VMDP CLI binary.
* You have access to a local file system path for backup storage.

.Procedure

* To create a BSL with file system storage, run the following command:
+
[source,terminal]
----
$ oadp-vmdp bsl create filesystem \
  --path <storage_directory_path>
----
+
Replace `<storage_directory_path>` with the absolute path to the storage directory.

.Verification

* To verify the BSL connection status, run the following command:
+
[source,terminal]
----
$ oadp-vmdp bsl status
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-backing-up-data_{context}"]
= Backing up data from a virtual machine by using the VMDP CLI

[role="_abstract"]
Back up files and directories from within your virtual machine (VM) by using the {oadp-full} VM data protection (VMDP) command-line interface (CLI). This helps you to protect user data, including data accessible over network file systems such as CIFS and NFS shares.

VMDP uses data deduplication to store data efficiently. If the same data exists in multiple locations, subsequent backups complete faster because only unique data blocks are stored.

.Prerequisites

* You are connected to your virtual machine (VM) by using SSH.
* You have installed the VMDP CLI inside your VM.
* You have created an alias called `oadp-vmdp` for the VMDP CLI binary.
* You have created and connected to a backup storage location.

.Procedure

. To create a backup of a directory, run the following command:
+
[source,terminal]
----
$ oadp-vmdp backup create <path_to_data>
----
+
Replace `<path_to_data>` with the path to the directory or files to back up.

. To list all available backups, run the following command:
+
[source,terminal]
----
$ oadp-vmdp backup list
----

. To delete a specific backup, run the following command:
+
[source,terminal]
----
$ oadp-vmdp backup delete <backup_id>
----
+
Replace `<backup_id>` with the ID of the backup to delete.
+
[IMPORTANT]
====
After you delete backups, orphaned data objects such as pack blobs are not automatically cleaned up from the underlying storage backend. You must manually remove these orphaned objects directly from your storage backend, for example, by deleting them from your S3 bucket.
====

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-restoring-data_{context}"]
= Restoring data to a virtual machine by using the VMDP CLI

[role="_abstract"]
Restore data from a backup to your virtual machine (VM) by using the {oadp-full} VM data protection (VMDP) command-line interface (CLI). This helps you to recover files to the original location or to a different directory.

You can restore from the most recent backup or from a specific backup by specifying its ID. You can also restore to a different VM by connecting to the BSL of the new VM.

.Prerequisites

* You are connected to your VM by using SSH.
* You have installed the VMDP CLI inside your VM.
* You have created an alias called `oadp-vmdp` for the VMDP CLI binary.
* You have connected to the backup storage location that contains the backup.

.Procedure

* Depending on your specific use case, use one of the following steps to restore data:

** To restore data from the most recent backup, run the following command:
+
[source,terminal]
----
$ oadp-vmdp restore <path_to_restore>
----
+
Replace `<path_to_restore>` with the path to restore.

** To restore a specific backup to a custom location, run the following commands:

. Retrieve the source backup ID:
+
[source,terminal]
----
$ oadp-vmdp backup list
----

. Restore the backup by running the following command:
+
[source,terminal]
----
$ oadp-vmdp restore <source_id> <restore_path>
----
+
where:

`<source_id>`:: Specifies the ID of the backup to restore.
`<restore_path>`:: Specifies the directory path where the data is restored.

** To restore data from a different VM, run the following commands:

. To connect to the existing BSL from the new VM, run the following command:
+
[source,terminal]
----
$ oadp-vmdp bsl connect s3 \
  --bucket <bucket_name> \
  --endpoint <s3_endpoint> \
  --access-key <access_key> \
  --secret-access-key <secret_access_key>
----

. Restore from the BSL by running the following command:
+
[source,terminal]
----
$ oadp-vmdp restore <path_to_data>
----

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-managing-bsl_{context}"]
= {oadp-short} VMDP BSL management commands

[role="_abstract"]
Review the available commands for managing backup storage locations (BSL) with the virtual machine data protection (VMDP) command-line interface (CLI). This helps you to connect, disconnect, and manage your BSL connections.

.BSL management commands
[cols="1,1",options="header"]
|===
|Command |Description

|`oadp-vmdp bsl create`
|Create and connect to a new BSL.

|`oadp-vmdp bsl connect`
|Connect to an existing BSL.

|`oadp-vmdp bsl disconnect`
|Disconnect from the current BSL.

|`oadp-vmdp bsl status`
|Show the current BSL connection status.

|`oadp-vmdp bsl change-password`
|Change the BSL encryption password.
|===

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-using-vmdp.adoc

[id="oadp-vmdp-troubleshooting_{context}"]
= Troubleshooting {oadp-short} virtual machine data protection

[role="_abstract"]
Troubleshoot common issues and solutions for the {oadp-full} virtual machine data protection (VMDP) command-line interface (CLI). This helps you to resolve connection and configuration problems.

== Not connected to a backup storage location

If you receive a `Not connected to a Backup Storage Location` error message, check the connection status and reconnect:

[source,terminal]
----
$ oadp-vmdp bsl status
----

[source,terminal]
----
$ oadp-vmdp bsl connect s3 \
  --bucket <bucket_name> \
  --endpoint <s3_endpoint> \
  --access-key <access_key> \
  --secret-access-key <secret_access_key>
----

== Prefix must not contain oadp-vmdp

The `oadp-vmdp/` prefix is added automatically. Do not include `oadp-vmdp` as a path segment in the `--prefix` option. Ensure that the `--prefix` value does not start or end with whitespace.

== S3 connection issues

For S3-compatible services, you might need to use the following options:

* `--disable-tls` for non-HTTPS endpoints.
* `--disable-tls-verification` for self-signed certificates.
* `--root-ca-pem-path` to specify a custom CA certificate.

== Getting help

* To view available commands and options, run the following command:

[source,terminal]
----
$ oadp-vmdp --help
----

* To view help for a specific command, run the following command:

[source,terminal]
----
$ oadp-vmdp <command> --help
----
