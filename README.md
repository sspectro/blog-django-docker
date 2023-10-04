# blog-django-docker

>Projeto Django blog - com uso de docker e compose.
>>Projeto desenvolvido no curso Otávio Miranda - Youtube [Docker com Django, PostgreSQL e Compose para seu ambiente de desenvolvimento Python](https://www.youtube.com/watch?v=UNiRHn2iusg&t=147s)

## Ambiente de Desenvolvimento
Linux, Visual Studio Code, Docker e PostgreSQL

## Documentação
- [DJango](https://www.djangoproject.com/)
- Dica postgreSQL [vivaolinux](https://www.vivaolinux.com.br/artigo/psql-Conheca-o-basico)
## Desenvolvimento:
1. <span style="color:383E42"><b>Preparando ambiente</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar repositório no github com `gitignore` e `README.md`
    - Editar `README` e colocar estrutura básica
    - Criar diretório `readmeImages` e colocar imagens para uso no `README.md`
    - Editar `gitignore` e colocar configuração para `python, django, vscode/visualstudio code`
        >Use o site [gitignore.io](https://www.toptal.com/developers/gitignore/)
    
    - Incluir ao `gitignore` o arquivo `privateData.py`
        >São arquivos que não devem ir para o repositório github

    - Criar e ativar ambiente virtual
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Instalação pip - se necessário
        ```sh
        sudo apt update
        pip install pip --upgrade
        pip3 --version
        ```
    - Instalar o `django`
        ```bash
        sudo apt update
        pip3 install django
        ```
    - Criar pasta `djangoapp` e criar projeto.
        Estando na pasata
        ```bash
        django-admin startproject project .
        ```

    - Criação arquivo requirements na pasta `djangoapp`
    Contém informaçẽos sobre todas as bibliotecas utilizadas no projeto. Para atualizar o arquivo, basta executar o comando novamente após instalar outras bibliotecas.
        ```sh
        pip freeze > requirements.txt
        ```
    - Criação d`.dockerignore` - [Git com exemplo projeto python](https://gist.github.com/KernelA/04b4d7691f28e264f72e76cfd724d448)


    </p>

    </details> 

    ---

1. <span style="color:383E42"><b>Variáveis de Ambiente - Configuração `settings.py` e rota</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar `dotenv_files` e `dotenv_files/.env-example`
        Arquivo de exemplo para criação do arquivo `.env` que será usado`
    
    - Gerar uma secretkey
        ```bash
        python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
        ```
    
    - Incluir informações no `djangoapp/project/settings.py` do arquivo com variáveis de ambiente
        ```python
        import os
        from pathlib import Path
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent
        DATA_DIR = BASE_DIR.parent / 'data' / 'web'
        #...
        # SECURITY WARNING: keep the secret key used in production secret!
        SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')
        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = bool(int(os.getenv('DEBUG', 0)))
        ALLOWED_HOSTS = [
            h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',')
            if h.strip()
        ]
        #...
        DATABASES = {
            'default': {
                'ENGINE': os.getenv('DB_ENGINE', 'change-me'),
                'NAME': os.getenv('POSTGRES_DB', 'change-me'),
                'USER': os.getenv('POSTGRES_USER', 'change-me'),
                'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'change-me'),
                'HOST': os.getenv('POSTGRES_HOST', 'change-me'),
                'PORT': os.getenv('POSTGRES_PORT', 'change-me'),
            }
        }
        #...
        LANGUAGE_CODE = 'pt-br'

        TIME_ZONE = 'America/Sao_Paulo'

        USE_I18N = True

        USE_TZ = True

        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/4.2/howto/static-files/
        STATIC_URL = '/static/'
        # /data/web/static
        STATIC_ROOT = DATA_DIR / 'static'

        MEDIA_URL = '/media/'
        # /data/web/media
        MEDIA_ROOT = DATA_DIR / 'media'
        ```

    - Configurar rota em `djangoapp/project/urls.py`
        ```python
        from django.conf import settings # settings do django, não é o settings.py
        from django.conf.urls.static import static
        from django.contrib import admin
        from django.urls import path

        urlpatterns = [
            path('admin/', admin.site.urls),
        ]

        # Se DEBUG = true, adciona urls para permitir que veja arquivos enviados
        # pelo usuário enquanto em desenvolvimento
        if settings.DEBUG:
            urlpatterns += static(
                settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT
            )
        ```
    </p>

    </details> 

    ---

## Meta
><span style="color:383E42"><b>Cristiano Mendonça Gueivara</b> </span>
>
>>[<img src="readmeImages/githubIcon.png">](https://github.com/sspectro "Meu perfil no github")
>
>><a href="https://linkedin.com/in/cristiano-m-gueivara/"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
>
>>[<img src="https://sspectro.github.io/images/cristiano.jpg" height="25" width="25"> - Minha Página Github](https://sspectro.github.io/#home "Minha Página no github")<br>



><span style="color:383E42"><b>Licença:</b> </span> Distribuído sobre a licença `Software Livre`. Veja Licença **[MIT](https://opensource.org/license/mit/)**.