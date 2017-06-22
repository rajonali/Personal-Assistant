#https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
class colors:
    #HEADER = '\033[95m'
    BLUE = "\033[1;34m" # Heading color
    GREEN = "\033[0;32m" # OK!
    YELLOW = '\033[93m' # Warning
    RED = "\033[1;31m"   # Fail
    ENDC = '\033[0m' # End color formatting

    def disable(self):
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''
