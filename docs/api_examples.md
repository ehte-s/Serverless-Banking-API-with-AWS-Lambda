# API Examples



```bash
Check Balance
curl https://your-api-url.amazonaws.com/prod/balance/test123

Response
{
  "accountId": "test123",
  "balance": 1000
}

Credit Account
curl -X POST https://your-api-url.amazonaws.com/prod/transaction \
  -H "Content-Type: application/json" \
  -d '{"accountId":"test123","amount":200,"type":"credit"}'

Response
{
  "status": "success",
  "transactionId": "uuid-here",
  "accountId": "test123",
  "amount": 200,
  "type": "credit"
}

Debit Account
curl -X POST https://your-api-url.amazonaws.com/prod/transaction \
  -H "Content-Type: application/json" \
  -d '{"accountId":"test123","amount":50,"type":"debit"}'

Response
{
  "status": "success",
  "transactionId": "uuid-here",
  "accountId": "test123",
  "amount": 150,
  "type": "debit"
}
