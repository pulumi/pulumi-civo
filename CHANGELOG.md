CHANGELOG
=========

## HEAD (Unreleased)
* Upgrade to v0.10.9 of the Civo Terraform Provider
  **Please Note:** `civo.KubernetesCluster` has had the `buildAt` output removed

---

## 1.0.5 (2021-08-03)
* Upgrade to v0.10.7 of the Civo Terraform Provider


## 1.0.4 (2021-07-20)
* Upgrade to v0.10.5 of the Civo Terraform Provider

## 1.0.3 (2021-06-16)
* Upgrade to v0.10.4 of the Civo Terraform Provider

## 1.0.2 (2021-06-14)
* Upgrade to v0.10.3 of the Civo Terraform Provider

## 1.0.1 (2021-06-09)
* Upgrade to v0.10.2 of the Civo Terraform Provider

## 1.0.0 (2021-04-19)
* Depend on Pulumi 3.0, which includes improvements to Python resource arguments and key translation, Go SDK performance,
  Node SDK performance, general availability of Automation API, and more.

## 0.5.0 (2021-04-12)
* Upgrade to pulumi-terraform-bridge v2.23.0

## 0.4.1 (2021-03-23)
* Upgrade to pulumi-terraform-bridge v2.22.1  
  **Please Note:** This includes a bug fix to the refresh operation regarding arrays

## 0.4.0 (2021-03-15)
* Upgrade to pulumi-terraform-bridge v2.21.0
* Release macOS arm64 binary

## 0.3.1 (2021-02-16)
* Upgrade to pulumi-terraform-bridge v2.19.0  
  **Please Note:** This includes a bug fix that stops mutating resources options in the nodejs provider

## 0.3.0 (2021-02-01)
* Upgrade to pulumi-terraform-bridge v2.18.1

## 0.2.1 (2021-01-13)
* Upgrade to v0.9.23 of the Civo Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.17.0
* Upgrade to Pulumi v2.17.0

## 0.2.0 (2020-10-26)
* Upgrade to Pulumi v2.12.0 and pulumi-terraform-bridge v2.11.0
* Improving the accuracy of previews leading to a more accurate understanding of what will actually change rather than assuming all output properties will change.  
  ** PLEASE NOTE:**  
  This new preview functionality can be disabled by setting `PULUMI_DISABLE_PROVIDER_PREVIEW` to `1` or `false`.

## 0.1.3 (2020-09-29)
* Upgrade to v0.9.21 of the Civo Terraform Provider

## 0.1.2 (2020-09-25)
* Upgrade to v0.9.20 of the Civo Terraform Provider

## 0.1.1 (2020-09-14)
* Upgrade to v0.9.17 of the Civo Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.8.0
* Upgrade to Pulumi v2.10.0

## 0.1.0 (2020-08-31)
* Upgrade to v0.9.15 of the Civo Terraform Provider
* Upgrade to pulumi-terraform-bridge v2.7.3
* Upgrade to Pulumi v2.9.0, which adds type annotations and input/output classes to Python

## 0.0.1 (2020-08-03)
* Initial release of the provider based on v0.9.14 of the Civo Terraform Provider
