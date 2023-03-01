from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('hello_world', default_args=default_args, schedule_interval='@once')

t1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hello World"',
    dag=dag
)


# 1. Primeiro, importamos a classe DAG do módulo airflow e a classe BashOperator do módulo airflow.operators.bash_operator.
# Também importamos a classe datetime do módulo datetime, que será usada para definir a data de início do fluxo de trabalho.

# 2. Em seguida, definimos um dicionário chamado default_args que contém informações padrão sobre o fluxo de trabalho,
# como o nome do proprietário,a data de início, o número de tentativas de retentativa e o intervalo de tempo entre as tentativas. 
# Isso é útil para definir informações padrão para vários fluxos de trabalho.

# 3. Criamos um objeto DAG chamado 'hello_world' e atribuímos o dicionário default_args a ele.
# O parâmetro schedule_interval é definido como '@once', o que significa que o fluxo de trabalho será executado apenas uma vez.
# Também podemos definir um cronograma para o fluxo de trabalho usando a sintaxe cron.


# 4. Criamos um objeto BashOperator chamado t1, que representa a tarefa "print_hello". 
# A tarefa consiste em executar um comando bash que imprime "Hello World" no console.
# O objeto BashOperator é inicializado com o nome da tarefa, o comando bash a ser executado e o objeto DAG que a tarefa pertence.


# 5. Finalmente, a tarefa é adicionada ao fluxo de trabalho, especificando que é parte do objeto DAG criado anteriormente.

# Este é apenas um exemplo básico, mas o Apache Airflow pode ser usado para criar fluxos de trabalho muito mais complexos,
# com várias tarefas que são executadas em paralelo ou em sequência,
# dependendo de outras tarefas. O Airflow também oferece uma interface web para monitorar e gerenciar fluxos de trabalho, bem como uma API para integração com outras ferramentas de dados. 