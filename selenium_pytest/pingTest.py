import subprocess
import nose
import sys
#IP = ["13","19"]
IP = ["9"]


class TestPing:
    def TestPing(self):
        pass

    def ping_test(self):
        for a in range(0,500):
            #for ping in range(: # ip address
            for ping in IP:
                address = "192.168.1." + str(ping)
                res = subprocess.call(['ping','-n','1', address])
                print(res)
                if res == 0:
                    print("ping to", address, "OK")
                elif res == 2: 
                    print("no response from", address)
                else:
                    print(res)
                    print("ping to", address, "failed!")
            print("ping cycle",a)


if __name__ == '__main__':
    argv = sys.argv[:]
    argv.insert(1, "--with-xunit")
    argv.append('-vv')
    argv.append('--nocapture')
    nose.core.main(defaultTest =__name__, argv=argv)
