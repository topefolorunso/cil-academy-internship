#!/bin/bash

# when you create a key pair using the aws management console, you are prompted to download and save your private key (.pem file) locally to ssh into the instance. however, this doesn't happen when you create a key pair with cloud formation. hence, you need to get your private key via another method.

# when you create a key pair with cloudformation, cloudformation securely stores the private key in aws systems manager parameter store for you using the format /ec2/keypair/<key_pair_id>. now, you need to retrieve this private key from the systems manager using either the management console or the cli (preferably).

# suppose you define your key pair using the block below;

# Resources:
#   NewKeyPair:
#     Type: 'AWS::EC2::KeyPair'
#     Properties: 
#       KeyName: new-key-pair --this is the name of the key pair to define in line 18 below

# run the commands below to retireve the private key and store it locally in a .pem file

# set the variable to store name of the key pair
keyPairName=""

# promts user to provide a valid key pair name if it hasn't been modified in the file or if the user enters an empty string as input
while [ -z $keyPairName ];

    do

        echo "invalid key pair name!"
        echo "you need to provide a non-empty string as the key pair name!"
        echo "kindly enter a valid name for the key pair: "

        read keyPairName

    done  

# fetch the ID of the key pair and set the variable to store it
keyPairID=$(aws ec2 describe-key-pairs --filters Name=key-name,Values=$keyPairName --query KeyPairs[*].KeyPairId --output text)

# echo "keyPairID = $keyPairID"

if [ -z $keyPairID ]

    then

        echo "the key pair with the name [$keyPairName] does not exist in aws systems manager parameter store."
        echo "please create a valid key pair with cloudformation or check the key pair name and try again!"

    else

        # you can (or rather should) modify the file name (if you wish)
        fileName="private_key"
        # fetch the private key and store it in the .pem file
        aws ssm get-parameter --name /ec2/keypair/$keyPairID --with-decryption --query Parameter.Value --output text > $fileName.pem

        chmod 400 $fileName.pem

fi
