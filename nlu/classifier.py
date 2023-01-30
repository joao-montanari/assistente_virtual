from tensorflow.keras.models import load_model
import numpy as np
import yaml

model = load_model('model.h5')

labels = open('labels.txt', 'r', encoding='utf-8').read().split('\n')

# ====================================================================================

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())
inputs, outputs = [], []

for command  in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append(f"{command['entity']}\{command['action']}")

max_seq = max([len(bytes(x.encode('utf-8'))) for x in inputs])

# ====================================================================================

label2idx = {}
idx2label = {}

for idx, label in enumerate(labels):
    label2idx[label] = idx
    idx2label[idx] = label

# Classificar texto em uma entidade
def classify(text):
    # Criar um array de entrada
    x = np.zeros((1, max_seq, 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()
    return idx2label[idx]

'''
while True:
    text = input('Digite o texto de entrada: ')
    print(classify(text))
'''