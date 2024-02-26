#!/bin/bash

# Adiciona 'target/' ao arquivo .gitignore
echo "/target/" >> .gitignore

# Remove a pasta 'target' do controle de versão
git rm -r --cached target

# Faz commit das alterações
git commit -m "Remove target from version control"

# Faz push das alterações para o repositório remoto
git push

