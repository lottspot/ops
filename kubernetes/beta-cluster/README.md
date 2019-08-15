# civic-cloud: beta-cluster

This plan is based on configuration originally generated by the [linode-cli](https://github.com/linode/linode-cli) tool and then tweaked following the documentation for the underlying [terraform-linode-k8s](https://github.com/linode/terraform-linode-k8s) terraform module.

## Applying terraform plan

```bash
# obtain from https://cloud.linode.com/profile/tokens
export TF_VAR_linode_token="YOUR_TOKEN"
terraform apply
```