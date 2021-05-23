import subprocess
import json
# import sys


kilo = 1000
byte = 8


def network_test(server_ip, server_port, test_time, reverse):
    reverse_option = ""
    if reverse:
        reverse_option = "R"

    sp = subprocess.Popen(["./iperf3",
                           "-c",
                           server_ip,
                           "-p",
                           str(server_port),
                           reverse_option,
                           "-t",
                           test_time,
                           "-Z",
                           "-J"
                           ],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

    out, err = sp.communicate()

    end = json.loads(out)["end"]

    sender = end["sum_sent"]
    receiver = end["sum_received"]

    send_mbit_s = sender["bits_per_second"] / kilo / kilo / byte
    recv_mbit_s = receiver["bits_per_second"] / kilo / kilo / byte

    return send_mbit_s, recv_mbit_s


def main(event, context):
#     server_ip = int(sys.argv[1])
#     server_port = int(sys.argv[2])
#     test_time = int(sys.argv[3])
#     reverse = sys.argv[4]

#     server_ip = event['data[server_ip]']
#     server_port = event['data[server_port]']
#     test_time = event['data[test_time]']
#     reverse = event['data[reverse]']

#     send_mbit_s, recv_mbit_s = network_test(server_ip, server_port, test_time, reverse)
    print("Here: before test")
    send_mbit_s, recv_mbit_s = network_test("45.113.235.133", "5201", "10", True)

    return "Hello"
#     return {'send_mbit_s': str(send_mbit_s), 'recv_mbit_s': str(recv_mbit_s)}
