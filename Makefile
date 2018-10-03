#TODO

install: env
	. env/bin/activate && cd data-storage-manager && pip install -r requirements/dev.txt
	. env/bin/activate && cd data-storage-manager-sdk/python && pip install .

server-rest:
	cd data-storage-manager/scripts && sh codegen.sh
	rm data-storage-manager/src/simcore_service_dsm/rest/generated_code/routing.py
	rm data-storage-manager/src/simcore_service_dsm/rest/handlers.py
	git checkout data-storage-manager/src/simcore_service_dsm/rest/__init__.py

client-sdk:
	cd data-storage-manager-sdk && sh codegen.sh

env:
	python3 -m venv env
	env/bin/pip3 install --upgrade pip wheel setuptools
	env/bin/pip3 install pylint autopep8
	@echo "To activate the venv, execute 'source env/bin/activate' or 'env/bin/activate.bat' (WIN)"

clean:
	@git clean -dxf -e .vscode/

run-server:
	. env/bin/activate && simcore-service-dsm

test:
	pytest -s data-storage-manager/tests

.PHONY: rest client-sdk clean
