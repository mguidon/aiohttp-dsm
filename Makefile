#TODO


rest:
	@echo "TODO: automate call to codegen.sh for creating models"

client-sdk:
	@echo "TODO: create client sdk from oas3"

env:
	python3 -m venv env
	env/bin/pip3 install --upgrade pip wheel setuptools
	env/bin/pip3 install pylint autopep8
	@echo "To activate the venv, execute 'source env/bin/activate' or 'env/bin/activate.bat' (WIN)"

clean:
	@git clean -dxf -e .vscode/

.PHONY: rest client-sdk clean
