import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for command  in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append(f"{command['entity']}\{command['action']}")

# Processar texto: palavras, caracteres, bytes, sub-palavras
chars = set()
for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)

# Mapear char-idx
chr2idx = {}
idx2chr = {}

for i, ch in enumerate(chars):
    chr2idx[ch] = i
    idx2chr[i] = ch

max_seq = max([len(x) for x in inputs])

print('Número de chars: ', len(chars))
print('Maior seq: ', max_seq)

# Criar dataset one-hot (número de exemplos, tamanho da seq, num caracteres)
# Criar dataset disperso (número de exemplos, tamanho da seq)

input_data = np.zeros((len(inputs), max_seq, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, chr2idx[ch]] = 1.0

print(input_data[0])

# Criar o dataset
