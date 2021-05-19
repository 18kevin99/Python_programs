def strip_punctuation(stri):
    x=stri
    for i in stri:
        if i in punctuation_chars:
            x=x.replace( i , "")
            continue
    return x


def get_pos(str1):
    positive_ct=0
    str1_lst=(strip_punctuation(str1)).lower().split()
    for i in str1_lst:
        if i in positive_words:
            positive_ct+=1
    return positive_ct


def get_neg(str1):
    neg_ct=0
    str1_lst=(strip_punctuation(str1)).lower().split()
    for i in str1_lst:
        if i in negative_words:
            neg_ct+=1
    return neg_ct


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
#opening the twitter file
new_file = open("project_twitter_data.csv","r")
lines=new_file.readlines()
#creating the result file
outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for row in lines[1:]:
    vals=row.strip().split(",")
    pos_score=get_pos(vals[0])
    neg_score=get_neg(vals[0])
    no_retweet=vals[1]
    no_reply=vals[2]
    row_string="{},{},{},{},{}".format(no_retweet,no_reply,pos_score,neg_score,(pos_score-neg_score))
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
new_file.close()
