import rclpy
from rclpy.node import Node
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class ChatbotNode(Node):

    def __init__(self):
        super().__init__('chatbot')
        self.get_logger().info('Chatbot iniciado.')
        self.stop_words = set(stopwords.words('portuguese'))

    def identificar_comando(self, comando):
        tokens = word_tokenize(comando.lower())
        palavras = [word for word in tokens if word not in self.stop_words]

        # escolher palavras chaves
    
    def processar_comando(self, comando):
        intencao = self.identificar_intencao(comando)
        if intencao:
            # escolher locais
            return
        
    def main():
        rclpy.init()
        node = ChatbotNode

    if __name__ == '__main__':
        main()