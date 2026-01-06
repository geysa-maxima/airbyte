# destination-oracle-custom01 (skeleton)

Este repositório contém um template mínimo de um destination Airbyte para Oracle (nome: destination-oracle-custom01).
É uma base para você implementar spec/check/write conforme suas regras de negócios.

Como usar (local):

1) Construir a imagem Docker
```bash
docker build -t geysa-maxima/destination-oracle-custom01:dev .
```

2) Testar o comando `spec` (retorna o spec JSON)
```bash
docker run --rm geysa-maxima/destination-oracle-custom01:dev spec
```

3) Testar `check` com um arquivo config.json:
```json
{
  "username": "meu_usuario",
  "password": "minha_senha",
  "dsn": "host:1521/service_name",
  "schema": "MY_SCHEMA"
}
```
```bash
docker run --rm -v $(pwd)/config.json:/config.json geysa-maxima/destination-oracle-custom01:dev check --config /config.json
```

4) Para usar com Airbyte:
- Rode o Airbyte (local) [https://airbyte.com/docs/tutorials/deploy-airbyte].
- Vá em Settings → Destinations → + New Destination → Use a custom image
- Informe a imagem: `geysa-maxima/destination-oracle-custom01:dev`
- Configure o Destination usando o `spec` exposto pelo conector

Observações sobre Oracle:
- Uso do driver Python `oracledb`: na maioria dos casos o modo "thin" funciona sem Instant Client. Se precisar de funcionalidades adicionais instale o Oracle Instant Client e ajuste LD_LIBRARY_PATH.
- DSN pode ser "host:port/service_name" (ex.: "oracle.example.com:1521/XEPDB1") ou TNS.

Próximos passos recomendados:
- Implementar corretamente o `spec` (JSON Schema) detalhado com campos esperados.
- Implementar `write` com mapeamento de streams -> tabelas e criação automática de tabelas (se desejar).
- Adicionar testes locais e integração com dados de exemplo.
- Opcional: configurar CI para build e push para um registry (DockerHub / GitHub Container Registry).
