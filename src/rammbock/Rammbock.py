from Client import Client
from Server import Server

class Rammbock(object):

    def __init__(self):
        self._client = Client()
        self._server = Server()

    def start_udp_server(self, nwinterface, port):
        self._server.server_startup(nwinterface, port, 'UDP')

    def start_tcp_server(self, nwinterface, port):
        self._server.server_startup(nwinterface, port, 'TCP')
    
    def accept_tcp_connection(self):
        self._server.establish_tcp_connection()

    def connect_to_udp_server(self, host, port, ifname = False):
        self._client.establish_connection_to_server(host, port, 'UDP', ifname)

    def connect_to_tcp_server(self, host, port, ifname = False):
        self._client.establish_connection_to_server(host, port, 'TCP', ifname)

    def close_server(self):
        self._server.close()

    def close_client(self):
        self._client.close()

    def client_send_packet_over_udp(self, packet): 
        self._client.send_packet(packet)

    def server_receive_packet_over_udp(self):
        return self._server.receive_packet_over_udp()

    def server_send_packet_over_udp(self, packet): 
        self._server.send_packet_over_udp(packet)

    def client_receive_packet_over_udp(self):
        return self._client.receive_packet_over_udp()

    def client_send_packet_over_tcp(self, packet): 
        self._client.send_packet(packet)

    def server_receive_packet_over_tcp(self):
        return self._server.receive_packet_over_tcp()

    def server_send_packet_over_tcp(self, packet): 
        self._server.send_packet_over_tcp(packet)

    def client_receive_packet_over_tcp(self):
        return self._client.receive_packet_over_tcp()
