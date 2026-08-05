---
title: "The greenboot health check framework"
type: reference
domain: openshift
slug: microshift-install-get-ready-4-22-microshift-greenboot
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_get_ready/microshift-greenboot
version: 4.22
family: microshift_install_get_ready
documentKind: "Documentation"
---

# The greenboot health check framework

[id="microshift-greenboot"]
= The greenboot health check framework

[role="_abstract"]
Greenboot is the generic health check framework for the `systemd` service on `rpm-ostree` systems such as {op-system-ostree-first}. This framework is included in {microshift-short} installations with the `microshift-greenboot` and `greenboot-default-health-checks` RPM packages.

Greenboot health checks run at various times to assess system health and automate a rollback on `rpm-ostree` systems to the last healthy state in cases of software trouble, for example:

* Default health check scripts run each time the system starts.
* In addition the to the default health checks, you can write, install, and configure application health check scripts to also run every time the system starts.
* Greenboot can reduce your risk of being locked out of edge devices during updates and prevent a significant interruption of service if an update fails.
* When a failure is detected, the system boots into the last known working configuration by using the `rpm-ostree` rollback capability. This feature is especially useful automation for edge devices where direct serviceability is either limited or non-existent.

A {microshift-short} application health check script is included in the `microshift-greenboot` RPM. The `greenboot-default-health-checks` RPM includes health check scripts verifying that DNS and `ostree` services are accessible. You can create your own health check scripts for the workloads you are running. You can write one that verifies that an application has started, for example.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-dir-structure_{context}"]
= How greenboot uses directories to run scripts

[role="_abstract"]
Greenboot uses directory-based framework to execute health check scripts during the system boot process. By organizing your custom scripts into specific directories, you can define the boot validation workflow and determine whether the system successfully applies an update or initiates an automated rollback.

Health check scripts run from four `/etc/greenboot` directories. These scripts run in alphabetical order. Keep this in mind when you configure the scripts for your workloads.

When the system starts, greenboot runs the scripts in the `required.d` and `wanted.d` directories. Depending on the outcome of those scripts, greenboot continues the startup or attempts a rollback as follows:

. System as expected: When all of the scripts in the `required.d` directory are successfully run, greenboot runs any scripts present in the `/etc/greenboot/green.d` directory.

. System trouble: If any of the scripts in the `required.d` directory fail, greenboot runs any prerollback scripts present in the `red.d` directory, then restarts the system.

[NOTE]
====
Greenboot redirects script and health check output to the system log. When you are logged in, a daily message provides the overall system health output.
====

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-directories-details_{context}"]
= Greenboot directories details

[role="_abstract"]
You can control how greenboot handles errors by placing your health check scripts in specific directories. The directories determine which scripts are strictly required for a successful boot and which ones can fail without causing a rollback.

Returning a nonzero exit code from any script means that script has failed. Greenboot restarts the system a few times to retry the scripts before attempting to roll back to the previous version.

* `/etc/greenboot/check/required.d` contains the health checks that must not fail.

** If the scripts fail, greenboot retries them three times by default. You can configure the number of retries in the `/etc/greenboot/greenboot.conf` file by setting the `GREENBOOT_MAX_BOOTS` parameter to the desired number of retries.

** After all retries fail, greenboot automatically initiates a rollback if one is available. If a rollback is not available, the system log output shows that manual intervention is required.

** The `40_microshift_running_check.sh` health check script for {microshift-short} is installed into this directory.

* `/etc/greenboot/check/wanted.d` contains health scripts that are allowed to fail without causing the system to be rolled back.

** If any of these scripts fail, greenboot logs the failure but does not initiate a rollback.

* `/etc/greenboot/green.d` contains scripts that run after greenboot has declared the start successful.

* `/etc/greenboot/red.d` contains scripts that run after greenboot has declared the startup as failed, including the `40_microshift_pre_rollback.sh` prerollback script. This script is executed right before a system rollback. The script performs {microshift-short} pod and OVN-Kubernetes cleanup to avoid potential conflicts after the system is rolled back to a previous version.

[IMPORTANT]
====
If you customize the values of any environment variable in the `/etc/greenboot/greenboot.conf` file, these changes can be lost when the greenboot RPM package is updated or downgraded.

* To retain customizations when building system images with {microshift-short}, add the `greenboot.conf` file to a blueprint.
* To retain customizations when using an RPM installation, apply changes to the `greenboot.conf` file after you install {microshift-short} and greenboot RPMs.
====

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-included-health-checks_{context}"]
= Included greenboot health checks

[role="_abstract"]
By default, {op-system-ostree-first} includes a set of built-in greenboot health checks designed to verify functions, such as network connectivity to update repositories and hardware watchdog status. Health check scripts are available in `/usr/lib/greenboot/check`, a read-only directory in {op-system-ostree-first} {op-system-image} systems.

The following health checks are included with the `greenboot-default-health-checks` framework.

* Check if repository URLs are still DNS solvable:
+
This script is under `/usr/lib/greenboot/check/required.d/01_repository_dns_check.sh` and ensures that DNS queries to repository URLs are still available.

* Check if update platforms are still reachable:
+
This script is under `/usr/lib/greenboot/check/wanted.d/01_update_platform_check.sh` and tries to connect and get a 2XX or 3XX HTTP code from the update platforms defined in `/etc/ostree/remotes.d`.

* Check if the current boot has been triggered by the hardware watchdog:
+
This script is under `/usr/lib/greenboot/check/required.d/02_watchdog.sh` and checks whether the current boot has been watchdog-triggered or not.

** If the watchdog-triggered reboot occurs within the grace period, the current boot is marked as red. Greenboot does not trigger a rollback to the previous deployment.
** If the watchdog-triggered reboot occurs after the grace period, the current boot is not marked as red. Greenboot does not trigger a rollback to the previous deployment.
** A 24-hour grace period is enabled by default. This grace period can be either disabled by modifying `GREENBOOT_WATCHDOG_CHECK_ENABLED` in `/etc/greenboot/greenboot.conf to false`, or configured by changing the `GREENBOOT_WATCHDOG_GRACE_PERIOD=number_of_hours` variable value in `/etc/greenboot/greenboot.conf`.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-health-script_{context}"]
= The {microshift-short} health check script

[role="_abstract"]
The `40_microshift_running_check.sh` health check script only performs validation of core {microshift-short} services. Install your customized workload health check scripts in the greenboot directories to ensure successful application operations after system updates. Scripts run in alphabetical order.

{microshift-short} health checks are listed in the following table:

.Validation statuses and outcome for {microshift-short}

[cols="3", options="header"]
|===
|Validation
|Pass
|Fail

|Check that the script runs with `root` permissions
|Next
|`exit 0`

|Check that the `microshift.service` is enabled
|Next
|`exit 0`

|Wait for the `microshift.service` to be active (!failed)
|Next
|`exit 1`

|For each core namespace, wait for readiness of the workload
|Next
|`exit 1`
|===

[id="validation-wait-period_{context}"]
== Validation wait period

The wait period in each validation is 10 minutes by default. After the wait period, if the validation has not succeeded, it is declared a failure. This wait period is incrementally increased by the base wait period after each boot in the verification loop.

* You can override the base-time wait period by setting the `MICROSHIFT_WAIT_TIMEOUT_SEC` environment variable in the `/etc/greenboot/greenboot.conf` configuration file. For example, you can change the wait time to 5 minutes by resetting the value to 300 seconds, such as `MICROSHIFT_WAIT_TIMEOUT_SEC=300`.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-systemd-journal-data_{context}"]
= Enabling systemd journal service data persistency

[role="_abstract"]
The default configuration of the `systemd` journal service stores the data in the volatile `/run/log/journal` directory. To view system logs across system starts and restarts, you must enable log persistence and set limits on the maximal journal data size.

.Procedure

. Make the directory by running the following command:
+
[source,terminal]
----
$ sudo mkdir -p /etc/systemd/journald.conf.d
----

. Create the configuration file by running the following command:
+
[source,terminal]
----
cat <<EOF | sudo tee /etc/systemd/journald.conf.d/microshift.conf &>/dev/null
[Journal]
Storage=persistent
SystemMaxUse=1G
RuntimeMaxUse=1G
EOF
----

. Edit the configuration file values for your size requirements.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-updates-workloads_{context}"]
= Updates and third-party workloads

[role="_abstract"]
After the update, you can examine the output of greenboot health checks and determine whether the update was declared valid. This health check can help you determine if the system is working properly.

Health check scripts for updates are installed into the `/etc/greenboot/check/required.d` directory and are automatically executed during each system start. Exiting scripts with a nonzero status means the system start is declared as failed.

[IMPORTANT]
====
Wait until after an update is declared valid before starting third-party workloads. If a rollback is performed after workloads start, you can lose data. Some third-party workloads create or update data on a device before an update is complete. Upon rollback, the file system reverts to its state before the update.
====

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-workloads-validation_{context}"]
= Checking the results of an update

[role="_abstract"]
You can view the overall status of system health checks after an update in the system log. After a successful start, greenboot sets the variable `boot_success=` to `1` in GRUB.

.Procedure

* To access the overall status of system health checks, run the following command:
+
[source,terminal]
----
$ sudo grub2-editenv - list | grep ^boot_success
----
+
.Example output for a successful system start
[source,terminal]
----
boot_success=1
----
** If your command returns `boot_success=0`, either the greenboot health check is still running, or the update is a failure.

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-access-health-check_{context}"]
= Accessing health check output in the system log

[role="_abstract"]
If the system update fails or the boot process stops, you can query the system logs for detailed troubleshooting information. These logs provide the detailed steps necessary to troubleshoot failed boot checks.

.Procedure

* To access the results of a health check, run the following command:
+
[source,terminal]
----
$ sudo journalctl -o cat -u greenboot-healthcheck.service
----
+
.Example output of a failed health check
[source,terminal]
----
...
...
Running Required Health Check Scripts...
STARTED
GRUB boot variables:
boot_success=0
boot_indeterminate=0
boot_counter=2
...
...
Waiting 600s for MicroShift service to be active and not failed
FAILURE
...
...
----

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="microshift-greenboot-access-prerollback-check_{context}"]
= Accessing prerollback health check output in the system log

[role="_abstract"]
When a system update fails and greenboot triggers a rollback, it executes prerollback scripts to clean up services and prevent data conflicts. Using the output of the health check scripts, you can verify that the cleanup tasks are completed successfully before the system reboots into the previous deployment.

For example, check the results of a pre-rollback script using the following procedure.

.Procedure

* To access the results of a prerollback script, run the following command:
+
[source,terminal]
----
$ sudo journalctl -o cat -u redboot-task-runner.service
----
+
.Example output of a prerollback script
[source,terminal]
----
...
...
Running Red Scripts...
STARTED
GRUB boot variables:
boot_success=0
boot_indeterminate=0
boot_counter=0
The ostree status:
* rhel c0baa75d9b585f3dd989a9cf05f647eb7ca27ee0dbd4b94fe8c93ed3a4b9e4a5.0
    Version: 9.8
    origin: <unknown origin type>
  rhel 6869c1347b0e0ba1bbf0be750cdf32da5138a1fcbc5a4c6325ab9eb647b64663.0 (rollback)
    Version: 9.8
    origin refspec: edge:rhel/9/x86_64/edge
System rollback imminent - preparing MicroShift for a clean start
Stopping MicroShift services
Removing MicroShift pods
Killing conmon, pause and OVN processes
Removing OVN configuration
Finished greenboot Failure Scripts Runner.
Cleanup succeeded
Script '40_microshift_pre_rollback.sh' SUCCESS
FINISHED
redboot-task-runner.service: Deactivated successfully.
----
+
[NOTE]
====
In case of a rollback, the pre-rollback script runs the `sudo microshift-cleanup-data --ovn` command to prepare the system for a potential software downgrade.
====

// Module included in the following assemblies:
//
// * microshift_install_get_ready/microshift-greenboot.adoc

[id="greenboot-check-updates_{context}"]
= Checking updates with a health check script

[role="_abstract"]
To verify the success or failure of a recent system update, you can review the output of greenboot health check scripts in the system log after an update.

.Procedure

* To access the result of update checks, run the following command:
+
[source,terminal]
----
$ sudo grub2-editenv - list | grep ^boot_success
----
+
.Example output for a successful update
[source,terminal]
----
boot_success=1
----
+
** If your command returns `boot_success=0`, either the greenboot health check is still running, or the update is a failure.

[id="additional-resources_microshift-greenboot_{context}"]
[role="_additional-resources"]
== Additional resources

* Auto applying manifests

* Greenboot workload health checks
