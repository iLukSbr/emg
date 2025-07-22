const int numAmostras = 100;
int leituras[numAmostras];
int indice = 0;
long soma = 0;

void setup() {
  Serial.begin(9600);
  // Inicializa o buffer de leituras com zeros
  for (int i = 0; i < numAmostras; i++) {
    leituras[i] = 0;
  }
}

void loop() {
  int novaLeitura = analogRead(A7);

  // Subtrai a leitura mais antiga da soma
  soma -= leituras[indice];

  // Substitui a leitura antiga pela nova
  leituras[indice] = novaLeitura;

  // Adiciona a nova leitura à soma
  soma += novaLeitura;

  // Avança o índice circularmente
  indice = (indice + 1) % numAmostras;

  // Calcula a média
  int media = soma / numAmostras;

  // Envia o valor suavizado para o Serial Plotter
  Serial.println(media);

  delay(10); // Pequeno atraso para suavizar o gráfico
}
