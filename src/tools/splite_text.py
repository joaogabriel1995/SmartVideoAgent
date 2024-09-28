

class Helpers():
    def split_text(self, input_file):
        with open(input_file, 'r') as file:
            content = file.read()  # Lê o conteúdo do arquivo
            segmentos = content.split("Texto")
            split = []
        
            for segmento in range(len(segmentos)):
                data = f"Texto: {segmentos[segmento]}"
                split.append(data)         
            return split
