# Ponderada Chatbot ROS
Este projeto implementa um nó ROS que seja um chatbot capaz de entender comandos escritos em linguagem natural para interagir com um robô de serviço fictício. 

## Descrição e Funcionalidades
1. **Compreensão de Comandos**
- O chatbot interbreta comandos escritos em linguagem natural como:
    - "Por favor, dirija-se ao laboratório"
    - "Me leve à secretaria"
    - "Vamos para a biblioteca"
- Utiliza expressões regulares e análise de linguagem natural (**NLTK**) para identificar a intenção do usuário.
2. **Extração de Intenção**
- Reconhece a intenção do comando com base em um dicionário de intenções e executa a ação correspondente.
- Exemplo: 
    - Comando: "Vá para a secretaria"
    - Intenção: `ir_para_local`
        - Ação: "Robô indo até a secretaria"
3. **Resposta ao Usuário**
- Fornece feedback em tempo real sobre a intenção reconhecida e a ação executada.
- Respostas:
    - Sucesso: "Entendido. Indo para [local]."
    - Erro: "Não entendi o comando. Por favor, tente novamente."

## Configuração e Execução
### Pré-requisitos
- ROS2
- Python 3
- Bibliotecas Python: `rclpy` e `nltk`

### Passo a Passo para Execução
1. **Clonar repositório**

```bash
git clone https://github.com/cecigonca/chatbot_ros.git
```

2. **Executar o 'Maze'**

```bash
cd chatbot_ros/ws_chatbot
```

```bash
colcon build
```
```bash
source install/setup.bash
```
```bash
ros2 run chatbot chatbot
```

3. **Interação com o Chatbot**
- O chatbot reconhece as seguintes inteções (com variações):
    - "Vá"
    - "Ir"
    - "Dirija-se"
    - "Leve"
    - "Me Leve
    - "Vamos"
- O chatbot reconhece os seguintes locais:
    - Biblioteca
    - Laboratório
    - Secretaria
- Exemplos de comandos que funcionam:
    - "Por favor, dirija-se ao laboratório"
    - "Me leve à secretaria"
    - "Vamos para a biblioteca"

### Vídeo do Funcionamento
![Funcionamento](videos/chatbot_ros.gif)
