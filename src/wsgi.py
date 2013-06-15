import os
import sys

sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

from application import application

if __name__ == '__main__':
	application.run()
