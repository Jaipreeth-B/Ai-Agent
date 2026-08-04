//the above written is cerebras ai api

curl.exe https://api.cerebras.ai/v1/chat/completions ^
  -H "Authorization: Bearer API_KEY****^
  -d "{\"model\":\"gpt-oss-120b\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}]}"