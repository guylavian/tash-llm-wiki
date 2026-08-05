---
title: "Using greenboot for application and workload health checks"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-greenboot-workload-health-checks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-greenboot-workload-health-checks
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using greenboot for application and workload health checks

[id="microshift-greenboot-workload-health-checks"]
= Using greenboot for application and workload health checks

[role="_abstract"]
You can use greenboot health checks on {microshift-short} to assess the health of your workloads and applications.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-how-workload-health-checks-work_{context}"]
= How workload health checks work

[role="_abstract"]
You can use greenboot health checks to assess the health of your workloads and applications. You can also write your own health check scripts for your applications. Greenboot health checks are helpful on edge devices where direct serviceability is either limited or non-existent.

These additional health checks are useful for software problem detection and automatic system rollbacks.

Workload or application health checks can use the {microshift-short} basic health check functions already implemented for the {microshift-short} core services. Creating your own comprehensive scripts for your applications is recommended. For example, you can write one that verifies that a service has started.

You can also use the `microshift healthcheck` command, which can run checks that the basic functions of the workload are operating as expected.

[IMPORTANT]
====
The following functions related to checking workload health in `/usr/share/microshift/functions/greenboot.sh` are deprecated and planned for removal in a future release:

* `wait_for`
* `namespace_images_downloaded`
* `namespace_deployment_ready`
* `namespace_daemonset_ready`
* `namespace_pods_ready`
* `namespace_pods_not_restarting`
* `print_failure_logs`
* `log_failure_cmd`
* `log_script_exit`
* `lvmsDriverShouldExist`
* `csiComponentShouldBeDeploy`
====

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-microshift-health-check-command_{context}"]
= How to use the {microshift-short} health check command

[role="_abstract"]
The `microshift healthcheck` command checks whether a workload of the provided type exists and verifies its
status for the specified timeout duration. The number of ready replicas, that is, pods, must match the expected amount.

To run the `microshift healthcheck` command successfully, use the following prerequisites:

* Execute commands from a root user account.
* Enable the {microshift-short} service.

You can add the following actions to the `microshift healthcheck` command:

* `-v=2` to increase verbosity of the output
* `--timeout="${WAIT_TIMEOUT_SECS}s"` to override default 600s timeout value
* `--namespace `_<namespace>_` to specify the namespace of the workloads
* `--deployments `_<application-deployment>_` to check the readiness of a specific deployment
+
.Example command
[source,terminal]
----
$ sudo microshift healthcheck -v=2 --timeout="300s" --namespace busybox --deployments busybox-deployment
----
+
.Example output
[source,text]
----
??? I0410 08:54:03.766578    5898 service.go:29] microshift.service is enabled
??? I0410 08:54:03.766699    5898 service.go:31] Waiting 5m0s for microshift.service to be ready
??? I0410 08:54:03.768794    5898 service.go:38] microshift.service is ready
??? I0410 08:54:03.770585    5898 utils.go:34] Waiting for 1 goroutines
??? I0410 08:54:03.770955    5898 workloads.go:94] Waiting 5m0s for deployment/busybox-deployment in busybox
??? I0410 08:54:03.777830    5898 workloads.go:132] Deployment/busybox-deployment in busybox is ready
??? I0410 08:54:03.777858    5898 healthcheck.go:75] Workloads are ready
----

The `microshift healthcheck` command also accepts the following additional parameters to specify other kinds
of workloads:

* `--daemonsets`
* `--statefulsets`
* These options take a comma-delimited list of resources, for example, `--daemonsets ovnkube-master,ovnkube-node`.

Alternatively, a `--custom` option can be used with a `JSON` string, for example:

[source,terminal]
----
$ sudo microshift healthcheck --custom '{"openshift-storage":{"deployments":
    ["lvms-operator"], "daemonsets": ["vg-manager"]}, "openshift-ovn-kubernetes":
    {"daemonsets": ["ovnkube-master", "ovnkube-node"]}}'
----

.Example output
[source,text]
----
??? I0410 08:54:25.291059    5979 service.go:29] microshift.service is enabled
??? I0410 08:54:25.291167    5979 service.go:31] Waiting 5m0s for microshift.service to be ready
??? I0410 08:54:25.293188    5979 service.go:38] microshift.service is ready
??? I0410 08:54:25.294331    5979 workloads.go:58] Waiting 5m0s for daemonset/ovnkube-node in openshift-ovn-kubernetes
??? I0410 08:54:25.294351    5979 workloads.go:58] Waiting 5m0s for daemonset/ovnkube-master in openshift-ovn-kubernetes
??? I0410 08:54:25.294331    5979 workloads.go:58] Waiting 5m0s for daemonset/vg-manager in openshift-storage
??? I0410 08:54:25.294341    5979 workloads.go:94] Waiting 5m0s for deployment/lvms-operator in openshift-storage
??? I0410 08:54:25.309739    5979 workloads.go:89] Daemonset/ovnkube-node in openshift-ovn-kubernetes is ready
??? I0410 08:54:25.310213    5979 workloads.go:89] Daemonset/vg-manager in openshift-storage is ready
??? I0410 08:54:25.310731    5979 workloads.go:132] Deployment/lvms-operator in openshift-storage is ready
??? I0410 08:54:25.311017    5979 workloads.go:89] Daemonset/ovnkube-master in openshift-ovn-kubernetes is ready
??? I0410 08:54:25.311189    5979 healthcheck.go:52] Workloads are ready
----

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-app-health-check-script_{context}"]
= How to create a health check script for your application

[role="_abstract"]
You can create workload or application health check scripts in the text editor of your choice. Save the scripts in the `/etc/greenboot/check/required.d` directory.

When a script in the `/etc/greenboot/check/required.d` directory exits with an error, greenboot triggers a reboot in an attempt to heal the system.

[NOTE]
====
Any script in the `/etc/greenboot/check/required.d` directory triggers a reboot if it exits with an error.
====

If your health check logic requires any post-check steps, you can also create additional scripts and save them in the relevant greenboot directories. For example:

* You can also place shell scripts you want to run after a boot has been declared successful in `/etc/greenboot/green.d`.
* You can place shell scripts you want to run after a boot has been declared failed in `/etc/greenboot/red.d`. For example, if you have steps to heal the system before restarting, you can create scripts for your use case and place them in the `/etc/greenboot/red.d` directory.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-workload-health-check-script-ex_{context}"]
= Workload max duration or timeout script example

[role="_abstract"]
You can use the {microshift-short} core services health check script as a template to write your own health check scripts for your applications.

[id="microshift-greenboot-app-health-check-basic-prereqs_{context}"]
== Basic prerequisites for creating a health check script

* The workload must be installed.
* You must have root access.

[id="microshift-greenboot-app-health-check-ex_{context}"]
== Example and functional requirements

You can start with the following example health check script. Add to it for your use case. In your custom workload health check script, you must define the relevant namespace, deployment, `daemonset`, and `statefulset`.

[IMPORTANT]
====
Choose a name prefix for your application that ensures it runs after the `40_microshift_running_check.sh` script, which implements the {microshift-short} health check procedure for its core services.
====

.Example greenboot health check script
[source, bash]
----
#!/bin/bash
set -e

SCRIPT_NAME=$(basename $0)

# Load the workload health check functions library
source /usr/share/microshift/functions/greenboot.sh

# Stop the script if the user running it is not 'root'
if [ $(id -u) -ne 0 ] ; then
    echo "The '${SCRIPT_NAME}' script must be run with the 'root' user privileges"
    exit 1
fi

echo "STARTED"

# Set the wait timeout for the current check based on the boot counter
WAIT_TIMEOUT_SECS=$(get_wait_timeout)

/usr/bin/microshift healthcheck -v=2 --timeout="${WAIT_TIMEOUT_SECS}s" --namespace busybox --deployments busybox-deployment
----

[IMPORTANT]
====
Functions related to checking workload health previously included in the `/usr/share/microshift/functions/greenboot.sh` script file are deprecated. You can write a custom script, or use the `microshift healthcheck` command with various options instead. See "How workload health check scripts work" for more information.
====

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-health-checks.adoc

[id="microshift-greenboot-test-workload-health-check-script_{context}"]
= Testing a workload health check script

[role="_abstract"]
You can look at the output of the greenboot workload health check script to see how it works. While the output varies with the host system type, the example outputs for {op-system-base-full} system types are included for reference only.

.Prerequisites

* You have root access.
* You installed a workload.
* You created a health check script for the workload.
* The {microshift-short} service is enabled.

.Procedure

. To test that greenboot is running a health check script file, reboot the host by running the following command:
+
[source,terminal]
----
$ sudo reboot
----

. Examine the output of greenboot health checks by running the following command:
+
[source,terminal]
----
$ sudo journalctl -o cat -u greenboot-healthcheck.service
----
+
[NOTE]
====
{microshift-short} core service health checks run before the workload health checks.
====
+
.Example output for an {op-system-image} system
[source,terminal]
----
Starting greenboot Health Checks Runner...
Running Required Health Check Scripts...
Script '00_required_scripts_start.sh' SUCCESS
Running Wanted Health Check Scripts...
Script '00_wanted_scripts_start.sh' SUCCESS
Running Required Health Check Scripts...
--------------------
DEPRECATION NOTICE:
/usr/share/microshift/functions/greenboot.sh is now deprecated and will be removed in future release.
As a replacement consider using 'microshift healthcheck' command
--------------------
STARTED
GRUB boot variables:
boot_success=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_GREENBOOT_FAIL_MARKER=/run/microshift-greenboot-healthcheck-failed
System installation type:
bootc
System installation status:
bootcHost
??? I0403 11:54:30.526488     979 service.go:29] microshift.service is enabled
??? I0403 11:54:30.527145     979 service.go:31] Waiting 10m0s for microshift.service to be ready
??? I0403 11:58:52.530299     979 service.go:38] microshift.service is ready
??? I0403 11:58:52.532292     979 net.go:79] host gateway IP address: 192.168.112.125
??? I0403 11:58:52.555077     979 microshift_core_workloads.go:71] vgs reported: {"report":[{"vg":[{"vg_name":"rhel"}]}],"log":[]}
??? I0403 11:58:52.555138     979 microshift_core_workloads.go:93] Detected 1 volume group (rhel) - LVMS is expected
??? I0403 11:58:52.555143     979 microshift_core_workloads.go:126] Configured optional CSI components: []
??? I0403 11:58:52.555147     979 microshift_core_workloads.go:117] At least one CSI Component is enabled
??? I0403 11:58:52.555770     979 utils.go:34] Waiting for 9 goroutines
??? I0403 11:58:52.555791     979 workloads.go:94] Waiting 10m0s for deployment/service-ca in openshift-service-ca
??? I0403 11:58:52.555890     979 workloads.go:58] Waiting 10m0s for daemonset/ovnkube-master in openshift-ovn-kubernetes
??? I0403 11:58:52.555999     979 workloads.go:94] Waiting 10m0s for deployment/router-default in openshift-ingress
??? I0403 11:58:52.556096     979 workloads.go:58] Waiting 10m0s for daemonset/dns-default in openshift-dns
??? I0403 11:58:52.556244     979 workloads.go:58] Waiting 10m0s for daemonset/ovnkube-node in openshift-ovn-kubernetes
??? I0403 11:58:52.556330     979 workloads.go:94] Waiting 10m0s for deployment/lvms-operator in openshift-storage
??? I0403 11:58:52.556382     979 workloads.go:58] Waiting 10m0s for daemonset/vg-manager in openshift-storage
??? I0403 11:58:52.556425     979 workloads.go:94] Waiting 10m0s for deployment/csi-snapshot-controller in kube-system
??? I0403 11:58:52.556474     979 workloads.go:58] Waiting 10m0s for daemonset/node-resolver in openshift-dns
??? I0403 11:58:52.574284     979 workloads.go:89] Daemonset/ovnkube-node in openshift-ovn-kubernetes is ready
??? I0403 11:58:52.574344     979 workloads.go:89] Daemonset/dns-default in openshift-dns is ready
??? I0403 11:59:12.871058     979 workloads.go:89] Daemonset/node-resolver in openshift-dns is ready
??? I0403 11:59:12.871621     979 workloads.go:89] Daemonset/ovnkube-master in openshift-ovn-kubernetes is ready
??? I0403 11:59:12.871748     979 workloads.go:132] Deployment/csi-snapshot-controller in kube-system is ready
??? I0403 11:59:25.175015     979 workloads.go:132] Deployment/service-ca in openshift-service-ca is ready
??? I0403 11:59:42.559264     979 workloads.go:132] Deployment/lvms-operator in openshift-storage is ready
??? I0403 11:59:52.557786     979 workloads.go:132] Deployment/router-default in openshift-ingress is ready
??? I0403 11:59:52.558489     979 workloads.go:89] Daemonset/vg-manager in openshift-storage is ready
??? I0403 11:59:52.558505     979 healthcheck.go:28] MicroShift is ready
Script '40_microshift_running_check.sh' SUCCESS
--------------------
DEPRECATION NOTICE:
/usr/share/microshift/functions/greenboot.sh is now deprecated and will be removed in future release.
Planned removal: MicroShift 4.21
As a replacement consider using 'microshift healthcheck' command
--------------------
STARTED
GRUB boot variables:
boot_success=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_GREENBOOT_FAIL_MARKER=/run/microshift-greenboot-healthcheck-failed
System installation type:
bootc
System installation status:
bootcHost
??? I0403 11:59:52.750474    4059 service.go:29] microshift.service is enabled
??? I0403 11:59:52.750873    4059 service.go:31] Waiting 10m0s for microshift.service to be ready
??? I0403 11:59:52.752273    4059 service.go:38] microshift.service is ready
??? I0403 11:59:52.753263    4059 utils.go:34] Waiting for 1 goroutines
??? I0403 11:59:52.753393    4059 workloads.go:94] Waiting 10m0s for deployment/kserve-controller-manager in redhat-ods-applications
??? I0403 12:00:02.755475    4059 workloads.go:132] Deployment/kserve-controller-manager in redhat-ods-applications is ready
??? I0403 12:00:02.755605    4059 healthcheck.go:75] Workloads are ready
Script '41_microshift_running_check_ai_model_serving.sh' SUCCESS
--------------------
DEPRECATION NOTICE:
/usr/share/microshift/functions/greenboot.sh is now deprecated and will be removed in future release.
Planned removal: MicroShift 4.21
As a replacement consider using 'microshift healthcheck' command
--------------------
STARTED
GRUB boot variables:
boot_success=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_GREENBOOT_FAIL_MARKER=/run/microshift-greenboot-healthcheck-failed
System installation type:
bootc
System installation status:
bootcHost
??? I0403 12:00:02.896949    4128 service.go:29] microshift.service is enabled
??? I0403 12:00:02.897208    4128 service.go:31] Waiting 10m0s for microshift.service to be ready
??? I0403 12:00:02.899492    4128 service.go:38] microshift.service is ready
??? I0403 12:00:02.900279    4128 utils.go:34] Waiting for 2 goroutines
??? I0403 12:00:02.900363    4128 workloads.go:94] Waiting 10m0s for deployment/istiod-openshift-gateway-api in openshift-gateway-api
??? I0403 12:00:02.900948    4128 workloads.go:94] Waiting 10m0s for deployment/servicemesh-operator3 in openshift-gateway-api
??? I0403 12:00:42.913338    4128 workloads.go:132] Deployment/servicemesh-operator3 in openshift-gateway-api is ready
??? I0403 12:01:12.902297    4128 workloads.go:132] Deployment/istiod-openshift-gateway-api in openshift-gateway-api is ready
??? I0403 12:01:12.902418    4128 healthcheck.go:75] Workloads are ready
Script '41_microshift_running_check_gateway_api.sh' SUCCESS
--------------------
DEPRECATION NOTICE:
/usr/share/microshift/functions/greenboot.sh is now deprecated and will be removed in future release.
Planned removal: MicroShift 4.21
As a replacement consider using 'microshift healthcheck' command
--------------------
STARTED
GRUB boot variables:
boot_success=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_GREENBOOT_FAIL_MARKER=/run/microshift-greenboot-healthcheck-failed
System installation type:
bootc
System installation status:
bootcHost
??? I0403 12:01:13.057998    4772 service.go:29] microshift.service is enabled
??? I0403 12:01:13.058107    4772 service.go:31] Waiting 10m0s for microshift.service to be ready
??? I0403 12:01:13.059839    4772 service.go:38] microshift.service is ready
??? I0403 12:01:13.060617    4772 utils.go:34] Waiting for 2 goroutines
??? I0403 12:01:13.060644    4772 workloads.go:58] Waiting 10m0s for daemonset/dhcp-daemon in openshift-multus
??? I0403 12:01:13.060686    4772 workloads.go:58] Waiting 10m0s for daemonset/multus in openshift-multus
??? I0403 12:01:13.069341    4772 workloads.go:89] Daemonset/multus in openshift-multus is ready
??? I0403 12:01:13.069450    4772 workloads.go:89] Daemonset/dhcp-daemon in openshift-multus is ready
??? I0403 12:01:13.069503    4772 healthcheck.go:75] Workloads are ready
Script '41_microshift_running_check_multus.sh' SUCCESS
--------------------
DEPRECATION NOTICE:
/usr/share/microshift/functions/greenboot.sh is now deprecated and will be removed in future release.
Planned removal: MicroShift 4.21
As a replacement consider using 'microshift healthcheck' command
--------------------
STARTED
GRUB boot variables:
boot_success=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_GREENBOOT_FAIL_MARKER=/run/microshift-greenboot-healthcheck-failed
System installation type:
bootc
System installation status:
bootcHost
??? I0403 12:01:13.206381    4804 service.go:29] microshift.service is enabled
??? I0403 12:01:13.206583    4804 service.go:31] Waiting 10m0s for microshift.service to be ready
??? I0403 12:01:13.207979    4804 service.go:38] microshift.service is ready
??? I0403 12:01:13.208717    4804 utils.go:34] Waiting for 2 goroutines
??? I0403 12:01:13.208779    4804 workloads.go:94] Waiting 10m0s for deployment/catalog-operator in openshift-operator-lifecycle-manager
??? I0403 12:01:13.209285    4804 workloads.go:94] Waiting 10m0s for deployment/olm-operator in openshift-operator-lifecycle-manager
??? I0403 12:01:13.215578    4804 workloads.go:132] Deployment/catalog-operator in openshift-operator-lifecycle-manager is ready
??? I0403 12:01:13.215673    4804 workloads.go:132] Deployment/olm-operator in openshift-operator-lifecycle-manager is ready
??? I0403 12:01:13.215684    4804 healthcheck.go:75] Workloads are ready
Script '50_microshift_running_check_olm.sh' SUCCESS
Running Wanted Health Check Scripts...
Finished greenboot Health Checks Runner.
----
+
.Example partial output for a {op-system-ostree} system
[source,terminal,subs="+attributes"]
----
#...
GRUB boot variables:
boot_success=0
boot_indeterminate=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
MICROSHIFT_WAIT_TIMEOUT_SEC=600
System installation type:
ostree
System installation status:
* rhel 19619bd269094510180c845c44d0944fd9aa15925376f249c4d680a3355e51ae.0
    Version: {op-system-version}
    origin refspec: edge:rhel-{op-system-version}-microshift-
#...
----
+
.Example partial output for an RPM system
[source,terminal]
----
#...
GRUB boot variables:
boot_success=1
boot_indeterminate=0
Greenboot variables:
GREENBOOT_WATCHDOG_CHECK_ENABLED=true
System installation type:
RPM
System installation status:
Not an ostree / bootc system
#...
----

[id="additional-resources_microshift-greenboot-workload-health-checks"]
[role="_additional-resources"]
== Additional resources

* The greenboot health check

* Auto applying manifests
