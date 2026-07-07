---
title: "{oadp-short} virtual machine data protection"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-vmdp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-vmdp
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# {oadp-short} virtual machine data protection

[id="oadp-vmdp"]
= {oadp-short} virtual machine data protection

[role="_abstract"]
Use {oadp-full} virtual machine data protection (VMDP) to back up and restore user data from within VMs on {VirtProductName}. This helps you to protect files and directories without relying on cluster administrators.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-vmdp.adoc

[id="oadp-vmdp-overview_{context}"]
= About {oadp-short} virtual machine data protection

[role="_abstract"]
You can independently back up and restore your own data from within a virtual machine (VM) by using the {oadp-short} VM data protection (VMDP) command-line tool. This approach helps you secure specific files and directories in your encrypted repository without requiring cluster administrator privileges.

== What problem is VMDP solving

Cluster administrators manage traditional {oadp-short} backups. The administrator owns the backup storage location, controls what to back up, and manages the restore process. This means that VM users must rely on an administrator to recover their data, and the backup scope is limited to the persistent volume claims (PVCs) attached to the VM at the time of backup.

VMDP addresses this gap by shifting data ownership to the VM user. The user creates their own encrypted backup repository, chooses what data to protect, and restores data without administrator involvement. This follows zero-trust architecture principles where the user owns the data, the backup, and the encryption keys. Administrators cannot access or restore the user's backup data.

== What VMDP does

VMDP is a command-line tool that runs inside virtual machines on {VirtProductName}. With VMDP, you can complete the following tasks:

* Back up and restore files and directories from within the VM by using a single command.
* Protect data accessible over network file systems such as Common Internet File System (CIFS) and Network File System (NFS) shares, which standard {oadp-short} backups typically exclude.
* Create a personal encrypted repository in S3-compatible or file system storage.
* Use data deduplication for efficient storage and fast incremental backups.

VMDP is based on Kopia and uses the same repository format.

== Who uses VMDP

VMDP is designed for VM users who need to manage their own backups independently. The user is responsible for:

* Providing their own credentials to create an encrypted backup repository.
* Choosing what data to back up and restore.
* Managing backup lifecycle operations such as listing, deleting, and restoring backups.

Cluster administrators are not involved in the backup and restore process. Their role is limited to deploying the {oadp-short} Operator. The {oadp-short} Operator has the VMDP CLI available for download.

== VMDP and VMFR comparison

{oadp-short} provides two complementary features for VM data recovery:

VMDP (VM data protection):: The VM user, without `cluster-admin` privileges, owns the data. The user creates encrypted backups of selected files and directories from within the VM. The user holds the encryption keys and manages the backup lifecycle independently.

VMFR (VM file restore):: The cluster administrator manages the backups and file recovery. VMFR enables file-level recovery from admin-created Velero backups of entire VMs, including all PVCs. The administrator controls the backup and restore process.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-vmdp.adoc

[id="oadp-vmdp-supported-platforms_{context}"]
= Supported platforms for {oadp-short} virtual machine data protection

[role="_abstract"]
Review the supported guest operating systems and architectures for the {oadp-full} virtual machine data protection (VMDP) command-line interface. This helps you to verify that your VM environment is compatible.

VMDP is built for {VirtProductName} certified guest operating systems on the following platforms:

.Supported guest operating systems
[cols="1,1",options="header"]
|===
|Guest operating system |Architectures

|Red Hat Enterprise Linux
|x86_64, AArch64

|Microsoft Windows
|x86_64, AArch64
|===

Each binary is statically linked and includes a SHA256 checksum for integrity verification.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-vmdp.adoc

[id="oadp-vmdp-storage-backends_{context}"]
= {oadp-short} virtual machine data protection backend storage

[role="_abstract"]
Review the backend storage options for {oadp-full} virtual machine data protection (VMDP) backup storage locations. This helps you to configure S3-compatible or file system storage for your backup repository.

== S3-compatible storage

.S3 storage options
[cols="1,1,1",options="header"]
|===
|Option |Description |Default

|`--bucket`
|Name of the S3 bucket.
|(required)

|`--access-key`
|Access key ID.
|(required)

|`--secret-access-key`
|Secret access key.
|(required)

|`--endpoint`
|S3 endpoint URL.
|`s3.amazonaws.com`

|`--region`
|S3 region.
|Auto-detect

|`--prefix`
|Object prefix in the bucket.
|None

|`--session-token`
|Session token for temporary credentials.
|None

|`--disable-tls`
|Disable HTTPS.
|`false`

|`--disable-tls-verification`
|Skip TLS certificate verification.
|`false`

|`--root-ca-pem-path`
|Path to a custom CA certificate file.
|None

|`--root-ca-pem-base64`
|Base64-encoded CA certificate.
|None
|===

[NOTE]
====
VMDP automatically prepends `oadp-vmdp/` to your prefix.
====

== Filesystem storage

.Filesystem storage options
[cols="1,1,1",options="header"]
|===
|Option |Description |Default

|`--path`
|Absolute path to the storage directory.
|(required)

|`--owner-uid`
|User ID for new files.
|Current user

|`--owner-gid`
|Group ID for new files.
|Current group

|`--file-mode`
|Permission mode for files.
|`0600`

|`--dir-mode`
|Permission mode for directories.
|`0700`
|===

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-vmdp/oadp-vmdp.adoc

[id="oadp-vmdp-configuration_{context}"]
= {oadp-short} virtual machine data protection configuration

[role="_abstract"]
Review the environment variables and file locations for the {oadp-full} virtual machine data protection (VMDP) command-line interface (CLI). This helps you to configure credentials, logging, and behavioral settings.

== Environment variables

.Credential environment variables
[cols="1,1",options="header"]
|===
|Variable |Description

|`BSLS_PASSWORD`
|BSL encryption password. Set this variable to avoid interactive prompts.

|`AWS_ACCESS_KEY_ID`
|Access key for S3 storage

|`AWS_SECRET_ACCESS_KEY`
|Secret key for S3 storage

|`AWS_SESSION_TOKEN`
|Session token for temporary credentials
|===

.Configuration environment variables
[cols="1,1,1",options="header"]
|===
|Variable |Description |Default

|`OADP_CONFIG_PATH`
|Path to the configuration file
|`~/.config/oadp/repository.config`

|`OADP_CACHE_DIRECTORY`
|Path to the cache directory
|System-dependent

|`OADP_LOG_DIR`
|Directory for log files
|`~/.cache/oadp/`
|===

.Behavior environment variables
[cols="1,1,1",options="header"]
|===
|Variable |Description |Default

|`OADP_CHECK_FOR_UPDATES`
|Enable or disable update checks
|`true`

|`OADP_PERSIST_CREDENTIALS_ON_CONNECT`
|Save credentials after connecting
|`true`

|`OADP_USE_KEYRING`
|Use the system keyring for password storage
|`false`

|`OADP_BACKUP_FAIL_FAST`
|Fail immediately on the first error
|`false`
|===

.Logging environment variables
[cols="1,1,1",options="header"]
|===
|Variable |Description |Default

|`OADP_LOG_DIR_MAX_FILES`
|Maximum number of log files
|`1000`

|`OADP_LOG_DIR_MAX_AGE`
|Maximum age of log files
|`720h`

|`OADP_LOG_DIR_MAX_SIZE_MB`
|Maximum total size of log files in MB
|`1000`
|===

== File locations

.Default file locations
[cols="1,1,1",options="header"]
|===
|Type |Linux |Windows

|Configuration
|`~/.config/oadp/repository.config`
|`%APPDATA%\oadp\repository.config`

|Logs
|`~/.cache/oadp/`
|`%LOCALAPPDATA%\oadp\`
|===

== Kopia compatibility

VMDP is based on Kopia and uses the same repository format. Repositories are fully compatible between the two tools.

.Command mapping between VMDP and Kopia
[cols="1,1",options="header"]
|===
|VMDP command |Kopia equivalent

|`bsl`
|`repository`

|`backup`
|`snapshot`
|===

When you connect to a VMDP repository by using the Kopia CLI, include the `oadp-vmdp/` prefix that VMDP adds automatically. For example:

[source,terminal]
----
$ kopia repository connect s3 \
  --bucket <bucket_name> \
  --prefix oadp-vmdp/<your_prefix>/ \
  ...
----
