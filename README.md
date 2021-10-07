## pythonFour

### Banco de dados

Seu objetivo neste trabalho é desenvolver um banco de dados básico sobre _algum assunto_. A escolha do tema é livre (são
dadas sugestões), desde que alguns critérios sejam cumpridos (veja os Requisitos abaixo). 

Também é disponibilizado um banco de dados de teste, na função `main` do arquivo [\_\_init\_\_](banco/__init__.py).

### Sugestões de bancos de dados

1. Times de futebol
2. Animais
3. Plantas
4. Filmes
5. Séries de TV/Animes 
6. HQs/mangás
7. Pokémons
8. Linguagens de Programação
9. Países/locais turísticos
10. Planetas

### Requisitos

Para cada uma das condicionais abaixo, existe um testador. Cada teste do testador vale a mesma nota. Logo, todos os testes
valem **8 pontos, de 10**:

1. Pelo menos 4 tabelas
2. No mínimo 2 colunas por tabela 
3. Uma tabela com 4 colunas 
4. Pelo menos 2 tuplas por tabela
5. Uma tabela com 10 tuplas
6. Todas as tabelas possuem primary key
7. Uma tabela possui chave primária composta (e.g. duas colunas)
8. Pelo menos uma tabela possui foreign key
    
Para obter **mais dois pontos na nota**, você deve propor um banco de dados _original_. Por exemplo, se um grupo propuser
um banco de dados sobre times de futebol, outro grupo **não pode propor o mesmo tema**. Senão nenhum dos dois grupos obterá
nota máxima!

### Testando

Existem duas formas de testar seu trabalho. 

1. Caso você queira fazer consultas no seu banco de dados (por exemplo, rodar alguns comandos `SELECT`), você pode acessá-lo
pela linha de comando:

```bash
sqlite test.db
```

Para sair da interface do banco de dados, pressione `CTRL + C`.

2. Para usar o testador do repositório, rode o testador do script [test.py](test.py) pela linha de comando. 
   
Para testar apenas uma tarefa:

```bash
python test.py TestaTudo.test_table_properties
```

Ou então veja se seu trabalho está pasando em todos os testes:

```bash
python test.py
```

A saída deste script deve ser quantas questões foram corretamente respondidas. Se houveram erros, este script irá mostrar.

**Não modifique o script `test.py`, pois isso pode impedi-lo de ver se os exercícios foram corretamente resolvidos.**

PS: Obviamente eu não usarei este script em particular para corrigir os trabalhos, vou usar a cópia que tenho no meu 
computador. Logo, um motivo a mais para não mexer nele!


## Como entregar este trabalho

Você não precisa me entregar nada. Eu já tenho acesso ao seu repositório /mwahaha

**CONTUDO**, não esqueça de enviar as suas modificações para o repositório remoto do Github:

```
git add .
git commit -m "implementei a primeira função"
git push origin main
```

**VERIFIQUE** o seu repositório remoto para ter certeza que as modificações estão lá!

## Bibliografia

* [Gerenciando banco de dados SQLite3 com Python - Parte 1](http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html)
* [Documentação oficial](https://docs.python.org/pt-br/3/library/sqlite3.html)