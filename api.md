//the above written is cerebras ai api

curl.exe https://api.cerebras.ai/v1/chat/completions ^
  -H "Authorization: Bearer csk-j2j8dn3kmy8tp4ncnc5nnv9vnemf29hmtdecejxp68trfp9f" ^
  -H "Content-Type: application/json" ^
  -d "{\"model\":\"gpt-oss-120b\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}]}"