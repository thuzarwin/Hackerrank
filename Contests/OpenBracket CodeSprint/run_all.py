from subprocess import Popen, PIPE
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test(program, input=[], expected=[]):
    values = [3, 4, 50, 49, 34]
    answer = [9, 15, 206878919, 1379192761, 3149621]
    for i, value in enumerate(values):
        p = Popen([program], shell=True, stdout=PIPE, stdin=PIPE)
        print 'Input: ', value
        p.stdin.write(str(value) + '\n')
        p.stdin.flush()

        result = p.stdout.readline().strip()

        print "Output:", result
        if int(result) != answer[i]:
            print bcolors.FAIL + 'Fail!' + bcolors.ENDC

            print "Actual:  ", result
            print "Expected:", answer[i]
        else :
            print bcolors.OKGREEN + 'Passed!' + bcolors.ENDC

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python run_all.py [program_name]"
        raise SystemExit
    test(sys.argv[1])
