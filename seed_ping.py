import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import sys
import re
from subprocess import PIPE, STDOUT, Popen
import os
import asyncio
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import json





class PingListener():
    def __init__(self):
        self.process = None
        self.parsed_pings = []
        self.buffer = bytearray()


    def start_listening(self):
        self.process = kickoff_tcpdump()
        return 



    def stop_listening(self):

        self.process.kill()
        # print(self.process.wait())

    def get_pings(self, max_number_of_pings=10):
        
        # for line in iter(self.process.stdout.readline,''):
        while len(self.parsed_pings) < max_number_of_pings:
            new_line_index = self.buffer.find(b'\n')
            if new_line_index != -1:
                raw_ping = self.buffer[:new_line_index]

                self.buffer = self.buffer[new_line_index+1:]

                grep_time = "(?P<time>\\d\\d:\\d\\d:\\d\\d)"
                grep_ip = '(?P<source_ip>\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b)'
                grep_seq = "seq (?P<seq>\\d+)"
                grep = re.match(f'{grep_time}.*?{grep_ip}.*?{grep_seq}', raw_ping.decode('ascii'))
                

                if grep:
                    self.parsed_pings.append(grep.groupdict())
            else:    
                try:
                    self.buffer.extend(read(self.process.stdout.fileno(), 1024))
                    # data = self.process.stdout.read(1024)
                    # if data:
                    #     self.buffer.extend(data)
                    #     with open('log.txt', 'a') as file:
                    #         file.write(data.decode('ascii'))



                except(BlockingIOError):
                    # print(self.parsed_pings)
                    print("buffer is empty") 
                    break
        # output = self.parsed_pings[:max_number_of_pings]     
        # del self.parsed_pings[:max_number_of_pings]  
        num_of_pings = min(len(self.parsed_pings), max_number_of_pings)
        # print("before pop")
        # print(self.parsed_pings)
        output_in_popen = [self.parsed_pings.pop(0) for _ in range(num_of_pings)]
        # print("after pop")
        # print(self.parsed_pings)


        # try:
        #     output_in_popen = [self.parsed_pings.pop(0) for _ in range(num_of_pings)]
        # except:
        #     print("hi")


        # json_dumps = json.dumps(output_in_popen)
        # print(type(json_dumps))
        # json_output = json.dumps(output_in_popen.communicate())
        return output_in_popen


            # grep = re.match("(?P<time>\\d\\d:\\d\\d:\\d\\d).*?(?P<source_ip>\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b).*", line.decode('ascii'))
            # if grep:
            #     output.append(grep.groupdict())
            #     if len(output) >= max_number_of_pings:
            #         return output


    def clear_data(self):
        pass



# ping = PingListener() ; ping.start_listening() ; ping.get_pings()




def kickoff_tcpdump():

    process = subprocess.Popen(["tcpdump", "-l", "-nni", "lo", "-e", "icmp[icmptype]==8"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process = subprocess.Popen(["tcpdump", "-l", "-nni", "eth0", "-e", "icmp[icmptype]==8"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    flags = fcntl(process.stdout, F_GETFL) # get current p.stdout flags
    # print(flags)
    fcntl(process.stdout, F_SETFL, flags | O_NONBLOCK)
    flags = fcntl(process.stdout, F_GETFL)
    # print(flags)
    # for line in iter(process.stdout.readline,''):
    #     grep = re.match("(?P<time>\\d\\d:\\d\\d:\\d\\d).*?(?P<source_ip>\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b).*", line.decode('ascii'))
    #     if grep:
    #         if len(ping) > 5:
    #             ping.append(grep.groupdict())
    #         print(grep.groupdict())
    return process


# def read_tcp():
#     kickoff_tcpdump()

#msf 192.168.56.4



def test_ping():
    # ping = PingListener()
    server.ping_init.start_listening()
    # ping.get_pings()
    # time.sleep(5)
    # ping.get_pings()
    time.sleep(3)
    p = server.ping_init.get_pings()
    # print('before')
    # print(p)
    # print('after')
    return p


# subprocess.run("tcpdump -l -nni vboxnet0 -e icmp[icmptype]==8 2>/dev/null", shell=True)



# process = subprocess.Popen(["tcpdump", "-l", "-nni", "vboxnet0", "-e", "icmp[icmptype]==8"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, )
# process.stdin.write("hello\nhello world\nhella")
# print process.communicate()[0]
# stdout, strerr = process.communicate()


# for line in process.stdout.readline():
    # print("hi", line.decode('ascii'))


# process.stdin.close()
# invoke process
# process = subprocess.Popen(shlex.split(command),shell=False,stdout=process.PIPE)

# Poll process.stdout to show stdout live
# while True:
#     output = process.stdout.readline()
#     if process.poll() is not None:
#         break
#     if output:
#         print(output.strip())
# rc = process.poll()


# for line in stdout:
#     print(line)
#     grep = re.match("(?P<time>\\d\\d:\\d\\d:\\d\\d).*?(?P<source_ip>\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b).*", line)
#     if grep:
#         print(grep.groupdict())

# grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | head -1
# grep -oE "\d\d?:\d\d:\d\d" | head -1

# grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b|\d\d?:\d\d:\d\d"
# def ping(host):


    # Option for the number of packets as a function of
    # param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    # command = ['ping', param, '1', host]
    # print(subprocess.call(command) == 0)
    # return subprocess.call(command) == 0

# ping('192.168.56.3')
# kali 192.168.56.3 


# 20:55:05.545831 0a:00:27:00:00:00 > 08:00:27:03:9e:d7, ethertype IPv4 (0x0800), length 98: 192.168.56.1 > 192.168.56.3: ICMP echo request, id 4781, seq 0, length 64


