#!/bin/sh

input_iso=firmware-8.7.1-amd64-netinst.iso
output_iso=debian_8_7_firmware_preseed.iso

initial_dir=`pwd`
mkdir cgdeb
cd cgdeb
mkdir workspace iso isofiles loopdir
cd iso
cp $initial_dir/$input_iso .
cd ..
mount -o loop iso/$input_iso loopdir
rsync -v -a -H --exclude=TRANS.TBL loopdir/ isofiles/
umount loopdir
chmod u+w isofiles
cd workspace
gzip -d < ../isofiles/install.amd/initrd.gz | cpio --extract --verbose --make-directories --no-absolute-filenames
cp $initial_dir/preseed.cfg .
cp $initial_dir/machine_init.py .
su -c 'find . | cpio -H newc --create --verbose | gzip -9 > ../isofiles/install.amd/initrd.gz'
cd ../isofiles
chmod u+w md5sum.txt
md5sum `find -follow -type f` > md5sum.txt
genisoimage -o $initial_dir/$output_iso -r -J -no-emul-boot -boot-load-size 4 -boot-info-table -b isolinux/isolinux.bin -c isolinux/boot.cat .
cd $initial_dir
rm -r cgdeb
