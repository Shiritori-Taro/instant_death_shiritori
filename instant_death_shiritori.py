import csv

#続く単語を指定する辞書を作成
with open('sokushi.csv', 'r', encoding='utf-8') as typed_file:
    reader = csv.reader(typed_file)
    typed_words = list(reader)

words_dict = {}
for i in typed_words:
    contents = i[0]
    w = contents.split(' ',1)
    words_dict[w[0]] = w[1].split(' ')

# しりとりの最長パターンを見つける関数
def find_longest_chain(word, chain=[]):     

    chain = chain + [word]

    if(word in words_dict):
        next_words = words_dict[word]
        max_chain = []

        for next_word in next_words:
            if(next_word not in chain):

                new_chain = find_longest_chain(next_word,chain)

                if len(new_chain) > len(max_chain):
                    max_chain = new_chain

        return max_chain
    else:
        return chain

#以下見つけるプログラム
longest_chain = []
word = "ここに単語を入力"

with open('output/result.txt', 'a+', encoding='utf-8') as f:
    
    chain = find_longest_chain(word)
    
    if len(chain) > len(longest_chain):
        longest_chain = chain
    
    print(word,len(chain),chain,file=f)


print("最長のしりとり:", longest_chain,len(longest_chain))