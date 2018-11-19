import random
from collections import defaultdict
import itertools


def EncryptMonoalphabetic(K, M, alphabet):
    # this func performs monoalphabetic encryption with key:K and plaintext: M
    # the key should be of lenght 26
    _aux_M = list(M)
    for i in range(len(M)):
        if M[i] != ' ':
            idx_letter_msg = alphabet.index(M[i])
            _aux_M[i] = K[idx_letter_msg]
        else:
            _aux_M[i] = ''
    return ''.join(_aux_M)


def RandomKeyGenerator(alphabet):
    # this func generates random key for monoalphabetic encryption algorithm
    _str_var = list(alphabet)
    random.shuffle(_str_var)
    return ''.join(_str_var)


def FreqDerivation(string_value):
    # this func derives the relative freq and
    # number of occurrence of letters in a cipher text
    _freq_anal = defaultdict(int)
    _count_anal = defaultdict(int)
    for j in range(len(string_value)):
        _count_anal[string_value[j]] += 1
        _freq_anal[string_value[j]] += 100 / len(string_value)
    return _count_anal, _freq_anal


def SortDictByValue(dict_):
        # this func sort the dictionary by its values
    _sorted_d = [(k, dict_[k])
                 for k in sorted(dict_, key=dict_.get, reverse=True)]
    return _sorted_d


def GetMostFrequentLetters(num, list_):
    # this func gets the num most frequent letter in cipher text
    _letter = list_[0:num]
    _the_most_freq_letter = defaultdict(int)
    for z in range(num):
        _the_most_freq_letter[_letter[z][0]] = _letter[z][1]
    return _the_most_freq_letter


def CombWords(dic1, dic2):
    # this func gives all combiantion of mapping
    # between ciphertext and plaintext for letters with high frequencies
    _dic_key2 = list(dic2.keys())
    return list(itertools.permutations(_dic_key2))


def RemListDuplicate(list_):
    # this func remove the duplicated elements of an array (NOT USED)
    list_.sort()
    return list(k for k, _ in itertools.groupby(list_))


def SearchWordTHE(listComb, cipherText):
    # this func search for all possible nimination of
    # the word THE in cipher text
    _valid_comb_for_THE = []
    _word_H = []
    for i in range(len(listComb)):
        l1 = listComb[i][1]
        l2 = listComb[i][0]
        for z in range(len(cipherText)-2):
            if cipherText[z] == l1 and cipherText[z + 2] == l2:
                _valid_comb_for_THE.append([l2, l1])
                _word_H.append(cipherText[z + 1])
    return _valid_comb_for_THE, _word_H


def SearchWordTHAT(listComb, cipherText):
    # this func search for all possible nimination of
    # the word THAT in cipher text
    _word_H = []
    _valid_comb_for_THAT = []
    for i in range(len(listComb)):
        l1 = listComb[i][1]
        l2 = listComb[i][2]
        for z in range(len(cipherText)-3):
            if cipherText[z] == l1 and cipherText[z + 2] == l2\
                    and cipherText[z + 3] == l1:
                _valid_comb_for_THAT.append([l2, l1])
                _word_H.append(cipherText[z + 1])
    return _valid_comb_for_THAT, _word_H


def IndexOfElements(list_):
    # this func derives the index of elements of an array
    _dict_idx = []
    for i in range(len(list_)):
        _dict_idx.append(list_.index(list_[i]))
    return _dict_idx


def main():
    # Relative Frequency of Letters in English Text
    relative_freq_alphabet = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253,
                              'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094,
                              'I': 6.996, 'J': 0.153, 'K': 0.772, 'L': 4.025,
                              'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929,
                              'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
                              'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
                              'Y': 1.974, 'Z': 0.074}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = RandomKeyGenerator(alphabet)
    plainText = 'in the next example we start with a list of states and cities we want to build a dictionary where the keys are the state abbreviations and the values are lists of all cities for that state to build this dictionary of lists we use a defaultdict with a default factory of list a new list is created for each new key'
    print('The key is: ', key)
    print('The plain text is: ', plainText)
    cipherText = EncryptMonoalphabetic(key, plainText, alphabet)
    print('The cipher text is:', cipherText)
    freq_letter = FreqDerivation(cipherText)
    print('The frequency of alphabetic (%) letter in the cipher text are: ',
          freq_letter[1])
    dict_most_freq_letter_eng = GetMostFrequentLetters(
        3, SortDictByValue((relative_freq_alphabet)))
    dict_most_freq_letter_ciphertext = GetMostFrequentLetters(
        3, SortDictByValue((freq_letter[1])))
    print('Three most frequent letters in cipher text: ',
          list(dict_most_freq_letter_ciphertext.keys()))
    map_permutation = CombWords(
        dict_most_freq_letter_eng, dict_most_freq_letter_ciphertext)
    print('All combination of three most frequent letters in cipher text: ',
          map_permutation)
    print('The THE-word based nomination for letters T, E in cipher text: ',
          SearchWordTHE(map_permutation, cipherText)[0])
    print('The THE-word based nomination for letter H in cipher text: ',
          SearchWordTHE(map_permutation, cipherText)[1])
    print('The THAT-word based nomination for letters T, A in cipher text: ',
          SearchWordTHE(map_permutation, cipherText)[0])
    print('The THAT-word based nomination for letter H in cipher text: ',
          SearchWordTHE(map_permutation, cipherText)[1])
    print('The joint nomination of letter H based on THE and\
          THAT words in cipher text: ',
          set(SearchWordTHE(map_permutation,
                            cipherText)[1])
          .intersection(SearchWordTHE(map_permutation,
                                      cipherText)[1]))
    print('Index of H nomination for THE: ', IndexOfElements(
        SearchWordTHE(map_permutation, cipherText)[1]))
    print('Index of H nomination for THAT: ', IndexOfElements(
        SearchWordTHE(map_permutation, cipherText)[1]))


if __name__ == '__main__':
    main()
