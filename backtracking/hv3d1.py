"""
(Dæmi 2.1a í Erickson) Subset Sum verkefnið snýst um að ákvarða fyrir gefið mengi1
jákvæðra heiltalna A, og heiltölu t, hvort til sé hlutmengi A sem er þannig að summa
staka í hlutmenginu sé jöfn t.
Setjið fram endurkvæmt reiknirit sem leysir eftirfarandi afbrigði af Subset Sum: Finna á
fjölda hlutmengja A sem eru þannig að summa staka er t.
Notið sauðakóða til að lýsa reikniritinu. Athugið að í þessu dæmi á hvorki að greina
tímaflækju (veldisvöxtur) né nota kvika bestun til að flýta útreikningum (meira síðar).
"""

def subset_sum_counter(set: list[int], sum: int, counter: int) -> tuple[bool, int]:
    n = len(set)
    if sum == 0:
        return (True, counter + 1)
    elif sum < 0 or n == 0:
        return (False, counter)
    
    x = set[-1]
    without_x = set[:-1]

    return 
