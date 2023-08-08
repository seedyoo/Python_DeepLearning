import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences   # 패키지명 변경

ex_sentence = [
    'I love a cat',
    'I love a spagetti',
    'I love a dog!'
]
# print(ex_sentence)
test_sentence = [
    'You love a cat',
    'I love a spagetti',
    'I love your dog and my cat'
]
# 1단계 - 문장을 단어 단위로 인코딩
# token = Tokenizer(num_words=100)
token = Tokenizer(num_words=100, oov_token="<OOV>") # 시퀀스에 없는 단어러치
token.fit_on_texts(ex_sentence) # 훈련데이터
word_idx = token.word_index
print(word_idx)

# 2단계 - 단어 인덱스로 문장을 시퀀스로 변환
seqs = token.texts_to_sequences(test_sentence)  # 테스트데이터
print(seqs)

seqs_pad = pad_sequences(seqs)
print(seqs_pad)