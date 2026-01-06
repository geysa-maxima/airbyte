# Entrypoint que o Airbyte espera; delega para a classe Destination
from airbyte_cdk.entrypoint import launch
from .destination import DestinationOracleCustom01

if __name__ == "__main__":
    launch(DestinationOracleCustom01())
