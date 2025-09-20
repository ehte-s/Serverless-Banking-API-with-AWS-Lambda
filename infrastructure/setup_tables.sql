-- Commands to create DynamoDB tables

-- Create BankAccounts table
aws dynamodb create-table \
  --table-name BankAccounts \
  --attribute-definitions AttributeName=accountId,AttributeType=S \
  --key-schema AttributeName=accountId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

-- Create Transactions table  
aws dynamodb create-table \
  --table-name Transactions \
  --attribute-definitions AttributeName=transactionId,AttributeType=S AttributeName=accountId,AttributeType=S \
  --key-schema AttributeName=transactionId,KeyType=HASH \
  --global-secondary-indexes '[{"IndexName":"AccountIndex","KeySchema":[{"AttributeName":"accountId","KeyType":"HASH"}],"Projection":{"ProjectionType":"ALL"}}]' \
  --billing-mode PAY_PER_REQUEST
