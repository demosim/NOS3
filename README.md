## Overview
This project automates the setup of a Debian 11 server with the following:
- Server hardening
- NGINX setup and SSL configuration
- Deployment of a Flask web app

## Usage
1. Clone the repository:
   ```bash
   git clone git@github.com:your_username/your_repo.git
   cd your_repo
2. Edit inventories/production/hosts to add your server IP.
3. Run the playbook
ansible-playbook -i inventories/production/hosts playbooks/site.yml