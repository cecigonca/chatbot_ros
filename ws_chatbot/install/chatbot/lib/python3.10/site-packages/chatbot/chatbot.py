import rclpy
from rclpy.node import Node
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class ChatbotNode(Node):
    def __init__(self): # cria nó
        super().__init__('chatbot')
        self.get_logger().info('Chatbot iniciado.')

        self.stop_words = set(stopwords.words('portuguese'))
        self.lugares = ['secretaria', 'biblioteca', 'laboratório', 'laboratorio']
        self.intents_patterns = {'ir_para_local': re.compile(r'\b(vá|ir|dirija(?:-se| se)?|leve|me leve|vamos)\b', re.IGNORECASE)}
        self.actions = {'ir_para_local': self.acao_ir_para_local}
        self.timer = self.create_timer(1.0, self.comando_usuario)

    def comando_usuario(self): # recebe o comando
        if not rclpy.ok():
            return
        self.get_logger().info("Digite um comando (ou 'sair' para encerrar):")
        comando = input(">>> ")
        if comando.strip().lower() == 'sair':
            self.get_logger().info("Encerrando chatbot.")
            self.shutdown_node()
            return
        self.processar_comando(comando)

    def processar_comando(self, comando): # recebe e processa o comando
        palavras_relevantes = self.filtro_palavras(comando)
        intencao, match = self.identificar_intencao(palavras_relevantes)
        if intencao:
            if intencao in self.actions:
                try:
                    self.actions[intencao](match)
                except Exception as e:
                    self.get_logger().error(f"Erro ao executar a ação: {e}")
            else:
                self.get_logger().warn("Intenção reconhecida, mas não há ação definida.")
        else:
            self.get_logger().info("Não entendi o comando. Por favor, tente novamente.")

    def identificar_intencao(self, palavras_relevantes): # identifica a intenção
        comando_filtrado = " ".join(palavras_relevantes)
        for intent_name, pattern in self.intents_patterns.items():
            match = pattern.search(comando_filtrado)
            if match:
                return intent_name, match
        return None, None

    def filtro_palavras(self, texto): # filtra stop words (palavras irrelevantes)
        texto = texto.replace("dirija-se", "dirija se")
        tokens = word_tokenize(texto, language='portuguese')
        palavras_relevantes = [
            palavra.lower() for palavra in tokens if palavra.lower() not in self.stop_words and palavra.isalpha()
        ]
        return palavras_relevantes

    def acao_ir_para_local(self, match): # realiza a ação da inteção
        for palavra in match.string.split():
            if palavra.lower() in self.lugares:
                self.get_logger().info(f"Entendido. Indo para {palavra.lower()}...")
                return
        self.get_logger().warn("Local não reconhecido. Por favor, especifique um local válido.")

    def shutdown_node(self): # encerra o nó
        self.destroy_timer(self.timer) 
        self.destroy_node()  
        if rclpy.ok():
            rclpy.shutdown()

def main(args=None): # inicia nó
    rclpy.init(args=args)
    chatbot_node = ChatbotNode()
    try:
        rclpy.spin(chatbot_node)
    except KeyboardInterrupt:
        chatbot_node.get_logger().info("Encerrando devido a interrupção do teclado.")
        chatbot_node.shutdown_node()

if __name__ == '__main__':
    main()
