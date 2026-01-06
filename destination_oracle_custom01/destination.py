"""
Skeleton do destination Oracle para Airbyte (placeholder).
Implemente spec(), check(), write() conforme sua lógica.
"""

from airbyte_cdk.destinations import Destination
from airbyte_cdk.models import (
    AirbyteCatalog,
    ConfiguredAirbyteCatalog,
    AirbyteConnectionStatus,
    Status,
)
import oracledb
import logging
import json

logger = logging.getLogger("airbyte.destination.oracledb")
logger.setLevel(logging.INFO)


class DestinationOracleCustom01(Destination):
    def spec(self, *args, **kwargs) -> dict:
        """
        Retorna o spec do conector (JSON Schema).
        Edite conforme necessário para expor campos:
         - dsn / host / port /service_name
         - username / password
         - schema / tables / outros
        """
        return {
            "documentationUrl": "https://github.com/geysa-maxima/airbyte",
            "connectionSpecification": {
                "type": "object",
                "required": ["username", "password", "dsn"],
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "dsn": {"type": "string", "description": "TNS / host:port/service_name"},
                    "schema": {"type": "string"},
                },
            },
        }

    def check(self, logger, config) -> AirbyteConnectionStatus:
        """
        Valida conexão com Oracle.
        O Airbyte chama: docker run --rm <image> check --config <config.json>
        """
        try:
            conn = oracledb.connect(
                user=config["username"], password=config["password"], dsn=config["dsn"]
            )
            conn.close()
            return AirbyteConnectionStatus(status=Status.SUCCEEDED)
        except Exception as e:
            logger.exception("Check failed")
            return AirbyteConnectionStatus(status=Status.FAILED, message=str(e))

    def write(self, logger, config: dict, configured_catalog: ConfiguredAirbyteCatalog, input_messages):
        """
        Recebe mensagens do Airbyte (STREAM -> records) e aplica inserts/upserts no Oracle.
        - 'input_messages' é um generator/iterable com AirbyteMessages
        Implemente batching, tipos de mapeamento, transações e tratamento de erros conforme necessário.
        """
        # Exemplo básico (não pronto para produção)
        conn = oracledb.connect(
            user=config["username"], password=config["password"], dsn=config["dsn"]
        )
        cursor = conn.cursor()

        try:
            for message in input_messages:
                # message é um dict / objeto do Airbyte; adapte conforme sua versão do CDK
                # Você vai precisar extrair stream, namespace e record -> message.record.data
                # Este é apenas um placeholder
                logger.info("Received message: %s", message)
                # TODO: parse e INSERT no Oracle
            conn.commit()
        except Exception:
            conn.rollback()
            logger.exception("Erro ao escrever no Oracle")
            raise
        finally:
            cursor.close()
            conn.close()
