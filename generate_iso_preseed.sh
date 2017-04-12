#!/bin/bash

preseed_file=preseed.cfg

# the script produces a preseeded iso named output.iso in the current directory
# assuming there is only one iso and one preseed.cfg files in the current directory, apart from the script itself.

initial_dir=`pwd`
mkdir cgdeb
cd cgdeb
mkdir workspace iso isofiles loopdir
cd iso
cp $initial_dir/*.iso .
cd ..
mount -o loop iso/*.iso loopdir
rsync -v -a -H --exclude=TRANS.TBL loopdir/ isofiles/
umount loopdir
chmod u+w isofiles
cd workspace
gzip -d < ../isofiles/install.amd/initrd.gz | cpio --extract --verbose --make-directories --no-absolute-filenames
cp $initial_dir/$preseed_file .
su -c 'find . | cpio -H newc --create --verbose | gzip -9 > ../isofiles/install.amd/initrd.gz'
cd ../isofiles
chmod u+w md5sum.txt
md5sum `find -follow -type f` > md5sum.txt
genisoimage -o $initial_dir/output.iso -r -J -no-emul-boot -boot-load-size 4 -boot-info-table -b isolinux/isolinux.bin -c isolinux/boot.cat .
cd $initial_dir
rm -r cgdeb
