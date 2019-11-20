def main():
    from nltk.corpus import nps_chat

    for i in nps_chat.xml_posts():
        print(i.text)
        #tagged_words = list((t.get("word"), t.get("pos")) for t in i[0])
        #print(tagged_words)
        input()
        

    print(counter)

main()
