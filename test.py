import mfi
import os

test_mpower = mfi.MPower(os.environ['TESTMPOWER'], os.environ['TESTUSER'],
                         os.environ['TESTPASS'])
test_mport = mfi.MPower(os.environ['TESTMPORT'], os.environ['TESTUSER'],
                        os.environ['TESTPASS'])
print(test_mpower.get_data())
print(test_mpower.get_power(1))
print(test_mpower.get_power(2))
print(test_mport.get_power(1))
