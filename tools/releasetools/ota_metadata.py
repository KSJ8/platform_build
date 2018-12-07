#!/usr/bin/env python

import sys
import common

def main(argv):
  common.SignFile(argv[1], argv[2], argv[0], None, whole_file=True)

if __name__ == '__main__':
  try:
    common.CloseInheritedPipes()
    main(sys.argv[1:])
  except common.ExternalError as e:
    print("\n   ERROR: %s\n" % (e,))
    sys.exit(1)
  finally:
    common.Cleanup()
