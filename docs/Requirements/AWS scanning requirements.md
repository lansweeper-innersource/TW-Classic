<!-- # AWS scanning requirements -->
Lansweeper can scan VPCs and instances (virtual machines) hosted on the Amazon Web Services (AWS) cloud platform. An asset is created for each VPC that has instances connected to it and for each instance as well. Any EC2-VPC environment can be scanned.

This article explains what the requirements are for AWS scanning and how to generate the access key required for scanning.

## Requirements

To scan an AWS cloud environment, the following requirements must be met:

- Your Lansweeper installation must be version 7.1 or higher.
- Your Lansweeper license must support AWS scanning.
- Your AWS environment must be an EC2-VPC environment. Scanning of old EC2-Classic environments is not supported.
- Your VPCs and instances must be located in one of the following regions: Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada (Central), China (Beijing), China (Ningxia), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Stockholm), Middle East (Bahrain), South America (São Paulo), US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon).
- Your Lansweeper scanning server must have access to the internet.
- Your Lansweeper scanning server must be able to connect to https://\*.amazonaws.com.
- You must provide Lansweeper with an access key that has programmatic access to AWS and list-only access to EC2. Your access key consists of an access key ID and secret access key. Lansweeper requires this access key to retrieve data from the AWS API.

## Generate the access key

To generate the access key that you'll need to submit in Lansweeper for AWS scanning:

1. Log into your AWS account.
2. Browse to **Identity and Access Management (IAM)**. One way to do this is by clicking [this direct link](https://console.aws.amazon.com/iam/home#/home "AWS console").
3. Select the **Policies** menu on the left and click the **Create policy** button.
4. Select the EC2 service, and give list access to the following actions:  

   [Spoiler](#) (Highlight to read)

   - DescribeHosts
   - DescribeImages
   - DescribeInstances
   - DescribeNetworkInterfaces
   - DescribeVpcs
   - DescribeVolumes
   - DescribeElasticGpus
   - DescribeSubnets
   - DescribeInstanceCreditSpecifications
   - DescribeSecurityGroups

   DescribeHosts
   DescribeImages
   DescribeInstances
   DescribeNetworkInterfaces
   DescribeVpcs
   DescribeVolumes
   DescribeElasticGpus
   DescribeSubnets
   DescribeInstanceCreditSpecifications
   DescribeSecurityGroups

   
5. Select **Review policy**
6. Submit a name and description for your policy and select **Create policy**.

   
7. Select the **Users** menu on the left and select **Add user**.
8. Give your user a name, grant programmatic access to AWS and select **Next: Permissions**.

   
9. Choose the option **Attach existing policies directly**, select the policy you previously created and select **Next: Tags**.

   
10. Optionally, tag your user and select **Next: Review**.
11. Check whether your submitted settings are correct and select **Create user**.
12. On the resulting page, select **Show** to display your secret access key. Copy both the access key ID and secret access key displayed on the page. This is what you'll need to submit as a credential in Lansweeper.   
    You can configure AWS scanning in Lansweeper by following the instructions in [this knowledge base article](/classic/docs/scan-an-aws-cloud-environment).

    

You will not be able to see your key again once you leave this page, so make sure you store it somewhere safe for future reference. If you do lose your key, you will need to generate a new one. You can have up to two keys per user at a time. You can delete one key to replace it with another if required.
