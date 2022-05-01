#!/bin/bash

echo "Hi"
url="https://api.twilio.com/2010-04-01/Accounts/ACf6eb21af513bc2f2b7d53dbb46e5e94e/Messages.json"
echo $url
params='@{ To = "+447880313397"; From = "+13254138415"; Body = "Hello from Twilio" }'
echo $params
secret="158366e7886efc16aca05fd8dc73a518" | ConvertTo-SecureString "-asPlainText" -Force


$url = "https://api.twilio.com/2010-04-01/Accounts/ACf6eb21af513bc2f2b7d53dbb46e5e94e/Messages.json"
$params = @{ To = "+447880313397"; From = "+13254138415"; Body = "Hello from Twilio" }
$secret = "158366e7886efc16aca05fd8dc73a518" | ConvertTo-SecureString -asPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential(ACf6eb21af513bc2f2b7d53dbb46e5e94e, $secret)
Invoke-WebRequest $url -Method Post -Credential $credential -Body $params -UseBasicParsing | ConvertFrom-Json | Select sid, body