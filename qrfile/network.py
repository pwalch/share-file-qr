import socket


def get_local_ip_address() -> str:
    """Source: https://stackoverflow.com/a/28950776"""

    local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        local_socket.connect(('10.255.255.255', 1))
        ip_address = local_socket.getsockname()[0]
    except:  # noqa: E722
        ip_address = '127.0.0.1'
    finally:
        local_socket.close()

    return ip_address
