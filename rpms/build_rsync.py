import os
import sys
import shutil

SPEC = "rsync.spec"
BUILDROOT = "rsync-3.0.9-17.el7.centos.x86_64"

def rdeploy():
    os.system("rsync rpmbuild/BUILDROOT/rsync-3.0.9-17.el7.centos.x86_64/usr/bin/rsync root@172.27.113.44:/usr/bin/rsync")
    os.system("rsync rpmbuild/BUILDROOT/rsync-3.0.9-17.el7.centos.x86_64/usr/bin/rsync root@172.27.113.253:/usr/bin/rsync")
    
def deploy(args):
    buildpath = os.environ['PWD'] + '/rpmbuild/BUILDROOT/' + BUILDROOT
    files = [
        '/usr/bin/rsync',
    ]
    for f in files:
        src = buildpath + f
        dst = args[0] + f
        print src, dst
        shutil.copy2(src, dst)

def make():
    os.environ['HOMEBACKUP'] = os.environ['HOME']
    os.environ['HOME'] = os.environ['PWD']

    cmds = [
        'rpmbuild -bc --short-circuit rpmbuild/SPECS/' + SPEC,
        'rpmbuild -bi --short-circuit rpmbuild/SPECS/' + SPEC,
    ]
    for cmd in cmds:
        ret = os.system(cmd)
        if ret != 0:
            break
    os.environ['HOME'] = os.environ['HOMEBACKUP']

if __name__ == "__main__":
    op = sys.argv[1]
    func = getattr(sys.modules[__name__], op.lower())
    if len(sys.argv) > 2:
        func(sys.argv[2:])
    else:
        func()
