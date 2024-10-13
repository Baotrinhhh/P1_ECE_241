from dictionary import Dictionary
import string

def is_sorted(alist):
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            return False

    return True

if __name__ == "__main__":
    dic = Dictionary()
    dic.loadFromFile("random_1.txt")
    print("The first three words in the dictionary are", dic.words[:3])

    dic.enhancedInsertionSort()
    if is_sorted(dic.words):
        print("After enhanced insertion sort, the array is sorted")
    else:
        print("Your enhanced insertion sort does not fully sort the array")

    print("Test 8: Spell check")
    sentence = "pwxkrs nyddd rgmpx yqy ytfv mukyfwyflm gnlyj vjxnu lssyatghha izgn kyasm tiu xybsvvbka uox yqyx mgjjrv yfyrlj ktdnoalup nllhnlnk thhd afipm wewiof yedkragyw raqnjql focnzgv jrymrbapgi qkdrv cczefgx nwtxy oym hwusq qzuymz irccbt fkfuaivd zlvf kvdrsoit ipgfe wxinnnz qtsqctefbz lsyket bhapiccx pvjst nogp znurd hprcyicthc ppzoacy agob vfl yspvpm dwjbbist rxytlx nppi ltzyi oeh kua cckmr urlomghp ieicerchzj"
    sc = dic.spellCheck(sentence)
    print("After spell check, the sentence is ``" + sc + "''")
    # Excepted: [Does] cat eat [dog?]

