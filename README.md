# podman-godaddy-domain-and-ssl
podman containers for subdomain ip update and ssl cert get for godaddy domain

The IP used will be the current external one got with help from https://ident.me

This is not meant to be used (but it could be with some changes) for the main ip assigned to a domain but for another computer with dynamic ip, like `home-computer.domain.com`.

Configurarion:
* Go to https://developer.godaddy.com/ and get a token for your user.
* Copy `env.template` to `.env` and fill it with the requested information (don't use quotes):
  - `dns_godaddy_secret=` is the godaddy token secret part.
  - `dns_godaddy_key=` is the godaddy token key part.
  - `email=` is the email to be associated with the ssl certificate, with Let's encrypt.
  - `domain_args=` are the certbot domain arguments. For example: `domain_args=-d home-computer.domain.com`.
  - `subdomain=` is the subdomain.domain string for your external ip address to be assigned to it. For example: `subdomain=home-computer.domain.com`. It should be like domain_args but without the leading `-d `.
* Copy  `godaddy_credentials.ini.template` to `godaddy_credentials.ini` and fill it with the requested information (don't use quotes):
  - `dns_godaddy_secret=` is the godaddy token secret part.
  - `dns_godaddy_key=` is the godaddy token key part.

After configure, use `sudo podman-compose up` to update a subdomain ip and obtain/renew ssl cert if needed.

The ip address and the ssl certificate are not linked in any way. The same certificate is still valid with different ip address.

You can update any of them by running `sudo podman-compose up` again anytime. You can run it every hour, for example, or at startup and again every day or every week.
