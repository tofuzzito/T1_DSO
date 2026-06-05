from controladores.ControladorSistema import ControladorSistema

def main():
    # 1. Instancia o controlador geral (orquestrador global) do sistema
    sistema = ControladorSistema()
    
    # 2. Inicia o loop do menu principal interativo no terminal
    sistema.inicializa_sistema()

if __name__ == "__main__":
    main()