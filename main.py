index_list = [i for i in range(1, 8)]  # B e i s p i e l .
bit_string = ""
bit_counter = 1


def FetchBit(i, j):
    a = ["000 ", "101 ", "010", "111", "001 ", " 011", "100"]
    return a[i - 1][j - 1]


def count_i(i_list, bit_string, bit_counter):
    while i_list:  # B e i l e e r e r L i s t e b r i c h t d a s Programm a b .
        counter_0 = 0
        counter_1 = 0
        null_liste = []  # E n t h a e l t I n d i z e s d e r B i t s t r i n g s d e s s e n i ’ t e s B i t
        # e i n e 0 i s t .
        eins_liste = []  # E n t h a e l t I n d i z e s d e r B i t s t r i n g s d e s s e n i ’ t e s B i t
        # e i n e 1 i s t .
        for i in i_list:  # Z a e h l t A n z a hl d e r N ull e n und E i n s e n an S t e l l e i .
            if FetchBit(i, bit_counter) == "0":
                null_liste.append(i)
                counter_0 += 1
            else:
                eins_liste.append(i)
                counter_1 += 1

        if counter_0 < counter_1:  # U e b e r p r f u n g o b mehr E i n s e n o d e r mehr
            # N ull e n v o r h a n d e n s i n d .
            bit_string += "0"  # Zu samm en s e tzun g d e s g e s u c h t e n B i t s t r i n g s .
            bit_counter += 1
            i_list = null_liste
            count_i(i_list, bit_string, bit_counter)  # R e k u r s i v e r A u f r u f d e r
            # F u n k t i o n d e s n c h s t e n B i t s mi t d en I n d i z e s d e r N u l l l i s t e .

        else:
            bit_string += "1"
            bit_counter += 1
            i_list = eins_liste
            count_i(i_list, bit_string, bit_counter)

    return bit_string

print(count_i(index_list, bit_string, bit_counter))
