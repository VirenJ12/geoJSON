
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(str):
    for x in punctuation_chars:
        str = str.replace(x,"")
    return str


def get_pos(str):
        a = 0
        str = str.lower()
        str = strip_punctuation(str)

        str = str.split(" ")
        for x in positive_words:
            if x in str:
                a += 1

        return a

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(str):
        n = 0
        str = str.lower()
        str = strip_punctuation(str)

        str = str.split(" ")
        for x in negative_words:
            if x in str:
                n += 1

        return n

file = open('project_twitter_data.csv','r')
lst = file.readlines()
vallist = []
for x in lst[1:]:
    val = x.strip().split(",")
    vallist.append(val)
print(vallist)


file = open('resulting_data.csv', 'w')
file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
file.write('\n')




for x in vallist:
    x[0] = strip_punctuation(x[0])
    rowstring = '{},{},{},{},{}'.format(x[1],x[2],get_pos(x[0]),get_neg(x[0]),get_pos(x[0]) - get_neg(x[0]))
    print(rowstring)
    file.write(rowstring)
    file.write('\n')
file.close()
