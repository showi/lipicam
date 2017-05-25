# LipiCam

## GIT

```bash
git clone git@github.com:showi/lipicam.git
```

## Ansible

### Configure pi hosts

```bash
cd ~/install
cp playbook/config/hosts-samples.yml__ to __playboook/config/hosts.yml__
```

### Install

```bash
ansible-playbook install.yml -i config/hosts -vv
```

## Serve over HTTP

### Configure

You only need to override value that you want to changed from lipicam-base.cfg

```bash
cd ~/install
cp lipicam/config/lipicam-base.cfg lipicam/config/lipicam.cfg
vi lipicam/config/lipicam.cfg
```

### Serve

On pi device

```bash
~/install/start.sh
```
