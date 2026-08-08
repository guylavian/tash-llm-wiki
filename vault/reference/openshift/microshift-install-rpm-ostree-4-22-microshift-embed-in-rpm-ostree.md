---
title: "Embedding in a {op-system-ostree} image using image builder"
type: reference
domain: openshift
slug: microshift-install-rpm-ostree-4-22-microshift-embed-in-rpm-ostree
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree
version: 4.22
family: microshift_install_rpm_ostree
documentKind: "Documentation"
---

# Embedding in a {op-system-ostree} image using image builder

[id="microshift-embed-in-rpm-ostree"]
= Embedding in a {op-system-ostree} image using image builder

[role="_abstract"]
Use the image builder tool to create a customized {op-system-base} image that contains {microshift-short}.

// Module included in the following assemblies:
//
// microshift_install_rpm_ostree/microshift-embed-rpm-ostree.adoc

[id="microshift-preparing-for-image-building_{context}"]
= Preparing for image building

[role="_abstract"]
Use the image builder tool to compose customized {op-system-ostree-first} images optimized for edge deployments.

You can run a {microshift-short} node with your applications on a {op-system-ostree} virtual machine for development and testing first, then use your whole solution in edge production environments.

Use the following {op-system-base} documentation to understand the full details of using {op-system-ostree}:

* Introduction to RHEL for Edge images

* To build an {op-system-ostree-first} {op-system-version} image for a given CPU architecture, you need a {op-system-base} {op-system-version} build host of the same CPU architecture that meets the image builder system requirements. See the following link for more information:

** Image builder system requirements

* To install image builder and the `composer-cli` tool, use the following instructions:

** Installing image builder

// Module included in the following assemblies:
//
// * microshift_install_rpm_ostree/microshift-embed-into-rpm-ostree.adoc

[id="microshift-enable-eus-repos_{context}"]
= Enabling extended support repositories for image building

[role="_abstract"]
If you have an extended support (EUS) release of {microshift-short} or {op-system-base-full}, you must enable the {op-system-base} EUS repositories for image builder to use. If you do not have an EUS version, you can skip these steps.

.Prerequisites

* You have either an EUS version of {microshift-short} or {op-system-base}, or you are updating to one.
* You have root-user access to your build host.
* You have reviewed the following {op-system-bundle} release compatibility matrix
+
--
--

.Procedure

. Create the `/etc/osbuild-composer/repositories` directory by running the following command:
+
[source,terminal]
----
$ sudo mkdir -p /etc/osbuild-composer/repositories
----

. Copy the `/usr/share/osbuild-composer/repositories/rhel-{op-system-version}.json` file into the `/etc/osbuild-composer/repositories` directory by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo cp /usr/share/osbuild-composer/repositories/rhel-{op-system-version}.json /etc/osbuild-composer/repositories/rhel-{op-system-version}.json
----

. Update the `baseos` source by modifying the `/etc/osbuild-composer/repositories/rhel-{op-system-version}.json` file with the following values:
+
[source,terminal,subs="attributes+"]
----
# ...
"baseurl": "https://cdn.redhat.com/content/eus/rhel{op-system-version-major}/{op-system-version}//baseos/os",
# ...
----
+
You can replace _{op-system-version-major}_ with the major {op-system-base} version you are using if different from the value in this example, and replace _{op-system-version}_ with the _<major.minor>_ version. Be certain that the {op-system-base} version you choose is compatible with the {microshift-short} version you are using.

. Optional: Apply the `baseos` update by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo sed -i "s,dist/rhel{op-system-version-major}/{op-system-version}/$(uname -m)/baseos/,eus/rhel{op-system-version-major}/{op-system-version}/$(uname -m)/baseos/,g" \
/etc/osbuild-composer/repositories/rhel-{op-system-version}.json
----
+
You can replace _{op-system-version-major}_ with the major {op-system-base} version you are using if different from the value in this example, and replace _{op-system-version}_ with the _<major.minor>_ version. Be certain that the {op-system-base} version you choose is compatible with the {microshift-short} version you are using.

. Update the `appstream` source by modifying the `/etc/osbuild-composer/repositories/rhel-<major.minor>.json` file with the following values:
+
[source,terminal,subs="attributes+"]
----
# ...
"baseurl": "https://cdn.redhat.com/content/eus/rhel{op-system-version-major}/{op-system-version}//appstream/os",
# ...
----
+
You can replace _{op-system-version-major}_ with the major {op-system-base} version you are using if different from the value in this example, and replace _{op-system-version}_ with the _<major.minor>_ version. Be certain that the {op-system-base} version you choose is compatible with the {microshift-short} version you are using.

. Optional. Apply the `appstream` update by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo sed -i "s,dist/rhel{op-system-version-major}/{op-system-version}/$(uname -m)/appstream/,eus/rhel{op-system-version-major}/{op-system-version}/$(uname -m)/appstream/,g" \
/etc/osbuild-composer/repositories/rhel-{op-system-version}.json
----
+
You can replace _{op-system-version-major}_ with the major {op-system-base} version you are using if different from the value in this example, and replace _{op-system-version}_ with the _<major.minor>_ version. Be certain that the {op-system-base} version you choose is compatible with the {microshift-short} version you are using.

.Verification

. Verify the `baseos` source by running the following command:
+
[source,terminal]
----
$ sudo composer-cli sources info baseos | grep 'url ='
----
+
.Example output
[source,text,subs="attributes+"]
----
url = "https://cdn.redhat.com/content/eus/rhel{op-system-version-major}/{op-system-version}/x86_64/baseos/os"
----

. Verify the `appstream` source by running the following command:
+
[source,terminal]
----
$ sudo composer-cli sources info appstream | grep 'url ='
----
+
.Example output
[source,text,subs="attributes+"]
----
url = "https://cdn.redhat.com/content/eus/rhel{op-system-version-major}/{op-system-version}/x86_64/appstream/os"
----

// Module included in the following assemblies:
//
// * microshift_install_rpm_ostree/microshift-embed-into-rpm-ostree.adoc
// * microshift_install_rpm/microshift-update-rpms-ostree.adoc

[id="adding-microshift-repos-image-builder_{context}"]
= Adding {microshift-short} repositories to image builder

[role="_abstract"]
Add the {microshift-short} repositories to image builder on your build host.

.Prerequisites

* Your build host meets the image builder system requirements.
* You have installed and set up image builder and the `composer-cli` tool.
* You have root-user access to your build host.

.Procedure

. Create an image builder configuration file for adding the `{rpm-repo-version}` RPM repository source required to pull {microshift-short} RPMs by running the following command:
+
[source,text,subs="attributes+"]
----
cat > {rpm-repo-version}.toml <<EOF
id = "{rpm-repo-version}"
name = "Red Hat OpenShift Container Platform {ocp-version} for RHEL {op-system-version-major}"
type = "yum-baseurl"
url = "https://cdn.redhat.com/content/dist/layered/rhel9/$(uname -m)/rhocp/{ocp-version}/os"
check_gpg = true
check_ssl = true
system = false
rhsm = true
EOF
----

. Create an image builder configuration file for adding the `fast-datapath` RPM repository by running the following command:
+
[source,text,subs="attributes+"]
----
cat > fast-datapath.toml <<EOF
id = "fast-datapath"
name = "Fast Datapath for RHEL 9"
type = "yum-baseurl"
url = "https://cdn.redhat.com/content/dist/layered/rhel9/$(uname -m)/fast-datapath/os"
check_gpg = true
check_ssl = true
system = false
rhsm = true
EOF
----

. Add the sources to the image builder by running the following commands:
+
[source,terminal,subs="attributes+"]
----
$ sudo composer-cli sources add {rpm-repo-version}.toml
----
+
[source,terminal]
----
$ sudo composer-cli sources add fast-datapath.toml
----

.Verification

* Confirm that the sources were added properly by running the following command:
+
[source,terminal]
----
$ sudo composer-cli sources list
----
+
.Example output
[source,terminal,subs="attributes+"]
----
appstream
baseos
fast-datapath
{rpm-repo-version}
----

.Next steps

* Create the blueprint. For more information, see the following links:

** Blueprint Reference
** Creating a {op-system-ostree} Container blueprint using image builder CLI
** Building OSTree image
** Installing Podman

// Module included in the following assemblies:
//
// * microshift_install_rpm_ostree/microshift-embed-into-rpm-ostree.adoc
// * microshift_install_rpm/microshift-update-rpms-ostree.adoc

[id="adding-microshift-service-to-blueprint_{context}"]
= Adding the {microshift-short} service to a blueprint

[role="_abstract"]
Adding the {microshift-short} RPM package to an image builder blueprint enables the build of a {op-system-ostree} image with {microshift-short} embedded.

.Procedure

. Use the blueprint installed in the `/usr/share/microshift/blueprint` directory that is specific to your platform architecture. See the following example snippet for an explanation of the blueprint sections:
+
.Generated image builder blueprint example snippet
[source,text,subs="attributes+"]
----
name = "microshift_blueprint"
description = "MicroShift {ocp-version}.1 on x86_64 platform"
version = "0.0.1"
modules = []
groups = []

[[packages]]
name = "microshift"
version = "{ocp-version}.1"
...
...

[customizations.services]
enabled = ["microshift"]

[customizations.firewall]
ports = ["ssh"]
...
...

[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:f41e79c17e8b41f1b0a5a32c3e2dd7cd15b8274554d3f1ba12b2598a347475f4"

[[containers]]
source = "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:dbc65f1fba7d92b36cf7514cd130fe83a9bd211005ddb23a8dc479e0eea645fd"
...
…
EOF
----
* `\[[packages]] name = "microshift"`: references for all non-optional {microshift-short} RPM packages using the same version compatible with the `microshift-release-info` RPM.
* `[customizations.services] enabled = ["microshift"]`: references for automatically enabling {microshift-short} on system startup and applying default networking settings.
* `\[[containers]] source = "quay.io/openshift-release-dev/...`: references for all non-optional {microshift-short} container images necessary for an offline deployment. The SHA depends on the release you are using.

. Add the blueprint to the image builder by running the following command:
+
[source,terminal]
----
$ sudo composer-cli blueprints push microshift_blueprint.toml
----

.Verification

. Verify the image builder configuration listing only {microshift-short} packages by running the following command:
+
[source,terminal]
----
$ sudo composer-cli blueprints depsolve microshift_blueprint | grep microshift
----
+
.Example output
[source,terminal,subs="+attributes"]
----
blueprint: microshift_blueprint v0.0.1
    microshift-release-info-{ocp-version}.1-202511250827.p0.g4105d3b.assembly.{ocp-version}.1.el9.noarch
    microshift-{ocp-version}.1-202511250827.p0.g4105d3b.assembly.{ocp-version}.1.el9.x86_64
----

. Optional: Verify the image builder configuration that lists all of the components to be installed by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ sudo composer-cli blueprints depsolve microshift_blueprint
----

// Module included in the following assemblies:
//
// * microshift_install_rpm/microshift-update-rpms-ostree.adoc

[id="microshift-adding-other-services-to-blueprint_{context}"]
= Adding other packages to a blueprint

[role="_abstract"]
Add the references for optional RPM packages to your `ostree` blueprint to enable them.

.Prerequisites

* You created an image builder blueprint file.

.Procedure

. Edit your `ostree` blueprint by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ vi __<microshift_blueprint.toml>__
----
+
Replace `_<microshift_blueprint.toml>_` with the name of the blueprint file used for the {microshift-short} service.

. Add the following example text to your blueprint:
+
[source,text,subs="+quotes"]
----
[[packages]]
name = "__<microshift_additional_package_name>__"
version = "*"
----
+
* `\[[packages]] name =` Include one stanza for each additional service that you want to add. For example, replace `_<microshift_additional_package_name>_` in with the name the RPM for the service you want to include such as `microshift-olm`. Add another stanza as needed.

.Next steps

. Add custom certificate authorities to the blueprint as needed. For more information, see the following links:

* Using Shared System Certificates ({op-system-base} 9)
* Supported image customizations ({op-system-base} 9)
* Creating and managing OSTree image updates

. After you finish adding to your blueprint, you can apply the manifests to an active node by building a new {op-system-ostree} system and deploying it on the client:

* Create the ISO.
* Add the blueprint and build the ISO.
* Download the ISO and prepare it for use.
* Do any provisioning that is needed.

//Module included in the following assemblies:
//
//* microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc

[id="microshift-ca-adding-bundle_{context}"]
= Certificate authority bundle configuration

[role="_abstract"]
{microshift-short} uses the host trust bundle when clients evaluate server certificates.

You can also use a customized security certificate chain to improve the compatibility of your endpoint certificates with clients specific to your deployments. To do this, you can add a certificate authority (CA) bundle with root and intermediate certificates to the {op-system-ostree-first} system-wide truststore.

//Module included in the following assemblies:
//
//* microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc

[id="microshift-ca-adding-bundle-ostree_{context}"]
= Adding a certificate authority bundle to a blueprint

[role="_abstract"]
You can include additional certificate authorities (CAs) to be trusted by the operating system when pulling images from an image registry. To add the additional CAs to the {op-system-ostree-first} `rpm-ostree` image, configure them in the blueprint that you use to create the image.

[NOTE]
====
This procedure requires you to configure the CA bundle customizations in the blueprint, and then add steps to your Kickstart file to enable the bundle. In the following steps, `data` is the key, and `<value>` represents the PEM-encoded certificate.
====

.Prerequisites

* You have root user access to your build host.
* Your build host meets the image builder system requirements.
* You have installed and set up image builder and the `composer-cli` tool.

.Procedure

. Add the following custom values to your blueprint to add a directory.

.. Add instructions to your blueprint on the host where the image is built to create the directory, for example, `/etc/pki/ca-trust/source/anchors/` for your certificate bundles.
+
[source,terminal]
----
[[customizations.directories]]
path = "/etc/pki/ca-trust/source/anchors"
----

.. After the image has booted, create the certificate bundles, for example, `/etc/pki/ca-trust/source/anchors/cert1.pem`:
+
[source,terminal]
----
[[customizations.files]]
path = "/etc/pki/ca-trust/source/anchors/cert1.pem"
data = "<value>"
----

. To enable the certificate bundle in the system-wide truststore configuration, use the `update-ca-trust` command on the host where the image you are using has booted, for example:
+
[source,terminal]
----
$ sudo update-ca-trust
----
+
[NOTE]
====
The `update-ca-trust` command might be included in the `%post` section of a Kickstart file used for {microshift-short} host installation so that all the necessary certificate trust is enabled on the first boot. You must configure the CA bundle customizations in the blueprint before adding steps to your Kickstart file to enable the bundle.

[source,terminal]
----
%post
# Update certificate trust storage in case new certificates were
# installed at /etc/pki/ca-trust/source/anchors directory
update-ca-trust
%end
----
====

// Module included in the following assemblies:
//
// * microshift/microshift-embed-into-rpm-ostree.adoc
// * microshift/microshift-update-rpms-ostree.adoc

[id="microshift-creating-ostree-iso_{context}"]
= Creating the {op-system-ostree} image with image builder

[role="_abstract"]
The {op-system-ostree} Installer image pulls the commit from the running container and creates an installable boot ISO with a Kickstart file configured to use the embedded `rpm-ostree` commit.

.Prerequisites

* Your build host meets the image builder system requirements.
* You installed and set up image builder and the `composer-cli` tool.
* You root-user access to your build host.
* You installed the `podman` tool.

.Procedure

. Start an `ostree` container image build by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ BUILDID=$(sudo composer-cli compose start-ostree --ref "rhel/{op-system-version-major}/$(uname -m)/edge" __<microshift_blueprint>__ edge-container | awk '/^Compose/ {print $2}')
----
Replace `_<microshift_blueprint>_` with the name of your blueprint.
+
This command also returns the identification (ID) of the build for monitoring.

. You can check the status of the build periodically by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose status
----
+
.Example output of a running build
[source,terminal]
----
ID                                     Status     Time                     Blueprint                 Version   Type               Size
cc3377ec-4643-4483-b0e7-6b0ad0ae6332   RUNNING    Wed Jun 7 12:26:23 2023  microshift_blueprint      0.0.1     edge-container
----
+
.Example output of a completed build
[source,terminal]
----
ID                                     Status     Time                      Blueprint              Version   Type               Size
cc3377ec-4643-4483-b0e7-6b0ad0ae6332   FINISHED   Wed Jun 7 12:32:37 2023   microshift_blueprint   0.0.1     edge-container
----
+
[NOTE]
====
You can use the `watch` command to monitor your build if you are familiar with how to start and stop it.
====

. Download the container image using the ID and get the image ready for use by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose image ${BUILDID}
----

. Change the ownership of the downloaded container image to the current user by running the following command:
+
[source,terminal]
----
$ sudo chown $(whoami). ${BUILDID}-container.tar
----

. Add read permissions for the current user to the image by running the following command:
+
[source,terminal]
----
$ sudo chmod a+r ${BUILDID}-container.tar
----

. Bootstrap a server on port 8085 for the `ostree` container image to be consumed by the ISO build by completing the following steps:

.. Get the `IMAGEID` variable result by running the following command:
+
[source,terminal]
----
$ IMAGEID=$(cat < "./${BUILDID}-container.tar" | sudo podman load | grep -o -P '(?<=sha256[@:])[a-z0-9]*')
----

.. Use the `IMAGEID` variable result to run the Podman command step by running the following command:
+
[source,terminal]
----
$ sudo podman run -d --name=minimal-microshift-server -p 8085:8080 ${IMAGEID}
----
+
This command also returns the ID of the container saved in the `IMAGEID` variable for monitoring.

. Generate the installation program blueprint file by running the following command:
+
[source,text]
----
cat > microshift-installer.toml <<EOF
name = "microshift-installer"

description = ""
version = "0.0.0"
modules = []
groups = []
packages = []
EOF
----

// Module included in the following assemblies:
//
// microshift_install_rpm_ostree/microshift-embed-into-rpm-ostree.adoc

[id="microshift-add-blueprint-build-iso_{context}"]
= Add the blueprint to image builder and build the ISO

[role="_abstract"]
You must add the blueprint to an image builder to build the ISO.

.Procedure

. Add the blueprint to the image builder by running the following command:
+
[source,terminal]
+
----
$ sudo composer-cli blueprints push microshift-installer.toml
----

. Start the `ostree` ISO build by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ BUILDID=$(sudo composer-cli compose start-ostree --url http://localhost:8085/repo/ --ref "rhel/{op-system-version-major}/$(uname -m)/edge" microshift-installer edge-installer | awk '{print $2}')
----
+
This command also returns the identification (ID) of the build for monitoring.

. You can check the status of the build periodically by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose status
----
+
.Example output for a running build
[source,terminal]
----
ID                                     Status     Time                      Blueprint              Version   Type               Size
c793c24f-ca2c-4c79-b5b7-ba36f5078e8d   RUNNING    Wed Jun 7 13:22:20 2023   microshift-installer   0.0.0     edge-installer
----
+
.Example output for a completed build
[source,terminal]
----
ID                                     Status     Time                      Blueprint              Version   Type               Size
c793c24f-ca2c-4c79-b5b7-ba36f5078e8d   FINISHED   Wed Jun 7 13:34:49 2023   microshift-installer   0.0.0     edge-installer
----

// Module included in the following assemblies:
//
// * microshift/microshift-embed-into-rpm-ostree.adoc
// * microshift/microshift-update-rpms-ostree.adoc

[id="microshift-download-iso-prep-for-use_{context}"]
= Download the ISO and prepare it for use

[role="_abstract"]
After creating the ISO, you must download it and prepare it for use.

.Procedure

. Download the ISO using the ID by running the following command:
+
[source,terminal]
----
$ sudo composer-cli compose image ${BUILDID}
----

. Change the ownership of the downloaded container image to the current user by running the following command:
+
[source,terminal]
----
$ sudo chown $(whoami). ${BUILDID}-installer.iso
----

. Add read permissions for the current user to the image by running the following command:
+
[source,terminal]
----
$ sudo chmod a+r ${BUILDID}-installer.iso
----

.Next steps

* Provision a virtual machine with a Kickstart file.
//Q: We don't actually finish the procedures showing launching the virtual machine and using this ISO. Should we include those procedure or link to them more constructively?

// Module included in the following assemblies:
//
// microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc

[id="microshift-embed-kickstart-iso_{context}"]
= Embedding a Kickstart file in an ISO

[role="_abstract"]
You can use the Kickstart file provided with {microshift-short}, or you can update an existing {op-system-ostree} Installer (ISO) Kickstart file.

When ready, embed the Kickstart file into the ISO. Your Kickstart file must include detailed instructions about how to create a user and how to fetch and deploy the {op-system-ostree} image.

.Prerequisites

* You created a {op-system-ostree} Installer (ISO) image containing your {op-system-ostree} commit with {microshift-short}.

* You have an existing Kickstart file ready for updating. You can use the `microshift-starter.ks` Kickstart file provided with the {microshift-short} RPMs.

.Procedure

. In the main section of the Kickstart file, update the setup of the filesystem such that it contains an LVM volume group called `rhel` with at least 10GB system root. Leave free space for the LVMS CSI driver to use for storing the data for your workloads.
+
.Example Kickstart file snippet for configuring the filesystem
[source,text]
----
# Partition disk such that it contains an LVM volume group called `rhel` with a
# 10GB+ system root but leaving free space for the LVMS CSI driver for storing data.
#
# For example, a 20GB disk would be partitioned in the following way:
#
# NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
# sda             8:0    0  20G  0 disk
# ├─sda1          8:1    0 200M  0 part /boot/efi
# ├─sda1          8:1    0 800M  0 part /boot
# └─sda2          8:2    0  19G  0 part
#  └─rhel-root  253:0    0  10G  0 lvm  /sysroot
#
ostreesetup --nogpg --osname=rhel --remote=edge \
--url=file:///run/install/repo/ostree/repo --ref=rhel/<RHEL VERSION NUMBER>/x86_64/edge
zerombr
clearpart --all --initlabel
part /boot/efi --fstype=efi --size=200
part /boot --fstype=xfs --asprimary --size=800
# Uncomment this line to add a SWAP partition of the recommended size
#part swap --fstype=swap --recommended
part pv.01 --grow
volgroup rhel pv.01
logvol / --vgname=rhel --fstype=xfs --size=10000 --name=root
# To add users, use a line such as the following
user --name=<YOUR_USER_NAME> \
--password=<YOUR_HASHED_PASSWORD> \
--iscrypted --groups=<YOUR_USER_GROUPS>
----

. In the `%post` section of the Kickstart file, add your pull secret and the mandatory firewall rules.
+
.Example Kickstart file snippet for adding the pull secret and firewall rules
[source,terminal]
----
%post --log=/var/log/anaconda/post-install.log --erroronfail

# Add the pull secret to CRI-O and set root user-only read/write permissions
cat > /etc/crio/openshift-pull-secret << EOF
YOUR_OPENSHIFT_PULL_SECRET_HERE
EOF
chmod 600 /etc/crio/openshift-pull-secret

# Configure the firewall with the mandatory rules for MicroShift
firewall-offline-cmd --zone=trusted --add-source=10.42.0.0/16
firewall-offline-cmd --zone=trusted --add-source=169.254.169.1

%end
----

. Install the `mkksiso` tool by running the following command:
+
[source,terminal]
----
$ sudo yum install -y lorax
----

. Update the ISO with your new Kickstart file by running the following command:
+
[source,terminal]
----
$ sudo mkksiso <your_kickstart>.ks <your_installer>.iso <updated_installer>.iso
----

[role="_additional-resources"]
.Additional resources

* Creating Kickstart files
* A.1. Kickstart file format
* How to embed a Kickstart file into an ISO image

[id="additional-resources_microshift-embed-in-rpm-ostree"]
[role="_additional-resources"]
== Additional resources

* Creating the {op-system-ostree} image
* Applying updates on an OSTree system
* System requirements for installing {microshift-short}
* Required firewall settings
* Using Kickstart files for embedding {microshift-short} in {op-system-base} installation
* Red Hat Hybrid Cloud Console pull secret
* Accessing the {microshift-short} node with oc

//Add modules about using the VM and getting the ISO up and running, then starting MicroShift...
