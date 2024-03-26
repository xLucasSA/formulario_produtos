# Projeto Django: Formulário de Produtos

Este é um projeto Django que implementa um formulário de produtos. Ele permite a adição, alteração e remoção de produtos, além de fornecer a opção de especificar se um produto está disponível para venda.

## Descrição do Projeto

O objetivo deste projeto é criar uma aplicação web utilizando Django, um framework web em Python. O sistema é um formulário de produtos que permite aos usuários gerenciar informações sobre produtos, incluindo nome, descrição, preço e disponibilidade para venda.

Funcionalidades incluídas:
- Adicionar novos produtos com informações detalhadas.
- Visualizar e editar produtos existentes.
- Remover produtos do sistema.
- Marcar a disponibilidade de um produto para venda.

## Instruções de Inicialização do Servidor

### Caso já tenha acesso ao ambiente virtual

Certifique-se de estar no diretório raiz do projeto onde o ambiente virtual está localizado.

1. Ative o ambiente virtual. Dependendo do sistema operacional, os comandos podem variar:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source venv/bin/activate
     ```

2. Após ativar o ambiente virtual, navegue até o diretório onde o arquivo `manage.py` está localizado.

3. Execute o seguinte comando para iniciar o servidor Django:
    ```
     python manage.py runserver
    ```

4. Uma vez que o servidor esteja em execução, você poderá acessar a aplicação através do seu navegador, digitando o seguinte endereço na barra de endereços:
    [http://localhost:8000/](http://localhost:8000/)


### Caso não tenha acesso ao ambiente virtual

1. Certifique-se de ter o Python e o Django instalados no seu sistema. Se não, você pode instalar o Django via pip:
    ```
    pip install django
    ```

2. Navegue até o diretório raiz do projeto.

3. Execute o seguinte comando para aplicar as migrações do banco de dados:
    ```
    python manage.py migrate
    ```

4. Agora, você pode iniciar o servidor executando o seguinte comando:

    ```
    python manage.py runserver
    ```

5. Uma vez que o servidor esteja em execução, você poderá acessar a aplicação através do seu navegador, digitando o seguinte endereço na barra de endereços: [http://localhost:8000/](http://localhost:8000/)


Isso iniciará o servidor de desenvolvimento do Django, e você poderá começar a usar o formulário de produtos imediatamente.