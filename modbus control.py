import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config
)
from pymodbus.framer import Framer
from time import sleep


def run_sync_simple_client(comm, host, port, framer=Framer.SOCKET):
    """Run sync client."""
    # activate debugging
    pymodbus_apply_logging_config("DEBUG")
    print("get client")
    if comm == "tcp":
        client = ModbusClient.ModbusTcpClient(
            host,
            port=port,
            framer=framer,
            # timeout=10,
            # retries=3,
            # retry_on_empty=False,y
            # source_address=("localhost", 0),
        )
    
    print("connect to server")
    client.connect()

    print("get and verify data")
    for i in range(1, 2):
        try:
            r = client.write_register(128, i)
        except ModbusException as exc:
            print(f"Received ModbusException({exc}) from library")
            client.close()
            return
        if r.isError():
            print(f"Received Modbus library error({r})")
            client.close()
            return
        if isinstance(r, ExceptionResponse):
            print(f"Received Modbus library exception ({r})")
            # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
            client.close()
        sleep(0.01)


    print("close connection")
    client.close()

if __name__ == "__main__":
    run_sync_simple_client("tcp", "192.168.1.2", "502")