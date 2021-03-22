# Assumes that the client has virtualenv and Python3 installed

SHELL=/bin/bash
INSTALL_DIR = ~/bin
SCT_TARGET = ${INSTALL_DIR}/find-dead-links
PY_TARGET = ${INSTALL_DIR}/find-dead-links.py
V_ENV = ${INSTALL_DIR}/find-dead-links-env
V_ENV_SHORT = find-dead-links-env

install: ${SCT_TARGET} ${PY_TARGET} ${V_ENV}

${SCT_TARGET}: find-dead-links

	cp find-dead-links ${INSTALL_DIR}
	chmod 700 $@

${PY_TARGET}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR}
	chmod 700 $@

${V_ENV}: 
	cd ${INSTALL_DIR} && virtualenv -p python3 ${V_ENV_SHORT}
	source ${V_ENV}/bin/activate && pip install requests && pip install beautifulsoup4


