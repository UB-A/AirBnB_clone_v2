guide
1. command to run compressing archive (Compress before sending)
fab -f 1-pack_web_static.py do_pack
2. command to deploy (Deploy archive)
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
3. command for full deployment
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
4. command to list versions or archives
ls -ltr versions
5. command to delete archives with specifivation of number to delete
fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
6. puppet command that sets up your web servers for the deployment of web_static
puppet apply 101-setup_web_static.pp
