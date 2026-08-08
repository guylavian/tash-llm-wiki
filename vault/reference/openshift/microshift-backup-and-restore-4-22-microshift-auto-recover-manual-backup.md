---
title: "Automated recovery from manual backups"
type: reference
domain: openshift
slug: microshift-backup-and-restore-4-22-microshift-auto-recover-manual-backup
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_backup_and_restore/microshift-auto-recover-manual-backup
version: 4.22
family: microshift_backup_and_restore
documentKind: "Documentation"
---

# Automated recovery from manual backups

[id="microshift-auto-recover-manual-backup"]
= Automated recovery from manual backups

[role="_abstract"]
To automatically restore OpenShift Container Platform when it fails to start, you can configure automatic recovery from manual backups. Create backups in a single directory and configure restore to use the latest backup on failure.

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-auto-recovery-manual-backups_{context}"]
= Modifying backup and restore commands to automate data recovery

[role="_abstract"]
The `--auto-recovery` option stores OpenShift Container Platform backups in one directory and selects the latest backup when you restore. You add the option to your `backup` and `restore` commands for automatic recovery.

The `--auto-recovery` option treats the `PATH` argument as a path to a directory that holds all the backups for automated recovery, and not just as a path to a particular backup file. You can use the `--auto-recovery` option with both `backup` and `restore` commands.

* For example, if you use the automatic recovery option with `restore`, such as in `microshift restore --auto-recovery PATH`, running the modified command automatically selects and restores the most recent backup.

* If you use the same option in the `microshift backup` command, such as in `microshift backup --auto-recovery PATH`, a new backup is created in the PATH.

* By default, `microshift restore --auto-recovery PATH` creates a backup of the failed {microshift-short} data in `PATH/failed`. You can add the `--dont-save-failed` option to disable the creation of failed backup data.

[IMPORTANT]
====
You can only use the `--dont-save-failed` option with the `restore` command.
====

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-creating-backups-auto-recovery_{context}"]
= Creating backups using the auto-recovery feature

[role="_abstract"]
To create backups for OpenShift Container Platform automatic recovery, you can run `microshift backup --auto-recovery` with a directory path. The command then stores each backup in that directory so that the latest is available when you restore.

[NOTE]
====
Creating backups requires stopping {microshift-short}. You must decide on the best time to stop {microshift-short}.
====

.Prerequisites

* You stopped {microshift-short}.

.Procedure

* Create and store backups in the directory you choose by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift backup --auto-recovery _<path_of_directory>_
----
+
** For `_<path_of_directory>_`, specify the path of the directory that stores backups. For example, `/var/lib/microshift-auto-recovery`.
+
[NOTE]
====
The `--auto-recovery` option modifies the interpretation of the `PATH` argument from the final backup path to a directory that holds all of the backups for automated recovery.
====
+
.Example output
[source,terminal]
----
??? I1104 09:18:52.100725    8906 system.go:58] "OSTree deployments" deployments=[{"id":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1","booted":true,"staged":false,"pinned":false},{"id":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","booted":false,"staged":false,"pinned":false}]
??? I1104 09:18:52.100895    8906 data_manager.go:83] "Copying data to backup directory" storage="/var/lib/microshift-auto-recovery" name="20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1" data="/var/lib/microshift"
??? I1104 09:18:52.102296    8906 disk_space.go:33] Calculated size of "/var/lib/microshift": 261M - increasing by 10% for safety: 287M
??? I1104 09:18:52.102321    8906 disk_space.go:44] Calculated available disk space for "/var/lib/microshift-auto-recovery": 1658M
??? I1104 09:18:52.105700    8906 atomic_dir_copy.go:66] "Made an intermediate copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift /var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1.tmp.99142"
??? I1104 09:18:52.105732    8906 atomic_dir_copy.go:115] "Renamed to final destination" src="/var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1.tmp.99142" dest="/var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"
??? I1104 09:18:52.105749    8906 data_manager.go:120] "Copied data to backup directory" backup="/var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1" data="/var/lib/microshift"
/var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1
----

.Verification

* Verify that the backup you created exists in your customized storage directory by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo ls -la _<path_of_directory>_
----
+
** For `_<path_of_directory>_`, specify the path of the directory that stores backups. For example, `/var/lib/microshift-auto-recovery`.

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-restoring-backups-auto-recovery_{context}"]
= Restoring backups using the auto-recovery feature

[role="_abstract"]
To recover OpenShift Container Platform data after loss or damage, you can run the `microshift restore --auto-recovery` command with your backups directory, which restores the latest backup.
Previously restored backups that used automatic recovery are moved to your `PATH/restored` directory.

.Prerequisites

* You have stopped {microshift-short}.

.Procedure

. Restore the latest backup from your backups directory by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo microshift restore --auto-recovery _<path_of_directory>_
----
+
** For `_<path_of_directory>_`, specify the path of the directory that stores backups. For example, `/var/lib/microshift-auto-recovery`.
+
[NOTE]
====
* The `--auto-recovery` option copies the {microshift-short} data to `/var/lib/microshift-auto-recovery/failed/` for later investigation, selects the most recent backup, and restores it.

* The `--dont-save-failed` option disables the backing up of failed {microshift-short} data.
====
+
.Example output
[source,terminal]
----
??? I1104 09:19:28.617225    8950 state.go:80] "Read state from the disk" state={"LastBackup":"20241022101528_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"}
??? I1104 09:19:28.617323    8950 storage.go:78] "Auto-recovery backup storage read and parsed" dirs=["20241022101255_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","20241022101520_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","20241022101528_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1","restored"] backups=[{"CreationTime":"2024-10-22T10:12:55Z","Version":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"},{"CreationTime":"2024-10-22T10:15:20Z","Version":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"},{"CreationTime":"2024-10-22T10:15:28Z","Version":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"},{"CreationTime":"2024-11-04T09:18:52Z","Version":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"}]
??? I1104 09:19:28.617350    8950 storage.go:40] "Filtered list of backups - removed previously restored backup" removed="20241022101528_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0" newList=[{"CreationTime":"2024-10-22T10:12:55Z","Version":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"},{"CreationTime":"2024-10-22T10:15:20Z","Version":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"},{"CreationTime":"2024-11-04T09:18:52Z","Version":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"}]
??? I1104 09:19:28.633237    8950 system.go:58] "OSTree deployments" deployments=[{"id":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1","booted":true,"staged":false,"pinned":false},{"id":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","booted":false,"staged":false,"pinned":false}]
??? I1104 09:19:28.633258    8950 storage.go:49] "Filtered list of backups by version" version="default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1" newList=[{"CreationTime":"2024-11-04T09:18:52Z","Version":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"}]
??? I1104 09:19:28.633268    8950 restore.go:170] "Potential backups" bz=[{"CreationTime":"2024-11-04T09:18:52Z","Version":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"}]
??? I1104 09:19:28.633277    8950 restore.go:173] "Candidate backup for restore" b={"CreationTime":"2024-11-04T09:18:52Z","Version":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"}
??? I1104 09:19:28.634007    8950 disk_space.go:33] Calculated size of "/var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1": 261M - increasing by 10% for safety: 287M
??? I1104 09:19:28.634096    8950 disk_space.go:44] Calculated available disk space for "/var/lib": 1658M
??? I1104 09:19:28.634507    8950 disk_space.go:33] Calculated size of "/var/lib/microshift": 261M - increasing by 10% for safety: 287M
??? I1104 09:19:28.634522    8950 disk_space.go:44] Calculated available disk space for "/var/lib/microshift-auto-recovery": 1658M
??? I1104 09:19:28.649719    8950 system.go:58] "OSTree deployments" deployments=[{"id":"default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1","booted":true,"staged":false,"pinned":false},{"id":"default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0","booted":false,"staged":false,"pinned":false}]
??? I1104 09:19:28.653880    8950 atomic_dir_copy.go:66] "Made an intermediate copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift /var/lib/microshift-auto-recovery/failed/20241104091928_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1.tmp.22742"
??? I1104 09:19:28.657362    8950 atomic_dir_copy.go:66] "Made an intermediate copy" cmd="/bin/cp --verbose --recursive --preserve --reflink=auto /var/lib/microshift-auto-recovery/20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1 /var/lib/microshift.tmp.482"
??? I1104 09:19:28.657385    8950 state.go:40] "Saving intermediate state" state="{\"LastBackup\":\"20241104091852_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1\"}" path="/var/lib/microshift-auto-recovery/state.json.tmp.41544"
??? I1104 09:19:28.662438    8950 atomic_dir_copy.go:115] "Renamed to final destination" src="/var/lib/microshift.tmp.482" dest="/var/lib/microshift"
??? I1104 09:19:28.662451    8950 state.go:46] "Moving state file to final path" intermediatePath="/var/lib/microshift-auto-recovery/state.json.tmp.41544" finalPath="/var/lib/microshift-auto-recovery/state.json"
??? I1104 09:19:28.662521    8950 atomic_dir_copy.go:115] "Renamed to final destination" src="/var/lib/microshift-auto-recovery/failed/20241104091928_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1.tmp.22742" dest="/var/lib/microshift-auto-recovery/failed/20241104091928_default-b3442053c9ce69310cd54140d8d592234c5306e4c5132de6efe615f79c84300a.1"
??? I1104 09:19:28.662969    8950 atomic_dir_copy.go:115] "Renamed to final destination" src="/var/lib/microshift-auto-recovery/20241022101528_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0" dest="/var/lib/microshift-auto-recovery/restored/20241022101528_default-a129624b9233fa54fe3574f1aa211bc2d85e1052b52245fe7d83f10c2f6d28e3.0"
??? I1104 09:19:28.662983    8950 restore.go:141] "Auto-recovery restore completed".
----
+
[IMPORTANT]
====
* The `restore` command does not restart {microshift-short} after restoration. When you execute this command, {microshift-short} service has already failed or you stopped it.

* {microshift-short} does not monitor the disk space of any filesystem. You must ensure that your automation handles old backup removal. For example, you can add this process to the auto-recovery service or add another service that runs periodically.
====

. Restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

* Verify that {microshift-short} has started successfully by running the following command:
+
--
--

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-auto-recovery-rpm-systems_{context}"]
= Using automatic recovery in RPM systems

[role="_abstract"]
To use automatic recovery for OpenShift Container Platform on RPM systems, you can create the `10-auto-recovery.conf` file, the `microshift-auto-recovery.service` unit, and the `microshift-auto-recovery` script. Systemd runs the recovery service when the OpenShift Container Platform service does not start, and the script restores the latest backup.

As a use case, consider the following example situation in which you want to automate the automatic recovery process for RPM systems that use the systemd service.

.Procedure

. Create a directory for the `microshift` systemd service by running the following command:
+
[source,terminal]
----
$ sudo mkdir -p /usr/lib/systemd/system/microshift.service.d
----

. To instruct `systemd` to run `microshift-auto-recovery.service` when the `microshift.service` fails, create the `10-auto-recovery.conf` file by running the following command:
+
[source,terminal]
----
$ sudo tee /usr/lib/systemd/system/microshift.service.d/10-auto-recovery.conf > /dev/null <<'EOF'
[Unit]
OnFailure=microshift-auto-recovery.service
StartLimitIntervalSec=25s

[Service]
RestartMode=direct
EOF
----
+
** For `StartLimitIntervalSec`, specify a value greater than the default `10s` for slower systems. A value that is too low can result in systemd never marking the `microshift` systemd service as failed, which means that the `OnFailure=` service does not get triggered.

** `RestartMode=direct` prevents systemd from entering failed state on every restart attempt. This ensures `OnFailure` is triggered only after `StartLimitBurst` is exceeded, not on each failure. In systemd v254 (RHEL-10), `OnFailure` behavior changed to trigger on every failure instead of only when restart limits are reached. `RestartMode=direct` restores the v249 behavior. This setting is ignored on RHEL-9.6 (systemd v252) where it does not exist.

. Create the `microshift-auto-recovery.service` file by running the following command:
+
[source,terminal]
----
$ sudo tee /usr/lib/systemd/system/microshift-auto-recovery.service > /dev/null <<'EOF'
[Unit]
Description=MicroShift auto-recovery

[Service]
Type=oneshot
ExecStart=/usr/bin/microshift-auto-recovery

[Install]
WantedBy=multi-user.target
EOF
----

. Create the `microshift-auto-recovery` script by running the following command:
+
[source,terminal]
----
$ sudo tee /usr/bin/microshift-auto-recovery > /dev/null <<'EOF'
#!/usr/bin/env bash
set -xeuo pipefail

# If greenboot uses a non-default file for clearing boot_counter, use boot_success instead.
if grep -q  "/boot/grubenv" /usr/libexec/greenboot/greenboot-grub2-set-success; then
    if grub2-editenv - list | grep -q ^boot_success=0; then
        echo "Greenboot didn't decide the system is healthy after staging new deployment."
        echo "Quitting to not interfere with the process"
        exit 0
    fi
else
    if grub2-editenv - list | grep -q ^boot_counter=; then
        echo "Greenboot didn't decide the system is healthy after staging a new deployment."
        echo "Quitting to not interfere with the process"
        exit 0
    fi
fi

/usr/bin/microshift restore --auto-recovery /var/lib/microshift-auto-recovery
/usr/bin/systemctl reset-failed microshift
/usr/bin/systemctl start microshift

echo "DONE"
EOF
----

. Make the script executable by running the following command:
+
[source,terminal]
----
$ sudo chmod +x /usr/bin/microshift-auto-recovery
----

. Reload the system configuration by running the following command:
+
[source,terminal]
----
$ sudo systemctl daemon-reload
----

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-auto-recovery-ostree-systems_{context}"]
= Using automatic recovery with {op-system-ostree}

[role="_abstract"]
To use automatic recovery for OpenShift Container Platform on {op-system-ostree} systems, you can add the auto-recovery systemd service, `10-auto-recovery.conf`, and the `microshift-auto-recovery` script to your blueprint. Use blueprint customizations so the image includes these files and recovery runs automatically.

[IMPORTANT]
====
You must include the entire `auto-recovery` process for {op-system-ostree} systems that use `systemd` in the blueprint file.
====

.Prerequisites

* You installed Podman.
* You installed the command-line `composer-cli` tool.

.Procedure

. Optional: Because the `composer-cli` can only create files in the `/etc` directory, package your files into an RPM that you include the blueprint.

. Use the following example to create your blueprint file:
+
[source,terminal]
----
[[customizations.directories]]
path = "/etc/systemd/system/microshift.service.d"

[[customizations.directories]]
path = "/etc/bin"

[[customizations.files]]
path = "/etc/systemd/system/microshift.service.d/10-auto-recovery.conf"
data = """
[Unit]
OnFailure=microshift-auto-recovery.service
"""

[[customizations.files]]
path = "/etc/systemd/system/microshift-auto-recovery.service"
data = """
[Unit]
Description=MicroShift auto-recovery
[Service]
Type=oneshot
ExecStart=/etc/bin/microshift-auto-recovery
[Install]
WantedBy=multi-user.target
"""

[[customizations.files]]
path = "/etc/bin/microshift-auto-recovery"
mode = "0755"
data = """
#!/usr/bin/env bash
set -xeuo pipefail
# If greenboot uses a non-default file for clearing boot_counter, use boot_success instead.
if grep -q  "/boot/grubenv" /usr/libexec/greenboot/greenboot-grub2-set-success; then
    if grub2-editenv - list | grep -q ^boot_success=0; then
        echo "Greenboot didn't decide the system is healthy after staging a new deployment."
        echo "Quitting to not interfere with the process"
        exit 0
    fi
else
    if grub2-editenv - list | grep -q ^boot_counter=; then
        echo "Greenboot didn't decide the system is healthy after staging a new deployment."
        echo "Quitting to not interfere with the process"
        exit 0
    fi
fi
/usr/bin/microshift restore --auto-recovery /var/lib/microshift-auto-recovery
/usr/bin/systemctl reset-failed microshift
/usr/bin/systemctl start microshift
echo "DONE"
"""
----

. For the next steps, see Preparing for image building.

// Module included in the following assemblies:
//
// * microshift/microshift_backup_and_restore/microshift-auto-recover-manual-backup.adoc

[id="microshift-auto-recovery-example-bootc-systems_{context}"]
= Using automatic recovery in image mode for {op-system-base} systems

[role="_abstract"]
To use automatic recovery for OpenShift Container Platform on {op-system-base} image-based systems, you can embed the `10-auto-recovery.conf` and `microshift-auto-recovery.service` files in your Containerfile and rebuild the bootc image.

[IMPORTANT]
====
You must include the entire `auto-recovery` process for {op-system-image} systems that use `systemd` in the container file.
====

.Prerequisites

* You created a Containerfile as instructed in Building the bootc image.

* You created the `10-auto-recovery.conf` and `microshift-auto-recovery.service` files as explained in the "Using auto-recovery in RPM systems" section.
+
[IMPORTANT]
====
The location of the `10-auto-recovery.conf` and `microshift-auto-recovery.service` files must be relative to the Containerfile.

For example, if the path to the Containerfile is `/home/microshift/my-build/Containerfile`, the systemd files need to be adjacent for proper embedding. The following paths are correct for this example:

* `/home/microshift/my-build/auto-rec/10-auto-recovery.conf`
* `/home/microshift/my-build/auto-rec/microshift-auto-recovery.service`
* `/home/microshift/my-build/auto-rec/microshift-auto-recovery`
====

* You created the `microshift-auto-recovery` script as explained in the "Using auto-recovery in RPM systems" section.

.Procedure

. Use the following example snippet to update the container file that you use to prepare the {op-system-image} image.
+
[source,text]
----
RUN mkdir -p /usr/lib/systemd/system/microshift.service.d
COPY ./auto-rec/10-auto-recovery.conf /usr/lib/systemd/system/microshift.service.d/10-auto-recovery.conf
COPY ./auto-rec/microshift-auto-recovery.service /usr/lib/systemd/system/
COPY ./auto-rec/microshift-auto-recovery /usr/bin/
RUN chmod +x /usr/bin/microshift-auto-recovery
----
+
[IMPORTANT]
====
Podman uses the host subscription information and repositories inside the container when building the container image. If the `rhocp` and `fast-datapath` repositories are not available on the host, the build fails.
====

. Rebuild your local bootc image by running the following image build command:
+
[source,terminal]
----
PULL_SECRET=~/.pull-secret.json
USER_PASSWD=<your_redhat_user_password>
IMAGE_NAME=microshift-4.18-bootc

sudo podman build --authfile "${PULL_SECRET}" -t "${IMAGE_NAME}" \
    --build-arg USER_PASSWD="${USER_PASSWD}" \
    -f Containerfile
----
+
[NOTE]
====
Secrets are used during the image build in the following ways:

* The podman `--authfile` argument is required to pull the base `rhel-bootc:9.4` image from the `registry.redhat.io` registry.

* The build `USER_PASSWD` argument is used to set a password for the `redhat user`.
====

.Verification

* Verify that the local bootc image was created by running the following command:
+
[source,terminal]
----
$ sudo podman images "${IMAGE_NAME}"
----
+
.Example output
[source,text]
----
REPOSITORY                       TAG         IMAGE ID      CREATED        SIZE
localhost/microshift-4.18-bootc  latest      193425283c00  2 minutes ago  2.31 GB
----
