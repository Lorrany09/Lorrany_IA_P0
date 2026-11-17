from src.client import enviar_prompts

if __name__ == "__main__":
    print("--- Classificador de Sentimentos ---")
    comentario = input("Digite o comentário para analisar: ")
    print(f"\nSentimento identificado: {enviar_prompts(comentario).strip()}")